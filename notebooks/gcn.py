import torch
from torch.nn import Linear, ReLU
from torch_geometric.nn import GCNConv
from torch_geometric.nn import global_mean_pool

class DualGCN(torch.nn.Module):
    def __init__(self, node_features_protein, node_features_ligand, hidden_channels, output_channels):
        super(DualGCN, self).__init__()

        # GCN parts
        self.protein_gcn = GCNConv(node_features_protein, hidden_channels)
        self.ligand_gcn = GCNConv(node_features_ligand, hidden_channels)

        # Output layer
        self.out = Linear(2*hidden_channels, output_channels)

        # Activation
        self.relu = ReLU()

    def forward(self, protein_data, ligand_data):
        protein_x, protein_edge_index, protein_batch = protein_data.x, protein_data.edge_index, protein_data.batch
        ligand_x, ligand_edge_index, ligand_batch = ligand_data.x, ligand_data.edge_index, ligand_data.batch

        # Obtain node-level embeddings 
        protein_x = self.relu(self.protein_gcn(protein_x, protein_edge_index))
        ligand_x = self.relu(self.ligand_gcn(ligand_x, ligand_edge_index))

        # Use global_mean_pool to obtain graph-level embeddings
        protein_embed = global_mean_pool(protein_x, protein_batch) 
        ligand_embed = global_mean_pool(ligand_x, ligand_batch) 

        # Concatenate the embeddings (or you could use any other method to combine/embed them)
        embed = torch.cat([protein_embed, ligand_embed], dim=1)

        # Output layer
        out = self.out(embed)

        return out

def train(model, loader, optimizer, device):
    model.train()

    total_loss = 0
    for data in loader:
        data = data.to(device)
        optimizer.zero_grad()
        out = model(data.protein, data.ligand)
        loss = torch.nn.functional.mse_loss(out, data.y)
        loss.backward()
        total_loss += loss.item() * data.num_graphs
        optimizer.step()

    return total_loss / len(loader.dataset)

def test(model, loader, device):
    model.eval()

    total_loss = 0
    for data in loader:
        data = data.to(device)
        with torch.no_grad():
            out = model(data.protein, data.ligand)
        loss = torch.nn.functional.mse_loss(out, data.y)
        total_loss += loss.item() * data.num_graphs
    return total_loss / len(loader.dataset)


#instantiate model
node_features_protein = 1
node_features_ligand = 1

hidden_channels = 32
output_channels = 1

model = DualGCN(node_features_protein, 
                node_features_ligand, 
                hidden_channels, 
                output_channels)

#instantiate data loaders
train_loader, val_loader, test_loader = #!TODO
#train_loader, val_loader, test_loader = #!TODO

#train model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(1, 201):
    train_loss = train(model, train_loader, optimizer, device)
    val_loss = test(model, val_loader, device)
    print(f'Epoch: {epoch:03d}, Train Loss: {train_loss:.4f}, Val Loss: {val_loss:.4f}')

#test model
test_loss = test(model, test_loader, device)
print(f'Test Loss: {test_loss:.4f}')

#save model
torch.save(model.state_dict(), 'model.pt')

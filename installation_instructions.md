# Installation instructions

## Part 1: Install Anaconda

For this course you need a working installation of Python along with some required packages. This is made easy by the *Anaconda* distribution, which provides a current Python version bundled together with many popular packages for Data Science. Anaconda also provides you with the *conda* package manager, which you can use to install additional Python packages.

To install Anaconda, follow [this link](https://www.anaconda.com/products/individual) to download the installer and use default settings for everything.

On a Windows computer you should now have an installed program named *Anaconda Prompt*. On Mac you can just use the regular *Terminal* window. Next, type the following commands in the Anaconda Prompt / Terminal:

```shell
conda activate base

jupyter notebook
```

Now, the Jupyter application should open in your webbrowser. Next, switch to some random folder on the Jupyter interface and then click on `New`→`Python 3`.

Now, a Jupyter Notebook with a single code cell should open. Click into the code cell and enter the following code which will test if your installation works as intended:

```python
import seaborn as sns

print("Hello World")

sns.scatterplot(x=[1,2,3], y=[1,2,3])
```

Click on the `▶ Run` button. Your output should now look like this:

<div>
<img src="img/jupyter_test.png" width="700"/>
</div>

If it does, congratulations! You now have a working installation of Python with a lot of packages required for scientific computing. Now close the Anaconda Prompt / Terminal and your webbrowser to shutdown Jupyter. You can also delete the `.ipynb_checkpoints` folder which Jupyter automatically built in the folder in which you just created this Python file.

## Part 2: Install VS Code

To install VS Code (our IDE of choice), follow the instructions at [this link](https://code.visualstudio.com/docs/python/python-tutorial). You can skip the section *Install a Python Interpreter* since we have already installed Anaconda in part 1.

After installing and setting VS Code up, try to create a new notebook file called `test.ipynb`. Here you should be able to run the same test as above: You can copy the Python code from Part I into the single code cell that should be present in your new notebook and run it via the `Run` button. If you see the same output as in part 1, congrats! You are good to go for the course.

If something went wrong in the installation and you cannot figure it out, feel free to message Lukas or me on the course discord.

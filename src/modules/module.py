#example script running directly commands and defining a few functions to use

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


def calculate_mean(data):
    return data.mean()

def calculate_median(data):
    return np.median(data)

def lower_quartile(data):
    return np.quantile(data, 0.25)

def upper_quartile(data):
    return np.quantile(data, 0.75)

def shout(text):
    return text.upper() + "!"

def whisper(text):
    return text.lower() + "..."

if __name__ == "__main__":
    analysis_data = np.array([10, 43, 24, 65, 32, 12, 98, 54, 76, 87, 23, 45, 67, 89])

    print("Mean: ", calculate_mean(analysis_data))
    print("Median: ", calculate_median(analysis_data))
    print("Lower Quartile: ", lower_quartile(analysis_data))
    print("Upper Quartile: ", upper_quartile(analysis_data))
    print("Shout: ", shout("Hello World"))
    print("Whisper: ", whisper("Hello World"))  
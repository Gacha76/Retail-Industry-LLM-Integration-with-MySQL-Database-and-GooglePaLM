import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import re
import pandas as pd
from langchain_helper import get_few_shot_db_chain


def generate_matplotlib_plot(response):

    sizes = re.findall(r'(\w+):\s*(\d+)', response)
    x = [size[0] for size in sizes]
    y = [int(size[1]) for size in sizes]

    # Plot the data
    plt.bar(x, y)
    plt.xlabel('Sizes')
    plt.ylabel('Counts')
    plt.title('Size Distribution')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    return plt
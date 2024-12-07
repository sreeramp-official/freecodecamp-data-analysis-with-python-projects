import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("sea-level-predictor/epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(16, 5))
    plt.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit (1880-2050)
    first_slope, first_intercept, _, _, _ = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"]
    )
    first_x = range(1880, 2051)
    first_y = [first_slope * i + first_intercept for i in first_x]
    plt.plot(first_x, first_y, "g", label="Fit Line 1880-2050")

    # Create second line of best fit (2000-2050)
    df_recent = df[df["Year"] >= 2000]
    second_slope, second_intercept, _, _, _ = linregress(
        df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"]
    )
    second_x = range(2000, 2051)
    second_y = [second_slope * i + second_intercept for i in second_x]
    plt.plot(second_x, second_y, "r", label="Fit Line 2000-2050")

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()

    # Save plot and return data for testing
    plt.savefig("sea-level-predictor/sea_level_plot.png")
    return plt.gca()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical-data-visualizer/medical_examination.csv")

# Add 'overweight' column: Calculate BMI and determine if a person is overweight
df["overweight"] = (df["weight"] / ((df["height"] / 100) ** 2) > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad.
# If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df[["gluc", "cholesterol"]] = df[["gluc", "cholesterol"]].apply(
    lambda x: (x > 1).astype(int)
)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using pd.melt, focusing on 'cardio', 'active', 'alco', 'cholesterol', 'gluc', 'overweight', and 'smoke'
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"],
    )

    # Group by 'cardio', show counts of each feature, and plot the categorical plot
    fig = (
        sns.catplot(data=df_cat, kind="count", x="variable", hue="value", col="cardio")
        .set(ylabel="Total")
        .fig
    )

    # Save and return the figure
    fig.savefig("medical-data-visualizer/catplot.png")
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, fmt="0.1f", square=True)

    # Do not modify the next two lines
    fig.savefig("medical-data-visualizer/heatmap.png")
    return fig

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# loading the dataset and assigning column names
# dataset can be used for clustering and/or classification
# target variable is wheat_type = [Kama, Rosa, Canadian]
df = pd.read_csv("datatsets/seeds_dataset.txt", delim_whitespace=" ", header=None)
df.columns = ["area", "perimeter", "compactness", "kernel_length", "kernel_width", "asymmetry_coefficient",
              "kernel_groove_length", "wheat_type"]
# replacing numerical values with Actual name for the target variable Wheat
df["wheat_type"].replace({1: "Kama", 2: "Rosa", 3: "Canadian"}, inplace=True)

_columns = list(df.columns)
_columns.remove("wheat_type")


def scatter_plot_matrix():
    sns.set_theme(style="ticks")
    sns.set(rc={'figure.figsize': (11, 14)})
    sns.pairplot(df, hue="wheat_type")
    plt.title("Scatter Matrix")
    plt.show()


def hexbin_plot():
    plt.hexbin(x=df["area"], y=df["perimeter"])
    plt.show()


def kde_plot():
    for col in _columns:
        # reshaping the data where the columns are the different wheat types
        # and values are the data points of associated with the wheat types
        reshaped = df.pivot(columns="wheat_type", values=col)
        reshaped.plot.kde()
        plt.title(col)
        plt.show()


def strip_plot():
    for col in _columns:
        sns.stripplot(x=df[col], y=df["wheat_type"])
        plt.title(col)
        plt.show()


def swarm_plot():
    for col in _columns:
        sns.swarmplot(x=df["wheat_type"], y=df[col])
        plt.title(col)
        plt.show()


def box_plot():
    for col in _columns:
        sns.boxplot(x=df[col], y=df["wheat_type"])
        plt.title(col)
        plt.show()


def bar_plot():
    for col in _columns:
        sns.barplot(x=df["wheat_type"], y=df[col])
        plt.title(col)
        plt.show()


bar_plot()
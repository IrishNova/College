import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""Program generates an assortment of graphs (3 to be specific) using accompanying data. 
"""

def pie_gen(df):
    """Creates a pie chart
    df: DataFrame
    """
    big_three = df.loc[3:5]
    values = big_three['Value']
    labels = big_three['Name']
    title = "McDonald's Hamburger Facts"
    colors = ['orangered', 'goldenrod', 'sienna']
    plt.pie(values, labels=labels, explode=[.1, .1, .1], autopct='%2.1f%%', colors=colors, shadow=[3])
    plt.legend(values, loc="lower right", bbox_to_anchor=(.05, .05))
    plt.text(-1.8, -.55, 'Grams by Category', fontsize=8)
    plt.title(title)
    # plt.show()
    plt.savefig('Facts_one.png')
    plt.clf()


def bar_chart_one(df):
    """Creates macro bar chart
    df: DataFrame
    """
    macro = df.loc[:5]
    width = 0.4
    x_indexes = np.arange(len(macro['Name']))
    plt.bar(x_indexes - width, macro['Value'], color="blue", label="Burger", width=width)
    plt.bar(x_indexes, macro['Daily Value'], color='orange', label="Daily Intake", width=width)
    plt.xticks(x_indexes - width / 2, macro['Name'], fontsize=8)
    plt.ylabel("Grams")
    plt.title('Macro Nutrients: Burger vs. Daily Recommended Avg.')
    # plt.show()
    plt.savefig('macro_nutes.png')
    plt.clf()


def bar_chart_two(df):
    """Creates micro bar chart
    df: DataFrame
    """
    micro = df.loc[6:12]
    width = 0.4
    x_indexes = np.arange(len(micro['Name']))
    plt.bar(x_indexes - width, micro['Value'], color="blue", label="Burger", width=width)
    plt.bar(x_indexes, micro['Daily Value'], color='orange', label="Daily Intake", width=width)
    plt.xticks(x_indexes - width / 2, micro['Name'], fontsize=8)
    plt.ylabel("Grams")
    plt.title('Micro Nutrients: Burger vs. Daily Recommended Avg.')
    # plt.show()
    plt.savefig('micro_nutes.png')
    plt.clf()


def scatter(df2):
    """Creates scatter plot
    df2: DataFrame
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x=df2['Calories'], y=df2['Cost'])
    ax.set_xlabel("Calories")
    ax.set_ylabel("Cost")
    for i in range(len(df2)):
        name = df2['Name'].loc[i]
        plt.annotate(name, xy=(df2['Calories'].loc[i] + .05, df2['Cost'].loc[i] + .05), ha='center')
    ax.yaxis.set_major_formatter('${x:1.2f}')
    plt.title("Cost vs. Calories: McDonald's Menu Options")
    # plt.show()
    plt.savefig('wack-scatter.png')
    plt.clf()


if __name__ == '__main__':
    df = pd.read_csv('wack-arnlads burger data.csv')
    df2 = pd.read_csv('cost to cals.csv')
    pie_gen(df)
    bar_chart_one(df)
    bar_chart_two(df)
    scatter(df2)
    print("Finished Graphs for GD115N, Project #1")


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Import data
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Clean data
data_percentile_2_5 = df.quantile([0.025, 0.975])
df_clean = df[(df > data_percentile_2_5.loc[0.025]) & (df < data_percentile_2_5.loc[0.975])]

def draw_line_plot(df):
    """Draw a line chart with daily page views."""
    df_line_plot = df.copy()
    plt.figure(figsize=(12, 6))
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.plot(df_line_plot.index, df_line_plot.values)
    return plt

def draw_bar_plot(df):
    """Draw a bar chart with average daily page views by month and year."""
    df_bar_plot = df.copy().resample('M').mean()
    plt.figure(figsize=(12, 6))
    plt.title("Average Page Views by Month and Year")
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.bar(df_bar_plot.index.year, df_bar_plot.page_views, label=df_bar_plot.index.month_name())
    plt.legend(title="Months")
    return plt

def draw_box_plot(df):
    """Draw two adjacent box plots for year-wise and month-wise page views."""
    df_box_plot_year = df.copy().resample('A').median()
    df_box_plot_month = df.copy().resample('M').median()

    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    plt.title("Year-wise Box Plot (Trend)")
    sns.boxplot(x=df_box_plot_year.index, y=df_box_plot_year.page_views)
    plt.xlabel("Year")
    plt.ylabel("Page Views")

    plt.subplot(122)
    plt.title("Month-wise Box Plot (Seasonality)")
    sns.boxplot(x=df_box_plot_month.index.month_name(), y=df_box_plot_month.page_views, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.xlabel("Month")
    plt.ylabel("Page Views")

    plt.tight_layout()
    return plt

# Display and save plots
line_plot = draw_line_plot(df_clean)
line_plot.savefig('line_plot.png')

bar_plot = draw_bar_plot(df_clean)
bar_plot.savefig('bar_plot.png')

box_plot = draw_box_plot(df_clean)
box_plot.savefig('box_plot.png')

plt.show()

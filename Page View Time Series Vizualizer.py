import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df.index = df['date']
df = df.drop('date', axis=1)

# Clean data
lo_view = df['value'] > df['value'].quantile(0.025)
hi_view = df['value'] < df['value'].quantile(0.975)
df_new = df[lo_view & hi_view]
df = df_new.copy()
# print(int(df.count(numeric_only=True)))


def draw_line_plot():
    # Draw line plot
    fig, axes = plt.subplots(figsize=(22, 9))
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.plot(df.index, df['value'], color='crimson', lw=1.5)
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    fil = df.copy()
    fil.index = pd.to_datetime(fil.index)
    fil['day'] = fil.index.day
    fil['month'] = fil.index.month
    fil['year'] = fil.index.year
    look_up = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May',
               6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    fil['month'] = fil['month'].apply(lambda x: look_up[x])

    # Draw bar plot
    fig, axes = plt.subplots(figsize=(12, 10))
    df_bar = sns.barplot(x='year', y='value', data=fil, hue='month', hue_order=['January', 'February', 'March', 'April',
                         'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
                         palette='bright', ci=None)
    df_bar = df_bar.set(xlabel="Years", ylabel="Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    fil = df.copy()
    fil.index = pd.to_datetime(fil.index)
    fil['day'] = fil.index.day
    fil['month'] = fil.index.month
    fil['year'] = fil.index.year
    look_up = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May',
               6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    fil['month'] = fil['month'].apply(lambda x: look_up[x])
    fil = fil.rename(columns={'value': 'Page Views', 'year': 'Year', 'month': 'Month'})

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(21, 9))

    axes[0].set_title('Year-wise Box Plot (Trend)')
    sns.boxplot(x='Year', y='Page Views', data=fil, palette='bright', ax=axes[0])

    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    sns.boxplot(x='Month', y='Page Views', data=fil, order=['Jan', 'Feb', 'Mar', 'Apr',
                                                            'May', 'Jun', 'Jul', 'Aug', 'Sep',
                                                            'Oct', 'Nov', 'Dec'], ax=axes[1])

    plt.tight_layout(pad=2)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

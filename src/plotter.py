import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import STL



class Plotter:
    """
    Reusable Plotter module for common visualizations.
    Supports: histogram, bar chart, line plot, scatter plot, box plot, heatmap.
    """

    def __init__(self, style="white"): 
        # "white" or "ticks" removes the background grid
        sns.set_style(style)
        # This increases the resolution for all plots in the session
        plt.rcParams['figure.dpi'] = 150 
        plt.rcParams['savefig.dpi'] = 300

    
    def line_plot(self, data, x, y, title=None, xlabel=None, ylabel=None, vlines=None):
        plt.figure(figsize=(12, 6))
        
        sns.lineplot(x=x, y=y, data=data)
        
        plt.title(title or f"Line Plot of {y} over {x}", fontsize=14)
        plt.xlabel(xlabel or x, fontsize=12)
        plt.ylabel(ylabel or y, fontsize=12)
        
        # Add vertical lines if provided
        if vlines:
            for line in vlines:
                plt.axvline(pd.Timestamp(line['date']), color=line.get('color','red'),
                            linestyle=line.get('linestyle','--'),
                            label=line.get('label'))
        
        sns.despine()
        plt.grid(False)
        plt.show()


    def box_plot(self, data, y, title=None, ylabel=None):
        """
        Draws a boxplot to identify outliers and price distribution.
        """
        plt.figure(figsize=(5, 3))
        
        # Creating the boxplot
        # flierprops highlights the outliers (the 'dots')
        sns.boxplot(y=y, data=data, color="#2f7fc5", 
                    flierprops={"marker": "o", "markerfacecolor": "red", "markersize": 3})
        
        plt.title(title or f"Box Plot of {y} to Detect Outliers", fontsize=6)
        plt.ylabel(ylabel or y, fontsize=2)
        
        sns.despine()
        plt.grid(False)
        plt.show()

    
    def decomposition_plot(self, data, value_col, model='additive', period=365):
        """
        Decomposes time series into Trend, Seasonal, and Residual components.
        Requires 'data' to have a DatetimeIndex.
        """
        # 1. Ensure the index is datetime
        if not isinstance(data.index, pd.DatetimeIndex):
            raise ValueError("Dataframe index must be a DatetimeIndex. Run df.set_index('Date') first.")

        # 2. Perform decomposition
        series = data[value_col].dropna()

        # 3. STL decomposition (EXPLICIT period)
        stl = STL(
            series,
            period=period,   # <-- THIS FIXES THE ERROR
            seasonal=13      # odd number, smoothing window
        )

        result = stl.fit()

        # 4. Plot
        plt.figure(figsize=(12, 12))

        plt.subplot(411)
        plt.plot(series, color='blue', label='Original Time Series')
        plt.legend(loc='upper left')

        plt.subplot(412)
        plt.plot(result.trend, color='green', label='Trend Component')
        plt.legend(loc='upper left')

        plt.subplot(413)
        plt.plot(result.seasonal, color='orange', label='Seasonal Component')
        plt.legend(loc='upper right')

        plt.subplot(414)
        plt.plot(result.resid, color='red', label='Residual Component')
        plt.legend(loc='upper right')

        plt.tight_layout()
        plt.show()
    

    def histogram_plot(self, data, bins=30, title=None, xlabel=None, ylabel=None, color='blue'):
        """
        Plots a histogram of numeric data.

        Parameters:
        - data: array-like or pandas Series of numeric values
        - bins: number of histogram bins
        - title: plot title
        - xlabel: label for x-axis
        - ylabel: label for y-axis
        - color: color of the bars
        """
        plt.figure(figsize=(8, 5))
        plt.hist(data, bins=bins, color=color, edgecolor='black')
        
        plt.title(title or "Histogram", fontsize=14)
        plt.xlabel(xlabel or "Value", fontsize=12)
        plt.ylabel(ylabel or "Frequency", fontsize=12)
        
        sns.despine()
        plt.grid(False)
        plt.show() 

                
           

    
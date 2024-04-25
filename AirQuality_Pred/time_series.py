# time_series.py

import matplotlib.pyplot as plt

def df_time_plotter(df_list, time_unit, y_col):
    months = ['January','February','March', 'April', 'May','June', 
              'July', 'August', 'September', 'October', 'November', 'December']
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    if time_unit == 'M':
        nRows = 3
        nCols = 4
        n_iter = len(months)
    elif time_unit == 'D':
        nRows = 2
        nCols = 4
        n_iter = len(days)
    elif time_unit == 'H':
        nRows = 4
        nCols = 6
        n_iter = 24
    else:
        print('time_unit must be a string equal to M,D, or H')
        return
        
    fig, axs = plt.subplots(nrows=nRows, ncols=nCols, figsize=(40, 30))
    axs = axs.ravel()
    for i in range(n_iter):
        data = df_list[i]
        ax = axs[i]
        data.plot(kind='scatter', x='DateTime', y=y_col, ax=ax, fontsize=24)
        ax.set_ylabel('Pollutant Concentration', fontsize=30)
        ax.set_xlabel('')
        if time_unit == 'M':
            ax.set_title(y_col + ' ' + months[i], size=40)
        elif time_unit == 'D':
            ax.set_title(y_col + ' ' + days[i], size=40)
        else:
            ax.set_title(y_col + ' ' + str(i), size=40)
        ax.tick_params(labelrotation=60)
    
    # Set the spacing between subplots
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.5)
    plt.show()

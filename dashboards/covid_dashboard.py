#Base libraries
from datetime import datetime
import numpy as np
import pandas as pd
import random

#Bokeh Libraries
from bokeh.layouts import gridplot
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, DataRange1d, Select
from bokeh.palettes import Blues4
from bokeh.plotting import figure, show


class Dashboard:
    def __init__(self,title,df) :
        self._title=title
        self._df=df
        self._source=ColumnDataSource()
    
    
    def _datetime(self,x):
        return np.array(x, dtype=np.datetime64)

    def _extract_selections(self):
        ''' Extracts selections like countries for selection fields in dashboard     
        '''
        dashboard_selections={}
        df=self._df
        countries=sorted(df.location.unique())
        self._country_select = Select(title="Country:", value="Argentina", options=countries)
        self._country_select.on_change('value',self.update_plot)
        dashboard_selections['country']=self._country_select
        return dashboard_selections
    
    def make_plot(self,country):
        plot = figure(x_axis_type="datetime", title=self._title)
        plot.grid.grid_line_alpha=0.3
        plot.xaxis.axis_label = 'Date'
        plot.yaxis.axis_label = 'Total Cases per million'
        
        #Controls
        dashboard_selections=self._extract_selections()
        selection_controls=column(dashboard_selections['country'])
        #df=self._df
        #df.set_index(df['location'],inplace=True)
        #data=df.loc['Argentina'][['date','total_cases_per_million']]
        self._source.data=self.filter_data("Argentina")
        self._source.data['date']=self._datetime(self._source.data['date'])
        plot.line(x="date",y="total_cases_per_million",color='#FF11AA',legend_label=self._title,source=self._source)
        return column([selection_controls,plot])
    
    def filter_data(self,country):
        df=self._df
        df.set_index(df['location'],inplace=True)
        data=df.loc[country][['date','total_cases_per_million']]
        data=data.dropna()
        return data


    def update_plot(self,attrname, old, new):
        country = self._country_select.value
        data=self.filter_data(country)
        data['date']=self._datetime(data['date'])
        #src = get_dataset(df, cities[city]['airport'], distribution_select.value)
        self._source.data.update(data)


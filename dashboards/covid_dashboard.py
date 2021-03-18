#Base libraries
import numpy as np
import logging

#Bokeh Libraries
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure


class Dashboard:
    def __init__(self,title,df) :
        self._title=title
        self._df=df
        self._source=ColumnDataSource()
        self._country_select=Select(title="Country:", value="Argentina")
        # Logging configurations
        # create logger
        self._logger = logging.getLogger('Dashboard')
        self._logger.setLevel(logging.INFO)
 
 
    
    
    def _datetime(self,x):
        return np.array(x, dtype=np.datetime64)

    def _extract_selections(self):
        ''' Extracts selections like countries for selection fields in dashboard     
        '''
        dashboard_selections={}
        df=self._df
        countries=sorted(df.location.unique())
        self._country_select.options=countries
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
        self._source.data=self.filter_data(country)
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
        self._logger.info(f"Updating dashboard data to {new}")
        country = new
        data=self.filter_data(country)
        data['date']=self._datetime(data['date'])
        self._source.data.update(data)


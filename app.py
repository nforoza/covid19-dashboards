import pandas as pd
import logging
import configparser
from bokeh.server.server import Server
from dashboards.covid_dashboard import Dashboard

# Logging configurations
# create logger
logger = logging.getLogger('App')
logger.setLevel(logging.INFO)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)

#App config
config = configparser.ConfigParser()
config.read('config.ini')
COVID_URL=str(config['DEFAULT']['COVID_URL'])
logger.info(f"Dataset URL {COVID_URL}")
PORT=int(config['DEFAULT']['PORT'])
logger.info(f"PORT {PORT}")
TITLE='Covid 19 Dashboard'
COLUMNS=['location','date','total_cases_per_million']    

def update_last_data(url,columns):
    logger.info(f"Updating dataset from:{url}")
    df=pd.read_csv(url)
    data=df[columns].copy()
    return data
covid_data=update_last_data(COVID_URL,COLUMNS)
def render_doc(doc):
    data=covid_data.copy()
    dashboard=Dashboard(TITLE,data)
    plot=dashboard.make_plot("Argentina") #Defaulting to Argentina as first data 
    doc.add_root(plot)
    return
server = Server({'/': render_doc},port=PORT,allow_websocket_origin=["*"]) 
server.start()

if __name__ == '__main__':
    logger.info(f"Opening Bokeh application on http://localhost:{PORT}")
    server.io_loop.add_callback(server.show, "/")
    server.io_loop.start()
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

def render_doc(doc):
    doc.add_root(plot)
    return

if __name__ == '__main__':
    logger.info(f"Updating dataset from:{COVID_URL}")
    df=pd.read_csv(COVID_URL)
    COLUMNS=['location','date','total_cases_per_million']
    data=df[COLUMNS]
    TITLE='Covid 19 Dashboard'
    dashboard=Dashboard(TITLE,data)
    plot=dashboard.make_plot("Argentina") #Defaulting to Argentina as first data 
    server = Server({'/': render_doc},port=PORT)
    logger.info(f"Opening Bokeh application on http://localhost:{PORT}")
    server.io_loop.add_callback(server.show, "/")
    server.io_loop.start()
import urllib
import urllib.error as urlerrors
import pandas as pd
from bokeh.server.server import Server
from dashboards.covid_dashboard import Dashboard

COVID_URL="https://github.com/owid/covid-19-data/raw/master/public/data/owid-covid-data.csv"
DESTINY_FOLDER="./owid-covid-data.csv"
COLUMNS=['location','date','total_cases_per_million']
TITLE='Covid 19 Dashboard'

def render_doc(doc):
    doc.add_root(plot)
    return

def get_dataset(url,destiny,columns):
    '''Retrieves dataset from url a stores it in destiny folder
    Parameters:
    url (string): URL to retrieve csv
    Returns:
    Pandas Dataframe:Returning value
    '''
    try:
        urllib.request.urlretrieve(url,destiny)
        return pd.read_csv(destiny)[columns]
    except urlerrors.HTTPError as e:
        print("HTTP error, probably the url is not available:",e)

print("Refreshing Data")
data=get_dataset(COVID_URL,DESTINY_FOLDER,COLUMNS)

dashboard=Dashboard(TITLE,data)
plot=dashboard.make_plot("Argentina")

server = Server({'/': render_doc},port=8080)

# start timers and services and immediately return
server.start()

if __name__ == '__main__':
    print('Opening Bokeh application on http://localhost:8080/')
    server.io_loop.add_callback(server.show, "/")
    server.io_loop.start()
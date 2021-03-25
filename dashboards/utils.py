import urllib
import urllib.error as urlerrors
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
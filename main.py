import os # samskipti við stýrikerfið
import tarfile # meðhöndlun tar skráa
from six.moves import urllib # samskipti við internetið


#Fall sem nær í gögnin
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "datasets/housing"
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "/housing.tgz"

def fetch_housing_data(housing_url = HOUSING_URL, housing_path = HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path,"housing.tgz")
    
    urllib.request.urlretrieve(housing_url,tgz_path) 
    #niðurhleð tgz skrá frá housing_url
    housing_tgz = tarfile.open(tgz_path) # opna tgz skrá
    
    housing_tgz.extractall(path=housing_path) # extrakta skrár
    housing_tgz.close()


# ## Fall sem hleður inn gögnunum í Pandas

import pandas as pd

def load_housing_data(housing_path = HOUSING_PATH):
    csv_path = os.path.join(housing_path,"housing.csv")
    return pd.read_csv(csv_path) # innflutningur í gegnum 
# býr til "dataframe" sjálfkrafa

fetch_housing_data() # næ í gögna
housing = load_housing_data() # hleð þeim inn í Pandas

housing.info() # Tilvikatalning
housing.describe() # tölfræðilegar upplýsingar

housing["ocean_proximity"].value_counts() #talning gilda


import matplotlib.pyplot as plt
housing.hist(bins=10,figsize=(20,15))
plt.show()



import requests
import pandas as pd
import numpy as np
import io
from sqlalchemy import create_engine 

def data_scraping():
    covid_time_series = 'paste the URL'
    countries_aggr = 'paste the URL'
    world_aggr = 'paste the URL'
    # data = requests.get(url, allow_redirects=True)
    data1 = requests.get(covid_time_series, allow_redirects=True).content
    data2 = requests.get(countries_aggr, allow_redirects=True).content
    data3 = requests.get(world_aggr, allow_redirects=True).content
    ts = pd.read_csv(io.StringIO(data1.decode('utf-8')))
    ts = ts.rename(columns={'Date':'date','Country/Region':'Country','Province/State':'Province'})
    ts = ts.rename_axis('index_ts')
    countries_aggr = pd.read_csv(io.StringIO(data2.decode('utf-8')))
    countries_aggr = countries_aggr.rename(columns={'Date':'date'})
    countries_aggr = countries_aggr.rename_axis('index_ts')
    world_aggr = pd.read_csv(io.StringIO(data3.decode('utf-8')))
    world_aggr = world_aggr.rename(columns={'Date':'date','Increase rate':'Increase_rate'})
    world_aggr = world_aggr.rename_axis('index_ts')
    return ts, countries_aggr, world_aggr

# ts_df, countries_aggr_df, world_aggr_df = data_collection()
# print(ts_df.head())

def data_to_SQL(dataset, table_name):
    engine = create_engine('mysql+pymysql://root:pwd@localhost/covid', echo=False)
    conn = engine.connect()
    dataset.to_sql(table_name, conn, if_exists='replace')
    conn.close()

def main():
    print('Data Collection in progess...')
    ts_df, countries_aggr_df, world_aggr_df = data_scraping()
    print('Data Collection Complete')
    if ts_df.empty or countries_aggr_df.empty or world_aggr_df.empty:
        print('Dataframe is empty!')
    else:    
        data_to_SQL(ts_df, 'time_series_data')
        data_to_SQL(countries_aggr_df, 'countries_data')
        data_to_SQL(world_aggr_df, 'world_data')

if __name__ == '__main__':
    main()


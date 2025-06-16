import utility
import requests
import pandas as pd
from keybert import KeyBERT
    
global df
news_Source = ['www.businesstoday.in','www.thehindu.com']

def data_extractor(arguments): # working
    
    baseUrl = utility.base_url()
    
    response = requests.get(url=baseUrl, params=arguments)
    response = response.json()

    articles = utility.data_transformer(response['data'])
    df = pd.DataFrame(articles).sort_values(by="published_at", ascending=False)
    df['domain_address'] = df['url'].apply(utility.url_to_domain)
    utility.source_domain_fn(df,news_Source)
    # print(df.columns)
    return df

# chat bot implemetation
def data_extended(df):
    utility.source_domain_fn(df,news_Source) # extraction of main content



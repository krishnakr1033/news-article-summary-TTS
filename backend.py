import utility
import requests
import pandas as pd
from keybert import KeyBERT
    
global df
news_Source = ['www.businesstoday.in','www.thehindu.com']

def data_extractor(arguments): # working
    baseUrl = utility.base_url()
    response = requests.get(url=baseUrl, params=arguments)
    response=response.json()
    articles = utility.data_transformer(response['data'])
    df = pd.DataFrame(articles).sort_values(by="published_at", ascending=False).reset_index(drop=True)
    df['domain_address'] = df['url'].apply(utility.url_to_domain)
    return df

# def display_basic(): #working
#     # return the json format of all the basic details from df
#     # topic, description, org_link, date, src, category
#     # df.columns = ['title', 'description', 'url', 'category', 'language', 'published_at','domain_address']
#     return df.to_json()

# def dispay_extended():
#     pass

#     utility.source_domain_fn(df,news_Source)
#     df_extended = df.dropna(subset=['main_context'], inplace=False)

# chat bot implemetation
def data_extended(df):
    utility.source_domain_fn(df,news_Source) # extraction of main content

def keywords_extractor(main_contextt):
    kw_model = KeyBERT(model='all-MiniLM-L6-v2')
    keywords = kw_model.extract_keywords(main_contextt, top_n=5)
    words=[]
    for item in keywords:
        words.append(item[0])
    return words



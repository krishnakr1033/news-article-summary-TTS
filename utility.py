import copy
from dotenv import load_dotenv 
from datetime import datetime
import os
from urllib.parse import urlparse
from scrapper import *


def user_input(params): 
    # Filter out empty values and deep copy
    arguments = {
        k: copy.deepcopy(v)
        for k, v in params.items()
        if v not in (None, '', [], {}, ())
    }

    # Conditionally join 'languages' and 'countries' if they exist
    if 'languages' in arguments:
        arguments['languages'] = ",".join(arguments['languages'])

    if 'countries' in arguments:
        arguments['countries'] = ",".join(arguments['countries'])

    print(arguments)
    return arguments


def base_url():
    BaseUrl = "http://api.mediastack.com/v1/news"
    load_dotenv()
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    link = BaseUrl+f"?access_key={NEWS_API_KEY}"

    return link

def data_transformer(data):
    articles = []
    for item in data:
        article = {
            "title": item.get("title"),
            "description": item.get("description"),
            "url": item.get("url"),
            "category": item.get("category"),
            "language": item.get("language"),
            "published_at": datetime.fromisoformat(item.get("published_at")).date() if item.get("published_at") else None,
        }
        articles.append(article)
    return articles

def url_to_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

def source_domain_fn(df,sources_domain : list):
    for source_domain in sources_domain:
        if source_domain=='www.businesstoday.in':
            bussinesstoday_scrapping(df, source_domain)
        elif source_domain=='www.thehindu.com':
            thehindu_scrapping(df, source_domain)

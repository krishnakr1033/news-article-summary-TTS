from packages import *

def thehindu_scrapping(df,source_domain):
     for index, row in df.iterrows():
        if row['domain_address'] == source_domain:
            try:
                response = requests.get(row['url'])
                soup = bs(response.content, 'html.parser')
                # Extract the main content of the article
                content = soup.find('div', attrs={"itemprop": "articleBody"})
                content = content.find_all('p')
                content = [p for p in content if not p.attrs] 
                if content:
                    # Get the text and clean it up
                    text = ' '.join([p.get_text() for p in content])
                    df.at[index, 'main_context'] = html.unescape(text)
            except Exception as e:
                print(f"Error processing {row['url']}: {e}")


def bussinesstoday_scrapping(df, source_domain):
    # traverse to each link with corresponding domain
    for index, row in df.iterrows():
        if row['domain_address'] == source_domain:
            try:
                response = requests.get(row['url'])
                soup = bs(response.content, 'html.parser')
                # Extract the main content of the article
                content =  soup.find('div', class_='story_witha_main_sec')
                content = content.find_all('p')
                if content:
                    # Get the text and clean it up
                    text = ' '.join([p.get_text() for p in content])
                    df.at[index, 'main_context'] = html.unescape(text)
            except Exception as e:
                print(f"Error processing {row['url']}: {e}")

def source_domain_fn(df,sources_domain : list):
    for source_domain in sources_domain:
        if source_domain=='www.businesstoday.in':
            bussinesstoday_scrapping(df, source_domain)
        elif source_domain=='www.thehindu.com':
            thehindu_scrapping(df, source_domain)


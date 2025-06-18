# News-article-summary-with-ai-assistant

This project implements an intelligent news article assistant that dynamically adjusts to user preferences through a chat-based interface. It fetches the articles as per the user requirement from MediaStack API , upon each articles it shows their basic informations along with the summarized content, keywords, and integrated chat interface for QnA, an easy and supportinve solution to trace the current Affairs quickly.

## Features
- Personilized preference based News Articles filteration.
- Real-time updated news articles with interface showing Topic, link to original website, language, article source domain, relevant keywords, summarized content from scrapped main content, integrated QnA Assistant.
- Multipage Interface to see news articles, filtered on the basis of language, country, keywords, dates, News Domain.
- Limits and offset can also be set.

## How to Run

### 1. Install Dependencies
Ensure you have Python installed. Create a virtual environment and install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2. Create a .env file and save access key for the following:

```bash
NEWS_API_KEY= ****************** (MediaStack API)
hf_token = *************
GROQ_API_KEY = *************
```
### 3. Lauch the Application
Run the following command to start the application:

```bash
streamlit run app.py
```

## Implementation Details
<!-- * **MediaStack API integration :** -->
    * Dyanamic URI created as per user preferences to seamlessly fetch news articles.
    * The main content scrapped from its original website through available link to it.
    * Summarized and bullated key points extracted using LLM, from main content.
    * Relevant KeyWords Extracted (Topic Modelling), and integrated with QnA interface.

## Modelling Details
### For QnA Modelling
- LangChain Based ChatGroq Interface used as Chat Assistant Model.
- In order to maintain the state or chat history, "ConversationBufferMemory" used
- In order make seamless integration, Sequence Runnables used along with parser
### For Content Summarizer and bullating relevant points of original content
- LangChain Based ChatGroq used as LLM to do the task
- Model is prompted to do the specific task, generate the relevant and concise response 
### For Topic Modelling
- Topic Modelling with LDA, an unsupervised machine learning method to extract keywords
- Keywords Extraction using pretrained KeyBERT model, which is task specific *"all-MiniLM-L6-v2"* BERT model (this is used finally)


## Streamlit Based Interface:

### Initial appearance of application, before the preference given by user.
#### ![Initial Logo](images\image1.png) 


### Setting Parameters for filteration and triggering "Update Parameter".
#### ![Initial Logo](images\image2.png)

### Triggering the Summary Generation button
#### ![Initial Logo](images\image3.png)


### Triggering the Chat Assistant button to have Chat Input Block, with "U" as user query and "A" as assistant response.
#### ![Initial Logo](images\image4.png)

### Similar setup is for other news articles, where each one have information as shown in picture along with extracted keywords from original context.
#### ![Initial Logo](images\image5.png)

### The "Refresh/Reset session" will clear all main body content.

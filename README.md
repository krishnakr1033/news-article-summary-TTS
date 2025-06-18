# news-article-summary-with-ai-assistant

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

**Implementation Approach**

<!-- * **Graph Database:**
    * Utilize Neo4j to store and manage personas, traits, and user preferences.
    * Model personas with their associated traits (preferred activities, interests) as nodes and relationships.
    * Store user preferences (city, time_range, budget, interests, starting_point) as nodes and relationships. -->

<!-- 
* **Workflow:**
    * **Initialize Personas:** Create persona nodes and their associated trait nodes in the graph.
    * **User Interaction:**
        * Process user messages using the LLM to maintain conversation flow.
        * Extract user preferences from the conversation history.
        * Store user preferences in the graph.
    * **Personalized Recommendations:** 
        * Use the graph to retrieve relevant information (e.g., persona preferences, user preferences) for personalized recommendations.
**Implementation Workflow**
<img src="tour_plan.png" alt="Flowchart of the Tour Planning Process" align="center" width="500px"> -->

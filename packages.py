import requests
from dotenv import load_dotenv
import os
import html
from datetime import datetime
import pandas as pd
import numpy as np
from urllib.parse import urlparse
from bs4 import BeautifulSoup as bs 
import re
import streamlit as st
# import langchain
from langchain_openai import ChatOpenAI
from huggingface_hub import login
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain_core.runnables import RunnablePassthrough, RunnableLambda, RunnableSequence
from langchain_core.output_parsers import StrOutputParser

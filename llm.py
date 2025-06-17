from packages import *
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder



# def modelling(): # no need to call it else where
#     load_dotenv()
#     os.getenv("hf_token")
#     llm=HuggingFaceEndpoint(
#         repo_id="microsoft/Phi-3-mini-4k-instruct",
#         task="text-generation",
#         max_new_tokens=512,
#         do_sample=False,
#         repetition_penalty=1.03,
#     )
#     return llm
load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')    

def model1_pipeline(main_contextt): # check for its main_content, is exist then call this

    # model1 = ChatHuggingFace(llm=modelling())

    model1 = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=GROQ_API_KEY,
        # other params...
    )

    prompt1 = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that summarizes news articles and enhances its content quality as per the main context provided."),
        ("human", "Here is the context: {context}, Now, please summarize the news article and mention the relevant point/events/incident which could be important for current affairs"),
    ])

    parser = StrOutputParser()
    chain1 = prompt1 | model1 | parser
    
    response1 = chain1.invoke({
        "context": main_contextt 
    })

    return response1 # have all three just reflect the ai message for here



from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder

class ChatInterface:
    def __init__(self, summarized_context):
        self.memory = ConversationBufferMemory(return_messages=True)
        self.parser = StrOutputParser()
        self.summarized_context = summarized_context

        self.model1 = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            api_key=GROQ_API_KEY,
        )

        # Add initial system message to memory
        self.memory.chat_memory.add_message({
            "role": "system",
            "content": f"""You are a helpful assistant that possesses summarized news articles. 
Users will ask questions based on this summary. Keep your answers concise, preferably bullet-pointed, and wrap up within 5-6 lines.
Summarized content: {self.summarized_context}"""
        })

    def reset(self, new_context):
        self.__init__(new_context)

    def chatModel_pipeline(self, user_input):
        try:
            self.prompt = ChatPromptTemplate.from_messages([
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{question}")
            ])

            self.chain = self.prompt | self.model1 | self.parser

            # Run the chain
            self.ai_message = self.chain.invoke({
                "question": user_input,
                "chat_history": self.memory.chat_memory.messages
            })

            # Add user and AI message to memory
            self.memory.chat_memory.add_message({"role": "human", "content": user_input})
            self.memory.chat_memory.add_message({"role": "ai", "content": self.ai_message})

            return self.ai_message
        
        except Exception as e:
            import traceback
            print("🛑 Error during chatModel_pipeline:")
            traceback.print_exc()
            return "⚠️ Assistant failed to respond."








    




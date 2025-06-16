from packages import *

def modelling(): # no need to call it else where
    load_dotenv()
    os.getenv("hf_token")
    llm=HuggingFaceEndpoint(
        repo_id="microsoft/Phi-3-mini-4k-instruct",
        task="text-generation",
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
    )
    return llm
    
global model1 

def model1_pipeline(main_contextt): # check for its main_content, is exist then call this

    model1 = ChatHuggingFace(llm=modelling())

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



class ChatInterface:
    def __init__(self, summarized_context):
        self.memory = ConversationBufferMemory(return_messages=True)
        self.parser = StrOutputParser()
        self.summarized_context = summarized_context
        self.memory.chat_memory.add_message({"role":'system',"content":
              """You are a helpful assistant that possess summarized news articles, user will have some query which you will answer as per your knowlege base, or exteranl web search if this tool calling facility allocated to you 
                    Make sure your answer should be to the point, not much text in your response, recommeded to make bullated points, wrap up your response with 5-6 line of text only
              """                          
        })
    def reset(self, new_context):
        self.__init__(new_context)  # Re-initializing
        
    def chatModel_pipeline(self,user_input):
        self.prompt = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="chat_history"),
            ("human","{question}"),
        ])

        self.chain = self.prompt | model1 | self.parser
        ai_message = self.chain.invoke({"question":self.user_input, "chat_history": self.memory.chat_memory.messages})

        human_message = self.prompt.messages[1].prompt.template.format(question=self.user_input)
        self.memory.chat_memory.add_message({"role": "human", "content": human_message})
        self.memory.chat_memory.add_message({"role": "ai", "content": ai_message})

        return ai_message







    




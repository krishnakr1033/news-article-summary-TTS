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
        ("system", "You are a helpful assistant that summarizes news articles and enhances its content as per the context provided and then start the conversation with user as per your knowledege base and context."),
        ("human", "Here is the context: {context}, Now, please summarize the news article and enhance it with your knowledge  base."),
    ])

    parser = StrOutputParser()
    chain1 = prompt1 | model1 | parser
    
    response1 = chain1.invoke({
        "context": main_contextt 
    })

    memory1 = ConversationBufferMemory(return_messages=True)
    memory1.chat_memory.add_message({"role":"system", "content":prompt1.messages[0].prompt.template})
    # Add the human message (with the context used in response1)
    human_message = prompt1.messages[1].prompt.template.format(context=main_contextt)
    memory1.chat_memory.add_message({"role": "human", "content": human_message})
    # Add the model1 response
    memory1.chat_memory.add_message({"role": "ai", "content": response1})

    return memory1 # have all three just reflect the ai message for here

def chatModel_pipeline(memory):

    prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="chat_history"),
        ("human","{question}"),
    ])
    parser = StrOutputParser()
    chain = prompt | model1  | parser

    def conversation():
        user_query = input("Enter your question: ")
        chat_history = memory.chat_memory.messages
        ai_message = chain.invoke({"question":user_query, "chat_history": memory.chat_memory.messages})

        human_message = prompt.messages[1].prompt.template.format(question=user_query)
        memory.chat_memory.add_message({"role": "human", "content": human_message})
        memory.chat_memory.add_message({"role": "ai", "content": ai_message})

        return ai_message




    




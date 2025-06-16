# import backend
# from packages import *
import streamlit as st
import math
import json
import llm, utility
import numpy as np

def mainContent(df):
    if df.empty:
        st.warning("No data available to display.")
        return

    # Settings
    ITEMS_PER_PAGE = 9
    COLUMNS = 1

    total_pages = math.ceil(len(df) / ITEMS_PER_PAGE)
    st.session_state.page = min(st.session_state.get("page", 1), total_pages)

    # Pagination controls
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("⬅ Prev") and st.session_state.page > 1:
            st.session_state.page -= 1
    with col3:
        if st.button("Next ➡") and st.session_state.page < total_pages:
            st.session_state.page += 1

    # Show current page
    st.markdown(f"### Page {st.session_state.page} of {total_pages}")

    # Compute current page slice
    start_idx = (st.session_state.page - 1) * ITEMS_PER_PAGE
    end_idx = start_idx + ITEMS_PER_PAGE
    page_data = df.iloc[start_idx:end_idx]

    # Render each row
    for idx, row in page_data.iterrows():
        cols = st.columns(COLUMNS)
        for col in cols:
            with col:
                main_text = row.get("main_context")
                st.markdown(f"### {row.get('title', 'No Title')}")
                st.write(f"**Description:** {row.get('description', 'N/A')}")

                col1,col2 = st.columns(2)
                with col1:
                    st.link_button("**URL**",row.get('url', 'N/A'))                       
                    st.write(f"**Category:** {row.get('category', 'N/A')}")
                    st.write(f"**Language:** {row.get('language', 'N/A')}")
                    st.write(f"**Published At:** {row.get('published_at', 'N/A')}")
                    st.write(f"**Domain Address:** {row.get('domain_address', 'N/A')}")
                with col2:
                    listKeywords = utility.keywords_extractor(row.get('title','') +'\n\n'+ row.get('description','')+'\n\n'+row.get('main_content',''))
                    st.write(listKeywords)
                
                if st.button('Summary of News Article followed with chatbot assistant',use_container_width=True,key=f'summary_button_{idx}'):
                    print(type(main_text))
                    if main_text == np.nan:                                          #this is unable to implement
                        st.write("Sorry! your article source is not fetched!!")
                    else:
                        with st.expander("🔍 More Info / Extended Study"):
                            # need to call a fn if it's original content is present                    
                            st.session_state.summarized_context = llm.model1_pipeline(main_text)
                            st.write(st.session_state.summarized_context)
                            st.session_state.chatbot = llm.ChatInterface(st.session_state.summarized_context)
                        
                            if st.button("Chat Assistant: ",use_container_width=True,key=f'chat_button_{idx}'):
                                user_prompt = st.chat_input("Ask Something...")
                                if user_prompt:
                                    @st.dialog("Your Assistant for Current Affairs")
                                    def chat_dialog():
                                        with st.chat_message("user: "):
                                            st.write(user_prompt) 
                                        # calling llm for response, pass user_prompt, update the memory with human and ai message, return ai_message    
                                        ai_message=st.session_state.chatbot.chatModel_pipeline(user_prompt)
                                        with st.chat_message('assistant: '):
                                            st.write(ai_message)
                                        
                                        if st.button("❌ Close Chat",key=f'chat_close_button_{idx}'):
                                            st.session_state.chatbot = llm.reset(st.session_state.summarized_context)
                st.markdown("---")
import streamlit as st
import utility
import app_mainContent
import backend


def init_session_state():
    if 'user_params' not in st.session_state:
        st.session_state.user_params = {
            # "keywords": [],
            # "languages": [],
            # "countries": [],
            # "categories":[],
            # # "sources":[],
            # "limit":15, #default values
            # "offset":0,
            # "date":None # shows the range from date and to date
        }
    if 'categorical_params' not in st.session_state:
        st.session_state.categorical_params={
            # making dictionary of parameters
            # "paramlist" : ["sources", "languages", "countries", "categories", "keywords", "limit", "offset", "date", "sort"],
            "categories" : ["general","business", "entertainment", "health", "science", "sports", "technology"],
            "countries" : ["ar", "at", "au", "be", "bg", "br", "ca", "cn", "co", "cu", "cz", "de", "eg", "fr", "gb", "gr", "hk", "hu", "id", "ie", "il", "in", "it", "jp", "kr", "lt", "lv", "ma", "mx", "my", "ng", "nl", "no", "nz", "ph", "pl", "pt", "ro", "rs", "ru", "sa", "se","sg","si","sk","th","tr","tw","ua","us","ve","za"],
            "languages" : ["ar", "de", "en", "es", "fr", "he", "it", "se", "nl", "pt", "ru", "zh"] 
        }

    # may be we can add for news sorces for extended study


def main():
    
    init_session_state()

    with st.sidebar:
        st.markdown('Parameter for *filteration*:')
        st.session_state.user_params['categories'] =str(st.selectbox(
            "category ",
            ("general","business", "entertainment", "health", "science", "sports", "technology"),
            index=None,
            placeholder = "your category of news... ",
            key='category_by_user' 
        )) 
        st.session_state.user_params['countries'] = list(st.multiselect(
            "Countries",
            ("ar", "at", "au", "be", "bg", "br", "ca", "cn", "co", "cu", "cz", "de", "eg", "fr", "gb", "gr", "hk", "hu", "id", "ie", "il", "in", "it", "jp", "kr", "lt", "lv", "ma", "mx", "my", "ng", "nl", "no", "nz", "ph", "pl", "pt", "ro", "rs", "ru", "sa", "se","sg","si","sk","th","tr","tw","ua","us","ve","za"),
            key='countries_by_user'
        ))
        st.session_state.user_params['languages'] = list(st.multiselect(
            label="Languages",
            options= ("ar", "de", "en", "es", "fr", "he", "it", "se", "nl", "pt", "ru", "zh"),
            placeholder= "select code of languages...",
            key='languages_by_user',
        ))
        st.session_state.user_params['keywords'] = str(st.text_input(
            "keywords",
            placeholder='few words keywords...'
        ))

        # If a mode is selected, show dialog accordingly
        options = ['-- Select --', 'on_date', 'from_to']
        date_mode = st.radio("Select dates:", options, horizontal=True)

        if date_mode != '-- Select --':
            st.subheader("Date:")
            st.session_state.user_params['date'] = None
            if date_mode == 'on_date':
                selected_date = st.date_input('Select a particular date', format='YYYY-MM-DD')
                st.session_state.user_params['date'] = str(selected_date)
                # print(st.session_state.date)

            elif date_mode == 'from-to':
                col1, col2 = st.columns(2)
                with col1:
                    start_date = st.date_input('Select a *from* date', key='start_date', format='YYYY-MM-DD')
                with col2:
                    end_date = st.date_input('Select a *to* date', key='end_date', format='YYYY-MM-DD')
                st.session_state.user_params['date'] = f"{start_date},{end_date}"
        else:
            if "date" in st.session_state.user_params:
                del st.session_state.user_params["date"]

        col1 ,col2 = st.columns(2)
        with col1:
            st.session_state.user_params['limit']=st.number_input("Insert Integer Value:",value=15)
        with col2:
            st.session_state.user_params['offset']=st.number_input("Insert Integer Value:",value=0)


        col1, col2 = st.columns(2)
        with col1:
            if st.button('update parameter'):
                st.session_state.parameter = utility.user_input(st.session_state.user_params)
                st.session_state.content = backend.data_extractor(st.session_state.parameter)
                st.session_state.main_body_calling = True

        with col2:
            if st.button('Reset session'):
                st.rerun()
                # init_session_state()

    # main body ----------------------------------------------------------------------------------------------------
    st.title("Hello, *Welcome* to **NewsMagic!** :sunglasses:")

    if st.session_state.get('main_body_calling',True):
        # st.markdown('this is okay- 108')
        app_mainContent.mainContent(
            st.session_state.content
        )
    else:
        st.info("Click **Update Parameter** in the sidebar to view content.")
    

if __name__== '__main__':
    main()
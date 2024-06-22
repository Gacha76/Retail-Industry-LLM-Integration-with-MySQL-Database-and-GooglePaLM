# streamlit run main.py
import streamlit as st
from langchain_helper import get_few_shot_db_chain
from generate_plot import generate_matplotlib_plot

st.title("NLM Project")

question = st.text_input("Question: ")
exit_app = st.sidebar.button("Shut Down")

if question:
    try:
        chain = get_few_shot_db_chain()
        response = chain.run(question)

        st.header("Answer")
        st.write(response)        

        print(response,len(list(response)),type(response))
        print(response.split(','))
        if len(response.split(',')) != 1:
            matplotlib_plot = generate_matplotlib_plot(response)
            st.pyplot(matplotlib_plot)
    except:
        st.write("Please provide a relevant query")

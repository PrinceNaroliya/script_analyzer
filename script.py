from langchain_groq import ChatGroq
from typing import TypedDict, Literal
from langgraph.graph import StateGraph, START, END
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.title("Script Reviewer")

script_input = st.text_area("Enter Your Script...", height=150)

model = ChatGroq(
    model = "llama-3.3-70b-versatile",
    groq_api_key = os.getenv("GROQ_API_KEY")
)

class ScriptReviewer(TypedDict):
    script: str
    sentiment: Literal['positive', 'negative']
    response: str

def find_sentiment(state: ScriptReviewer):
    prompt = f"""Find the sentiment according to this Script and it should be positve or negative and don't provide any extra information. \n\n {state['script']}"""

    response = model.invoke(prompt).content

    return {
        'sentiment': response
    }

def check_sentiment(state: ScriptReviewer) -> Literal['positive', 'negative']:
    if state['sentiment'] == 'positive':
        return 'positive'
    else:
        return 'negative'

def positive(state: ScriptReviewer):
    prompt = f'Write a positive 1 to 2 lines of short review about the script \n\n {state['script']} \n\n and tell it is a positive script and there is no issue.'

    response = model.invoke(prompt).content

    return {
        'response': response
    }

def negative(state: ScriptReviewer):
    prompt = f'Write a negative 1 to 2 lines of short review about the script \n\n {state['script']} \n\n and tell it is a negative script and there is issue and also tell what is the issue.'

    response = model.invoke(prompt).content

    return {
        'response': response
    }

graph = StateGraph(ScriptReviewer)

graph.add_node('find_sentiment', find_sentiment)
graph.add_node('positive', positive)
graph.add_node('negative', negative)

graph.add_edge(START, 'find_sentiment')
graph.add_conditional_edges('find_sentiment', check_sentiment)
graph.add_edge('positive', END)
graph.add_edge('negative', END)

workflow = graph.compile()

if st.button("Enter"):
    if script_input:
        initial_state = {
            'script': script_input
        }

        with st.spinner("Analysing..."):
            result = workflow.invoke(initial_state)

        st.header("Sentiment of the Script: ")
        st.subheader(result['sentiment'])

        st.header("Response: ")
        st.write(result['response'])
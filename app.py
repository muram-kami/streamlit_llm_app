from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
# langchain_comunityのインストールが必要です
# pip install langchain-community

# タイトル
st.title("Streamlit LLM App")
# 説明
st.write("このアプリは、ユーザーが質問を入力し、選択した専門家に回答を求めるものです。")

st.divider()

# ラジオボタン
option = st.radio("回答させる専門家を選択:", ("教育の専門家", "睡眠の専門家"))
# テキスト入力
user_input = st.text_input("質問を入力してください:")

# 実行ボタン
if st.button("実行"):
    if user_input:
        system_template = "あなたは、{expert}AIです。ユーザーからの質問に100文字以内で回答して下さい。"
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_template),
            ("human", "{input}")
        ])
        messages = prompt.format_messages(expert=option, input=user_input)
        chat = ChatOpenAI()
        response = chat(messages)
        st.markdown(f"**{option}の回答:**")
        st.write(response.content)
    else:
        st.warning("質問を入力してください。")


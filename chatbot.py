import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.header("ChatBot")

# inmitialise session state

if "messages" not in st.session_state:
    st.session_state.messages = []


# display all chat history 
# messages
# {"role":"user/ assitant",  "content": "propmt/response"}
    
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# chat layout
# chat input : kind of placeholder where useer will input his/her prompt
# chat message: display all input messages by user and response from assistant

# directly assignemnt + validation of prompt
if prompt:= st.chat_input('Message'):
    msg={
        "role": "user",
        "content": prompt
    }
    st.session_state.messages.append(msg)
    
    with st.chat_message('user'):
        st.markdown(prompt)

    with st.chat_message("assistant"):
    # create chat completion api
        chatRespone = client.chat.completions.create(
            model= "gpt-3.5-turbo-0125",
            messages= st.session_state.messages,
            temperature=0.7,
            n =1
        )

        response = chatRespone.choices[0].message.content

        st.markdown(response)

    st.session_state.messages.append(
        {
        "role": "assistant",
        "content": response
    }
    )
    
        
    

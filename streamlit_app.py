from openai import OpenAI
import streamlit as st
import requests

st.title("HalluGuard")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
chatBotResponse = None

#Classify Fact and Opinion Endpoint
def classify_fact(answer):
    url = 'https://antihallucination.naufalfaza80.repl.co/user/classify-fact'
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImIxNWYyZWMzLTA2OWUtNDBjNS05MGY5LWNiOGRjNzFhZjA2YiIsImVtYWlsIjoidGVzMTIzQGdtYWlsLmNvbSIsImlhdCI6MTcwMjE5Mjc2NH0.TGEK5hHMd_nbTecZutIHkee6m9f6fWRxW2xgyvP-zC0',
        'Content-Type': 'application/json',
    }

    data = {
        'answer': answer
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        # Extract "facts" and "opinions" from the result
        facts = result.get("facts", [])
        opinions = result.get("opinions", [])
        return facts, opinions
    else:
        return {'error': f"Failed to classify fact. Status code: {response.status_code}"}
    
#Fact Checker Endpoint
def check_fact(fact):
    url = 'https://antihallucination.naufalfaza80.repl.co/user/check-fact'
    
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImIxNWYyZWMzLTA2OWUtNDBjNS05MGY5LWNiOGRjNzFhZjA2YiIsImVtYWlsIjoidGVzMTIzQGdtYWlsLmNvbSIsImlhdCI6MTcwMjE5Mjc2NH0.TGEK5hHMd_nbTecZutIHkee6m9f6fWRxW2xgyvP-zC0',
        'Content-Type': 'application/json',
    }

    data = {
        'fact': fact
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        return result.get("status",[])
    else:
        return {'error': f"Failed to check fact. Status code: {response.status_code}"}

#Main Page (ChatBot)
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []
full_response = ""
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += (response.choices[0].delta.content or "")
            message_placeholder.markdown(full_response + "")
        message_placeholder.markdown(full_response)
        chatBotResponse = full_response
    st.session_state.messages.append({"role": "assistant", "content": full_response})


# Sidebar with input field and button
# Classify text input and button
st.sidebar.title("HalluGuard Feature")
user_input = st.sidebar.text_area("Enter text to classify:", "")
col1, col2 = st.sidebar.columns(2)
if col1.button("Classify Fact"):
    facts, opinions = classify_fact(user_input)
    
    # Display facts
    st.sidebar.markdown("### Facts:")
    for fact in facts:
        st.sidebar.markdown(f"- {fact}")

    # Display opinions
    st.sidebar.markdown("### Opinions:")
    for opinion in opinions:
        st.sidebar.markdown(f"- {opinion}")

# Insert a divider between the two text areas
st.sidebar.markdown("<hr>", unsafe_allow_html=True)

# Check Fact text input and button
user_fact = st.sidebar.text_area("Enter the fact to check:", "")
if st.sidebar.button("Check Fact"):
    result = check_fact(user_fact)
    
    if result != True:
        st.sidebar.markdown(
            f"<div style='color:#C02727; padding:10px; border-radius:5px;'>The Text is not a Fact</div>",
            unsafe_allow_html=True
        )
    else:
        st.sidebar.markdown(
            f"<div style='color:#1FC561; padding:10px; border-radius:5px;'>The Text is a Fact</div>",
            unsafe_allow_html=True
        )

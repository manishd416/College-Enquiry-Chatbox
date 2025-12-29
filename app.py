import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# One-time downloads (comment after first run)
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

# NLP tools
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Knowledge base
responses = {
    "admission": "Admissions start in May every year. Visit the official website for online applications.",
    "fee": "The annual fee for the AI & ML department is ₹1,50,000.",
    "principal": "Our principal is Dr. K. Venkatesh.",
    "college": "This is Sri Venkateswara College of Engineering and Technology.",
    "placement": "Our placement cell partners with TCS, Infosys, and Wipro.",
    "courses": "We offer B.Tech, M.Tech, and MBA programs.",
    "ai": "The AI lab is located in Block B, 2nd floor, with GPU systems.",
    "library": "The library is open from 8 AM to 8 PM on weekdays.",
    "where library": "The library is open from 8 AM to 8 PM on weekdays.",

    "canteen": "The canteen is open from 9 AM to 5 PM.",
    "hostel": "Hostel facilities are available with Wi-Fi and security."
}

# Preprocessing
def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
        if word.isalnum() and word not in stop_words
    ]
    return tokens

# Chatbot logic
def chatbot_response(user_input):
    tokens = preprocess(user_input)
    matches = [key for key in responses if key in tokens]

    if matches:
        confidence = round(len(matches) / len(tokens), 2)
        return responses[matches[0]], confidence
    else:
        return "Sorry, I don't have information about that. Please contact the admin office.", 0.0

# Page title
st.title("College Enquiry Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history (scrollable automatically)
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input (ChatGPT-style)
user_input = st.chat_input("Ask me anything about the college...")

if user_input:
    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot response
    reply, confidence = chatbot_response(user_input)
    bot_message = f"{reply}\n\n**Confidence:** {confidence}"

    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_message
    })

    with st.chat_message("assistant"):
        st.markdown(bot_message)

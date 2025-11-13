import nltk
import re
import streamlit as st

responses = {
    "admission": "Admissions start in May every year. Visit the official website for online applications.",
    "fee": "The annual fee for the AI & ML department is ₹1,50,000.",
    "principal": "Our principal is Dr. K. Venkatesh.",
    "college name": "This is Sri Venkateswara College of Engineering and Technology.",
    "placement": "Our placement cell partners with top companies like TCS, Infosys, and Wipro.",
    "courses": "We offer B.Tech, M.Tech, and MBA programs across various specializations.",
    "ai lab": "The AI lab is located in Block B, 2nd floor, with high-end GPU systems.",
    "library": "The library is open from 8 AM to 8 PM on weekdays.",
    "canteen": "The canteen serves hygienic food and is open from 9 AM to 5 PM.",
    "hostel": "Hostel facilities are available for both boys and girls with Wi-Fi and security.",
}
def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in responses.keys():
        if re.search(key, user_input):
            return responses[key]
    return "Sorry, I don't have information about that. Please contact the admin office."
st.title("🎓 College Enquiry Chatbot")
st.write("Hi! I'm your AI assistant. Ask me anything about the college.")

# Chat input box
user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input.strip() != "":
        reply = chatbot_response(user_input)
        st.write(f"**Bot:** {reply}")

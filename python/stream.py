import streamlit as st
from streamlit_feedback import streamlit_feedback

# Sample API response
api_response = [
    ["Sentence 1A", "Sentence 1B", "Sentence 1C"],
    ["Sentence 2A", "Sentence 2B", "Sentence 2C"],
    ["Sentence 3A", "Sentence 3B", "Sentence 3C"]
]

# Custom CSS for the boxes and feedback alignment
st.markdown("""
    <style>
    .sentence-box {
        border: 1px solid #ccc;
        padding: 10px;
        margin: 10px 0;
        border-radius: 5px;
        position: relative;
    }
    .feedback {
        position: absolute;
        right: 10px;
        top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Function to display the response with feedback
def display_response(api_response):
    for index, sentences in enumerate(api_response):
        for sentence_index, sentence in enumerate(sentences):
            with st.container():
                st.markdown(f'<div class="sentence-box">', unsafe_allow_html=True)
                st.write(sentence)
                st.markdown(f'<div class="feedback">', unsafe_allow_html=True)
                feedback = streamlit_feedback(
                    options=["👍", "👎"],
                    key=f"feedback_{index}_{sentence_index}"
                )
                if feedback == "👍":
                    st.write(f"Thumbs up clicked for Sentence {sentence_index + 1} in Response {index + 1}")
                elif feedback == "👎":
                    st.write(f"Thumbs down clicked for Sentence {sentence_index + 1} in Response {index + 1}")
                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

# Display the API response
display_response(api_response)

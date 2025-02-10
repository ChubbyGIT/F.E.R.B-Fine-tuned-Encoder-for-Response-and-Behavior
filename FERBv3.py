import streamlit as st

# Set page configuration (must be the first Streamlit command)
st.set_page_config(page_title="F.E.R.B - Voice Assistant", page_icon="Ferb Fletcher.png", layout='wide')



# Title
st.title("F.E.R.B – Fine-tuned Encoder for Response and Behavior")

# About Section
st.header("About F.E.R.B")
st.write(
    "F.E.R.B is an advanced voice assistant powered by deep learning and NLP techniques, "
    "designed for intelligent and context-aware interactions. Built upon transformer-based "
    "architectures like BERT or GPT, it utilizes fine-tuned encoders to process and generate "
    "natural language responses efficiently."
)

st.subheader("Key Features:")
st.markdown(
    "- 🔹 **Fine-Tuned Model** – Trained on diverse datasets to enhance response accuracy and adaptability.\n"
    "- 🔹 **Encoder-Based NLP** – Leverages attention mechanisms for deep contextual understanding.\n"
    "- 🔹 **Context-Aware Responses** – Dynamically adjusts behavior based on user inputs.\n"
    "- 🔹 **Adaptive Learning** – Improves over time through reinforcement learning and sentiment analysis.\n"
    "- 🔹 **Multimodal Capabilities** – Can integrate with voice recognition and text-to-speech engines."
)

st.write(
    "F.E.R.B is designed for applications in virtual assistance, customer support, smart automation, "
    "and interactive AI systems, offering human-like conversational experiences with high precision. 🚀"
)

# Features Section
st.header("Features of a Voice Assistant")
st.write(
    "Voice assistants can perform a wide range of tasks using NLP and AI. Some key functionalities include:\n"
    "- 📞 **Call & Message Handling** – Place calls and send messages via voice commands.\n"
    "- 🔍 **Information Retrieval** – Answer queries using the web, encyclopedias, or knowledge bases.\n"
    "- 🏠 **Smart Home Control** – Manage IoT devices like lights, thermostats, and security systems.\n"
    "- 📅 **Task & Schedule Management** – Set reminders, schedule meetings, and manage to-do lists.\n"
    "- 🎵 **Entertainment** – Play music, podcasts, and videos.\n"
    "- 🛍 **E-commerce Assistance** – Help with online shopping, order tracking, and recommendations.\n"
    "- 🌍 **Multilingual Support** – Understand and translate multiple languages.\n"
    "- 🔒 **Security & Authentication** – Provide voice-based authentication and user verification."
)

# Designed By Section
st.header("Designed by Abhigyan Das")
st.write(
    "**Abhigyan Das** is a final-year Computer Science student at Vellore Institute of Technology, "
    "with expertise in AI, machine learning, cybersecurity, and web development. He has interned at multiple "
    "organizations, working on projects ranging from petroleum price prediction to process management web applications. "
    "With experience in deep learning models like VGGNet, LSTM, and BiLSTM, he is passionate about developing intelligent systems."
)

# Buttons for External Links
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Colab Link"):
        st.markdown("[Click here](https://colab.research.google.com/drive/1jVsmDHGltxlV8ZbAmL6dkC1R1LUwq2Yk?usp=sharing)")

with col2:
    if st.button("Architecture Page"):
        st.markdown("[Click here](https://www.wikipedia.org)")

with col3:
    if st.button("Future Scope"):
        st.markdown("[Click here](https://www.amazon.com)")

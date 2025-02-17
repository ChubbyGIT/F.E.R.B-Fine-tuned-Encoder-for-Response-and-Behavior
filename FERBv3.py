import streamlit as st

# Set page configuration (must be the first Streamlit command)
st.set_page_config(page_title="F.E.R.B - Voice Assistant", page_icon="Ferb Fletcher.png", layout='wide')



# Title
st.title("F.E.R.B – Fine-tuned Encoder for Response and Behavior")

# About Section
# Introduction
st.write("""
F.E.R.B is an advanced voice assistant powered by deep learning and natural language processing (NLP) techniques, designed for intelligent and context-aware interactions. Unlike traditional assistants, F.E.R.B leverages **LLama 2**, a powerful transformer-based large language model (LLM) developed by Meta, for efficient and natural language generation.
""")

# LLama 2 Architecture Overview
st.header("LLama 2 Architecture Overview")

st.write("""
LLama 2 is a **decoder-only transformer model** optimized for **autoregressive text generation**. It builds upon the advancements of models like GPT while improving **efficiency and scalability**.
""")

# Key Features of LLama 2
st.subheader("🔹 Model Variants")
st.write("LLama 2 comes in **7B, 13B, and 65B** parameter versions.")

st.subheader("🔹 Architecture Type")
st.write("Decoder-only transformer, designed for **causal language modeling (CLM)**.")

st.subheader("🔹 Training Data")
st.write("Trained on **2 trillion tokens**, covering diverse datasets for enhanced reasoning and contextual understanding.")

st.subheader("🔹 Optimization")
st.write("Uses **Grouped-Query Attention (GQA)** and **SwiGLU activation functions**, improving efficiency and inference speed.")

st.subheader("🔹 Fine-Tuning & Quantization")
st.write("Supports **low-bit quantization (4-bit, 8-bit)** using **BitsAndBytes** for reduced memory usage without major performance loss.")


st.header("About the Dataset")

st.write("""
The model **aboonaji/llama2finetune-v2** is a fine-tuned version of Meta's LLama 2, specifically tailored for medical applications. The fine-tuning process utilized the **aboonaji/wiki_medical_terms_llam2_format** dataset, which comprises medical terminology and related information. This dataset was employed to enhance the model's understanding and generation of medical language, making it more proficient in handling health-related queries and discussions.  
""")

st.markdown("[GitHub Repository: AI Doctor Chatbot using LLMs](https://github.com/khaz-dev/AI_DoctorChatbot_LLMs)")
st.markdown("[Hugging Face Model Page](https://huggingface.co/aboonaji/llama2finetune-v2)")

st.write("""
The fine-tuning was conducted using Hugging Face's **AutoTrain** platform, which streamlines the process of training and deploying machine learning models. This approach ensures that the model is well-suited for applications requiring medical knowledge and conversational capabilities.  
""")

st.markdown("[Medium Article: Unlocking Medical Conversations - Fine-Tuning LLMs with Hugging Face](https://medium.datadriveninvestor.com/unlocking-medical-conversations-fine-tuning-llms-with-hugging-face-a73103362028)")

st.write("""
These resources provide comprehensive information on the dataset and the methodologies employed in fine-tuning the **aboonaji/llama2finetune-v2** model for medical applications.
""")

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

st.header("Features of a Voice Assistant")

st.write("""
### 🏥 Medical Knowledge & Assistance  
✅ **Symptom Analysis** – Provides insights on possible conditions based on symptoms.  
✅ **Medical Advice** – Offers general health guidance based on trained data.  
✅ **Drug & Prescription Info** – Provides details about common medications, dosages, and uses.  
✅ **Emergency Guidance** – Suggests first-aid measures and emergency response steps.  
""")

st.write("""
### 🎙️ Voice-Powered Interaction  
✅ **Hands-Free Operation** – Uses AI-driven voice recognition for seamless communication.  
✅ **Natural Language Processing (NLP)** – Understands complex medical queries conversationally.  
✅ **Multilingual Support** – Can be trained to recognize and respond in multiple languages.  
""")

st.write("""
### 🔬 AI-Powered Insights  
✅ **Machine Learning-Based Responses** – Continuously improves accuracy with real-world data.  
✅ **Personalized Suggestions** – Adapts recommendations based on user history and queries.  
✅ **Data-Driven Analysis** – Uses trained datasets for accurate health-related responses.  
""")

# Designed By Section
st.header("Designed by Abhigyan Das")
st.write(
    "**Abhigyan Das** is a final-year Computer Science student at Vellore Institute of Technology, "
    "with expertise in AI, machine learning, cybersecurity, and web development. He has interned at multiple "
    "organizations, working on projects ranging from petroleum price prediction to process management web applications. "
    "With experience in deep learning models like VGGNet, LSTM, and BiLSTM, he is passionate about developing intelligent syssttems."
)

st.header("Parthasarathi Mohanty")
st.write(
    "**Parthasarathi Mohanty** is a final-year Computer Science student at Vellore Institute of Technology, specializing in IoT. "
    "He has expertise in data analytics, SQL, Python, Power BI, and full-stack development. Parthasarathi has worked on various projects, "
    "including a Credit Card Financial Dashboard and blockchain-based research for the Internet of Vehicles. "
    "He is passionate about leveraging data-driven insights and innovative technologies to solve complex problems and contribute to impactful solutions."
)
st.header("Manas Ranjan")
st.write(
    "**Manas Ranjan** is a final-year Computer Science student at Vellore Institute of Technology, with expertise in AI, machine learning, SQL, and Python. "
    "He has interned at IIT BHU in the field of deep learning and AI. He is passionate about integrating sports with technologies and is a data-driven individual "
    "who analyzes various types of data. He intends on working in the field of sports technology and analysis."
)
import streamlit as st

# Create three columns for the images to be displayed side by side
col1, col2, col3 = st.columns(3)
with col1:
    st.image("C:/Users/91988/Desktop/codes/F.E.R.B/Trial Codes/AbhigyanPic.jpg", 
             caption="Abhigyan Das", 
             width=300)

with col2:
    st.image("C:/Users/91988/Desktop/codes/F.E.R.B/Trial Codes/Manas Pic.jpg", 
             caption="Manas Ranjan", 
             width=200)

with col3:
    st.image("C:/Users/91988/Desktop/codes/F.E.R.B/Trial Codes/Parth Pic.jpg", 
             caption="Parthasarathi Mohanty", 
             width=300)

# Buttons for External Links
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Colab Link"):
        st.markdown("[Click here](https://colab.research.google.com/drive/1jVsmDHGltxlV8ZbAmL6dkC1R1LUwq2Yk?usp=sharing)")

with col2:
    if st.button("GitHub Page"):
        st.markdown("[Click here](https://github.com/ChubbyGIT/F.E.R.B-Fine-tuned-Encoder-for-Response-and-Behavior)")

with col3:
    if st.button("Future Scope"):
        st.markdown("[Click here](https://colab.research.google.com/drive/1jccaA-87biLWqwp9QnoGoMRKrX03p6P8?usp=sharing#scrollTo=WVa0caPZlogN)")



st.title("Version 4")

# Path to your video file
video_file = r"C:\Users\91988\Desktop\codes\F.E.R.B\Trial Codes\F.E.R.Bv4 – aboonaji - Colab - Google Chrome 2025-02-16 13-31-54.mp4"


# Display the video
st.video(video_file)
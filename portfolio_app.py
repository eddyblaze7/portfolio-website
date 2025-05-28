
import streamlit as st

# Page config
st.set_page_config(page_title="Eddy Blaze Portfolio", layout="wide")


# Header
st.title("👨‍💻 Edmund Ashitey Amarh")
st.subheader("Python Developer | Machine Learning | GUI & Web App Enthusiast")
st.markdown("Email: niiashiteyamarh7@hotmail.com | Phone: +233 545 37 1045")
st.markdown("GitHub: [https://github.com/eddyblaze7 ] | LinkedIn: [https://linkedin.com/in/edmund-amarh-3362243b]")
st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Home", "📘 About", "💼 Projects", "🛠 Skills", "📫 Contact"])

with tab1:
    st.header("Welcome!")
    st.write("I'm Eddy Blaze, a Python Developer focused on building smart, interactive applications using ML, Streamlit, and PyQt.")
    st.write("This site highlights my professional background, skills, and project portfolio.")

with tab2:
    st.header("About Me")
    st.write("""
    I'm a Python Developer at Soko Aerial Robotics Centre with practical experience building real-world tools and ML-powered apps.

    - 🔧 I enjoy solving problems with automation and clean Python code
    - 📊 I use tools like Streamlit, PyQt, Pandas, and Scikit-learn daily
    - 🚀 Passionate about turning ideas into full-featured tools for end users
    """)

with tab3:
    st.header("Projects")

    st.subheader("🧠 Resume Classifier App")
    st.write("An ML app that predicts job roles from uploaded resumes using logistic regression.")
    st.markdown("🔗 [https://github.com/eddyblaze7/resume-classifier](#)")

    st.subheader("💰 Expense Tracker App")
    st.write("A desktop app for tracking expenses and generating charts.")
    st.markdown("🔗 [GitHub Repo](#)")

    st.subheader("🧪 Upcoming Projects")
    st.markdown("""
    - 📉 Customer Churn Predictor  
    - 🧾 PDF Organizer Tool  
    - 📊 Resume Dashboard Analyzer  
    - 📈 CSV Data Explorer  
    """)

with tab4:
    st.header("Skills")
    st.markdown("""
    - **Languages:** Python  
    - **Frameworks/Libraries:** Streamlit, Scikit-learn, PyQt6/PySide6, Pandas, NumPy, Matplotlib  
    - **Tools:** Git, VS Code, Google Colab  
    - **Databases:** SQLite  
    - **OS:** Windows  
    """)

with tab5:
    st.header("Get in Touch")
    st.markdown("""
    **📧 Email:** niiashiteyamarh7@hotmail.com  
    **📞 Phone:** +233 545 37 1045  
    **🔗 LinkedIn:** [https://linkedin.com/in/edmund-amarh-3362243b]  
    **💻 GitHub:** [https://github.com/eddyblaze7 ]
    """)

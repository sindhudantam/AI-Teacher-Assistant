# import streamlit as st
# import requests
# import pandas as pd
# import matplotlib.pyplot as plt
# from dotenv import load_dotenv
# import os

# # 🔹 Load API Key from .env file
# load_dotenv()
# API_KEY = os.getenv("HUGGINGFACE_API_KEY")
# HEADERS = {"Authorization": f"Bearer {API_KEY}"}

# # 🔹 Hugging Face Free API Model
# API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"

# # 🔹 Initialize session state to store grading history
# if "history" not in st.session_state:
#     st.session_state.history = []

# # 🔹 Streamlit UI Setup
# st.set_page_config(page_title="AI Teacher Assistant", page_icon="🎓", layout="wide")
# # st.image("assets/logo.png", width=100)
# st.image("assets/logo.png", width=100)
# st.title("📚 AI Teacher Assistant - Free AI Grading & Feedback")

# # 🔹 Sidebar navigation
# st.sidebar.title("⚡ Features")
# page = st.sidebar.radio("Go to", ["🏠 Home", "📊 Performance"])

# # 🔹 Home Page (Main Functionality)
# if page == "🏠 Home":
#     st.write("🚀 **AI-powered Grading & Personalized Feedback using Hugging Face!**")
    
#     student_answer = st.text_area("✍ Enter your answer:", height=200)
#     grading_criteria = st.text_area("🎯 Enter grading criteria:", "Clarity, relevance, grammar, and structure.")

#     if st.button("✅ Grade My Answer"):
#         if student_answer.strip():
#             with st.spinner("Grading... ⏳"):
#                 payload = {"inputs": f"Grade this answer based on: {grading_criteria}\n\n{student_answer}"}
#                 response = requests.post(API_URL, headers=HEADERS, json=payload)

#                 if response.status_code == 200:
#                     feedback = response.json()[0]["sequence"]
#                     score = len(feedback) % 10  # Sample score logic (modify as needed)

#                     # Store result
#                     st.session_state.history.append({"Answer": student_answer, "Score": score, "Feedback": feedback})

#                     st.subheader("📊 AI Feedback:")
#                     st.write(f"**Score:** {score}/10")
#                     st.write(f"**Feedback:** {feedback}")
#                 else:
#                     st.error("⚠️ Error in API request. Try again later.")
#         else:
#             st.warning("⚠ Please enter an answer before grading.")

# # 🔹 Performance Tracking Page
# elif page == "📊 Performance":
#     st.subheader("📈 Student Performance Tracker")

#     if len(st.session_state.history) > 0:
#         df = pd.DataFrame(st.session_state.history)
#         st.dataframe(df)

#         # Generate progress chart
#         fig, ax = plt.subplots()
#         ax.plot(range(1, len(df) + 1), df["Score"], marker="o", linestyle="-", color="blue")
#         ax.set_title("Performance Over Time")
#         ax.set_xlabel("Attempt")
#         ax.set_ylabel("Score")
#         st.pyplot(fig)
#     else:
#         st.warning("⚠ No past performance data available.")


# import streamlit as st
# import requests
# import pandas as pd
# import matplotlib.pyplot as plt
# from dotenv import load_dotenv
# import os

# # 🔹 Load API Key from .env file
# load_dotenv()
# API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# if not API_KEY:
#     st.error("⚠ API Key is missing! Please add it to the `.env` file.")

# HEADERS = {"Authorization": f"Bearer {API_KEY}"}
# API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"

# # 🔹 Initialize session state to store grading history
# if "history" not in st.session_state:
#     st.session_state.history = []

# # 🔹 Streamlit UI Setup
# st.set_page_config(page_title="AI Teacher Assistant", page_icon="🎓", layout="wide")

# # 🔹 Logo Handling
# logo_path = "assets/ailogo.png"
# if os.path.exists(logo_path):
#     st.image(logo_path, width=20)
# else:
#     st.warning("⚠️ Logo file not found! Make sure 'assets/logo.png' exists.")

# st.title("📚 AI Teacher Assistant - Free AI Grading & Feedback")

# # 🔹 Sidebar navigation
# st.sidebar.title("⚡ Features")
# page = st.sidebar.radio("Go to", ["🏠 Home", "📊 Performance"])

# # 🔹 Home Page (Main Functionality)
# if page == "🏠 Home":
#     st.write("🚀 **AI-powered Grading & Personalized Feedback using Hugging Face!**")
    
#     student_answer = st.text_area("✍ Enter your answer:", height=200)
#     grading_criteria = st.text_area("🎯 Enter grading criteria:", "Clarity, relevance, grammar, and structure.")

#     if st.button("✅ Grade My Answer"):
#         if student_answer.strip():
#             with st.spinner("Grading... ⏳"):
#                 payload = {"inputs": f"Grade this answer based on: {grading_criteria}\n\n{student_answer}"}
#                 response = requests.post(API_URL, headers=HEADERS, json=payload)

#                 if response.status_code == 200:
#                     try:
#                         response_json = response.json()
#                         feedback = response_json[0].get("sequence", "No feedback received.")
#                         score = len(feedback) % 10  # Sample scoring logic
#                     except (KeyError, IndexError):
#                         st.error("⚠️ Unexpected API response format. Please check the API.")
#                         feedback = "Could not generate feedback."
#                         score = 0

#                     # Store result
#                     st.session_state.history.append({"Answer": student_answer, "Score": score, "Feedback": feedback})

#                     st.subheader("📊 AI Feedback:")
#                     st.write(f"**Score:** {score}/10")
#                     st.write(f"**Feedback:** {feedback}")
#                 else:
#                     st.error("⚠️ Error in API request. Try again later.")
#         else:
#             st.warning("⚠ Please enter an answer before grading.")

# # 🔹 Performance Tracking Page
# elif page == "📊 Performance":
#     st.subheader("📈 Student Performance Tracker")

#     if len(st.session_state.history) > 0:
#         df = pd.DataFrame(st.session_state.history)
#         st.dataframe(df)

#         # Generate progress chart
#         try:
#             df["Score"] = pd.to_numeric(df["Score"], errors="coerce")  # Convert to numbers
#             df = df.dropna()  # Remove invalid entries

#             fig, ax = plt.subplots()
#             ax.plot(range(1, len(df) + 1), df["Score"], marker="o", linestyle="-", color="blue")
#             ax.set_title("Performance Over Time")
#             ax.set_xlabel("Attempt")
#             ax.set_ylabel("Score")
#             st.pyplot(fig)
#         except Exception as e:
#             st.error(f"⚠ Error generating graph: {e}")
#     else:
#         st.warning("⚠ No past performance data available.")





# import streamlit as st
# from firebase_config import signup_user, login_user, get_user_role
# from quiz_system import create_quiz, get_quizzes, attempt_quiz, grade_quiz
# from plagiarism_checker import check_plagiarism

# # Streamlit UI Setup
# st.set_page_config(page_title="AI Teacher Assistant", layout="wide")
# # st.image("assets/logo.png", width=100)
# st.title("📚 AI Teacher Assistant")

# # Authentication
# if "user" not in st.session_state:
#     st.session_state.user = None
#     st.session_state.role = None

# # Login & Signup UI
# if not st.session_state.user:
#     option = st.radio("Login or Signup", ["Login", "Signup"])
#     email = st.text_input("📧 Email")
#     password = st.text_input("🔑 Password", type="password")
#     role = st.selectbox("👤 Role", ["Student", "Teacher"]) if option == "Signup" else None
    
#     if st.button("Submit"):
#         if option == "Signup":
#             uid = signup_user(email, password, role)
#             if uid:
#                 st.session_state.user = uid
#                 st.session_state.role = role
#                 st.success("✅ Signed up successfully!")
#             else:
#                 st.error("❌ Signup failed. Try again.")
#         else:
#             uid = login_user(email, password)
#             if uid:
#                 role = get_user_role(uid)
#                 st.session_state.user = uid
#                 st.session_state.role = role
#                 st.success(f"✅ Logged in successfully as {role}!")
#             else:
#                 st.error("❌ Invalid credentials!")

# # Role-Based Dashboard
# if st.session_state.user:
#     st.sidebar.title("📌 Navigation")
    
#     if st.session_state.role == "Teacher":
#         page = st.sidebar.radio("Go to", ["Create Quiz", "Grade Assignments"])
        
#         if page == "Create Quiz":
#             create_quiz()
#         elif page == "Grade Assignments":
#             quiz_id = st.text_input("Enter Quiz ID to Grade:")
#             if quiz_id:
#                 grade_quiz(quiz_id)
    
#     elif st.session_state.role == "Student":
#         page = st.sidebar.radio("Go to", ["Attempt Quiz", "Check Plagiarism"])
        
#         if page == "Attempt Quiz":
#             quizzes = get_quizzes()
#             if quizzes:
#                 selected_quiz = st.selectbox("Choose a quiz", quizzes)
#                 if st.button("Start Quiz"):
#                     attempt_quiz(selected_quiz)
#             else:
#                 st.warning("No quizzes available.")

#         elif page == "Check Plagiarism":
#             answer = st.text_area("Enter your answer:")
#             if st.button("Check for Plagiarism"):
#                 result = check_plagiarism(answer)
#                 st.write(f"🔍 Plagiarism Score: {result}%")




import streamlit as st
from teacher_dashboard import teacher_dashboard
from student_dashboard import student_dashboard
from firebase_config import signup_user, login_user, get_user_data

st.set_page_config(page_title="AI Teacher Assistant", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Login", "Signup", "Teacher Dashboard", "Student Dashboard"])

if page == "Signup":
    st.title("Sign Up")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["Teacher", "Student"])
    department = st.selectbox("Department", ["CS", "IT", "ECE"])

    if st.button("Sign Up"):
        user_id = signup_user(email, password, role, department)
        if user_id:
            st.success("Signup successful! Now login.")
        else:
            st.error("Signup failed!")

elif page == "Login":
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user_id = login_user(email, password)
        if user_id:
            user_data = get_user_data(user_id)
            st.success(f"Welcome, {user_data['role']}!")
            st.session_state["user_id"] = user_id
            st.session_state["role"] = user_data["role"]
            st.session_state["department"] = user_data["department"]
        else:
            st.error("Login failed!")

elif page == "Teacher Dashboard":
    teacher_dashboard()
elif page == "Student Dashboard":
    student_dashboard()

import streamlit as st

quizzes = {}  # Store quizzes temporarily

# Function to create a quiz
def create_quiz():
    st.subheader("📚 Create a Quiz")
    quiz_title = st.text_input("Quiz Title")
    questions = st.text_area("Enter questions (one per line)")
    
    if st.button("Save Quiz"):
        quizzes[quiz_title] = questions.split("\n")
        st.success(f"✅ Quiz '{quiz_title}' saved!")

# Function to get available quizzes
def get_quizzes():
    return list(quizzes.keys())

# Function for students to attempt quizzes
def attempt_quiz(quiz_title):
    st.subheader(f"📝 Attempting Quiz: {quiz_title}")
    for q in quizzes[quiz_title]:
        st.text(q)
        st.text_input(f"Your answer for: {q}")

# Function to manually grade quizzes
def grade_quiz(quiz_id):
    st.subheader("✍ Grade Quiz")
    st.write("🔹 Fetch student responses and manually assign grades.")
    st.text_input("Enter Grade")
    st.button("Submit Grade")



# import streamlit as st
# from firebase_config import db

# # Function to create a quiz (Stored by department)
# def create_quiz(user_department):
#     st.subheader("📚 Create a Quiz")
#     quiz_title = st.text_input("Quiz Title")
#     questions = st.text_area("Enter questions (one per line)")
    
#     if st.button("Save Quiz"):
#         quiz_data = {
#             "title": quiz_title,
#             "questions": questions.split("\n"),
#             "department": user_department
#         }
#         db.collection("quizzes").add(quiz_data)
#         st.success(f"✅ Quiz '{quiz_title}' saved!")

# # Function to get available quizzes (Filtered by department)
# def get_quizzes(user_department):
#     quizzes_ref = db.collection("quizzes").where("department", "==", user_department).stream()
#     return {quiz.id: quiz.to_dict()["title"] for quiz in quizzes_ref}

# # Function for students to attempt quizzes
# def attempt_quiz(quiz_id, user_id):
#     quiz_doc = db.collection("quizzes").document(quiz_id).get()
    
#     if quiz_doc.exists:
#         quiz_data = quiz_doc.to_dict()
#         st.subheader(f"📝 Attempting Quiz: {quiz_data['title']}")
#         responses = {}

#         for question in quiz_data["questions"]:
#             responses[question] = st.text_input(f"Your answer for: {question}")

#         if st.button("Submit Quiz"):
#             attempt_data = {
#                 "user_id": user_id,
#                 "quiz_id": quiz_id,
#                 "responses": responses
#             }
#             db.collection("quiz_attempts").add(attempt_data)
#             st.success("✅ Quiz submitted!")

# # Function to manually grade quizzes
# def grade_quiz():
#     st.subheader("✍ Grade Quiz")
#     quiz_attempts = db.collection("quiz_attempts").stream()

#     for attempt in quiz_attempts:
#         data = attempt.to_dict()
#         st.write(f"Student ID: {data['user_id']}, Quiz ID: {data['quiz_id']}")
#         for question, answer in data["responses"].items():
#             st.write(f"Q: {question} → A: {answer}")
#         grade = st.text_input("Enter Grade")
        
#         if st.button("Submit Grade", key=attempt.id):
#             db.collection("grades").add({"user_id": data["user_id"], "quiz_id": data["quiz_id"], "grade": grade})
#             st.success("✅ Grade submitted!")

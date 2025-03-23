import streamlit as st
import uuid
from firebase_config import db

def teacher_dashboard():
    st.title("Teacher Dashboard")

    # Create Quiz
    st.subheader("Create a Quiz")
    quiz_title = st.text_input("Quiz Title")
    department = st.selectbox("Select Department", ["CS", "IT", "ECE"])
    
    questions = []
    num_questions = st.number_input("Number of Questions", min_value=1, max_value=10, step=1)

    for i in range(num_questions):
        questions.append(st.text_area(f"Question {i+1}"))

    if st.button("Publish Quiz"):
        quiz_id = str(uuid.uuid4())
        quiz_data = {
            "title": quiz_title,
            "questions": questions,
            "department": department,
            "assignedTo": [],
        }

        db.collection("quizzes").document(quiz_id).set(quiz_data)

        # Assign quiz to students in the same department
        students_ref = db.collection("users").where("department", "==", department).where("role", "==", "student").stream()
        assigned_students = [student.id for student in students_ref]
        
        db.collection("quizzes").document(quiz_id).update({"assignedTo": assigned_students})

        st.success("Quiz created and assigned to students!")

    # Grade Submissions
    st.subheader("Grade Student Submissions")
    quizzes = db.collection("quizzes").stream()
    for quiz in quizzes:
        quiz_data = quiz.to_dict()
        st.write(f"### {quiz_data['title']}")
        
        submissions = db.collection("submissions").where("quizId", "==", quiz.id).stream()
        for submission in submissions:
            sub_data = submission.to_dict()
            st.write(f"Student ID: {sub_data['studentId']}")
            for i, answer in enumerate(sub_data['answers']):
                st.write(f"Q{i+1}: {answer}")

            score = st.slider(f"Grade Submission {submission.id}", 0, 100, 50)
            if st.button(f"Submit Grade for {submission.id}"):
                db.collection("submissions").document(submission.id).update({"score": score, "graded": True})
                st.success("Grade submitted!")

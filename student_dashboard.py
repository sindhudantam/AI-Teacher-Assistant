import streamlit as st
from firebase_config import db
import uuid

def student_dashboard():
    st.title("Student Dashboard")

    student_id = st.text_input("Enter Student ID")
    
    if st.button("Fetch My Quizzes"):
        quizzes = db.collection("quizzes").where("assignedTo", "array_contains", student_id).stream()
        for quiz in quizzes:
            quiz_data = quiz.to_dict()
            st.write(f"### {quiz_data['title']}")
            answers = []
            for i, q in enumerate(quiz_data["questions"]):
                answers.append(st.text_area(f"Q{i+1}: {q}"))

            if st.button(f"Submit Answers for {quiz.id}"):
                submission_id = str(uuid.uuid4())
                db.collection("submissions").document(submission_id).set({
                    "quizId": quiz.id,
                    "studentId": student_id,
                    "answers": answers,
                    "graded": False,
                    "score": None
                })
                st.success("Answers submitted successfully!")

    if st.button("View My Grades"):
        submissions = db.collection("submissions").where("studentId", "==", student_id).stream()
        for sub in submissions:
            sub_data = sub.to_dict()
            quiz_title = db.collection("quizzes").document(sub_data["quizId"]).get().to_dict()["title"]
            st.write(f"### {quiz_title}")
            st.write(f"Score: {sub_data['score']}" if sub_data["graded"] else "Not graded yet")

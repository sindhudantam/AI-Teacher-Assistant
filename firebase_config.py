# import firebase_admin
# from firebase_admin import credentials, auth, firestore

# # Load Firebase Credentials
# cred = credentials.Certificate("config/serviceAccountKey.json")

# # Initialize Firebase App
# firebase_admin.initialize_app(cred)

# # Initialize Firestore
# db = firestore.client()

# # Function to sign up users
# def signup_user(email, password, role):
#     try:
#         user = auth.create_user(email=email, password=password)
#         # Store role in Firestore
#         db.collection("users").document(user.uid).set({"email": email, "role": role})
#         return user.uid
#     except Exception as e:
#         return str(e)

# # Function to authenticate users
# def login_user(email, password):
#     try:
#         user = auth.get_user_by_email(email)
#         return user.uid
#     except Exception as e:
#         return None

# # Function to get user role from Firestore
# def get_user_role(user_id):
#     try:
#         user_doc = db.collection("users").document(user_id).get()
#         if user_doc.exists:
#             return user_doc.to_dict().get("role", "Student")  # Default to Student
#         return "Student"
#     except Exception as e:
#         return "Student"


import firebase_admin
from firebase_admin import credentials, auth, firestore

# Load Firebase Credentials
cred = credentials.Certificate("config/serviceAccountKey.json")

# Initialize Firebase App
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Function to sign up users
def signup_user(email, password, role, department):
    try:
        user = auth.create_user(email=email, password=password)
        # Store role and department in Firestore
        db.collection("users").document(user.uid).set({"email": email, "role": role, "department": department})
        return user.uid
    except Exception as e:
        return str(e)

# Function to authenticate users
def login_user(email, password):
    try:
        user = auth.get_user_by_email(email)
        return user.uid
    except Exception as e:
        return None

# Function to get user role from Firestore
def get_user_data(user_id):
    try:
        user_doc = db.collection("users").document(user_id).get()
        if user_doc.exists:
            return user_doc.to_dict()
        return None
    except Exception as e:
        return None

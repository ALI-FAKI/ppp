from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["user_database"]
collection = db["users"]

@app.route("/", methods=["GET", "POST"])  # Ensure both GET and POST methods are allowed
def index():
    try:
        if request.method == "POST":
            print("POST request received")  # Debugging log
            # Get form data
            name = request.form.get("name")
            email = request.form.get("email")
            password = request.form.get("password")
            print(f"Form data: Name={name}, Email={email}, Password={password}")  # Debugging log
            
            # Insert into MongoDB
            collection.insert_one({"name": name, "email": email, "password": password})
            print("Data inserted into MongoDB")  # Debugging log
            return "Form submitted successfully!"
    except Exception as e:
        print(f"Error occurred: {e}")  # Debugging log
        return f"An error occurred: {e}"
    
    print("GET request received")  # Debugging log
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

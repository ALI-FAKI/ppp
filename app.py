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
            # Get form data
            name = request.form.get("name")
            email = request.form.get("email")
            password = request.form.get("password")
            
            # Insert into MongoDB
            collection.insert_one({"name": name, "email": email, "password": password})
            return "Form submitted successfully!"
    except Exception as e:
        return f"An error occurred: {e}"
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from flask_ngrok import run_with_ngrok
import db

app = Flask(__name__)
run_with_ngrok(app)

@app.route('/')
def flask_mongodb_atlas():
    return "flask mongodb atlas!"


#test to insert data to the data base
@app.route("/test")
def test():
    db.db.collection.insert_one({"name": "John"})
    return "Connected to the data base!"

if __name__ == '__main__':
    app.run()
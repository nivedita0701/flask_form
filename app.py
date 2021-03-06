from flask import Flask,render_template, url_for, request
from flask_ngrok import run_with_ngrok
import db
from forms import myForm
from wtforms import validators

app = Flask(__name__)
app.config['SECRET KEY'] = 'Thisissecret!'


run_with_ngrok(app)

@app.route('/')
def flask_mongodb_atlas():
    return "flask mongodb atlas!"


# #test to insert data to the data base
# @app.route("/test")
# def test():
#     db.db.collection.insert_one({"name": "John"})
#     return "Connected to the data base!"

@app.route('/form', methods=['GET','POST'])
def form():
    form = myForm()
    if request.method == "POST":
        db.db.collection.insert_one({"message": request.form['message']})
        return '<h1> The message is : {} '.format(request.form['message'])
    else:
        return render_template("form.html", form=form)

if __name__ == '__main__':
    app.run()
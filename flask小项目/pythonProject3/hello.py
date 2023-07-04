from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    user = {"username": '123'}
    posts = [
        {
            "author": {"username ": 'John'},
            "body": 'Beautiful day in Portland! '
        },
        {
            "author ": {"username ": 'Susan'},
            " body  ": 'The Avengers movie was so cool!'
        }
    ]
    good = [1,2,3]

    return render_template("user.html", user=user, post=posts, good=good)

if __name__ == '__main__':
    app.run(debug=True)
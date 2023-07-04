
from flask import render_template
from app import app
from app.froms import LoginForm

@app.route('/')
def test():
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

    return render_template('frist.html', user=user, post=posts, good=good)

@app.route('/login')
def login():
    login_from = LoginForm()
    return render_template('login.html', title='login', form=login_from )

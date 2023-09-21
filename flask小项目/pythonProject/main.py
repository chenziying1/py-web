from flask import Flask,render_template,session,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_mail import Mail
from flask_mail import Message

base_dir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SECRET_KEY'] = 'HARD TO GUESS WORD'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = False
app.config['FLASK_MAIL_SUBJECT_PREFIX'] = '[Flask]'
app.config['FLASK_MAIL_SENDER'] = 'Flask Admin <flasky@example.com>'
app.config['FLASK_ADMIN']=os.environ.get('FLASKY_ADMIN')

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '1060324818@qq.com'
app.config['MAIL_PASSWORD'] = 'knmqbjzbntiqbfgf'

db = SQLAlchemy(app)
migrate = Migrate(app,db)
bootstrap = Bootstrap(app)
moment = Moment(app)
mail = Mail(app)

class NameForm(FlaskForm):
    name = StringField('what is your name?',validators=[DataRequired()])
    submit = SubmitField('submit')

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known']=False
            if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASK_ADMIN'],'New User','mail/new_user',user=user)
        else:
            session['known']=True
        session['name'] = form.name.data
        form.name.data=''
        return redirect(url_for('index'))
    return render_template('login.html',form=form,name=session.get('name'),known=session.get('known',False))



@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name,current_time = datetime.utcnow())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@app.shell_context_processor
def make_shell_context():
    return dict(db=db,User=User,Role=Role)


def send_email(to,subject,template,**kwargs):
    msg = Message(app.config['FLASK_MAIL_SUBJECT_PREFIX']+subject,sender=app.config['FLASKY_MAIL_SENDER'],recipients=[to])
    msg.body=render_template(template+'.txt',**kwargs)
    msg.html=render_template(template+'.html',**kwargs)
    mail.send(msg)



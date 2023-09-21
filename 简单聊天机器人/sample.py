#开源代码，一起改进，转载请注明出处，

from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
trainer.train("data/data.yml")

@app.route("/get")
def get_bot_response():
	userText = request.args.get("msg")
	return str(english_bot.get_response(userText))

@app.route("/")
def index():
	return render_template("login.html")

if __name__ == '__main__':
	app.run(debug = True,port=8880)
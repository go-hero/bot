from flask import *
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
  return redirect(url_for("bot"))
  
@app.route('/bot')
def bot():
  return render_template(
    "bot.html",
    home=url_for("home")
    )
  
def run():
  app.run(host="0.0.0.0",port=8080)
  
def keep_alive():
  t = Thread(target=run)
  t.start()

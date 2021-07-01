from flask import *
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
  return redirect(url_for("bot"))
  
@app.route('/bot', methods=['GET','POST'])
def bot():
  return render_template(
    "bot.html",
    home=url_for("home"),
    )

@app.route('/invite')
def invite():
  return redirect("https://discord.com/api/oauth2/authorize?client_id=857634436584570920&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.gg%2FpwMQ3wrf3e&response_type=code&scope=bot%20applications.commands%20guilds.join")

def run():
  app.run(host="0.0.0.0",port=8080)
  
def keep_alive():
  t = Thread(target=run)
  t.start()

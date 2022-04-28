from flask import *
from dotenv import load_dotenv, dotenv_values
from api.message_api import app1

env=str('.env.'+dotenv_values('.env')["MODE"])
load_dotenv(override=True)

app=Flask(__name__)
app.config["JSON_AS_ASCII"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True

@app.route("/")
def index():
    return render_template("index.html")

app.register_blueprint(app1, url_prefix="/api")

app.debug=True
app.run(host=dotenv_values(env)["app_host"], port=4000)
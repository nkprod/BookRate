import os

from flask import Flask, session, render_template
from flask_login import current_user, LoginManager
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html", title="Home")

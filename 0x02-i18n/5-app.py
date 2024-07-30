#!/usr/bin/env python3
""" Define Flask-Babel Module """
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """ Configration class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = ["UTC"]

app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """ Select language based on user prefrences """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user():
    """ Returns a use dictionary or None"""
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None

@app.before_request
def before_request():
    """ Set user before each request """
    g.user = get_user()

@app.route('/')
def index() -> str:
    """ render index.html """
    username = g.user.get('name') if g.user else None
    return render_template('5-index.html', username=username)


if __name__ == "__main__":
    app.run(debug=True)

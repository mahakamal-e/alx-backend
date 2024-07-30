#!/usr/bin/env python3
"""Define Flask-Babel Module"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


class Config:
    """Configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


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
    """Select language based on user preferences"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ find timezone """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone).zone
        except pytz.UnknownTimeZoneError:
            return app.config['BABEL_DEFAULT_TIMEZONE']
    
    user_timezone = g.user.get("timezone")
    if user_timezone:
        return user_timezone
    return app.config['BABEL_DEFAULT_TIMEZONE']


def get_user():
    """Returns a user dictionary or None"""
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """Set user before each request"""
    g.user = get_user()


@app.route('/')
def index() -> str:
    """Render index.html"""
    username = g.user.get('name') if g.user else None
    return render_template('6-index.html', username=username)


if __name__ == "__main__":
    app.run(debug=True)

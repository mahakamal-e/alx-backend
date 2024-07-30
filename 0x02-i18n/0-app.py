#!/usr/bin/env python3
"""Setup a basic Flask app."""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """Route index.html"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)

# 0x02. i18n

## Project Overview

This project involves implementing internationalization (i18n) and localization (l10n) in a Flask application. The goal is to display different languages in Flask templates, infer the correct locale based on various parameters, and localize timestamps.

### Learning Objectives

- **Parametrize Flask Templates**: Use Flask-Babel to display different languages in your templates.
- **Infer the Correct Locale**: Determine the locale based on URL parameters, user settings, or request headers.
- **Localize Timestamps**: Format and display timestamps according to the user's locale.

### Resources

- [Flask-Babel Documentation](https://python-babel.github.io/flask-babel/)
- [Flask i18n Tutorial](https://flask-babel.tuxfamily.org/)
- [pytz Documentation](https://pytz.sourceforge.net/)

### Requirements

- **Python Version**: 3.7
- **Operating System**: Ubuntu 18.04 LTS
- **Style Guide**: Follow the [pycodestyle](https://pycodestyle.pycqa.org/) style (version 2.5)
- **File Requirements**:
  - All files must end with a new line.
  - The first line of all Python files should be `#!/usr/bin/env python3`.
  - All `*.py` files should be executable.
  - Each module, class, and function should have proper documentation.
  - All functions and coroutines must be type-annotated.

### Setup Instructions

1. **Install Flask and Flask-Babel**:
   ```bash
   pip install Flask Flask-Babel

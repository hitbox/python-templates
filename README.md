# Opinionated Python Templates

[Scheduled Tasks](schedule.md)

[Code Repository](repos.md)

[Web Apps](www.md)

## Common command line and Scheduled Task template

[service.py](service.py)

A base template of what I often do for a service script that will run on a schedule.

[config.ini](config.ini)

Simple base configuration file

## Virtual Environment

Projects are kept independent in virtual environments. Even if they have no external dependencies.

```sh
# create virtual environment
python -m venv venv
# activate virtual environment
source venv/Script/activate
# upgrade this pip immediately and whenever it prompts you
python -m pip install --upgrade pip
```

## External Dependencies

A `requirements.txt` file for dependencies is working fine for me.

I avoid external dependencies but some I install without hesitation. Things like:

- [Flask](https://flask.palletsprojects.com)
- [Requests](https://requests.readthedocs.io)
- [SQLAlchemy](https://www.sqlalchemy.org)
- [WTForms](https://wtforms.readthedocs.io)
- [marshmallow](https://marshmallow.readthedocs.io)

If a major project like these, or Python itself, is incompatible with the code I've written, I fix my code.

My general strategy has been to develop an application, keeping the dependencies updated to their newest version. Deploy with newest Python and dependencies in a virtual environment which locks everything down in production. Then, when the app needs any work, I pull it up in a development environment and update everything and fix any problems; and then do my work on the app.

I've pinned version numbers before but I don't like it. I want the updates from the major projects and if that means a lesser project is now incompatble then it has to go.

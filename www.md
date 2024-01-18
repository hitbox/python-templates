# Web Apps

- [Flask](https://flask.palletsprojects.com)
- [SQLAlchemy](https://www.sqlalchemy.org)
- [WTForms](https://wtforms.readthedocs.io)

## Flask Directory Structure

└── projectname/
    ├── app.py .............. App factory, hook up blueprints and extensions
    ├── extensions.py ....... Create Flask extensions
    ├── forms.py ............ All forms
    ├── models.py ........... Database models
    ├── static/
    │   ├── site.css ........ Styles
    │   └── site.js ......... Code
    ├── templates
    │   ├── base.html ....... Inherits skeleton.html, every other template should inherit this.
    │   └── skeleton.html ... Bare minimum html template.
    └── views.py ............ Blueprints for routes/views and Flask subcommands

- Pluggable views can be difficult to make and worth the effort.
- WTForms probably has what you want.
- Avoid blueprint templates, paths become painfully long.
- Prefer keeping subfolders for blueprints in normal templates folder.
- `source`-able file for populating environment variables in the instance dir.
- Prefer doing as little as possible in templates. Mostly just loop over data structures and render attributes; or very simple flow control.


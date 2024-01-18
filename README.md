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

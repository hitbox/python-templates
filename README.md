# Opinionated Python Templates

## Common command line and Scheduled Task template

[service.py](service.py)

A base template of what I often do for a service script that will run on a schedule.

[config.ini](config.ini)

Simple base configuration file

## Git for Windows

Excellent project that, like Python itself, smooths over a lot of the differences between Windows and Unix-likes. It provides a nearly complete Bash command line experience.

Take care to know when to use `winpty`. You can hang the window.

## New Machine SSH Key

```sh
cat ~/.ssh/id_rsa.pub > /dev/clipboard
```

Then paste into your repo host configuration.

## instance directory

Sensitive configuration and logging goes in the instance directory. The name comes from Flask. It is never committed to the repo.

```sh
git init
echo instance >> .gitignore
echo venv >> .gitignore
```

- usernames and passwords
- email addresses
- paths to files

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

## Scheduled Tasks

- prefer keeping name of project short
- repository and main file (or directory) are often the same
- use the virtual environment

  in the "Program/script" textbox:
  `c:\repos\project\venv\Scripts\pythonw.exe`

  "Add arguments (optional)"
  `service.py instance/config.ini`
  (or for a module)
  `-m service instance/config.ini`

  "Start in (optional)" textbox:
  `c:\repos\project\`

  Making the current directory ("State in") allows intuitive relative paths like you would have in Bash.

  Note the "w" in `pythonw.exe`. This prevents command windows from popping up.

- As little as possible in the scheduled task to get the program to run. Debugging a scheduled task is very difficult for lack of output capturing. If the program is not running, you want to be able to drop down into a shell and run it like the scheduled task does. Hopefully the problem is in the script.
- Prefer, if you can, running the task as the same user you developed under.

- If many changes are needed, it is easier to:

1. export to XML
2. edit
3. remove existing tasks
4. import updated XML

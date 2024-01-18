# Scheduled Tasks

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

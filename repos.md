# Code Repository

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

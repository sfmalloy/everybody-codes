# Event 1 Solutions

These are my solutions to Event 1 - [*The Kingdom of Algorithmia*](https://everybody.codes/event/1/quests) written in Python.

## Running

This project uses `uv`. Simply create a virtual environment using `uv venv` and you're good to go! There are no outside dependencies as of now.

There is a simple command-line interface used to run various quest solutions. Below is all the flags available to use.

```plaintext
usage: main.py [-h] -q QUEST [-p PART] [-a] [-f FILE] [-g] [-t]

options:
  -h, --help         show this help message and exit
  -q, --quest QUEST  Runs quest <q>. If -f is not specified, default uses input file from a quest's directory
  -p, --part PART    Runs a specific part
  -a, --all          Run all quests
  -f, --file FILE    Specify different input file from default
  -g, --generate     Generate template solution file for given quest
  -t, --test         Shorthand for "-f test.txt"
```

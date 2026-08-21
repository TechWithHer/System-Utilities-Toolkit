# What I learned:

1. Python "import subprocesses"
Python subprocess is a tool built into Python that lets you run other programs directly from your Python code.Think of it like opening your computer's terminal (or Command Prompt) and typing a command, but Python does it for you automatically.

2. 1. Python can execute Bash scripts : subprocess.run(...) --> can launch:
````
bash scripts/disk-usage-analyzer.sh
````
So Python can act as the CLI controller/orchestrator, while Bash performs the Linux operation.

3. capture_output=True changes the CLI experience

We initially had: capture_output=True

That captures the output instead of letting the Bash script interact naturally with the terminal. For an interactive CLI tool, we learned that:
````
subprocess.run(command, shell=True, check=True)
````
is more appropriate.
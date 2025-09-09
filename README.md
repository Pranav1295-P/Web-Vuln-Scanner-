# Web-Vuln-Scanner-
This is open-source web vulnerability scanner. This is applicable for only demo. This is basically a beta version we are working more with respect to this . Hope this helps you. Regards, Pranav Murthy


Used items:
1. Folders: Hackathon > web-vuln-scanner > app.py > scanner.py > _pychache_ > venv
2. scanner.cpython-311 - is the PYC file A .pyc file is a compiled Python file containing bytecode. When a Python source file (.py) is executed or imported as a module, the Python interpreter compiles it into this bytecode, which is then saved as a .pyc file. This process is primarily done for optimization purposes.
3. Key characteristics of .pyc files:
Bytecode Representation:
They contain the compiled bytecode, a low-level, platform-independent representation of the Python source code.
Automatic Generation:
The Python interpreter automatically generates .pyc files when a .py file is run or imported, typically storing them in a __pycache__ subdirectory.
Faster Execution:
The main purpose of .pyc files is to speed up subsequent executions or imports of the same module. By having the bytecode readily available, the interpreter can skip the compilation step, leading to faster startup times.
Not Human-Editable:
.pyc files are in a binary format and are not intended for direct human editing.
Invalidation:
The Python interpreter checks the modification timestamp of the source (.py) file against the .pyc file. If the source file has been modified, the .pyc file is recompiled to ensure the bytecode is up-to-date.
deployed at streamlit.

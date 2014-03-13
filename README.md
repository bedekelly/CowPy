CowPy
=====

###A basic implementation of the *nix "tool" cowsay in Python.
#####Usage:
cow.py \<message\>

###Suggestions:
To be able to run this as "cowpy <message>" from anywhere, do the following:
#####Windows/CMD:
Create a batch file with the following line, somewhere that's in your PATH environment variable, and name it "cowpy.bat".
```
python /path/to/cow.py %* :: Change this to python3 if necessary.
```

#####Bash (Linux/CygWin):
Edit your ~/.bashrc file to include the following line:
```
alias cowpy='python /path/to/cow.py'
```

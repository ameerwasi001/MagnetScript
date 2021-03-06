print("""Thanks for using MagnetScript. To make your simulations as fast as possible you can use this program you can run various commands to help you get your files executed, commands ran and much more. Consider typing 'help()' for help""")
print("Loading dependencies...")
from functions import *
import os
import tokens
from traceback import print_tb, format_exception
print('Loaded!!!')

def file(path):
    directory = os.path.dirname(os.path.realpath(os.path.abspath(path)))
    file = open(path, "r+")
    lines = file.readlines()
    linenum = 0
    while(linenum<len(lines)):
        lines[linenum] = tokens.tokenize(lines[linenum], directory=relpath(path))
        linenum+=1
    content = '\n'.join(lines)
    exec(content)

def libraries():
    print("""Numpy
Scipy
Magpylib
Seaborn
Astropy
EinsteinPy
Galgebra
Skimage
Matplotlib
""")

def help():
    print("""
Following are the all the commands that are avalible except the ones built into the functions.py

libraries() -This command shows you all libraries that are used in fuctions.py and are loaded into this at the start of this program's execution

file() -This command can execute your file and takes a single argument that being the path to the file

terminal() -This command executes commands directly on your terminal so that you wouldn't have to exit and enter program repeatedly.

exit() or quit() -Used simply to exit or quit the program. """)

def terminal(command):
        os.system(command)

while True:
    given = input('>>>')
    given = tokens.tokenize(given)
    try:
        exec(given)
    except Exception as error:
        print(''.join(format_exception(etype=type(error), value=error, tb=error.__traceback__)))

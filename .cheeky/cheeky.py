#!python3
version = "v1"
import sys
import os 
import interpreter
os.environ["version"] = "v1.0.0"
file = sys.argv[1]
print("CheekyScript version:", os.getenv('version'))
print ("Running file:", file)
interpreter.interpret(file, False)
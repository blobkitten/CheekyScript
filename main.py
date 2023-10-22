version = "v0.0.1"
import sys
import os 

os.environ["version"] = "v0.0.1"
file = sys.argv[1]
print("CheekyScript version:", os.getenv('version'))
print ("Running file:", file)
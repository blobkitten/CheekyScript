import sys
import os
import math
import buffer

def interpret(file, DEBUG):
    with open(file, 'r') as f:
        for line in f:
            parts = line.split(",")
            cmd = parts[0]
            arg = parts[1]
            if DEBUG == True:
                print("Command:", cmd, "Argument:", arg)
            if cmd == "echo" and "var" in arg:
              vartitle = arg.split(" ")[1].replace(" ", "").replace("\n", "")
              print(buffer.variables[vartitle].replace('"', ''))
            if cmd == "echo" and "var" not in arg:
             print(arg.replace('"', ''))
            if "add int" in cmd:
              cmdpartsint = cmd.split(" ")
              cmdpartsint[2] = cmdpartsint[2].replace(" ", "")
              argpartsint = arg.split(" ")
              argpartsint[1] = argpartsint[1].replace(" ", "")
              print(int(cmdpartsint[2]) + int(argpartsint[1]))
            if "sub int" in cmd:
              cmdpartsint = cmd.split(" ")
              cmdpartsint[2] = cmdpartsint[2].replace(" ", "")
              argpartsint = arg.split(" ")
              argpartsint[1] = argpartsint[1].replace(" ", "")
              print(int(cmdpartsint[2]) - int(argpartsint[1]))
            if "div int" in cmd:
              cmdpartsint = cmd.split(" ")
              cmdpartsint[2] = cmdpartsint[2].replace(" ", "")
              argpartsint = arg.split(" ")
              argpartsint[1] = argpartsint[1].replace(" ", "")
              print(int(cmdpartsint[2]) / int(argpartsint[1]))
            if "times int" in cmd:
              cmdpartsint = cmd.split(" ")
              cmdpartsint[2] = cmdpartsint[2].replace(" ", "")
              argpartsint = arg.split(" ")
              argpartsint[1] = argpartsint[1].replace(" ", "")
              print(int(cmdpartsint[2]) * int(argpartsint[1]))
            if "square int" in cmd:
              cmdpartsint = cmd.split(" ")
              cmdpartsint[2] = cmdpartsint[2].replace(" ", "")
              print(int(cmdpartsint[2]) ** 2)
            if "sqr int" in cmd:
              cmdpartsint = cmd.split(" ")
              cmdpartsint[2] = cmdpartsint[2].replace(" ", "")
              print(math.sqrt(int(cmdpartsint[2])))
            if "var" in cmd:
              cmdpartsvar = cmd.split(" ")
              var_name = cmdpartsvar[1].replace(" ", "")
              var_value = arg.replace(" ", "")
              buffer.variables[var_name] = var_value
            
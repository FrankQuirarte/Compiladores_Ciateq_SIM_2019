#!/usr/bin/python
import os
#creating the output file
new_file = open("class2_preprocessed.c", "w+")
#list to save the variables names and values
defines_list = {}
#global variables
DebugMessage = True
#-------------------------------------------------------------------------------------------------
print("**********Running Frank´s C preprocessor**********************")
def include_file(file_name):
    try:
        f = open(file_name, "r")
        file = f.readlines()
        for line in file:
            new_file.write(line)
        new_file.write("\n")  # Insert newline at the end of file'
        f.close()
    except FileNotFoundError:
        print("Error: Can't find include file \"%s\" " %file_name)
#-------------------------------------------------------------------------------------------------
with open("class2.c", "r") as fd:
    archivo = fd.readlines()


for lineIndex, line in enumerate(archivo, start=1):
#-------------------------------------------------------------------------------------------------
    if line.startswith("#include "):
        line = line.rstrip()  # removing trailing space
        if ((line[9] == "<" and line[-1] == ">") or (line[9] == "\"" and line[-1] == "\"")):
            name = ""
            for c in line[10:-1]:
                if (c != '/') and (c != '\\'):
                    name = name + c
            if DebugMessage:
                print("Name: ", name)
            include_file(name)  
        else:
            print("Error: Syntax error in #include at line: %d\n" %lineIndex)
#-------------------------------------------------------------------------------------------------
    elif line.startswith("#define "):
        line = line.rstrip()  # removing trailing space
        var_name = ""
        value = ""
        for charIndex, c in enumerate(line[8:], start=8):
            if c != ' ':  # stops when it finds a blank space
                var_name = var_name + c
            else:
                break  
        for c in line[charIndex + 1:]:
            value = value + c
        defines_list[var_name] = value
        if DebugMessage:
            print("[%s] = %s" % (var_name, defines_list[var_name]))
#-------------------------------------------------------------------------------------------------
    elif line.startswith("#undef "):
        line = line.rstrip()  # removing trailing space
        var_name = ""
        value = ""
        for charIndex, c in enumerate(line[7:], start=7):
            if c != ' ':  # stops when it finds a blank space
                var_name = var_name + c
            else:
                break  
        for c in line[charIndex + 1:]:
            value = None
        defines_list[var_name] = value
#-------------------------------------------------------------------------------------------------
    elif line.startswith("#if "):
        print("#if found TBF.... ")
        continue
#-------------------------------------------------------------------------------------------------
    elif line.startswith("#else "):
        print("#else found TBF.... ")
        continue
#-------------------------------------------------------------------------------------------------
    elif line == "#endif":
        print("#enfif found TBF.... ")
        continue
#-------------------------------------------------------------------------------------------------

fd.close()
new_file.close()
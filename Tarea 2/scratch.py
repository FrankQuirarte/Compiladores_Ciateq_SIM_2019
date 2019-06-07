#!/usr/bin/python
import os
#creating the output file
new_file = open("class2_preprocessed.c", "w+")
#list to save the variables names and values
defines_list = {}
#global variables
DebugMessage = None
if_reached = False
else_reached = False
if_condition = False
else_condition = False

print("**********Running Frank´s C preprocessor**********************")
def include_file(file_name):
    try:
        f = open(file_name, "r")
        file = f.readlines()
        for line in file:
            new_file.write(line)
        new_file.write("\n")  # Inserts a newline at the end of file'
        f.close()
    except FileNotFoundError:
        print("Error: Can't find include file \"%s\" " %file_name)

def replace_var(text):
	for var in defines_list:
		i = text.find(var)
		if i > -1: # It was found
			text = text.replace(var, defines_list[var])
	return text

def find_var(line):
    out_of_string = ""
    new_line = ""
    inside_of_string = False
    if "\"" in line:
        for c in line[:]:
            if c != "\"":
                out_of_string = out_of_string + c
            else:
                if not inside_of_string:  # First "
                    inside_of_string = True
                    out_of_string = replace_var(out_of_string)
                    new_line = new_line + out_of_string
                    out_of_string = "\""
                else:  # Last "
                    inside_of_string = False
                    new_line = new_line + out_of_string + "\""
                    out_of_string = ""
        if out_of_string:
            out_of_string = replace_var(out_of_string)
            new_line = new_line + out_of_string
    else:
        new_line = replace_var(line)
    return new_line

with open("class2.c", "r") as fd:
    archivo = fd.readlines()

for lineIndex, line in enumerate(archivo, start=1):
#-------------------------------------------------------------------------------------------------
    if line.startswith("#include "):
        line = line.rstrip()  # removing trailing space
        if ((line[9] == "<" and line[-1] == ">") or (line[9] == "\"" and line[-1] == "\"")):
            name = ""
            for c in line[10:-1]:
                if (c != '/' and c != '\\'):
                    name = name + c
                else:
                    if c == '/':
                        name = name + "//"  # escape slash
                    else:
                        name = name + "\\"  # escape slash
            #if DebugMessage: print("Name: ", name)
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
        #if DebugMessage: print("[%s] = %s" % (var_name, defines_list[var_name]))
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
        if_reached = True
        if_var = ""
        if_value = ""
        for lineIndex, c in enumerate(line[4:], start=4):
            if (c != ' ' and c != '='): # continues until finds white space or simple "="
                if_var = if_var + c
            else:
                break
        if line[lineIndex + 2] == ' ':
            lineIndex = lineIndex + 3 #ignores white space
        else:
            lineIndex = lineIndex + 2 #no space between "if" and ""==""
        for c in line[lineIndex:]:
            if_value = if_value + c #saves if_value to compare with existing defines_list

        try:
            if defines_list[if_var] == if_value:
                if_condition = True

        except KeyError:
            print("Undefined variable: %s at line %d" % (if_var, i))
#-------------------------------------------------------------------------------------------------
    elif line.startswith("#else "):
        if if_reached:
            else_reached = True
            if_reached = False
        if not if_condition:
            else_condition = True
        else:
            print("Error: No #if detected before line %d" %i)
#-------------------------------------------------------------------------------------------------
    elif line == "#endif":
        if (if_reached or else_reached):
            if_reached = False
            else_reached = False
#-------------------------------------------------------------------------------------------------
    elif line.startswith("//") or not line:  # Checks for comments or empty lines
        new_file.write(line + "\n")
#-------------------------------------------------------------------------------------------------
    elif not line.startswith("#"):
        if (not if_reached and not else_reached):
            line = find_var(line)
            new_file.write(line + "\n")
        else:
            if (if_reached and if_condition):
                line = find_var(line)
                new_file.write(line + "\n")
            elif (else_reached and else_condition):
                line = find_var(line)
                new_file.write(line + "\n")
            else:
                continue
#-------------------------------------------------------------------------------------------------

fd.close()
new_file.close()
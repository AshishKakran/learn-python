#!/usr/bin/python3

#This program implements a simple version of cat command

#usage ./Cat.py < inputFile > OutputFile , this execution copies the file

while True:
    try:
        line=input()
        print(line)
    except EOFError:
        break
    

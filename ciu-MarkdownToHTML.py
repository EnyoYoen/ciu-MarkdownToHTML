# -*- coding: utf-8 -*-

from os import system, path, name
import markdown
import codecs

def retrieveRepo():
    if name == "posix":
        copy = "cp -r splendor coding-interview-university"
        rmdir = "rm -r"
        gitpath = "git"
    elif name == "nt":
        copy = "xcopy splendor coding-interview-university\splendor /E /i /q"
        rmdir = "rmdir /S /Q"
        gitpath = "\"C:\Program Files\Git\cmd\git\""

    dirpath = path.dirname(__file__)
    system(rmdir + " coding-interview-university")
    system("cd " + dirpath)
    system(gitpath + " clone https://github.com/jwasham/coding-interview-university.git")
    system(copy)

def convert():
    dirpath = path.dirname(__file__)
    with codecs.open("coding-interview-university/README.md", "r", encoding='utf-8') as mdf:
        text = mdf.read()
        html = markdown.markdown(text)
    
    html = "<link rel=\"stylesheet\" href=\"splendor/css/splendor.css\">" + html

    with codecs.open(dirpath + "/coding-interview-university/README.html", "w", encoding='utf-8') as htmlf:
        htmlf.write(html)

def ciu():
    retrieveRepo()
    convert()

ciu()
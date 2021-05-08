# -*- coding: utf-8 -*-

from os import system, path, name
import markdown
import codecs

def retrieveRepo():
    if name == "posix":
        copy = "cp -r splendor-master coding-interview-university"
        gitpath = "git"
    elif name == "nt":
        copy = "xcopy splendor-master coding-interview-university\splendor-master /E /i /q"
        gitpath = "\"C:\Program Files\Git\cmd\git\""

    dirpath = path.dirname(__file__)
    system("cd " + dirpath)
    system(gitpath + " clone https://github.com/jwasham/coding-interview-university.git")
    system(copy)

def convert():
    dirpath = path.dirname(__file__)
    with codecs.open("coding-interview-university/README.md", "r", encoding='utf-8') as mdf:
        text = mdf.read()
        html = markdown.markdown(text)
    
    html = "<link rel=\"stylesheet\" href=\"splendor-master/css/splendor.css\">" + html

    with codecs.open(dirpath + "/coding-interview-university/README.html", "w", encoding='utf-8') as htmlf:
        htmlf.write(html)

def ciu():
    retrieveRepo()
    convert()

ciu()
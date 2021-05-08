# -*- coding: utf-8 -*-

from os import system, path, name
import markdown
import codecs

def retrieveRepo():
    if name == "posix":
        copy = "cp -r splendor coding-interview-university"
        rmdir = "rm -r coding-interview-university"
        git = "git clone https://github.com/jwasham/coding-interview-university.git"
    elif name == "nt":
        copy = "xcopy splendor coding-interview-university\splendor /E /i /q"
        rmdir = "rmdir /S /Q coding-interview-university"
        git = "\"C:\Program Files\Git\cmd\git\" clone https://github.com/jwasham/coding-interview-university.git"

    dirpath = path.dirname(__file__)
    system(rmdir)
    system("cd " + dirpath)
    system(git)
    system(copy)

def convert():
    with codecs.open("coding-interview-university/README.md", "r", encoding='utf-8') as mdf:
        text = mdf.read()
        html = markdown.markdown(text)
    
    html = "<link rel=\"stylesheet\" href=\"splendor/css/splendor.css\">" + html

    with codecs.open(coding-interview-university/README.html", "w", encoding='utf-8') as htmlf:
        htmlf.write(html)

retrieveRepo()
convert()
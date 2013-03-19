import shelve
from os import path
from cPickle import HIGHEST_PROTOCOL
from contextlib import closing

from flask import Flask

from skill import Skill

SHELVE_DB = 'whos_got_what.db'

app = Flask(__name__)
app.config.from_object(__name__)

db = shelve.open(path.join(app.root_path, app.config['SHELVE_DB']),
    protocol=HIGHEST_PROTOCOL, writeback=True)

def populate_db():
    skills = dict()
    skills['programming'] = 
        Skill('programming', 'The act of writing computer programs')
    skills['C#'] = Skill('C#', 'A general purpose strongly typed class-based \
        object-oriented programming language with characteristics of C++ and Java \
        and support for namespacing, delegates, and generics')
    skills['C#'].associated_skills.append(skills['programming'])
    skills['Python'] = Skill('Python', 'A general purpose dynamically typed with support \
        for both object-oriented and structured programming.')
    skills['Python'].associated_skills.append(skills['programming'])

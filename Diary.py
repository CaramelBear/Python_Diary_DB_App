import datetime

from collections import OrderedDict
from peewee import *

db = MySQLDatabase('dev',user="root",password='kjoshi31')



class Entry(Model):
    #content
    content = TextField()
    #timestamp
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def initialize():
    """ create db and table if they dont exist"""
    db.connect()
    db.create_tables([Entry],safe = True)


def menu_loop():
    """ show the menu """
    choice = None

    while choice != 'q':
        print("Enter q to quite.")
        for key, value in menu.items():
            print('{}) {}'.format(key,value.__doc__))
        choice = input('Action: '.lower().strip())

        if choice in menu:
            menu[choice]()

def add_entry():
    """ Add an entry """

def view_entries():
    """ View previoes entries"""

def delete_entry(entry):
    """ Delete an entry """


menu = OrderedDict([
    ('a',add_entry),
    ('v',view_entries),
])


if __name__ == "__main__":
    initialize()
    menu_loop()

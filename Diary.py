import datetime
import sys
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
    """Create db and table if they dont exist"""
    db.connect()
    db.create_tables([Entry],safe = True)


def menu_loop():
    """Show the menu """
    choice = None

    while choice != 'q':
        print("Enter q to quite.")
        for key, value in menu.items():
            print('{}) {}'.format(key,value.__doc__))
        choice = input('Action: '.lower().strip())

        if choice in menu:
            menu[choice]()

def add_entry():
    """Add an entry"""
    print("Enter your entry. press ctrl+d when finished")
    data = sys.stdin.read().strip()

    if data:
        if input('Save Entry? [Y/n] ').lower() != 'n':
            Entry.create(content = data)
            print("Saved successfully!")

def view_entries(search_query=None):
    """View previoes entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())

    if search_query:
        entries = entries.where(Entry.content.contains(search_query))

    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d %Y %I:%M%p')
        print(timestamp)
        print('='*len(timestamp))
        print(entry.content)
        print('n) next entry')
        print('q) return to main menu' )

        next_action = input('Action: [N/q]').lower().strip()
        if next_action == 'q':
            break

def search_entries():
    """Search entries for a string"""
    view_entries(input("Search query: "))

def delete_entry(entry):
    """Delete an entry """


menu = OrderedDict([
    ('a',add_entry),
    ('v',view_entries),
    ('s', search_entries)
])


if __name__ == "__main__":
    initialize()
    menu_loop()

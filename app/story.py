import datetime
import json

class Story:
    def __init__(self, start_location=None, start_time=None, events=None, connections=None):
        self.start_location = start_location
        self.start_time = start_time

        self.events = events
        self.connections = connections

    def add_event(self, event):
        self.events.append(event)

class Connection:
    def __init__(self, connection_type=None):
        self.connection_type = connection_type

class Event:
    def __init__(self, location=None, starting_time=None, ending_time=None):
        self.location = location
        self.starting_time = starting_time
        self.ending_time = ending_time
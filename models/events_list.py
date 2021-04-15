from models.event import *

event_1 = Event("12/11/2021", "Wedding", 50, "Gretna Green", "Peng")
event_2 = Event("15/11/2020", "Football Match", 2000, "Anfield", "Not so peng", True)
event_3 = Event("17/03/2021", "Festival", 20000, "T in the Park", "Overly peng", True)

events = [event_1, event_2, event_3]

def add_event(event):
    events.append(event)


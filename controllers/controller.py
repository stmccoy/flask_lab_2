from app import app
from flask import render_template, request
from models.events_list import events, add_event
from models.event import Event

@app.route('/')
def index():
    return render_template('index.html', events=events)

# @app.route('/form')
# def form():
#     return render_template('form.html')

@app.route('/', methods=['POST'])
def submit_form():
    event_date = request.form['date']
    event_name = request.form['name']
    event_num_of_guests = request.form['num_of_guests']
    event_room_location = request.form['room_location']
    event_description = request.form['description']
    event_recurrance = request.form['recurring']
    new_event = Event(event_date, event_name, event_num_of_guests, event_room_location, event_description, event_recurrance)
    add_event(new_event)
    return render_template('index.html', events=events)
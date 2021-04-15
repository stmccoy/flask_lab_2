class Event:

    def __init__(self, date, name, num_of_guests, room_location, description, recurring=False):
        self.date = date
        self.name = name
        self.num_of_guests = num_of_guests
        self.room_location = room_location
        self.description = description
        self.recurring = recurring
    


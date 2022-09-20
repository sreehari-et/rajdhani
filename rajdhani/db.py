"""
Module to interact with the database.
"""

from . import placeholders
from . import db_ops
import json

db_ops.ensure_db()


def search_stations(q):
    """Returns the top ten stations matching the given query string.

    This is used to get show the auto complete on the home page.

    The q is the few characters of the station name or
    code entered by the user.
    """
    # TODO: make a db query to get the matching stations
    # and replace the following dummy implementation
    return placeholders.AUTOCOMPLETE_STATIONS
def get_dynamic_query(ticket_class):
    if(ticket_class=="SL"):
        return "and sleeper =1"
    elif(ticket_class=="3A"):
        return "and third_ac =1"
    elif(ticket_class=="2A"):
        return "and second_ac =1"
    elif(ticket_class=="1A"):
        return "and first_ac =1"
    elif(ticket_class=="FC"):
        return "and first_class =1"
    elif(ticket_class=="CC"):
        return "and chair_car =1"
    else:
        return ""

def search_trains(
        from_station_code,
        to_station_code,
        ticket_class,
        departure_date=None,
        departure_time=[],
        arrival_time=[]):
    """Returns all the trains that source to destination stations on
    the given date. When ticket_class is provided, this should return
    only the trains that have that ticket class.

    This is used to get show the trains on the search results page.
    """
    
    
    dynamic_query=get_dynamic_query(ticket_class)
    col,trains_data=db_ops.exec_query(f"select number,name,from_station_code,from_station_name,to_station_code,to_station_name,departure,arrival,duration_h,duration_m from train where from_station_code like '%{from_station_code}%' and to_station_code like '%{to_station_code}%'{dynamic_query};")
    # TODO: make a db query to get the matching trains
    # and replace the following dummy implementation
    array_data= [ {
        "number":i[0],
        "name": i[1],
        "from_station_code": i[2],
        "from_station_name": i[3],
        "to_station_code": i[4],
        "to_station_name": i[5],
        "departure":i[6],
        "arrival": i[7],
        "duration_h":i[8],
        "duration_m": i[9]
        } for i in trains_data]
    print(array_data)
    return array_data


def get_schedule(train_number):
    """Returns the schedule of a train.
    """
    return placeholders.SCHEDULE

def book_ticket(train_number, ticket_class, departure_date, passenger_name, passenger_email):
    """Book a ticket for passenger
    """
    # TODO: make a db query and insert a new booking
    # into the booking table

    return placeholders.TRIPS[0]

def get_trips(email):
    """Returns the bookings made by the user
    """
    # TODO: make a db query and get the bookings
    # made by user with `email`

    return placeholders.TRIPS


"""
Module to interact with the database.
"""

from . import placeholders
from . import db_ops
import json
from datetime import datetime

db_ops.ensure_db()


def search_stations(q):
    """Returns the top ten stations matching the given query string.

    This is used to get show the auto complete on the home page.

    The q is the few characters of the station name or
    code entered by the user.
    """

    col, rows = db_ops.exec_query(f"select code ,name from station where name like '%{q}%'")
    array_data= [ {
        "code":i[0],
        "name": i[1],
       
        } for i in rows]
    print("-----search_stations-----",array_data)
    # TODO: make a db query to get the matching stations
    # and replace the following dummy implementation
    return array_data
search_stations("sr")    
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
    slot1 = datetime.strptime('00:00:00', '%H:%M:%S')

    slot2 = datetime.strptime('08:00:00', '%H:%M:%S')

    slot3 = datetime.strptime('12:00:00', '%H:%M:%S')

    slot4 = datetime.strptime('16:00:00', '%H:%M:%S')

    slot5 = datetime.strptime('20:00:00', '%H:%M:%S')
    
    
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
    

    if len(departure_time)>0 or len(arrival_time)>0:
        new_train_data=[]
        for data in array_data:
            for slot in departure_time:
                if slot == "slot1" and slot1 <= datetime.strptime(data["departure"], '%H:%M:%S') and slot2>= datetime.strptime(data["departure"], '%H:%M:%S'):
                    new_train_data.append(data)
                if slot == "slot3" and slot3 <= datetime.strptime(data["arrival"], '%H:%M:%S') and slot4>= datetime.strptime(data["arrival"], '%H:%M:%S'):

                    new_train_data.append(data)     
                if slot == "slot4" and slot4 <= datetime.strptime(data["arrival"], '%H:%M:%S') and slot5>= datetime.strptime(data["arrival"], '%H:%M:%S'):

                    new_train_data.append(data)   
                if slot == "slot5" and slot5 < datetime.strptime(data["arrival"], '%H:%M:%S'):

                    new_train_data.append(data)

        array_data= new_train_data
    return array_data


def get_schedule(train_number):
    """Returns the schedule of a train.
    """
    col, rows = exec_query(f"select * from schedule where train_number = '{int(train_number)}';")

    s = schedule_table

    sa = select([ s.c.station_code ,

                s.c.station_name ,

                s.c.train_number ,

                s.c.train_name ,

                s.c.day ,

                s.c.arrival ,

                s.c.departure ]).where(s.c.train_number == int(train_number))

    rows = (list(sa.execute()))

    # print((rows[0:10]))

    sch = []

    for row in rows:

        # print(row)

        d = {"station_code": row[0], "station_name":  row[1], "day": row[4], "arrival": row[5], "departure":row[6]}

        sch.append(d)

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


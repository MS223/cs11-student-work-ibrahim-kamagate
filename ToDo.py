action = raw_input("What do you want today?")
days = raw_input("What day?").lower
days_of_week = {
    'monday':[],
    'tuesday':[],
    'wednesday':[],
    'thursday':[],
    'friday' :[],
    'saturday':[],
    'sunday':[]
}

def add():
    days_of_week[days]=action.apend()


print days_of_week
#im trying to get the days of the week in oder

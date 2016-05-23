# user = raw_input("How can I help you?")
days_of_week = {
    'monday':[],
    'tuesday':[],
    'wednesday':[],
    'thursday':[],
    'friday' :[],
    'saturday':[],
    'sunday':[]
}
#
# def add(user, days):
#     days = raw_input("What day?")
#     action = raw_input("What do you want to do?")
#     days_of_week[days]=user.apend(days)
#
#
# def get(days):
#     print days_of_week[days]
#     # I need an option to call choice()
#
# def choice():
#     user_choice = raw_input("How can I help you?")
#     # if they choose 'add' call add()
#     # if they choose 'get' call get()
# add("something", "monday")
#
# get("monday")
#
def get(days):
    print days_of_week[days]


def add(user, days):
            days_of_week[days]=user.apend(days)



def choice():
    user_choice = raw_input("How can I help you?")
    if user_choice == 'get':
        day = raw_input("What day do you want to get?")
        get(day)

    elif user_choice == 'add':
        days = raw_input("What day?")
        action = raw_input("What do you want to do?")
        days_of_week[days]=user_choice.apend(days)

    else:
        print "have a nice day."
choice()

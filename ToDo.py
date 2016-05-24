
days_of_week = {
    'monday':[],
    'tuesday':[],
    'wednesday':[],
    'thursday':[],
    'friday' :[],
    'saturday':[],
    'sunday':[]
}
def get(day):
    print days_of_week[day]


def add(user, days):
    days_of_week[days]=user.append(days)



def choice():
    user_choice = raw_input("How can I help you?")
    while user_choice != 'exit':
        if user_choice == 'get':
            day = raw_input("What day do you want to get?")
            get(day)
            user_choice = raw_input("How can I help you?")

        elif user_choice == 'add':
            days = raw_input("What day?")
            action = raw_input("What do you want to do?")
            days_of_week[days].append(action)
            user_choice = raw_input("How can I help you?")

choice()

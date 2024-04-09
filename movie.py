'''
Task 1: 
	Movie Ticketing System

	Functionality:
		Users can sign up without any account.
		Each user has a unique username, and the system ensures uniqueness.
		User history of all previous movies watched is recorded.
		After logging in, users can book tickets for available movies.
		Users can select seats based on availability.
		Once a seat is booked, it becomes unavailable for other users.
		Database handling using json/txt file handling 
    
'''
import json

class MovieTicketingSystem:
    def __init__(self):
        self.users_file='users.json'
        self.movies_file='movies.json'
        self.users_data=self.load_data(self.users_file)
        self.movies_data=self.load_data(self.movies_file)

    def load_data(self,file_name):
        try:
            with open(file_name,'r') as file:
                return json.load(file)
        except Exception as e:
            print(f"Error on loading data: {e}")

    def save_data(self,file_name,data):
        try:
            with open(file_name,'w') as file:
                json.dump(data,file)
        except Exception as e:
            print(f"Error on saving data: {e}")

    def signup(self,username):
        if username in self.users_data:
            print('User already exists')
        else:
            self.users_data[username]={"history":[]}
            self.save_data(self.users_file,self.users_data)
            print("Users created successfully")
            self.dashboard(username)
            

    def login(self,username):
        if username in self.users_data:
            print("Logged in successfully")
            self.dashboard(username)
        else:
            print('User does not exist')

    def dashboard(self, username):
        print("\n********************************")
        print(f"Welcome, {username} !!")
        print("********************************")
        while True:
            print("\n 1. Display Movies with seats\n 2. Book Ticket\n 3. View your history\n 4. Logout\n")
            user_input=input("Enter your choice: ")
            if user_input=='1':
                self.display_movie_with_seat()
            elif user_input=='2':
                movie_name=input("Enter movie name: ")
                seat_no=input("Enter seat number: ")
                self.book_ticket(username,movie_name,seat_no)
            elif user_input=='3':
                self.view_history(username)
            elif user_input=='4':
                print("\nLogged out successfully")
                break

    def book_ticket(self,username,movie_name,seat_no):
        if movie_name in self.movies_data and seat_no in self.movies_data[movie_name]['available_seats']:
            if username in self.users_data:
                self.movies_data[movie_name]['available_seats'].remove(seat_no)
                self.save_data(self.movies_file,self.movies_data)
                self.users_data[username]['history'].append({'movie':movie_name,'seat':seat_no})
                self.save_data(self.users_file,self.users_data)
                print('\nTicket booked successfully')
            else:
                print('\nUser not available !! Sign-up first')
        elif movie_name not in self.movies_data:
                print('\nMovie not available')
        else:
            print('\nSeat not available')

    def display_movie_with_seat(self):
        print("\nAvailable Movies with seats: \n")
        for movie_name, details in self.movies_data.items():
            movie=movie_name.upper()
            print(f"{movie}    \nAvailable Seats: {details['available_seats']}\n")
    
    def view_history(self,username):
        if username in self.users_data:
            print("\nYour booking history: ")
            for history in self.users_data[username]['history']:
                print(f"Movie: {history['movie']}, Seat: {history['seat']}")


movie_instance=MovieTicketingSystem()

print("\n*******************************************************************")
print("----------------Welcome to Movie Ticketing System----------------")
print("*******************************************************************\n")

# print(" 1. Signup\n 2. Login\n 3. Exit\n")
user_input=input("Already have an account? (y/n):")
if user_input=='y' or user_input=='Y':
    user_name=input("Enter username: ")
    movie_instance.login(user_name)
elif user_input=='n' or user_input=='N':
    user_name=input("Enter username: ")
    movie_instance.signup(user_name)
else:
    print("Invalid input")
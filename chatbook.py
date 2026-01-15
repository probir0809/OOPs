class chatbook:
    def __init__(self):        #this is constructor
        # below are the attributes
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()


    def menu(self): #this is method
        user_input = input("""
                           Welcome to chatbook !! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. press 3 to write a post
                           4. press 4 to message a friend
                           5. press any other key to exit
                           """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

    def signup(self):
        email = input("enter your email here ->")
        pwd = input("enter your password here ->")
        self.username = email
        self.password = pwd
        print("You have sucessfully signed up !!")
        print("\n")
        self.menu()

obj = chatbook()
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
            self.signin()
        elif user_input == "3":
            self.post()
        elif user_input == "4":
            self.sending()
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

    def signin(self):
        if self.username == "" and self.password == "" :
            print("Please signup first by pressing 1 in the main menu")
        else:
            username = input("enter your email here ->")
            password = input("enter your password ->")
            if username == self.username and password == self.password :
                print("you have signedin sucessfully ..")
                self.loggedin = True

            else:
                print("please input correct credentials...")
        print("\n")
        self.menu()

    def post(self):
        if self.loggedin == False :
            print("Please signin first, to post something !!")
        else:
            post = input("please write wour post here ")
            print(f"following content has been posted -> {post}")

        print("\n")
        self.menu()

    def sending(self):
        if self.loggedin == True:
            txt = input("Enter your massage here ->")
            print("\n")
            frnd = input("Whome to send the msg? ->")
            print(f"your massage has been sent to {frnd}")
        else :
            print("you need to sighin to send a massage")
        print("\n")
        self.menu()

obj = chatbook()
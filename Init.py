####################################################################################
# Author    : Faddi Susanto  						           #
####################################################################################

import Database

class Init:
	
    tbUser = []
    isLogin = []
	
    def __init__(self):
        self.db = Database.Database()
        opnUsr = open("User.py","r")
        for ff in opnUsr:
            gg = ff.replace("\n","").split(",")
            Init.tbUser.append(gg)
        opnUsr.close()
        self.choice()

    def choice(self):
        if self.isLoggedIn() == False:
            self.index()
        else:
            self.index2()
        return 0
    
    def index2(self):
        print "-----------------"
        print "Faddi Application"
        print "-----------------"
        print "Welcome, %s" %(Init.isLogin[0][2])
        print "1. logout"
        self.chooseIndex2()
        return 0
    
    def chooseIndex2(self):
        try:
            cse = input("Choose : ")
            cse = int(cse)
            if cse == 1:
                del Init.isLogin[0]
                print "Have a nice day.."
                print ""
                self.choice()
            else:
                print "Input doesn't match the current list"
                print ""
                self.choice()
        except:
            print "Input number only"
            print ""
            self.choice()
        return 0

    def index(self):
        print "-----------------"
        print "Faddi Application"
        print "-----------------"
        print ""
        print "1. Login"
        print "2. Register"
        print "3. Show Users"
        print "4. Delete User"
        print "5. Exit"
        self.chooseIndex()
        return 0

    def chooseIndex(self):
        try :
            chs = input("Choose : ")
            chs = int(chs)
            if chs == 1:
                self.login()
                self.choice()
            elif chs == 2:
                self.indexReg()
	        self.choice()
            elif chs == 3:
                self.db.currUser()
                self.choice()
            elif chs == 4:
                self.DUser()
                self.choice()
            elif chs == 5:
                self.exit()
            else :
                print "Number %d you choose, not in the list" %(chs)
                print ""
                self.choice()
        except :
            print "Input does not match the current list"
            print ""
            self.choice()
        return 0
    
    def DUser(self):
        q = raw_input("Delete User : ")
        q = "%s = " %q
        self.db.dellUser(q)
        return 0

    def indexReg(self):
        print ""
        print "---------------------"
        print "Register Your Account"
        print "---------------------"
        print ""
        username = raw_input("Username : ")
        password = raw_input("Password : ")
        name = raw_input("Name     : ")
        born = raw_input("Born In  : ")
        print "Birth Format dd-mm-yyyy"
        birth = raw_input("Birth    : ")
        address = raw_input("Address  : ")
        hobbies = raw_input("Hobbies  : ")
        self.db.regUser(username,password,name,born,birth,address,hobbies)
        self.choice()
        return 0
	
    def login(self):
        usrnm = raw_input("Masukkan Username : ")
	pwd = raw_input("Masukkan Password : ")
        j = 0
        jum = len(Init.tbUser)
        while j < jum:
	    if usrnm == Init.tbUser[j][0] and pwd == Init.tbUser[j][1] :
	        Init.isLogin.append(Init.tbUser[j])
	    j = j + 1
	return 0
    
    def isLoggedIn(self):
        log = False
        jm = len(Init.isLogin)
        if jm > 0:
            log = True
        else:
            log = False
        return log

    def exit(self):
        print "Feel free to come again..."
        print "....."
        print "bye.."
        print ""
        SystemExit()
        return 0

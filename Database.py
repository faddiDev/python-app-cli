####################################################################################
#Author    : Faddi Susanto  													   #
#Important : You can edit or share this application but do                         #
#            not do commercial as the author are not take credit from it           #
#Penting   : Silahkan meng-edit atau membagikan aplikasi ini namun dilarang        #
#            keras melakukan penjualan karena pencipta aplikasi tidak meminta uang #
####################################################################################

class Database:
    
    def __init__(self):
        print ""
		
    def allUsers(self):
        gg = ""
        opnUsr = open("User.py","r")
	for ff in opnUsr:
	    gg = ff.replace("\n","").split(",")
	opnUsr.close()
        return gg
	
    def regUser(self,usrnme,pwd,name,born,birth,address,hobbies):
        svReg = open("User.py","a")
        data = "%s,%s,%s,%s,%s,%s,%s\n" %(usrnme,pwd,name,born,birth,address,hobbies)
        svReg.writelines(data)
        svReg.close()
        return 0
    
    def currUser(self):
        opUs = open("User.py","r")
        for i in opUs:
            print i
        opUs.close()
        return 0

    def dellUser(self, user):
        with open("User.py","r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if user not in line:
                    f.write(line)
            f.truncate()
        return 0

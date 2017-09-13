class EasyComment:

    def welcoming(self):
        # Shows a welcomig message to user
        print("Welcome to Easy Comment");

    def getInfo(self):

        # Gets informations about source file to write 
        # the top of the source file
        # Program works for c files, the other language will be added soon.
        self.file_name = input("Enter a file name: ")
        self.name_author = input("Enter author: ")
        self.created_date = input("Enter creation date: ")
        self.last_update = self.created_date
        self.description = input("Enter a description for your source file: ")

    def createFile(self, fileName):

        f = open(self.file_name, "w+");
        f.write("/*----------------------------------------------*")
        f.write(" * Author       : " + self.name_author + "           *\n")
        f.write(" * Created Date : " + self.created_date + "          *\n")
        f.write(" * Last Update  : " + self.last_update + "           *\n")
        f.write(" * Description  : " + self.description + "           *\n")
        f.write(" *----------------------------------------------*")
        f.write(" */\n")
    
        f.close()

def main():
    ec = EasyComment()
    ec.welcoming()
    ec.getInfo()
    ec.createFile(ec.file_name)

main()

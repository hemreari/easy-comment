class EasyComment:

    def welcoming(self):

        # Shows a welcomig message to user
        # and detects the type of the source file

        print("Welcome to Easy Comment")
        print("Avaible programming languages:\n")
        print("C [1], Python [2], Java [3]\n")
        self.type_source_file = input("Your choice: ")
        
    def getInfo(self):

        # Gets informations about source file to write 
        # the top of the source file

        self.file_name = input("Enter a file name: ")
        self.name_author = input("Enter author: ")
        self.created_date = input("Enter creation date: ")
        self.last_update = self.created_date
        self.description = input("Enter a description for your source file: ")
        
        if self.type_source_file == '1':
            self.createC(self.file_name);
        elif self.type_source_file == '2':
            self.createPython(self.file_name);
        elif self.type_source_file == '3':
            self.createJava(self.file_name);
        else:
            print("You have to choose [1], [2] or [3]")


    # if the given files isn't there creates a file with given name
    def createFile(self, fileName):
        f = open(self.file_name, 'w')

    def createC(self, fileName):

        
        # creates a source file for C with comment block, if the file doesn't exist.
        # If the file exists, writes a comment block this file.  
        while True:
            try:
                f = open(self.file_name, "r+");
                break
            except OSError:
                createFile(self.file_name)

        content = f.read()
        f.seek(0, 0)

        f.write("/*" + '-' * 77 + "*\n")
        f.write(" * Author       : " + self.name_author + ' ' * (80 - (19 + len(self.name_author))) + "*\n")
        f.write(" * Created Date : " + self.created_date + ' ' * (80 - (19 + len(self.created_date))) + "*\n")
        f.write(" * Last Update  : " + self.last_update + ' ' * (80 - (19 + len(self.last_update))) + "*\n")
        f.write(" * Description  : " + self.description + ' ' * (80 - (19 + len(self.description))) + "*\n")
        f.write(" *" + '-' * 77 + "*\n")
        f.write(" */\n")
        f.write(content)
        
        f.close()

    def createPython(self, fileName):

        # creates a source file for Python with comment block.

        f = open(self.file_name, "w+");
        f.write(" '''\n *" + '-' * 77 +"*\n")
        f.write(" * Author       : " + self.name_author + ' ' * (80 - (19 + len(self.name_author))) + "*\n")
        f.write(" * Created Date : " + self.created_date + ' ' * (80 - (19 + len(self.created_date))) + "*\n")
        f.write(" * Last Update  : " + self.last_update + ' ' * (80 - (19 + len(self.last_update))) + "*\n")
        f.write(" * Description  : " + self.description + ' ' * (80 - (19 + len(self.description))) + "*\n")
        f.write(" *" + '-' * 77 + "*\n")
        f.write(" '''\n")
        
        f.close()



    def createJava(self, fileName):

        f = open(self.file_name, "w+");
        f.write("/*" + '-' * 77 + "*\n")
        f.write(" * Author       : " + self.name_author + ' ' * (80 - (19 + len(self.name_author))) + "*\n")
        f.write(" * Created Date : " + self.created_date + ' ' * (80 - (19 + len(self.created_date))) + "*\n")
        f.write(" * Last Update  : " + self.last_update + ' ' * (80 - (19 + len(self.last_update))) + "*\n")
        f.write(" * Description  : " + self.description + ' ' * (80 - (19 + len(self.description))) + "*\n")
        f.write(" *" + '-' * 77 + "*\n")
        f.write(" */\n")
        
        f.close()

        
def main():
    ec = EasyComment()

    ec.welcoming()
    ec.getInfo()
    print("\nEverything is done, Your file is created.\n")

main()

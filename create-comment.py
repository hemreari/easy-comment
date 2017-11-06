class EasyComment:

    def welcoming(self):

        # Shows a welcomig message to user
        # and detects the type of the source file

        print("Welcome to Easy Comment")
        print("Avaible programming languages:\n")
        print("C [1], Python [2], Assembly [3]\n")
        self.type_source_file = input("Your choice: ")
        self.check_Option(self.type_source_file)
        
    def getInfo(self):

        # Gets informations about source file to write 
        # the top of the source file
        # Program works for c files, the other language will be added soon.

        self.file_name = input("Enter a file name: ")
        self.name_author = input("Enter author: ")
        self.created_date = input("Enter creation date: ")
        self.last_update = self.created_date
        self.description = input("Enter a description for your source file: ")
        
        if self.type_source_file == '1':
            self.create_C_File(self.file_name);
       #elif self.type_source_file == '2':
       #    self.create_Python_File(self.file_name);
       #elif self.type_source_file == '3':
       #    self.create_Assem_File(self.file_name);

    def create_C_File(self, fileName):

        '''
            creates a source file for C pl with comment block, if the file doesn't exist.
            If the file is existed, writes a comment block this file.  
        '''
        f = open(self.file_name, "w+");
        f.write("/*" + '-' * 77 + "*\n")
        f.write(" * Author       : " + self.name_author + ' ' * (80 - (19 + len(self.name_author))) + "*\n")
        f.write(" * Created Date : " + self.created_date + ' ' * (80 - (19 + len(self.created_date))) + "*\n")
        f.write(" * Last Update  : " + self.last_update + ' ' * (80 - (19 + len(self.last_update))) + "*\n")
        f.write(" * Description  : " + self.description + ' ' * (80 - (19 + len(self.description))) + "*\n")
        f.write(" *" + '-' * 77 + "*\n")
        f.write(" */\n")
        
        f.close()

    def create_Python_File(self, fileName):

        print("This option is not avaible yet.\n")


    def create_Assem_File(self, fileName):

        print("This option is not avaible yet.\n")


    def check_Option(self, typeOfFile):

        '''
           This function is temporary. It checks for 
           unavaible choices and prints a information
           message. End of the function it calls 
           welcoming function.
        '''
        if typeOfFile == '2' or typeOfFile == '3':
            print("This option is unavaible.")
            print("*" * 30)
            self.welcoming()

    
def main():
    ec = EasyComment()

    ec.welcoming()
    ec.getInfo()
    print("\nEverything is done, Your file is created.\n")

main()

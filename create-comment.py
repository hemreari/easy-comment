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
        f.write("/*" + '-' * 77 + "*\n")
        f.write(" * Author       : " + self.name_author + ' ' * (80 - (19 + self.countAuthor)) + "*\n")
        f.write(" * Created Date : " + self.created_date + ' ' * (80 - (19 + self.countDate)) + "*\n")
        f.write(" * Last Update  : " + self.last_update + ' ' * (80 - (19 + self.countUpdate)) + "*\n")
        f.write(" * Description  : " + self.description + ' ' * (80 - (19 + self.countDescription)) + "*\n")
        f.write(" *" + '-' * 77 + "*\n")
        f.write(" */\n")
    
        f.close()

    def wordCount(self):
        
        self.countAuthor = len(self.name_author)
        self.countDate = len(self.created_date)
        self.countUpdate = len(self.last_update)
        self.countDescription = len(self.description)
        
        
def main():
    ec = EasyComment()

    ec.welcoming()
    ec.getInfo()
    ec.wordCount()
    ec.createFile(ec.file_name)
    print("Everything is done, Your file created.\n")

main()

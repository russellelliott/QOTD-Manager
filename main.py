#tutorial: https://www.youtube.com/watch?v=DArlLAq56Mo

import os
from dotenv import load_dotenv
load_dotenv() #take environment variables from .env

import requests #for sending message
from csv import writer #for adding data to csv

#channel id and authorization tag are stored in env file for security/privacy purposes
id = os.environ.get("ID")#channel id for headstarter #general
authority = os.environ.get("AUTHORITY") #get the authorization tag from env fie

#sends a message to specific discord channel
def makeMessage(content):
    #go to discord on desktop, click f12, go under the payload tab, copy content
    payload = {
        "content": content
    }

    #go to discord on desktop, click f12, go to request headers -> authorization
    header = {
        "authorization": authority
    }
    #go to discord on desktop, click f12, go to network tab, click anything to see request posted
    #get the id by right clicking a channel and selcting "copy id" (developer mode must be enabled for option to appear)
    url = "https://discord.com/api/v9/channels/"+id+"/messages"

    #make the post with the data and header
    r = requests.post(url, data=payload, headers=header)
    #questions and their statuses will be stored in questions.csv

#print a list of commands
def help():
    print("PROGRAM COMMANDS")
    print("help: prints list of commands")
    print("exit: exit the program at any stage")
    print("send: upon entering this command, you have the option to add a question to the end of the list, or type \"exit\" to exit.")
    print("delete: upon entering this command, you have the option to delete a question by specifying its number, or type \"exit\" to exit. ")

questions = "questions.csv" #file that stores questions
#main function
if __name__ == "__main__":
    while(True):
        print("Enter a valid command, or type \"help\" to see list of commands, or type \"exit\" to exit: ")
        command = input()
        if(command.lower()=="help"):
            help()
        if(command.lower()=="exit"):
            break
        if(command.lower()=="send"):
            print("Type a message to send, or type \"exit\" to exit: ")
            message = input()
            if(message.lower() == "exit"):
                break
            #add question id, message, and status to csv file
            #iterate through file, count lines
            #https://pynative.com/python-count-number-of-lines-in-file/
            with open(questions, 'r') as fp:
                number = sum(1 for line in fp)
                print('Total lines:', number)
            fp.close()
            #https://www.delftstack.com/howto/python/python-append-to-csv/
            # First, open the old CSV file in append mode, hence mentioned as 'a'
            # Then, for the CSV file, create a file object
            with open(questions, "a", newline='') as f_object:
                #data to add
                list_data = [number, message]
                # Pass the CSV  file object to the writer() function
                writer_object = writer(f_object)
                # Result - a writer object
                # Pass the data in the list as an argument into the writerow() function
                writer_object.writerow(list_data)  
                # Close the file object
                f_object.close()
            #at this point, message is sent
            #makeMessage(message)
        if(command.lower()=="delete"):
            print("Type a question number to delete, or type \"exit\" to exit: ")
            question = int(input())
            #find that question number in the csv file
            num = 1 #row number
            delete = False
            with open(questions, "r+", newline='') as f_object: #read and write
                for line in f_object:
                    #https://stackoverflow.com/questions/4796764/read-file-from-line-2-or-skip-header-row
                    next(f_object) #skip header row
                    #print(num)
                    if(line[0]==str(question)):
                        print("FOUND")
                        print(line)
                        print("Delete this question? yes/no: ")
                        answer = input()
                        if(answer.lower() == "yes"):
                            #proceed with deletion
                            delete = True
                            print("Deleting the question")
                            pass
                        else:
                            print("Deletion canceled")
                    elif(line[0]>str(question) and delete): #only need to change id numbers if deletion is occurring
                        #fix the id numbers after question is deleted
                        pass
                    num+=1
                        
            
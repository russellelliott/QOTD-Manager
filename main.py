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
    #questions will be stored in questions.txt

#print a list of commands
def help():
    print("PROGRAM COMMANDS")
    print("help: prints list of commands")
    print("exit: exit the program at any stage")
    print("send: upon entering this command, you have the option to add a question to the end of the list, or type \"exit\" to exit.")
    print("delete: upon entering this command, you have the option to delete a question by specifying its number, or type \"exit\" to exit. ")

questions = "questions.txt" #file that stores questions

#https://www.pythonforbeginners.com/files/how-to-delete-a-specific-line-in-a-file
def remove_line(fileName,lineToSkip):
    """ Removes a given line from a file """
    with open(fileName,'r') as read_file:
        lines = read_file.readlines()

    currentLine = 1
    with open(fileName,'w') as write_file:
        for line in lines:
            if currentLine == lineToSkip:
                pass
            else:
                write_file.write(line)
	
            currentLine += 1

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
            with open(questions, "a") as myfile:
                #https://stackoverflow.com/questions/4706499/how-do-you-append-to-a-file
                myfile.write(message)
                myfile.write("\n")
            #at this point, message is sent
            #makeMessage(message)
        if(command.lower()=="delete"):
            print("Type a question number to delete, or type \"exit\" to exit: ")
            question = int(input())
            #find that question number in the csv file
            num = 1 #row number
            with open(questions, "r+", newline='') as f_object: #read and write
                for line in f_object:
                    if(num==question):
                        print("FOUND")
                        print(line)
                        print("Delete this question? yes/no: ")
                        answer = input()
                        if(answer.lower() == "yes"):
                            #proceed with deletion
                            print("Deleting the question")
                            remove_line(questions, num)
                        else:
                            print("Deletion canceled")
                    num+=1
                        
            
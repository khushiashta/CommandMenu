import smtplib
import pywhatkit
import os
from twilio.rest import Client
import speech_recognition as sr
import subprocess

def command1():
    print("Running command 1...")
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('senders mail id','password')
    server.sendmail('senders mail id','	receivers mail id','This message is sent by python code')
    print('mail sent successfully')

def command2():
    print("Running command 2...")
    pywhatkit.sendwhatmsg("number" , "hello, this message iss sent through python code",12,45,10,True,2)

def command3():
    print("Running command 3...")
    account_sid = '[auth_acc]'
    auth_token = '[auth_token]'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            from_='twilio number',
            body='hello,how are you',
            to='number'
            )
    print(message.sid)
    print("Message sent")

def exit_program():
    print("Exiting the program...")
    # Add any cleanup or finalization code here
    quit()

def main_menu():
    while True:
        print("\n===== Main Menu =====")
        print("1. Send Email")
        print("2. Send Whatsapp")
        print("3. Send SMS")
        print("4. Exit")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            command1()
        elif choice == "2":
            command2()
        elif choice == "3":
            command3()
        elif choice == "4":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

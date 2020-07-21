from random import choice
from string import ascii_lowercase as letters
import time

class KeyValue:
    def __init__(self,data_size,email_size):
        self.data_size = data_size
        self.email_size = email_size

    @staticmethod
    def value():
        return choice(['Software Engineer','Cyber Security Specialist','Web Develo\
per','Hydropower Expert','Mechanical Engineer','Surgeon'])

    @staticmethod
    def domain_generator():
        return choice(['gmail.com','outlook.com','yahoo.com','hotmail.com'])

    def email_generator(self):
        email=[]
        for i in range(self.email_size):
            email.append(choice(letters))
        return ''.join(email)+'@'+KeyValue.domain_generator()

    def KeyValuePair(self):
        with open('KeyValuePair.txt','a+') as writer:
            for i in range(self.data_size):
                writer.write(self.email_generator()+' : '+KeyValue.value()+"\n")
        return "Dataset Generated"

    def __str__(self):
        return "Key Value Pair Generator"
start=time.time()
trial=KeyValue(100,7)
print(trial.KeyValuePair())
end=time.time()
print("Time Required to generate the Key Value Pair: ",(end-start))

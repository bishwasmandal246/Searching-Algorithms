import time
from random import choice
from string import ascii_lowercase as letters
from binary_search import binary_search_iter as bin1
from binary_search import binary_search_recur as bin2

def domain():
    return choice(['yahoo.com','gmail.com','hotmail.com','outlook.com'])

def n_email_generator(individual_email_length,number_of_emails):
    email=[]
    for i in range(number_of_emails):
        abc=[choice(letters) for i in range(individual_email_length)]
        email.append(''.join(abc)+'@'+domain())
    return email

all_email=n_email_generator(5,1000)
print(bin1(sorted(all_email),'randm@gmail.com'))
print(bin2(sorted(all_email),'randm@gmail.com',0,1000))

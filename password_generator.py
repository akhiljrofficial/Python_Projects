import random

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numb=['0','1','2','3','4','5','6','7','8','9']

symbol=['!','@','#','$','%','^','&','*','(',')']

n_numb=int(input("enter the no of integers in the password"))
n_symb=int(input("enter the no of symbols in the password"))
n_letter=int(input("enter the no of letter in the password"))
password_list=[]
for i in range(1,n_numb+1):
    password_list.append(random.choice(numb))
for i in range(1,n_symb+1):
    password_list.append(random.choice(symbol))
for i in range(1,n_letter+1):
    password_list.append(random.choice(letters))
print(password_list)
random.shuffle(password_list)
password=""
for i in password_list:
    password+=i
print(password)

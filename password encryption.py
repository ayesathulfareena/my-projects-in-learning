'''this code is used for create a byte string for your password.
   if you require extra security here you can create your passkey with options such as custom passkey and random generated passkey.
   if you forget your password and passkey we have a encrypted files here you can see your password and passkey.'''

from cryptography.fernet import Fernet
import random
import string
print(''' your can create a password with letters,numbers and punctuations\n''')
password=input("enter your password:" )
password=Fernet.generate_key()
print(f"this is byte string of your password:{password}")
with open("key.txt","wb") as key:
 key.password=Fernet.encrypt
 key.write(password)
while True:
 print("if you require two security factor ")
 user=input("choose option for passkey\n 1.random passkey generation.\n 2.custom passkey \n or press 'q'to quit") 
 if user =='q':
  break
 if user=='2':
  print("your custom passkey will convert into byte string for more security ")
  passkey=input("enter a passkey:" )
  with open("key.key","wb") as paasky:
   passkey=Fernet.generate_key()
   paasky.write(passkey)
  print(f"your passkey is securely stored in'key.key' byte file\n here is your passkey: {passkey}")
  break
 if user=='1':
   randpasskey=" "
   randompasskey=string.ascii_letters+string.digits+'_'

   
   rand=randompasskey
   length=43
   for i in range(length):
     randm=random.choice(rand)
     randpasskey+=randm
   
   print(f"random passkey is:{randpasskey}")
   print('''your passkey is securely stored in'randkey.key' file''')
   with open("randkey.key","w") as randy:
    randy.write(randpasskey)
 else:
    print("invalid input")

   
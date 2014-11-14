	
import uuid         # generate a random number
import hashlib

import uuid
import hashlib

def hash_pswd(pswd):
    salt = uuid.uuid4().hex
    return hashlib.sha512(salt.encode() + pswd.encode()).hexdigest() + ":" + salt

def ck_pswd(hashed_pswd, user_pswd):
    pswd, salt = hashed_pswd.split(":")
    return pswd == hashlib.sha512(salt.encode() + user_pswd.encode()).hexdigest() 

enter_pswd = input("Enter a password: ")
hashed_pswd = hash_pswd(enter_pswd)
print("The string to store in the database is: %s" % hashed_pswd)
reenter_pswd = input("Re-enter your password: ")
if ck_pswd(hashed_pswd, reenter_pswd):
    print("Your password matches.")
else:
    print("Your password does not match.")
 
 
    



import hashlib
str=input("Enter string : ")
hash=hashlib.sha256(str.encode()).hexdigest()
print("SUCCESSFULLY CONVERTED INTO HASH FORMAT!!!")
print("The Encrypted Code is : ",hash)
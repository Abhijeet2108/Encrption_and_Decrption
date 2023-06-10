# This Program is made by - Abhijeet Bhaisare

print("Welcome To the Program of Encrption And Decryption ")
print(" 1. for Encrption ")
print(" 2. for Decryption \n")
choice = int(input("Enter your choice :"))

if choice == 1:
    data = int(input("Enter the Number in Encrpt Data : "))
    ec = data * 2108 
    print("The Encrpted Data is : ",ec)
 
elif choice == 2:
    data = int(input("Enter the Number for Decrpt Data :"))
    de = data / 2108
    print("The Decrpted Data is ",de)
else:
    print("Invalid input ")
    
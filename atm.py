amount=int(input("Enter the amount you would like to withdraw: "))
note1=amount//20000
note3=(amount%20000)%10000//5000
note2=(amount%20000)//10000
print("notes of 20000 soms=", note1)
print("notes of 10000 soms=",note2)
print("notes of 5000 soms=",note3)
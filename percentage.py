math=int(input("Enter your math grade:"))/100
sc=int(input("Enter your science grade:"))/100
physics=int(input("Enter your physics grade:"))/100
chem=int(input("Enter your chemistry grade:"))/100
eng=int(input("Enter your english grade:"))/100
print("Here is your percentage:")
result=((math+sc+physics+chem+eng)/5 *100)
print(result, "%")
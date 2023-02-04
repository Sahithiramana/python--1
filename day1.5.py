a=int(input("Enter the number of fresh loaves purchased: "))
c=int(input("Enter the number of day old loaves purchased: "))
b=a*185
print("Amount of new loaves",b)
d=(c*185)-(c*185*.6)
print("Amount of day old loaves",d)
#print("total discount",b*6)
print("Total amount",b+d)

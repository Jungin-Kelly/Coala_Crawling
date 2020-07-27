#1
for i in range (1,10):
    print("*"*i)
#1-1
for i in range(10):
    for j in range(i+1):
        print("*",end="")
    print()

print("--------------------------")
for i in range (1,10,2):
    print("*" * i)

print("--------------------------")
for i in range (10,1,-1):
    print("*" * i)

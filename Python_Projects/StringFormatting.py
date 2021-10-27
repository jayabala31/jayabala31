
for i in range(4,10):
    print("No. {0} squared is {1} and cubed is {2}".format(i,i**2,i**3))

for i in range(4,10):   #left alignment
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i,i**2,i**3))


for i in range(4,10):   #right alignment
    print("No. {0:2} squared is {1:>4} and cubed is {2:>4}".format(i,i**2,i**3))

for i in range(4,10):     #center alignment
    print("No. {0:2} squared is {1:^4} and cubed is {2:^4}".format(i,i**2,i**3))


print("Pi value is {0}".format(22/7))
print("Pi value is {0:5f}".format(22/7))
print("Pi value is {0:10f}".format(22/7))
print("Pi value is {0:10.5f}".format(22/7))
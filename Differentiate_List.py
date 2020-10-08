#this code diffrentiate the list in intrgers, floats, strings.


a= ['Hello',35,'b',45.5,'world',60]
I=f=s=0
for j in a:
    if isinstance(j,int):
        I=I+1
    elif isinstance(j,float):
        f=f+1
    else:
        s=s+1
print('Number of integers are:',I)
print('Number of Floats are:',f)
print("numbers of strings are:",s)

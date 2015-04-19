for i in range(1,10):
    for k in range(0,i-1):
        print(end="        ")
    for j in range(i,10):
        print(str.format("{0:1}*{1:1}={2:<2}",i,j,i*j),end="  ")
    print() 


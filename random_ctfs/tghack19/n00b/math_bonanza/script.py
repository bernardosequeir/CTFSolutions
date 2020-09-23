from pwn import *
r = remote("math.tghack.no",10000)
for x in range(1000):
    print r.recvline()
    line = r.recvline()
    print line
    items = line.split(" ")
    if items[1] == "+":
        sum = int(items[0]) + int(items[2])   
        print sum
        print r.send(str(sum))
    elif items[1] == "-":
        sub = int(items[0]) - int(items[2])
        print sub
        print r.send(str(sub))
    elif items[1] == "*":
        mul = int(items[0]) * int(items[2])
        print mul
        print r.send(str(mul))
    else:
        div = int(items[0])/int(items[2])
        print div
        print r.send(str(div))  
    print r.recvline()          
print r.recvline()        
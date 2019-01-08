r = int(input("Enter The Row Of The Matrix:- "))
c = int(input("Enter The Columns Of The Matrix:- "))
mat = []
chips = []
adj=[]
chk1=[]
for i in range(r):
    mat += [0]

for i in range(r):
    mat[i] = [0]*c

for i in range(r):
    for j in range(c):
        print('Enter', i+1,'th row and', j+1,'th column:-')
        mat[i][j] = int(input())

print("")
print("")

for i in range(r):
    for j in range(c):
        print(mat[i][j], end="")
        print("\t", end="")
    print("")


for i in range(r):
    for j in range(c):
        if(mat[i][j] == 1):
            chips.append([i,j])

print("")
print("")
print(chips)
nc=chips[:]

print("")
print("")

for a in chips:
    adj.append(a)
    
    a[0] = a[0] + 1
    print(a)
    if(a in nc):
##        print(a)
        print("Present Sir!")
##        adj.append(a)
##    a[0] = a[0] - 1
##    a[1] = a[1] + 1
##    if(a in chips):
##        adj.append(a)
##    a[1] = a[1] - 1

print(adj)

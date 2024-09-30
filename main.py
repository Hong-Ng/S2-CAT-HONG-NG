min = 5
max = 5
names = []
namequantity = 0

with open('names.txt', 'r') as file:
    names = file.readlines()
    names = [name.strip() for name in names]

def namelength(name):
    a = 0
    for char in name:
        a= a + 1
    return a
def minmaxnames(names, min, max):
    for name in names:
        a = 0
        a = namelength(name)
        namequantity = 0
        namequantity = namequantity + 1
        if a >= max:
            maxname = name
            max = a
        elif a <= min:
            minname = name
            min = a
    print("Number of names:", namequantity)    
    print("Longest name:", maxname + ". Shortest name:", minname)

def pairing():
    num = 0
    pairlist = []
    a = 0
    b = 1   
    name = input("Enter name: ")
    for char in name:
        num = num+1
    num = num - 1
    while b <= num:
        
        pair = name[a], name[b]
        pairlist.append(pair)
        a = a+1
        b = b+1
    print (pairlist)
    
while True:   
    print("Welcome to Hell")
    print("Choose an option:")
    print("1. Find the Longest and Shortest names")
    print("2. Enter a name and recieve the character pairings")
    print("TO QUIT ENTER 0")
    inputs = int(input())
    if inputs == 1:
        minmaxnames(names, min, max)
    elif inputs == 2:
        pairing()
    elif inputs == 0:
        break
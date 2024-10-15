import random as r
min = 5
max = 5
names = []
namequantity = 0
freqlist = []
namefrequency = {}
x = 0
#opening the .txt file before taking all the names out as a list
with open('names.txt', 'r') as file:
    names = file.readlines()
    names = [name.strip() for name in names]
#I forgot .len existed
def namelength(name):
    a = 0
    for char in name:
        a = a + 1
    return a

def minmaxnames(names, min, max):
    for name in names:
        a = 0
        a = namelength(name)
        namequantity = 0
        namequantity = namequantity + 1
        #counter for the names
        if a >= max:
            maxname = name
            max = a
            #if the length of the name exceeded the current best, then it would become the new name, else nothing would happen
        elif a <= min:
            minname = name
            min = a
            #same here if the length of the name was shorter than the current best
    print("Number of names:", namequantity)    
    print("Longest name:", maxname + ". Shortest name:", minname)

def pairing(name):
    num = 0
    pairlist = []
    a = 0
    b = 1   
    num = namelength(name)
    num = num - 1
    pair = "#", name[a]
    pairlist.append(pair)
    while b <= num:
        pair = name[a], name[b]
        pairlist.append(pair)
        a = a+1
        b = b+1
    pair = name[b-1], "$"
    pairlist.append(pair)
    return (pairlist)
        
def cointoss():
    coin = ['0','1']
    coin_probs = [0.8,0.2]
    return r.choices(coin,coin_probs)

def wheelspin():
    spinner = ['0','1','2','3']
    spinner_probs = [0.2,0.1,0.1,0.6]
    return r.choices(spinner,spinner_probs)

while True:   
    print("Choose an option:")
    print("1. Find the Longest and Shortest names")
    print("2. Enter a name and recieve the character pairings")
    print("3. Recieve all character pairings")
    print("4. Weighted Coin Toss")
    print("5. Wheel Spin")
    print("TO QUIT ENTER 0")
    inputs = int(input())
    if inputs == 1:
        minmaxnames(names, min, max)
    elif inputs == 2:
        name = input("Enter name: ")
        print(pairing(name))
    elif inputs == 3:
        for name in names:
            freq = pairing(name)
            for name in freq:
                if name in namefrequency:
                    namefrequency[name] = namefrequency[name] + 1
                else:
                    namefrequency[name] = 1
        with open('pair_freq_sorted.txt', 'w') as file:
            for key, value in namefrequency.items():
                file.write(f"{key}: {value}\n")
    elif inputs == 4:
        i = 1
        while i < 21:
            print(cointoss())
            i = i + 1
    elif inputs == 5:
        i = 1
        while i < 21:
            print(wheelspin())
            i = i + 1
    elif inputs == 0:
        break
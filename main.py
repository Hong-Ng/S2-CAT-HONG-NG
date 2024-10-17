import random as r
min = 5
max = 5
names = []
namequantity = 0
freqlist = []
namefrequency = {}
keyfrequency = {}
x = 0
#oOpening the .txt file before taking all the names out as a list
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
#Counter for the names
        if a >= max:
            maxname = name
            
            max = a
#If the length of the name exceeded the current best, then it would become the new name, else nothing would happen
        elif a <= min:
            minname = name
            min = a
#Same here if the length of the name was shorter than the current best
    print("Number of names:", namequantity)    
    print("Longest name:", maxname + ". Shortest name:", minname)

def pairing(name):
    num = 0
    pairlist = []
    a = 0
    b = 1   
    num = namelength(name)
    num = num - 1
#I take the first letter and add a hash onto it to make it easy to identify if the letter started a word later on
    pair = "#", name[a]
    pairlist.append(pair)
    while b <= num:
        pair = name[a], name[b]
        pairlist.append(pair)
#Pairing the names together before adding them to a larger list
        a = a+1
        b = b+1
    pair = name[b-1], "$"
#Added a dollar sign to the last character to make it easier to tell which characters end names
    pairlist.append(pair)
    return (pairlist)
#Returning the word divided into pairs
        
def cointoss():
    coin = ['0','1']
#Outcomes, with 0 being tails and 1 being heads
    coin_probs = [0.8,0.2]
#Coin probablities, 0.8 and 0.2 being 0 and 1 respectively
    return r.choices(coin,coin_probs)

def wheelspin():
    spinner = ['0','1','2','3']
    spinner_probs = [0.2,0.1,0.1,0.6]
    return r.choices(spinner,spinner_probs)
#Same as the coin toss

for name in names:
            freq = pairing(name)
            for name in freq:
                if name in namefrequency:
                    namefrequency[name] = namefrequency[name] + 1
                else:
                    namefrequency[name] = 1 
for key in namefrequency: 
    if key[0] in keyfrequency:
        keyfrequency[key[0]] = namefrequency[key] + keyfrequency[key[0]]
    else:
        keyfrequency[key[0]] = namefrequency[key]

def pairfind(namefrequency):
    letter = input("Enter the letter you wish to find: ")

    for key, value in namefrequency.items():
        if key[0] == letter:
            print(key, ':', value)

def name_prob(namefrequency, keyfrequency):
    final = 1
    OGname = input("Enter Name: ").lower()
    paired_name = pairing(OGname)
    overall_probability = []
    for name in paired_name:
        denominator = keyfrequency[name[0]]
        numerator = namefrequency[name]
        probability = numerator/denominator
        overall_probability.append(probability)
        print("Probability of", name , ":", probability, '%')
    for num in overall_probability:
        final = final*num
    print("The overall probability of", OGname, "is:", final,'%')

while True:
    print("Choose an option:")
    print("1. Find the Longest and Shortest names")
    print("2. Enter a name and recieve the character pairings")
    print("3. Recieve all character pairings")
    print("4. Weighted Coin Toss")
    print("5. Wheel Spin")
    print("TO QUIT ENTER 0")
#Menu
    inputs = int(input())
    if inputs == 1:
        minmaxnames(names, min, max)
    elif inputs == 2:
        name = input("Enter name: ")
        print(pairing(name))
    elif inputs == 3:
        
        with open('pair_freqs_raw.txt', 'w') as file:
            for key, value in namefrequency.items():
                file.write(f"{key}: {value}\n")
        with open('Starting_Character_Freq.txt', 'w') as file:
            for key, value in keyfrequency.items():
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
#If the user enters a number on the menu it will them excute the function accordingly
    elif inputs == 0:
        break
#If the user enters 0 the loop is broken and the code ends
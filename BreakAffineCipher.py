import math;
import time;
import msvcrt;
#Using math module again for greatest common divider.

array = (open("dictionary.txt").read()).split("\n")

def crackAffine(m):
    plainText = '';
    counter = 0;
    matchList = [];

    encryptText = input('Please enter your encrypted text: \n');
    encryptText = encryptText.upper();

    start_time = time.time();

    length = len(encryptText);
    #Simular to decryption however only asks for the encrypted text, not the keys.
    
    print('Thank you, working on it...');
    
    coprimes = [];
    for i in range(m):
        #A function which takes m, the range of letters, and checks for coprimes in that range.
        testI = math.gcd(int(i), int(m));
        if testI == 1:
            coprimes.append(i);
            #If it is a coprime, appends it to the end of the array.

    for i in range(len(coprimes)):
        #Nested for loops. This one takes the "a" variable, which needs to be the coprime, from the coprime array.
        a = int(inverse(coprimes[i], m));
        for b in range(m):
            #This loop takes the "b" variable, from 0 to "m".
            plainText = '';
            for y in range(length):
                #This one takes the letters from the encrypted text one by one as "y".
                encryptNum = ord(encryptText[y]);
                #Changing it to Unicode number.
                if encryptNum >= 65 and encryptNum <= 90:
                    #If character was a capital letter, runs through this if loop.
                    plainNum = (((encryptNum - 65) - b) * a) % m;
                    #This is the decryption algorithm, using "a", "b", "m" and the Unicode number of character.
                    plainText += chr(plainNum + 65);
                    #Appends the final character version of Unicode number to end of string.
                    counter += 1;
                    #For testing.
                elif encryptNum == 32:
                    #If space, adds it to the string too
                    plainText += chr(encryptNum);
                    counter += 1;
                #Every other character gets discarded.

            ##dictionaryCheck(plainText);
            
            match = dictionaryCheck(plainText);
            if match.weight != 0:
                matchList.append(match);
                
                
            
    sortedList = sorted(matchList, key=lambda i: i.weight, reverse=True);

    print("My program took", time.time() - start_time, "to run")

    for z in sortedList:
        print(z.text, "with a weight of", z.weight);
        trigger = input("Enter \"Exit\" if you found it, or press enter to continue:\n")
        if trigger == "Exit":
            break;


    
def inverse(a, m):
    a1 = 1;
    a2 = a;

    b1 = 0;
    b2 = m;

    while b2 != 0:
        #Loops around untill b2 is equal to 0 (so the remainder is 0).
        x = a2 // b2;
        b1, b2, a1, a2 = (a1 - x * b1), (a2 - x * b2), b1, b2;
        #All in one line so they all get changed at same time, and not messsed up by the new values.
    return a1 % m;
    #Returns the remainder. This is to make sure it is not a negative number or a large number. 

def dictionaryCheck(plain):
    lenCounter = 0;
    for i in array:
        if i in plain:
            lenCounter += len(i)*len(i);
    
    class textCounter:
        def __init__(self):
            self.text = plain
            self.weight = lenCounter

    return textCounter();    

def main():
    m = 26;
    #Range of letters.
    crackAffine(m);
    #Starts the function with argument "m".
    #Encrypted text is "YFKLZOYWFFSRYGSC"            
    
    trigger = input("Press enter to exit or type \"Again\" to restart.");
    if trigger == "Again":
        main();


main();
#Boots up the start of the program.

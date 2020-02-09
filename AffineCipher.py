import math;


def encryption():
    encryptText = '';
    counter = 0;
    plainText = input("Please enter your plaintext: \n");
    plainText = plainText.upper();
    ##print(plaintext);
    ##a = input('Please enter your first encryption key, make sure it is a coprime of 26: \n');
    print('Please input your first encryption key, make sure it is a coprime of 26: ');
    inputType = 'a';
    a = int(validateType(inputType));
    ##print('a is' + a);
    
    ##b = input('Please enter the second encryption key: \n');
    print('Please enter the second encryption key: ');
    inputType = 'b';
    b = int(validateType(inputType));
    ##print('b is' + b);
    
    length = len(plainText);
    
    for x in range(length):
        plainNum = ord(plainText[x]);
        if plainNum >= 65 and plainNum <= 90: 
            encryptNum = ((plainNum - 65) * a + b) % 26;
            encryptText += chr(encryptNum + 65);
            counter += 1;
        elif plainNum == 32:
            encryptText += chr(plainNum);
            counter += 1;
    ##print(x);
    return encryptText;
    ##print(counter);


def decryption():
    plainText = '';
    counter = 0;
    encryptText = input('Please enter your encrypted text: \n');
    encryptText = encryptText.upper();
    print('Please enter your first encryption key you used, make sure it is still a coprime of 26: ');
    inputType = 'a';
    a = int(validateType(inputType));

    print('Please enter the second encryption key: ');
    inputType = 'b';
    b = int(validateType(inputType));

    length = len(encryptText);

    aInverse = int(inverse(a, 26));

    for x in range(length):
        encryptNum = ord(encryptText[x]);
        if encryptNum >= 65 and encryptNum <= 90:
            plainNum = (((encryptNum - 65) - b) * aInverse) % 26;
            plainText += chr(plainNum + 65);
            counter += 1;
        elif encryptNum == 32:
            plainText += chr(encryptNum);
            counter += 1;

    return plainText;


def validateType(inputType):
    ##print('validateType');
    a = input('');
    ##print(a.isdigit());
    while a.isdigit() == False:
        a = input('That is not a valid number. Please try again: \n');
    
    if inputType == 'a':
        validateCoprime(a);
    return a;
    


def validateCoprime(a):
    inputType = 'a';
    testA = math.gcd(int(a), 26);
    ##print(testA);
    while testA != 1:
        print('That number is not a coprime of 26. Please try again: ');
        validateType(inputType);
        break;

def inverse(a, m):
    a1 = 1;
    a2 = a;

    b1 = 0;
    b2 = m;

    while b2 != 0:
        x = a2 // b2;
        b1, b2, a1, a2 = (a1 - x * b1), (a2 - x * b2), b1, b2;
    return a1 % m;

def main():
    choice = '';
    while choice != 'Exit':
        choice = input('Please enter if you want to encrypt or decrypt a text. \nPlease put "Encrypt", "Decrypt" or "Exit": \n');
        if choice == 'Encrypt':
            print(encryption());
        elif choice == 'Decrypt':
            print(decryption());
        elif choice == 'Exit':
            break;
        else:
            print('You have entered incorrect choice.');
            main();

main();

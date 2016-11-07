text=input("Input text :")
key=int(input("Input key (number from 0 to 25) :"))
cipher=""
for i in range(len(text)):
    if text[i].isalpha():
        if text[i].isupper():
            print("upper")
            cipher=cipher+chr(ord('A')+((ord(text[i])-ord('A')+key)%26))
        else:
            print("lower")
            cipher=cipher+chr(ord('a')+((ord(text[i])-ord('a')+key)%26))
    else:
        cipher=cipher+text[i]

print(cipher)

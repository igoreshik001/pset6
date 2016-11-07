text=input("Input text :")
keys=""
while not keys.isalpha():
    keys=input("input text key :")
keys=keys.upper()
count=0
cipher=""
for i in range(len(text)):
    if text[i].isalpha():
        key=ord(keys[count])-ord('A')
        if text[i].isupper():
            cipher=cipher+chr(ord('A')+((ord(text[i])-ord('A')+key)%26))
        else:
            cipher=cipher+chr(ord('a')+((ord(text[i])-ord('a')+key)%26))
        count=count+1
        if count>=len(keys):
            count=0
    else:
        cipher=cipher+text[i]

print(cipher)

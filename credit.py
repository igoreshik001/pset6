def isFormat(number):
    count=0
    even=0
    uneven=0
    for i in number:
        if count%2==1:
            even=even+(((int(i))*2)//10+((int(i))*2)%10)
            #print(i+"i",count,"=count",count%2,"=count%2",even,"=even")
        else:
            uneven=uneven+int(i)
            #print(i+"i",count,"=count",count%2,"=count%2",uneven,"=uneven")
        count=count+1
    if (even+uneven)%10==0:
        return True
    return False
f=True
y="1234567890"
while f:
    number=input("Number :")
    for x in number:
        if x not in y:
            f=True
            break
        else:
            f=False
#for i in number:
#    print(i)
#print(number[0:2],len(number))
#print(isFormat(number))
if len(number)==15 and (number[0:2]=="37" or number[0:2]=="37") and isFormat(number):
    print("AMEX")
elif len(number)==16 and (number[0:2]=="51" or number[0:2]=="52" or number[0:2]=="53" or number[0:2]=="54" or number[0:2]=="55") and isFormat(number):
    print("MASTERCARD")
elif (len(number)==13 or len(number)==16) and number[0:1]=="4" and isFormat(number):
    print("VISA")
else:
    print("INVALID")

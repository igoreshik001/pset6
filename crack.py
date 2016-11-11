import sys
import crypt

if len(sys.argv) != 2:
    print ("python crack.py hashValue")
    sys.exit()
    
hash=sys.argv[1]
psw=""
alph=['']
flag=True

for i in range(26):
    alph.append(chr(i+ord('A')))
for i in range(26):
    alph.append(chr(i+ord('a')))
    
for i1 in range(53):
    if not flag:
        break
    
    for i2 in range(53):
        if not flag:
            break
        
        for i3 in range(53):
            if not flag:
                break
            
            for i4 in range(53):
                psw=psw+alph[i1]+alph[i2]+alph[i3]+alph[i4]
                if crypt.crypt(psw,"50")==hash:
                    print (psw)
                    flag=False
                if not flag:
                    break
                psw=""

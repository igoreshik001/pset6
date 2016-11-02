change=int(float(input("How much change is owned :"))*100)
print ((change//25)+((change%25)//10)+((change%25%10)//5)+(change%25%10%5))

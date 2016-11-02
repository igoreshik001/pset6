height=int(input("Height: "))
for i in range(height):
    print((' '*((height-1)-i))+('*'*(i+1))+'  '+("*"*(i+1)))

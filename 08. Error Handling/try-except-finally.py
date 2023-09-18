try:
    l = [1, 3, 5, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    
except:
    print("some error accurred")

finally:
    print("I an always executed")
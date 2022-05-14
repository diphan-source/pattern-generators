
# A program to display patterns using loops
n = int(input("Enter a number of layers ...:  "))
i = 1
while i <= n:
    j = 1
    while j <= n-i:
        print(" ",end="")
        j = j + 1
    j= 1
    while j <= 2*i-1:
        print("*", end="")
        j = j + 1
    print()
    i = i + 1

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0) +1 ):
            if num % i==0:
                break
            else:
                print(num)
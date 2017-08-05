def numloop(max, add):
    i = 0
    numbers = []

    while i < max:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + add
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

numloop(8, 2)

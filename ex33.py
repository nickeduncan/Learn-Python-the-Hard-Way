def numloop(max):
    numbers = []

    numrange = range(max)
    for i in numrange:
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

numloop(8)

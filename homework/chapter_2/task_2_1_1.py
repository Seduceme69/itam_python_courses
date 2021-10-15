def summation(inpet):
    inpet = inpet.split(", ")
    sum = 0
    for i in (inpet):
        sum += int(i)
    return sum
print(summation(input()))
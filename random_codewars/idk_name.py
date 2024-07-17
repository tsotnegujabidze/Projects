sum = 0
nubmers = [1,5,7,2,9,7,11,66,44,]

for i in range(len(nubmers)):
    if nubmers[i] % 5 == 0:
        sum += nubmers[i]
print(sum)
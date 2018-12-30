
big = []
sample = ['12345','22345','33345','33345','33345','33345','33345','33345',]
for i in range(len(sample)):
    big.append(list(sample[i]))


possible1 = []
possible2 = []


for start in range(len(big)):
    for inc in range(start+1, len(big)-1):
        count = 0
        
        for j in range(len(big[0])):
            if big[start][j] != big[inc][j]:
                count += 1
        
        if count <= 1:
            possible1.append(big[start])
            possible2.append(big[inc])
        

for i in range(len(possible1)):
    possible1[i] = ''.join(possible1[i])
    possible2[i] = ''.join(possible2[i])


print(possible1)
print(possible2)

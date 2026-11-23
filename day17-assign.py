s="aaaabbcccddddffffff"

result={}

for letter in s:
    if letter not in result:
        result[letter]=1
    else:
        result[letter]+=1

print(result)
    
    

final = int(input('final number ?  :'))
lst = []

for i in range(2, final): 
    is_prime = True 
    
  
    for a in range(2, int(i**0.5) + 1):
        if i % a == 0:
            is_prime = False
            break  
    
    if is_prime:
        lst.append(i)

print(lst)
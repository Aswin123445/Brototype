def prime(number):
    if number <= 1:
        return False 
    if number == 2 :
        return True 
    if number % 2 == 0 :
        return False 
    for i in range(3,number,2):
        if number % i == 0 :
            return False 
    return True 
print(prime(13))
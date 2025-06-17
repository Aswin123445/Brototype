def palidrome(string):
    if string == string[::-1]:
        return True 
    
print('palidrome') if palidrome('ardra') else print('not palidrome')
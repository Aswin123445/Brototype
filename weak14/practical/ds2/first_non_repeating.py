def character(string):
    di = {}
    for i in string:
       di[i] = di.get(i,0)+1
    for i in string:
        if di[i] == 1 :
            return i
    
print(character('aswina'))
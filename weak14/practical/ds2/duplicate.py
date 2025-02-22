def remove_duplicat(arr):
    hash_table = {}
    for i in arr:
        if i not in hash_table:
            hash_table[i] = True
    return hash_table.keys()
print(remove_duplicat([10,20,2,20,2]))
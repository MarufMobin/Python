
# 3 no Due
def nearly_equal(a, b):
    count = 0
    i = j = 0
    while (i < len(a) and j < len(b)):
        if (a[i] != b[j]):
            count = count+1
            if (len(a) > len(b)):
                i = i+1
 
            else:
                i = i-1
        if (count > 1):
            return False
        i = i+1
        j = j+1
    if (count < 2):
        return True
 
 
print(nearly_equal('python', 'perl'))
print(nearly_equal('distroy', 'dist'))
print(nearly_equal('pearl', 'perl'))

 
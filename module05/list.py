""" 
    python ar array ar index 0 hote suru hoi ar len-1 a giye ses hoi ar python a index negetive ta -1 hote suru hoi ja reverse order ar set kra jai
"""
numbers = [ 12, 45, 65, 23, 89, 78, 11 ]

# print(numbers[1])
# print(numbers[-6])
#  Array ar akta porsone O print kra jaite pare ja slice blte pari ar aita likhar way holow ( arrayName[ start index : end-1 element ] )


# jodi last index na dewa hoi tile akdom ses porjontow list ar element print hbe 

#  Signature of List Slice list[ start: end: step ]

# print( numbers[ 1: 5 ])
# print( numbers[ 3: ])
# print( numbers[ 3: -3])
# print( numbers[ 3: -3])
# print(numbers[ 2: 7: 2 ])
# print(numbers[ 2: 5: -1 ]) # output [ ]
# print( numbers[ 5: 2 : -1 ])
# print( numbers[ -2: -8 : -1 ])
# print( numbers[ -2: -8 : -2 ])
# print(numbers[ : ]) # full Array 
# print(numbers[ : : -1 ]) # full Array reverse order 
# numbers.append(111)
# newList = [ 0, 33, 333, 444, 555 ]
# numbers.extend(newList)
# numbers.insert( 1, 200)
# numbers.remove(12)
# numbers.pop( 2 )
# numbers.clear()

# Not undestand 
# print(numbers.index( 65, 0, -1 ))

# numbers.append(65)
# numbers.append(65)
# numbers.append(65)
# print(numbers.count(65))

# numbers.reverse()
numbers1 = numbers.copy()
numbers.clear()
print(numbers1)
print(numbers[:]) 
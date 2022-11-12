anagrams = (['eat', 'ate', 'done', 'tea', 'soup', 'node']) 

def find_anagrams( anagrams ):
    result = {}
    for obj in anagrams:
        sort = str( sorted(obj) )

        if sort in result:
            result[sort].append(obj)
        else:
            result[sort] = [obj]

    return result

ans = find_anagrams( anagrams )
print(list(ans.values()))


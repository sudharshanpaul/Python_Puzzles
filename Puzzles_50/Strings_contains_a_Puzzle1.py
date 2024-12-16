
def filter_strings_contains_a(lst):
    ans = []
    for word in lst:
        for letter in word:
            if letter == 'a':
                ans.append(word)
                break
    return ans

lst = ['apple','banana','cherry','date']
print(filter_strings_contains_a(lst))
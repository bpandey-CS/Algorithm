"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
"""

def count_occurences(string, substring):
    try:
        i = string.index(substring)
        return 1 + count_occurences(string[i+1:], substring)
    except ValueError:
        return 0

def add_string(d, prev, string):
    for k in d.keys():
        for arr in d[k]:
            if prev is arr[-1][-1]:
                arr.append(arr[-1]+string)

def generate_substrings(string):
    # generate list of all substring starting with vowels
    d = {}
    for i in range(len(string)):
        arr = d.get(string[i], [[]])
        prev = string[i-1] if i else ''
        add_string(d, prev, string[i]) # immutable so reference is passed
        if string[i] not in arr[0]:
            arr[0].append(string[i])
            d[string[i]] = arr
        else:
            arr.append([string[i]])

    for k in d.keys():
        arr = []
        for a in d[k]:
            arr.extend(a)            
        d[k] = list(set(arr))
    return d

def minion_game(string):
    # your code goes here
    d = generate_substrings(string)
    stuart = 0
    kevin = 0
    for k in d.keys():
        if k in ['A', 'E', 'I', 'O', 'U']:
            kevin += sum([count_occurences(string, d[k][i]) for i in range(len(d[k]))])
        else:
            stuart += sum([count_occurences(string, d[k][i]) for i in range(len(d[k]))])
        
    if kevin < stuart:
        print(f"Stuart {stuart}")
    elif kevin > stuart:
        print(f"Kevin {kevin}")
    else:
        print("Draw")
    return

# def minion_game(string):
#     vowels = 'AEIOU'

#     kevsc = 0
#     stusc = 0
#     for i in range(len(s)):
#         if s[i] in vowels:
#             kevsc += (len(s)-i)
#         else:
#             stusc += (len(s)-i)

#     if kevsc > stusc:
#         print(f"Kevin {kevsc}")
#     elif kevsc < stusc:
#         print(f"Stuart {stusc}")
#     else:
#         print("Draw")
#     return

if __name__ == '__main__':
    s = input()
    minion_game(s)
    
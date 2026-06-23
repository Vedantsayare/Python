#Given a list of words, group all anagrams together into sublists.
#group_anagrams(['eat','tea','tan','ate','nat','bat']) -> [['eat','tea','ate'], ['tan','nat'], ['bat']]

def group_anagrams(words):
    groups = {}

    for word in words:
        key = ''.join(sorted(word))
        groups.setdefault(key, []).append(word)

    return list(groups.values())

print(group_anagrams(['eat','tea','tan','ate','nat','bat']))
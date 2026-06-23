#Given a list with duplicate values, return a new list with duplicates removed but original order preserved.

def remove_dupes(numbers):
    seen = set()
    new_list = []
    for i in numbers:
        if i not in seen:
            seen.add(i)
            new_list.append(i)

    return new_list

removed = remove_dupes([3,1,3,2,1,5])
print(removed)
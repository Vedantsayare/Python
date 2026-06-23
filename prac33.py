#Given a list that contains other lists nested inside it (any depth), flatten it into a single flat list.

def flatten(num):
    new = []

    for i in num:
        if isinstance(i , list):
            new.extend(flatten(i))
        else:
            new.append(i)

    return new

old_list = [1, [2, 3, [4, 5]], 6]
new_list = flatten(old_list)
print(f"{old_list} flattened to {new_list}")
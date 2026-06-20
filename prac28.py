#login attempt log File analyzer

counts = {}
with open("D:/Project/Small tools/logs.txt" , "r") as file:
    for line in file:
        username , timestamp, attempt =line.lower().strip().split(",")
        if attempt == "failed":
           counts[username] = counts.get(username,0) + 1

print(counts)
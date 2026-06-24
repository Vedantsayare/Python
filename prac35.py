#Given a list of [start, end] interval pairs, merge any that overlap and return the merged list.
#merge([[8,10],[1,3],[15,18],[2,6]]) -> [[1,6],[8,10],[15,18]]

def merge(intervals):
    if not intervals:
        return []
    
    intervals.sort(key = lambda x: x[0])
    merged = [intervals[0]]

    for start , end in intervals[1:]:
        last_end = merged[-1][1]

        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged

intervals = [[8,10],[1,3],[15,18],[2,6]]
print(f"Before merging: {intervals}")
print(f"After merging:{merge(intervals)}")
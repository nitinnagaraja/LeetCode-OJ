def removealloccurances(a, val):
    start = 0
    end = len(a)
        
    while start <= end:
        print start, end
        if a[start] == val:
            a[start], a[end - 1] = a[end - 1], a[start]
            end -= 1
        start += 1

    print start, end, a

    if end == len(a):
        return end

    return end - 1

a = map(int, raw_input().split())
k = int(raw_input())

print removealloccurances(a, k)

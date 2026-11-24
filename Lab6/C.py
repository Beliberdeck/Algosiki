import sys

numbers = sys.stdin.read().split()
n = int(numbers[0])                     
m = int(numbers[1])                     

unique_edges = set()                    
for i in range(m):
    first_konets = int(numbers[2 + 2 * i])         
    second_konets = int(numbers[3 + 2 * i])         
    if first_konets != second_konets:                          
        unique_edges.add((min(first_konets, second_konets), max(first_konets, second_konets)))

needed = n * (n - 1) // 2               
print("YES" if len(unique_edges) == needed else "NO")
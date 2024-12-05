import time

def correct(l: list, ruleList: list):
    for (i, num) in enumerate(l):
        for b in ruleList[num]:
            if b in l[0:i]:
                return False
            
    return True

start = time.time()
lines = list(map(lambda s: s.strip(), open('input.txt').readlines()))
rulesIn = list(map(lambda s: list(map(int, s.split('|'))), lines[:lines.index('')]))
listsIn = list(map(lambda l: list(map(int, l.split(','))), lines[lines.index('')+1:]))

ruleList = [[] for _ in range(0, 100)]
for (a, b) in rulesIn:
    ruleList[a].append(b)

result = 0
for l in listsIn:
    if correct(l, ruleList):
        continue

    for (a, rules) in enumerate(ruleList):
        if a not in l:
            continue
        
        bMinInd = 100
        for b in rules:
            if b in l:
                bMinInd = min(bMinInd, l.index(b))

        if bMinInd == 100:
            continue

        aInd = l.index(a)
        if (bMinInd < aInd):
            l.remove(a)
            l.insert(bMinInd, a)
    
    result += l[len(l)//2]
end = time.time()

print(f"{result}, took: {(end-start) * 1000.0}ms")
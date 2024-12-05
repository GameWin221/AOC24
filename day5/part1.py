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

result = sum(map(lambda l: l[len(l)//2] if correct(l, ruleList) else 0, listsIn))
end = time.time()

print(f"{result}, took: {(end-start) * 1000.0}ms")
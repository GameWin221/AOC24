import time

[patterns, designs] = open('input.txt').read().split('\n\n')
patterns = set(patterns.strip().split(', '))
designs = designs.splitlines()

longest_pat_len = 0
for pat in patterns:
    longest_pat_len = max(longest_pat_len, len(pat))

start = time.time()
result = 0
for design in designs:
    # start from largest so that they are checked first later
    sub_patterns = []
    for l in reversed(range(1, longest_pat_len+1)):
        for i in range(len(design) - l + 1):
            p = design[i:i+l]
            if p in patterns:
                sub_patterns.append(p)

    memo = dict()
    
    def verify(i: int) -> int:
        if i in memo:
            return memo[i]
        
        for pat in sub_patterns:
            l = len(pat)
            if i+l > len(design):
                continue

            if design[i:i+l] == pat:
                if i+l == len(design):
                    memo[i] = True
                    return True
                
                if verify(i+l):
                    memo[i] = True
                    return True
        
        memo[i] = False
        return False

    result += 1 if verify(0) else 0
          
end = time.time()
print(f"{result}, took: {(end-start)*1000.0}ms")
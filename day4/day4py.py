import time

start = time.time()

# hihi python
lines = list(map(lambda line: list(map(ord, line)), open('input.txt', 'r').readlines()))
result = sum(map(lambda xy: 1 if lines[xy[1]][xy[0]] == ord('A') and (lines[xy[1]-1][xy[0]-1] ^ lines[xy[1]+1][xy[0]+1] == ord('M') ^ ord('S')) and (lines[xy[1]+1][xy[0]-1] ^ lines[xy[1]-1][xy[0]+1] == ord('M') ^ ord('S')) else 0, [(x,y) for y in range(1, len(lines)-1) for x in range(1, len(lines[0])-1)]))
              
end = time.time()
      
print(f"{result}, took {(end-start) * 1000.0}ms")  
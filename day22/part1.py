import time

start = time.time()
result = 0
for code in list(map(lambda x: int(x.strip()), open('input.txt').readlines())):
    for i in range(2000): 
        code = (code ^ (code << 6)) & 16777215
        code = (code ^ (code >> 5)) & 16777215
        code = (code ^ (code << 11)) & 16777215
    
    result += code

end = time.time()

print(f"{result}, took: {(end-start) * 1000.0}")
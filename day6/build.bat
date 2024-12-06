nasm -f win64 part1.asm -o part1.o
:: Use x64 GNU MinGW linker: https://www.msys2.org/ or https://winlibs.com/
gcc part1.o -o part1.exe
del part1.o

nasm -f win64 part2.asm -o part2.o
:: Use x64 GNU MinGW linker: https://www.msys2.org/ or https://winlibs.com/
gcc part2.o -o part2.exe
del part2.o
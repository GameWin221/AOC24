[regs, instructions] = open('input.txt').read().split('\n\n')

[reg_a, reg_b, reg_c] = list(map(lambda x: int(x[12:]), regs.splitlines()))

def combo(op: int):
    if op <= 3:
        return op
    else:
        return [reg_a, reg_b, reg_c][op-4]

instructions = list(map(int, instructions[9:].split(',')))
ip = 0

while ip < len(instructions):
    opcode = instructions[ip]
    operand = instructions[ip+1]

    if opcode == 0: #adv
        reg_a //= 2**combo(operand)
    elif opcode == 1: #bxl
        reg_b = reg_b ^ operand
    elif opcode == 2: #bst
        reg_b = combo(operand) & 0b111
    elif opcode == 3: #jnz
        if reg_a != 0:
            ip = operand
            continue
    elif opcode == 4: #bxc
        reg_b = reg_b ^ reg_c
    elif opcode == 5: #out
        print(combo(operand)&0b111, end=',')
    elif opcode == 6: #bdv
        reg_b = reg_a // (2**combo(operand))
    elif opcode == 7: #cdv
        reg_c = reg_a // (2**combo(operand))

    ip += 2
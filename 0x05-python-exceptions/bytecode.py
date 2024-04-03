import dis

bytecode = dis.Bytecode(magic_calculation)
for instruction in bytecode:
    print(instruction.opname, instruction.argval)

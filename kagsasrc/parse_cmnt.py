def __init__(value,parseMemory):
    if value.startswith('//'):
        pass
    else:
        parseMemory[4] += value.count('\n')
    return parseMemory
def __init__(value,parseMemory):
    parseMemory=list(parseMemory)
    if value.startswith('//'):
        pass
    else:
        parseMemory[4] += value.count('\n')
    return parseMemory
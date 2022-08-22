

def prettify(counts):
    ret = 'WORD --> NO.OF TIMES USED\n'
    for element in counts:
        ret = ret + element[0] + ' --> ' + str(element[1]) + '\n'
    return ret

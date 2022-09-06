# COMPRESSOR
def splitter(string):
    result = []
    start = 0
    end = 0
    while end < len(string):
        if string[end] == string[start]:
            end += 1
        else:
            result.append(string[start:end])
            result.append(end - start)
            start = end
            end += 1
    result.append(string[start:end])
    result.append(end - start)
    return result


def formater(data):
    result = ''
    for i in range(len(data)):
        if i % 2 == 0:
            result += data[i][0]
        else:
            result += str(data[i])
    return result


def compressor(string):
    return formater(splitter(string))
# DECOMPRESSOR

def liner(lst):
    if lst[0] == '1':
        lst = lst[1:]
    if lst[-1].isalnum():
        pass
    else:
        lst = lst[:-1]
    return lst

def splitter_dec(string):
    result = []
    num = ''
    i = 0
    while i < len(string):
        if string[i].isalpha() and num == '':
            result.append(string[i])
        elif string[i].isalpha():
            result.append(num)
            result.append(string[i])
            num = ''
        else:
            num +=string[i]
        i += 1
    result.append(num)
    return result

def formatter_dec(lst):
    result = ''
    i = 0
    while i < len(lst) - 1:
        if i % 2 == 0:
            result += lst[i] * int(lst[i + 1])
        i += 1
    return result

def decompressor(st):
    return formatter_dec(splitter_dec(liner(st)))







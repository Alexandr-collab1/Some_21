def recurs_sum(spysok):
    if len(spysok) < 2 or spysok == []:
        return spysok
    else:
        return spysok[0] + sum(spysok[1:])

def recurs_kilk(spysok):
    if len(spysok) < 2 or spysok == []:
        return spysok
    else:
        return len(spysok)


def recurs_naibilsh(spysok):
    if len(spysok) < 2 or spysok == []:
        return spysok
    else:
        if spysok[0] > spysok[1] and spysok[0] > spysok[2]:
            return spysok[0]
        else:
            if spysok[1] > spysok[2]:
                return spysok[1]
            else:
                return spysok[2]



print(recurs_sum([2, 4, 8]))
print(recurs_kilk([2, 4, 8]))
print(recurs_naibilsh([8, 1, 7]))
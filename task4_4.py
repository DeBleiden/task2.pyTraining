vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
result = []


def vlanSort(vlanList):
    for i in vlanList:
        if i in result:
            continue
        else:
            result.append(i)
    result.sort()
    print(result)


vlanSort(vlans)

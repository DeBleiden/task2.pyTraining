command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
result = []


def gatheringSimilarVlans(inputString1, inputString2):
    inputList1 = ((inputString1.replace('switchport trunk allowed vlan ', ' ')).strip()).split(',')
    inputList2 = ((inputString2.replace('switchport trunk allowed vlan ', ' ')).strip()).split(',')
    for i in inputList1:
        if i in result:
            continue
        for x in inputList2:
            if i == x:
                result.append(i)
                break
    print(result)


gatheringSimilarVlans(command1, command2)

config = "switchport trunk allowed vlan 1,3,10,20,30,100"
result = []


def listGeneration(string):
    tempList = (string.replace('switchport trunk allowed vlan', ' ')).strip().split(',')
    for i in tempList:
        result.append(i)
    print(result)


listGeneration(config)

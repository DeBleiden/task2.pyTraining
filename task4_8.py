ip = "192.168.3.1"
ipTable = '{:<10}' * 4, '{:>08b}  ' * 4


def ipOutput():
    tempList = ip.split('.')
    for i in ipTable:
        print(i.format(int(tempList[0]), int(tempList[1]), int(tempList[2]), int(tempList[3])))


ipOutput()

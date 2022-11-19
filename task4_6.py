ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
outputStr = '\n{:25} {}' * 5


def stringFlow(ospfRoute, output):
    tempList = (ospfRoute.translate((ospfRoute.maketrans({',': ' ', '[': '', ']': ''})))).split()
    print(output.format(
        'Prefix', tempList[0],
        'AD/Metric', tempList[1],
        'Next-Hop', tempList[3],
        'Last update', tempList[4],
        'Outbound Interface', tempList[5]))


stringFlow(ospf_route, outputStr)

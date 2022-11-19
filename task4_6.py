ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
output = '\n{:25} {}' * 5


def stringFlow():
    tempList = (ospf_route.translate((ospf_route.maketrans({',': ' ', '[': '', ']': ''})))).split()
    print(output.format(
        'Prefix', tempList[0],
        'AD/Metric', tempList[1],
        'Next-Hop', tempList[3],
        'Last update', tempList[4],
        'Outbound Interface', tempList[5]))


stringFlow()

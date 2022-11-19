nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"


def partialReplacement(string):
    result = string.replace("Fast", "Gigabit")
    print(result)


partialReplacement(nat)

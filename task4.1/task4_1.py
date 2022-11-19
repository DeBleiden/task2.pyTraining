nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"


def partialReplacement(string):
    nat2 = nat.replace("Fast", "Gigabit")
    print(nat2)


partialReplacement(nat)

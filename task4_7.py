mac = "AAAA:BBBB:CCCC"


def binaryReplacement():
    print('{:8b}'.format(int(mac.replace(':', ''), base=16)))


binaryReplacement()

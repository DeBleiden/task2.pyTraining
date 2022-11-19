mac = "AAAA:BBBB:CCCC"


def binaryReplacement(string):
    print('{:8b}'.format(int(string.replace(':', ''), base=16)))


binaryReplacement(mac)

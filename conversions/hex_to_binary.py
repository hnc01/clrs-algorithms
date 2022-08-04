def hexToBinary(hex):
    hexToBinaryMap = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'a': '1010',
        'b': '1011',
        'c': '1100',
        'd': '1101',
        'e': '1110',
        'f': '1111'

    }

    hex = hex.lower()

    binaryRepresentation = ''

    for i in range(0, len(hex)):
        # we need to transform every character in hex to a 4-bit string
        binaryRepresentation += hexToBinaryMap[hex[i]]

    return binaryRepresentation

print(hexToBinary('1AC5') == '0001101011000101')
print(hexToBinary('5D1F') == '0101110100011111')
print(hexToBinary('ffffffff'))
def toDecimal(binary):
    isNegative = False

    # we are dealing with a positive number
    if binary[0] == "1":
        isNegative = True

        # we need to get the 2's complement of the number to get its positive decimal representation
        # first we flip all the bits
        binaryFlipped = []

        for i in range(0, len(binary)):
            if binary[i] == "0":
                binaryFlipped.append("1")
            else:
                binaryFlipped.append("0")

        # now we add 1 to the end of it
        if binaryFlipped[-1] == "0":
            # we just add 1 instead of the 0
            binaryFlipped[-1] = "1"
        else:
            # we need to do the addition
            # we know that the last bit is 1 so we set the last bit to 0
            # and make carry = 1
            binaryFlipped[-1] = 0
            carry = 1

            i = -2

            while carry > 0:
                if binaryFlipped[i] == "0":
                    # we just replace it with 1 and we're done
                    binaryFlipped[i] = "1"
                    carry = 0
                else:
                    # we replace it with 0 and keep the carry
                    binaryFlipped[i] = "0"
                    carry = 1

                i -= 1

                if i + len(binaryFlipped) < 0:
                    break

        binary = "".join(binaryFlipped)

    power = 0

    decimal = 0

    for i in range(len(binary) - 1, -1, -1):
        decimal += int(binary[i]) * (2 ** power)

        power += 1

    if isNegative:
        return - decimal
    else:
        return decimal

print(toDecimal("00001010"))
print(toDecimal("11111001"))
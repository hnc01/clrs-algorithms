def toBinary(num):
    if num == 0:
        return "0"
    else:
        # this works for positive and negative numbers
        binaryRepresentation = ""

        for i in range(0, 32):
            # this will isolate the right-most bit in num
            binaryRepresentation = str(num & 1) + binaryRepresentation
            num >>= 1

            # this would remove the trailing 0s on the left
            # so we'd get 1010 instead of 00000000000000000000000000001010
            if num == 0:
                break

        return binaryRepresentation

print(toBinary(10))
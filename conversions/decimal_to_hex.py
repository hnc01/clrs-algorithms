class Solution:
    def toHex(self, num: int) -> str:
        hexRepresentation = ""

        characters = "0123456789abcdef"

        # we have 32 bits but we need to treat each 4 bits separately
        # 32 / 4 = 8 iterations
        for i in range(0, 8):
            # we need to isolate the last 4 bits
            # to do that, we & with 15 which is 0000 ... 0000 1111
            last4Bits = num & 15

            # now last4Bits will act like our index in characters
            hexRepresentation = characters[last4Bits] + hexRepresentation

            # now we need to get rid of the last 4 bits
            num >>= 4

            if num == 0:
                break

        return hexRepresentation

class Solution1:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        elif num > 0:
            hexRepresentation = []

            while num > 0:
                remainder = num % 16

                # we can represent it by digits 0 to 9
                # these digit characters start at 48
                if remainder < 10:
                    hexRepresentation.append(chr(remainder + ord('0')))
                else:
                    # we need to use letters to represent the character
                    hexRepresentation.append(chr(remainder + ord('a')))

                num //= 16

            hexRepresentation.reverse()

            return "".join(hexRepresentation)
        else:
            # the number is negative so we need use 2's complement method
            # first we need to get the absolute value of the number
            num = -1 * num

            # now we transform this into binary
            binaryRepresentation = []

            while num > 0:
                remainder = num % 2

                binaryRepresentation.append(remainder)

                num //= 2

            binaryRepresentation.reverse()

            # we need 32 bits to represent our number
            while len(binaryRepresentation) < 32:
                binaryRepresentation.insert(0, 0)

            # now we need to flip all the bits
            for i in range(0, len(binaryRepresentation)):
                binaryRepresentation[i] = int(not binaryRepresentation[i])

            # now we add 000...0001 to the binary representation to get 2's complement
            if binaryRepresentation[-1] == 0:
                # adding the 1 at that bit is only a matter of flipping the 0 into 1
                binaryRepresentation[-1] = 1
            else:
                # we need to add the bits together
                # 1 + 1 = 10 so we keep the 0 at [-1] and carry the 1
                binaryRepresentation[-1] = 0
                carry = 1

                i = -2

                # we keep going until our carrry is 0 because the rest of the bits
                # we're adding to binaryRepresentation are 0
                while carry > 0:
                    if binaryRepresentation[i] == 0:
                        binaryRepresentation[i] = carry
                        carry = 0
                    else:
                        binaryRepresentation[i] = 0
                        carry = 1

                    i -= 1

            # now that we have 2's complement, we need to isolate every 4 bits to get our hex representation
            hexRepresentation = []

            start = 0

            while start < len(binaryRepresentation):
                currentBits = binaryRepresentation[start:start + 4]

                currentNumber = (currentBits[0] * (2 ** 3)) + (currentBits[1] * (2 ** 2)) + (currentBits[2] * (2 ** 1)) + (currentBits[3] * (2 ** 0))

                if currentNumber < 10:
                    hexRepresentation.append(chr(48 + currentNumber))
                else:
                    hexRepresentation.append(chr(55 + currentNumber).lower())

                start += 4

            return "".join(hexRepresentation)


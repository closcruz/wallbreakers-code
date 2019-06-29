# Counts the unique morse code representation of a list of words


class MorseCode:
    def uniqueMorse(self, words):
        morseTable = {chr(ord('a') + n): i for (n, i) in enumerate([".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
                                                                    ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."])}

        return len(set(["".join([morseTable[c] for c in w])
                        for w in words]))


print(MorseCode().uniqueMorse(["gin", "zen", "gig", "msg"]))

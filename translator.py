class MorseCodeTranslator():
    def __init__(self) -> None:
        self.MORSE_CODE = {
            "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
            "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
            "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
            "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----",
            "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
            "8": "---..", "9": "----.", "0": "-----"
        }
        self.CODE_CHAR_SET = [".", "-", " "]

    def translate(self, input_text) -> str:
        "Translates input to and from morse code as appropriate."
        # check to see if underscores used, if so replace with dashes
        if "_" in input_text:
            input_text = input_text.replace("_", "-")
        if self.determine_direction(input_text):
            return self.translate_from(input_text)
        return self.translate_to(input_text)

    def determine_direction(self, input_text) -> bool:
        """Determines if input should be translated from code to plain text
        or plain text to code."""
        # each character is evaluated against the CODE_CHAR_SET
        matched_list = [char in self.CODE_CHAR_SET for char in input_text]
        # returns True only if all in matched list are True
        return all(matched_list)

    def translate_to(self, input_text) -> str:
        """Translates to morse code from plain text."""
        output = ""
        for char in input_text:
            # if the character is a space, a double space is added to 
            # distinguish between each word
            if char == " ":
                output += "  "
                continue
            elif char.upper() not in self.MORSE_CODE:
                # if character doesn't have associated code, it is ignored
                # and nothing is added instead
                output += ""
                continue
            # code for character added to output with trailing space to
            # separate from other characters
            output += self.MORSE_CODE[char.upper()] + " "
        return output

    def translate_from(self, input_text) -> str:
        """Translates from morse code to plain text."""
        # add "@__@" in place of double spaces to differentiate between words
        cleaned_input = input_text.replace("  ", " @__@ ")

        # split to list of individual characters
        code_list = cleaned_input.split()

        output = ""
        for entry in code_list:
            # add spaces as appropriate with distinguishing tag added above
            if entry == "@__@":
                output += " "
            # loop through dictionary to get corresponding letter
            for char, code in self.MORSE_CODE.items():
                if entry == code:
                    output += char
        return output

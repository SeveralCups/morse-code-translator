from translator import MorseCodeTranslator
import pyperclip


class App(MorseCodeTranslator):
    def __init__(self) -> None:
        super().__init__()

    def run(self) -> None:
        """Runs the app. Prompts for input and performs appropriate
        translation."""
        # loops until user inputs '!exit' command
        print("Welcome to the morse code translator!\nType '!exit' to quit.")

        while True:
            user_input = input("Enter text or morse code to translate: ")

            if user_input == "!exit":
                break

            # input is translated accordingly
            output = self.translate(user_input)
            # result is copied to user clipboard and printed
            pyperclip.copy(output)
            print(output)


# MAIN
if __name__ == "__main__":
    app = App()
    app.run()

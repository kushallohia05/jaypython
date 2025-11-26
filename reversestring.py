class StringReverser:
    def __init__(self, text):
        self.__reversed = text[::-1]  # private variable

    def get(self):
        return self.__reversed  # public getter


# Take user input
user_text = input("Enter a string: ").strip()
reverser = StringReverser(user_text)

# Show reversed string
print("Reversed string:", reverser.get())
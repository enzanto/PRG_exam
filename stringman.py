class sentence:
    def __init__(self, string: str, delim: str):
        self.string = string
        self.delim = delim

    def strLength(self) -> int:
        print(f"The length of the string is {len(self.string)}")
        return len(self.string)

    def cutString(self) -> list[str]:
        cut_string = self.string.split(self.delim)
        return cut_string

    def showWordAt(self, string_list: list[str], location: int) -> str:
        word = string_list[location]
        print(f"The word at index {location} is {word}")
        return word

    def showIndexAt(self, string_list: list[str], word: str) -> int:
        location = string_list.index(word)
        print(f"the index for the word {word} is {location}")
        return location

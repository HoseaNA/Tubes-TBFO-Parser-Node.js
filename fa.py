# SIGMA
# upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
#          "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# underscore = ['_']
# anotherAscii = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.',
#                 '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~'] -> 8 bit printable except whitespaces

# STATES
# start, dead, final -> accepted state is final state

finiteAutomata = {
    'start': {
        'A': 'final', 'B': 'final', 'C': 'final', 'D': 'final', 'E': 'final', 'F': 'final', 'G': 'final', 'H': 'final', 'I': 'final', 'J': 'final', 'K': 'final', 'L': 'final', 'M': 'final', 'N': 'final', 'O': 'final', 'P': 'final', 'Q': 'final', 'R': 'final', 'S': 'final', 'T': 'final', 'U': 'final', 'V': 'final', 'W': 'final', 'X': 'final', 'Y': 'final', 'Z': 'final',
        'a': 'final', 'b': 'final', 'c': 'final', 'd': 'final', 'e': 'final', 'f': 'final', 'g': 'final', 'h': 'final', 'i': 'final', 'j': 'final', 'k': 'final', 'l': 'final', 'm': 'final', 'n': 'final', 'o': 'final', 'p': 'final', 'q': 'final', 'r': 'final', 's': 'final', 't': 'final', 'u': 'final', 'v': 'final', 'w': 'final', 'x': 'final', 'y': 'final', 'z': 'final',
        '_': 'final', '0': 'dead', '1': 'dead', '2': 'dead', '3': 'dead', '4': 'dead', '5': 'dead', '6': 'dead', '7': 'dead', '8': 'dead', '9': 'dead',
        '!': 'dead', '"': 'dead', '#': 'dead', '$': 'dead', '%': 'dead', '&': 'dead', "'": 'dead', '(': 'dead', ')': 'dead', '*': 'dead', '+': 'dead', ',': 'dead', '-': 'dead', '.': 'dead', '/': 'dead', ':': 'dead', ';': 'dead', '<': 'dead', '=': 'dead', '>': 'dead', '?': 'dead', '@': 'dead', '[': 'dead', '\\': 'dead', ']': 'dead', '^': 'dead', '`': 'dead', '{': 'dead', '|': 'dead', '}': 'dead', '~': 'dead'
    },
    'dead': {
        'A': 'dead', 'B': 'dead', 'C': 'dead', 'D': 'dead', 'E': 'dead', 'F': 'dead', 'G': 'dead', 'H': 'dead', 'I': 'dead', 'J': 'dead', 'K': 'dead', 'L': 'dead', 'M': 'dead', 'N': 'dead', 'O': 'dead', 'P': 'dead', 'Q': 'dead', 'R': 'dead', 'S': 'dead', 'T': 'dead', 'U': 'dead', 'V': 'dead', 'W': 'dead', 'X': 'dead', 'Y': 'dead', 'Z': 'dead',
        'a': 'dead', 'b': 'dead', 'c': 'dead', 'd': 'dead', 'e': 'dead', 'f': 'dead', 'g': 'dead', 'h': 'dead', 'i': 'dead', 'j': 'dead', 'k': 'dead', 'l': 'dead', 'm': 'dead', 'n': 'dead', 'o': 'dead', 'p': 'dead', 'q': 'dead', 'r': 'dead', 's': 'dead', 't': 'dead', 'u': 'dead', 'v': 'dead', 'w': 'dead', 'x': 'dead', 'y': 'dead', 'z': 'dead',
        '_': 'dead', '0': 'dead', '1': 'dead', '2': 'dead', '3': 'dead', '4': 'dead', '5': 'dead', '6': 'dead', '7': 'dead', '8': 'dead', '9': 'dead',
        '!': 'dead', '"': 'dead', '#': 'dead', '$': 'dead', '%': 'dead', '&': 'dead', "'": 'dead', '(': 'dead', ')': 'dead', '*': 'dead', '+': 'dead', ',': 'dead', '-': 'dead', '.': 'dead', '/': 'dead', ':': 'dead', ';': 'dead', '<': 'dead', '=': 'dead', '>': 'dead', '?': 'dead', '@': 'dead', '[': 'dead', '\\': 'dead', ']': 'dead', '^': 'dead', '`': 'dead', '{': 'dead', '|': 'dead', '}': 'dead', '~': 'dead'
    },
    'final': {
        'A': 'final', 'B': 'final', 'C': 'final', 'D': 'final', 'E': 'final', 'F': 'final', 'G': 'final', 'H': 'final', 'I': 'final', 'J': 'final', 'K': 'final', 'L': 'final', 'M': 'final', 'N': 'final', 'O': 'final', 'P': 'final', 'Q': 'final', 'R': 'final', 'S': 'final', 'T': 'final', 'U': 'final', 'V': 'final', 'W': 'final', 'X': 'final', 'Y': 'final', 'Z': 'final',
        'a': 'final', 'b': 'final', 'c': 'final', 'd': 'final', 'e': 'final', 'f': 'final', 'g': 'final', 'h': 'final', 'i': 'final', 'j': 'final', 'k': 'final', 'l': 'final', 'm': 'final', 'n': 'final', 'o': 'final', 'p': 'final', 'q': 'final', 'r': 'final', 's': 'final', 't': 'final', 'u': 'final', 'v': 'final', 'w': 'final', 'x': 'final', 'y': 'final', 'z': 'final',
        '_': 'final', '0': 'final', '1': 'final', '2': 'final', '3': 'final', '4': 'final', '5': 'final', '6': 'final', '7': 'final', '8': 'final', '9': 'final',
        '!': 'dead', '"': 'dead', '#': 'dead', '$': 'dead', '%': 'dead', '&': 'dead', "'": 'dead', '(': 'dead', ')': 'dead', '*': 'dead', '+': 'dead', ',': 'dead', '-': 'dead', '.': 'dead', '/': 'dead', ':': 'dead', ';': 'dead', '<': 'dead', '=': 'dead', '>': 'dead', '?': 'dead', '@': 'dead', '[': 'dead', '\\': 'dead', ']': 'dead', '^': 'dead', '`': 'dead', '{': 'dead', '|': 'dead', '}': 'dead', '~': 'dead'
    }
}


class FA:
    def __init__(self, string) -> None:
        self.currentState = 'start'
        self.accept = 'final'
        self.string = string

    def readSymbol(self):
        for char in self.string:
            self.currentState = finiteAutomata[self.currentState][char]
        return self.currentState == self.accept
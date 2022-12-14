import re
from pathlib import Path
import itertools
import sys
import fa

class CykParser:

    # Menginisialisasi program utama dengan menerima path file cnf. path file test.
    # chomsky grammar (cnf dari txt file), kondisi string valid atau tidak, input text yang dibentuk
    # menjadi list, tabel cyk, hasil pembacaan file test, dan err_line yang menyimpan lokasi kesalahan
    # penulisan string
    def __init__(self, cnfPath, testFile):
        self.cnfPath = cnfPath
        self.testFile = testFile
        self.chomskyGrammar = {}
        self.validString: bool
        self.inputText: list
        self.cykTable: list
        self.contents: str
        self.err_line = 0

    # Membaca file cnf dari path yang sudah diinisialisasi dan diolah untuk 
    # dimasukkan ke dalam chomskuGrammar
    def __loadGrammar(self):
        f = open(self.cnfPath, "r")
        rules = f.readlines()
        for i in range(len(rules)):
            origin, res = rules[i].split(' -> ')
            options = res.replace(" ", "").removesuffix("\n").split('|')
            for j in range(len(options)):
                value = self.chomskyGrammar.get(options[j])
                if (value):
                    self.chomskyGrammar[options[j]].append(origin)
                else:
                    self.chomskyGrammar.update({options[j]: [origin]})
        f.close()

    # Menganalisis string dan memvalidasikannya
    def __string_analyzer(self):
        stack_like = []
        current_line = 0
        for line in self.contents.split("\n"):
            current_line += 1
            for char in line:
                if char == '\'' or char == '\"':
                    if len(stack_like) and stack_like[-1] == char:
                        stack_like = stack_like[:-1]
                    else:
                        stack_like.append(char)
            if len(stack_like):
                self.err_line = current_line
                break
            stack_like.clear()

        if not self.err_line:
            new_input = []
            for line in self.contents.split("\n"):
                new_input.append(re.sub('\"(.*?)\"|\'(.*?)\'', '"string"', line))
            self.validString = True
            self.contents = "\n".join(new_input)
        else:
            self.validString = False

    # Melakukan formatting pada setiap ekspresi yang ada sehingga membentuk simbol
    # terminal yang valid dan membersihkan string kosong
    def __readInputFile(self):
        f = open(self.testFile, "r")
        self.contents = f.read()
        self.__string_analyzer()
        if not self.validString:
            return
        contents = self.contents.split()
        f.close()

        delimiters = [':', ',', '\.', '=', '<', '>', '!', r'\+',
                      '-', r'\*', '/', r'\*\*', r'\(', r'\)', r'\[', r'\]', r'\'\'\'', r'\'', r'\"']

        format = r"(" + "|".join(delimiters) + r")"
        contents = [re.split(format, content) for content in contents]
        contents = list(itertools.chain(*contents))

        def exclude(x): return x != ''
        cleaned_contents = list(filter(exclude, contents))

        self.validString = True
        self.inputText = cleaned_contents

    # Memasukkan ekspresi ke dalam tabel cyk
    def __insertTable(self, level, position, key):
        for rule in self.chomskyGrammar[key]:
            self.cykTable[level][position].add(rule)

    # Melakukan validasi variabel, angka, dan string dan semua ekspresi lainnya
    # dan diletakkan pada cyk table
    def __makeCYKTable(self):
        FA = fa.FA
        inputText = self.inputText
        insertTable = self.__insertTable
        self.cykTable = [[set() for _ in range(i)]
                         for i in range(len(inputText), 0, -1)]

        for i in range(len(self.inputText)):
            if inputText[i] in self.chomskyGrammar:
                insertTable(0, i, self.inputText[i])
            else:
                variable = FA(inputText[i])
                if variable.readVar():
                    insertTable(0, i, 'variable')
                if re.match(r'[0-9]*', inputText[i]):
                    insertTable(0, i, 'number')
                if re.match(r'[A-z0-9]*', inputText[i]):
                    insertTable(0, i, 'string')

        for i in range(1, len(inputText)):
            for j in range(len(inputText)-i):
                for k in range(i):
                    for p in self.cykTable[k][j]:
                        for p1 in self.cykTable[i-k-1][j+k+1]:
                            p2 = p + p1
                            if p2 in self.chomskyGrammar:
                                insertTable(i, j, p2)

    # Menunjukkan hasil apakah kode valid atau tidak
    def __result(self):
        if self.cykTable and 'S' in self.cykTable[-1][-1]:
            print("Accepted")
        else:
            print("Syntax error!")

    # Memanggil setiap fungsi berdasarkan kondisi yang memenuhi
    def validate(self):
        self.__loadGrammar()
        self.__readInputFile()
        if self.validString:
            self.__makeCYKTable()
            self.__result()
        else:
            print(f"String error in line {self.err_line}")

# Memulai program utama
if __name__ == "__main__":
    if len(sys.argv) > 1:
        testPath = str(sys.argv[1])
    else:
        testPath = input("Path to test file: ")
    workdir = Path(__file__).absolute().parent
    cykParser = CykParser(workdir/"cnf.txt", workdir/testPath)
    cykParser.validate()
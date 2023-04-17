import string

# Alphabet


class Alphabet:
    def __init__(self, language, letters):
        self.language = language
        self.letters = list(letters)

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):

    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def letters_num(self):
        return EngAlphabet.__letters_num

    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        else:
            return False

    @ staticmethod
    def example(text_en):
        return text_en


if __name__ == '__main__':

    eng_alphabet = EngAlphabet()
    eng_alphabet.print()
    print(f'Количество букв: {eng_alphabet.letters_num()}')
    print(eng_alphabet.is_en_letter('F'))
    print(eng_alphabet.is_en_letter('Щ'))
    print(eng_alphabet.example('Example: Hello,my dear friend!'))

# homework


class Tomato:
    states = {1: "появление всходов", 2: "первый лист", 3: "разрастание корней",
              4: "образование бутонов", 5: "цветение", 6: "созревание плода"}

    def __init__(self, index):
        self._index = index
        self._state = Tomato.states[1]

    def grow(self):
        self._state += 1
        print(self._state)

    def is_ripe(self):
        if self._state == Tomato.states[6]:
            print('Томат созрел')
        else:
            print('Томат еще не созрел')


class TomatoBush:

    def __init__(self, numb_tomato):
        self.tomatoes = [Tomato(i) for i in range(numb_tomato)]
        self.numb_tomato = numb_tomato

    def grow_all(self):
        for object in self.tomatoes:
            object.grow()

    def all_are_ripe(self):
        return all([object.is_ripe() for object in self.tomatoes])

    def give_away_all(self):
        return self.tomatoes.clear()


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print('Урожай собран, все томаты созрели')
        else:
            print("Не созрел урожай!")

    @staticmethod
    def knowledge_base():
        print('Справка по садоводству \nСтадии созревания помидоров: появление всходов, первого настоящего листа, '
              'разрастание надземной массы и корней, образование бутонов, цветение, формирование и созревание плодов.')


tomato_bush = TomatoBush(3)
garden_1 = Gardener('Bob', 'Tomato')
garden_1.knowledge_base()
garden_1.work()
garden_1.harvest()































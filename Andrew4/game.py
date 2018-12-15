import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit
import random


class People:
    def __init__(self, name, role, rolestr):
        self.name = name
        self.role = role
        self.rolestr = rolestr


class Sunduk:
    def __init__(self, thing):
        self.thing = thing


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def ShowInside1(self):
        global sunduk
        self.sunduk_btn1.setText(sunduk[0].thing)
        self.end(0)

    def ShowInside2(self):
        global sunduk
        self.sunduk_btn2.setText(sunduk[1].thing)

        self.end(1)

    def ShowInside3(self):
        global sunduk
        self.sunduk_btn3.setText(sunduk[2].thing)
        self.end(2)

    def createInterface(self):

        global things, things2, people, gold, lifes, labels, sunduk, level, numpeop, people2, people3
        sunduk = []  # распределем вещи по сундука
        t = [0, 1, 2]
        for i in range(3):
            sunduk.append(Sunduk(""))
        i = random.choice(t)
        sunduk[i].thing = things[0]
        del t[i]
        j = random.choice(t)
        sunduk[j].thing = things[1]
        sunduk[3 - i - j].thing = random.choice(things[2:])

        # создаем фразы
        self.dalee.setEnabled(False)

        kolvoKnigts = 0
        kolvoLiars = 0
        for x in range(3):
            numpeop[x] = random.choice(range(0, len(people2[level])))
            people3[x] = people2[level][numpeop[x]]
            del people2[level][numpeop[x]]

        for x in range(3):
            j = random.choice(range(3))
            if j < 3:
                y = random.choice(range(len(things)))
                if (people3[x].role and sunduk[j].thing == things[y]) or (
                        not (people3[x].role) and sunduk[j].thing != things[y]):
                    frase = "В " + str(j + 1) + " сундуке есть " + things[y]
                else:
                    frase = "В " + str(j + 1) + " сундуке нет " + things2[y]
            """
            elif j < 3:
                y = random.choice(range(len(things)))
                if (people3[x].role and sunduk[j].thing == things[y]) or (
                        not (people3[x].role) and sunduk[j].thing != things[y]):
                    frase = "В " + str(j + 1) + " сундуке есть " + things[y]
                else:
                    frase = "В " + str(j + 1) + " сундуке нет " + things2[y]
            """
            self.labels[x + 3].setText(people3[x].name + ": " + frase)
            self.labels[x + 3].adjustSize()

            if people3[x].role:
                kolvoKnigts += 1
            else:
                kolvoLiars += 1
        if kolvoKnigts and kolvoLiars:
            self.labels[2].setText("Кол-во рыцарей: " + str(kolvoKnigts) + ", кол-во лжецов: " + str(kolvoLiars))
            self.labels[2].adjustSize()
        else:
            self.labels[2].setText("У всех  одинаковая роль")
            self.labels[2].adjustSize()

        self.sunduk_btn1.setText("Первый сундук")
        self.sunduk_btn1.setEnabled(True)
        self.sunduk_btn2.setText("Второй сундук")
        self.sunduk_btn2.setEnabled(True)
        self.sunduk_btn3.setText("Третий сундук")
        self.sunduk_btn3.setEnabled(True)

    def end(self, numSund):
        global sunduk, gold, lifes, level, thing
        self.sunduk_btn1.setEnabled(False)
        self.sunduk_btn2.setEnabled(False)
        self.sunduk_btn3.setEnabled(False)

        if sunduk[numSund].thing == things[0]:
            gold += 1
        elif sunduk[numSund].thing == things[1]:
            lifes -= 1
        elif sunduk[numSund].thing == things[2]:
            if gold >= 5:
                gold -= 5
            else:
                lifes -= 3

        elif sunduk[numSund].thing == things[3]:
            lifes += 1

        self.labels[1].setText("кол-во золота: " + str(gold) + "    кол-во жизней: " + str(lifes))
        self.labels[1].adjustSize()
        if lifes > 0:
            level += 1
            self.dalee.setEnabled(True)

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('игра')
        global things, things2, people, gold, lifes, labels, sunduk, level, numpeop, people2, people3
        level = 0
        things = ["Золото", "Змеи", "Гном", "Доп.Жизнь"]
        things2 = ["Золота", "Змей", "Гнома", "Доп.Жизни"]

        # создаем персонажей
        names = ["Вася", "Петя", "Вова", "Игорь", "Костя", "Андрей", "Ваня", "Юра", "Миша", "Дима", "Даня", "Саша",
                 "Лёша",
                 "Влад", "Сергей", "Гоша", "Олег", "Гриша", "Илья", "Слава", "Гена"]

        people = []
        for i in range(len(names)):
            role = random.choice([0, 1])
            if role:
                rolestr = "Рыцарь"
            else:
                rolestr = "Лжец"
            people.append(People(names[i], role, rolestr))
        people2 = []
        for i in range(len(names) - 2):
            people2.append(people[0:i + 4])

        people3 = [people[0], people[0], people[0]]
        numpeop = [0, 0, 0]
        gold = 0
        lifes = 3
        self.labels = []
        for x in range(6):
            self.labels.append(QLabel(self))
            self.labels[x].setText("")
            self.labels[x].move(10, x * 15)

        self.labels[0].setText("Выбери верный сундук")
        self.labels[1].setText("кол-во золота: " + str(gold) + "    кол-во жизней: " + str(lifes))

        self.sunduk_btn1 = QPushButton("Первый сундук", self)  # создаем кнопки
        self.sunduk_btn1.resize(self.sunduk_btn1.sizeHint())
        self.sunduk_btn1.move(5, 100)
        self.sunduk_btn1.clicked.connect(self.ShowInside1)

        self.sunduk_btn2 = QPushButton("Второй сундук", self)
        self.sunduk_btn2.resize(self.sunduk_btn2.sizeHint())
        self.sunduk_btn2.move(105, 100)
        self.sunduk_btn2.clicked.connect(self.ShowInside2)

        self.sunduk_btn3 = QPushButton("Третий сундук", self)
        self.sunduk_btn3.resize(self.sunduk_btn3.sizeHint())
        self.sunduk_btn3.move(205, 100)
        self.sunduk_btn3.clicked.connect(self.ShowInside3)

        self.dalee = QPushButton("Далее", self)
        self.dalee.resize(self.dalee.sizeHint())
        self.dalee.move(105, 140)
        self.dalee.clicked.connect(self.createInterface)

        self.createInterface()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

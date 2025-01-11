
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QHBoxLayout, QGroupBox, QButtonGroup
from random import *

app = QApplication([])
main_win = QWidget()

main_win.setWindowTitle('Memo Card')
question = QLabel('Самый сложный вопрос в мире!')
RadioGroupBox = QGroupBox('Варианты ответов')
btn_answer1 = QRadioButton('Энцы')
btn_answer2 = QRadioButton('Смурфы')
btn_answer3 = QRadioButton('Чульмцы')
btn_answer4 = QRadioButton('Алеуты')

button = QPushButton('Ответить')


layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(btn_answer1)
layout_ans2.addWidget(btn_answer2)
layout_ans3.addWidget(btn_answer3)
layout_ans3.addWidget(btn_answer4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QVBoxLayout()

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результаты теста')

doubt = QLabel('Правильно/Неправильно')
answer = QLabel('тут будет ответ!')

layout_axis = QVBoxLayout()

layout_axis.addWidget(doubt, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_axis.addWidget(answer, alignment=(Qt.AlignHCenter | Qt.AlignVCenter ))

AnsGroupBox.setLayout(layout_axis)

answer_ = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)

RadioGroupBox.show()
AnsGroupBox.hide()

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')

class Question():
    def __init__(self, question1, right_answer, wrong1, wrong2, wrong3):
        self.question1 = question1
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Итальянский', 'Испанский', 'Бразильский'))
question_list.append(Question('Кто написал стихотворение "19 октября"', 'Пушкин', 'Маяковский', 'Ахматова', 'Есенин'))
question_list.append(Question('Если U(напряжение) делить на R(сопротивление), то в ответе получат', 'I', 'A', 'F', 't'))
question_list.append(Question('Какой объём крови теряется при кровотечении средней тяжести','1,5-2л', '500мл', '750-1500мл', 'более 2л'))
question_list.append(Question('К какому отряду относят семейство тушканчиковых', 'Грызуны', 'Насекомоядные', 'Хищные', 'Зайцеобразные' ))
question_list.append(Question('Какие арки могут быть в автомобиле', 'Цельные', 'Килевидные', 'Многолопастные', 'Полукруглые'))
question_list.append(Question('Что не считается за органоид клетки?', 'Цитоплазма', 'Комплекс Гольджи', 'Митохондрии', 'Пластиды'))
question_list.append(Question('Какую реакцию организм даёт на смешение снотворного с алкоголем', 'токсическое поражение мозга', 'отсутствие эффекта', 'остановка дыхания', 'токсическое поражение печени'))
question_list.append(Question('Какое животное принято считать мусорным', 'енот', 'осёл', 'свинья', 'пёс'))
question_list.append(Question('Какой вид дальтонизма характеризуется нарушением цветовых ощущений в сине-фиолетовой области спктра', 'тританомалия', 'ахроматизм', 'протаномалия', 'тританотопия'))

def ask(q: Question):
    shuffle(answer_)
    answer_[0].setText(q.right_answer)
    answer_[1].setText(q.wrong1)
    answer_[2].setText(q.wrong2)
    answer_[3].setText(q.wrong3)
    question.setText(q.question1)
    answer.setText(q.right_answer)
    show_question()

def show_correct(unclear):
    doubt.setText(unclear)
    show_result()
    
def check_answer():
    if answer_[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистика:\n-Всего вопросов:', main_win.total, '\n-Правильных ответов:', main_win.score)
        total_rating = (main_win.score / main_win.total) * 100
        print('Рейтинг:', total_rating, '%')
    else:
        if answer_[1].isChecked() or answer_[2].isChecked() or answer_[3].isChecked():
            show_correct('Неправильно!')

def next_question():
    main_win.total += 1
    print('Статистика:\n-Всего вопросов:', main_win.total, '\n-Правильных ответов:', main_win.score)
    total_rating = (main_win.score / main_win.total) * 100
    print('Рейтинг:', total_rating, '%')
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)
    

def click_okey():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()




button.clicked.connect(click_okey)


layout_card = QVBoxLayout()
layout_line1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(button, stretch=2)
layout_line3.addStretch(1)
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=7)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=2)


layout_card.setSpacing(5)
main_win.setLayout(layout_card)

main_win.score = 0
main_win.total = 0

next_question()



#отображение окна приложения 
main_win.show()
app.exec_()

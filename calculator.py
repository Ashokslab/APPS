from  PyQt5.QtCore import Qt
from  PyQt5.QtWidgets import QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QApplication,QGridLayout,QLineEdit


app = QApplication([])
main = QWidget()
main.setWindowTitle("CALCULATOR")
main.resize(500,700)

textbox = QLineEdit()
grid = QGridLayout()

buttons = ["7","8","9","/",
           "4","5","6","*",
           "3","2","1","-",
           "0",".","=","+"
]

clear = QPushButton("clear")
delete = QPushButton("<")

def button_click():
    button = app.sender()
    text = button.text()

    if text ==  "=":
        symbol = textbox.text()
        try:
            res = eval(symbol)
            textbox.setText(str(res))
        
        except Exception as e:
            print("error:",e)

    if  text == "clear":
        textbox.clear()

    if text == "<":
        current_value = textbox.text()
        textbox.setText(current_value[:-1])

    else:
        current_value = textbox.text()
        textbox.setText(current_value+text)





row = 0 
col = 0

for text in buttons:
    button = QPushButton(text)
    button.clicked.connect(button_click)
    grid.addWidget(button, row, col)
    col += 1
    if col > 3:
        col = 0
        row += 1
 




#design
layout = QVBoxLayout()
layout.addWidget(textbox)
layout.addLayout(grid)




buttonrow = QHBoxLayout()
buttonrow.addWidget(clear)
buttonrow.addWidget(delete)

clear.clicked.connect(button_click)
delete.clicked.connect(button_click)


layout.addLayout(buttonrow)
main.setLayout(layout)
main.show()
app.exec_()

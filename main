from tkinter import *
#from contracts import contract

class Cell(Button):

    #name - положение клетки!
    # 1 цирфа это по Х, вторая по У
    def __init__(self, x, y, size, name):
        super(Cell, self).__init__(root,
                                   text='',
                                   width=size,
                                   height=size,
                                   bg='black',
                                   activebackground='grey', command=self.click_button)
        self.alive = False
        self.x = x
        self.y = y
        self.name = name
        self.place(x=self.x, y=self.y)

    # функция которая дает возможность кликать на кнопки, не знаю зачем это тебе пигу, вроде и так понятно)))))))
    def click_button(self):
        self.alive = True
        self.configure(bg='white')


#@contract вот с ним я не совсем разобралась но вот попыталсь прописать все тесты максимально возможные

# функция создающая все клетки на поле, они уже сразу объекты типа Клетка
def background(size):
    '''
    :type size: int, < 40, not zero
    :rtype: list(str)
    '''
    cells = []
    for j in range(0, 500, size):
        for k in range(0, 400, size):
            our_cell = Cell(j, k, size, str(int(j / size + 1)) + ',' + str(int(k / size + 1)))
            cells.append(our_cell)
    return cells

#@contract
# здесь поределяем все живые клетки на поле в самом начале
def live_cells(cells):
    """
    :param cells: list, not null
    :rtype: list(tuple)
    """
    living = []
    for cell in cells:
        if cell.alive:
            living.append((cell, cell.name))
    # living содержит набор кортежей, в которых первый элемент это сама клетка, а второй это ее положение, т. е. строка и столбец
    print(living)



root = Tk()
root.title('Игра ЖИЗНЬ')
root.geometry('500x400')
size = int(input('Введите сторону клетки: '))
cells = background(size)

but = Button(text='Start',
             bg='white',
             fg='black',
             command=lambda: live_cells(cells))
but.pack()

root.mainloop()

from tkinter import *
from contracts import contract


class Cell(Button):

    # name - положение клетки!
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

    def killer(self):
        self.alive = False
        self.configure(bg='black')


@contract
# функция создающая все клетки на поле, они уже сразу объекты типа Клетка
def background(size):
    '''
    :type size: int, <=40, != 0
    :rtype: list
    '''
    cells = []
    for j in range(0, 500, size):
        for k in range(0, 400, size):
            our_cell = Cell(j, k, size, [int(j / size + 1), int(k / size + 1)])
            cells.append(our_cell)
    return cells


# @contract
def live_cells(cells):
    """
    :param cells: list, not null
    :type cells: list
    :rtype: list
    """
    living = []
    for cell in cells:
        if cell.alive:
            living.append([cell, cell.name])
    print(living)
    killing(living)

@contract
def killing(living):
    '''
    :type living: list
    '''
    while living:
        old_living = living
        for white_cell in living:
            neighbours = 0
            l_x = white_cell[1][0]
            l_y = white_cell[1][1]
            for neighbour in living:
                n_x = neighbour[1][0]
                n_y = neighbour[1][1]
                if (n_x - l_x) + (n_y - l_y) != 0:
                    if abs(n_x - l_x) < 2 and abs(n_y - l_y) < 2:
                        neighbours += 1
            if neighbours < 2 or neighbours > 3:
                white_cell[0].killer()
                living.remove(white_cell)
            if old_living == living:
                for white_cell in living:
                    white_cell[0].killer()
                living = []
                break


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
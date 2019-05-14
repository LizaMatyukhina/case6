from tkinter import *
from contracts import contract


class Cell(Button):

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

    def click_button(self):
        self.alive = True
        self.configure(bg='white')

    def killer(self):
        self.alive = False
        self.configure(bg='black')


@contract
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
    dying = []
    for cell in cells:
        if cell.alive:
            living.append([cell, cell.name])
        if cell.alive == False:
            dying.append([cell, cell.name])
    killing(living, dying)


@contract
def killing(living, dying):
    '''
    :type living: list
    :type dying: list
    '''
    old_living = []
    while living:
        old_living.append(living.copy())
        for neighbor in dying:
            n_x = neighbor[1][0]
            n_y = neighbor[1][1]
            neighbours = 0
            variants = [[n_x - 1, n_y + 1], [n_x, n_y + 1], [n_x + 1, n_y + 1], [n_x - 1, n_y], [n_x + 1, n_y],
                        [n_x - 1, n_y - 1], [n_x, n_y - 1], [n_x + 1, n_y - 1]]

            for white_cell in living:
                for variant in variants:
                    if white_cell[1] == variant:
                        neighbours += 1
            if neighbours == 3:
                print('Клетка ', neighbor[1], 'родилась')
                neighbor[0].click_button()
                dying.remove(neighbor)
                living.append(neighbor)

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
                dying.append(white_cell)
                if neighbours<2:
                    print('Клетка ',white_cell[1],' умерла от одиночества')
                if neighbours > 3:
                    print('Клетка ', white_cell[1], ' умерла от перенаселённости')

            if living in old_living:
                for white_cell in living:
                    white_cell[0].killer()
                living = []
                break

    else:
        print('Игра окончена')
        sys.exit(0)


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

# объявление функции
def draw_triangle():
    c = 1
    z = 7
    for i in range(8):
        print(' '* (z+i), end='')
        print('*'*c)
        c += 2
        z -= 2
# основная программа
draw_triangle()  # вызов функции
print('''       *
      ***
     *****
    *******
   *********
  ***********
 *************
***************''')
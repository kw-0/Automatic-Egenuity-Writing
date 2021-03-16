import pyautogui as pag
import numpy as np


# coord for different button placements for writing
enter = (1097, 799)
solution = (805, 594)
end_of_sol = (877, 602)
entry_box = (809, 651)


def copy():
    pag.mouseDown(button='right')
    pag.sleep(0.5)
    pag.moveRel(100, 35)
    pag.mouseUp()


def paste():
    pag.moveTo(entry_box, duration=0.25)
    pag.sleep(0.5)
    pag.click()
    pag.mouseDown(button='right')
    pag.moveRel(50, 150)
    pag.mouseUp()


for x in range(15):
    pag.sleep(4.75)  # 4.75 is optimal
    pag.moveTo(entry_box)
    pag.mouseDown(button='left')
    pag.moveRel(200, 100)
    pag.keyDown('delete')
    pag.keyUp('delete')
    pag.click(enter, duration=0.2)
    pag.moveTo(solution, duration=1)
    pag.mouseDown(button='left')
    pag.moveRel(10, 17)
    copy()
    paste()

    pag.click(enter, duration=0.25)




# posXY = pag.position()
# # feeds colors
# while not (posXY[0] == 0):
#     posXY = pag.position()
#     print(posXY, pag.pixel(posXY[0], posXY[1]))

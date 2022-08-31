import mouse
import time
import keyboard
from PIL import Image
import os
import easyocr
from pykeyboard import PyKeyboard



def Get_Price():
    reader = easyocr.Reader(["en"])
    result = reader.readtext('result.png', detail=0)
    return(result)


def Get_Full_Image(path):
    os.remove('result.png')
    img = Image.open(path) 
    left = 589
    top = 522
    right = 700
    bottom = 550
    img_res = img.crop((left, top, right, bottom))
    img_res.save('result.png')


def Get_pos ():
    while (True):

        if (keyboard.is_pressed('space')):
            print (mouse.get_position())
        if (keyboard.is_pressed('shift')):
            exit()
        time.sleep(1)

def Scroll (up_or_dn):
    if(up_or_dn == True):
        mouse.move(1672, 679)
        mouse.click(button='left')
    else:
        mouse.move(1673, 983)
        mouse.click(button='left')
        mouse.click(button='left')
        mouse.click(button='left')


def Update_pg ():
    mouse.move(86, 50)
    mouse.click(button='left')

def Sell_button ():
    mouse.move(875, 238)
    mouse.click(button='left')
    time.sleep(1)
    mouse.move(911, 456)
    mouse.click(button='left')
    time.sleep(1)
    mouse.move(827, 500)
    mouse.click(button='left')
    time.sleep(1)


def Print_Num(data):
    k = PyKeyboard()
    k.type_string(data)

def Save_Scr():
    k = PyKeyboard()
    k.tap_key(k.print_screen_key)
    mouse.move(101, 1031)
    mouse.click(button='left')
    k.press_key(k.control_key)
    time.sleep(0.1)
    k.tap_key('v')
    time.sleep(0.1)
    k.release_key(k.control_key)
    mouse.move(24, 33)
    mouse.click(button='left')
    time.sleep(1)
    mouse.move(98, 152)
    mouse.click(button='left')
    time.sleep(1)
    mouse.move(165, 1034)
    mouse.click(button='left')

def Cancel_Ordr():
    mouse.move(1296, 536)
    mouse.click(button='left')
    time.sleep(1)
    mouse.click(button='left')

def Sell (price):
    mouse.move(605, 540)
    mouse.click(button='left')
    mouse.click(button='left')
    time.sleep(1)
    k = PyKeyboard()
    k.type_string(price)
    time.sleep(1)
    mouse.move(743, 735)
    mouse.click(button='left')



plank = float(input('Enter plank:'))
time.sleep(5)
Scroll (False)
time.sleep(3)
Scroll (True)
Update_pg()
time.sleep(2)
Sell_button()
Save_Scr()
Get_Full_Image('test.png')
time.sleep(1)
price = Get_Price()[0]
price = price.replace(',', '.')
price = float(price)
price -= 0.0000001
price = str(price)[:9]
old_my_price = price
Sell(price)
time.sleep(15)
while (True):
    Scroll (True)
    Update_pg()
    time.sleep(2)
    Sell_button()
    Save_Scr()
    Get_Full_Image('test.png')
    time.sleep(1)
    price = Get_Price()[0]
    price = price.replace(',', '.')
    try:
        print('\n\n\n\n\n', price, "  ||  ", old_my_price)
        while (True):
            if (price != old_my_price):
                price = float(price)
                if (price < plank):
                    break
                else:
                    Scroll (False)
                    Cancel_Ordr()
                    time.sleep(20)
                    Scroll (False)
                    time.sleep(1)
                    Scroll (True)
                    time.sleep(1)
                    price = float(price)
                    price -= 0.0000001
                    price = str(price)[:9]
                    old_my_price = price
                    Sell_button()
                    Sell(price)
                    time.sleep(15)
                    break
            else:
                time.sleep(5)
                break
    except:
        print('somesing heppened')
        time.sleep(5)


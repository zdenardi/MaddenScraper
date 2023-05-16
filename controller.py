import subprocess
import os
import vgamepad as vg
import time
import msvcrt as m
import keyboard
import msvcrt
from pynput.keyboard import Key, Listener


def wait():
    m.getch()


Xbox = 'C:\\Program Files\\WindowsApps\\Microsoft.GamingApp_2304.1001.15.0_x64__8wekyb3d8bbwe.exe'
# subprocess.Popen('C:\\Windows\\System32\\calc.exe')
gamepad = vg.VX360Gamepad()


# time.sleep(10)
# os.startfile (r"C:\Xbox.lnk")


# 31 Fi
def make_all_zeros():
    i = 0
    while i < 10:
        hold_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT, 4)
        press_once(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        print(i)
        i += 1


def set_stat_to_fifty():
    hold_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT, 2.6)


# {1:11,2:34,3:69,4:99}
def set_stat_to():
    hold_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT, 4)


def clear_text():
    press_amount(3, vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    press_amount(2, vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    press_once(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    press_amount(2, vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
    press_amount(3, vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)


def type_madden():
    clear_text()
    first_name = "Zach"
    last_name = "DeNardi"
    current_pos = 2
    first_row_start = 0,
    first_row_end = 12,
    second_row_start = 13
    second_row_end = 25
    third_row_start = 26
    third_row_end = 37
    buffer_characters = 0

    for character in first_name.lower():
        current_row = 0
        move_row = 0
        print(character)

        def determine_row(position):
            # first row
            if position < 12:
                return 0
            # second row
            elif 12 < position < 25:
                return 1
            # third row
            else:
                return 2

        def move_to_character(move, current):
            # negative number is backwards (left), postive is forwards (right)
            move_number = move - current
            if move_number < 0:
                print("left")
                print(move_number)
                # move left
                press_amount(abs(move_number), vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
            elif move_number > 0:
                print("right")
                print(move_number)
                # move right
                press_amount(move_number, vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
            else:
                print("dont move a muscle")

        def determine_buffer_characters(row):
            if row == 1:
                return 13
            else:
                return 26

        keys = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '{', '}', 'BACK', 'a', 's', 'd', 'f', 'g', 'h', 'j',
                'k', 'l', ':', 'qts', '|', 'caps', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<', '>', '?', '~', 'clr']

        # get position number
        move_pos = keys.index(character)

        # determine rows for each current and move
        current_row = determine_row(current_pos)
        move_row = determine_row(move_pos)
        # in same row
        if current_row == move_row:
            move_to_character(move_pos, current_pos)
        # not in same row
        else:
            rows_to_move = abs(current_row - move_row)
            buffer_characters = determine_buffer_characters(rows_to_move)
            # move down
            if current_row < move_row:

                print("move down")
                print(rows_to_move)
                press_amount(rows_to_move, vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)

                # determine how many spaces
                move_amount = abs(current_pos - move_pos) - buffer_characters
                if move_amount > 0:
                    print("move right")
                    print(move_amount)
                    # move right
                    press_amount(move_amount, vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
                else:
                    print("move left")
                    print(move_amount)
                    # move left
                    if move_amount != 0:
                        press_amount(abs(move_amount), vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
            # move up
            else:
                print("move up")
                print(rows_to_move)
                press_amount(rows_to_move, vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
                # determine move
                move_amount = abs(current_pos - move_pos) - buffer_characters
                if move_amount < 0:
                    print("move right")
                    print(move_amount)
                    # move right
                    press_amount(abs(move_amount), vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
                else:
                    print("move left")
                    print(move_amount)
                    # move left
                    if move_amount != 0:
                        press_amount(move_amount, vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)

        current_pos = move_pos
        press_once(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)


def go_left():
    gamepad.left_joystick_float(x_value_float=-1, y_value_float=0)
    gamepad.update()


def go_right():
    gamepad.left_joystick_float(x_value_float=+1, y_value_float=0)
    gamepad.update()


def go_down():
    gamepad.left_joystick_float(x_value_float=0, y_value_float=-1)
    gamepad.update()


def go_up():
    gamepad.left_joystick_float(x_value_float=0, y_value_float=1)
    gamepad.update()


def stop_moving():
    gamepad.left_joystick_float(x_value_float=0, y_value_float=0)
    gamepad.update()
    print("Stop moving")


def hold_button(btn, sec):
    gamepad.press_button(btn)
    gamepad.update()
    time.sleep(sec)
    gamepad.release_button(btn)
    gamepad.update()
    time.sleep(0.1)


def press_once(btn):
    gamepad.press_button(button=btn)
    gamepad.update()
    time.sleep(0.1)
    gamepad.release_button(button=btn)
    gamepad.update()
    time.sleep(0.2)


def press_and_release_controller_button(btn):
    gamepad.press_button(button=btn)
    gamepad.update()
    time.sleep(1)
    gamepad.release_button(button=btn)
    gamepad.update()


def press_amount(amount, btn):
    i = 0
    while i < amount:
        press_once(btn)
        i += 1


def on_press(key):
    print(key)
    try:
        if key.char == 'w':
            go_left()
            return True
        # Movement
    except:
        if key == Key.left:
            print(key)
            go_left()
            return True
        if key == Key.right:
            go_right()
            return True
        if key == Key.up:
            go_up()
            return True
        if key == Key.down:
            go_down()
            return True


def on_release(key):
    # Buttons
    if key == Key.esc:
        # Stop listener
        return False
    if key == Key.enter:
        press_and_release_controller_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        return True
    if key == Key.f12:
        press_and_release_controller_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        return True
    if key == Key.backspace:
        press_and_release_controller_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        return True
    if key == Key.ctrl_r:
        press_and_release_controller_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
    if key == Key.alt_l:
        press_and_release_controller_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        return True
    if key == Key.shift_r:
        press_and_release_controller_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        return
    if key == Key.shift_r:
        press_and_release_controller_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        return True
    # Movement
    if key == Key.left:
        print(key)
        stop_moving()
        return True
    if key == Key.right:
        stop_moving()
        return True
    if key == Key.up:
        stop_moving()
        return True
    if key == Key.down:
        stop_moving()
        return True
    if key == Key.f1:
        make_all_zeros()
        return True
    if key == Key.f2:
        set_stat_to()
        return True
    if key == Key.f3:
        type_madden()
        return True
    # Utils


# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

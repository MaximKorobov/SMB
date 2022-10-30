# Copyright (C) 2022 Maxim Korobov maxim.korobov@gmail.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pystray
from pystray import MenuItem, Menu
from PIL import Image, ImageDraw
import ctypes


# Icon stuff
def create_image_left(width, height, color1, color2):
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle((0, 0, width // 3, height), fill=color2)

    return image


def create_image_right(width, height, color1, color2):
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle((width * 2 // 3, 0, width, height), fill=color2)

    return image


def get_icon(state_left):
    if state_left:
        return create_image_left(64, 64, 'gray', 'white')
    else:
        return create_image_right(64, 64, 'gray', 'white')


# Context menu items
def action_quit():
    icon.stop()
    exit()


def action_swap():
    print("Swap")
    global stateLeft, icon

    stateLeft = not stateLeft
    icon.icon = get_icon(stateLeft)
    set_system_state(stateLeft)


menu = (
    MenuItem('Swap', action_swap, default=True, visible=True),
    Menu.SEPARATOR,
    MenuItem('Quit', action_quit)
)


# Windows OS related API calls
def get_system_state():
    get_state = 23  # 0x0017 for SM_SWAPBUTTON
    is_left_from_win = ctypes.windll.user32.GetSystemMetrics(get_state)
    return is_left_from_win


def set_system_state(state_left):
    swap_mouse_button = ctypes.windll.user32.SwapMouseButton(not state_left)
    return swap_mouse_button


# Main
if __name__ == '__main__':
    stateLeft = get_system_state() == 0

    icon = pystray.Icon('SMB', get_icon(stateLeft), "Swap mouse buttons", menu)
    icon.run()

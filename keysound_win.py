import win32api
import win32con
import time
import requests
import json
import asyncio


URL = 'http://127.0.0.1:5000/'

sound_map = {
    'num1': '',
    'num2': '',
    'num3': '',
    'num4': '',
    'num5': '',
    'num6': '',
    'num7': 'iwo',
    'num8': 'airhorn',
    'num9': 'horn'
}

async def play_sound(sound: str):
    # NumPad 9 key is pressed
    print("NumPad 9 is pressed!")
    sound = sound_map.get(sound)
    data = {
        "guild_id": 372795842223931392,
        "user_id": 320592587872534530,
        "sound": sound
    }

    print(f'Sending request to play sound {sound}...')
    try:
        response = await asyncio.to_thread(requests.post, URL, data=json.dumps(data))
        response.raise_for_status()
    except:
        print('Sending request to bot failed')
        response = None

    if response:
        if response.status_code == 200:
            print('Playing sound ' + sound)
        if response.status_code != 200:
            print(f'Request failed with code: {response.status_code}, {response.data}')
        

print('Started to listen num keys...')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_NUMPAD9):
        asyncio.run(play_sound('num9'))
    if win32api.GetAsyncKeyState(win32con.VK_NUMPAD8):
        asyncio.run(play_sound('num8'))
    if win32api.GetAsyncKeyState(win32con.VK_NUMPAD7):
        asyncio.run(play_sound('num7'))
    if win32api.GetAsyncKeyState(win32con.VK_NUMPAD6):
        asyncio.run(play_sound('num6'))
    if win32api.GetAsyncKeyState(win32con.VK_NUMPAD5):
        asyncio.run(play_sound('num5'))
    if win32api.GetAsyncKeyState(win32con.VK_NUMPAD4):
        asyncio.run(play_sound('num4'))
    if win32api.GetAsyncKeyState(win32con.VK_NUMPAD3):
        asyncio.run(play_sound('num3'))
    if win32api.GetAsyncKeyState(win32con.VK_NUMPAD2):
        asyncio.run(play_sound('num2'))
    if win32api.GetAsyncKeyState(win32con.VK_NUMPAD1):
        asyncio.run(play_sound('num1'))
    
    time.sleep(0.15)

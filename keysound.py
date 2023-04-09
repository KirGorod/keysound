import keyboard
import requests
import json


URL = 'http://127.0.0.1:5000/'

sound_map = {
    79: '', # Num 1
    80: '', # Num 2
    81: '', # Num 3
    75: '', # Num 4
    76: '', # Num 5
    77: '', # Num 6
    71: 'iwo', # Num 7
    72: 'airhorn', # Num 8
    73: 'horn', # Num 9
    
}


def on_press(event):
    try:
        if event.event_type == 'down' and event.scan_code in sound_map.keys():
            sound = sound_map.get(event.scan_code)
            data = {
                "guild_id": 372795842223931392,
                "user_id": 320592587872534530,
                "sound": sound
            }
            response = requests.post(URL, data=json.dumps(data))
            if response.status_code == 200:
                print('Playing sound ' + sound)
    except Exception as e:
        print(e)
        

keyboard.on_press(on_press)

# keep the script running
while True:
    pass

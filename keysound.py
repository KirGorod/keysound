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
    print(event.scan_code)
    try:
        if event.event_type == 'down' and event.scan_code in sound_map.keys():
            sound = sound_map.get(event.scan_code)
            data = {
                "guild_id": 372795842223931392,
                "user_id": 320592587872534530,
                "sound": sound
            }
            response = requests.post(URL, data=json.dumps(data))
            print(f'Send request to play sound {sound}...')
            if response.status_code == 200:
                print('Playing sound ' + sound)
    except:
        print("Some error occured while sending request")
        

keyboard.on_press(on_press)

# keep the script running
while True:
    pass

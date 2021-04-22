import os
import subprocess
import time

device_id = 'Your Android Device ID'
pin = 'Pin to Unlock Your Phone'

# wait for DUO notification
while True:
    out = subprocess.check_output('adb -s {} shell dumpsys notification'.format(device_id))
    if b'pkg=com.duosecurity.duomobile' in out:
        if b'tickerText=Login re...' in out:
            break
    time.sleep(0.2)

# unlock screen
os.system('adb -s {} shell input keyevent 224'.format(device_id))
os.system('adb -s {} shell input swipe 300 1000 300 500'.format(device_id))
os.system('adb -s {} shell input text {}'.format(device_id, pin))

# clear notification 
os.system('adb -s {} shell input swipe 510 200 510 100'.format(device_id))
# NOTE: if rooted, can be replaced by 'adb shell service call notification 1'

# open DUO and accept the notification
os.system('adb -s {} shell am start com.duosecurity.duomobile/com.duosecurity.duomobile.account_list.AccountListActivity'.format(device_id))
time.sleep(0.1)
os.system('adb -s {} shell input tap 510 300'.format(device_id))
time.sleep(0.1)
os.system('adb -s {} shell input tap 200 1600'.format(device_id))

# return to home and lock
os.system('adb -s {} shell input keyevent KEYCODE_BACK'.format(device_id))
os.system('adb -s {} shell input keyevent 26'.format(device_id))
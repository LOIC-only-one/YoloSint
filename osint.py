import requests
import json
from requests import HTTPError
from requests.models import Response
import random


banner1 = '''

 ▄· ▄▌      ▄▄▌        .▄▄ · ▪   ▐ ▄ ▄▄▄▄▄
▐█▪██▌▪     ██•  ▪     ▐█ ▀. ██ •█▌▐█•██  
▐█▌▐█▪ ▄█▀▄ ██▪   ▄█▀▄ ▄▀▀▀█▄▐█·▐█▐▐▌ ▐█.▪
 ▐█▀·.▐█▌.▐▌▐█▌▐▌▐█▌.▐▌▐█▄▪▐█▐█▌██▐█▌ ▐█▌·
  ▀ •  ▀█▄▀▪.▀▀▀  ▀█▄▀▪ ▀▀▀▀ ▀▀▀▀▀ █▪ ▀▀▀ 
(YoloSint Letux - Simple Osint Tool)
'''
banner2 = '''

                                                                              
8b        d8           88                ad88888ba   88                       
 Y8,    ,8P            88               d8"     "8b  ""                ,d     
  Y8,  ,8P             88               Y8,                            88     
   "8aa8"  ,adPPYba,   88   ,adPPYba,   `Y8aaaaa,    88  8b,dPPYba,  MM88MMM  
    `88'  a8"     "8a  88  a8"     "8a    `"""""8b,  88  88P'   `"8a   88     
     88   8b       d8  88  8b       d8          `8b  88  88       88   88     
     88   "8a,   ,a8"  88  "8a,   ,a8"  Y8a     a8P  88  88       88   88,    
     88    `"YbbdP"'   88   `"YbbdP"'    "Y88888P"   88  88       88   "Y888  
                                                                              
(YoloSint Letux - Simple Osint Tool)                                                                              
'''
banner3 = '''                                                        
\\    / /                      //   ) )                     
 \\  / /  ___     //  ___     ((        ( )   __    __  ___ 
  \\/ / //   ) ) // //   ) )    \\     / / //   ) )  / /    
   / / //   / / // //   / /       ) ) / / //   / /  / /     
  / / ((___/ / // ((___/ / ((___ / / / / //   / /  / /      
(YoloSint Letux - Simple Osint Tool)
'''
banner_finally = random.choice(banner1,banner2,banner3)
print(banner_finally) and '\n'
username = input('Enter unsername: ')
url = {
    "twitter": "https://twitter.com/"+username,
    "instagram": "https://instagram.com/"+username,
    "facebook": "https://facebook.com/"+username,
    "github": "https://github.com/"+username,
    "reddit": "https://www.reddit.com/user/"+username,
    "tiktok": "https://www.tiktok.com/@"+username,
    "pinterest": "https://www.pinterest.com/"+username,
    "linkedin": "https://www.linkedin.com/in/"+username,
}
    

for cle, valeur in url.items():
    

    try:
        print('----------------------------------')
        data = requests.get(valeur) and print(cle)
        
        # If the response was successful, no Exception will be raised
        data.raise_for_status()
        if data.status_code == 200:
            print('Compte trouvé avec succès !')
            print(valeur)
            print('----------------------------------')
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        print('----------------------------------')
    except Exception as err:
        print('Compte invalide')  
        print('----------------------------------')
    except KeyboardInterrupt as key:
        print('Vous avez interompu le programme avec CTRL + C')
        print('----------------------------------')

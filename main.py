
import json
import os
from pytube import YouTube
import requests
from bs4 import BeautifulSoup
import re , time
from colorama import Back , Fore , Style

mainlogo = """

   __ __                             ____             _           
  / // /__  __ _____  ___ ____ _____/ __/__ _____  __(_)______ ___
 / _  / _ \/ // / _ \/ _ `/ _ `/ __/\ \/ -_) __/ |/ / / __/ -_|_-<
/_//_/\___/\_,_/_//_/\_,_/\_,_/_/ /___/\__/_/  |___/_/\__/\__/___/



		Created By : Hounaar
		website = https://hounaar.com
		AI Model = https://eai.hounaar.com
		Github = https://github.com/hounaar

"""

print(Fore.YELLOW + mainlogo)
print("Choose from the following commands:")
print("1> Youtube Video Downloader")
print("2> Crypto Momental Price")
print("3> Exit")
main_input = input("Enter one option:")




def youtub():
      logo = """

#     #                                          
 #   #   ####  #    # ##### #    # #####  ###### 
  # #   #    # #    #   #   #    # #    # #      
   #    #    # #    #   #   #    # #####  #####  
   #    #    # #    #   #   #    # #    # #      
   #    #    # #    #   #   #    # #    # #      
   #     ####   ####    #    ####  #####  ###### 



######                                                                 
#     #  ####  #    # #    # #       ####    ##   #####  ###### #####  
#     # #    # #    # ##   # #      #    #  #  #  #    # #      #    # 
#     # #    # #    # # #  # #      #    # #    # #    # #####  #    # 
#     # #    # # ## # #  # # #      #    # ###### #    # #      #####  
#     # #    # ##  ## #   ## #      #    # #    # #    # #      #   #  
######   ####  #    # #    # ######  ####  #    # #####  ###### #    # 




      """

      print(Fore.GREEN +logo)



      real = input("Enter video url:")

      print("Checking video url validation...")
      video = YouTube(real)
      print("URL set: Checked")

      print("Checking Resolutions...")
      stream = video.streams.get_highest_resolution()
      print("Highest resolution: Checked")

      print("Downloading the file...")
      downloader = stream.download()
      print("<================================>")

      print("DONE !!")


def crypt():
      
      logo ="""
      .o88b. d8888b. db    db d8888b. d888888b  .d88b.  
      d8P  Y8 88  `8D `8b  d8' 88  `8D `~~88~~' .8P  Y8. 
      8P      88oobY'  `8bd8'  88oodD'    88    88    88 
      8b      88`8b      88    88~~~      88    88    88 
      Y8b  d8 88 `88.    88    88         88    `8b  d8' 
      `Y88P' 88   YD    YP    88         YP     `Y88P' 

      d8888b. d8888b. d888888b  .o88b. d88888b 
      88  `8D 88  `8D   `88'   d8P  Y8 88'     
      88oodD' 88oobY'    88    8P      88ooooo 
      88~~~   88`8b      88    8b      88~~~~~ 
      88      88 `88.   .88.   Y8b  d8 88.     
      88      88   YD Y888888P  `Y88P' Y88888P 
                                             


      """

      print(Fore.GREEN +logo)  
      crypto = input("Enter your cryptocurrency in ALL CAPITAL Letters:")
      key = "https://api.binance.com/api/v3/ticker/price?symbol="+crypto
      while True:
         data = requests.get(key)  
         data = data.json()
         print(f"{data['symbol']} price is {data['price']}")



def main(choice):
	if choice == '1':
		youtub()
	elif choice == '2':
		crypt()

	elif choice == '3':
		os.system('exit')
	else:
		print("No choice Selected")
		os.system('exit')
		
main(main_input)
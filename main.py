#github.com/Kenokey

#Discordlink
#https://discord.gg/DnwnCrvZv8
#DONT CHANGE ANY CODE


from selenium import webdriver
from colorama import Fore
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import os
import time


class Main:
    def __init__(self):
        self.driver = None
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.xpaths = [
            "/html/body/div[6]/div/div[2]/div/div/div[2]/div/button", #followers
            "/html/body/div[6]/div/div[2]/div/div/div[3]/div/button", #hearts
            "/html/body/div[6]/div/div[2]/div/div/div[4]/div/button", #comment_hearts
            "/html/body/div[6]/div/div[2]/div/div/div[6]/div/button", #views
            "/html/body/div[6]/div/div[2]/div/div/div[7]/div/button", #shares
            "/html/body/div[6]/div/div[2]/div/div/div[8]/div/button", #favorites
            "/html/body/div[6]/div/div[2]/div/div/div[9]/div/button"  #livestream
        ]
        self.enter_video_url = [
            "/html/body/div[7]/div/form/div/input", #followers
            "/html/body/div[8]/div/form/div/input", #hearts
            "/html/body/div[9]/div/form/div/input", #comment_hearts
            "/html/body/div[10]/div/form/div/input", #views
            "/html/body/div[11]/div/form/div/input", #shares
            "/html/body/div[12]/div/form/div/input", #favorites
            "/html/body/div[13]/div/form/div/input"  #livestream
        ]
        self.timer_text = [
            "/html/body/div[7]/div/div/span[1]", #followers
            "/html/body/div[8]/div/div/span[1]", #hearts
            "/html/body/div[9]/div/div/span[1]", #comment_hearts
            "/html/body/div[10]/div/div/span[1]", #views
            "/html/body/div[11]/div/div/span[1]", #shares
            "/html/body/div[12]/div/div/span[1]", #favorites
            "/html/body/div[13]/div/div/span[1]"  #livestream
        ]
        self.search_button = [
            "/html/body/div[7]/div/form/div/div/button", #followers
            "/html/body/div[8]/div/form/div/div/button", #hearts
            "/html/body/div[9]/div/form/div/div/button", #comment_hearts
            "/html/body/div[10]/div/form/div/div/button", #views
            "/html/body/div[11]/div/form/div/div/button", #shares
            "/html/body/div[12]/div/form/div/div/button", #favorites
            "/html/body/div[13]/div/form/div/div/button"  #livestream
        ]
        self.send_button = [
            "/html/body/div[7]/div/div/div[1]/div/form/button", #followers
            "/html/body/div[8]/div/div/div[1]/div/form/button", #hearts
            "/html/body/div[9]/div/div/div[1]/div/form/button", #comment_hearts
            "/html/body/div[10]/div/div/div[1]/div/form/button", #views
            "/html/body/div[11]/div/div/div[1]/div/form/button", #shares
            "/html/body/div[12]/div/div/div[1]/div/form/button", #favorites
            "/html/body/div[13]/div/div/div[1]/div/form/button"  #livestream
        ]
        self.xpathnames = [
            "Followers", #followers
            "Hearts", #hearts
            "Comment Hearts", #comment_hearts
            "Views", #views
            "Shares", #shares
            "Favorites", #favorites
            "Livestream"  #livestream
        ]
        self.discord = "https://discord.gg/DnwnCrvZv8"
        self.option = 0


    def clear_console(self):
        os.system("cls")



    def wait_for_page_to_load(self):
        self.check_if_website_loaded('ua-check', "[+] Page is Ready!", "[-] 001 Error - Cant connect to web service", 10)

    def wait_for_captcha_solve(self):
        print("[~] Waiting For CAPTCHA to solve")
        self.check_if_website_loaded('row', "[+] CAPTCHA solved successfully!\n", "[-] 002 Error - CAPTCHA took too long OR no webservice detected", 100)



    def check_if_button_is_enabled(self, button): 
        if button.is_enabled():
            return True
        else:
            return False



    def check_button_status(self, xpath):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            if element.is_enabled():
                return f"{Fore.GREEN}[ONLINE]{Fore.RESET}"
            else:
                return f"{Fore.RED}[OFFLINE]{Fore.RESET}"
        except TimeoutException:
            print("[-] 003 Error - Fatal error while generating list")
            quit()



    def display_button_list(self):
        text = "[~] Decide which bot you want [1 to 8]\n"
        for i in range(7):
            text = text + "[" + str(i+1) + "] " + self.xpathnames[i] + " " + self.check_button_status(self.xpaths[i]) + "\n" 
            i+=i
        text = text + f"[8] Discord {Fore.GREEN}[ONLINE]{Fore.RESET}"
        print(text)



    def click_button(self, number_option):
        try:
            xpath = self.xpaths[number_option - 1]
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            if element.is_enabled():
                element.click()
            else:
                print("[-] 004 Error - Offline OR Number not found")
                quit()
        except TimeoutException:
            print("[-] 005 Error - Offline OR Number not found OR Network error")
            quit()



    def user_input_option(self):
        self.option = int(input())
        if self.option == 8:
            self.driver.get(self.discord)
        else:
            self.click_button(self.option)

 

    def check_if_website_loaded(self, path, message, error_message, delay):
        try:
            myElem = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME,path)))
            print(message) 
        except TimeoutException:
            print(error_message)
            quit()



    def get_insert_tiktok_link(self):
        print("[~] Send the Tiktok Link")
        tiktok_link = input()
        myElem = None
        try:
            myElem = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, self.enter_video_url[self.option-1])))
            print("\n[+] Loading input Field")
        except TimeoutException:
            print("[-] 006 Error - Cant Find Input Field")
            quit()
        myElem = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, self.enter_video_url[self.option-1])))
        myElem.send_keys(str(tiktok_link))

        time.sleep(2)



    def send(self):
        text_box = None
        search_button = None
        send_button = None
        
        #Search Button init
        try:
            search_button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.search_button[self.option-1])))
            print("[+] Loading Search Field") 
            time.sleep(1)
            search_button.click()
        except TimeoutException:
            print("[-] 009 Error - Search not Found OR disabled")
            quit()

        time.sleep(3)


        #Send Button init
        try:
            send_button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.send_button[self.option-1])))
            time.sleep(1)
            send_button.click()
            print("[+] Loading Button Field")
            print("[+] Loaded Everything successfully!")
            print(f"\n{Fore.WHITE}[BOT IS RUNNING NOW]{Fore.RESET}")
            self.successfully_message()
            self.generate_and_send(text_box, search_button, send_button)
        except TimeoutException:
            print("[+] Loading Text Field")
            

        time.sleep(1)

        #Trying to get textbox
        try:
            text_box = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.timer_text[self.option-1])))
            print("[+] Loaded Everything successfully!")
            print(f"\n{Fore.WHITE}[BOT IS RUNNING NOW]{Fore.RESET}")
            self.generate_and_send(text_box, search_button, send_button)
        except TimeoutException:
            print("[-] 008 Error - Send Key not Found")
            quit()

       


    def generate_and_send(self, text_box, search_button, send_button):
        delay = 900
        
        #Send Message
        try:
            while True:
                text_box = WebDriverWait(self.driver, delay).until(EC.text_to_be_present_in_element((By.XPATH, self.timer_text[self.option-1]), "Next Submit: READY....!"))
                time.sleep(3)
                search_button.click()
                send_button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.send_button[self.option-1])))
                time.sleep(5)
                send_button.click()
                self.successfully_message()
                text_box = None
        except TimeoutException:
            print("[-] 007 Error - Cant send "+(self.xpathnames[self.option+1])+" because of Connection Error or Closed Service")
            quit()




    def successfully_message(self):
        print(f"{Fore.MAGENTA}[#]{Fore.WHITE} Send "+(self.xpathnames[self.option-1])+" successfully!")




    def main(self):
        self.clear_console()

        print(Fore.GREEN + """
         
    ███      ▄█     ▄█   ▄█▄ ▀█████████▄   ▄██████▄      ███     
▀█████████▄ ███    ███ ▄███▀   ███    ███ ███    ███ ▀█████████▄ 
   ▀███▀▀██ ███▌   ███▐██▀     ███    ███ ███    ███    ▀███▀▀██ 
    ███   ▀ ███▌  ▄█████▀     ▄███▄▄▄██▀  ███    ███     ███   ▀ 
    ███     ███▌ ▀▀█████▄    ▀▀███▀▀▀██▄  ███    ███     ███     
    ███     ███    ███▐██▄     ███    ██▄ ███    ███     ███     
    ███     ███    ███ ▀███▄   ███    ███ ███    ███     ███     
   ▄████▀   █▀     ███   ▀█▀ ▄█████████▀   ▀██████▀     ▄████▀   
                   ▀ by @Kenokey
        """ + Fore.RESET)

        self.driver.get("https://zefoy.com/")

        print("[~] Bot Loading, please wait!")
        self.wait_for_page_to_load()
        time.sleep(2)
        self.wait_for_captcha_solve()

        self.display_button_list()
        self.user_input_option()

        time.sleep(1)
        self.check_if_website_loaded('row', "[+] Started successfully!", "[-] 006 Error - Site cant Connect AND Load", 5)

        self.get_insert_tiktok_link()
        self.send()

        # Weitere Schritte und Methoden hier einfügen

        self.driver.quit()



if __name__ == "__main__":
    main = Main()
    main.main()

import requests, json, sys, os
from colorama import Fore

with open("config.json") as configFile:
    jsonObject = json.load(configFile)
    configFile.close()

token = jsonObject['token']
prefix = jsonObject['prefix']
channelId = jsonObject['channelId']
userId = jsonObject['userId']
url =  f"https://discord.com/api/v9/channels/{channelId}/messages"
argument = sys.argv[1]
green = Fore.GREEN
reset = Fore.RESET

if os.name == "nt":
    os.system("cls")
    print(f"""
{green}    

 ________                                                                         ______    __                          __                     
/        |                                                                       /      \  /  |                        /  |                    
$$$$$$$$/   _______   ______   _______    ______   _____  ____   __    __       /$$$$$$  |_$$ |_     ______    ______  $$ |  ______    ______  
$$ |__     /       | /      \ /       \  /      \ /     \/    \ /  |  /  |      $$ \__$$// $$   |   /      \  /      \ $$ | /      \  /      \ 
$$    |   /$$$$$$$/ /$$$$$$  |$$$$$$$  |/$$$$$$  |$$$$$$ $$$$  |$$ |  $$ |      $$      \$$$$$$/   /$$$$$$  | $$$$$$  |$$ |/$$$$$$  |/$$$$$$  |
$$$$$/    $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |       $$$$$$  | $$ | __ $$    $$ | /    $$ |$$ |$$    $$ |$$ |  $$/ 
$$ |_____ $$ \_____ $$ \__$$ |$$ |  $$ |$$ \__$$ |$$ | $$ | $$ |$$ \__$$ |      /  \__$$ | $$ |/  |$$$$$$$$/ /$$$$$$$ |$$ |$$$$$$$$/ $$ |      
$$       |$$       |$$    $$/ $$ |  $$ |$$    $$/ $$ | $$ | $$ |$$    $$ |      $$    $$/  $$  $$/ $$       |$$    $$ |$$ |$$       |$$ |      
$$$$$$$$/  $$$$$$$/  $$$$$$/  $$/   $$/  $$$$$$/  $$/  $$/  $$/  $$$$$$$ |       $$$$$$/    $$$$/   $$$$$$$/  $$$$$$$/ $$/  $$$$$$$/ $$/       
                                                                /  \__$$ |                                                                     
                                                                $$    $$/                                                                      
                                                                 $$$$$$/                                                                       
                                
{reset}
    """)
else:
    os.system("clear")
    print(f"""
{green}    

 ________                                                                         ______    __                          __                     
/        |                                                                       /      \  /  |                        /  |                    
$$$$$$$$/   _______   ______   _______    ______   _____  ____   __    __       /$$$$$$  |_$$ |_     ______    ______  $$ |  ______    ______  
$$ |__     /       | /      \ /       \  /      \ /     \/    \ /  |  /  |      $$ \__$$// $$   |   /      \  /      \ $$ | /      \  /      \ 
$$    |   /$$$$$$$/ /$$$$$$  |$$$$$$$  |/$$$$$$  |$$$$$$ $$$$  |$$ |  $$ |      $$      \$$$$$$/   /$$$$$$  | $$$$$$  |$$ |/$$$$$$  |/$$$$$$  |
$$$$$/    $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |       $$$$$$  | $$ | __ $$    $$ | /    $$ |$$ |$$    $$ |$$ |  $$/ 
$$ |_____ $$ \_____ $$ \__$$ |$$ |  $$ |$$ \__$$ |$$ | $$ | $$ |$$ \__$$ |      /  \__$$ | $$ |/  |$$$$$$$$/ /$$$$$$$ |$$ |$$$$$$$$/ $$ |      
$$       |$$       |$$    $$/ $$ |  $$ |$$    $$/ $$ | $$ | $$ |$$    $$ |      $$    $$/  $$  $$/ $$       |$$    $$ |$$ |$$       |$$ |      
$$$$$$$$/  $$$$$$$/  $$$$$$/  $$/   $$/  $$$$$$/  $$/  $$/  $$/  $$$$$$$ |       $$$$$$/    $$$$/   $$$$$$$/  $$$$$$$/ $$/  $$$$$$$/ $$/       
                                                                /  \__$$ |                                                                     
                                                                $$    $$/                                                                      
                                                                 $$$$$$/                                                                       
                                
{reset}
    """)

if argument == "usage":
    print(f"{green}Usage: python app.py <method>")
    exit()
elif argument == "methods":
    print(f"""{green}List of methods you can use:
    
    1. collect
    2. givemoney
    3. withall
    4. depall
    {reset}""")
    exit()
elif argument == "collect":
    collectData = {
        "content": f"{prefix}collect" 
    }
    collectRequest = requests.post(url=url, headers={"authorization":f"{token}", "content-type": "application/json"}, json=collectData)
    print(f"{green}Have a nice day :){reset}")
    exit()
elif argument == "givemoney":
    giveMoneyData = {
        "content": f"{prefix}give <@{userId}> all" 
    }
    giveMoneyRequest = requests.post(url=url, headers={"authorization":f"{token}", "content-type": "application/json"}, json=giveMoneyData)
    print(f"{green}Have a nice day :){reset}")
    exit()
elif argument == "withall":
    withallData = {
        "content": f"{prefix}with all" 
    }
    withallRequest = requests.post(url=url, headers={"authorization":f"{token}", "content-type": "application/json"}, json=withallData)
    print(f"{green}Have a nice day :){reset}")
    exit()
elif argument == "depall":
    depallData = {
        "content": f"{prefix}dep all" 
    }
    depallRequest = requests.post(url=url, headers={"authorization":f"{token}", "content-type": "application/json"}, json=depallData)
    print(f"{green}Have a nice day :){reset}")
    exit()

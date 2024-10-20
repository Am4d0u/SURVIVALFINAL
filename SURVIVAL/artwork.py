﻿import time

def print_slow(text,speed):
    #Prints text one character at a time."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)

def survival():
    print_slow(R"""

  ██████  █    ██  ██▀███   ██▒   █▓ ██▓ ██▒   █▓ ▄▄▄       ██▓    
▒██    ▒  ██  ▓██▒▓██ ▒ ██▒▓██░   █▒▓██▒▓██░   █▒▒████▄    ▓██▒    
░ ▓██▄   ▓██  ▒██░▓██ ░▄█ ▒ ▓██  █▒░▒██▒ ▓██  █▒░▒██  ▀█▄  ▒██░    
  ▒   ██▒▓▓█  ░██░▒██▀▀█▄    ▒██ █░░░██░  ▒██ █░░░██▄▄▄▄██ ▒██░    
▒██████▒▒▒▒█████▓ ░██▓ ▒██▒   ▒▀█░  ░██░   ▒▀█░   ▓█   ▓██▒░██████▒
▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░   ░ ▐░  ░▓     ░ ▐░   ▒▒   ▓▒█░░ ▒░▓  ░
░ ░▒  ░ ░░░▒░ ░ ░   ░▒ ░ ▒░   ░ ░░   ▒ ░   ░ ░░    ▒   ▒▒ ░░ ░ ▒  ░
░  ░  ░   ░░░ ░ ░   ░░   ░      ░░   ▒ ░     ░░    ░   ▒     ░ ░   
      ░     ░        ░           ░   ░        ░        ░  ░    ░  ░
                                ░            ░                     
""",0.0005)

def gameover():
    print_slow(R"""
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                   
""",0.0005)




def pitbull():
    print_slow(R"""
                                                                    
                                                                       
                ████▓▓██                       ██▓▓████                
             ███▓▓▒▒▒▒░▒█                     █▒▒▒▒▒▒▓▓███             
         ████▒▒▓▒▓███▓▒▒▓█                   █▓▒▒▓███▓▒▓▒▒████         
       █▓░▒▒▒▓▓███████▓▓▓▒████████   ████████▒▓▓▓███████▒▓▒▒▒░▓█       
      ██▒▒▒▓▓█▓▓▓█▓███▓█▓▓▓▓▒▒▓▒▒▓███▓▒▒▓▒▒▓▓▓▓█▓███▓█▓▓██▓▓▒▒▒██      
     ██▒▒▒▓███▓▓▓▓▓█████▓▒▒▓██▓█▓▒█▓█▒▓█▓██▓▒▒▓█████▓▓▓▓▓███▓▒▒▒██     
    ██▒▒▓██▒▓▓██▓▓█████▓▒▓█▓▒▓█▒▓██▓██▓▒█▓▒▓▓▓▒▓█████▓▓██▓▓▒██▓▒▒██    
    █▓▒███████▓██████▓▓▓▓▒▒▒▓▓▓▓▓█▓▓▓█▓▓▓▓▓▒▒▒▓▓▓▓██████▓███████▒▓█    
    ███  ██▓▓▒▒▓███▓▓▒▒▒▒▒▒▒▓▒▒▓▓▒▒█▒▒▓▓▒▒▓▒▒▒▒▒▒▒▓▓███▓▒▒▓▓██  ███    
         ███▓▒███▓▓▒▒▒▒▒▒▓█▒▒▓▒▒▒▓▓▒▓▓▒▒▒▓▒▒▓▓▒▒▒▒▒▒▓▓███▒▓▓██         
          ██████▓▓▒▒▒▒▒▓▓▒▒▒▒▓▒▒▓▓▓█▓▓▓▒▒▓▒▒▒▒▓▓▒▒▒▒▒▓▓██████          
           ████▓▓▒▒▒▒▓▓██▓▓▓▒▒▓▓▓█████▓▓▓▒▒▓▓▓█▓▓▓▒▒▒▒▓▓████           
            ██▓▓▓▒▒▒▒▒▒▒▒▒▓█▓█▓▓▓▓███▓▓▓▓█▓█▓▒▒▒▒▒▒▒▒▒▓▓▓██            
            █▓▓▓▓▒▒▓▓▓▓▓▓▓▒▒▓▓▓█▓▓▓█▓▓▓█▓▓▓▒▒▓▓▓▓▓▓▓▒▒▓▓▓▓█            
            █▓▓▓▓▓▓▓▓▓▓▓▒▓█▓▓▒▒▓██▓██▓█▓▒▒▓▓█▓▒▓▓▓▓▓▓▓▓▓▓▓█            
            ██▒▓▓▓▓▓█████▓▓██▓▓▓███▓███▓▓▓██▓▓█████▓▓▓▓▓▒██            
            ██▒▓▓▒▒▓██▓▓▓▓████████▓▒▓████████▓▓▓▓██▓▒▒▓▓▒██            
            ██▒▓▓▓▒▒▒▓██████████▓▒▒▒▒▒▓██████████▓▒▒▒▓▓▓▒▒██           
           ██▓▒▒▓██▓▒▒▓▓▓███▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓███▓▓▓▒▒▓██▓▒▓▒▓█           
           ██▓▓▒▓█████▓▓███▓▓▒▒▒▒░░░░░▒▒▒▒▓▓███▓▓█████▓▒▓▒▓█           
           ██▓▓▓▒▓████▓▓██▓▓▓▓▓▓▒▒░░░▒▓▓▓▓▓▓▓██▓▓████▓▒▓▓▓▓█           
           ██▓█▓▒▓▓██▓▓██▓▓▓▓▓▓▓▓█████▓▓▓▓▓▓▓▓██▓▓██▓▓▓▓█▓▓█           
           ██████▓▓██▓███▓▒▒▒█▓▓▓▒▒▓▒▒▓▓██▒▒▒▓▓██▓██▓▓███▓██           
            ███████▓██▓█▓▒░▓▓▓█▓▓▓▓█▓▓▓▓█▓▓▓░▒▓█▓██▓████▓▓█            
             ██████▓███▓▒░░▓██████▓▓▓██████▓░░▒▓███▓██████             
              █████▓▓█▓▒░░░▒▓██▓▓▓███▓▓▓██▓▒░░░▒▓█▓▓█████              
                ██████▒░░░░░▒▓▓█████████▓▓▒░░░░░▒██████                
                  ████░░░░░░▓▓▓▓███████▓▓▓▓░░░░░░████                  
                   ██▓▒░░░▒░▒▓▓▓▓██▓▓█▓▓▓▓▒░▒░░░▒▓██                   
                   ██▓▓▒░░▒▓▓▓▓▒▓▓▓█▓█▓▒▓▓▓▓▒░░▒▓▓██                   
                  ██▓▓▒▒▓▒▒▒▒▒▒▓███████▓▒▒▒▒▒▒▓▒▒▓▓█                   
                   ██▒░░░░░▒▒▓███████████▓▒▒░░░░░▒██                   
                   ███▓▒▒▒▓████▓▓▓▓█▓▓▓▓████▓▒▒▒▓███                   
                     █████████████████████████████                     
                         █    ███████████    █                         
                                                                                             
""",0.000075)

def pegi():
    print_slow(R"""
████████████████████████████████████████████████████
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒█▒█▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▓▓▓▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▒▒▒▒▒▒▒▒▒▒░      ▒▒▒▒▒▒▒▒▒▒▒▒░░         ░░▒▒▒▒▒▒▒▒█
█▒▒▒▒▒▒▒▒░░       ▒▒▒▒▒▒▒▒▒▒░               ░▒▒▒▒▒▒█
█▒▒▒▒             ▒▒▒▒▒▒▒▒▒░                 ░▒▒▒▒▒█
█▒▒▒▒             ▒▒▒▒▒▒▒▒░        ░▒▒        ▒▒▒▒▒█
█▒▒▒▒             ▒▒▒▒▒▒▒▒░       ░▒▒▒▒░      ░▒▒▒▒█
█▒▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒▒▒░       ▒▒▒▒▒░░░░░░░▒▒▒▒▒█
█▒▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▒▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒▒▒        ▒▒░     ░▒▒▒▒▒▒▒▒█
█▒▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒▒▒        ░         ░▒▒▒▒▒▒█
█▒▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒▒░                   ░▒▒▒▒▒█
█▒▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒▒░                    ░▒▒▒▒█
█▒▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒▒░        ░▒▒▒░       ░▒▒▒▒█
█▒▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒▒▒        ▒▒▒▒▒░      ░▒▒▒▒█
█▒▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒▒▒        ▒▒▒▒▒░      ░▒▒▒▒█
█▒▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒▒▒        ▒▒▒▒▒░      ░▒▒▒▒█
█▒▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒▒▒░       ░▒▒▒▒░      ░▒▒▒▒█
█▒▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒▒▒░        ░░░        ▒▒▒▒▒█
█▒▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒▒▒▒░                 ░▒▒▒▒▒█
█▒▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒▒▒▒▒░               ░▒▒▒▒▒▒█
█▒▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒▒▒▒▒▒▒░░         ░░▒▒▒▒▒▒▒▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
████████████████████████████████████████████████████
██████████████████████████████████▓███▓██████▒██████
██░█▓▒█░░█░▓█░░█░█▓▓██▒░▒█▓░░█▓░▓█░███░█░░░█░░█░░███
██▓▓▒▒█▓▓█░░▒█░█▓▒░███▒█▒▓░▒░▓▒███░███░█░█▒█▒█▒██░██
███░▓█░██░█▓░██░█░▒█▒█░▓▒█░█▒█░▓░█░█▒█░█░█▒█▒█▓▒▓▒██
██████████████████████▒███████░▒░███████████████████
████████████████████████████████████████████████████
""",0.0005)

# Deobfuscated BY HTR-TECH | Tahmid Rayat

# Github    : https://github.com/htr-tech 
# Instagram : https://www.instagram.com/tahmid.rayat
# Facebook  : https://fb.com/tahmid.rayat.oficial 
# Messenger : https://m.me/tahmid.rayat.oficial 

import os,sys,time
os.system("clear")

##### LOGO #####
logo='''
88888888ba   888      88  888888888888
88      "8b  8888     88       88
88      ,8P  88 88    88       88
88_____-8P'  88  88   88       88
88------8b,  88   88  88       88
88      `8b  88    88 88       88
88      a8P  88     8888       88
88888888P"   88      888       88

--------------------------------------------------

 Auther   : Binyamin
 GitHub   : https://github.com/binyamin-binni
 YouTube  : Trick Proof
 Blogspot : https://trickproof.blogspot.com

--------------------------------------------------
                                '''

CorrectUsername = "binyamin"
CorrectPassword = "bnt"

loop = 'true'
while (loop == 'true'):
    print logo
    username = raw_input(" TOOL USERNAME: ")
    if (username == CorrectUsername):
    	password = raw_input(" TOOL PASSWORD: ")
        if (password == CorrectPassword):
            print " Logged in successfully as " + username
            time.sleep(1)
            loop = 'false'
        else:
            print " Wrong Password !"
            os.system('xdg-open https://trickproof.blogspot.com/2020/03/termux-target-command-for-fb-without.html')
            os.system("clear")
    else:
        print " Wrong Username !"
        os.system('xdg-open https://trickproof.blogspot.com/2020/03/termux-target-command-for-fb-without.html')
        os.system("clear")

os.system("python2 .README.md")

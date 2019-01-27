import subprocess
import time
while True:
    print("--------------------------------------")
    print("            BlackArch  Author:KattStof")
    print("            Install           ")
    print("            Script                ")
    print("--------------------------------------")
    print(" ")
    print(" ")
    print("[1] Install All Blackarch *This will take a while go drink some coffee*")
    print("[2] Install Certain Blackarch Tool")
    print("[3] Verify strap.sh")
    print("[4] Only Install Strap.sh")
    print("[0] Exit")
    spam = input(":")
    if spam == '1':
        print("-------------------------------------")
        print("INSTALLING AND EXECUTING STRAP.SH     ")
        print("PLEASE WAIT.........                   ")
        print("--------------------------------------")
        subprocess.call("curl -O https://blackarch.org/strap.sh", shell=True)
        subprocess.call("sudo chmod +x strap.sh", shell=True)
        subprocess.call("sudo ./strap.sh", shell=True)
        subprocess.call("sudo pacman -S blackarch", shell=True)
    elif spam == '2':
        print("------------------------------------")
        print("INSTALLING AND EXECUTING STRAP.SH    ")
        print("PLEASE WAIT.......                  ")
        print("------------------------------------")

        time.sleep(3)
        subprocess.call("curl -O https://blackarch.org/strap.sh", shell=True)
        subprocess.call("sudo chmod +x strap.sh", shell=True)
        subprocess.call("sudo ./strap.sh", shell=True)
        eggs = input("Which tool would you like to install?:")
        subprocess.call("sudo pacman -S " + eggs, shell=True)
    elif spam == '3':
        subprocess.call("curl -O https://blackarch.org/strap.sh", shell=True)
        subprocess.call("sudo sha1sum strap.sh", shell=True)
        print("Above Sha-1 should be:9f770789df3b7803105e5fbc19212889674cd503 strap.sh")
    elif spam == '4':
        subprocess.call("curl -O https://blackarch.org/strap.sh", shell=True)
        subprocess.call("sudo chmod +x strap.sh", shell=True)
        subprocess.call("sudo ./strap.sh", shell=True)
    elif spam == '0':
        print("If you do not go get us a shrubbery we shall nee you again")
        time.sleep(1)
        print("...one that looks good")
        time.sleep(1)
        print("...but not too expensive")
        exit()
    else:
        print("Invalid Option Lrn2keyboard")

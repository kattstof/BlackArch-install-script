import subprocess
print("---------------------------------")
print("            BlackArch  By:KattStof")
print("            Install    v:0.0.1    ")
print("            Script                ")
print("----------------------------------")
print(" ")
print (" ")
print ("[Y] Install All Blackarch *This will take a while go drink some coffee*")
print ("[N] Exit")
chce = input(":")
if chce == 'y':
        subprocess.call("curl -O https://blackarch.org/strap.sh", shell=True)
        subprocess.call("sudo chmod +x strap.sh", shell=True)
        subprocess.call("sudo ./strap.sh", shell=True)
        subprocess.call("sudo pacman -S blackarch", shell=True)
if chce == 'n':
        print("Okay Scipt kiddie, Go back to hackforums")
        exit()

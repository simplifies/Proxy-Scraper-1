import colorama
from colorama import Fore, init
import sys
import os
import requests
import time
import os.path
import ctypes

init(convert=True)

def exitProgram():
    os.system(f'cls')
    print('Exiting')
    sys.exit()

def generate_proxies_http():
    if os.path.exists('http.txt'):
        os.remove("http.txt")
        os.system(f'cls')
        print(Fore.GREEN + 'Generating HTTP proxies...')
        url = 'http://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=US&ssl=all&anonymity=all'
        r = requests.get(url, allow_redirects=True)
        open('http.txt', 'wb').write(r.content)
        print(Fore.GREEN + 'Generated HTTP Proxies to http.txt')
        os.system('pause')
        main()
    else:
        os.system(f'cls')
        print(Fore.GREEN + 'Generating HTTP proxies...')
        url = 'http://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=US&ssl=all&anonymity=all'
        r = requests.get(url, allow_redirects=True)
        open('http.txt', 'wb').write(r.content)
        print(Fore.GREEN + 'Generated HTTP Proxies to http.txt')
        os.system('pause')
        main()

def generate_proxies_socks4():
    if os.path.exists('socks4.txt'):
        os.remove("socks4.txt")
        os.system(f'cls')
        print(Fore.GREEN + 'Generating Socks4 proxies...')
        url = 'http://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=US'
        r = requests.get(url, allow_redirects=True)
        open('socks4.txt', 'wb').write(r.content)
        print(Fore.GREEN + 'Generated Socks4 Proxies to socks4.txt')
        os.system('pause')
        main()
    else:
        os.system(f'cls')
        print(Fore.GREEN + 'Generating Socks4 proxies...')
        url = 'http://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=US'
        r = requests.get(url, allow_redirects=True)
        open('socks4.txt', 'wb').write(r.content)
        print(Fore.GREEN + 'Generated Socks4 Proxies to socks4.txt')
        os.system('pause')
        main()

def generate_proxies_socks5():
    if os.path.exists('socks5.txt'):
        os.remove("socks5.txt")
        os.system(f'cls')
        print(Fore.GREEN + 'Generating Socks5 proxies...')
        url = 'http://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=US'
        r = requests.get(url, allow_redirects=True)
        open('socks5.txt', 'wb').write(r.content)
        print(Fore.GREEN + 'Generated Socks5 Proxies to socks5.txt')
        os.system('pause')
        main()
    else:
        os.system(f'cls')
        print(Fore.GREEN + 'Generating Socks5 proxies...')
        url = 'http://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=US'
        r = requests.get(url, allow_redirects=True)
        open('socks5.txt', 'wb').write(r.content)
        print(Fore.GREEN + 'Generated Socks5 Proxies to socks5.txt')
        os.system('pause')
        main()


def main():
    os.system(f'cls')
    print(Fore.WHITE + "--------------------------------------------------------\n| " + Fore.RED + "Simple Proxy Scraper")
    print(Fore.WHITE + "|" + Fore.CYAN + " [?] Please choose which proxy to scrape.\n" + Fore.WHITE +
     " ----------------------------------------------- \n\n" + Fore.WHITE + "[1] HTTP \n[2] Socks4\n[3] Socks5\n[4] Exit")
    try:
        response = int(input())
        if response < 1 or response > 5:
            os.system(f'cls')
            print('Please choose a valid number.')
            os.system(f'PAUSE')
            main()
    except ValueError:
        print(Fore.RED + 'Not a valid number!')
        print(Fore.RED + 'Please give a valid reponse : 1 or 2 or 3 or 4')
        os.system('pause')
        sys.exit()
    if response == 1:
        generate_proxies_http()
    elif response == 2:
        generate_proxies_socks4()
    elif response == 3:
        generate_proxies_socks5()
    elif response == 4:
        exitProgram()



main()
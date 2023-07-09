import requests
import urllib3
import dns.resolver
import shodan
import sys

def check_url_accessibility(url):
    try:
        response = requests.head(url, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False


def get_ip_address(hostname):
    resolver = dns.resolver.Resolver()
    answers = resolver.resolve(hostname, "A")
    for rdata in answers:
        return str(rdata.address)

def check_open_ports(ip):
    api_key = "ENTER API KEY HERE"
    api = shodan.Shodan(api_key)
    try:
        host = api.host(ip)
        open_ports = []
        for item in host['data']:
            open_ports.append(item['port'])
        return open_ports
    except shodan.APIError as e:
        print(f"Error: {e}")
        return None

def check_url_accessibility(url):
    try:
        response = requests.head(url, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

def on_message():
    color = "\033[93m"
    domain = sys.argv[1]
    url = f"https://{domain}"
    if check_url_accessibility(url):
        print(f"{color}{url}\033[28m is accessible.")
        ip = get_ip_address(domain)
        if ip:
            open_ports = check_open_ports(ip)
            if open_ports:
                print(f"{url} ({ip}) has open ports: {open_ports}")
    else:
        print(f"{url} is not found")
        

on_message()

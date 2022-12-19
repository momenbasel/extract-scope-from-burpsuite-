#!/usr/bin/python3

#script for reading burpsuite scope and extract the urls



#requirements 
#python3 -m pip install -U find_domains iplookup python-whois 
#or pip3 install -r requirements.txt
 
import sys 
from find_domains import find_domains
from iplookup import iplookup
import whois 


ip = iplookup.iplookup
domains = []
subdomains = []
#import os


print("scope is: \n\n")
filename= sys.argv[1]
#filepath= os.path.abspath(os.getcwd())


json_file = open(filename, "r+") 
obj_data = json_file.read()


def find_domain():
	for domain in find_domains(obj_data):
		print(domain)
		domains.append(domain)


def iplook():
	for domain in domains:
		print(f"{domain} :  {ip(domain)}")


def whoisInfo(): 
	for domain in domains:
		try: 
			w = whois.whois(domain)
			print(f"domain {domain} whois resolves to: {w}")
		except Exception:
		 False
		else: 
		 bool(w.domain)



#def subdomainBrute():


#def pathfinder():


find_domain()
iplook()
whoisInfo()

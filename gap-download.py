#!/usr/bin/env python3

import ckanapi
import datetime
import os
import requests
import sys
import subprocess as sp
import concurrent.futures

#Theo Allnutt 2022

'''
Downloads files from the GAP data portal https://data.bioplatforms.com/organization/about/bpa-plants
usage:
gap-download.py samples.txt outfolder/ 8
samples.txt is text file of search terms, usually sample IDs followed by terms, e.g.:

356463, Phylogenomics, Angio353
356888, Phylogenomics, Ozbaits
7665583, Phylogenomics

'8' is number of threads
'''



remote = ckanapi.RemoteCKAN('https://data.bioplatforms.com', apikey='705a5c04-68d4-49a0-bf90-b637e81d6bbb')

def gap_search(field,sample_id):
	print(sample_id)
	data = remote.action.package_search(q="{}:{}".format(field,sample_id),rows=50000,include_private=True)
	#print(data)
	return data

def download(i):
	sample_id=i.rstrip("\n")
	result=(gap_search('title',sample_id))
	

	for package in result['results']:
	
			
	#print(package['resources'])
		for resource in package['resources']:
				
			url = resource['url']
			print("downloading",url)
				
			resp = requests.get(resource['url'], headers={'Authorization': remote.apikey})
				
			filename=url.split("/")[-1]

			p0=sp.Popen('curl -O -L -C - -H "Authorization: 705a5c04-68d4-49a0-bf90-b637e81d6bbb" {}'.format(url),shell=True).wait()
			p1=sp.Popen("mv {} {}".format(filename,outfolder+"/"),shell=True).wait()

	

if __name__ == '__main__':
	
	f=open(sys.argv[1],'r')
	
	outfolder=sys.argv[2]
	
	threads=int(sys.argv[3])

	
	executor1 = concurrent.futures.ProcessPoolExecutor(threads)
	futures1 = [executor1.submit(download,i) for i in f]
	concurrent.futures.wait(futures1)
		
				
	
					
					
					
	
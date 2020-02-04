import requests
from bs4 import BeautifulSoup
import os
import argparse
import subprocess
import joblib
import time

ROOT = "https://projecteuclid.org"
PAUSE = 3

def get_pdf(url, pth):
    _, tail = os.path.split(url)
    print(ROOT + url)
    print(os.path.join(pth, tail+".pdf"))
    subprocess.call(["bash", "get_pe.sh", ROOT + url, os.path.join(pth, tail + ".pdf")])

def rmtree(pth):
    for root, dirs, files in os.walk(pth, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    args = parser.parse_args()
    _, tail = os.path.split(args.url)
    rmtree(tail)
    os.makedirs(tail)
    request = requests.get(args.url)
    soup = BeautifulSoup(request.text)
    pdflinks = []
    for link in soup.find_all('a'):
        if link.get("title") == "PDF":
            pdflinks.append(link.get("href"))
    for url in pdflinks:
        get_pdf(url, tail)
        time.sleep(PAUSE)
    pdffiles = sorted(os.listdir(tail))
    subprocess.call(["pdftk"] + [os.path.join(tail, f) for f in pdffiles] + ["cat", "output", os.path.join(tail, "out.pdf")])
    for f in pdffiles:
        os.remove(os.path.join(tail, f))

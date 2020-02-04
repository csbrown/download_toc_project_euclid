# download_toc_project_euclid
download and merge the contents of the toc page on project euclid books

Usage: 

1) find a table-of-contents page that you can access on project euclid, e.g. https://projecteuclid.org/euclid.chmm/1428680535#toc
2) $ python3 scrape.py <the url from task 1>

This downloads all the bits and shoves them together.
Needs pdftk, wget, python3, python3 beautifulsoup4, python3 requests

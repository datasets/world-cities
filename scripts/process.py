import sqlite3
import csv
import os
import requests
from io import BytesIO
from zipfile import ZipFile
from os import mkdir
from os.path import exists, join
from urllib import request

def step1():    
    # Download the cities15000.zip file
    url = "http://download.geonames.org/export/dump/cities15000.zip"
    response = requests.get(url)
    zipfile = ZipFile(BytesIO(response.content))

    # Extract the cities15000.txt file from the zip archive
    zipfile.extract("cities15000.txt")

    # Create a SQLite database for world-cities
    DBFILE = 'world-cities.sqlite'
    conn = sqlite3.connect(DBFILE)
    c = conn.cursor()

    # Create and populate the city table
    with open('cities15000.txt') as incsv:
        reader = csv.reader(incsv, delimiter="\t")
        c.execute('''CREATE TABLE city
                     (name, country_code, subcountry_code, geonameid)''')
        for geonameid, name, asciiname, alternatenames, latitude, longitude, \
                featureclass, featurecode, countrycode, cc2, admin1code, admin2code, \
                admin3code, admin4code, population, elevation, dem, timezone, \
                modificationdate in reader:
            c.execute("INSERT INTO city VALUES (?, ?, ?, ?)", (name, countrycode, admin1code, geonameid))



    conn.commit()
    conn.close()

def step2():

    # Define the remote file to retrieve
    remote_url = 'http://download.geonames.org/export/dump/admin1CodesASCII.txt'
    # Define the local filename to save data
    local_file = 'admin1CodesASCII.txt'
    # Download remote and save locally
    request.urlretrieve(remote_url, local_file)
    INFILE = 'admin1CodesASCII.txt'
    DBFILE = 'world-cities.sqlite'

    with open(INFILE, encoding='utf-8') as incsv:
        reader = csv.reader(incsv, delimiter="\t")        
        conn = sqlite3.connect(DBFILE)
        c = conn.cursor()
        c.execute('''CREATE TABLE admin1
                     (country_code, subcountry_code, name, geonameid)''')
        for code, name, asciiname, geonameid in reader:
            country_code, subcountry_code = code.split('.', 2)
            c.execute("INSERT INTO admin1 VALUES (?, ?, ?, ?)", (country_code, subcountry_code, name, geonameid))
        conn.commit()
        conn.close()

def step3():

    # Define the remote file to retrieve
    remote_url = 'http://download.geonames.org/export/dump/countryInfo.txt'
    # Define the local filename to save data
    local_file = 'countryInfo.txt'
    # Download remote and save locally
    request.urlretrieve(remote_url, local_file)
    INFILE = 'countryInfo.txt'
    DBFILE = 'world-cities.sqlite'
    conn = sqlite3.connect(DBFILE)
    c = conn.cursor()

    def skip_comment(instream):
        for line in instream:
            if line[0] != "#":
                yield line

    with open('countryInfo.txt') as incsv:
        reader = csv.reader(skip_comment(incsv), delimiter="\t")
        c.execute('''CREATE TABLE country
                     (country_code, name, geonameid)''')
        for ISO, ISO3, ISONumeric, fips, Country, Capital, Area, \
                Population, Continent, tld, CurrencyCode, CurrencyName, \
                Phone, PostalCodeFormat, PostalCodeRegex, Languages, \
                geonameid, neighbours, EquivalentFipsCode in reader:
            c.execute("INSERT INTO country VALUES (?, ?, ?)", (ISO, Country, geonameid))
        conn.commit()
        conn.close()


def step4():

    # Create and populate the world-cities.csv file
    OUTFILE = 'data/world-cities.csv'
    DBFILE = 'world-cities.sqlite'
    HEADERS = ['name', 'country', 'subcountry', 'geonameid']
    conn = sqlite3.connect(DBFILE)
    c = conn.cursor()
    sql = '''SELECT 
                city.name, 
                country.name, 
                IFNULL(admin1.name, "N/A"),
                city.geonameid
             FROM city 
                LEFT OUTER JOIN country ON city.country_code = country.country_code
                LEFT OUTER JOIN admin1 ON city.subcountry_code = admin1.subcountry_code AND city.country_code = admin1.country_code
             '''
    with open(OUTFILE, 'w') as outcsv:
        writer = csv.writer(outcsv, lineterminator="\n")
        writer.writerow(HEADERS)
        for name, country, subcountry, geonameid in c.execute(sql):
            writer.writerow([name, country, subcountry, geonameid])

    # Create and populate the ambiguities.csv file
    OUTFILE = 'ambiguities.csv'
    HEADERS = ['name', 'country', 'subcountry', 'nb']
    conn = sqlite3.connect(DBFILE)
    c = conn.cursor()
    sql = '''SELECT 
                city.name, 
                country.name, 
                IFNULL(admin1.name, "N/A"),
                COUNT(*) as nb
             FROM city 
                LEFT OUTER JOIN country ON city.country_code = country.country_code
                LEFT OUTER JOIN admin1 ON city.subcountry_code = admin1.subcountry_code AND city.country_code = admin1.country_code
             GROUP BY 
                city.name, 
                country.name, 
                IFNULL(admin1.name, "N/A")
             HAVING COUNT(*) > 1
             '''
    with open(OUTFILE, 'w', newline='') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(HEADERS)
        for name, country, subcountry, nb in c.execute(sql):
            writer.writerow([name, country, subcountry, nb])

def world_cities_process():
    step1()
    step2()
    step3()
    step4()
    os.remove("admin1CodesASCII.txt")
    os.remove("ambiguities.csv")
    os.remove("cities15000.txt")
    os.remove("countryInfo.txt")
    os.remove("world-cities.sqlite")
if __name__ == '__main__':
    world_cities_process()

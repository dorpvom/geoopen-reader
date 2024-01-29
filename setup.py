from setuptools import setup
from pathlib import Path

import requests

DB_DIR = Path(__file__).parent / 'geoopen_reader' / 'db'

COUNTRY_PATH = (DB_DIR / 'GeoOpen-Country.mmdb')
if not COUNTRY_PATH.exists():
    COUNTRY_PATH.write_bytes(requests.get('https://cra.circl.lu/opendata/geo-open/mmdb-country/latest.mmdb').content)

ASN_PATH = (DB_DIR / 'GeoOpen-Country-ASN.mmdb')
if not ASN_PATH.exists():
    ASN_PATH.write_bytes(requests.get('https://cra.circl.lu/opendata/geo-open/mmdb-country-asn/latest.mmdb').content)

setup()

from setuptools import setup
from pathlib import Path

import requests

DB_DIR = Path(__file__).parent / 'geoopen_reader' / 'db'

(DB_DIR / 'GeoOpen-Country.mmdb').write_bytes(requests.get('https://cra.circl.lu/opendata/geo-open/mmdb-country/latest.mmdb').content)
(DB_DIR / 'GeoOpen-Country-ASN.mmdb').write_bytes(requests.get('https://cra.circl.lu/opendata/geo-open/mmdb-country-asn/latest.mmdb').content)

setup()

#!/usr/bin/env python3
#
# This database access code is largely ripped of from mmdb-server by Alexandre Dulaunoy.
# Here is his docstring:
#
# mmdb-server is an open source fast API server to lookup IP addresses for their geographic location.
#
# The server is released under the AGPL version 3 or later.
#
# Copyright (C) 2022 Alexandre Dulaunoy
#
# My contributions:
# Copyright (C) 2024 Johannes vom Dorp, Fraunhofer FKIE

import logging
import time
from ipaddress import ip_address
import json
from typing import List

import maxminddb
from pathlib import Path

MMDB_FILES = [
    Path(__file__).parent / "db/GeoOpen-Country.mmdb",
    Path(__file__).parent / "db/GeoOpen-Country-ASN.mmdb"
]
COUNTRY_INFO = json.loads((Path(__file__).parent / "db/country.json").read_text())


class GeoLookup:
    def __init__(self):
        self.databases = []
        for mmdb_file in MMDB_FILES:
            meta = {}
            meta['reader'] = maxminddb.open_database(str(mmdb_file), maxminddb.MODE_MEMORY)
            meta['description'] = meta['reader'].metadata().description
            meta['build_db'] = time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime(meta['reader'].metadata().build_epoch)
            )
            meta['db_source'] = meta['reader'].metadata().database_type
            meta['nb_nodes'] = meta['reader'].metadata().node_count
            self.databases.append(meta)

    @staticmethod
    def valid_ip_address(address: str) -> bool:
        try:
            type(ip_address(address))
            return True
        except ValueError:
            return False

    @staticmethod
    def country_lookup(country: str) -> dict:
        if country != 'None' or country is not None or country != 'Unknown':
            if country in COUNTRY_INFO:
                return COUNTRY_INFO[country]
            else:
                return {}
        else:
            return {}

    def look_up_address(self, address: str) -> List[dict]:
        collected_results = []
        if not self.valid_ip_address(address):
            logging.error(
                f"IPv4 or IPv6 address {address} is in an incorrect format. "
                "Dotted decimal for IPv4 or textual representation for IPv6 are required."
            )
            return collected_results
        for database in self.databases:
            single_result = database['reader'].get(address)
            meta = database.copy()
            del meta['reader']
            single_result['meta'] = meta
            single_result['ip'] = address
            if single_result['country']['iso_code'] != 'None':
                single_result['country_info'] = self.country_lookup(
                    country=single_result['country']['iso_code']
                )
            else:
                single_result['country_info'] = {}
            collected_results.append(single_result)
        return collected_results

# geoopen-reader

This project is a hack of Alexandre's implementation to shortcut hosting a server while making use of his well-thought-out output format and usage. It is as of now a PoC, used for a research project. Feel free to open issues anyway.

Please refer to [Alexandre's README](https://github.com/adulau/mmdb-server) for all information regarding the original mmdb-server.

## Installation

- `pip3 install .`
- `cd ./db; bash update.sh; cd ..` (to get the latest version of the GeoOpen database)

## Usage

### Lookup of an IP address

Invoke a lookup

```python
from geoopen_reader.reader import GeoLookup

lookup = GeoLookup()
print(json.dumps(lookup.look_up_address('188.65.220.25'), indent=2))
```

results in such output

```json
[
  {
    "country": {
      "iso_code": "BE"
    },
    "meta": {
      "description": {
        "en": "Geo Open MMDB database - https://github.com/adulau/mmdb-server"
      },
      "build_db": "2022-02-05 11:37:33",
      "db_source": "GeoOpen-Country",
      "nb_nodes": 1159974
    },
    "ip": "188.65.220.25",
    "country_info": {
      "Country": "Belgium",
      "Alpha-2 code": "BE",
      "Alpha-3 code": "BEL",
      "Numeric code": "56",
      "Latitude (average)": "50.8333",
      "Longitude (average)": "4"
    }
  },
  {
    "country": {
      "iso_code": "BE",
      "AutonomousSystemNumber": "49677",
      "AutonomousSystemOrganization": "MAEHDROS-AS"
    },
    "meta": {
      "description": {
        "en": "Geo Open MMDB database - https://github.com/adulau/mmdb-server"
      },
      "build_db": "2022-02-06 10:30:25",
      "db_source": "GeoOpen-Country-ASN",
      "nb_nodes": 1159815
    },
    "ip": "188.65.220.25",
    "country_info": {
      "Country": "Belgium",
      "Alpha-2 code": "BE",
      "Alpha-3 code": "BEL",
      "Numeric code": "56",
      "Latitude (average)": "50.8333",
      "Longitude (average)": "4"
    }
  }
]
```

## Output format (from mmdb-server README)

The output format is an array of JSON object (to support the ability to serve multiple geo location database).  Each JSON object of the JSON array includes a `meta`, `country`, `ip` and `country_info` fields. The `country` give the geographic location of the IP address queried. The `meta` field includes the origin of the MMDB database which the the metadata. `ip` returns the queried IP address. `country_info` gives additional information about the country such as `Country`, `Alpha-2 code`, `Alpha-3 code`, `Numeric code`, Latitude and Longitude (average centric value).

## Public online version of mmdb-server (from mmdb-server README)

- [https://ip.circl.lu/](https://ip.circl.lu/) - lookup via [https://ip.circl.lu/geolookup/8.8.8.8](https://ip.circl.lu/geolookup/8.8.8.8)
- [https://ipv4.circl.lu](https://ipv4.circl.lu/) If you are dual-homed IPv6/IPv4, return your IPv4 address. 
- [https://ipv6.circl.lu](https://ipv6.circl.lu/) If you are dual-homed IPv6/IPv4, return your IPv6 address. 

## License

```
    Copyright (C) 2022 Alexandre Dulaunoy 
    Copyright (C) 2024 Johannes vom Dorp

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
```

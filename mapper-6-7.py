#!/usr/bin/env python3

"""
This mapper parses input with the following shape:
'172.16.0.3 - - [25/Sep/2002:14:04:19 +0200] "GET / HTTP/1.1" 401 - "" "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1) Gecko/20020827"'
"""

import sys
import re

REGEX = '([(\d\.)]+) (.*?) (.*?) \[(.*?) (.*?)\] "(.*?) (.*?) (.*?)" (\d+) (-{0,1}\d{0,})'

for line in sys.stdin:
    data = re.match(REGEX, line).groups()
    if 10 != len(data):
        continue
    ipv4, \
        client_id, \
        user_id, \
        date_time, \
        time_zone, \
        method, \
        resource, \
        protocol, \
        status, \
        size = data

    print(f"{ipv4}")

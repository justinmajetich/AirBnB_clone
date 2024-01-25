#!/usr/bin/python3
import sys
import requests
from lxml import html
import re

states = [
    ('421a55f4-7d82-47d9-b51c-a76916479545', 'stateA'),
    ('421a55f4-7d82-47d9-b51c-a76916479546', 'stateB'),
    ('421a55f4-7d82-47d9-b52c-a76916479547', 'stateC'),
    ('421a55f4-7d82-47d9-b53c-a76916479548', 'stateD'),
    ('421a55f4-7d82-47d9-b57c-a76916479549', 'stateE')
]

NO_PROXY = {
    'no': 'pass',
}


## Request
page = requests.get('http://0.0.0.0:5000/states_list', proxies=NO_PROXY)
if int(page.status_code) != 200:
    print("Status fail: {}".format(page.status_code))
    sys.exit(1)

## Parsing
tree = html.fromstring(page.content)
if tree is None:
    print("Can't parse page")
    sys.exit(1)

## H1
h1_tags = tree.xpath('//body/h1/text()')
if h1_tags is None or len(h1_tags) == 0:
    print("H1 tag not found")
    sys.exit(1)

if not re.search(r".*States.*", h1_tags[0]):
    print("Title `States` doesn't found")
    sys.exit(1)

## LI state ID
li_tags = list(filter(None, [x.replace(" ", "").strip(" ").strip("\n").strip("\t") for x in tree.xpath('//body/ul/li/text()')]))
if li_tags is None or len(li_tags) != 5:
    print("Doesn't find 5 LI tags (found {})".format(len(li_tags)))
    sys.exit(1)

for li_tag in li_tags:
    is_found = False
    for state_tuple in states:
        is_found = re.search(r".*{}.*".format(state_tuple[0]), li_tag)
        if is_found:
            break
    if not is_found:
        print("{} not found".format(li_tag))
        sys.exit(1)
            
## LI state name sorted
li_tags_b = list(filter(None, [x.replace(" ", "").strip(" ").strip("\n").strip("\t") for x in tree.xpath('//body/ul/li/b/text()')]))
if li_tags_b is None or len(li_tags_b) != 5:
    print("Doesn't find 5 LI tags with B tag (found {})".format(len(li_tags_b)))
    sys.exit(1)

idx = 0
for li_tag in li_tags_b:
    if not re.search(r".*{}.*".format(states[idx][1]), li_tag):
        print("{} not found or not sorted".format(li_tag))
        sys.exit(1)
    idx += 1

print("OK", end="")

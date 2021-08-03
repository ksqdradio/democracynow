#!/usr/bin/env python

import xmltodict
import urllib.request
import dropbox
import pathlib
import shutil


readfile = True
usedropbox = True


def read_dn_xml(filename):
    with urllib.request.urlopen(filename) as fd:
        return xmltodict.parse(fd.read())


def get_token(filename):
    with open(filename, "r") as f:
        return f.readline().strip()


xml = read_dn_xml("http://www.democracynow.org/podcast-stations.xml")
latest = xml["rss"]["channel"]["item"][0]
url = latest["enclosure"]["@url"]
file_name = url.split("/")[-1]
print(f"Latest URL: {url}")
print(f"Latest DN filename: {file_name}")

if readfile:
    with urllib.request.urlopen(url) as response, open(file_name, "wb") as out_file:
        shutil.copyfileobj(response, out_file)

if usedropbox:
    apitoken = get_token("dropbox.apitoken")
    d = dropbox.Dropbox(apitoken)
    with open(file_name, "rb") as f:
        meta = d.files_upload(
            f.read(), "/" + file_name
        )  # , mode=dropbox.files.WriteMode("overwrite"))
    print(meta)

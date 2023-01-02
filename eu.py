#!/usr/bin/env python

import shutil
import urllib.request

import dropbox
import xmltodict

readfile = True
usedropbox = True


def read_dn_xml(filename):
    with urllib.request.urlopen(filename) as fd:
        return xmltodict.parse(fd.read())


def get_token(filename):
    with open(filename, "r") as f:
        return f.readline().strip()


xml = read_dn_xml(
    "http://audioport.org/rss.php?series=Economic+Update&id=37687970af9b74eafdb03455c8f47372"
)
print(xml["rss"]["channel"]["item"].keys())
latest = xml["rss"]["channel"]["item"]
url = latest["enclosure"]["@url"]
file_name = url.split("/")[-1]
file_date = file_name.split("_")[2]
clean_file = latest["title"]
clean_file = clean_file.split(":")[0]
clean_file = "".join(clean_file.split())
clean_file = clean_file + "-" + file_date + ".mp3"
print(f"Latest URL: {url}")
print(f"Latest filename: {file_name}")
print(f"Clean filename: {clean_file}")

if readfile:
    with urllib.request.urlopen(url) as response, open(clean_file, "wb") as out_file:
        shutil.copyfileobj(response, out_file)

if usedropbox:
    apitoken = get_token("dropbox.apitoken")
    d = dropbox.Dropbox(apitoken)
    with open(clean_file, "rb") as f:
        meta = d.files_upload(
            f.read(), "/Economic Update-Richard Wolff/" + clean_file
        )  # , mode=dropbox.files.WriteMode("overwrite"))
    print(meta)

#!/usr/bin/env python3

import os
import requests
import subprocess
import sys

if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

response = requests.get("https://api.github.com/users/gabormajerszky/repos")
repos_json = response.json()

os.chdir("..")
directories = set(os.listdir("."))

for repo in repos_json:
    name = repo["name"]
    clone_url = repo["clone_url"]
    if name in directories:
        print("Skipped {} - directory already exists".format(name))
    else:
        print("Cloning {}...".format(name))
        cmd = "git clone " + clone_url
        return_code = subprocess.call(cmd)
        if return_code == 0:
            print("Cloned {}".format(name))
        else:
            print("Failed to clone {}".format(name))

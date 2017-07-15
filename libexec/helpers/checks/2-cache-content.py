#!/usr/bin/env python
# 
# Copyright (c) 2017, SingularityWare, LLC. All rights reserved.
# Copyright (c) 2015-2017, Gregory M. Kurtzer. All rights reserved.
# Copyright (c) 2017, Vanessa Sochat. All rights reserved.
#
# Alert the user about files in the cache

import platform
import sys
import os

os_base,os_name,os_version = platform.linux_distribution()
os_base = os_base.lower()

returncode = 0

# Apt-get cache
if os_base in ["debian","ubuntu"]:

    skip = ['partial','lock']
    count = len([x for x in os.listdir("/var/cache/apt/archives/")
                if x not in skip])

    # The apt cache should be cleaned
    if count > 0:
        print("PROBLEM:  apt-get cache should be cleaned.")
        print("RESOLVE:  sudo apt-get clean")
        returncode = 1

    # The cache should only have apt debconf ldconfig
    skip = ["apt", "debconf", "ldconfig"]
    cache_dirs = [x for x in os.listdir("/var/cache") 
                  if x not in skip]
    if len(cache_dirs) > 3:
        to_remove = "\n".join(["rm -rf /var/cache/%s" %x for x in cache_dirs])
        print("PROBLEM:  /var/cache has uneccessary entries")
        print("RESOLVE:  \n%s" %to_remove)
        returncode = 1
    

sys.exit(returncode)

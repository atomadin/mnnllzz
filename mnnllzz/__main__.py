#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import glob
import json

from .mnnllzz import typeset_tests

ver_string = "1.0.1"

texfiles = glob.glob("*.tex")

if (len(texfiles) < 1):
    sys.exit("TeX file not found in current directory.")
elif (len(texfiles) > 1):
    sys.exit("More than one TeX file found in current directory.")
else:
    print("\n  mnnllzz %s\n" % ver_string)

files = open(texfiles[0],"r").read().split("MNNLLZZ")

template_text = files[0]
params = json.loads(files[1])

typeset_tests(params, template_text)

# -*- coding: utf-8 -*-
"""Check that version numbers match.

Check version number in setup.json and aiida_statefile_scheduler/__init__.py and make sure
they match.
"""
from __future__ import absolute_import
from __future__ import print_function
import os
import json
import sys

this_path = os.path.split(os.path.realpath(__file__))[0]

# Get content of setup.json
SETUP_FNAME = 'setup.json'
SETUP_PATH = os.path.join(this_path, os.pardir, SETUP_FNAME)
with open(SETUP_PATH) as f:
    setup_content = json.load(f)

# Get version from python package
sys.path.insert(0, os.path.join(this_path, os.pardir))
import aiida_statefile_schedulers  # pylint: disable=wrong-import-position

VERSION = aiida_statefile_schedulers.__version__

if VERSION != setup_content['version']:
    print('Version number mismatch detected:')
    print("Version number in '{}': {}".format(SETUP_FNAME,
                                              setup_content['version']))
    print("Version number in '{}/__init__.py': {}".format(
        'aiida_statefile_scheduler', VERSION))
    sys.exit(1)

# Overwrite version in setup.json
#setup_content['version'] = version
#with open(SETUP_PATH, 'w') as f:
#	json.dump(setup_content, f, indent=4, sort_keys=True)

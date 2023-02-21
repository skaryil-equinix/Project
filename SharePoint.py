from shareplum import Site, Office365
from shareplum.site import Version

import os
import json

from FileLocation import FileLocation

configPath = None

with open(configPath) as config_file:
    config = json.load(config_file)
    config = config['share_point']

username = None
password = None

sharepoint_URL = None
sharepoint_site = None

class SharePoint(FileLocation):


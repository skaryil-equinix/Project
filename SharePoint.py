from shareplum import Site, Office365
from shareplum.site import Version

import os
import json

from FileLocation import FileLocation

configPath = None

with open(configPath) as config_file:
    config = json.load(config_file)
    config = config['share_point']

USERNAME = config['user']
PASSWORD = config['password']
SHAREPOINT_URL = config['url']
SHAREPOINT_SITE = config['site']
SHAREPOINT_DOC = config['doc_library']

class SharePoint(FileLocation):

    def __init__(self):
        self._folder = None
        self.folder = None
        self.sharepoint_dir = None
        self.auth_site = None
        self.site = None
        self.authcookie = None

    def auth(self):
        self.authcookie = Office365(SHAREPOINT_URL, username=USERNAME, password=PASSWORD).GetCookies()
        self.site = Site(SHAREPOINT_SITE, version=Version.v365, authcookie=self.authcookie)

        return self.site

    def connect_folder(self, folder_name):
        self.auth_site = self.auth()

        self.sharepoint_dir = '\\'.join([SHAREPOINT_DOC, folder_name])
        self.folder = self.auth_site.Folder(self.sharepoint_dir)

        return self.folder

    def connect_to_list(self, ls_name):
        self.auth_site = self.auth()

        list_data = self.auth_site.List(list_name=ls_name).GetListItems()

        return list_data

    def download_file(self, file_name, folder_name):
        self._folder = self.connect_folder(folder_name)
        return self._folder.get_file(file_name)
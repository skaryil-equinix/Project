from FileLocation import FileLocation
import pysftp
import re

cnOpts = pysftp.CnOpts()
cnOpts.hostkeys = None

hostName = None
userName = None
password = None
remotePath = None
localPath = None
regex_pattern = None
filename_matching_regex = []

with pysftp.Connection(hostName, username=userName, password=password, cnopts=cnOpts) as sftp:
    print("Connected to server")
    sftp.cwd("/")
    sftp.get(remotePath, localPath)  # get a remote file


class SFTPServer(FileLocation):

    def set_connection_to_database(self):
        pass

    def read_directory_with_regrex(self):

        list_dir = sftp.listdir_attr()
        for filename in list_dir:
            if re.search(self.regex_pattern, filename):
                self.filename_matching_regex.append(filename)

        return self.filename_matching_regex

from FileLocation import FileLocation
import pysftp
import re


class SFTPServer(FileLocation):
    cnOpts = pysftp.CnOpts()
    cnOpts.hostkeys = None

    hostName = None
    userName = None
    password = None
    remotePath = None
    localPath = None
    regex_pattern = None
    filename_matching_regex = []

    def set_connection_to_database(self):
        with pysftp.Connection(self.hostName, username=self.userName, password=self.password,
                               cnopts=self.cnOpts) as sftp:
            print("Connected to server")
            sftp.cwd("/")
            sftp.get(self.remotePath, self.localPath)  # get a remote file
            list_dir = sftp.listdir_attr()

            for filename in list_dir:
                if re.search(self.regex_pattern, filename):
                    self.filename_matching_regex.append(filename)

    def read_directory_with_regrex(self):
        return self.filename_matching_regex

from FileLocation import FileLocation
import pysftp

class SFTPServer(FileLocation) :

    cnOpts = pysftp.CnOpts()
    cnOpts.hostkeys = None

    hostName = None
    userName = None
    password = None
    remotePath = None
    localPath = None

    def sftp_list_files(self):
        with pysftp.Connection(self.hostName, username= self.userName, password=self.password,cnopts=self.cnOpts) as sftp:
            sftp.get(self.remotePath,self.localPath)  # get a remote file

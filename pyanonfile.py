import requests
import json
import os
import urllib

class pyAnonFile():
    def __init__(self, file, service = 'anonfile'):
        self.file = file
        self.service = service
        server_list = {'anonfile': 'https://api.anonfiles.com',
                        'openload': 'https://api.openload.cc',
                        'letsupload': 'https://api.letsupload.cc',
                        'megaupload': 'https://api.megaupload.nz',
                        'bayfiles': 'https://api.bayfiles.com'}

        imagefile = {'file': open(self.file, 'rb')}

        self.response = requests.post(server_list[self.service] if not self.service == None else 'anonfile' + '/upload', files=imagefile)

        self.status = (self.response.json()['status'])
        if self.status == False: return("Failed to upload file")

        return()

    def getLink(self, encode=True):
        self.filelink = (self.response.json()['data']['file']['url']['full'])
        if encode == True:
            self.filelink = urllib.parse.quote_plus(self.filelink)
        return(self.filelink)

    def getRaw(self):
        return(self.response.json())

    def getStatus(self):
        return(self.status)
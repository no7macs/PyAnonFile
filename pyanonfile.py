import requests
import urllib

class upload:
    def __init__(self, file, service = 'anonfile'):
        self.file = file
        self.service = service
        server_list = {'anonfile': 'https://api.anonfiles.com',
                        'openload': 'https://api.openload.cc',
                        'letsupload': 'https://api.letsupload.cc',
                        'megaupload': 'https://api.megaupload.nz',
                        'bayfiles': 'https://api.bayfiles.com'}

        imagefile = {'file': open(self.file, 'rb')}

        response = requests.post(server_list[self.service] + '/upload', files=imagefile)
        self.response = response.json()

        self.status = ((self.response)['status'])
        if self.status == False: pass

        return

    def getLink(self, encode=False):
        self.filelink = (self.response['data']['file']['url']['full'])
        if encode == True:
            self.filelink = urllib.parse.quote_plus(self.filelink)
        return(self.filelink)

    def getRaw(self):
        return(self.response)

    def getStatus(self):
        return(self.status)
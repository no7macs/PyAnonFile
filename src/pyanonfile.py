import requests
import urllib
    
def upload(file, service = 'anonfile') -> dict:
    server_list = {'anonfile': 'https://api.anonfiles.com',
                    'openload': 'https://api.openload.cc',
                    'letsupload': 'https://api.letsupload.cc',
                    'megaupload': 'https://api.megaupload.nz',
                    'bayfiles': 'https://api.bayfiles.com'}
    imagefile = {'file': open(file, 'rb')}
    response = requests.post(server_list[service] + '/upload', files=imagefile).json()
    if (response)['status'] == False: return(None)
    return(response)

def getLink(response, encode=False) -> str:
    if not response == None:
        filelink = (response['data']['file']['url']['full'])
        if encode == True:
            filelink = urllib.parse.quote_plus(filelink)
        return(filelink)
    return('')

def getStatus(response) -> bool:
    if not response == None:
        return((response)['status'])
    return(False)
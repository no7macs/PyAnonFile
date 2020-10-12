import requests, json, os, random

def upload(filetype,**kwars):
    output = kwars.get('output',None)
    website = kwars.get('website',None)
    server_list = {'anonfile': 'https://api.anonfiles.com',
                        'openload': 'https://api.openload.cc',
                       'letsupload': 'https://api.letsupload.cc',
                       'megaupload': 'https://api.megaupload.nz',
                       'bayfiles': 'https://api.bayfiles.com'}

    imagefile = {'file': open(filetype, 'rb')}

    if website == 'anonfile' or website == None:
        response = requests.post(server_list['anonfile']+'/upload', files=imagefile)
    elif website == 'letsupload':
         response = requests.post(server_list['letsupload']+'/upload', files=imagefile)
    elif website == 'openload':
        response = requests.post(server_list['openload']+'/upload', files=imagefile)
    elif website == 'megaupload':
        response = requests.post(server_list['megaupload']+'/upload', files=imagefile)
    elif website == 'bayfiles':
        response = requests.post(server_list['bayfiles']+'/upload', files=imagefile)

    print("--REPONSE--" + str(response))

    status = (response.json()['status'])
    filelink = (response.json()['data']['file']['url']['full'])

    if status == False: return("Failed to upload file")

    if output == None or output == 'link':
        return filelink
    elif output == 'raw': 
        return response.json()
    elif output == 'status':
        return status
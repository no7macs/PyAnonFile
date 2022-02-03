# PyAnonFile
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/no7macs/PyAnonFile.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/no7macs/PyAnonFile/context:python)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/no7macs/PyAnonFile.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/no7macs/PyAnonFile/alerts/)

## Usage

### to upload a file:
```
pyanonfile.upload('/myfile', service = 'anonfile')
```
- in
    - takes a file directory (relative or complete)
    - can take the name of a service that is in the list of services
        - anonfile
        - openload
        - letsupload
        - megaupload
        - bayfiles
- out
    - if a sucess: returns a dictionary data from the upload 
    - if failed: returns None

### to get the uplaod link
```
pyanonfile.getLink(upload, encode=False)
```
- in
    - Requires the dictionary returned from the "upload" function 
    - Optionally it can take the encode boolean to use % encoding, "False" by default
- out 
    - if a sucess: returns the file url as a string
    - if failed: returns and empty string

### to get upload status
```
pyanonfile.getStatus(upload)
```
- in
    - takes the dictionary returned by the "upload function"
- out
    - if a sucess: returns True
    - if failed: returns False

## Usage example
```
import PyAnonFile

upload = pyanonfile.upload('/somefile', service = 'anonfile') # returns a dictionary of the uplad info
status = pyanonfile.getStatus(upload) # returns the status of the upload
link = pyanonfile.getLink(upload, encode = True) # returns the link to the file encoded
```
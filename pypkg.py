import os
import time
import requests

def instPkg(pkg):
    print("Searching for", pkg, "and installing...")

    downloadName = pkg + ".py"

    url = 'https://pyospypkg.puter.site/' + downloadName

    response = requests.get(url)

    # Check if the request was successful (status code 200 means OK)
    if response.status_code == 200:
        # Open a local file to write the content to
        with open(downloadName, 'wb') as file:
            file.write(response.content)
        print("File downloaded successfully! (Located in /Home/Programs)")
        instPkgHelp(pkg)
    else:
        print(f"This program does not exist. Status code: {response.status_code}")

def instPkgHelp(pkg2):
    print("Searching for", pkg2, "and installing...")

    downloadName = pkg2 + "help" + ".txt"

    url = 'https://pyospypkg.puter.site/' + downloadName

    response = requests.get(url)

    # Check if the request was successful (status code 200 means OK)
    if response.status_code == 200:
        # Open a local file to write the content to
        with open(downloadName, 'wb') as file:
            file.write(response.content)
        print("Helpfile downloaded successfully!")
    else:
        print(f"This program does not exist. Status code: {response.status_code}")

def removePkg(pkgDir):
    rmcmd = "rm " + pkgDir + ".py"
    os.system(str(rmcmd))
    print("Package", pkgDir, "sucsessfully removed.")

def listPkgs():
    api_url = 'https://pyospypkg.puter.site/'

    # Send a GET request to the API
    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:
        files = response.json()  # Assuming the API returns a JSON list of file names
        for file in files:
            print(file)
        else:
            print(f"Failed to retrieve files. Status code: {response.status_code}")

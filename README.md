# PyPKG
A simple Python package manager that you can implement into your Python operating system.

## All functions

> instPkg(pkg)
Appends ".py" to the pkg variable input and installs the package from your webserver/repo.

> instPkgHelp(pkg2)
Gets the .txt file of the name of the package with help on how to use the package.

> removePkg(pkgDir)
Deletes the specified package.

## How it works

It fetches the specified Python file from your specified webserver or GitHub repository then downloads it, along with its helpfile (just a text file) for integration in a Python OS "help" command.

It takes input from the instPkg() function. You put the name of the package on your webserver/repo you want to install in the function, then it appends ".py" to the end of it for ease of use.

The "URL" variable is the URL of your webserver/repo that you want your files to be in.

Also, sorry if I didn't explain it the best, I'm new to GitHub and have never really had to explain how my code works in-depth lol :)

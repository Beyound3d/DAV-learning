# Solutions_And_Installation

Welcome to the Installation repository! This document outlines the steps needed to install and set up the necessary components for the project.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation Steps](#installation-steps)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contact](#contact)

# Prerequisites
- [Node.js](https://nodejs.org/) (version 14 or higher)
- [Python](https://www.python.org/downloads/) 
- [Git](https://git-scm.com/)
- Any other dependencies required for your project.


## Python ()
<img src="https://github.com/beyound3d/Solutions_And_Installation/blob/master/pythonbanner.png" width="50dp" height="50dp"/>

**check installation succeesful**
```
python --version
```

```
py --version
```

**To open shell**
```
python -v
```

```
py
```

**What is the shortcut key to exit from Python shell?**
Keyboard shortcuts to exit Python

In the Python interpreter or terminal, you can exit Python by pressing Ctrl + Z on Windows or Ctrl + D on macOS.
These shortcuts signal the interpreter that the file is complete and tell it to terminate Python. Like os. _exit(),
this method does not execute any cleanup tasks.

## Node js
**Successful installlation**
```
node -v
```

```
npm -v
```
## Express js 
Install node before express it a framework of nodejs
```
npm i express
```
## Git
**In between compare sign fill your details**
```
git config --global user.name <Username>
```


```
git status
```

```
git init
```


or file name after add
```
git add .
```
 
```
touch
```


```
git commit -m <commit msz>
```

create repo in GitHub before ADDING TO GITHUB
```
git remote add origin <gitUrl>
```

```
git remote
```

```
git push -u origin master
```

**pull changes to local repository**
```
git pull origin master --allow-unrelated-histories
```

**push changes to remote repo after pull**
  something related to upstream
  to manage LF and CRLF
  ```
git config --global core.autocrlf true
```


**undo commit changes from staged area to local area**
```
git rm --cached -r .
```

 ```
 git reset --hard
```

 ```
 git add .
```

```
 git commit -m "Normalize line endings"
```

**merge branch**
```
git update-ref -d MERGE_HEAD
```



## Troubleshooting
If you encounter issues during installation, consider the following steps:

- Ensure all prerequisites are met.
- Check for typos in command-line inputs.
- Review the logs for any error messages.
- Search the Issues section of the repository for similar problems.


**Feel free to modify any sections to better fit your project’s needs!**

   

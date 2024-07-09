# git-commands
[Reference talk](https://chatgpt.com/share/fe7796d8-a73c-41ad-b41c-57aaf5008bb2)

## Working with remote repository
* git status
* git init
* git add . or file name after add
* touch <filename>
* git config --global user.name "<name>"
* git commit -m "initial commit"
* git remote add origin "<link>"
* git remote
* git push -u origin master

## pull chaanges to local repository 
git pull origin master --allow-unrelated-histories

## push changes to remote repo after pull
 something related to upstream

## to manage LF and CRLF 
git config --global core.autocrlf true

## undo commit changes from staged area to local area 
git rm --cached -r .
git reset --hard
git add .
git commit -m "Normalize line endings"

## merge branch 
 git update-ref -d MERGE_HEAD


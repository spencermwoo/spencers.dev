#!/bin/bash
upstream='origin'

# update release
git fetch $upstream
git checkout develop
git pull --rebase $upstream develop && {
	git pull --rebase $upstream release
	git merge develop
} || {
	exit
}

if [ $? -ne 0 ]; then
	exit
fi

tag release
release=$(date '+%Y.%m.%d' | cut -c 3-)
echo $release > RELEASE

git commit -am "Bump release to $release"
git tag $release
git push $upstream release --tags

# create release
gh release create $release  --title "v$release" --notes ""

# build and update
cd scripts
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
bash update.sh
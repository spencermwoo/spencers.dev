#!/bin/bash
upstream='origin'

git fetch $upstream
git checkout develop
git pull --rebase $upstream develop
git pull --rebase $upstream release
git merge develop


release=$(date '+%Y.%m.%d' | cut -c 3-)
echo $release > RELEASE

git commit -am "Bump release to $release"
git tag $release-t1
git push $upstream release --tags

# gh release create $release  --title "v$release" --notes ""

# cd scripts
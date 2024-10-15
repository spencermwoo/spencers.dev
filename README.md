# spencers.dev

https://spencers.dev/

# overview
The architecture was originally developed for my game server but it's used here to quickly tear-down or spin-up this website.

Specifically we're using
* [Terraform](https://www.terraform.io/) to manage [DigitalOcean](https://www.digitalocean.com/) machines
* [Cloudflare](https://www.cloudflare.com/) to manage DNS records
* [11ty](https://github.com/11ty/eleventy) static site generator

These technological choices were primarily made for fun and learning.

# folder layout

```
.
|-- nginx
|-- scripts
|-- static
|-- web
`-- web_puzzle
```

### [nginx](https://github.com/spencermwoo/spencers.dev/tree/main/nginx)
Configuration files for the NGINX webserver

### [scripts](https://github.com/spencermwoo/spencers.dev/tree/main/scripts)
Scripts used to destroy or regenerate the hosted website

### [static](https://github.com/spencermwoo/spencers.dev/tree/main/static)
Static websites to be hosted without compilation

### [web](https://github.com/spencermwoo/spencers.dev/tree/main/web)
Source files for website content

### [web_puzzle](https://github.com/spencermwoo/spencers.dev/tree/main/web_puzzle)
Folder containing files for hosting easter egg puzzle

# release

`./release.sh`

```
git fetch origin
git checkout develop
git pull --rebase origin develop
git pull --rebase origin release
git merge develop
vi RELEASE
git commit -am "Bump release to x.y.z"
git tag x.y.z-rc1
git push origin release --tags

gh release create x.y.z  --title "vx.y.z" --notes ""
```
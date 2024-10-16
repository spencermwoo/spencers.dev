# scripts

```
export D_PAT=
export CF_API_TOKEN=
```


```
py -m venv .venv
source .venv/bin/activate
py -m pip install -r requirements.txt

py -V
Python 3.12.4

pip -V
pip 24.1.1
```

# deploy
`./create.sh`

# update
`./update.sh`

# debug
`./connect.sh`

```
cd /etc/nginx/sites-available/
cd /var/www/spencers.dev/html/

service nginx reload
systemctl restart nginx

nginx -t
nginx -T | grep "spencers.dev"

tail -f /var/log/nginx/access.log
```

# todo

There's much to improve here.
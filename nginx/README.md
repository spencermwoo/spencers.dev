```
/etc/nginx/sites-available
/etc/nginx/sites-enabled

sudo ln -s /etc/nginx/sites-available/spencers.dev /etc/nginx/sites-enabled/

service nginx reload
systemctl restart nginx

nginx -t
nginx -T | grep "spencers.dev"

tail -f /var/log/nginx/access.log
```
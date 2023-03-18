#!/bin/bash

# crontab -e
# 0 * * * * /home/your_user/check_status.sh

##
# Discord webhook
##
url="https://discord.com/api/webhooks"

##
# List of websites to check
##
websites_list="spencers.dev spencermwoo.github.io"

for website in ${websites_list} ; do
        status_code=$(curl --write-out %{http_code} --silent --output /dev/null -L ${website})

        if [[ "$status_code" -ne 200 ]] ; then
            # POST request to Discord Webhook with the domain name and the HTTP status code
            curl -H "Content-Type: application/json" -X POST -d '{"content":"'"${domain} : ${status_code}"'"}'  $url
        fi
done
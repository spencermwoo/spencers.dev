#!/bin/bash

# ======================
# 0) PREREQUISITES
./_init.sh

# ======================
# 1) CREATE PLAN
terraform -chdir=terra plan -var "do_token=${D_PAT}" -var "pvt_key=$HOME/.ssh/id_rsa" -input=false -out=tfplan

sleep 5

echo '
		Creating DO droplet.
		'

# ======================
# 2) APPLY PLAN
terraform -chdir=terra apply -input=false tfplan

sleep 90

ipv4=$(terraform -chdir=terra output -raw droplet_ipv4_address)
ipv6=$(terraform -chdir=terra output -raw droplet_ipv6_address)

echo '
		Successfully created DO droplet : ${ipv4}
		'
echo $ipv4

# ======================
# 3) Create CF DNS entry
domain='spencers.dev'
type='A'

echo '
		Creating CF record for domain.

		'

(cd cf && ./run-add.sh $ipv4 $domain $type)

# Create CF DNS entries for subdomains as well...
(cd cf && ./run-add.sh $ipv4 puzzle $type)
(cd cf && ./run-add.sh $ipv4 api $type)
(cd cf && ./run-add.sh $ipv4 test $type)

echo '
		Successfully added A record : 
			${ip} ${domain}
			${ip} api
			${ip} puzzle
			${ip} test
		'

# ======================
# 4) Add server to known_hosts
ssh-copy-id root@$ipv4
# cat ~/.ssh/id_rsa.pub | ssh root@$ipv4 'cat >> ~/.ssh/authorized_keys'

echo '
		Building site : eleventy
		'

# ======================
# 5) Upload static site files

./update.sh
# if [[ "$OSTYPE" =~ ^msys ]]; then
# 	py upload.py --server $ipv4 --username root
# else
# 	python3 upload.py --server $ipv4 --username root
# fi
# run setup-block.sh - configure nginx

# run setup-monitor.sh - configure monitoring

# run test-setup.sh - confirm

# ======================
# 6) Copy static dirs
# cp -a ../static/ ../_site
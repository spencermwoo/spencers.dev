# email

email domains

# send

`py devmail.py`

# recieve

* pull emails from s3 bucket

	`aws s3 sync s3://email1-spencersdev download`

* view emails via `.eml`

	`for f in download/*; do mv -- "$f" "${f}.eml"; done`
	`rm download/*`

* delete emails from s3 bucket

	`aws s3 rm s3://email1-spencersdev --recursive --dryrun`
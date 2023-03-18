https://docs.digitalocean.com/reference/api/api-reference/#operation/sizes_list
https://registry.terraform.io/providers/digitalocean/digitalocean/latest/docs

```
curl -X GET \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DIGITALOCEAN_TOKEN" \
  "https://api.digitalocean.com/v2/sizes" 
```

terraform init

terraform plan -var "do_token=${D_PAT}" -var "pvt_key=$HOME/.ssh/id_rsa"

terraform apply -var "do_token=${D_PAT}" -var "pvt_key=$HOME/.ssh/id_rsa"

terraform show terraform.tfstate

terraform refresh -var "do_token=${D_PAT}" -var "pvt_key=$HOME/.ssh/id_rsa"

terraform plan -destroy -out=terrform.tfplan -var "do_token=${D_PAT}" -var "pvt_key=$HOME/.ssh/id_rsa"

terraform apply terraform.tfplan

terraform -chdir=terra output
terraform -chdir=terra show

----

setup ssh denial

VM hardening

https://docs.digitalocean.com/reference/api/api-reference/#tag/Sizes
curl -X GET \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DIGITALOCEAN_TOKEN" \
  "https://api.digitalocean.com/v2/sizes" 
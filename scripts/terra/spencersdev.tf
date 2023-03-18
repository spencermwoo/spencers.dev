resource "digitalocean_droplet" "spencersdev" {
  image = "ubuntu-18-04-x64"
  name = "spencersdev"
  region = "sfo3"
  size = "s-1vcpu-512mb-10gb"
  backups = false
  monitoring = false
  ipv6 = true
  ssh_keys = [
    data.digitalocean_ssh_key.small.id
  ]
  tags = ["spencersdev"]
  user_data = file("config/config.sh")
  connection {
    host = self.ipv4_address
    user = "root"
    type = "ssh"
    public_key = file(var.pvt_key)
    timeout = "2m"
  }
}

output "droplet_ipv4_address" {
  value = digitalocean_droplet.spencersdev.ipv4_address
}

output "droplet_ipv6_address" {
  value = digitalocean_droplet.spencersdev.ipv6_address
}
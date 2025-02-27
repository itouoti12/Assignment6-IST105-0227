# Assignment6-IST105-0227


sudo chmod +x /var/www/html/data_management.py

```bash
sudo dnf update -y
sudo dnf install -y httpd
sudo dnf install python3 -y
sudo dnf install -y php
sudo dnf -y install git
cd /var/www/html
sudo git clone https://github.com/itouoti12/Assignment6-IST105-0227.git .
sudo chmod +x /var/www/html/data_management.py
sudo systemctl start httpd

```
#!/bin/bash
sudo yum install httpd -y
sudo systemctl start httpd
sudo chkconfig httpd on 
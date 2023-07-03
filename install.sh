#!/bin/bash


sudo apt install nmap -y

sudo apt update -y
sudo apt upgrade -y

sudo apt install masscan -y

wget "https://go.dev/dl/go1.20.5.linux-amd64.tar.gz"
rm -rf /usr/local/go && tar -C /usr/local -xzf go1.20.5.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin
go version

sudo apt install gobuster


echo "[+] Done"


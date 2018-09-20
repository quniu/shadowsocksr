#!/bin/bash
rm -rf CyMySQL
rm -rf cymysql
yum install -y wget
wget https://github.com/nakagami/CyMySQL/archive/REL_0_9_4.tar.gz
tar zxvf REL_0_9_4.tar.gz
mv CyMySQL-REL_0_9_4/cymysql/ ./

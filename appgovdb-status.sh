#!/bin/bash
source ./mysql/mysql.config
$DOCKERI mysqladmin -u root --password=$MYSQL_ROOT_PASSWORD processlist

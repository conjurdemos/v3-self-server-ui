#!/bin/bash
source ./mysql/mysql.config
$DOCKERIT mysql -h $MYSQL_HOSTNAME -u root --password=$MYSQL_ROOT_PASSWORD

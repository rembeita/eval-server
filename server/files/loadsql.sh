#!/bin/bash
sleep 10
cd /tmp/test_db
/usr/bin/mysql -uroot -peval-server -h 127.0.0.1 --port=3306 < /tmp/test_db/employees.sql

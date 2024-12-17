@echo off

docker exec -t -u postgres telegram_tests-db-1 pg_dumpall -c > dump.sql

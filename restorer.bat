@echo off

type .\dump.sql | docker exec -i telegram_tests-db-1  psql -Upostgres
type .\dump.sql | docker exec -i telegram_tests-db-1  psql -Upostgres
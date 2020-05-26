#!/bin/bash

docker build -t opencart_tests .;
docker run --name opencart opencart_tests;
docker cp opencart:/app/allure_report .;
allure serve allure_report;
rm -rf allure_report;
docker system prune
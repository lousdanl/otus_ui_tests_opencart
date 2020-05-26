#!/bin/bash

sudo docker build -t opencart_tests ~/otus_ui_tests_opencart;
sudo docker run --name opencart opencart_tests;
sudo docker cp opencart:/app/allure_report ~/otus_ui_tests_opencart;
sudo allure-2.7.0/bin/allure serve ~/otus_ui_tests_opencart/allure_report;
sudo rm -rf allure_report;
sudo docker system prune -a
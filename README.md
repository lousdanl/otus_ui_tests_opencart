# OPENCART - UI TESTS 


Для ручного запуска тестов выполнить следующие требования:
1. Клонировать репозиторий.
2. Установить браузер Chrome или Firefox.
3. Установить драйвер версии браузера, добавить путь до драйвера в переменную среды.
4. Установить зависимости:

        pip install -r requirements.txt

5. Запускать:
 
       pytest --alluredir allure_report   
       --selenoid={True,False, default=False}
       --browser={chrome,firefox, default="chrome"}
       --executor={url для запуска на удаленной машине}
       --url={url opencart}
       --time={TIME implicitly_wait, default=0}
       --file={log file, default="output.log"}
6. После выполнения для просмотра отчета выполнить:

        allure serve allure_report
    
       
Для запуска тестов в докере, выполнить из корня репозитория следующую команду.
Если команда не найдена, сделать файл исполняемым. 
В системе должен быть установлен allure2.
    
        ./tests_suite.sh


ИЛИ

Собрать проект:

        docker build -t opencart_tests .
Запустить контейнер и тесты:

        docker run --name opencart opencart_tests 
        [здесь можно указать команду которую нужно выполнить внутри контейнера 
        с необходимыми параметрами как в пн.5, 
        указать флаг -it]
Получить отчет. В системе должен быть установлен allure2.

        docker cp opencart:/app/allure_report .;
        allure serve allure_report;
        
Удалить отчет и удалить контейнер:

        rm -rf allure_report;
        docker system prune
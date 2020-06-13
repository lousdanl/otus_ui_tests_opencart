# OPENCART - UI TESTS 


Для ручного запуска тестов выполнить следующие требования:
1. Клонировать репозиторий.
2. Установить браузер Chrome или Firefox.
3. Установить драйвер версии браузера, добавить путь до драйвера в переменную среды.
4. Установить зависимости:

        pip install -r requirements.txt

5. Запускать:
 
       pytest --alluredir allure-results   
       --selenoid={True,False, default=False}
       --browser={chrome,firefox, default="chrome"}
       --executor={url для запуска на удаленной машине}
       --url={url opencart}
       --time={TIME implicitly_wait, default=0}
       --file={log file, default="output.log"}
6. После выполнения для просмотра отчета выполнить:

        allure serve allure-results
    
       
Для запуска тестов в докере c selenoid, выполнить из корня репозитория следующую команду.

Собрать проект:

        docker-compose build
Запустить контейнеры и тесты:

        docker-compose up --no-start 
        docker start selenoid selenoid-ui
        docker start -a tests 

Получить отчет. В системе должен быть установлен allure2.

        docker cp tests:/app/allure-results .
        allure serve allure-results
        
Удалить отчет и удалить контейнер:

        rm -rf allure-results
        docker-compose down
        docker system prune -f
        

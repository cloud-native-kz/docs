# Быстрое создание задач с помощью API Explorer 

## Шаг 1: Вход в консоль Cloud API

Перейдите в [консоль Cloud API](https://console.tencentcloud.com/api/explorer?Product=cvm&Version=2017-03-12&Action=DescribeRegions) и войдите, используя учетные данные своего аккаунта. Если у вас возникнут проблемы с авторизацией аккаунта, см. раздел [Авторизация аккаунта](https://www.tencentcloud.com/document/product/1041/69220) для завершения настройки прав доступа.

## Шаг 2: Выберите API интерфейс

- **Быстрое создание задачи обработки VOD**

Для быстрого создания задачи обработки VOD перейдите на страницу [API Explorer](https://console.tencentcloud.com/api/explorer?Product=mps&Version=2019-06-12&Action=ProcessMedia). Выберите продукт "Media Processing Service (MPS)"; нажмите "**Processing Task Initiation APIs > ProcessMedia > JSON**"; затем найдите соответствующие поля входных параметров в JSON.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/5a8c0e348c8911f0814e525400bf7822.png)

- **Быстрое создание задачи обработки трансляции**

Для быстрого создания задачи обработки трансляции перейдите на страницу [API Explorer](https://console.tencentcloud.com/api/explorer?Product=mps&Version=2019-06-12&Action=ProcessMedia). Выберите продукт "Media Processing Service (MPS)"; нажмите "**Processing Task Initiation APIs > ProcessLiveStream > JSON**"; затем найдите соответствующие поля входных параметров в JSON.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/927e01878c8911f0ae9d5254001c06ec.png)

## Шаг 3: Заполните код JSON и инициируйте вызов

В поля входных параметров введите код JSON для инициирования задачи — путем прямого ввода или вставки. Перед инициированием вызова вы можете при необходимости настроить параметры в этих полях. После завершения настройки нажмите **Initiate Invocation** для прямого запуска задачи.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/a4ce8e358c8911f088af5254005ef0f7.png)

## Шаг 4: Запросите результаты задачи

После инициирования вызова будет автоматически сгенерирован **TaskId**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/ba410dba8c8911f0b321525400e889b2.png)

- Вы можете проверить статус выполнения и результаты вывода соответствующих задач в консоли Media Processing Service (MPS) в разделе "Task Management" ([VOD Processing Tasks](https://console.tencentcloud.com/mps/tasks/vod-list) или [Live Processing Tasks](https://console.tencentcloud.com/mps/tasks/live-list)).
- Кроме того, вы можете напрямую вызвать **Task Management APIs** и ввести **TaskId** для запроса статуса выполнения задачи и результатов вывода.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/13798c258c8a11f0814e525400bf7822.png)


---
*Источник: [https://www.tencentcloud.com/document/product/1041/73127](https://www.tencentcloud.com/document/product/1041/73127)*

---
*Источник (EN): [quickly-create-tasks-using-api-explorer.md](./quickly-create-tasks-using-api-explorer.md)*

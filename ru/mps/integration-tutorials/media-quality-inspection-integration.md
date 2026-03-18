# Интеграция проверки качества медиа

## Сценарий 1: Проверка качества файла VOD

### Метод 1: Инициирование задачи в консоли

#### Шаг 1: Создание оркестрации VOD

1. Войдите в консоль MPS, нажмите [Create VOD Orchestration](https://console.tencentcloud.com/mps/workflows/vod/add) и добавьте узел Media Quality Inspection в поле Actions.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/41f303d771d611f0b9a25254007c27c5.png)

2. После добавления узла откроется новая страница. На этой странице выберите предопределённый системный шаблон или создайте пользовательский шаблон на основе фактического сценария бизнеса. Затем сохраните параметры.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/4276b9bd9a8311f09936525400e889b2.png)

3. По завершении конфигурации узла нажмите кнопку **Create** в нижней части страницы, чтобы завершить создание оркестрации.
4. После создания оркестрации вернитесь к списку оркестраций VOD, найдите в списке только что созданную оркестрацию и нажмите переключатель, чтобы её включить. Оркестрация вступит в силу примерно через 3–5 минут после включения.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/f83f96d3d2e811ef81865254005ef0f7.png)

#### Шаг 2: Инициирование задачи проверки качества VOD

После того как оркестрация вступит в силу, загрузите файлы VOD, требующие проверки качества, в директорию триггера, указанную в конфигурации оркестрации. Загруженные файлы будут обработаны для проверки качества в соответствии с настроенным узлом и шаблоном оркестрации.

#### Шаг 3: Управление задачами проверки качества VOD

Задачи проверки качества можно просматривать на странице [VOD Processing Tasks](https://console.tencentcloud.com/mps/tasks/vod-list).

![](https://staticintl.cloudcachetci.com/cms/backend-cms/0d36d57be43411efb98e525400e889b2.png)

### Метод 2: Вызов API для обработки

#### Шаг 1: Инициирование задачи проверки качества VOD

Для инициирования задачи обработки видеоURL-адресов или медиафайлов в COS см. [ProcessMedia](https://www.tencentcloud.com/zh/document/product/1041/33640) в документации API.

Пример запроса:

```
POST / HTTP/1.1Host: mps.tencentcloudapi.comContent-Type: application/jsonX-TC-Action: ProcessMedia
```

```
{  "InputInfo": {    "Type": "COS",    "CosInputInfo": {      "Bucket": "test-<appid>",      "Region": "ap-shanghai",      "Object": "/video/test.mp4"    }  },  "AiQualityControlTask": {    "Definition": 10  }}
```

Описание примера:

1. Type может быть установлен как COS или URL. Заполните путь исходного файла на основе значения Type.
2. Definition указывает ID шаблона, настроенного в задаче. Шаблоны создаются путём вызова CreateQualityControlTemplate.

Пример ответа:

```
}  "Response": {    "TaskId": "26000002-ScheduleTask-8c0bb3a13e10462fc405262c623aeff4tt7"  }}
```

Описание примера: TaskId указывает уникальный ID задачи, который используется для запроса и управления задачами.

#### Шаг 2: Запрос деталей задачи

Вы можете запросить статус выполнения и детальный результат задачи по ID задачи. Для получения дополнительной информации см. [DescribeTaskDetail](https://www.tencentcloud.com/zh/document/product/1041/33644) в документации API.

Пример запроса:

```
POST / HTTP/1.1Host: mps.tencentcloudapi.comContent-Type: application/jsonX-TC-Action: DescribeTaskDetail
```

```
{  "TaskId": "26000002-ScheduleTask-8c0bb3a13e10462fc405262c623aeff4tt7"}
```

Пример ответа:

```
}  "Response": {    "WorkflowTask": {      "Output": {        "QualityControlResultSet": [          {            "Type": "BackWhiteEdge",            "QualityControlItems": [              {                "Confidence": 100,                "StartTimeOffset": 12,                "EndTimeOffset": 12              }            ]          }        ],        "ContainerDiagnoseResultSet": [          {            "Category": "StreamAbnormalCharacteristics",            "DateTimeSet": [],            "SeverityLevel": "Warning",            "TimestampSet": [              11.006            ],            "Type": "AudioDuplicatedFrame"          }        ],        "QualityEvaluationScore": 68      }    }  }}
```

### Просмотр результатов проверки качества

После инициирования задачи проверки качества вы можете просмотреть отчёт о результатах проверки качества на странице [VOD Task Management](https://console.tencentcloud.com/mps/tasks/vod-list).

![](https://staticintl.cloudcachetci.com/cms/backend-cms/469b4fbb71df11f09f3d52540099c741.png)

#### Отчёт о результатах проверки качества

Отчёт о результатах проверки качества показывает результаты проверки и содержит информацию о видео и предпросмотры. Включённые элементы проверки позволяют пользователям проверить частоту возникновения проблем качества и общую оценку видео.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/60ee60c871df11f081ce52540044a08e.png)

Если во время проверки качества видео обнаруживаются какие-либо проблемы, отображаются конкретные временные сегменты, где возникают проблемы. Вы можете щёлкнуть мышью на шкале времени, чтобы перейти непосредственно к соответствующему сегменту видео и просмотреть конкретную проблему.

На странице списка проблем проверки качества вы можете просмотреть точное время отчёта для каждой проблемы проверки качества, что позволяет вам более точно определить и проанализировать проблемы.

## Сценарий 2: Проверка качества трансляции

### Метод 1: Инициирование задачи в консоли

#### Шаг 1: Создание оркестрации трансляции

1. Войдите в консоль MPS, нажмите [Create Live Orchestration](https://console.tencentcloud.com/mps/workflows/live/add) и добавьте узел Media Quality Inspection в поле Actions.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/6e71928d71d611f0b9a25254007c27c5.png)

2. После добавления узла откроется новая страница. На этой странице выберите предопределённый системный шаблон или создайте пользовательский шаблон на основе фактического сценария бизнеса. Затем сохраните параметры.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/6de58c53d2e911ef82a5525400e889b2.png)

3. По завершении конфигурации узла нажмите кнопку **Create** в нижней части страницы, чтобы завершить создание оркестрации.
4. После создания оркестрации вернитесь к списку оркестраций трансляции и найдите в списке только что созданную оркестрацию.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/8fd0f8d4d2e911efb1a552540099c741.png)

#### Шаг 2: Создание задачи проверки качества трансляции

Перейдите на страницу [Live Processing Tasks](https://console.tencentcloud.com/mps/tasks/live-list), нажмите **Create task**, введите адрес трансляции для обработки на странице создания задачи, выберите оркестрацию трансляции, созданную на предыдущем этапе, при необходимости заполните другую информацию и нажмите **Create**, чтобы завершить создание.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d8ca694871d611f096685254001c06ec.png)

#### Шаг 3: Управление задачами проверки качества трансляции

Задачи проверки качества можно просматривать на странице [Live Processing Tasks](https://console.tencentcloud.com/mps/tasks/live-list).

### Метод 2: Вызов API для обработки

#### Шаг 1: Инициирование задачи проверки качества трансляции

Для инициирования задачи обработки трансляции см. [ProcessLiveStream](https://www.tencentcloud.com/zh/document/product/1041/33641) в документации API.

Пример запроса:

```
POST / HTTP/1.1Host: mps.tencentcloudapi.comContent-Type: application/jsonX-TC-Action: ProcessLiveStream
```

```
{  "Url": "rtmp://tlivecloud.com/live/test",  "TaskNotifyConfig": {    "NotifyType": "URL",    "NotifyUrl": "http://tlivecloud.com/callback"  },  "AiQualityControlTask": {    "Definition": 10  }}
```

Описание примера:

1. Url указывает адрес трансляции.
2. TaskNotifyConfig указывает адрес сервиса обратного вызова. При обнаружении проблемы в видеопотоке информация о проблеме будет отправлена на этот адрес в реальном времени.

Пример ответа:

```
}    "Response": {        "TaskId": "24000002-live-procedure-813dc41e6fdc22dcf24aa6e9c61cp92"    }}
```

Описание примера: TaskId указывает уникальный ID задачи, который используется для запроса и управления задачами.

#### Шаг 2: Анализ уведомлений трансляции и выполнение обратного вызова для проблем

После получения сообщения содержимое уведомления о событии обработки трансляции MPS анализируется из поля msgBody в сообщении. Для получения деталей см. [ParseLiveStreamProcessNotification](https://www.tencentcloud.com/zh/document/product/1041/33680).

Если при инициировании задачи проверки качества трансляции установлена TaskNotifyConfig, информация об обнаруженных проблемах трансляции будет отправлена на настроенный адрес в реальном времени.

Пример запроса обратного вызова:

```
POST / HTTP/1.1Content-Type: application/json
```

```
{  "NotificationType": "AiQualityControlResult",  "TaskId": "24000002-procedure-live-813dc41e6fdc22dcf24aa6e9c61cp92",  "AiQualityControlResultInfo": {    "QualityControlResultSet": [      {        "Type": "BackWhiteEdge",        "QualityControlItems": [          {            "Confidence": 100,            "StartTimeOffset": 12,            "EndTimeOffset": 12          }        ]      }    ],    "DiagnoseResultSet": [      {        "Category": "StreamStatusException",        "Type": "StreamOpenFailed",        "Timestamp": 0,        "Description": "Open url failed.",        "DateTime": "2023-11-06T06:37:28Z",        "SeverityLevel": "Fatal"      }    ]  }}
```

Описание примера: QualityControlResultSet указывает информацию о проблемах, обнаруженных посредством проверок качества содержимого. DiagnoseResultSet указывает информацию о проблемах, обнаруженных посредством диагностики формата.


---
*Источник: [https://www.tencentcloud.com/document/product/1041/67727](https://www.tencentcloud.com/document/product/1041/67727)*

---
*Источник (EN): [media-quality-inspection-integration.md](./media-quality-inspection-integration.md)*

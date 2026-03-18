# Учебное пособие по интеллектуальному выделению ключевых моментов

## Обзор

Функция интеллектуального выделения ключевых моментов использует интеллектуальные алгоритмы для автоматического захвата и создания выделенных моментов видео, предоставляя пользователям быстрый просмотр и возможность обмена.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/f8bf9524a2fd11efb81c52540055f650.png)

#### Демонстрация

1. Перейдите в [Experience Center](https://mps.live/demo/ai/highlight), чтобы открыть страницу интеллектуального выделения ключевых моментов. На правой стороне выберите либо локальный видеофайл, либо трансляцию в прямом эфире, укажите категорию видеоконтента и нажмите **One-Click Processing**.
2. После завершения обработки вы можете просмотреть результаты.

> **Примечание:** Функции демонстрационной версии MPS относительно простые и предназначены только для ознакомления с базовым эффектом. Используйте доступ через API для тестирования полного функционала.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/014db0a8563211f090d5525400bf7822.png)

## Предустановленный шаблон

Служба обработки медиа (MPS) предоставляет предустановленный шаблон интеллектуального выделения ключевых моментов (**Идентификатор шаблона: 26**). Вы можете инициировать задачи интеллектуального выделения ключевых моментов на основе этого шаблона. Для получения подробных инструкций см. раздел ниже [Инициирование задачи интеллектуального выделения ключевых моментов](#Highlights).

![](https://staticintl.cloudcachetci.com/cms/backend-cms/8e65a222a19e11ef834b525400f69702.png)

## Инициирование задач интеллектуального выделения ключевых моментов

## **Сценарий первый: обработка локальных видеофайлов**

### Метод 1: интеграция через API

#### 1. Быстрая проверка с помощью API Explorer

Сначала перейдите в [консоль MPS](https://console.tencentcloud.com/mps/index) для активации сервиса и подтвердите, что [авторизация COS](https://www.tencentcloud.com/document/product/1041/33482#.E6.AD.A5.E9.AA.A42.EF.BC.9A.E6.8E.88.E6.9D.83.E7.AE.A1.E7.90.86) завершена.

Затем перейдите на страницу [API Explorer](https://console.intl.cloud.tencent.com/api/explorer?Product=mps&Version=2019-06-12&Action=ProcessMedia) для онлайн-отладки, выберите интерфейс `ProcessMedia` и заполните пути входа/выхода и идентификатор шаблона. Установите **Definition** в `AiAnalysisTask` на **26** (предустановленный шаблон для интеллектуального выделения ключевых моментов) и используйте **ExtendedParameter** для конкретных функций. Подробная информация о расширенных параметрах приведена в разделе ниже [Расширенные параметры](#note).

> **Примечание:** API Explorer будет автоматически преобразовывать данные, поэтому вы можете напрямую заполнить соответствующий JSON для ExtendedParameter без преобразования его в строку. Однако при прямом вызове API необходимо экранировать строку JSON. Пример ExtendedParameter: {"hht":{"top_clip":10, "force_cls":5003, "need_vad":1, "threshold":0.9, "merge_time":60, "merge_type":0, "res_save_type":1}} Для понимания смысла параметров см. раздел ниже [Описание расширенных параметров](#note). Чтобы обеспечить качество обработки, рекомендуется связаться с нами для подтверждения конкретной конфигурации в автономном режиме.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/102b7daca30311efa5395254002693fd.png)

#### 2. Инициирование через API

Выше было описано, как использовать API Explorer для вызова и отладки интерфейса в режиме онлайн. Вы также можете напрямую инициировать POST-запрос к Tencent Cloud. Домен запроса API: mps.tencentcloudapi.com. При инициировании POST-запроса определение — это идентификатор предустановленного шаблона интеллектуального выделения ключевых моментов (26). Ниже приведен эталонный пример запроса:

> **Примечание:** При прямом вызове API необходимо экранировать строку JSON при вводе параметра ExtendedParameter.

```
{    "InputInfo": {        "Type": "URL",        "UrlInputInfo": {            "Url": "https://mg-aidata-1258344699.cos-internal.ap-guangzhou.tencentcos.cn/test/hht_test/MyStoryForYouEP39.mp4"        }    },    "OutputStorage": {        "Type": "COS",        "CosOutputStorage": {            "Bucket": "mg-aidata-1258344699",            "Region": "ap-guangzhou"        }    },    "OutputDir": "/test_data/",    "AiAnalysisTask": {        "Definition": 26,        "ExtendedParameter": "{\\"hht\\":{\\"top_clip\\":10, \\"force_cls\\":5003, \\"need_vad\\":1, \\"threshold\\":0.9, \\"merge_time\\":60, \\"merge_type\\":0, \\"res_save_type\\":1}}"    }}
```

#### 3. Запрос результатов задачи

- Обратный вызов задачи: при использовании [ProcessMedia](https://www.tencentcloud.com/document/product/1041/33640) для инициирования задачи MPS вы можете установить информацию обратного вызова через параметр `TaskNotifyConfig`. После обработки задачи результат задачи будет передан через установленную информацию обратного вызова. Вы можете анализировать результаты уведомлений о событиях с помощью [ParseNotification](https://www.tencentcloud.com/document/product/1041/33679).
- Запрос через API [DescribeTaskDetail](https://www.tencentcloud.com/document/product/1041/33644):
  - Для задач, запущенных с помощью API и шаблона, как описано в **методе интеграции 1** выше, используйте `TaskId` из [ProcessMedia](https://www.tencentcloud.com/document/product/1041/33640) (например: 24000022-WorkflowTask-b20a8exxxxxxx1tt110253) для анализа `AiAnalysisResultSet` в `WorkflowTask`.
  - Для задач, запущенных через [ProcessMedia](https://www.tencentcloud.com/document/product/1041/33640) без шаблона, но с `ScheduleId`, возвращаемый `TaskId` будет содержать "ScheduleTask" (например, 24000022-ScheduleTask-774f101xxxxxxx1tt110253). В этом сценарии используйте `TaskId` для анализа `ActivityResultSet` в `ScheduleTask`.
  - Для задач, инициированных из консоли, как описано в **методе интеграции 2** ниже, перейдите в [Задачи -> VOD](https://console.tencentcloud.com/mps/tasks/vod-list) для получения идентификатора задачи и результатов. Вы также можете анализировать `ActivityResultSet` в `ScheduleTask` в API [DescribeTaskDetail](https://www.tencentcloud.com/document/product/1041/33644), чтобы получить результаты задачи.
- Запрос задачи через консоль: перейдите в консоль [VOD Processing Tasks](https://console.intl.cloud.tencent.com/mps/tasks/vod-list), новые инициированные задачи будут отображены в списке задач.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/d8c192dfa61811efae7d5254002693fd.png)

Когда статус подзадачи станет "Success", вы можете перейти в **COS Bucket > Output Bucket** для поиска вашей выходной директории, а файлы, начинающиеся с `hht` в директории, являются выходными файлами интеллектуального выделения ключевых моментов, включая видеофайлы и изображения обложек.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/e0a225e1a61811efb7b7525400bdab9d.png)

### Метод 2: инициирование задачи через консоль (автоматическое создание без кода)

> **Примечание:** Инициирование задачи из консоли требует предустановленного шаблона (предустановленные параметры интеллектуального выделения ключевых моментов). Из-за некоторых специальных параметров в выделении ключевых моментов, которые невозможно настроить в шаблоне, это может повлиять на эффект интеллектуального выделения ключевых моментов. Поэтому рекомендуется использовать интеграцию через API.

#### 1. Создание задачи

1.1. Перейдите в [консоль MPS](https://console.intl.cloud.tencent.com/mps/tasks/create) и нажмите **Creating a Task > Quick Create a VOD Processing Task.**

![](https://staticintl.cloudcachetci.com/cms/backend-cms/5c066820a1a011ef992f52540075b605.png)

1.2. Сначала укажите входной видеофайл. В настоящее время функция горизонтального преобразования видео в вертикальное поддерживает два типа источников входных данных: [Tencent Cloud Object Storage (COS)](https://www.tencentcloud.com/products/cos) и ссылка для загрузки по URL. AWS S3 не поддерживается.

1.3. Затем добавьте **Intelligent Analysis** на этапе "Process Input Files".

![](https://staticintl.cloudcachetci.com/cms/backend-cms/4b936aaba1a011efa04c5254002693fd.png)

1.4. В всплывающем окне параметров интеллектуального анализа выберите **Intelligent Highlights Preset Template (Template ID:26)**.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/81afc2b1a1a011efa0b3525400bdab9d.png)

1.5. Наконец, укажите путь сохранения выходного видео и нажмите **Create** для инициирования задачи.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/fc5dbbc4a1a011efa646525400329841.png)

#### **2. Запрос результатов задачи**

См. указанный выше раздел [3. Запрос результатов задачи](#result).

#### 3. Автоматическое запуск задач (необязательно)

Если вы хотите загрузить видеофайл в сегмент COS и достичь автоматического интеллектуального удаления согласно предустановленным параметрам, вы можете:

3.1. Нажмите **Save the Orchestration** при создании задачи и настройте сегмент триггера, директорию триггера и другие параметры во всплывающем окне.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/fb326c22a30411efb3de525400d5f8ef.png)

3.2. Затем перейдите в **VOD Orchestration List**, найдите только что созданную оркестровку и включите ее, нажав кнопку **Enable**. Для последующих новых видеофайлов в директории триггера задачи будут автоматически запускаться согласно предустановленному процессу и параметрам в оркестровке, и обработанные видеофайлы будут сохранены в выходной путь, настроенный оркестровкой.

> **Примечание:** Вступление в силу занимает 3-5 минут после успешного включения оркестровки.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/214f1157a30611efa5395254002693fd.png)

## Сценарий второй: обработка прямых трансляций

### 1. Инициирование запросов

#### **Инициирование запросов через API Explorer**

Для инициирования задачи обработки прямой трансляции путем вызова API вы можете обратиться к [Initiate Processing on Live Streams](https://www.tencentcloud.com/document/product/1041/33641). Вы можете нажать [API Explorer Debugging](https://console.tencentcloud.com/api/explorer?Product=mps&Version=2019-06-12&Action=ProcessLiveStream) в файле для перехода на страницу и заполнить соответствующую информацию о параметрах для инициирования онлайн-вызова.

OutputStorage можно заполнить, указав на обработку сценария с локальным видео выше. Ниже приведен пример ExtendedParameter, и конкретное значение параметров можно найти в разделе [Расширенные параметры](#note).

```
 {"hht":{"top_clip":10, "force_cls":5003, "need_vad":1, "res_save_type":1}}
```

![](https://staticintl.cloudcachetci.com/cms/backend-cms/ad52d5a1a32a11efae16525400bdab9d.png)

#### **Инициирование через API**

POST-запрос инициируется непосредственно в Tencent Cloud, и определение — это идентификатор созданного шаблона анализа видео. Ниже приведен эталонный пример запроса:

```
{    "Url": "http://mps-pull.test.org/live/test.flv",    "TaskNotifyConfig": {        "NotifyType": "URL",        "NotifyUrl": "http://test.cloud.com/callback"    },    "OutputStorage": {        "Type": "COS",        "CosOutputStorage": {            "Bucket": "mg-aidata-1258344699",            "Region": "ap-guangzhou"        }    },    "OutputDir": "/output/",    "AiAnalysisTask": {        "Definition": 26,        "ExtendedParameter": "{\\"hht\\":{\\"top_clip\\":10, \\"force_cls\\":5003, \\"need_vad\\":1, \\"threshold\\":0.9, \\"merge_time\\":60, \\"merge_type\\":0, \\"res_save_type\\":1}}"    }}
```

### 2. Получение обратных вызовов

Обратитесь к [Parse Live Stream Processing Results](https://www.tencentcloud.com/document/product/1041/33680) для анализа полей AiAnalysisResultInfo.

### 3. Протокол завершения задачи

Обратитесь к [Task Management Documentation](https://www.tencentcloud.com/document/product/1041/37462) для управления инициированными задачами.

## Описание расширенных параметров

| Параметр | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| top_clip | Нет | int | Выберите выделенные клипы с наивысшими баллами доверия, значение по умолчанию — 5. Пример: `\\"top_clip\\":10` указывает на вывод до 10 выделенных клипов с наивысшими баллами доверия. |
| force_cls | Нет | int | Укажите категорию выделения ключевых моментов:5003: Variety/TV Series4001: Football4002: Basketball1001: Honor of Kings100101: Honor of Kings Competition1003: League of Legends |
| need_vad | Нет | int | VAD используется для определения конца предложения в видео. Расширение VAD позволяет полностью использовать видеоречь, включено по умолчанию.1: Использовать VAD0: Не использовать |
| threshold | Нет | float | Порог доверия. Клипы ниже порога отфильтровываются, и для каждого типа выделения ключевых моментов установлены настройки порога по умолчанию. Примечание: Рекомендуется не устанавливать этот параметр в первый раз. |
| res_save_type | Нет | int | Сохранять ли результаты, сохраняются по умолчанию.1: Сохранять результаты0: Выводить только временной период |
| output_pattern | Нет | string | Формат наименования выходного видео. {} указывает заполнитель.{year}-{month}-{day}-{hour}-{minute}-{second}_{start_dts}-{end_dts}-{timestamp}-{session}.mp4Формат вывода по умолчанию:hht-{year}{month}{day}{hour}{minute}-{session}-{timestamp}-index.mp4 |
| image_pattern | Нет | string | image-{start_dts}.jpgПараметры, которые можно использовать в качестве заполнителей, — те же, что и выше. Формат вывода по умолчанию:hht-{year}{month}{day}{hour}{minute}-{session}-{timestamp}-index.jpg |
| merge_type | Нет | int | **Примечание: Доступно только в автономных сценариях. Не объединять для значения по умолчанию 5003, и объединять в других сценариях.** Объединять ли результаты в одно видео:1: Объединять (параметр top_clip не вступает в силу)0: Не объединять (параметр merge_time не вступает в силу) |
| merge_time | Нет | int | **Примечание: Доступно только в автономных сценариях. Значение по умолчанию 5003 — это фактический вывод, а время не должно превышать один час в других сценариях.** Укажите длину выходного видео при объединении в одно видео. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/66043](https://www.tencentcloud.com/document/product/1041/66043)*

---
*Источник (EN): [intelligent-highlights-tutorial.md](./intelligent-highlights-tutorial.md)*

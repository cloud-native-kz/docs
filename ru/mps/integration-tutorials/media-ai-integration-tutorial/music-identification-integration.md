# Интеграция идентификации музыки

## Введение в функцию

Функция идентификации музыки использует передовые технологии Tencent Music для идентификации музыки и распознавания кавер-версий. На основе долгосрочных исследований в области искусственного интеллекта и больших данных техническая команда интегрирует архитектуру трансформера с алгоритмами аудио-отпечатков для построения многоуровневой сети функций. Эта сеть может преодолевать поверхностные различия и точно анализировать глубокие корреляции между различными интерпретациями и оригинальной песней с точки зрения певцов, аранжировок инструментов, темпа, тональности и даже музыкального стиля. Это обеспечивает ведущий в отрасли объем базы данных музыки и точность идентификации.

## Предварительные требования

Перед использованием этой функции необходимо выполнить следующие предварительные операции:

- Зарегистрируйтесь/Войдите в учетную запись Tencent Cloud, активируйте Media Processing Service (MPS) и завершите авторизацию роли сервиса**.**
- Если вы используете вспомогательную учетную запись Tencent Cloud, убедитесь, что учетная запись имеет достаточные разрешения для использования MPS.

Подробное руководство см. в разделе [Быстрый старт](https://www.tencentcloud.com/document/product/1041/33482). По вопросам авторизации учетной записи см. раздел [Авторизация учетной записи](https://www.tencentcloud.com/document/product/1041/69220).

## Инструкции по выставлению счетов

Функция идентификации музыки Tencent Cloud MPS использует режим выставления счетов на основе продолжительности входного файла. Полные инструкции по правилам выставления счетов см. в разделе [Интеллектуальная идентификация элементов атомарного выставления счетов - Идентификация музыки](https://www.tencentcloud.com/document/product/1041/49204#345449ad-2771-471e-b724-816a9358ebdc).

## Инициирование задачи идентификации музыки

### Способ 1: Использование API Explorer для быстрой проверки

1. Перейдите в [консоль MPS](https://console.tencentcloud.com/mps/index) для активации сервиса и убедитесь, что [авторизация COS](https://www.tencentcloud.com/en/document/product/1041/33482#.E6.AD.A5.E9.AA.A42.EF.BC.9A.E6.8E.88.E6.9D.83.E7.AE.A1.E7.90.86) завершена.
2. Перейдите на страницу [API Explorer](https://console.intl.cloud.tencent.com/api/explorer?Product=mps&Version=2019-06-12&Action=ProcessMedia) онлайн-отладки MPS и выберите API `ProcessMedia` из списка API в левой части. См. следующий рисунок для заполнения параметров, таких как входной путь, выходной путь и ID шаблона. Установите **Definition** в **21** (предустановленный шаблон идентификации музыки) в конфигурации AiAnalysisTask для инициирования указанной задачи идентификации музыки. **ExtendedParameter** - это расширенный параметр, и требуется заполнить {"tag":{"process_type":"1102"}}.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/b1dd34f3c37311f0aa02525400e889b2.png)

### Способ 2: Инициирование через API

Выше описано, как использовать API Explorer для вызова и отладки API в Интернете. Вы также можете отправить POST-запрос непосредственно в Tencent Cloud. Доменное имя запроса API - mps.tencentcloudapi.com. Инициируйте POST-запрос с definition в качестве ID предустановленного шаблона идентификации музыки (21). Пример ссылки на запрос выглядит следующим образом:

> **Примечание:** При прямом вызове API экранируйте строку JSON, когда указан ExtendedParameter.

```
{    "InputInfo": {        "Type": "URL",        "UrlInputInfo": {            "Url": "https://data-125xxxxxxx.cos.ap-guangzhou.tencentcos.cn/test/01-%E3%%%B7.mp4"        //Input file URL. Replace it with the available file URL during the actual call.        }    },    "OutputStorage": {        "Type": "COS",        "CosOutputStorage": {            "Bucket": "ie-mps-125xxxxxxx",            "Region": "ap-nanjing"        }    },    "OutputDir": "/common/test/tiger/",    "AiAnalysisTask": {        "Definition": 21,        "ExtendedParameter": "{\\"tag\\":{\\"process_type\\":\\"1102\\"}}"    },    "TaskNotifyConfig": {        "NotifyType": "URL",        "NotifyUrl": "http://xx.xx.xx.xx:5000//callback"    }}
```

## Просмотр результата обратного вызова

После успешного инициирования задачи вы можете получить информацию о песне из результата обратного вызова после идентификации музыки.

- Tag: название песни
- Структура SpecialInfo

| Имя поля | Тип | Описание |
| --- | --- | --- |
| song_name | string | Название песни |
| album_name | string | Название альбома |
| singer_name | string | Имя певца |
| other_singer_list | array | Список связанных певцов |
| reference_start | int | Приблизительная начальная временная точка песни |
| reference_end | int | Приблизительная конечная временная точка песни |
| segment_list | array | Период времени появления песни |

> **Примечание:** Когда TagSet в результате обратного вызова отображается как [], это указывает на то, что для аудиоклипа нет совпадающих песен. reference_start и reference_end предназначены только для справки. Конкретный диапазон времени определяется segment_list. Поскольку интервал обнаружения составляет 15 секунд, ошибка по сравнению с фактической продолжительностью музыки не превышает 15 секунд.

Конкретный пример результата возврата:

```
 "AiAnalysisResultSet": [        {            "ClassificationTask": null,            "CoverTask": null,            "DeLogoTask": null,            "DescriptionTask": null,            "FrameTagTask": null,            "HeadTailTask": null,            "HighlightTask": null,            "HorizontalToVerticalTask": null,            "SegmentTask": null,            "TagTask": {                "BeginProcessTime": "2025-06-13T12:08:20Z",                "ErrCode": 0,                "ErrCodeExt": "",                "FinishTime": "2025-06-13T12:08:57Z",                "Input": {                    "Definition": 283568                },                "Message": "SUCCESS",                "Output": {                    "TagSet": [                        {                            "Confidence": 100,                            "Tag": "An Array of Stars",                            "SpecialInfo": "{\\"song_mid\\": \\"000Quzkn4N0CBN\\", \\"song_id\\": 521340020, \\"reference_start\\": 30, \\"song_name\\": \\"An Array of Stars\\", \\"album_name\\": \\"An Array of Stars\\", \\"reference_end\\": 255, \\"singer_name\\": \\"TIA RAY\\", \\"segment_list\\": [[30, 165], [180, 255]], \\"other_singer_list\\": [{\\"singer_name\\": \\"Jam Hsiao\\"}]}"                        }                    ]                },                "Progress": 100,                "Status": "SUCCESS"            },            "Type": "Tag"        }    ]
```


---
*Источник: [https://www.tencentcloud.com/document/product/1041/74318](https://www.tencentcloud.com/document/product/1041/74318)*

---
*Источник (EN): [music-identification-integration.md](./music-identification-integration.md)*

# DescribeContentReviewTemplates

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для запроса шаблонов модерации контента по ID шаблона. Будут возвращены как пользовательские, так и предустановленные шаблоны, соответствующие переданным ID шаблонов.

Максимум 10 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

В следующем списке параметров запроса указаны только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: DescribeContentReviewTemplates. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definitions.N | Нет | Array of Integer | ID шаблонов модерации контента для запроса. Лимит длины массива: 50. |
| Offset | Нет | Integer | Смещение для разбивки на страницы. Значение по умолчанию: 0. |
| Limit | Нет | Integer | Количество возвращаемых записей. Значение по умолчанию: 10. Максимальное значение: 50. |
| Type | Нет | String | Фильтр для запроса шаблонов. Если этот параметр оставлен пустым, возвращаются как предустановленные, так и пользовательские шаблоны. Допустимые значения: * Preset * Custom |
| Name | Нет | String | Условие фильтра для идентификаторов шаблонов интеллектуального аудита с лимитом длины 64 символа. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TotalCount | Integer | Количество подходящих записей. |
| ContentReviewTemplateSet | Array of [ContentReviewTemplateItem](https://www.tencentcloud.com/document/api/1041/33690#ContentReviewTemplateItem) | Список деталей шаблонов аудита контента. |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Примеры

### Пример 1. Получение указанного количества шаблонов интеллектуального аудита

Этот пример показывает, как получить до 10 шаблонов интеллектуального аудита, включая стандартные, начиная с первой записи (offset = 0).

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=DescribeContentReviewTemplates
&Offset=0
&Limit=10
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "TotalCount": 2,
        "ContentReviewTemplateSet": [
            {
                "Definition": 30,
                "Name": "Template 1",
                "Type": "Preset",
                "Comment": "Intelligent content moderation template",
                "PornConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "porn"
                        ],
                        "BlockConfidence": 80,
                        "ReviewConfidence": 30
                    },
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    }
                },
                "TerrorismConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "bloody"
                        ],
                        "BlockConfidence": 80,
                        "ReviewConfidence": 30
                    },
                    "OcrReviewInfo": {
                        "Switch": "OFF",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "PoliticalConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "politician"
                        ],
                        "BlockConfidence": 80,
                        "ReviewConfidence": 30
                    },
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    }
                },
                "ProhibitedConfigure": null,
                "UserDefineConfigure": {
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [],
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [],
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    }
                },
                "CreateTime": "2019-01-01T12:00:00Z",
                "UpdateTime": "2019-01-01T16:00:00Z"
            },
            {
                "Definition": 31,
                "Name": "Template 2",
                "Type": "Preset",
                "Comment": "Content moderation template",
                "PornConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "OFF"
                    },
                    "AsrReviewInfo": {
                        "Switch": "OFF"
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    }
                },
                "TerrorismConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [],
                        "BlockConfidence": 80,
                        "ReviewConfidence": 30
                    },
                    "OcrReviewInfo": {
                        "Switch": "OFF",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "PoliticalConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "politician"
                        ],
                        "BlockConfidence": 80,
                        "ReviewConfidence": 30
                    },
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    }
                },
                "ProhibitedConfigure": null,
                "UserDefineConfigure": {
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [],
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [],
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    }
                },
                "CreateTime": "2019-01-01T12:00:00Z",
                "UpdateTime": "2019-01-01T16:00:00Z"
            }
        ],
        "RequestId": "19ae8d8e-dce3-4151-9d4b-5594384987a9"
    }
}
```

### Пример 2. Получение шаблона интеллектуального аудита с ID 30

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=DescribeContentReviewTemplates
&Definitions.0=30
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "TotalCount": 1,
        "ContentReviewTemplateSet": [
            {
                "Definition": 30,
                "Name": "Template 1",
                "Type": "Preset",
                "Comment": "Intelligent content moderation template",
                "PornConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "porn"
                        ],
                        "BlockConfidence": 80,
                        "ReviewConfidence": 30
                    },
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    }
                },
                "TerrorismConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "bloody"
                        ],
                        "BlockConfidence": 80,
                        "ReviewConfidence": 30
                    },
                    "OcrReviewInfo": {
                        "Switch": "OFF",
                        "BlockConfidence": 0,
                        "ReviewConfidence": 0
                    }
                },
                "PoliticalConfigure": {
                    "ImgReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [
                            "politician"
                        ],
                        "BlockConfidence": 80,
                        "ReviewConfidence": 30
                    },
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    }
                },
                "ProhibitedConfigure": null,
                "UserDefineConfigure": {
                    "AsrReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [],
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    },
                    "OcrReviewInfo": {
                        "Switch": "ON",
                        "LabelSet": [],
                        "BlockConfidence": 100,
                        "ReviewConfidence": 75
                    }
                },
                "CreateTime": "2019-01-01T12:00:00Z",
                "UpdateTime": "2019-01-01T16:00:00Z"
            }
        ],
        "RequestId": "19ae8d8e-dce3-4151-9d4b-5594384987a9"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы облегчить вам вызов API.

Tencent Cloud SDK 3.0 for Python
Tencent Cloud SDK 3.0 for Java
Tencent Cloud SDK 3.0 for PHP
Tencent Cloud SDK 3.0 for Go
Tencent Cloud SDK 3.0 for Node.js
Tencent Cloud SDK 3.0 for .NET
Tencent Cloud SDK 3.0 for C++

### Интерфейс командной строки

Tencent Cloud CLI 3.0

## 6. Коды ошибок

Далее приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Операция не удалась: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameterValue.Definitions | Ошибка параметра: Definitions. |
| InvalidParameterValue.Limit | Ошибка параметра: Limit. |
| ResourceNotFound.TemplateNotExist | Ресурс не существует: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33659](https://www.tencentcloud.com/document/product/1041/33659)*

---
*Источник (EN): [describecontentreviewtemplates.md](./describecontentreviewtemplates.md)*

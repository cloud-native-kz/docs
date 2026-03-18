# ProcessImage

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для инициирования обработки изображений со следующими возможностями:

Преобразование формата.
Улучшение изображения.
Удаление элементов из изображения.

Максимально 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: ProcessImage. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| InputInfo | Да | [MediaInputInfo](https://www.tencentcloud.com/document/api/1041/33690#MediaInputInfo) | Информация о входном файле для обработки изображения. |
| OutputStorage | Нет | [TaskOutputStorage](https://www.tencentcloud.com/document/api/1041/33690#TaskOutputStorage) | Целевое хранилище для выходных файлов обработки изображения. Если оставить пусто, наследует местоположение хранилища из InputInfo. |
| OutputDir | Нет | String | Выходной путь файла для обработки изображения. Если оставить пусто, это каталог файла в InputInfo. Если это каталог, например `/image/201907/`, это означает наследование исходного имени файла и вывод в этот каталог. |
| OutputPath | Нет | String | Выходной путь, который может быть относительным или абсолютным путем. Путь должен заканчиваться на `.{format}`. Для подробной информации см. [Переменная имени файла](https://www.tencentcloud.com/document/product/1041/33495). **Пример относительного пути:** `Filename_{Variablename}.{format}`. `Filename.{format}`.  **Пример абсолютного пути:** `/Path/Filename_{Variablename}.{format}`.  Если не заполнено, относительный путь по умолчанию: `{inputName}.{format}`. |
| Definition | Нет | Integer | Уникальный идентификатор шаблона обработки изображения. Функция шаблона изображения находится на этапе бета-тестирования. Если вы хотите использовать её, подайте заявку на получение доступа. |
| ResourceId | Нет | String | ID ресурса. Убедитесь, что соответствующий ресурс включен. Значение по умолчанию — основной ID ресурса учетной записи. |
| ImageTask | Нет | [ImageTaskInput](https://www.tencentcloud.com/document/api/1041/33690#ImageTaskInput) | Параметры обработки изображения. |
| StdExtInfo | Нет | String | Расширенные параметры для обработки изображения. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | ID задачи. |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Примеры

### Example1 Инициирование улучшения изображения

Этот пример показывает, как инициировать улучшение изображения.

#### Пример ввода

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ProcessImage
<Common request parameters>

{
    "InputInfo": {
        "Type": "COS",
        "CosInputInfo": {
            "Bucket": "bucket-test",
            "Region": "ap-shanghai",
            "Object": "/image/test.png"
        }
    },
    "OutputStorage": {
        "Type": "COS",
        "CosOutputStorage": {
            "Bucket": "bucket-test",
            "Region": "ap-shanghai"
        }
    },
    "ImageTask": {
        "EncodeConfig": {
            "Format": "jpeg",
            "Quality": 75
        },
        "EnhanceConfig": {
            "SuperResolution": {
                "Switch": "ON"
            }
        }
    }
}
```

#### Пример вывода

```json
{
    "Response": {
        "RequestId": "03b25aab-8883-497e-838f-d760c3e220f6",
        "TaskId": "3pg2p4jEfbFHYo2rgB0Kzl0esg4NeBItcZyllxO4HNJXdNeRUhk9GjDMjCj1auPv"
    }
}
```

### Example2 Инициирование удаления элементов из изображения

Этот пример показывает, как инициировать удаление элементов из изображения.

#### Пример ввода

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ProcessImage
<Common request parameters>

{
    "InputInfo": {
        "Type": "COS",
        "CosInputInfo": {
            "Bucket": "bucket-test",
            "Region": "ap-shanghai",
            "Object": "/image/test.png"
        }
    },
    "OutputStorage": {
        "Type": "COS",
        "CosOutputStorage": {
            "Bucket": "bucket-test",
            "Region": "ap-shanghai"
        }
    },
    "ImageTask": {
        "EncodeConfig": {
            "Format": "jpeg",
            "Quality": 75
        },
        "EraseConfig": {
            "ImageEraseLogo": {
                "Switch": "ON",
                "ImageAreaBoxes": [
                    {
                        "Type": "logo",
                        "AreaCoordSet": [
                            101,
                            85,
                            111,
                            95
                        ]
                    }
                ]
            }
        }
    }
}
```

#### Пример вывода

```json
{
    "Response": {
        "RequestId": "03b25aab-8883-497e-838f-d760c3e220f6",
        "TaskId": "3pg2p4jEfbFHYo2rgB0Kzl0esg4NeBItcZyllxO4HNJXdNeRUhk9GjDMjCj1auPv"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы упростить вызов API.

Tencent Cloud SDK 3.0 для Python
Tencent Cloud SDK 3.0 для Java
Tencent Cloud SDK 3.0 для PHP
Tencent Cloud SDK 3.0 для Go
Tencent Cloud SDK 3.0 для Node.js
Tencent Cloud SDK 3.0 для .NET
Tencent Cloud SDK 3.0 для C++

### Интерфейс командной строки

Tencent Cloud CLI 3.0

## 6. Коды ошибок

Далее приведены только коды ошибок, связанные с деловой логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Операция не выполнена: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameterValue.SessionContextTooLong | `SessionContext` слишком длинный. |
| InvalidParameterValue.SessionId | ID дедупликации уже существует. Запрос удален из-за дублирования. |
| InvalidParameterValue.SessionIdTooLong | `SessionId` слишком длинный. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/66929](https://www.tencentcloud.com/document/product/1041/66929)*

---
*Источник (EN): [processimage.md](./processimage.md)*

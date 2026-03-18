# CreateSchedule

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для установки правил обработки загруженных медиафайлов в указанной директории Bucket в COS, включая:
- Этот API используется для транскодирования видео с водяными знаками.
- Этот API используется для создания анимированных изображений.
- Этот API используется для создания снимков экрана в указанные моменты времени.
- Этот API используется для создания выборочных снимков экрана из видео.
- Этот API используется для создания спрайт-снимков видео.
- Этот API используется для транскодирования в адаптивное потоковое вещание.
- Этот API используется для интеллектуальной модерации контента, включая обнаружение порнографии и конфиденциальной информации.
- Этот API используется для интеллектуального анализа контента (теги, категория, обложка, маркировка кадров).
- Этот API используется для интеллектуального распознавания контента (человеческие лица, полный текст, текстовые ключевые слова, полная речь, ключевые слова речи).

Проверка качества медиа (диагностика формата потокового вещания, обнаружение содержимого аудио и видео (дрожание, размытость, низкое освещение, переэкспозиция, чёрно-белые края, чёрно-белые экраны, глюки экрана, шум, мозаика, QR-код и другое), оценка без эталона).

Интеллектуальные субтитры (полная речь, горячие слова речи и перевод речи).

Этот API используется для интеллектуального стирания (удаление водяных знаков, удаление субтитров, защита приватности).

Этот API используется для создания оркестровки, которая по умолчанию находится в отключённом состоянии и требует ручного включения.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Приведённый ниже список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Для полного списка общих параметров см. [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: CreateSchedule. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| ScheduleName | Да | String | Имя схемы (макс. 128 символов). Это имя должно быть уникальным в рамках вашего аккаунта. |
| Trigger | Да | [WorkflowTrigger](https://www.tencentcloud.com/document/api/1041/33690#WorkflowTrigger) | Триггер схемы. Если файл загружен в указанный bucket, схема будет активирована. |
| Activities.N | Да | Array of [Activity](https://www.tencentcloud.com/document/api/1041/33690#Activity) | Подзадачи схемы. |
| OutputStorage | Нет | [TaskOutputStorage](https://www.tencentcloud.com/document/api/1041/33690#TaskOutputStorage) | Bucket для сохранения выходного файла. Если вы не указываете этот параметр, будет использован bucket из `Trigger`. |
| OutputDir | Нет | String | Директория для сохранения выходного медиафайла, которая должна начинаться и заканчиваться на `/`, например `/movie/201907/`. |
| TaskNotifyConfig | Нет | [TaskNotifyConfig](https://www.tencentcloud.com/document/api/1041/33690#TaskNotifyConfig) | Конфигурация уведомления. Если вы не указываете этот параметр, уведомления не будут отправлены. |
| ResourceId | Нет | String | ID ресурса. Убедитесь, что соответствующий ресурс включен. Значение по умолчанию — основной ID ресурса аккаунта. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| ScheduleId | Integer | ID схемы. |
| RequestId | String | Уникальный ID запроса, сгенерированный сервером, будет возвращён для каждого запроса (если запрос не достигнет сервера по другим причинам, RequestId не будет получен). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1. Конфигурирование правила транскодирования

Этот пример показывает, как создать схему для bucket'а "evan-test-1300828900". Она будет активирована при загрузке файла MP4 или FLV в директорию `/input/` bucket'а. После активации будет выполнена задача транскодирования (ID шаблона 10) несколько раз.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateSchedule
<Common request parameters>

{
    "ScheduleName": "evan_test7",
    "Trigger": {
        "Type": "CosFileUpload",
        "CosFileUploadTrigger": {
            "Bucket": "evan-test-1300828900",
            "Region": "ap-guangzhou",
            "Dir": "/input/",
            "Formats": [
                "mp4",
                "flv"
            ]
        }
    },
    "Activities": [
        {
            "ActivityType": "input",
            "ReardriveIndex": [
                1,
                2
            ]
        },
        {
            "ActivityType": "action-trans",
            "ReardriveIndex": [
                3
            ],
            "ActivityPara": {
                "TranscodeTask": {
                    "Definition": 10
                }
            }
        },
        {
            "ActivityType": "action-trans",
            "ReardriveIndex": [
                6,
                7
            ],
            "ActivityPara": {
                "TranscodeTask": {
                    "Definition": 10
                }
            }
        },
        {
            "ActivityType": "action-trans",
            "ReardriveIndex": [
                4,
                5
            ],
            "ActivityPara": {
                "TranscodeTask": {
                    "Definition": 10
                }
            }
        },
        {
            "ActivityType": "action-trans",
            "ReardriveIndex": [
                10
            ],
            "ActivityPara": {
                "TranscodeTask": {
                    "Definition": 10
                }
            }
        },
        {
            "ActivityType": "action-trans",
            "ReardriveIndex": [
                10
            ],
            "ActivityPara": {
                "TranscodeTask": {
                    "Definition": 10
                }
            }
        },
        {
            "ActivityType": "action-trans",
            "ReardriveIndex": [
                10
            ],
            "ActivityPara": {
                "TranscodeTask": {
                    "Definition": 10
                }
            }
        },
        {
            "ActivityType": "action-trans",
            "ReardriveIndex": [
                8
            ],
            "ActivityPara": {
                "TranscodeTask": {
                    "Definition": 10
                }
            }
        },
        {
            "ActivityType": "action-trans",
            "ReardriveIndex": [
                9
            ],
            "ActivityPara": {
                "TranscodeTask": {
                    "Definition": 10
                }
            }
        },
        {
            "ActivityType": "action-trans",
            "ReardriveIndex": [
                10
            ],
            "ActivityPara": {
                "TranscodeTask": {
                    "Definition": 10
                }
            }
        },
        {
            "ActivityType": "output",
            "ActivityPara": {}
        }
    ],
    "OutputStorage": {
        "Type": "COS",
        "CosOutputStorage": {
            "Bucket": "evan-test-1300828900",
            "Region": "ap-nanjing"
        }
    },
    "OutputDir": "output/"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "ScheduleId": 157482
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы упростить вам вызов API.

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.CosStatusInavlid | Операция не удалась: служба COS приостановлена. |
| FailedOperation.GenerateResource | Ошибка создания ресурса. |
| FailedOperation.InvalidMpsUser | Операция не удалась: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InternalError.AccessDBError | Ошибка данных. |
| InternalError.GenDefinition | Внутренняя ошибка: ошибка при создании ID шаблона. |
| InvalidParameterValue | Неправильное значение параметра. |
| LimitExceeded.TooMuchTemplate | Ограничение достигнуто: количество шаблонов превышает лимит. |
| ResourceNotFound.CosBucketNameInvalid | Ресурс не найден: неправильное имя bucket'а COS. |
| ResourceNotFound.CosBucketNotExist | Ресурс не найден: bucket COS не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/54035](https://www.tencentcloud.com/document/product/1041/54035)*

---
*Источник (EN): [createschedule.md](./createschedule.md)*

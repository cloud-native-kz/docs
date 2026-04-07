# CreateCommonMixStream

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для создания общего потока микширования. Его можно использовать практически так же, как устаревший API `mix_streamv2.start_mix_stream_advanced`.
Примечание: в настоящее время можно смешивать до 16 потоков.
Лучшие практики: https://intl.cloud.tencent.com/document/product/267/45566?from_cn_redirect=1

Максимум 200 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: CreateCommonMixStream. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| MixStreamSessionId | Да | String | ID сеанса микширования потока (от подачи заявки на микширование потока до его отмены). Этот параметр может содержать до 80 байт букв, цифр и подчеркиваний. |
| InputStreamList.N | Да | Array of [CommonMixInputParam](https://www.tencentcloud.com/document/api/267/30767#CommonMixInputParam) | Список входных потоков для микширования потока. |
| OutputParams | Да | [CommonMixOutputParams](https://www.tencentcloud.com/document/api/267/30767#CommonMixOutputParams) | Параметр выходного потока для микширования потока. |
| MixStreamTemplateId | Нет | Integer | ID входного шаблона. Если этот параметр установлен, выходные данные будут сгенерированы согласно макету шаблона по умолчанию, и нет необходимости вводить пользовательские параметры позиции. |
| ControlParams | Нет | [CommonMixControlParams](https://www.tencentcloud.com/document/api/267/30767#CommonMixControlParams) | Специальный параметр управления для микширования потока. Если нет особых требований, оставьте пусто. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1. Подача заявки на микширование потока — использование шаблона 40

В этом примере показано, как использовать предустановленный шаблон микширования потока для смешивания потоков.

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateCommonMixStream
<Common request parameters>

{
    "MixStreamTemplateId": 40,
    "MixStreamSessionId": "test_room",
    "InputStreamList": [
        {
            "LayoutParams": {
                "ImageLayer": 1
            },
            "InputStreamName": "test_stream1"
        },
        {
            "LayoutParams": {
                "ImageLayer": 2
            },
            "InputStreamName": "test_stream2"
        }
    ],
    "OutputParams": {
        "OutputStreamName": "test_stream1"
    }
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

### Пример 2. Подача заявки на микширование потока — использование пользовательских параметров макета

В этом примере показано, как использовать пользовательский макет.

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateCommonMixStream
<Common request parameters>

{
    "InputStreamList": [
        {
            "LayoutParams": {
                "ImageLayer": 1,
                "ImageHeight": 720,
                "ImageWidth": 1280
            },
            "InputStreamName": "test_stream1"
        },
        {
            "LayoutParams": {
                "ImageLayer": 2,
                "ImageHeight": 320,
                "ImageWidth": 240,
                "LocationX": 100,
                "LocationY": 100
            },
            "InputStreamName": "test_stream2"
        }
    ],
    "OutputParams": {
        "OutputStreamName": "test_stream1"
    },
    "MixStreamSessionId": "test_room"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

### Пример 3. Подача заявки на микширование потока — использование параметров обрезки

В этом примере показано, как использовать параметры обрезки.

#### Пример входных данных

```
POST / HTTP/1.1
Host: live.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: CreateCommonMixStream
<Common request parameters>

{
    "InputStreamList": [
        {
            "LayoutParams": {
                "ImageLayer": 1,
                "ImageHeight": 720,
                "ImageWidth": 1280
            },
            "InputStreamName": "test_stream1"
        },
        {
            "LayoutParams": {
                "ImageLayer": 2,
                "ImageHeight": 320,
                "ImageWidth": 240,
                "LocationX": 100,
                "LocationY": 100
            },
            "InputStreamName": "test_stream2",
            "CropParams": {
                "CropWidth": 240,
                "CropHeight": 320,
                "CropStartLocationX": 100,
                "CropStartLocationY": 100
            }
        }
    ],
    "OutputParams": {
        "OutputStreamName": "test_stream1"
    },
    "MixStreamSessionId": "test_room"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы облегчить вызов API.

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

Здесь указаны только коды ошибок, связанные с бизнес-логикой API. Другие коды ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| FailedOperation.CallOtherSvrError | Ошибка при вызове стороннего сервиса. |
| FailedOperation.CallOtherSvrFailed | Ошибка при вызове внутреннего сервиса. |
| FailedOperation.CancelSessionNotExist | Отменяемый сеанс микширования потока не существует. |
| FailedOperation.GetPictureUrlError | Невозможно получить URL водяного знака. |
| FailedOperation.GetStreamResolutionError | Ошибка при получении длины и ширины входного потока. |
| FailedOperation.ProcessMixError | Ошибка при запуске микширования потока. |
| FailedOperation.StreamNotExist | Поток не существует. |
| InternalError | Внутренняя ошибка. |
| InternalError.JiFeiOtherError | Платежная платформа вернула другие ошибки. |
| InvalidParameter | Неверный параметр. |
| InvalidParameter.CancelSessionNotExist | Отменяемый сеанс не существует. |
| InvalidParameter.InputNumLimitExceeded | Количество входов превышает лимит. |
| InvalidParameter.InvalidBackgroudResolution | Неверная длина и ширина фона. |
| InvalidParameter.InvalidBitrate | Неверный выходной битрейт. |
| InvalidParameter.InvalidCropParam | Обрезаемая область выходит за границы исходного изображения. |
| InvalidParameter.InvalidLayerParam | Неверный параметр слоя. |
| InvalidParameter.InvalidOutputStreamID | ID выходного потока уже используется. |
| InvalidParameter.InvalidOutputType | Неверный тип вывода. Проверьте совпадение `OutputPram-StreamId` и `OutputType`. |
| InvalidParameter.InvalidPictureID | ID водяного знака не установлен. |
| InvalidParameter.InvalidRoundRectRadius | Неверный радиус скругления прямоугольника. |
| InvalidParameter.OtherError | Другие ошибки. |
| InvalidParameter.SessionOutputStreamChanged | Выходной поток одного и того же сеанса изменился. |
| InvalidParameter.TemplateNotMatchInputNum | Шаблон не соответствует количеству входных потоков. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.StopService | Сервис приостановлен из-за задолженности по счету. Пополните счет до положительного баланса, чтобы активировать сервис. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/35997](https://www.tencentcloud.com/document/product/267/35997)*

---
*Источник (EN): [createcommonmixstream.md](./createcommonmixstream.md)*

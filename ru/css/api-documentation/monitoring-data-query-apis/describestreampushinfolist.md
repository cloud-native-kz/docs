# DescribeStreamPushInfoList

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для получения данных трансляции потока, включая частоту кадров аудио/видео, битрейт, прошедшее время и кодек.

Максимум 40 запросов можно инициировать в секунду для этого API.

Рекомендуется использовать API Explorer

Попробовать

API Explorer предоставляет диапазон возможностей, включая онлайн-вызовы, проверку подписи, генерацию кода SDK и быстрый поиск API. Он позволяет вам просматривать запросы, ответы и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DescribeStreamPushInfoList. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| StreamName | Да | String | Имя потока. |
| StartTime | Да | String | Время начала запроса, поддерживает запрос данных за последние семь дней, интервал между временем начала и временем окончания не может превышать три часа. Запрос интерфейса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат времени ISO, подробнее см. [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: при использовании этого формата по умолчанию обозначает время по Пекину. |
| EndTime | Да | String | Время окончания запроса, поддерживает запрос данных за последние семь дней, интервал между временем начала и временем окончания не может превышать три часа. Запрос интерфейса поддерживает два формата времени: 1) YYYY-MM-DDThh:mm:ssZ: формат времени ISO, подробнее см. [Описание формата даты ISO](https://intl.cloud.tencent.com/document/product/267/32941) 2) YYYY-MM-DD hh:mm:ss: при использовании этого формата по умолчанию обозначает время по Пекину. |
| PushDomain | Нет | String | Домен трансляции. |
| AppName | Нет | String | Путь трансляции, который должен совпадать с `AppName` в URL трансляции и воспроизведения. Значение по умолчанию — `live`. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| DataInfoList | Array of [PushQualityData](https://www.tencentcloud.com/document/api/267/30767#PushQualityData) | Возвращаемый список данных. |
| RequestId | String | Уникальный идентификатор запроса, возвращаемый для каждого запроса. RequestId требуется для определения проблемы. |

## 4. Пример

### Пример 1. Пример запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DescribeStreamPushInfoList
&StartTime=2019-06-21 12:00:00
&EndTime=2019-06-21 12:01:02
&StreamName=abcd
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "DataInfoList": [
            {
                "StreamParam": "xx",
                "ACodec": "AAC",
                "AppName": "live",
                "AudioFps": 43,
                "AudioRate": 131580,
                "AudioTs": 5004,
                "BeginPushTime": "2019-06-21 00:29:12.252",
                "ClientIp": "125.39.132.102",
                "LocalTs": 5000,
                "PushDomain": "123.livepush.myqcloud.com",
                "Resolution": "368*640",
                "Sequence": "10151483429474411508",
                "Time": "2019-06-21 01:10:39.87",
                "VCodec": "H264",
                "VideoFps": 24,
                "VideoRate": 701528,
                "VideoTs": 5032,
                "MateFps": 30,
                "MetaAudioRate": 22,
                "MetaVideoRate": 4885,
                "Bandwidth": 1.0,
                "Flux": 1.0
            }
        ],
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

## 5. Ресурсы разработчика

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, для упрощения вызова API.

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

Ниже приводится только перечень кодов ошибок, связанных с бизнес-логикой API. Другие коды ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не выполнена. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба была приостановлена из-за задолженности по счету. Пополните счет до положительного баланса, чтобы активировать службу. |
| ResourceNotFound.UserDisableService | Вы отключили службу. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/36094](https://www.tencentcloud.com/document/product/267/36094)*

---
*Источник (EN): [describestreampushinfolist.md](./describestreampushinfolist.md)*

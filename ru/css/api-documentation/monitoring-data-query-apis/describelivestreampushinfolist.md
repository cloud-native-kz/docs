# DescribeLiveStreamPushInfoList

## 1. Описание API

Доменное имя для запроса API: live.intl.tencentcloudapi.com.

Этот API используется для запроса информации о передаче всех потоков в реальном времени, включая IP-адрес клиента, IP-адрес сервера, частоту кадров, битрейт, доменное имя и время начала передачи.

Максимум 500 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: DescribeLiveStreamPushInfoList. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Значение, используемое для этого API: 2018-08-01. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| PushDomain | Нет | String | Доменное имя передачи. |
| AppName | Нет | String | Путь передачи, который совпадает с `AppName` в адресах передачи и воспроизведения и по умолчанию имеет значение `live`. |
| PageNum | Нет | Integer | Номер страницы. Диапазон значений: [1,10000]. Значение по умолчанию: 1. |
| PageSize | Нет | Integer | Количество записей на странице. Диапазон значений: [1,1000]. Значение по умолчанию: 200. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| DataInfoList | Array of [PushDataInfo](https://www.tencentcloud.com/document/api/267/30767#PushDataInfo) | Список статистики потока трансляции. |
| TotalNum | Integer | Общее количество потоков трансляции. |
| TotalPage | Integer | Общее количество страниц. |
| PageNum | Integer | Номер страницы, где находятся текущие данные. |
| PageSize | Integer | Количество потоков трансляции на странице. |
| RequestId | String | Уникальный ID запроса, который возвращается для каждого запроса. RequestId требуется для определения местоположения проблемы. |

## 4. Примеры

### Пример 1 Образец запроса

#### Пример входных данных

```
https://live.intl.tencentcloudapi.com/?Action=DescribeLiveStreamPushInfoList
&PushDomain=5000.pushdomain.com
&AppName=live
&PageNum=1
&PageSize=1000
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "DataInfoList": [
            {
                "StreamName": "test1",
                "AppName": "live",
                "ClientIp": "127.0.0.1",
                "ServerIp": "127.0.0.1",
                "VideoFps": 100,
                "VideoSpeed": 100,
                "AudioFps": 40,
                "AudioSpeed": 40,
                "AsampleRate": 48000,
                "PushDomain": "5000.pushdomain.com",
                "BeginPushTime": "2019-02-01 00:00:00",
                "Acodec": "AAC",
                "Vcodec": "H264",
                "Resolution": "350*350",
                "MetaAudioSpeed": 22,
                "MetaFps": 30,
                "MetaVideoSpeed": 4885
            }
        ],
        "PageNum": 1,
        "PageSize": 1000,
        "TotalNum": 1,
        "TotalPage": 1,
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что облегчает вызов API.

SDK Tencent Cloud 3.0 для Python
SDK Tencent Cloud 3.0 для Java
SDK Tencent Cloud 3.0 для PHP
SDK Tencent Cloud 3.0 для Go
SDK Tencent Cloud 3.0 для Node.js
SDK Tencent Cloud 3.0 для .NET
SDK Tencent Cloud 3.0 для C++

### Интерфейс командной строки

Tencent Cloud CLI 3.0

## 6. Коды ошибок

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.HasNotLivingStream | Нет потока трансляции. |
| FailedOperation.QueryUploadInfoFailed | Ошибка при запросе информации о загрузке. |
| InternalError | Внутренняя ошибка. |
| InternalError.InvalidRequest | Неправильный запрос. |
| InternalError.QueryProIspPlayInfoError | Ошибка при запросе информации о воспроизведении по поставщику услуг и округу. |
| InternalError.QueryUploadInfoFailed | Ошибка при запросе информации о загрузке. |
| InvalidParameterValue | Неверное значение параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Служба приостановлена. |
| ResourceNotFound.StopService | Служба была приостановлена из-за задолженности по счету. Пополните счет до положительного баланса, чтобы активировать услугу. |
| ResourceNotFound.UserDisableService | Вы отключили услугу. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/37303](https://www.tencentcloud.com/document/product/267/37303)*

---
*Источник (EN): [describelivestreampushinfolist.md](./describelivestreampushinfolist.md)*

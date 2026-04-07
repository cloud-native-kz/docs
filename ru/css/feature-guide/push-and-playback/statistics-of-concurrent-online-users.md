# Статистика одновременно активных пользователей онлайн

Существует два метода подсчета одновременно активных пользователей онлайн. В зависимости от различных протоколов воспроизведения выберите подходящий метод статистики:

## Метод первый: протокол воспроизведения — RTMP или FLV

Если протокол воспроизведения — RTMP или FLV, количество одновременных соединений равно количеству активных пользователей. Вы можете просмотреть количество активных пользователей непосредственно через консоль. Для конкретных операций см. [справочное руководство](https://www.tencentcloud.com/document/product/267/31078). Вы также можете [получить количество активных зрителей](https://www.tencentcloud.com/document/product/267/37297), вызвав метод DescribeStreamPlayInfoList API 3.0 Cloud Streaming Services (CSS).

## Метод второй: протокол воспроизведения — HLS

Если протокол воспроизведения — HLS, статистика количества одновременных пользователей будет неточной, если опираться только на облачные данные, поскольку протокол имеет атрибут непостоянного соединения. Необходимо, чтобы URL запроса воспроизведения на стороне пользователя содержал строку UUID, и статистика должна быть включена в облаке. Ниже приводится описание практического решения для подсчета одновременных пользователей при использовании протокола воспроизведения HLS.

### Со стороны пользователя

Это решение реализовано на основе UUID, который генерируется сервером приложений клиента и добавляется в качестве параметра запроса в конец адреса URL воспроизведения. UUID каждого пользователя уникален.

**Пример URL воспроизведения:**

`http(s)://${your_domain_name}/${path}/${to}/${stream}/${playlist_name}.m3u8?uuid=c44ada05-3431-442f-9233-cb245d3624c8`

**или**

`http(s)://${your_domain_name}/${app_name}/${stream_name}.m3u8?uuid=2c2b59d0-e0c7-4877-9823-e4965d92f7bf`

### Поддержка облака

Вы можете [отправить тикет](https://console.tencentcloud.com/workorder) для получения поддержки статистики одновременных пользователей для HLS на основе UUID.

#### Описание API

Доменное имя запроса API: `live.tencentcloudapi.com.`

Этот API используется для запроса статистики одновременно активных пользователей онлайн для HLS, включая количество обращений, количество активных пользователей и трафик.

#### Входные параметры

Следующий список параметров запроса включает только параметры запроса API и некоторые общие параметры запроса. Полный список общих параметров запроса см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/267/30763).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общий параметр](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API — DescribeHLSConcurrentUserInfo. |
| Version | Да | String | [Общий параметр](https://www.tencentcloud.com/document/api/267/30763). Значение для этого API — 2018-08-01. |
| Region | Нет | String | [Общий параметр](https://www.tencentcloud.com/document/api/267/30763). Этот параметр не требуется для этого API. |
| StartTime | Да | String | UTC время начала в формате yyyy-mm-ddTHH:MM:SSZ. Дополнительные сведения см. в разделе [Формат даты ISO](https://www.tencentcloud.com/document/product/267/32941).Например, время UTC+8 2019-01-08 10:00:00 соответствует UTC времени 2019-01-08T10:00:00+08:00.Поддерживает запросы за прошлый месяц.Пример значения: 2006-01-02T15:04:05Z. |
| EndTime | Да | String | UTC время завершения в формате yyyy-mm-ddTHH:MM:SSZ. Дополнительные сведения см. в разделе [Формат даты ISO](https://www.tencentcloud.com/document/product/267/32941).Например, время UTC+8 2019-01-08 10:00:00 соответствует UTC времени 2019-01-08T10:00:00+08:00.Поддерживает запросы за прошлый месяц, промежуток времени между временем начала и временем завершения не превышает шести часов.Пример значения: 2006-01-02T15:04:05Z. |
| PlayDomains.N | Нет | Array of String | Список доменных имен воспроизведения. Если пусто, по умолчанию запрашиваются все доменные имена.Пример значения: testplay.com. |
| StreamNames.N | Нет | Array of String | Список имен потоков. Если пусто, по умолчанию проверяются все потоки.Запрашивает имя потока в модели публикации. Значение поля StreamName (streamid — это ID потока в модели публикации):hls:Multi-bitrate: streamid_sub-bitrate template name.Single-bitrate transcoding: streamid_template name.No transcoding: streamid.dash:Single-bitrate transcoding: streamid_template name.No transcoding: streamid.Пример значения: test |

#### Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| DataInfoList | Array of HLSConcurrentUserInfo | Статистика одновременных пользователей для потокового вещания HLS. |
| RequestId | String | Уникальный идентификатор запроса. Он генерируется сервером и возвращается для каждого запроса. (Если запрос не получен сервером по какой-либо причине, RequestId не возвращается.) RequestId требуется для определения проблемы. |

### Пример

#### Пример входных данных

Этот API показывает, как запросить статистику количества одновременно активных пользователей онлайн для HLS.

```
POST / HTTP/1.1Host: live.tencentcloudapi.comContent-Type: application/jsonX-TC-Action: DescribeHLSConcurrentUserInfo<Common request parameters>{"StartTime": "2022-10-12T14:00:00+08:00",    "EndTime": "2022-10-12T15:10:00+08:00"}
```

#### Пример выходных данных

```
{    "Response": {        "DataInfoList": [            {                "Flux": 2893,                "OnlineNums": 1,                "RequestCount": 11,                "Bandwidth": 123,                "Time": "2022-10-12T14:35:00+08:00"            }        ],        "RequestId": "b725570a-c1f1-4df7-b864-5ec3a9326cc0"    }}
```

## Ресурсы разработчика

### SDK

TencentCloud API 3.0 предоставляет поддерживающий комплект разработки программного обеспечения (SDK), который поддерживает несколько языков программирования, что упрощает вызов API.

- [Tencent Cloud SDK 3.0 для Python](https://github.com/TencentCloud/tencentcloud-sdk-python-intl-en/blob/master/tencentcloud/live/v20180801/live_client.py)
- [Tencent Cloud SDK 3.0 для Java](https://github.com/TencentCloud/tencentcloud-sdk-java-intl-en/blob/master/src/main/java/com/tencentcloudapi/live/v20180801/LiveClient.java)
- [Tencent Cloud SDK 3.0 для PHP](https://github.com/TencentCloud/tencentcloud-sdk-php-intl-en/blob/master/src/TencentCloud/Live/V20180801/LiveClient.php)
- [Tencent Cloud SDK 3.0 для Go](https://github.com/TencentCloud/tencentcloud-sdk-go-intl-en/blob/master/tencentcloud/live/v20180801/client.go)
- [Tencent Cloud SDK 3.0 для Node.js](https://github.com/TencentCloud/tencentcloud-sdk-nodejs-intl-en/blob/master/tencentcloud/live/v20180801/live_client.js)
- [Tencent Cloud SDK 3.0 для .NET](https://github.com/TencentCloud/tencentcloud-sdk-dotnet-intl-en/blob/master/TencentCloud/Live/V20180801/LiveClient.cs)
- [Tencent Cloud SDK 3.0 для C++](https://github.com/TencentCloud/tencentcloud-sdk-cpp-intl-en/blob/master/live/src/v20180801/LiveClient.cpp)

### Интерфейс командной строки

[Tencent Cloud CLI 3.0](https://www.tencentcloud.com/document/product/1013)

## Код ошибки

Ниже приведены коды ошибок, связанные с логикой бизнеса API. Для других кодов ошибок см. раздел [Общий код ошибки](https://www.tencentcloud.com/document/api/267/30851#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation | Операция не удалась. |
| FailedOperation.NotFound | Не удалось найти записи. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| ResourceNotFound.ForbidService | Пользователь отключен. |
| ResourceNotFound.FreezeService | Служба пользователя заморожена. |
| ResourceNotFound.StopService | Учетная запись приостановлена. Пожалуйста, активируйте службу после пополнения счета до положительного баланса, а затем выполните операции. |
| ResourceNotFound.UserDisableService | Пользователь самостоятельно отменил учетную запись. |


---
*Источник: [https://www.tencentcloud.com/document/product/267/70461](https://www.tencentcloud.com/document/product/267/70461)*

---
*Источник (EN): [statistics-of-concurrent-online-users.md](./statistics-of-concurrent-online-users.md)*

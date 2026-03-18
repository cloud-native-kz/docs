# UpdatePublishCdnStream

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

Этот API используется для изменения параметров задачи трансляции.
Примечание: Для получения подробной информации об использовании этого API см. документ `StartPublishCdnStream`.

Максимально 20 запросов могут быть инициированы в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, проверку подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: UpdatePublishCdnStream. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительную информацию см. в [списке поддерживаемых регионов](https://www.tencentcloud.com/document/api/647/34263#region-list) для продукта. Этот API поддерживает только: ap-guangzhou, ap-hongkong, ap-singapore. |
| SdkAppId | Да | Integer | [SDKAppID](https://intl.cloud.tencent.com/document/product/647/37714) комнаты TRTC, потоки которой транслируются. |
| TaskId | Да | String | Идентификатор задачи. |
| SequenceNumber | Да | Integer | Последовательность запроса. Этот параметр обеспечивает правильный порядок запросов на изменение параметров одной и той же задачи трансляции. Увеличивается при каждом новом запросе. |
| WithTranscoding | Да | Integer | Требуется ли транскодирование потоков. 0: нет; 1: да. |
| AudioParams | Нет | [McuAudioParams](https://www.tencentcloud.com/document/api/647/36760#McuAudioParams) | Передайте этот параметр для изменения пользователей, чьи аудиопотоки смешиваются. Если вы не передадите этот параметр, изменения не будут внесены. |
| VideoParams | Нет | [McuVideoParams](https://www.tencentcloud.com/document/api/647/36760#McuVideoParams) | Передайте этот параметр для изменения видеопараметров, кроме кодека, включая раскладку видео, фоновое изображение, цвет фона и информацию о водяном знаке. Этот параметр действителен только при транскодировании потоков. Если вы не передадите его, изменения не будут внесены. |
| SingleSubscribeParams | Нет | [SingleSubscribeParams](https://www.tencentcloud.com/document/api/647/36760#SingleSubscribeParams) | Передайте этот параметр для изменения одного потока, который транслируется. Этот параметр действителен только при отсутствии транскодирования потоков. Если вы не передадите этот параметр, изменения не будут внесены. |
| PublishCdnParams.N | Нет | Array of [McuPublishCdnParam](https://www.tencentcloud.com/document/api/647/36760#McuPublishCdnParam) | Передайте этот параметр для изменения CDN, на которые следует транслировать. Если вы не передадите этот параметр, изменения не будут внесены. |
| SeiParams | Нет | [McuSeiParams](https://www.tencentcloud.com/document/api/647/36760#McuSeiParams) | Параметры SEI смешивания потоков. |
| FeedBackRoomParams.N | Нет | Array of [McuFeedBackRoomParams](https://www.tencentcloud.com/document/api/647/36760#McuFeedBackRoomParams) | Информация о комнате, на которую транслируются потоки. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | Идентификатор задачи. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером. Возвращается для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId необходим для локализации проблемы. |

## 4. Примеры

### Пример 1. Изменение смешиваемых аудиопотоков и раскладки видео

Этот пример показывает, как изменить задачу трансляции для смешивания аудио и видео `Trtc_User_0` и `Trtc_User_3`.

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: UpdatePublishCdnStream
<Common request parameters>

{
    "SdkAppId": 1400188366,
    "TaskId": "-m97l2ZU7kOlV5cTRMoU6yoGp2nDYkzbJ13EC4K-4pycoZXVv+XVrNoUXQ8++8Z2PwUlAQ..",
    "SequenceNumber": 20,
    "WithTranscoding": 1,
    "AudioParams": {
        "SubscribeAudioList": [
            {
                "UserInfo": {
                    "RoomId": "48111",
                    "RoomIdType": 0,
                    "UserId": "Trtc_User_0"
                }
            },
            {
                "UserInfo": {
                    "RoomId": "48111",
                    "RoomIdType": 0,
                    "UserId": "Trtc_User_3"
                }
            }
        ]
    },
    "VideoParams": {
        "LayoutParams": {
            "MixLayoutMode": 4,
            "MixLayoutList": [
                {
                    "UserMediaStream": {
                        "UserInfo": {
                            "RoomId": "48111",
                            "RoomIdType": 0,
                            "UserId": "Trtc_User_3"
                        },
                        "StreamType": 0
                    },
                    "ImageWidth": 640,
                    "ImageHeight": 720,
                    "LocationX": 0,
                    "LocationY": 0,
                    "ZOrder": 0,
                    "RenderMode": 0
                },
                {
                    "UserMediaStream": {
                        "UserInfo": {
                            "RoomId": "48111",
                            "RoomIdType": 0,
                            "UserId": "Trtc_User_0"
                        },
                        "StreamType": 0
                    },
                    "ImageWidth": 640,
                    "ImageHeight": 720,
                    "LocationX": 640,
                    "LocationY": 360,
                    "ZOrder": 0,
                    "RenderMode": 0
                }
            ]
        }
    }
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f",
        "TaskId": "xxxx"
    }
}
```

### Пример 2. Изменение параметров трансляции

Этот пример показывает, как изменить параметры трансляции.

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: UpdatePublishCdnStream
<Common request parameters>

{
    "SdkAppId": 1400188366,
    "TaskId": "-m97l2ZU7kOlV5cTRMoU6yoGp2nDYkzbJ13EC4K-4pycoZXVv+XVrNoUXQ8++8Z2PwUlAQ..",
    "SequenceNumber": 20,
    "WithTranscoding": 1,
    "PublishCdnParams": [
        {
            "IsTencentCdn": 1,
            "PublishCdnUrl": "rtmp://3891.livepush.myqcloud.com/live/trtc_publishcdn_test2?bizid=3891&txSecret=23aeb6ec16fd275af0d00a447b2282f7&txTime=62635BDE"
        }
    ]
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f",
        "TaskId": "xxxx"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 включает SDK, поддерживающие различные языки программирования, чтобы облегчить вызов API.

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/647/34270#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| AuthFailure | Ошибка подписи CAM или проверки подлинности. |
| AuthFailure.UnRealNameAuthenticated | Проверка личности не была завершена, поэтому эта операция не допускается. |
| AuthFailure.UnauthorizedOperation | Ошибка проверки подлинности CAM. |
| AuthFailure.UnsupportedOperation | Неподдерживаемая операция. |
| FailedOperation | Ошибка операции. |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| MissingParameter | Отсутствует параметр. |
| ResourceNotFound | Ресурс не найден. |
| UnsupportedOperation | Неподдерживаемая операция. |


---
*Источник: [https://trtc.io/document/48245](https://trtc.io/document/48245)*

---
*Источник (EN): [updatepublishcdnstream.md](./updatepublishcdnstream.md)*

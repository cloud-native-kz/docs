# StartPublishCdnStream

## 1. Описание API

Доменное имя для запроса API: trtc.intl.tencentcloudapi.com.

**Описание API**

Этот API запускает задачу микширования потоков и трансляции. Этот API объединяет несколько аудио- и видеопотоков из комнаты TRTC в один поток, кодирует его и затем передает его на сервер CDN или публикует в комнату TRTC. Он также поддерживает трансляцию одного потока из комнаты TRTC напрямую без перекодирования.

После успешного выполнения API возвращает глобально уникальный TaskID. Вам потребуется этот TaskId в последующих операциях, таких как обновление или остановка задачи.

Для получения дополнительной информации см. документацию: [Описание функции](https://trtc.io/zh/document/47858?product=rtcengine) и [Часто задаваемые вопросы](https://trtc.io/zh/document/36058?product=rtcengine&menulabel=core%20sdk&platform=web) .

Примечание: Вы можете включить трансляцию в CDN в консоли для мониторинга событий в статусе трансляции в CDN. Для получения подробной информации об обратных вызовах см.: [Описание обратного вызова трансляции в CDN](https://trtc.io/zh/document/54913?product=rtcengine&menulabel=core%20sdk&platform=web) .

Запуск задачи трансляции может повлечь за собой следующие платежи:
Комиссия за микширование потоков MCU и перекодирование: [См. Цены на облачное микширование и перекодирование потоков](https://trtc.io/zh/document/47631) .

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызовы, аутентификацию подписей, генерацию кода SDK и быстрый поиск API. Это позволяет вам просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/647/34263).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: StartPublishCdnStream. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Значение, используемое для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/647/34263). Дополнительную информацию см. в разделе [Список регионов](https://www.tencentcloud.com/document/api/647/34263#region-list), поддерживаемых продуктом. Этот API поддерживает только: ap-guangzhou, ap-hongkong, ap-singapore. |
| SdkAppId | Да | Integer | [SDKAppID](https://intl.cloud.tencent.com/document/product/647/37714) комнаты TRTC, потоки которой трансляются. |
| RoomId | Да | String | ID комнаты, потоки которой трансляются (основная комната). |
| RoomIdType | Да | Integer | Тип параметра `RoomId`, который должен совпадать с типом ID комнаты, потоки которой трансляются. 0: целое число; 1: строка. |
| AgentParams | Да | [AgentParams](https://www.tencentcloud.com/document/api/647/36760#AgentParams) | Информация о роботе трансляции в комнате. |
| WithTranscoding | Да | Integer | Следует ли перекодировать потоки. `0`: нет. `1`: да. Этот параметр определяет, взимается ли комиссия за перекодирование. Если это `0`, потоки будут только трансляться, и комиссия за перекодирование не будет взиматься. Если это `1`, потоки будут перекодированы перед трансляцией, и будет взиматься комиссия за перекодирование. |
| AudioParams | Нет | [McuAudioParams](https://www.tencentcloud.com/document/api/647/36760#McuAudioParams) | Параметры кодирования аудио. Поскольку аудио всегда перекодируется (комиссия не взимается), этот параметр необходим при запуске задачи трансляции. |
| VideoParams | Нет | [McuVideoParams](https://www.tencentcloud.com/document/api/647/36760#McuVideoParams) | Параметры кодирования видео для трансляции. Если вы не передадите этот параметр, будет транслироваться только аудио. |
| SingleSubscribeParams | Нет | [SingleSubscribeParams](https://www.tencentcloud.com/document/api/647/36760#SingleSubscribeParams) | Информация о одном транслируемом потоке. При трансляции одного потока установите для `WithTranscoding` значение 0. |
| PublishCdnParams.N | Нет | Array of [McuPublishCdnParam](https://www.tencentcloud.com/document/api/647/36760#McuPublishCdnParam) | Информация о CDN, в которые следует транслировать. Вам необходимо указать хотя бы один из этого параметра и `FeedBackRoomParams.N`. |
| SeiParams | Нет | [McuSeiParams](https://www.tencentcloud.com/document/api/647/36760#McuSeiParams) | Параметры SEI микширования потоков. |
| FeedBackRoomParams.N | Нет | Array of [McuFeedBackRoomParams](https://www.tencentcloud.com/document/api/647/36760#McuFeedBackRoomParams) | Информация о комнате, в которую трансляются потоки. Между этим параметром и `PublishCdnParams` вы должны указать хотя бы один. Обратите внимание, что трансляция в комнату TRTC поддерживается только в некоторых версиях SDK. Для получения подробной информации свяжитесь с технической поддержкой. |
| RecordParams | Нет | [McuRecordParams](https://www.tencentcloud.com/document/api/647/36760#McuRecordParams) | Параметры записи трансляции. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | ID задачи, сгенерированный сервером Tencent Cloud. Вам необходимо передать ID задачи при выполнении запроса на обновление или остановку задачи трансляции. |
| RequestId | String | Уникальный ID запроса, сгенерированный сервером, будет возвращаться для каждого запроса (если запрос не достигает сервера по другим причинам, запрос не получит RequestId). RequestId необходим для определения проблемы. |

## 4. Пример

### Пример1 Микширование аудио/видео и трансляция

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: StartPublishCdnStream
<Common request parameters>

{
    "AgentParams": {
        "MaxIdleTime": 30,
        "UserSig": "eJw1zV8LgjAUBfCvInsO2dStGfQSQUb2pFJvsnLJJZW1LekPffdc6X08v8O5b5Snmd9LjRYeCnyMZt4vgUp2Fi7wB6vtuVRC207q0kpjSzIVTXUVSkE11EiEMeE8ZGw0*VCg5SCcDeRuBAutiwkLeRRwOo*nMajduy5O*gIaus9qel9vX*lJbHJmyDMxuKFFI27tsT*I1S6pl*jzBb*IOTE_",
        "UserId": "trtc_partner_test_1"
    },
    "AudioParams": {
        "AudioEncode": {
            "SampleRate": 48000,
            "Codec": 0,
            "BitRate": 64,
            "Channel": 2
        }
    },
    "VideoParams": {
        "VideoEncode": {
            "Height": 720,
            "Width": 1280,
            "Fps": 15,
            "BitRate": 1536,
            "Gop": 2
        },
        "LayoutParams": {
            "PureAudioHoldPlaceMode": 0,
            "MixLayoutMode": 4,
            "MixLayoutList": [
                {
                    "LocationX": 0,
                    "LocationY": 0,
                    "UserMediaStream": {
                        "StreamType": 0,
                        "UserInfo": {
                            "RoomIdType": 0,
                            "RoomId": "295066",
                            "UserId": "Trtc_User_0"
                        }
                    },
                    "ZOrder": 0,
                    "ImageHeight": 720,
                    "ImageWidth": 640,
                    "RenderMode": 0
                },
                {
                    "LocationX": 640,
                    "LocationY": 0,
                    "UserMediaStream": {
                        "StreamType": 0,
                        "UserInfo": {
                            "RoomIdType": 0,
                            "RoomId": "295066",
                            "UserId": "Trtc_User_1"
                        }
                    },
                    "ZOrder": 0,
                    "ImageHeight": 720,
                    "ImageWidth": 640,
                    "RenderMode": 0
                }
            ]
        },
        "BackGroundColor": "0xFF0000",
        "WaterMarkList": [
            {
                "WaterMarkType": 0,
                "WaterMarkImage": {
                    "LocationX": 64,
                    "LocationY": 64,
                    "WaterMarkHeight": 64,
                    "WaterMarkWidth": 64,
                    "WaterMarkUrl": "https://xkt-course-1304449343.cos.ap-beijing.myqcloud.com/test/mark/37f9eb62-ca72-430e-bfca-e700b59b20e0.png",
                    "ZOrder": 3
                }
            }
        ]
    },
    "PublishCdnParams": [
        {
            "PublishCdnUrl": "rtmp://3891.livepush.myqcloud.com/live/trtc_publishcdn_test1",
            "IsTencentCdn": 1
        }
    ],
    "RoomIdType": 0,
    "SdkAppId": 1400188366,
    "WithTranscoding": 1,
    "RoomId": "295066"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "TaskId": "-m97l2ZU7vxyBSmXYsRx1Xy9Kf4bVVfbbhSKC4K-4pycoZWKv542xbi139uTvGt1zAHoAQ..",
        "RequestId": "b934c535-8d82-4f52-bd52-a1cbb043c4be"
    }
}
```

### Пример2 Микширование аудио и трансляция

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: StartPublishCdnStream
<Common request parameters>

{
    "AgentParams": {
        "MaxIdleTime": 30,
        "UserSig": "eJw1zV8LgjAUBfCvInsO2dStGfQSQUb2pFJvsnLJJZW1LekPffdc6X08v8O5b5Snmd9LjRYeCnyMZt4vgUp2Fi7wB6vtuVRC207q0kpjSzIVTXUVSkE11EiEMeE8ZGw0*VCg5SCcDeRuBAutiwkLeRRwOo*nMajduy5O*gIaus9qel9vX*lJbHJmyDMxuKFFI27tsT*I1S6pl*jzBb*IOTE_",
        "UserId": "trtc_partner_test_1"
    },
    "AudioParams": {
        "AudioEncode": {
            "SampleRate": 48000,
            "Codec": 0,
            "BitRate": 64,
            "Channel": 2
        },
        "SubscribeAudioList": [
            {
                "UserInfo": {
                    "RoomIdType": 0,
                    "RoomId": "295066",
                    "UserId": "Trtc_User_0"
                }
            },
            {
                "UserInfo": {
                    "RoomIdType": 0,
                    "RoomId": "295066",
                    "UserId": "Trtc_User_1"
                }
            }
        ]
    },
    "PublishCdnParams": [
        {
            "PublishCdnUrl": "rtmp://3891.livepush.myqcloud.com/live/trtc_publishcdn_test1",
            "IsTencentCdn": 1
        }
    ],
    "RoomIdType": 0,
    "SdkAppId": 1400188366,
    "WithTranscoding": 1,
    "RoomId": "295066"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "388014ec-a0b8-4b8f-86bc-1f467448f5f0",
        "TaskId": "-m9lnV5U7nj4rkLBWMXF9n8-EohONCXbalWuLYK-4pycoZWQndibcqSVnrlqKF5om7EIDVk4awE."
    }
}
```

### Пример3 Трансляция аудио/видео

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: StartPublishCdnStream
<Common request parameters>

{
    "AgentParams": {
        "MaxIdleTime": 30,
        "UserSig": "eJw1zV8LgjAUBfCvInsO2dStGfQSQUb2pFJvsnLJJZW1LekPffdc6X08v8O5b5Snmd9LjRYeCnyMZt4vgUp2Fi7wB6vtuVRC207q0kpjSzIVTXUVSkE11EiEMeE8ZGw0*VCg5SCcDeRuBAutiwkLeRRwOo*nMajduy5O*gIaus9qel9vX*lJbHJmyDMxuKFFI27tsT*I1S6pl*jzBb*IOTE_",
        "UserId": "trtc_partner_test_1"
    },
    "AudioParams": {
        "AudioEncode": {
            "SampleRate": 48000,
            "Codec": 0,
            "BitRate": 64,
            "Channel": 2
        }
    },
    "VideoParams": {
        "VideoEncode": {
            "Height": 720,
            "Width": 1280,
            "Fps": 15,
            "BitRate": 1536,
            "Gop": 2
        }
    },
    "SingleSubscribeParams": {
        "UserMediaStream": {
            "StreamType": 0,
            "UserInfo": {
                "RoomIdType": 0,
                "RoomId": "295066",
                "UserId": "Trtc_User_0"
            }
        }
    },
    "PublishCdnParams": [
        {
            "PublishCdnUrl": "rtmp://3891.livepush.myqcloud.com/live/trtc_publishcdn_test1",
            "IsTencentCdn": 1
        }
    ],
    "RoomIdType": 0,
    "SdkAppId": 1400188366,
    "WithTranscoding": 0,
    "RoomId": "295066"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "TaskId": "-m97l2ZU7tq6nEsHR89259B8aCDblqnbGhWKC4K-4pycoZWpyHnld1jC9aCD+EU7V8WRAQ..",
        "RequestId": "f23d95bf-ddaf-4d0c-86c0-6bf50c74c0a0"
    }
}
```

### Пример4 Трансляция аудио

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: StartPublishCdnStream
<Common request parameters>

{
    "AgentParams": {
        "MaxIdleTime": 30,
        "UserSig": "eJw1zV8LgjAUBfCvInsO2dStGfQSQUb2pFJvsnLJJZW1LekPffdc6X08v8O5b5Snmd9LjRYeCnyMZt4vgUp2Fi7wB6vtuVRC207q0kpjSzIVTXUVSkE11EiEMeE8ZGw0*VCg5SCcDeRuBAutiwkLeRRwOo*nMajduy5O*gIaus9qel9vX*lJbHJmyDMxuKFFI27tsT*I1S6pl*jzBb*IOTE_",
        "UserId": "trtc_partner_test_1"
    },
    "AudioParams": {
        "AudioEncode": {
            "SampleRate": 48000,
            "Codec": 0,
            "BitRate": 64,
            "Channel": 2
        }
    },
    "SingleSubscribeParams": {
        "UserMediaStream": {
            "StreamType": 0,
            "UserInfo": {
                "RoomIdType": 0,
                "RoomId": "295066",
                "UserId": "Trtc_User_0"
            }
        }
    },
    "PublishCdnParams": [
        {
            "PublishCdnUrl": "rtmp://3891.livepush.myqcloud.com/live/trtc_publishcdn_test1",
            "IsTencentCdn": 1
        }
    ],
    "RoomIdType": 0,
    "SdkAppId": 1400188366,
    "WithTranscoding": 0,
    "RoomId": "295066"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "TaskId": "-m97l2ZU7r57nZBesMa84KgzxhH0OBbbCRaKC4K-4pycoZW7yFPtusNuZOen1Ca0qtQQAQ..",
        "RequestId": "ef089f8b-d0d1-4131-894d-4edd68d61605"
    }
}
```

### Пример5 Микширование аудио/видео, затем обратная трансляция

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: StartPublishCdnStream
<Common request parameters>

{
    "AgentParams": {
        "MaxIdleTime": 30,
        "UserSig": "eJw1zV8LgjAUBfCvInsO2dStGfQSQUb2pFJvsnLJJZW1LekPffdc6X08v8O5b5Snmd9LjRYeCnyMZt4vgUp2Fi7wB6vtuVRC207q0kpjSzIVTXUVSkE11EiEMeE8ZGw0*VCg5SCcDeRuBAutiwkLeRRwOo*nMajduy5O*gIaus9qel9vX*lJbHJmyDMxuKFFI27tsT*I1S6pl*jzBb*IOTE_",
        "UserId": "trtc_partner_test_1"
    },
    "AudioParams": {
        "AudioEncode": {
            "SampleRate": 48000,
            "Codec": 0,
            "BitRate": 64,
            "Channel": 2
        }
    },
    "VideoParams": {
        "VideoEncode": {
            "Height": 720,
            "Width": 1280,
            "Fps": 15,
            "BitRate": 1536,
            "Gop": 2
        },
        "LayoutParams": {
            "PureAudioHoldPlaceMode": 0,
            "MixLayoutMode": 4,
            "MixLayoutList": [
                {
                    "LocationX": 0,
                    "LocationY": 0,
                    "UserMediaStream": {
                        "StreamType": 0,
                        "UserInfo": {
                            "RoomIdType": 0,
                            "RoomId": "295066",
                            "UserId": "Trtc_User_0"
                        }
                    },
                    "ZOrder": 0,
                    "ImageHeight": 720,
                    "ImageWidth": 640,
                    "RenderMode": 0
                },
                {
                    "LocationX": 640,
                    "LocationY": 0,
                    "UserMediaStream": {
                        "StreamType": 0,
                        "UserInfo": {
                            "RoomIdType": 0,
                            "RoomId": "295066",
                            "UserId": "Trtc_User_1"
                        }
                    },
                    "ZOrder": 0,
                    "ImageHeight": 720,
                    "ImageWidth": 640,
                    "RenderMode": 0
                }
            ]
        },
        "BackGroundColor": "0xFF0000",
        "WaterMarkList": [
            {
                "WaterMarkType": 0,
                "WaterMarkImage": {
                    "LocationX": 64,
                    "LocationY": 64,
                    "WaterMarkHeight": 64,
                    "WaterMarkWidth": 64,
                    "WaterMarkUrl": "https://xkt-course-1304449343.cos.ap-beijing.myqcloud.com/test/mark/37f9eb62-ca72-430e-bfca-e700b59b20e0.png",
                    "ZOrder": 3
                }
            }
        ]
    },
    "FeedBackRoomParams": [
        {
            "RoomId": "630777",
            "RoomIdType": 0,
            "UserId": "trtc_partner_test_2",
            "UserSig": "eJwtjEELgjAYhv-Ldy10m7mtQYcQOtklU6mLSFs1LVnzq4Tovwfa8Xmel+cD*zQLXsaDAhYQmI9stenQnu2o0eOpcrXHzvgKTY8V*8963dbOWQ2KLgihUkacTwXt3YCigpIlo0KyyZrBWW9ARZyQ-4O9gIJrYfK365M85PEw02HZPneNaJJbg4-1Nj6KQqZZacVhI1fw-QEkCzYe"
        }
    ],
    "RoomIdType": 0,
    "SdkAppId": 1400188366,
    "WithTranscoding": 1,
    "RoomId": "295066"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "921e9cf6-b77c-4a7a-ab0e-c66a3e66fc59",
        "TaskId": "-m9lnV5U7n7TwoLKSsii1JivUn7DLDDbP16uLYK-4pycoZWQndib8GQJZEMMXFyOHe9Ds6WfxAE."
    }
}
```

### Пример6 Микширование аудио/видео и трансляция с макетом

#### Пример входных данных

```
POST / HTTP/1.1
Host: trtc.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: StartPublishCdnStream
<Common request parameters>

{
    "AgentParams": {
        "MaxIdleTime": 30,
        "UserSig": "eJw1zV8LgjAUBfCvInsO2dStGfQSQUb2pFJvsnLJJZW1LekPffdc6X08v8O5b5Snmd9LjRYeCnyMZt4vgUp2Fi7wB6vtuVRC207q0kpjSzIVTXUVSkE11EiEMeE8ZGw0*VCg5SCcDeRuBAutiwkLeRRwOo*nMajduy5O*gIaus9qel9vX*lJbHJmyDMxuKFFI27tsT*I1S6pl*jzBb*IOTE_",
        "UserId": "trtc_partner_test_1"
    },
    "AudioParams": {
        "AudioEncode": {
            "SampleRate": 48000,
            "Codec": 0,
            "BitRate": 64,
            "Channel": 2
        }
    },
    "VideoParams": {
        "VideoEncode": {
            "Height": 720,
            "Width": 1280,
            "Fps": 15,
            "BitRate": 1536,
            "Gop": 2
        },
        "LayoutParams": {
            "PureAudioHoldPlaceMode": 0,
            "MixLayoutMode": 4,
            "MixLayoutList": [
                {
                    "LocationX": 0,
                    "LocationY": 0,
                    "UserMediaStream": {
                        "StreamType": 0,
                        "UserInfo": {
                            "RoomIdType": 0,
                            "RoomId": "295066",
                            "UserId": "Trtc_User_0"
                        }
                    },
                    "ZOrder": 0,
                    "ImageHeight": 720,
                    "ImageWidth": 640,
                    "RenderMode": 0
                },
                {
                    "LocationX": 640,
                    "LocationY": 0,
                    "UserMediaStream": {
                        "StreamType": 0,
                        "UserInfo": {
                            "RoomIdType": 0,
                            "RoomId": "295066",
                            "UserId": "Trtc_User_1"
                        }
                    },
                    "ZOrder": 0,
                    "ImageHeight": 720,
                    "ImageWidth": 640,
                    "RenderMode": 0
                }
            ]
        },
        "BackGroundColor": "0xFF0000",
        "WaterMarkList": [
            {
                "WaterMarkType": 0,
                "WaterMarkImage": {
                    "LocationX": 64,
                    "LocationY": 64,
                    "WaterMarkHeight": 64,
                    "WaterMarkWidth": 64,
                    "WaterMarkUrl": "https://xkt-course-1304449343.cos.ap-beijing.myqcloud.com/test/mark/37f9eb62-ca72-430e-bfca-e700b59b20e0.png",
                    "ZOrder": 3
                }
            }
        ]
    },
    "SeiParams": {
        "LayoutVolume": {
            "AppData": "layout_sei_test",
            "PayloadType": 100,
            "Interval": 1000,
            "FollowIdr": 1
        }
    },
    "PublishCdnParams": [
        {
            "PublishCdnUrl": "rtmp://3891.livepush.myqcloud.com/live/trtc_publishcdn_test1",
            "IsTencentCdn": 1
        }
    ],
    "RoomIdType": 0,
    "SdkAppId": 1400188366,
    "WithTranscoding": 1,
    "RoomId": "295066"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "6dfc18

---
*Источник (EN): [startpublishcdnstream.md](./startpublishcdnstream.md)*

# Определение типов

### Распространённые структуры

#### TUICallDefine

| Тип | Описание |
| --- | --- |
| [TUICallParams](#TUICallParams) | Дополнительный параметр. |
| [TUIOfflinePushInfo](#TUIOfflinePushInfo) | Информация о конфигурации поставщика автономной отправки |
| [TUICallObserverExtraInfo](#TUICallObserverExtraInfo) | Дополнительная информация |

#### TUICommonDefine

| Тип | Описание |
| --- | --- |
| [TUIRoomId](#TUIRoomId) | ID комнаты для аудио и видео в звонке. |
| [TUINetworkQuality](#TUINetworkQuality) | Информация о качестве сети |
| [TUIVideoRenderParams](#TUIVideoRenderParams) | Параметры отрисовки видео |
| [TUIVideoEncoderParams](#TUIVideoEncoderParams) | Параметры кодирования видео |

### Определение перечислений

#### TUICallDefine

| Тип | Описание |
| --- | --- |
| [TUICallMediaType](#TUICallMediaType) | Тип медиа в звонке |
| [TUICallRole](#TUICallRole) | Роли участников в звонке |
| [TUICallStatus](#TUICallStatus) | Статус звонка |
| [TUICallScene](#TUICallScene) | Сценарий звонка |
| [TUICallIOSOfflinePushType](#TUICallIOSOfflinePushType) | Тип автономной отправки на iOS |
| [TUICallEndReason](#TUICallEndReason) | Причина завершения звонка |

#### TUICommonDefine

| Тип | Описание |
| --- | --- |
| [TUIAudioPlaybackDevice](#TUIAudioPlaybackDevice) | Маршрут аудио |
| [TUICamera](#TUICamera) | Тип камеры |
| [TUINetworkQuality](#TUINetworkQuality) | Качество сети |
| [TUIVideoRenderParamsFillMode](#TUIVideoRenderParamsFillMode) | Режим заполнения видеоизображения |
| [TUIVideoRenderParamsRotation](#TUIVideoRenderParamsRotation) | Направление поворота видеоизображения |
| [TUIVideoEncoderParamsResolutionMode](#TUIVideoEncoderParamsResolutionMode) | Режим соотношения сторон видео |
| [TUIVideoEncoderParamsResolution](#TUIVideoEncoderParamsResolution) | Разрешение видео |

### TUICallParams

Параметры звонка

| Значение | Тип | Описание |
| --- | --- | --- |
| roomId | [TUIRoomId](#TUIRoomId) | ID комнаты для аудио и видео в звонке. |
| offlinePushInfo | [TUIOfflinePushInfo](#TUIOfflinePushInfo) | Информация о конфигурации поставщика автономной отправки. |
| timeout | int | Время ожидания звонка, по умолчанию: 30 сек., единица: секунды. |
| userData | NSString | Дополнительный параметр. Обратный вызов при получении вызванным [onCallReceived](https://www.tencentcloud.com/document/product/647/51013#onCallReceived) |
| chatGroupId | NSString | ID группы чата |

### TUIOfflinePushInfo

Информация о конфигурации поставщика автономной отправки. Обратитесь к [Автономной отправке вызовов](https://www.tencentcloud.com/document/product/647/54923#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E9.85.8D.E7.BD.AE.E7.A6.BB.E7.BA.BF.E6.8E.A8.E9.80.81).

| Значение | Тип | Описание |
| --- | --- | --- |
| title | NSString | Название уведомления автономной отправки |
| desc | NSString | Описание уведомления автономной отправки |
| ignoreIOSBadge | BOOL | Игнорировать счётчик значков для автономной отправки (только для iOS). Если установить значение true, сообщение не будет увеличивать счётчик непрочитанных сообщений значка приложения на стороне получателя iOS. |
| iOSSound | NSString | Установка звука автономной отправки (только для iOS). Когда звук = **IOS_OFFLINE_PUSH_NO_SOUND**, при получении сообщения звук не воспроизводится. Когда звук = **IOS_OFFLINE_PUSH_DEFAULT_SOUND**, при получении сообщения воспроизводится системный звук. Если вы хотите настроить пользовательский iOSSound, сначала необходимо связать аудиофайл с проектом Xcode, а затем установить имя аудиофайла (с расширением) в iOSSound. |
| androidSound | NSString | Установка звука автономной отправки (только для Android, поддерживается IMSDK 6.1 и выше). Только телефоны Huawei и Google поддерживают установку звуковых оповещений. Для телефонов Xiaomi обратитесь к: [Пользовательские рингтоны Xiaomi.](https://dev.mi.com/console/doc/detail?pId=1278%23_3_0#_3_0) Кроме того, для телефонов Google, чтобы установить звуковые оповещения для FCM отправки на системах Android 8.0 и выше, необходимо вызвать setAndroidFCMChannelID для установки channelID, чтобы это вступило в силу. |
| androidOPPOChannelID | NSString | Установите ID канала для телефонов OPPO с системами Android 8.0 и выше. |
| androidVIVOClassification | NSInteger | Классификация сообщений VIVO отправки (устаревший интерфейс, служба VIVO отправки оптимизирует правила классификации сообщений 3 апреля 2023 г. Рекомендуется использовать setAndroidVIVOCategory для установки категории сообщений). 0: Операционные сообщения, 1: Системные сообщения. Значение по умолчанию: 1. |
| androidXiaoMiChannelID | NSString | Установите ID канала для телефонов Xiaomi с системами Android 8.0 и выше. |
| androidFCMChannelID | NSString | Установите ID канала для телефонов Google с системами Android 8.0 и выше. |
| androidHuaWeiCategory | NSString | Классификация сообщений Huawei отправки. Обратитесь к: [Стандарт классификации сообщений Huawei.](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835) |
| isDisablePush | BOOL | Отключить ли отправку уведомлений (по умолчанию включено). |
| iOSPushType | [TUICallIOSOfflinePushType](#TUICallIOSOfflinePushType) | Тип автономной отправки на iOS. По умолчанию APNs |

### TUICallObserverExtraInfo

Дополнительная информация обратного вызова.

| Тип | Тип | Описание |
| --- | --- | --- |
| roomId | [TUIRoomId](#TUIRoomId) | ID комнаты |
| role | [TUICallRole](#TUICallRole) | Роль в звонке |
| userData | String | Пользовательское дополнительное поле при инициировании звонка |
| chatGroupId | String | ID группы |

### TUIRoomId

ID комнаты для аудио и видео в звонке.
**Примечание:**

(1) `intRoomId` и `strRoomId` являются взаимоисключающими. Если вы решите использовать `strRoomId`, `intRoomId` должен быть заполнен значением 0. Если оба заполнены, SDK будет отдавать приоритет `intRoomId`.

(2) Не смешивайте `intRoomId` и `strRoomId`, так как они не взаимозаменяемы. Например, число 123 и строка "123" представляют две совершенно разные комнаты.

| Значение | Тип | Описание |
| --- | --- | --- |
| intRoomId | UInt32 | Числовой ID комнаты. **диапазон:** 1 - 2147483647 (2^31-1) |
| strRoomId | NSString | ID комнаты в виде строки. **диапазон:** Ограничено 64 байтами. Поддерживаемый набор символов выглядит следующим образом (всего 89 символов): Прописные и строчные английские буквы. (a-zA-Z) Цифры (0-9) `пробел`, `!`, `#`, `$`, `%`, `&`, `(`, `)`, `+`, `-`, `:`, `;`, `<`, `=`, `.`, `>`, `?`, `@`, `[`, `]`, `^`, `_`, `{`, `}`, `\|`, `~`, `,` |

> **Примечание:** В настоящее время номер комнаты со строковым типом поддерживается только на платформах Android, iOS, Flutter и Uni-app. Поддержка других платформ, таких как Web и Mini Programs, будет доступна в будущем. Следите за обновлениями!

### TUIVideoRenderParams

Параметры отрисовки видео

| Значение | Тип | Описание |
| --- | --- | --- |
| fillMode | [TUIVideoRenderParamsFillMode](#TUIVideoRenderParamsFillMode) | Режим заполнения видеоизображения |
| rotation | [TUIVideoRenderParamsRotation](#TUIVideoRenderParamsRotation) | Направление поворота видеоизображения |

### TUINetworkQualityInfo

Информация о качестве сети пользователя

| Значение | Тип | Описание |
| --- | --- | --- |
| userId | NSString | ID пользователя |
| quality | [NetworkQuality](#TUINetworkQuality) | Качество сети |

### TUIVideoEncoderParams

Параметры кодирования видео

| Значение | Тип | Описание |
| --- | --- | --- |
| resolution | [TUIVideoEncoderParamsResolution](#TUIVideoEncoderParamsResolution) | Разрешение видео |
| resolutionMode | [TUIVideoEncoderParamsResolutionMode](#TUIVideoEncoderParamsResolutionMode) | Режим соотношения сторон видео |

### TUICallMediaType

Тип медиа в звонке

| Тип | Значение | Описание |
| --- | --- | --- |
| TUICallMediaTypeUnknown | 0 | Неизвестно |
| TUICallMediaTypeAudio | 1 | Аудиозвонок |
| TUICallMediaTypeVideo | 2 | Видеозвонок |

### TUICallRole

Роль в звонке

| Тип | Значение | Описание |
| --- | --- | --- |
| TUICallRoleNone | 0 | Неизвестно |
| TUICallRoleCall | 1 | Звонящий (инициатор) |
| TUICallRoleCalled | 2 | Вызванный (получатель) |

### TUICallStatus

Статус звонка

| Тип | Значение | Описание |
| --- | --- | --- |
| TUICallStatusNone | 0 | Неизвестно |
| TUICallStatusWaiting | 1 | Звонок ожидается |
| TUICallStatusAccept | 2 | Звонок принят |

### TUICallScene

Сценарий звонка

| Тип | Значение | Описание |
| --- | --- | --- |
| TUICallSceneGroup | 0 | Групповой звонок |
| TUICallSceneMulti | 1 | Анонимный групповой звонок (в настоящее время не поддерживается, следите за обновлениями). |
| TUICallSceneSingle | 2 | Звонок один на один |

### TUICallIOSOfflinePushType

Тип автономной отправки на iOS

| Тип | Значение | Описание |
| --- | --- | --- |
| TUICallIOSOfflinePushTypeAPNs | 0 | APNs |
| TUICallIOSOfflinePushTypeVoIP | 1 | VoIP |

### TUICallEndReason

Причина завершения звонка

| Тип | Значение | Описание |
| --- | --- | --- |
| TUICallEndReasonUnknown | 0 | Неизвестно |
| TUICallEndReasonHangup | 1 | Завершение |
| TUICallEndReasonReject | 2 | Отказ |
| TUICallEndReasonNoResponse | 3 | Нет ответа |
| TUICallEndReasonOffline | 4 | В режиме оффлайн |
| TUICallEndReasonLineBusy | 5 | Линия занята |
| TUICallEndReasonCanceled | 6 | Звонок отменён |
| TUICallEndReasonOtherDeviceAccepted | 7 | Другое устройство ответило |
| TUICallEndReasonOtherDeviceReject | 8 | Другое устройство отказало |
| TUICallEndReasonEndByServer | 9 | Сервер завершил |

### TUIAudioPlaybackDevice

Маршрут аудио

| Тип | Значение | Описание |
| --- | --- | --- |
| TUIAudioPlaybackDeviceSpeakerphone | 0 | Громкая связь |
| TUIAudioPlaybackDeviceEarpiece | 1 | Наушник |

### TUICamera

Передняя/задняя камера

| Тип | Значение | Описание |
| --- | --- | --- |
| TUICameraFront | 0 | Передняя камера |
| TUICameraBack | 1 | Задняя камера |

### TUINetworkQuality

Качество сети

| Тип | Значение | Описание |
| --- | --- | --- |
| TUINetworkQualityUnknown | 0 | Неизвестно |
| TUINetworkQualityExcellent | 1 | Отличное |
| TUINetworkQualityGood | 2 | Хорошее |
| TUINetworkQualityPoor | 3 | Плохое |
| TUINetworkQualityBad | 4 | Очень плохое |
| TUINetworkQualityVbad | 5 | Критическое |
| TUINetworkQualityDown | 6 | Отсутствует |

### TUIVideoRenderParamsFillMode

Если соотношение сторон области отображения видео не равно соотношению сторон видеоизображения, необходимо указать режим заполнения:

| Тип | Значение | Описание |
| --- | --- | --- |
| TUIVideoRenderParamsFillModeFill | 0 | Режим заполнения: видеоизображение будет центрировано и масштабировано для заполнения всей области отображения, где части, выходящие за границы области, будут обрезаны. Отображаемое изображение может быть неполным в этом режиме. |
| TUIVideoRenderParamsFillModeFit | 1 | Режим подгонки: видеоизображение будет масштабировано на основе его большей стороны, чтобы соответствовать области отображения, где меньшая сторона будет заполнена чёрными полосами. Отображаемое изображение полное в этом режиме, но могут быть чёрные полосы. |

### TUIVideoRenderParamsRotation

Предоставляются API-интерфейсы установки угла поворота для локальных и удалённых изображений. Все следующие углы поворота — по часовой стрелке.

| Тип | Значение | Описание |
| --- | --- | --- |
| TUIVideoRenderParamsRotation_0 | 0 | Без поворота |
| TUIVideoRenderParamsRotation_90 | 1 | Поворот по часовой стрелке на 90 градусов |
| TUIVideoRenderParamsRotation_180 | 2 | Поворот по часовой стрелке на 180 градусов |
| TUIVideoRenderParamsRotation_270 | 3 | Поворот по часовой стрелке на 270 градусов |

### TUIVideoEncoderParamsResolutionMode

Режим соотношения сторон видео

| Тип | Значение | Описание |
| --- | --- | --- |
| TUIVideoEncoderParamsResolutionModeLandscape | 0 | Разрешение в альбомной ориентации, например: TUIVideoEncoderParamsResolution_640_360 + TUIVideoEncoderParamsResolutionModeLandscape = 640 × 360 |
| TUIVideoEncoderParamsResolutionModePortrait | 1 | Разрешение в портретной ориентации, например: TUIVideoEncoderParamsResolution_640_360 + TUIVideoEncoderParamsResolutionModePortrait = 360 × 640 |

### TUIVideoEncoderParamsResolution

Разрешение видео

| Тип | Значение | Описание |
| --- | --- | --- |
| TUIVideoEncoderParamsResolution_640_360 | 1 | Соотношение сторон: 16:9, разрешение: 640×360, рекомендуемый битрейт: 500 кбит/с |
| TUIVideoEncoderParamsResolution_960_540 | 2 | Соотношение сторон: 16:9, разрешение: 960×540, рекомендуемый битрейт: 850 кбит/с |
| TUIVideoEncoderParamsResolution_1280_720 | 3 | Соотношение сторон: 16:9, разрешение: 1280×720, рекомендуемый битрейт: 1200 кбит/с |
| TUIVideoEncoderParamsResolution_1920_1080 | 4 | Соотношение сторон: 16:9, разрешение: 1920×1080, рекомендуемый битрейт: 2000 кбит/с |


---
*Источник: [https://trtc.io/document/54902](https://trtc.io/document/54902)*

---
*Источник (EN): [type-definition.md](./type-definition.md)*

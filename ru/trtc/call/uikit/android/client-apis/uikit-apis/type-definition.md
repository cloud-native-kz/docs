# Определение типов

### Общие структуры

#### TUICallDefine

| Тип | Описание |
| --- | --- |
| [CallParams](https://www.tencentcloud.com/document/product/647/54900#CallParams) | Дополнительный параметр. |
| [OfflinePushInfo](https://www.tencentcloud.com/document/product/647/54900#OfflinePushInfo) | Информация конфигурации поставщика автономной отправки. |
| [CallObserverExtraInfo](https://www.tencentcloud.com/document/product/647/54900#CallObserverExtraInfo) | Расширенная информация |

#### TUICommonDefine

| Тип | Описание |
| --- | --- |
| [RoomId](https://www.tencentcloud.com/document/product/647/54900#RoomId) | Идентификатор комнаты для аудио и видео в звонке. |
| [NetworkQualityInfo](https://www.tencentcloud.com/document/product/647/54900#NetworkQualityInfo) | Информация о качестве сети |
| [VideoRenderParams](https://www.tencentcloud.com/document/product/647/54900#VideoRenderParams) | Параметры рендеринга видео |
| [VideoEncoderParams](https://www.tencentcloud.com/document/product/647/54900#VideoEncoderParams) | Параметры кодирования видео |

### Определение перечисления

#### TUICallDefine

| Тип | Описание |
| --- | --- |
| [MediaType](https://www.tencentcloud.com/document/product/647/54900#MediaType) | Тип мультимедиа в звонке |
| [Role](https://www.tencentcloud.com/document/product/647/54900#Role) | Роли лиц в звонке. |
| [Status](https://www.tencentcloud.com/document/product/647/54900#Status) | Статус звонка |
| [Scene](https://www.tencentcloud.com/document/product/647/54900#Scene) | Сценарий звонка |
| [IOSOfflinePushType](https://www.tencentcloud.com/document/product/647/54900#IOSOfflinePushType) | Тип автономной отправки iOS |
| [CallEndReason](https://www.tencentcloud.com/document/product/647/54900#CallEndReason) | Причина завершения звонка |

#### TUICommonDefine

| Тип | Описание |
| --- | --- |
| [AudioPlaybackDevice](https://www.tencentcloud.com/document/product/647/54900#AudioPlaybackDevice) | Аудиомаршрут |
| [Camera](https://www.tencentcloud.com/document/product/647/54900#Camera) | Тип камеры |
| [NetworkQuality](https://www.tencentcloud.com/document/product/647/54900#NetworkQuality) | Качество сети |
| [FillMode](https://www.tencentcloud.com/document/product/647/54900#FillMode) | Режим заполнения видеоизображения |
| [Rotation](https://www.tencentcloud.com/document/product/647/54900#Rotation) | Направление поворота видеоизображения |
| [ResolutionMode](https://www.tencentcloud.com/document/product/647/54900#ResolutionMode) | Режим соотношения сторон видео |
| [Resolution](https://www.tencentcloud.com/document/product/647/54900#Resolution) | Разрешение видео |

### CallParams

Параметры звонка

| Значение | Тип | Описание |
| --- | --- | --- |
| offlinePushInfo | [OfflinePushInfo](https://www.tencentcloud.com/document/product/647/54900#OfflinePushInfo) | Информация конфигурации поставщика автономной отправки. |
| timeout | int | Период ожидания звонка, по умолчанию: 30 сек., единица: секунды. |
| userData | String | Дополнительный параметр. Обратный вызов при получении вызываемым [onCallReceived](https://www.tencentcloud.com/document/product/647/51007#oncallreceived) |
| chatGroupId | String | Идентификатор группы чата. |

### OfflinePushInfo

Информация конфигурации поставщика автономной отправки, см.: [Автономная отправка звонков](https://www.tencentcloud.com/document/product/647/50999).

| Значение | Тип | Описание |
| --- | --- | --- |
| title | String | Название уведомления автономной отправки |
| desc | String | Описание уведомления автономной отправки |
| ignoreIOSBadge | boolean | Игнорировать количество значков для автономной отправки (только для iOS). Если установлено значение true, сообщение не будет увеличивать количество непрочитанных на значке приложения у получателя iOS. |
| iOSSound | String | Параметр звука автономной отправки (только для iOS). Когда `sound = IOS_OFFLINE_PUSH_NO_SOUND`, при получении сообщения звук не воспроизводится. Когда `sound = IOS_OFFLINE_PUSH_DEFAULT_SOUND`, при получении сообщения воспроизводится системный звук. Если вы хотите настроить пользовательский iOSSound, необходимо сначала связать аудиофайл с проектом Xcode, а затем установить имя аудиофайла (с расширением) на iOSSound. |
| androidSound | String | Параметр звука автономной отправки (только для Android, поддерживается IMSDK 6.1 и выше). Только телефоны Huawei и Google поддерживают установку звуковых подсказок. Для телефонов Xiaomi см.: [Пользовательские мелодии звонков Xiaomi](https://dev.mi.com/console/doc/detail?pId=1278%23_3_0#_3_0). Кроме того, для телефонов Google, чтобы установить звуковые подсказки для FCM push на системах Android 8.0 и выше, необходимо вызвать `setAndroidFCMChannelID`, чтобы установить для него channelID для вступления в силу. |
| androidOPPOChannelID | String | Установите ID канала для телефонов OPPO с системами Android 8.0 и выше. |
| androidVIVOClassification | int | Классификация сообщений push VIVO (устаревший интерфейс, служба push VIVO оптимизирует правила классификации сообщений 3 апреля 2023 г. Рекомендуется использовать setAndroidVIVOCategory для установки категории сообщения). 0: Операционные сообщения, 1: Системные сообщения. Значение по умолчанию — 1. |
| androidXiaoMiChannelID | String | Установите ID канала для телефонов Xiaomi с системами Android 8.0 и выше. |
| androidFCMChannelID | String | Установите ID канала для телефонов Google с системами Android 8.0 и выше. |
| androidHuaWeiCategory | String | Классификация сообщений push Huawei, см.: [Стандарт классификации сообщений Huawei.](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835) |
| isDisablePush | boolean | Следует ли отключить push-уведомления (по умолчанию включено). |
| iOSPushType | [IOSOfflinePushType](https://www.tencentcloud.com/document/product/647/54900#IOSOfflinePushType) | Тип автономной отправки iOS, по умолчанию APNs |

### CallObserverExtraInfo

| Значение | Тип | Описание |
| --- | --- | --- |
| roomId | [TUICommonDefine.RoomId](https://www.tencentcloud.com/document/product/647/54900#RoomId) | Идентификатор комнаты |
| role | [Role](https://www.tencentcloud.com/document/product/647/54900#Role) | Роль в звонке |
| userData | NSString | Пользовательское расширенное поле при инициировании звонка. |
| chatGroupId | NSString | Идентификатор группы |

### RoomId

Идентификатор комнаты для аудио и видео в звонке.
**Примечание:**

(1) `intRoomId` и `strRoomId` являются взаимоисключающими. Если вы решите использовать `strRoomId`, `intRoomId` должен быть заполнен как 0. Если оба заполнены, SDK будет отдавать приоритет `intRoomId`.

(2) Не смешивайте `intRoomId` и `strRoomId`, так как они не являются взаимозаменяемыми. Например, число 123 и строка "123" представляют две совершенно разные комнаты.

| Значение | Тип | Описание |
| --- | --- | --- |
| intRoomId | int | Числовой идентификатор комнаты. **диапазон:** 1 - 2147483647 (2^31-1) |
| strRoomId | String | Строковый идентификатор комнаты. **диапазон:** Ограничено 64 байтами длины. Поддерживаемый диапазон набора символов выглядит следующим образом (всего 89 символов): Строчные и прописные буквы латинского алфавита. (a-zA-Z) Цифра (0-9) `пробел`, `!`, `#`, `$`, `%`, `&`, `(`, `)`, `+`, `-`, `:`, `;`, `<`, `=`, `.`, `>`, `?`, `@`, `[`, `]`, `^`, `_`, `{`, `}`, `\|`, `~`, `,` |

> **Примечание:** В настоящее время строковый номер комнаты поддерживается только на платформах Android и iOS. Поддержка других платформ, таких как Web, Mini Programs, Flutter и Uniapp, появится в будущем. Оставайтесь в курсе!

### NetworkQualityInfo

Информация о качестве сети пользователя

| Значение | Тип | Описание |
| --- | --- | --- |
| userId | String | Идентификатор пользователя |
| quality | [NetworkQuality](https://www.tencentcloud.com/document/product/647/54900#NetworkQuality) | качество сети |

### VideoRenderParams

Параметры рендеринга видео

| Значение | Тип | Описание |
| --- | --- | --- |
| fillMode | [VideoRenderParams.FillMode](https://www.tencentcloud.com/document/product/647/54900#FillMode) | Режим заполнения видеоизображения |
| rotation | [VideoRenderParams.Rotation](https://www.tencentcloud.com/document/product/647/54900#Rotation) | Направление поворота видеоизображения |

### VideoEncoderParams

Параметры кодирования видео

| Значение | Тип | Описание |
| --- | --- | --- |
| resolution | [VideoEncoderParams.Resolution](https://www.tencentcloud.com/document/product/647/54900#Resolution) | Разрешение видео |
| resolutionMode | [VideoEncoderParams.ResolutionMode](https://www.tencentcloud.com/document/product/647/54900#ResolutionMode) | Режим соотношения сторон видео |

### MediaType

Тип мультимедиа звонка

| Значение | Тип | Описание |
| --- | --- | --- |
| Unknown | 0 | Неизвестно |
| Audio | 1 | Аудиозвонок |
| Video | 2 | Видеозвонок |

### Role

Роль в звонке

| Значение | Тип | Описание |
| --- | --- | --- |
| None | 0 | Неизвестно |
| Caller | 1 | Вызывающий (инициатор) |
| Called | 2 | Вызываемый (приглашенный) |

### Status

Статус звонка

| Значение | Тип | Описание |
| --- | --- | --- |
| None | 0 | Неизвестно |
| Waiting | 1 | Звонок в настоящее время ожидает |
| Accept | 2 | Звонок был принят |

### Scene

Сценарий звонка

| Значение | Тип | Описание |
| --- | --- | --- |
| SINGLE_CALL | 0 | Групповой звонок |
| GROUP_CALL | 1 | Анонимный групповой звонок (в настоящее время не поддерживается, оставайтесь в курсе). |
| MULTI_CALL | 2 | Звонок один на один |

### IOSOfflinePushType

Тип автономной отправки iOS

| Тип | Значение | Описание |
| --- | --- | --- |
| APNs | 0 | APNs |
| VoIP | 1 | VoIP |

### CallEndReason

| Значение | Тип | Описание |
| --- | --- | --- |
| UNKNOWN | 0 | Неизвестно |
| HANGUP | 1 | Повесить трубку |
| REJECT | 2 | Отклонить |
| NO_RESPONSE | 3 | Нет ответа |
| OFFLINE | 4 | Автономный |
| LINE_BUSY | 5 | Занято |
| CANCELED | 6 | Отмена звонка |
| OTHER_DEVICE_ACCEPTED | 7 | Другое устройство ответило |
| OTHER_DEVICE_REJECT | 8 | Другое устройство отклонило |
| END_BY_SERVER | 9 | Завершение на стороне сервера |

### AudioPlaybackDevice

Аудиомаршрут

| Тип | Значение | Описание |
| --- | --- | --- |
| Speakerphone | 0 | Наушник |
| Earpiece | 1 | Громкая связь |

### Camera

Передняя/задняя камера

| Тип | Значение | Описание |
| --- | --- | --- |
| Front | 0 | Передняя камера |
| Back | 1 | Задняя камера |

### NetworkQuality

Качество сети

| Тип | Значение | Описание |
| --- | --- | --- |
| UNKNOWN | 0 | Неизвестно |
| EXCELLENT | 1 | Отличное |
| GOOD | 2 | Хорошее |
| GOOD | 3 | Плохое |
| BAD | 4 | Плохое |
| VERY_BAD | 5 | Очень плохое |
| DOWN | 6 | Неработающее |

### FillMode

Если соотношение сторон области отображения видео не равно соотношению сторон видеоизображения, необходимо указать режим заполнения:

| Тип | Значение | Описание |
| --- | --- | --- |
| Fill | 0 | Режим заполнения: видеоизображение будет центрировано и масштабировано для заполнения всей области отображения, где части, выходящие за границы области, будут обрезаны. Отображаемое изображение может быть неполным в этом режиме. |
| Fit | 1 | Режим подгонки: видеоизображение будет масштабировано на основе его длинной стороны, чтобы соответствовать области отображения, где короткая сторона будет заполнена черными полосами. Отображаемое изображение полное в этом режиме, но могут присутствовать черные полосы. |

### Rotation

Мы предоставляем API для установки угла поворота локальных и удаленных изображений. Все следующие углы поворота идут по часовой стрелке.

| Тип | Значение | Описание |
| --- | --- | --- |
| Rotation_0 | 0 | Без поворота |
| Rotation_90 | 1 | Поворот по часовой стрелке на 90 градусов |
| Rotation_180 | 2 | Поворот по часовой стрелке на 180 градусов |
| Rotation_270 | 3 | Поворот по часовой стрелке на 0 градусов |

### ResolutionMode

Режим соотношения сторон видео

| Тип | Значение | Описание |
| --- | --- | --- |
| Landscape | 0 | Ландшафтное разрешение, например Resolution.Resolution_640_360 + ResolutionMode.Landscape = 640 × 360. |
| Portrait | 1 | Портретное разрешение, например Resolution.Resolution_640_360 + ResolutionMode.Portrait = 360 × 640. |

### Resolution

Разрешение видео

| Тип | Значение | Описание |
| --- | --- | --- |
| Resolution_640_360 | 108 | Соотношение сторон: 16:9, разрешение: 640x360, рекомендуемый битрейт: 500 кбит/с |
| Resolution_960_540 | 110 | Соотношение сторон: 16:9, разрешение: 960x540, рекомендуемый битрейт: 850 кбит/с |
| Resolution_1280_720 | 112 | Соотношение сторон: 16:9, разрешение: 1280x720, рекомендуемый битрейт: 1200 кбит/с |
| Resolution_1920_1080 | 114 | Соотношение сторон: 16:9, разрешение: 1920x1080, рекомендуемый битрейт: 2000 кбит/с |


---
*Источник: [https://trtc.io/document/54900](https://trtc.io/document/54900)*

---
*Источник (EN): [type-definition.md](./type-definition.md)*

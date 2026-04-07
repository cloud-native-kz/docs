# Определение типов

## Общие структуры

### TUIResult

Возвращаемое значение при вызове API.

| Значение | Тип | Описание |
| --- | --- | --- |
| code | String | Если код пуст "", это означает, что вызов выполнен успешно, если код не пуст "", это означает, что вызов не выполнен. |
| message | String? | Сообщение об ошибке |

### TUIRoomId

Идентификатор комнаты для аудио и видео в звонке.

**Примечание:**

(1) `intRoomId` и `strRoomId` являются взаимоисключающими. Если вы выбираете использование `strRoomId`, `intRoomId` должен быть установлен на 0. Если оба заполнены, SDK будет отдавать приоритет `intRoomId`.

(2) Не смешивайте `intRoomId` и `strRoomId`, так как они не взаимозаменяемы. Например, число 123 и строка "123" представляют две совершенно разные комнаты.

| Значение | Тип | Описание |
| --- | --- | --- |
| intRoomId | int | Числовой идентификатор комнаты. |
| strRoomId | String | Строковый номер комнаты. |

### VideoRenderParams

Параметры отрисовки видео.

| Значение | Тип | Описание |
| --- | --- | --- |
| fillMode | [FillMode](https://www.tencentcloud.com/document/product/647/54909#FillMode) | Режим заполнения видеоизображения |
| rotation | [Rotation](https://www.tencentcloud.com/document/product/647/54909#Rotation) | Направление поворота видеоизображения |

### VideoEncoderParams

Параметры кодирования видео.

| Значение | Тип | Описание |
| --- | --- | --- |
| resolution | [Resolution](https://www.tencentcloud.com/document/product/647/54909#Resolution) | Разрешение видео |
| resolutionMode | [ResolutionMode](https://www.tencentcloud.com/document/product/647/54909#ResolutionMode) | Режим соотношения сторон видео |

### TUICallParams

Параметры вызова.

| Значение | Тип | Описание |
| --- | --- | --- |
| roomId | [TUIRoomId](https://www.tencentcloud.com/document/product/647/54909#TUIRoomId) | Идентификатор комнаты. |
| offlinePushInfo | [TUIOfflinePushInfo](https://www.tencentcloud.com/document/product/647/54909#TUIOfflinePushInfo) | Информация о конфигурации поставщика автономной доставки. |
| timeout | String | Период ожидания звонка, по умолчанию: 30 с, единица: секунды. |
| userData | String | Дополнительный параметр. |
| chatGroupId | String | Идентификатор группы. |

### TUIOfflinePushInfo

Информация о конфигурации поставщика автономной доставки. Дополнительную информацию см. в: [Автономная доставка звонков](https://www.tencentcloud.com/document/product/647/50999#).

| Значение | Тип | Описание |
| --- | --- | --- |
| title | String | Название уведомления автономной доставки |
| desc | String | Описание уведомления автономной доставки |
| ignoreIOSBadge | bool | Игнорировать счетчик значков для автономной доставки (только для iOS). При установке значения true сообщение не будет увеличивать счетчик непрочитанных сообщений значка приложения на стороне получателя iOS. |
| iOSSound | String | Настройка звука для автономной доставки (только для iOS). Когда sound = IOS_OFFLINE_PUSH_NO_SOUND , звук не будет воспроизводиться при получении сообщения. Когда sound = IOS_OFFLINE_PUSH_DEFAULT_SOUND , системный звук будет воспроизводиться при получении сообщения. Если вы хотите настроить iOSSound, вам сначала нужно связать аудиофайл с проектом Xcode, а затем установить имя аудиофайла (с расширением) на iOSSound. |
| androidSound | String | Настройка звука для автономной доставки (только для Android, поддерживается IMSDK 6.1 и выше). Только телефоны Huawei и Google поддерживают установку звуковых сигналов. Для телефонов Xiaomi см.: Пользовательские рингтоны Xiaomi . Кроме того, для телефонов Google, чтобы установить звуковые сигналы для FCM push на системах Android 8.0 и выше, вы должны вызвать setAndroidFCMChannelID , чтобы установить для него channelID, чтобы это вступило в силу. |
| androidOPPOChannelID | String | Установить идентификатор канала для телефонов OPPO с системами Android 8.0 и выше. |
| androidVIVOClassification | int | Классификация push-сообщений VIVO (устаревший интерфейс, служба push VIVO оптимизирует правила классификации сообщений 3 апреля 2023 г. Рекомендуется использовать setAndroidVIVOCategory для установки категории сообщений). 0: Операционные сообщения, 1: Системные сообщения. Значение по умолчанию — 1. |
| androidXiaoMiChannelID | String | Установить идентификатор канала для телефонов Xiaomi с системами Android 8.0 и выше. |
| androidFCMChannelID | String | Установить идентификатор канала для телефонов Google с системами Android 8.0 и выше. |
| androidHuaWeiCategory | String | Классификация push-сообщений Huawei. Дополнительную информацию см. в: [Стандарт классификации сообщений Huawei.](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835) |
| isDisablePush | bool | Отключить ли push-уведомления (по умолчанию включено). |
| iOSPushType | [TUICallIOSOfflinePushType](https://www.tencentcloud.com/document/product/647/54909#TUICallIOSOfflinePushType) | Тип автономной доставки iOS, по умолчанию APNs |

### TUICallRecords

Информация о записи вызова.

| Значение | Тип | Описание |
| --- | --- | --- |
| callId | String | Идентификатор записи вызова. |
| inviter | String | Идентификатор приглашающего. |
| inviteList | List<String> | Список идентификаторов приглашенных пользователей. |
| scene | [TUICallScene](https://www.tencentcloud.com/document/product/647/54909#83cc1eda-8838-4ad9-8d60-538b097ab2b7) | Сценарий вызова. |
| mediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54909#TUICallMediaType) | Тип мультимедиа. |
| groupId | String | Идентификатор группы. |
| role | [TUICallRole](https://www.tencentcloud.com/document/product/647/54909#2be5b153-a7fc-4608-b095-edc663d0f37c) | Роль. |
| result | [TUICallResultType](https://www.tencentcloud.com/document/product/647/54909#TUICallMediaType) | Тип результата вызова. |
| beginTime | int | Время начала. |
| totalTime | int | Общее время. |

### TUICallRecentCallsFilter

Условия фильтрации записей вызовов.

| Значение | Тип | Описание |
| --- | --- | --- |
| begin | double | Время начала. |
| end | double | Время окончания. |
| resultType | [TUICallResultType](https://www.tencentcloud.com/document/product/647/54909#TUICallResultType) | Тип результата вызова. |

### CallObserverExtraInfo

Информация о расширении обратного вызова.

| Тип | Тип | Описание |
| --- | --- | --- |
| roomId | [TUIRoomId](https://www.tencentcloud.com/document/product/647/54909#TUIRoomId) | Идентификатор комнаты |
| role | [TUICallRole](https://www.tencentcloud.com/document/product/647/54909#2be5b153-a7fc-4608-b095-edc663d0f37c) | Роль вызова |
| userData | String | Пользовательское расширенное поле при инициировании звонка. Дополнительную информацию см. в [TUICallParams](https://www.tencentcloud.com/document/product/647/54909#TUICallParams). |
| chatGroupId | String | Идентификатор группы |

## **Определение перечисления**

### TUICallMediaType

Тип мультимедиа вызова.

| Тип | Описание |
| --- | --- |
| none | Неизвестный |
| audio | Аудиозвонок |
| video | Видеозвонок |

### TUICallRole

Роль вызова.

| Тип | Описание |
| --- | --- |
| none | Неизвестный |
| caller | Инициатор (приглашающий) |
| called | Получатель (приглашенный) |

### TUICallStatus

Статус вызова.

| Тип | Описание |
| --- | --- |
| none | Неизвестный |
| waiting | Вызов в настоящее время ожидает |
| accept | Вызов принят |

### TUICallScene

Сценарий вызова.

| Тип | Описание |
| --- | --- |
| groupCall | Групповой вызов |
| singleCall | Персональный вызов один на один |

### TUINetworkQuality

Качество сети.

| Тип | Описание |
| --- | --- |
| unknown | Неизвестный |
| excellent | Отличный |
| good | Хороший |
| poor | Плохой |
| bad | Очень плохой |
| vBad | Очень плохой |
| down | Выключено |

### FillMode

Если соотношение сторон области отображения видео не равно соотношению сторон видеоизображения, необходимо указать режим заполнения:

| Тип | Описание |
| --- | --- |
| fill | Режим заполнения: видеоизображение будет отцентрировано и масштабировано, чтобы заполнить всю область отображения, где части, выходящие за пределы области, будут обрезаны. Отображаемое изображение может быть неполным в этом режиме. |
| fit | Режим подгонки: видеоизображение будет масштабировано по его длинной стороне, чтобы поместиться в области отображения, где короткая сторона будет заполнена черными полосами. Отображаемое изображение полное в этом режиме, но могут быть черные полосы. |

### Rotation

Мы предоставляем API-интерфейсы для установки угла поворота для локальных и удаленных изображений. Следующие углы поворота все по часовой стрелке.

| Тип | Описание |
| --- | --- |
| rotation_0 | Нет поворота |
| rotation_90 | Поворот по часовой стрелке на 90 градусов |
| rotation_180 | Поворот по часовой стрелке на 180 градусов |
| rotation_270 | Поворот по часовой стрелке на 270 градусов |

### ResolutionMode

Режим соотношения сторон видео.

| Тип | Описание |
| --- | --- |
| landscape | Ландшафтное разрешение, например Resolution.Resolution_640_360 + ResolutionMode.Landscape = 640 × 360. |
| portrait | Портретное разрешение, например Resolution.Resolution_640_360 + ResolutionMode.Portrait = 360 × 640. |

### Resolution

Разрешение видео.

| Тип | Описание |
| --- | --- |
| resolution_640_360 | Соотношение сторон: 16:9, разрешение: 640x360, рекомендуемый битрейт: 500 кбит/с |
| resolution_960_540 | Соотношение сторон: 16:9, разрешение: 960x540, рекомендуемый битрейт: 850 кбит/с |
| resolution_1280_720 | Соотношение сторон: 16:9, разрешение: 1280x720, рекомендуемый битрейт: 1200 кбит/с |
| resolution_1920_1080 | Соотношение сторон: 16:9, разрешение: 1920x1080, рекомендуемый битрейт: 2000 кбит/с |

### TUICallIOSOfflinePushType

Тип автономной доставки iOS.

| Тип | Описание |
| --- | --- |
| APNs | APNs |
| VoIP | VoIP |

### TUICamera

Тип камеры.

| Тип | Описание |
| --- | --- |
| front | Фронтальная камера. |
| back | Задняя камера. |

### TUIAudioPlaybackDevice

Устройство воспроизведения аудио.

| Тип | Описание |
| --- | --- |
| speakerphone | Динамик |
| earpiece | Наушники |

### TUICallResultType

Тип записи вызова.

| Тип | Описание |
| --- | --- |
| unknown | Неизвестный |
| missed | Пропущенный |
| incoming | Входящий звонок |
| outgoing | Исходящий звонок |

### CallEndReason

Причина завершения вызова.

| Тип | Описание |
| --- | --- |
| unknown | Неизвестный |
| hangup | Завершить |
| reject | Отклонить |
| noResponse | Нет ответа |
| offline | Автономный |
| lineBusy | Линия занята |
| canceled | Отменить звонок |
| otherDeviceAccepted | Другое устройство ответило |
| otherDeviceReject | Другое устройство отклонило |
| endByServer | Завершено сервером |


---
*Источник: [https://trtc.io/document/54909](https://trtc.io/document/54909)*

---
*Источник (EN): [type-definition.md](./type-definition.md)*

# TUIRoomEngine Определения

Введение в определение ключевых типов TUIRoomEngine для стороны Electron.

## Значения перечисления

### TUIRole

Роль пользователя. TUIRoomEngine предоставляет три роли пользователя: Host, Administrator и Regular User.

| Поле | Тип | Описание |
| --- | --- | --- |
| kRoomOwner | number | Роль Host |
| kAdministrator | number | Роль Administrator |
| kGeneralUser | number | Роль Regular User |

### TUIVideoQuality

Разрешение видео

| Поле | Тип | Описание |
| --- | --- | --- |
| kVideoQuality_360p | number | Низкое качество, разрешение 640 * 360 |
| kVideoQuality_540p | number | SD, разрешение 960 * 540 |
| kVideoQuality_720p | number | HD, разрешение 1280 * 720 |
| kVideoQuality_1080p | number | Ultra HD, разрешение 1920 * 1080 |

### TUIAudioProfile

Разрешение аудио

| Поле | Тип | Описание |
| --- | --- | --- |
| kAudioProfileSpeech | number | Режим голоса |
| kAudioProfileDefault | number | Стандартный режим (режим по умолчанию) |
| kAudioProfileMusic | number | Режим музыки |

### TUIVideoStreamType

Тип потоков

| Поле | Тип | Описание |
| --- | --- | --- |
| kCameraStream | number | Потоки камеры |
| kScreenStream | number | Потоки совместного использования экрана |
| kCameraStreamLow | number | Потоки камеры низкого разрешения |

### TUINetworkQuality

Состояние сети

| Поле | Тип | Описание |
| --- | --- | --- |
| kQualityUnknown | number | Состояние сети неизвестно |
| kQualityExcellent | number | Состояние сети отличное |
| kQualityGood | number | Состояние сети хорошее |
| kQualityPoor | number | Состояние сети удовлетворительное |
| kQualityBad | number | Состояние сети плохое |
| kQualityVeryBad | number | Состояние сети очень плохое |
| kQualityDown | number | Сетевое соединение разорвано |

### TUIRoomType

Тип комнаты

| Поле | Тип | Описание |
| --- | --- | --- |
| kGroup | number | Групповой тип комнаты, подходит для конференций и сценариев обучения. Позиции микрофона в этой комнате неупорядочены и не имеют ограничений по количеству |
| kOpen | number | Открытый тип комнаты, подходит для сценариев прямого вещания. Позиции микрофона в этой комнате упорядочены и имеют ограничение по количеству |

### TUISpeechMode

Тип речи

| Поле | Тип | Описание |
| --- | --- | --- |
| kFreeToSpeak | number | Режим свободной речи |
| kApplyToSpeak | number | Режим речи с поднятием руки |
| kSpeakAfterTakingSeat | number | Речь после захвата позиции (захват позиции микрофона) |

### TUICaptureSourceType

Тип совместного использования экрана

| Поле | Тип | Описание |
| --- | --- | --- |
| kWindow | number | Целью совместного использования является конкретное окно Windows или Mac (только для electron) |
| kScreen | number | Целью совместного использования является весь рабочий стол Windows или Mac |

### TUIChangeReason

Причина изменения (причина изменения состояния аудио и видео: собственное изменение или изменение, произведенное владельцем комнаты/администратором)

| Поле | Тип | Описание |
| --- | --- | --- |
| kChangedBySelf | number | Собственная операция |
| kChangedByAdmin | number | Операция владельца комнаты или администратора |

### TUIMediaDevice

| Поле | Тип | Описание |
| --- | --- | --- |
| kMicrophone | number | Микрофон |
| kCamera | number | Камера |
| kScreen | number | Совместное использование экрана |

### TUIRequestAction

Тип комнаты

| Поле | Тип | Описание |
| --- | --- | --- |
| kInvalidAction | number | Недопустимая операция |
| kRequestToOpenRemoteCamera | number | Запрос на включение удаленной камеры |
| kRequestToOpenRemoteMicrophone | number | Запрос на включение удаленного микрофона |
| kRequestToConnectOtherRoom | number | Запрос на трансляцию между комнатами, веб-сторона временно не поддерживается |
| kRequestToTakeSeat | number | Запрос на начало прямого вещания |
| kRequestRemoteUserOnSeat | number | Запрос на начало удаленного прямого вещания |

### TUIRequestCallbackType

Тип запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| kRequestAccepted | number | Принято участником |
| kRequestRejected | number | Отклонено участником |
| kRequestCancelled | number | Запрос отменен |
| kRequestTimeout | number | Истечение времени ожидания запроса |
| kRequestError | number | Ошибка запроса |

## Определение типов

### TUILoginUserInfo

Информация о текущем вошедшем пользователе

| Поле | Тип | Описание |
| --- | --- | --- |
| userId | string | ID вошедшего пользователя |
| userName | string | Имя вошедшего пользователя |
| avatarUrl | string | Аватар вошедшего пользователя |

### TUIRoomInfo

Данные комнаты. Пользователь может использовать roomEngine.getRoomInfo для получения данных комнаты.

| Поле | Тип | Описание |
| --- | --- | --- |
| roomId | string | Номер комнаты, номер комнаты строкового типа |
| roomType | [TUIRoomType](https://www.tencentcloud.com/document/product/647/54886#TUIRoomType) | Тип комнаты |
| owner | string | userId владельца комнаты |
| name | string | ID комнаты |
| createTime | string | Время создания |
| roomMemberCount | number | Текущее общее количество людей в комнате |
| maxSeatCount | number | Максимальное количество позиций микрофона в комнате |
| enableVideo | boolean | Разрешить пользователям присоединиться и включить аудио |
| enableAudio | boolean | Разрешить пользователям присоединиться и включить видео |
| enableMessage | boolean | Разрешить пользователям присоединиться и отправлять сообщения |
| enableSeatControl | boolean | Включить управление позицией микрофона |

### TUIUserInfo

Информация о пользователе

| Поле | Тип | Описание |
| --- | --- | --- |
| userId | string | ID пользователя |
| userName | string | Имя пользователя |
| avatarUrl | string | Аватар пользователя |
| userRole | [TUIRole](https://www.tencentcloud.com/document/product/647/54886#TUIRole) | Роль пользователя |
| hasAudioStream | boolean | Наличие потока аудио |
| hasVideoStream | boolean | Наличие потока видео |
| hasScreenStream | boolean | Наличие потока совместного использования экрана |

### TUIMessage

Информация о сообщении

| Поле | Тип | Описание |
| --- | --- | --- |
| messageId | string | ID сообщения |
| message | string | Сообщение |
| timestamp | number | Информация о временной метке, точность до секунд |
| userId | string | ID пользователя |
| userName | string | Имя пользователя |
| avatarUrl | string | Аватар пользователя |

### TUIRequest

Информация о запросе

| Поле | Тип | Описание |
| --- | --- | --- |
| requestAction | [TUIRequestAction](https://www.tencentcloud.com/document/product/647/54886#e2746642-b1ff-453c-bb41-ca4c64c75566) | Тип запроса |
| timestamp | number | Время инициирования запроса |
| requestId | string | ID запроса. В версиях v1.0.2 и выше тип requestId является string; в версиях v1.0.0 и v1.0.1 тип requestId является number; |
| userId | string | ID пользователя, инициирующего запрос |
| content | string | Другое содержимое |

### TUIRequestCallback

Информация о обратном вызове запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| requestCallbackType | [TUIRequestCallbackType](https://www.tencentcloud.com/document/product/647/54886#a0211e22-30e2-4b3a-bc89-1cf1aa816695) | Тип обратного вызова запроса: принять/отклонить/отменить/истечение времени/ошибка |
| requestId | string | ID запроса. В версиях v1.0.2 и выше тип requestId является string; в версиях v1.0.0 и v1.0.1 тип requestId является number; |
| userId | string | ID пользователя |
| code | number | Код ответа запроса |
| message | string | Дополнительное описание статуса запроса |

### TUISeatInfo

Информация о позиции микрофона

| Поле | Тип | Описание |
| --- | --- | --- |
| index | number | Номер позиции микрофона |
| userId | string | ID пользователя, соответствующий позиции микрофона |
| locked | boolean | Заблокирована ли текущая позиция микрофона |
| videoMuted | boolean | Запрещено ли видео на текущей позиции микрофона |
| audioMuted | boolean | Запрещено ли аудио на текущей позиции микрофона |

### TUISeatLockParams

Статус блокировки микрофона

| Поле | Тип | Описание |
| --- | --- | --- |
| lockSeat | boolean | Заблокировать позицию микрофона |
| lockVideo | boolean | Заблокировать видео позиции микрофона |
| lockAudio | boolean | Заблокировать аудио позиции микрофона |

### TUINetwork

Информация о сети

| Поле | Тип | Описание |
| --- | --- | --- |
| userId | string | ID пользователя |
| quality | TUINetworkQuality | Качество сети |
| upLoss | number | Коэффициент потери пакетов в восходящем канале, единица измерения (%). Чем меньше значение, тем лучше. В настоящее время только локальные пользователи имеют эту информацию |
| downLoss | number | Коэффициент потери пакетов в нисходящем канале, единица измерения (%). Чем меньше значение, тем лучше. В настоящее время только локальные пользователи имеют эту информацию |
| delay | number | Задержка сети, единица измерения ms. В настоящее время только локальные пользователи имеют эту информацию |


---
*Источник: [https://trtc.io/document/54886](https://trtc.io/document/54886)*

---
*Источник (EN): [tuiroomengine-defines.md](./tuiroomengine-defines.md)*

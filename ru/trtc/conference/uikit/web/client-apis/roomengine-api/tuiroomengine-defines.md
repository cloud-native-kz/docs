# TUIRoomEngine Defines

Введение в определение ключевых типов TUIRoomEngine для веб-стороны.

## Значения Enum

### TUIRole

Роль пользователя, TUIRoomEngine предоставляет три роли пользователя: Host, Administrator и Regular User.

| Поле | Тип | Описание |
| --- | --- | --- |
| kRoomOwner | number | Роль Host |
| kAdministrator | number | Роль Administrator |
| kGeneralUser | number | Роль Regular User |

### TUIVideoProfile

Разрешение видео

| Поле | Тип | Описание |
| --- | --- | --- |
| kLowDefinition | number | Низкое разрешение |
| kStandardDefinition | number | SD |
| kHighDefinition | number | HD |
| kSuperDefinition | number | Ultra HD |

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
| kScreenStream | number | Потоки общего доступа к экрану |
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
| kGroup | number | Комната группового типа, подходит для сценариев конференций и обучения, позиции микрофонов в такой комнате неупорядочены и не имеют ограничений по количеству |
| kOpen | number | Комната открытого типа, подходит для сценариев прямых трансляций, позиции микрофонов в такой комнате упорядочены и имеют ограничения по количеству |

### TUISpeechMode

Тип речи

| Поле | Тип | Описание |
| --- | --- | --- |
| kFreeToSpeak | number | Режим свободной речи |
| kApplyToSpeak | number | Режим речи с поднятием руки |
| kSpeakAfterTakingSeat | number | Говорить после занятия места (захват позиции микрофона) |

### TUICaptureSourceType

Тип общего доступа к экрану

| Поле | Тип | Описание |
| --- | --- | --- |
| kWindow | number | Целью общего доступа является конкретное окно Windows или Mac todo (только для electron) |
| kScreen | number | Целью общего доступа является весь рабочий стол Windows или рабочий стол Mac |

### TUIChangeReason

Причина изменения (причина изменения состояния аудио и видео: самостоятельное изменение или изменение владельцем комнаты/администратором)

| Поле | Тип | Описание |
| --- | --- | --- |
| kChangedBySelf | number | Самостоятельная операция |
| kChangedByAdmin | number | Операция владельца комнаты или администратора |

### TUIRequestAction

Тип комнаты

| Поле | Тип | Описание |
| --- | --- | --- |
| kInvalidAction | number | Некорректная операция |
| kRequestToOpenRemoteCamera | number | Запрос на включение удаленной камеры |
| kRequestToOpenRemoteMicrophone | number | Запрос на включение удаленного микрофона |
| kRequestToConnectOtherRoom | number | Запрос удаленной трансляции между комнатами, веб-сторона временно не поддерживается |
| kRequestToTakeSeat | number | Запрос на трансляцию |
| kRequestRemoteUserOnSeat | number | Запрос на удаленную трансляцию |

### TUIRequestCallbackType

Тип запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| kRequestAccepted | number | Одобрено |
| kRequestRejected | number | Отклонено |
| kRequestCancelled | number | Запрос отменен |
| kRequestTimeout | number | Истечение времени ожидания запроса |
| kRequestError | number | Ошибка запроса |

## Определение типов

### TUIRoomInfo

Данные комнаты, пользователь может использовать roomEngine.getRoomInfo для получения данных комнаты.

| Поле | Тип | Описание |
| --- | --- | --- |
| roomId | string | Номер комнаты, номер комнаты строкового типа |
| roomType | [TUIRoomType](/document/product/647/54876#d149b153-35ff-4cab-84cb-c8d0009e179f) | Тип комнаты |
| owner | string | userId хоста |
| name | string | Идентификатор комнаты |
| createTime | string | Время создания |
| roomMemberCount | number | Текущее общее количество людей в комнате |
| maxSeatCount | number | Максимальное количество позиций микрофонов в комнате |
| enableVideo | boolean | Разрешить пользователям присоединиться и включить аудио |
| enableAudio | boolean | Разрешить пользователям присоединиться и включить видео |
| enableMessage | boolean | Разрешить пользователям отправлять сообщения |
| enableSeatControl | boolean | Включить управление позициями микрофонов |

### TUIUserInfo

Информация о пользователе

| Поле | Тип | Описание |
| --- | --- | --- |
| userId | string | Id пользователя |
| userName | string | Имя пользователя |
| avatarUrl | string | Аватар пользователя |
| userRole | [TUIRole](/document/product/647/54876#ca95b9a1-9ce7-4f90-9d05-caef5616592d) | Роль пользователя |
| hasAudioStream | boolean | Есть ли потоки аудио |
| hasVideoStream | boolean | Есть ли потоки видео |
| hasScreenStream | boolean | Есть ли поток общего доступа к экрану |

### TUIMessage

Информация о сообщении

| Поле | Тип | Описание |
| --- | --- | --- |
| messageId | string | Id сообщения |
| message | string | Сообщение |
| timestamp | number | Информация о временной метке, точность до секунд |
| userId | string | Id пользователя |
| userName | string | Имя пользователя |
| avatarUrl | string | Аватар пользователя |

### TUIRequest

Информация о запросе

| Поле | Тип | Описание |
| --- | --- | --- |
| requestAction | [TUIRequestAction](/document/product/647/54876#e2746642-b1ff-453c-bb41-ca4c64c75566) | Тип запроса |
| timestamp | number | Время инициирования запроса |
| requestId | string | Id запроса. В версиях v1.0.2 и выше requestId имеет тип string; в версиях v1.0.0 и v1.0.1 requestId имеет тип number; |
| userId | string | Id пользователя, инициирующего запрос |
| content | string | Другое содержание |

### TUIRequestCallback

Информация об обратном вызове запроса

| Поле | Тип | Описание |
| --- | --- | --- |
| requestCallbackType | [TUIRequestCallbackType](/document/product/647/54876#a0211e22-30e2-4b3a-bc89-1cf1aa816695) | Тип обратного вызова запроса, одобрение/отклонение/отмена/истечение времени/ошибка |
| requestId | string | Id запроса. В версиях v1.0.2 и выше requestId имеет тип string; в версиях v1.0.0 и v1.0.1 requestId имеет тип number; |
| userId | string | Id пользователя |
| code | number | Код ответа на запрос |
| message | string | Дополнительное описание статуса запроса |

### TUISeatInfo

Информация о позиции микрофона

| Поле | Тип | Описание |
| --- | --- | --- |
| index | number | Номер позиции микрофона |
| userId | string | Id пользователя, соответствующего позиции микрофона |
| locked | boolean | Заблокирована ли текущая позиция микрофона |
| videoMuted | boolean | Запрещено ли видео на текущей позиции микрофона |
| audioMuted | boolean | Запрещено ли аудио на текущей позиции микрофона |


---
*Источник: [https://trtc.io/document/54876](https://trtc.io/document/54876)*

---
*Источник (EN): [tuiroomengine-defines.md](./tuiroomengine-defines.md)*

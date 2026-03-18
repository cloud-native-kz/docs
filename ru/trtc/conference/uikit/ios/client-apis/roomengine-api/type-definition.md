# Определение типов

### Определение перечисления

#### TUIRoomDefine

| Тип | Описание |
| --- | --- |
| [TUIRoomType](/document/product/647/54859#RoomType) | Тип комнаты |
| [TUISpeechMode](/document/product/647/54859#55e7dd70-efb6-4d47-a31e-d64f290ab6c1) | Режим управления микрофоном |
| [TUIMediaDevice](/document/product/647/54859#45f8cc27-8bbe-4ed5-bb40-511a08e27477) | Тип медиа-устройства комнаты |
| [TUIRole](/document/product/647/54859#Role) | Тип роли в комнате |
| [TUIVideoQuality](/document/product/647/54859#74d0aadf-0c54-4a05-9e30-f40b427f1402) | Качество видео |
| [TUIAudioQuality](/document/product/647/54859#c079e8f9-62be-4ea2-b740-20658dcec529) | Качество аудио |
| [TUIVideoStreamType](/document/product/647/54859#VideoStreamType) | Тип потока видео |
| [TUIChangeReason](/document/product/647/54859#ChangeReason) | Причина изменения (Причина изменения статуса аудио и видео пользователя: самостоятельное изменение или изменение владельцем/администратором комнаты) |
| [TUICaptureSourceType](/document/product/647/54859#02abd5f6-ef70-4636-9ff5-fd331baac4f5) | Тип источника захвата при совместном использовании экрана |
| [TUIRequestAction](/document/product/647/54859#RequestAction) | Тип запроса |

#### TUICommonDefine

| Тип | Описание |
| --- | --- |
| [TUINetworkQuality](/document/product/647/54859#NetworkQuality) | Качество сети |

### Общие структуры

#### TUIRoomDefine

| Тип | Описание |
| --- | --- |
| [TUIRoomInfo](/document/product/647/54859#RoomInfo) | Данные комнаты |
| [TUILoginUserInfo](/document/product/647/54859#83093ad1-7671-4f9f-aada-3c74d5006c75) | Информация для входа пользователя |
| [TUIUserInfo](/document/product/647/54859#UserInfo) | Информация пользователя в комнате |
| [TUISeatInfo](/document/product/647/54859#SeatInfo) | Информация о месте в комнате |
| [TUISeatLockParams](/document/product/647/54859#080212f8-d6ce-4430-b745-2fdd5ef8c330) | Параметры операции блокировки места |
| [TUIUserVoiceVolume](/document/product/647/54859#UserVoiceVolume) | Громкость голоса пользователя в комнате |
| [TUIRequest](/document/product/647/54859#Request) | Сигнальный запрос |
| [TUIShareTarget](/document/product/647/54859#200329d6-b424-4bec-b9a1-7e6b7f8ea580) | Информация об источнике захвата при совместном использовании экрана |

#### TUICommonDefine

| Тип | Описание |
| --- | --- |
| [TUINetworkInfo](/document/product/647/54859#NetworkInfo) | Информация о качестве сети |
| [TUIMessage](/document/product/647/54859#Message) | Сообщение |

### TUIRoomType

Тип комнаты

| Перечисление | Значение | Описание |
| --- | --- | --- |
| TUIRoomTypeConference | 1 | Комната типа конференция, подходит для сценариев конференций и образования, в этой комнате можно включить свободную речь, запрос на выступление, режимы прямого эфира и т. д. |
| TUIRoomTypeLivingRoom | 2 | Комната типа прямая трансляция, подходит для сценариев трансляции, в этой комнате можно включить свободную речь, режим управления микрофоном, и места в этой комнате пронумерованы. |

### TUISpeechMode

Режим управления микрофоном

| Перечисление | Значение | Описание |
| --- | --- | --- |
| TUISpeechModeFreeToSpeak | 1 | Режим свободной речи. |
| TUISpeechModeApplyToSpeak | 2 | Режим запроса на выступление. (Действует только в комнате типа конференция) |
| TUISpeechModeApplySpeakAfterTakingSeat | 3 | Режим прямого эфира. |

### TUIMediaDevice

Тип медиа-устройства комнаты

| Перечисление | Значение | Описание |
| --- | --- | --- |
| TUIMediaDeviceMicrophone | 1 | Микрофон |
| TUIMediaDeviceCamera | 2 | Камера |
| TUIMediaDeviceApplyScreenSharing | 3 | Совместное использование экрана |

### TUIRole

Типы ролей в комнате

| Перечисление | Значение | Описание |
| --- | --- | --- |
| TUIRoleRoomOwner | 0 | Владелец комнаты, обычно относится к создателю комнаты, обладает наивысшим уровнем прав в комнате |
| TUIRoleAdministrator | 1 | Администратор комнаты |
| TUIRoleGeneralUser | 2 | Обычный участник комнаты |

### TUIVideoQuality

Качество видео

| Перечисление | Значение | Описание |
| --- | --- | --- |
| TUIVideoQuality360P | 1 | Низкое качество 360P |
| TUIVideoQuality540P | 2 | Стандартное качество 540P |
| TUIVideoQuality720P | 3 | Высокое качество 720P |
| TUIVideoQuality1080P | 4 | Ультра-четкое 1080P |

### TUIAudioQuality

Качество аудио

| Перечисление | Значение | Описание |
| --- | --- | --- |
| TUIAudioQualitySpeech | 0 | Режим речи |
| TUIAudioQualityDefault | 1 | Режим по умолчанию |
| TUIAudioQualityMusic | 2 | Режим музыки |

### TUIVideoStreamType

Тип потока видео

| Перечисление | Значение | Описание |
| --- | --- | --- |
| TUIVideoStreamTypeCameraStream | 0 | Высокачественный поток видео с камеры |
| TUIVideoStreamTypeScreenStream | 1 | Поток видео совместного использования экрана |
| TUIVideoStreamTypeCameraStreamLow | 2 | Низкокачественный поток видео с камеры |

### TUIChangeReason

Причина изменения (Причина изменения статуса аудио и видео пользователя: самостоятельное изменение или изменение владельцем/администратором комнаты)

| Перечисление | Значение | Описание |
| --- | --- | --- |
| TUIChangeReasonBySelf | 0 | Самостоятельная операция |
| TUIChangeReasonByAdmin | 1 | Операция владельца комнаты или администратора |

### TUICaptureSourceType

Тип источника захвата при совместном использовании экрана

| Перечисление | Значение | Описание |
| --- | --- | --- |
| TUICaptureSourceTypeUnknown | -1 | Неопределено |
| TUICaptureSourceTypeWindow | 0 | Окно |
| TUICaptureSourceTypeScreen | 1 | Экран |

### TUIRequestAction

Тип запроса

| Перечисление | Значение | Описание |
| --- | --- | --- |
| TUIRequestActionInvalidAction | 0 | Неверный запрос |
| TUIRequestActionOpenRemoteCamera | 1 | Запрос открыть камеру удаленного пользователя |
| TUIRequestActionOpenRemoteMicrophone | 2 | Запрос открыть микрофон удаленного пользователя |
| TUIRequestActionConnectOtherRoom | 3 | Запрос подключиться к другой комнате |
| TUIRequestActionTakeSeat | 4 | Запрос на прямой эфир |
| TUIRequestActionRemoteUserOnSeat | 5 | Запрос удаленному пользователю на прямой эфир |
| TUIRequestActionApplyToAdminToOpenLocalCamera | 6 | Запрос администратору открыть локальную камеру |
| TUIRequestActionApplyToAdminToOpenLocalMicrophone | 7 | Запрос администратору открыть локальный микрофон |

### TUINetworkQuality

Качество сети

| Перечисление | Значение | Описание |
| --- | --- | --- |
| TUINetworkQualityUnknown | 0 | Неопределено |
| TUINetworkQualityExcellent | 1 | Текущая сеть отличная |
| TUINetworkQualityGood | 2 | Текущая сеть хорошая |
| TUINetworkQualityPoor | 3 | Текущая сеть средняя |
| TUINetworkQualityBad | 4 | Текущая сеть плохая |
| TUINetworkQualityVeryBad | 5 | Текущая сеть очень плохая |
| TUINetworkQualityDown | 6 | Текущая сеть не соответствует минимальным требованиям TRTC |

### TUIRoomInfo

Информация о комнате

| Поле | Тип | Описание |
| --- | --- | --- |
| roomId | NSString * | ID комнаты |
| roomType | [TUIRoomType](/document/product/647/54859#RoomType) | Тип комнаты |
| ownerId | NSString * | ID хоста, по умолчанию это создатель комнаты (только для чтения) |
| name | NSString * | Имя комнаты, по умолчанию это ID комнаты |
| speechMode | [TUISpeechMode](/document/product/647/54859#55e7dd70-efb6-4d47-a31e-d64f290ab6c1) | Режим управления микрофоном |
| createTime | NSUInteger | Время создания комнаты (только для чтения) |
| memberCount | NSInteger | Количество участников в комнате (только для чтения) |
| maxSeatCount | NSUInteger | Максимальное количество мест с микрофоном (поддерживается только при входе и создании комнаты) |
| isCameraDisableForAllUser | BOOL | Отключить открытие камеры (опционально при создании комнаты), значение по умолчанию: false |
| isMicrophoneDisableForAllUser | BOOL | Отключить открытие микрофона (опционально при создании комнаты), значение по умолчанию: false |
| isMessageDisableForAllUser | BOOL | Отключить отправку сообщений (опционально при создании комнаты), значение по умолчанию: false |
| enableCDNStreaming | BOOL | Включить прямую трансляцию CDN (опционально при создании комнаты, для комнат трансляции), значение по умолчанию: false |
| cdnStreamDomain | NSString* | Домен для прямой трансляции (опционально при создании комнаты, для комнат трансляции), значение по умолчанию: пусто |

### TUILoginUserInfo

Информация для входа пользователя

| Поле | Тип | Значение |
| --- | --- | --- |
| userId | NSString * | ID пользователя |
| userName | NSString * | Имя пользователя |
| avatarUrl | NSString * | URL аватара пользователя |

### TUIUserInfo

Информация пользователя в комнате

| Поле | Тип | Описание |
| --- | --- | --- |
| userId | NSString * | ID пользователя |
| userName | NSString * | Имя пользователя |
| avatarUrl | NSString * | URL аватара пользователя |
| userRole | [TUIRole](/document/product/647/54859#Role) | Тип роли пользователя |
| hasAudioStream | BOOL | Наличие аудиопотока, значение по умолчанию: false |
| hasVideoStream | BOOL | Наличие видеопотока, значение по умолчанию: false |
| hasScreenStream | BOOL | Наличие потока совместного использования экрана, значение по умолчанию: false |

### TUISeatInfo

Информация о месте в комнате

| Поле | Тип | Описание |
| --- | --- | --- |
| index | NSInteger | Номер места с микрофоном |
| userId | NSString * | ID пользователя |
| isLocked | BOOL | Заблокировано ли место с микрофоном, значение по умолчанию: false |
| isVideoLocked | BOOL | Запрещено ли открывать камеру на этом месте, значение по умолчанию: false |
| isAudioLocked | BOOL | Запрещено ли открывать микрофон на этом месте, значение по умолчанию: false |

### TUISeatLockParams

Параметры операции блокировки места

| Поле | Тип | Значение |
| --- | --- | --- |
| lockSeat | BOOL | Заблокировать место с микрофоном, значение по умолчанию: false |
| lockVideo | BOOL | Заблокировать камеру на месте с микрофоном, значение по умолчанию: false |
| lockAudio | BOOL | Заблокировать микрофон на месте с микрофоном, значение по умолчанию: false |

### TUIUserVoiceVolume

Громкость голоса пользователя в комнате

| Поле | Тип | Описание |
| --- | --- | --- |
| userId | NSString * | ID пользователя |
| volume | NSUInteger | Размер громкости, диапазон значений 0 - 100 |

### TUIRequest

Сигнальный запрос

| Поле | Тип | Описание |
| --- | --- | --- |
| requestId | NSString * | ID запроса |
| requestAction | [TUIRequestAction](/document/product/647/54859#RequestAction) | Тип запроса |
| userId | NSString * | ID пользователя |
| content | NSString * | Содержание сигнала |
| timestamp | NSUInteger | Временная метка |

### TUIShareTarget

Информация об источнике захвата при совместном использовании экрана

| Поле | Тип | Описание |
| --- | --- | --- |
| targetId | NSString * | ID источника захвата, для окон это поле представляет ID окна; для экранов это поле представляет ID дисплея |
| sourceType | [TUICaptureSourceType](/document/product/647/54859#02abd5f6-ef70-4636-9ff5-fd331baac4f5) | Тип источника захвата |
| sourceName | NSString * | Имя источника захвата |
| thumbnailImage | TUIImage * | Эскиз |
| iconImage | TUIImage * | Значок |
| extInfo | NSDictionary * | Расширенная информация окна |

### TUINetworkInfo

Информация о качестве сети

| Поле | Тип | Описание |
| --- | --- | --- |
| userId | NSString * | ID пользователя |
| quality | [TUINetworkQuality](/document/product/647/54859#NetworkQuality) | Качество сети |
| upLoss | uint32_t | Частота потери пакетов в восходящем направлении |
| downLoss | uint32_t | Частота потери пакетов в нисходящем направлении |
| delay | uint32_t | Задержка сети |

### TUIMessage

Сообщение

| Поле | Тип | Описание |
| --- | --- | --- |
| messageId | NSString * | ID сообщения |
| message | NSString * | Текст сообщения |
| timestamp | uint64_t | Время сообщения |
| userId | NSString * | Отправитель сообщения |
| userName | NSString * | Псевдоним отправителя сообщения |
| avatarUrl | NSString * | Аватар отправителя сообщения |


---
*Источник: [https://trtc.io/document/54859](https://trtc.io/document/54859)*

---
*Источник (EN): [type-definition.md](./type-definition.md)*

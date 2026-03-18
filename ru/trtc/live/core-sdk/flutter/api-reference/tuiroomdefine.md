# TUIRoomDefine

### Определения перечислений

#### TUIRoomDefine

| Тип | Описание |
| --- | --- |
| [TUIRoomType](https://www.tencentcloud.com/document/product/647/67259#RoomType) | Тип комнаты |
| [TUISeatMode](https://www.tencentcloud.com/document/product/647/67259#TUISeatMode) | Режим микрофона |
| [TUIMediaDevice](https://www.tencentcloud.com/document/product/647/67259#45f8cc27-8bbe-4ed5-bb40-511a08e27477) | Тип медиа-устройства в комнате |
| [TUIRole](https://www.tencentcloud.com/document/product/647/67259#Role) | Тип роли в комнате |
| [TUIVideoQuality](https://www.tencentcloud.com/document/product/647/67259#74d0aadf-0c54-4a05-9e30-f40b427f1402) | Качество видео |
| [TUIAudioQuality](https://www.tencentcloud.com/document/product/647/67259#c079e8f9-62be-4ea2-b740-20658dcec529) | Качество аудио |
| [TUIVideoStreamType](https://www.tencentcloud.com/document/product/647/67259#VideoStreamType) | Тип видеопотока |
| [TUIChangeReason](https://www.tencentcloud.com/document/product/647/67259#ChangeReason) | Причина изменения (причина изменения статуса аудио/видео пользователя: инициативное действие или изменение владельцем комнаты или администратором) |
| [TUICaptureSourceType](https://www.tencentcloud.com/document/product/647/67259#02abd5f6-ef70-4636-9ff5-fd331baac4f5) | Тип источника захвата при совместном использовании экрана |
| [TUIRequestAction](https://www.tencentcloud.com/document/product/647/67259#RequestAction) | Тип запроса |
| [TUIResolutionMode](https://www.tencentcloud.com/document/product/647/67259#TUIResolutionMode) | Режим разрешения (альбомная или портретная ориентация) |
| [TUIUserInfoModifyFlag](https://www.tencentcloud.com/document/product/647/67259#TUIUserInfoModifyFlag) | Тип модификации информации пользователя |

#### TUICommonDefine

| Тип | Описание |
| --- | --- |
| [TUIError](https://www.tencentcloud.com/document/product/647/67259#NetworkQuality) | Коды ошибок |
| [TUINetworkQuality](https://www.tencentcloud.com/document/product/647/67259#960e26d8-5853-4903-8174-57d6e7f225a3) | Качество сети |
| [TUIExtensionType](https://www.tencentcloud.com/document/product/647/67259#55ea0b2e-7c8d-4217-a78c-2d447aa72d08) | Тип плагина |

### Общие структуры

#### TUIRoomDefine

| Тип | Описание |
| --- | --- |
| [TUIRoomInfo](https://www.tencentcloud.com/document/product/647/67259#RoomInfo) | Информация о комнате |
| [TUILoginUserInfo](https://www.tencentcloud.com/document/product/647/67259#83093ad1-7671-4f9f-aada-3c74d5006c75) | Информация входа пользователя |
| [TUIUserInfo](https://www.tencentcloud.com/document/product/647/67259#UserInfo) | Информация о пользователе в комнате |
| [TUISeatInfo](https://www.tencentcloud.com/document/product/647/67259#SeatInfo) | Информация о местоположении микрофона в комнате |
| [TUISeatLockParams](https://www.tencentcloud.com/document/product/647/67259#080212f8-d6ce-4430-b745-2fdd5ef8c330) | Параметры блокировки местоположения микрофона |
| [TUIUserVoiceVolume](https://www.tencentcloud.com/document/product/647/67259#UserVoiceVolume) | Громкость пользователя в комнате |
| [TUIRequest](https://www.tencentcloud.com/document/product/647/67259#Request) | Сигнальный запрос |
| [TUIActionCallback](https://www.tencentcloud.com/document/product/647/67259#TUIActionCallback) | Обратный вызов операции пользователя |
| [TUIPlayCallback](https://www.tencentcloud.com/document/product/647/67259#TUIPlayCallback) | Обратный вызов воспроизведения видео |
| [TUIRequestCallback](https://www.tencentcloud.com/document/product/647/67259#TUIRequestCallback) | Обратный вызов запроса пользователя |
| [TUIUserListResult](https://www.tencentcloud.com/document/product/647/67259#TUIUserListResult) | Информация о списке пользователей |
| [TUIUserVoiceVolume](https://www.tencentcloud.com/document/product/647/67259#TUIUserVoiceVolume) | Информация о громкости пользователя |
| [TUIValueCallBack<T>](https://www.tencentcloud.com/document/product/647/67259#TUIValueCallBack<T>) | Обратный вызов с возвращаемым значением (T) |
| [TUIRoomVideoEncoderParams](https://www.tencentcloud.com/document/product/647/67259#TUIVideoEncoderParams) | Параметры видеокодировщика |
| [TUIEnterRoomOptions](https://www.tencentcloud.com/document/product/647/67259#b27a2140-db19-4e74-b537-dde71f0a14b2) | Параметры входа в комнату |

#### TUICommonDefine

| Тип | Описание |
| --- | --- |
| [TUINetwork](https://www.tencentcloud.com/document/product/647/67259#NetworkInfo) | Информация о качестве сети |
| [TUIMessage](https://www.tencentcloud.com/document/product/647/67259#Message) | Сообщение |
| [TUIImageBuffer](https://www.tencentcloud.com/document/product/647/67259#046c7dbf-4a6c-4367-a074-2186c2fa9632) | Информация об изображении |

### TUIRoomType

Тип комнаты

| Перечисление | Значение | Описание |
| --- | --- | --- |
| conference | 1 | Комната типа конференции, подходит для собраний и образовательных целей. В этой комнате пользователи могут выбирать различные режимы, такие как режим свободной речи, подача заявки на выступление и микрофон на микрофоне |
| livingRoom | 2 | Комната типа прямой трансляции, подходит для сценариев прямой трансляции. В этой комнате пользователи могут свободно говорить, а комната использует режим управления местоположением микрофона, где каждое местоположение микрофона имеет номер |

## TUISeatMode

Режим микрофона

| Перечисление | Значение | Описание |
| --- | --- | --- |
| freeToTake | 1 | Режим свободного присоединения к микрофону, аудитория может свободно присоединяться к микрофону без подачи заявки |
| applyToTake | 2 | Режим подачи заявки на микрофон, аудитория нуждается в одобрении владельца комнаты или администратора для присоединения к микрофону |

### TUIMediaDevice

Тип медиа-устройства в комнате

| Перечисление | Значение | Описание |
| --- | --- | --- |
| microphone | 1 | Микрофон |
| camera | 2 | Камера |
| screen | 3 | Совместное использование экрана |

### TUIRole

Тип роли в комнате

| Перечисление | Значение | Описание |
| --- | --- | --- |
| roomOwner | 0 | Владелец комнаты. Обычно относится к создателю комнаты и владельцу высшего уровня разрешений в комнате |
| administrator | 1 | Администратор комнаты |
| generalUser | 2 | Обычный член в комнате |

### TUIVideoQuality

Качество видео

| Перечисление | Значение | Описание |
| --- | --- | --- |
| videoQuality_360P | 1 | Низкое качество 360p |
| videoQuality_540P | 2 | Стандартное качество 540p |
| videoQuality_720P | 3 | HD 720p |
| videoQuality_1080P | 4 | Ultra HD 1080p |

### TUIAudioQuality

Качество аудио

| Перечисление | Значение | Описание |
| --- | --- | --- |
| audioProfileSpeech | 0 | Режим голоса |
| audioProfileDefault | 1 | Режим по умолчанию |
| audioProfileMusic | 2 | Режим музыки |

### TUIVideoStreamType

Тип видеопотока

| Перечисление | Значение | Описание |
| --- | --- | --- |
| cameraStream | 0 | Видеопоток HD камеры |
| screenStream | 1 | Видеопоток совместного использования экрана |
| cameraStreamLow | 2 | Видеопоток камеры низкого качества |

### TUIChangeReason

Причина изменения (причина изменения статуса аудио/видео пользователя: инициативное действие или изменение владельцем комнаты или администратором)

| Перечисление | Значение | Описание |
| --- | --- | --- |
| changedBySelf | 0 | Операция пользователя |
| changedByAdmin | 1 | Операция владельца комнаты или администратора |

### TUICaptureSourceType

Тип источника захвата при совместном использовании экрана

| Перечисление | Значение | Описание |
| --- | --- | --- |
| unknown | -1 | Не определено |
| window | 0 | Окно |
| screen | 1 | Экран |

### TUIRequestAction

Тип запроса

| Перечисление | Значение | Описание |
| --- | --- | --- |
| invalidAction | 0 | Недействительный запрос |
| requestToOpenRemoteCamera | 1 | Запрос на включение камеры удаленного пользователя |
| requestToOpenRemoteMicrophone | 2 | Запрос на включение микрофона удаленного пользователя |
| requestToConnectOtherRoom | 3 | Запрос на подключение к другой комнате |
| requestToTakeSeat | 4 | Запрос на присоединение к микрофону |
| requestRemoteUserOnSeat | 5 | Запрос удаленному пользователю присоединиться к микрофону |
| applyToAdminToOpenLocalCamera | 6 | Запрос администратору на включение локальной камеры |
| applyToAdminToOpenLocalMicrophone | 7 | Запрос администратору на включение локального микрофона |

### TUIResolutionMode

| Перечисление | Значение | Описание |
| --- | --- | --- |
| landscape | 0 | Альбомная ориентация |
| portrait | 1 | Портретная ориентация |

### TUIUserInfoModifyFlag

| Перечисление | Значение | Описание |
| --- | --- | --- |
| none | 0x00 | Пусто, указывает на отсутствие изменений |
| userRole | 0x01 << 0 | Роль пользователя |
| nameCard | 0x01 << 1 | Никнейм в комнате |

### TUIError

Коды ошибок

| Перечисление | Значение | Описание |
| --- | --- | --- |
| success | 0 | Операция выполнена успешно |
| errFailed | -1 | Общая ошибка, еще не классифицированная |
| errFreqLimit | -2 | Запрос был частотно ограничен, повторите попытку позже |
| errRepeatOperation | -3 | Дублированная операция, проверьте, повторяется ли ваш вызов API |
| errSDKAppIDNotFound | -1000 | SDKAppID не найден, пожалуйста, подтвердите информацию приложения в [Консоли TRTC](https://console.trtc.io/app) |
| errInvalidParameter | -1001 | Во время вызова API было передано недопустимое значение параметра |
| errSdkNotInitialized | -1002 | SDK не инициализирован |
| errPermissionDenied | -1003 | Отсутствуют разрешения на выполнение операции |
| errRequirePayment | -1004 | Эта функция требует дополнительного пакета |
| errCameraStartFailed | -1100 | Не удалось включить камеру |
| errCameraNotAuthorized | -1101 | Камера не авторизована |
| errCameraOccupy | -1102 | Камера используется |
| errCameraDeviceEmpty | -1103 | Нет доступного устройства камеры |
| errMicrophoneStartFailed | -1104 | Не удалось открыть микрофон |
| errMicrophoneNotAuthorized | -1105 | Микрофон не авторизован |
| errMicrophoneOccupy | -1106 | Микрофон занят |
| errMicrophoneDeviceEmpty | -1107 | Нет доступного устройства микрофона |
| errGetScreenSharingTargetFailed | -1108 | Не удалось получить объекты совместного использования экрана |
| errStartScreenSharingFailed | -1109 | Не удалось включить совместное использование экрана |
| errRoomIdNotExist | -2100 | Комната не существует при входе, она может быть растворена |
| errOperationInvalidBeforeEnterRoom | -2101 | Вам необходимо войти в комнату для использования этой функции |
| errExitNotSupportedForRoomOwner | -2102 | Владелец комнаты не может выполнить процедуру выхода, тип конференц-комнаты: сначала передайте владельца, затем выходите. Тип комнаты LivingRoom: владелец может только растворить комнату |
| errOperationNotSupportedInCurrentRoomType | -2103 | Эта операция не поддерживается при текущем типе комнаты |
| errRoomIdInvalid | -2105 | Недопустимое создание ID комнаты, пользовательский ID должен быть печатаемыми символами ASCII (0x20-0x7e), максимум 48 байт |
| errRoomIdOccupied | -2106 | ID комнаты уже используется, пожалуйста, выберите другой ID комнаты |
| errRoomNameInvalid | -2107 | Недопустимое имя комнаты, максимальная длина 30 байт, кодировка символов должна быть UTF-8, если она включает китайские символы |
| errAlreadyInOtherRoom | -2108 | Текущий пользователь уже находится в другой комнате и должен выйти перед входом в новую комнатуОдин экземпляр RoomEngine поддерживает только входящего пользователя в одну комнату. Для входа в другую комнату, пожалуйста, выходите или используйте новый экземпляр RoomEngine |
| errUserNotExist | -2200 | Пользователь не существует. |
| errUserNotEntered | -2201 | Пользователь не находится в текущей комнате |
| errUserNeedOwnerPermission | -2300 | Требуются привилегии владельца комнаты для операции |
| errUserNeedAdminPermission | -2301 | Требуются привилегии владельца комнаты или администратора для операции |
| errRequestNoPermission | -2310 | Отсутствуют разрешения для сигнального запроса, например отмена приглашения, инициированного другим пользователем |
| errRequestIdInvalid | -2311 | ID сигнального запроса недействителен или уже был обработан |
| errMaxSeatCountLimit | -2340 | Ограничение максимального количества местоположений микрофона превышает квоту пакета |
| errAlreadyInSeat | -2341 | Текущий пользователь уже находится на местоположении микрофона |
| errSeatOccupied | -2342 | Текущее местоположение микрофона уже занято |
| errSeatLocked | -2343 | Текущее местоположение микрофона заблокировано |
| errSeatIndexNotExist | -2344 | Номер местоположения микрофона не существует |
| errUserNotInSeat | -2345 | Текущий пользователь не находится на микрофоне |
| errAllSeatOccupied | -2346 | Количество пользователей на микрофоне полное |
| errOpenMicrophoneNeedSeatUnlock | -2360 | Текущее местоположение микрофона заблокировано для аудио |
| errOpenMicrophoneNeedPermissionFromAdmin | -2361 | Вам необходимо запросить разрешение у владельца комнаты или администратора для использования микрофона |
| errOpenCameraNeedSeatUnlock | -2370 | Текущее местоположение микрофона заблокировано для видео, необходимо разблокировать владельцем для использования камеры |
| errOpenCameraNeedPermissionFromAdmin | -2371 | Вам необходимо запросить разрешение у владельца комнаты или администратора для использования камеры |
| errSendMessageDisabledForAll | -2380 | Все члены отключены в текущей комнате |
| errSendMessageDisabledForCurrent | -2381 | Вы отключены в текущей комнате |

### TUINetworkQuality

Качество сети

| Перечисление | Значение | Описание |
| --- | --- | --- |
| qualityUnknown | 0 | Не определено |
| qualityExcellent | 1 | Текущая сеть очень хорошая |
| qualityGood | 2 | Текущая сеть довольно хорошая |
| qualityPoor | 3 | Текущая сеть средняя |
| qualityBad | 4 | Текущая сеть плохая |
| qualityVeryBad | 5 | Текущая сеть очень плохая |
| qualityDown | 6 | Текущая сеть не соответствует минимальным требованиям TRTC |

### TUIRoomInfo

Информация о комнате

| Поле | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| roomType | [TUIRoomType](https://www.tencentcloud.com/document/product/647/67259#RoomType) | Тип комнаты |
| ownerId | String | ID хоста. По умолчанию создатель комнаты (только для чтения) |
| name | String | Имя комнаты. По умолчанию ID комнаты |
| isSeatEnabled | bool | Включено ли управление местоположением микрофона |
| seatMode | [TUISeatMode](https://www.tencentcloud.com/document/product/647/67259#TUISeatMode) | Режим микрофона (вступает в силу только при включении управления местоположением микрофона) |
| createTime | int | Время создания комнаты (только для чтения) |
| memberCount | int | Количество членов в комнате (только для чтения) |
| maxSeatCount | int | Максимальное количество микрофонов (может быть установлено только перед входом в комнату или при создании комнаты) |
| isCameraDisableForAllUser | bool | Отключена ли камера (опциональный параметр при создании комнаты). Значение по умолчанию: false |
| isMicrophoneDisableForAllUser | bool | Отключен ли микрофон (опциональный параметр при создании комнаты). Значение по умолчанию: false |
| isMessageDisableForAllUser | bool | Отключена ли отправка сообщений (опциональный параметр при создании комнаты). Значение по умолчанию: false |
| enableCDNStreaming | bool | Включена ли трансляция CDN (опциональный параметр при создании комнаты, используется в живых комнатах). Значение по умолчанию: false |
| cdnStreamDomain | String | Доменное имя трансляции (опциональный параметр при создании комнаты, используется в живых комнатах). Значение по умолчанию: пусто |
| password | String | Пароль комнаты |

### TUILoginUserInfo

Информация входа пользователя

| Поле | Тип | Значение |
| --- | --- | --- |
| userId | String | ID пользователя |
| userName | String | Имя пользователя |
| avatarUrl | String | URL фото профиля пользователя |
| customInfo | Map<String, String> | Пользовательская информация |

### TUIUserInfo

Информация о пользователе в комнате

| Поле | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| userName | String | Имя пользователя |
| nameCard | String | Никнейм в комнате |
| avatarUrl | String | URL фото профиля пользователя |
| userRole | [TUIRole](https://www.tencentcloud.com/document/product/647/67259#Role) | Тип роли пользователя |
| hasAudioStream | bool | Наличие аудиопотока. Значение по умолчанию: false |
| hasVideoStream | bool | Наличие видеопотока. Значение по умолчанию: false |
| hasScreenStream | bool | Наличие потока совместного использования экрана. Значение по умолчанию: false |
| customInfo | Map<String, String>? | Пользовательская информация члена комнаты |
| isMessageDisabled | bool | Отключен ли звук |

### TUISeatInfo

Информация о местоположении микрофона в комнате

| Поле | Тип | Описание |
| --- | --- | --- |
| index | int | Серийный номер местоположения микрофона |
| userId | String | ID пользователя |
| userName | String | Имя пользователя |
| nameCard | String | Никнейм в комнате |
| avatarUrl | String | URL фото профиля пользователя |
| isLocked | bool | Заблокировано ли местоположение микрофона. Значение по умолчанию: false |
| isVideoLocked | bool | Запрещено ли открывать камеру на местоположении микрофона. Значение по умолчанию: false |
| isAudioLocked | bool | Запрещено ли открывать микрофон на местоположении микрофона. Значение по умолчанию: false |
| userName | String | Никнейм пользователя |
| avatarUrl | String | URL фото профиля пользователя |

### TUISeatLockParams

Параметры блокировки местоположения микрофона

| Поле | Тип | Значение |
| --- | --- | --- |
| lockSeat | bool | Заблокировать местоположение микрофона. По умолчанию false |
| lockVideo | bool | Заблокировать камеру местоположения микрофона. По умолчанию false |
| lockAudio | bool | Заблокировать микрофон местоположения микрофона. По умолчанию false |

### TUIUserVoiceVolume

Громкость пользователя в комнате

| Поле | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| volume | int | Громкость. Используется для передачи размера громкости всех говорящих пользователей, диапазон значений 0-100 |

### TUIRequest

Сигнальный запрос

| Поле | Тип | Описание |
| --- | --- | --- |
| requestId | String | ID запроса |
| requestAction | [TUIRequestAction](https://www.tencentcloud.com/document/product/647/67259#RequestAction) | Тип запроса |
| userId | String | ID пользователя |
| userName | String | Имя пользователя |
| nameCard | String | Никнейм в комнате |
| avatarUrl | String | URL фото профиля пользователя |
| content | String | Содержание сигнала |
| timestamp | int | Временная метка |
| userName | String | Никнейм пользователя |
| avatarUrl | String | URL фото профиля пользователя |

### TUIActionCallback

| Поле | Тип | Описание |
| --- | --- | --- |
| code | [TUIError](https://www.tencentcloud.com/document/product/647/67259#NetworkQuality) | Коды ошибок |
| message | String? | Сообщение об ошибке |

### TUIPlayCallback

| Поле | Тип | Описание |
| --- | --- | --- |
| onPlaying | (String userId) {} | Обратный вызов воспроизведения |
| onLoading | (String userId) {} | Обратный вызов загрузки |
| onPlayError | (String userId, TUIError code, String message) {} | Обратный вызов ошибки воспроизведения |

### TUIRequestCallback

| Поле | Тип | Описание |
| --- | --- | --- |
| onAccepted | (String requestId, String userId) {} | Обратный вызов принятия запроса |
| onRejected | (String requestId, String userId, String message) {} | Обратный вызов отклонения запроса |
| onCancelled | (String requestId, String userId) {} | Обратный вызов отмены запроса |
| onTimeout | (String requestId, String userId) {} | Обратный вызов истечения времени ожидания запроса |
| onError | (String requestId, String userId, TUIError error, String message) {} | Обратный вызов ошибки запроса |

### TUIUserListResult

| Поле | Тип | Описание |
| --- | --- | --- |
| nextSequence | int | Флаг извлечения данных по страницам. Если возвращенное значение nextSequence не равно нулю, используйте возвращенное значение nextSequence для повторного извлечения, пока оно не вернет ноль |
| userInfoList | List<TUIUserInfo> | Список пользователей, возвращенный этим вызовом |

### TUIUserVoiceVolume

| Поле | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| volume | int | Уровень громкости пользователя |

### TUIValueCallBack<T>

| Поле | Тип | Описание |
| --- | --- | --- |
| code | [TUIError](https://www.tencentcloud.com/document/product/647/67259#NetworkQuality) | Коды ошибок |
| message | String? | Сообщение об ошибке |
| data | T? | Возвращаемые данные, пример: если T является TUIUserInfo, тип поля data объекта TUIValueCallBack<TUIUserInfo> является TUIUserInfo |

### TUIRoomVideoEncoderParams

| Поле | Тип | Описание |
| --- | --- | --- |
| videoResolution | TUIVideoQuality | Качество видео |
| resolutionMode | TUIResolutionMode | Режим разрешения |
| fps | int | Частота кадров захвата видео |
| bitrate | int | Целевой битрейт видео |

### TUIEnterRoomOptions

| Поле | Тип | Описание |
| --- | --- | --- |
| password | String | Пароль комна

---
*Источник (EN): [tuiroomdefine.md](./tuiroomdefine.md)*

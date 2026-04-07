# Определение типов

### Определение перечисления

#### TUIRoomDefine

| Тип | Описание |
| --- | --- |
| [TUIRoomType](https://www.tencentcloud.com/document/product/647/57515#RoomType) | Тип комнаты |
| [TUISpeechMode](https://www.tencentcloud.com/document/product/647/57515#SpeechMode) | Режим управления микрофоном |
| [TUIMediaDevice](https://www.tencentcloud.com/document/product/647/57515#MediaDevice) | Тип медиаустройства комнаты |
| [TUIRole](https://www.tencentcloud.com/document/product/647/57515#Role) | Тип роли в комнате |
| [TUIVideoQuality](https://www.tencentcloud.com/document/product/647/57515#VideoQuality) | Качество видео |
| [TUIAudioQuality](https://www.tencentcloud.com/document/product/647/57515#AudioQuality) | Качество аудио |
| [TUIVideoStreamType](https://www.tencentcloud.com/document/product/647/57515#VideoStreamType) | Тип видеопотока |
| [TUIChangeReason](https://www.tencentcloud.com/document/product/647/57515#ChangeReason) | Причина изменения (причина изменения статуса аудио и видео пользователя: самостоятельное изменение или изменение владельцем/администратором комнаты) |
| [TUICaptureSourceType](https://www.tencentcloud.com/document/product/647/57515#CaptureSourceType) | Тип источника захвата при совместном использовании экрана |
| [TUIRequestAction](https://www.tencentcloud.com/document/product/647/57515#RequestAction) | Тип запроса |
| [TUIResolutionMode](https://www.tencentcloud.com/document/product/647/57515#TUIResolutionMode) | Режим разрешения видео (альбомная или портретная ориентация) |

#### TUICommonDefine

| Тип | Описание |
| --- | --- |
| [TUIError](https://www.tencentcloud.com/document/product/647/57515#TUIError) | Код ошибки |
| [TUINetworkQuality](https://www.tencentcloud.com/document/product/647/57515#NetworkQuality) | Качество сети |

### Общие структуры

#### TUIRoomDefine

| Тип | Описание |
| --- | --- |
| [TUIRoomInfo](https://www.tencentcloud.com/document/product/647/57515#RoomInfo) | Данные комнаты |
| [TUILoginUserInfo](https://www.tencentcloud.com/document/product/647/57515#LoginUserInfo) | Информация о входе пользователя |
| [TUIUserInfo](https://www.tencentcloud.com/document/product/647/57515#UserInfo) | Информация о пользователе в комнате |
| [TUISeatInfo](https://www.tencentcloud.com/document/product/647/57515#SeatInfo) | Информация о месте в комнате |
| [TUISeatLockParams](https://www.tencentcloud.com/document/product/647/57515#SeatLockParams) | Параметры блокировки места |
| [TUIUserVoiceVolume](https://www.tencentcloud.com/document/product/647/57515#UserVoiceVolume) | Громкость пользователя в комнате |
| [TUIRequest](https://www.tencentcloud.com/document/product/647/57515#Request) | Запрос сигнализации |
| [TUIActionCallback](https://www.tencentcloud.com/document/product/647/57515#TUIActionCallback) | Обратный вызов операции пользователя |
| [TUIPlayCallback](https://www.tencentcloud.com/document/product/647/57515#TUIPlayCallback) | Обратный вызов воспроизведения видео |
| [TUIRequestCallback](https://www.tencentcloud.com/document/product/647/57515#TUIRequestCallback) | Обратный вызов запроса пользователя |
| [TUIUserListResult](https://www.tencentcloud.com/document/product/647/57515#TUIUserListResult) | Информация о списке пользователей |
| [TUIUserVoiceVolume](https://www.tencentcloud.com/document/product/647/57515#TUIUserVoiceVolume) | Информация об уровне громкости пользователя |
| [TUIValueCallBack<T>](https://www.tencentcloud.com/document/product/647/57515#TUIValueCallBack<T>) | Обратный вызов с возвращаемым значением (T) |
| [TUIRoomVideoEncoderParams](https://www.tencentcloud.com/document/product/647/57515#TUIVideoEncoderParams) | Параметры видеокодека |

#### TUICommonDefine

| Тип | Описание |
| --- | --- |
| [TUINetwork](https://www.tencentcloud.com/document/product/647/57515#NetworkInfo) | Информация о качестве сети |
| [TUIMessage](https://www.tencentcloud.com/document/product/647/57515#Message) | Сообщение |
| [TUIImageBuffer](https://www.tencentcloud.com/document/product/647/57515#ImageBuffer) | Информация об изображении |

### TUIRoomType

Тип комнаты

| Перечисление | Значение | Описание |
| --- | --- | --- |
| conference | 1 | Тип конференц-комнаты, подходит для конференций и образовательных сценариев. Эта комната может поддерживать режимы свободной речи, запросов на выступление, трансляции и другие режимы. |
| livingRoom | 2 | Тип комнаты прямой трансляции, подходит для сценариев прямого эфира. Эта комната может поддерживать режимы свободной речи и управления микрофоном, места в этой комнате пронумерованы. |

### TUISpeechMode

Режим управления микрофоном

| Перечисление | Значение | Описание |
| --- | --- | --- |
| freeToSpeak | 1 | Режим свободной речи |
| applyToSpeak | 2 | Режим запроса на выступление. (Эффективно только в комнате типа конференция) |
| applySpeakAfterTakingSeat | 3 | Режим прямой трансляции |

> **Пояснение:** Связь между типом комнаты, режимом управления микрофоном и трансляцией (takeSeat). Тип комнаты. Режим управления микрофоном
> 
> 
> freeToSpeakapplyToSpeakapplySpeakAfterTakingSeatconferenceНе поддерживаетсяНе поддерживаетсяНеобходимо одобрение от владельца/администратора (takeSeat), после одобрения можно говорить с включенными микрофоном/камеройlivingRoomМожно свободно начать трансляциюНе поддерживаетсяНеобходимо одобрение от владельца/администратора (takeSeat), после одобрения можно говорить с включенными микрофоном/камерой

### TUIMediaDevice

Тип медиаустройства комнаты

| Перечисление | Значение | Описание |
| --- | --- | --- |
| microphone | 1 | Микрофон |
| camera | 2 | Камера |
| screen | 3 | Совместное использование экрана |

### TUIRole

Типы ролей в комнате

| Перечисление | Значение | Описание |
| --- | --- | --- |
| roomOwner | 0 | Владелец комнаты. Обычно это создатель комнаты, лицо с наивысшими полномочиями в комнате |
| administrator | 1 | Администратор комнаты |
| generalUser | 2 | Обычный член комнаты |

### TUIVideoQuality

Качество видео

| Перечисление | Значение | Описание |
| --- | --- | --- |
| videoQuality_360P | 1 | Низкое качество 360P |
| videoQuality_540P | 2 | Стандартное качество 540P |
| videoQuality_720P | 3 | Высокое качество 720P |
| videoQuality_1080P | 4 | Очень высокое качество 1080P |

### TUIAudioQuality

Качество аудио

| Перечисление | Значение | Описание |
| --- | --- | --- |
| audioProfileSpeech | 0 | Режим речи |
| audioProfileDefault | 1 | Режим по умолчанию |
| audioProfileMusic | 2 | Режим музыки |

### TUIVideoStreamType

Типы видеопотоков

| Перечисление | Значение | Описание |
| --- | --- | --- |
| cameraStream | 0 | Видеопоток с высоким разрешением с камеры |
| screenStream | 1 | Видеопоток совместного использования экрана |
| cameraStreamLow | 2 | Видеопоток с низким разрешением с камеры |

### TUIChangeReason

Причина изменения (причина изменения статуса аудио и видео пользователя: самостоятельное изменение или изменение владельцем/администратором комнаты)

| Перечисление | Значение | Описание |
| --- | --- | --- |
| changedBySelf | 0 | Самостоятельная операция |
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
| requestToOpenRemoteCamera | 1 | Запрос удаленному пользователю открыть камеру |
| requestToOpenRemoteMicrophone | 2 | Запрос удаленному пользователю открыть микрофон |
| requestToConnectOtherRoom | 3 | Запрос на подключение к другой комнате |
| requestToTakeSeat | 4 | Запрос на начало трансляции |
| requestRemoteUserOnSeat | 5 | Запрос удаленному пользователю начать трансляцию |
| applyToAdminToOpenLocalCamera | 6 | Запрос администратору на открытие локальной камеры |
| applyToAdminToOpenLocalMicrophone | 7 | Запрос администратору на открытие локального микрофона |

### TUIResolutionMode

Режим разрешения видео (альбомная или портретная ориентация)

| Перечисление | Значение | Описание |
| --- | --- | --- |
| landscape | 0 | альбомная ориентация |
| portrait | 1 | портретная ориентация |

### TUIError

Код ошибки

| Перечисление | Значение | Описание |
| --- | --- | --- |
| success | 0 | Операция выполнена успешно |
| errFailed | -1 | Временная неклассифицированная общая ошибка |
| errFreqLimit | -2 | Запрос ограничен, пожалуйста, повторите попытку позже |
| errRepeatOperation | -3 | Повторная операция, пожалуйста, проверьте, не повторяется ли вызов вашего интерфейса |
| errSDKAppIDNotFound | -1000 | SDKAppID не найден, пожалуйста, подтвердите информацию приложения в [консоли TRTC](https://console.tencentcloud.com/trtc/allapp) |
| errInvalidParameter | -1001 | Недопустимые входные параметры при вызове API |
| errSdkNotInitialized | -1002 | SDK не инициализирован |
| errPermissionDenied | -1003 | Нет прав на выполнение операции |
| errRequirePayment | -1004 | Требуется открыть дополнительный пакет для этой функции |
| errCameraStartFailed | -1100 | Ошибка открытия камеры |
| errCameraNotAuthorized | -1101 | Камера не авторизована |
| errCameraOccupy | -1102 | Камера занята |
| errCameraDeviceEmpty | -1103 | В настоящее время нет устройства камеры |
| errMicrophoneStartFailed | -1104 | Ошибка открытия микрофона |
| errMicrophoneNotAuthorized | -1105 | Микрофон не авторизован |
| errMicrophoneOccupy | -1106 | Микрофон занят |
| errMicrophoneDeviceEmpty | -1107 | В настоящее время нет устройства микрофона |
| errGetScreenSharingTargetFailed | -1108 | Ошибка получения целевого объекта совместного использования экрана |
| errStartScreenSharingFailed | -1109 | Ошибка запуска совместного использования экрана |
| errRoomIdNotExist | -2100 | Комната не существует при входе или может быть закрыта |
| errOperationInvalidBeforeEnterRoom | -2101 | Требуется войти в комнату перед использованием этой функции |
| errExitNotSupportedForRoomOwner | -2102 | Владелец комнаты не поддерживает операцию выхода. Для комнат типа конференция: вы можете сначала передать права владельца, затем выйти из комнаты. Для комнат типа гостиная: владелец комнаты может только закрыть комнату |
| errOperationNotSupportedInCurrentRoomType | -2103 | Эта операция не поддерживается в текущем типе комнаты |
| errOperationNotSupportedInCurrentSpeechMode | -2104 | Эта операция не поддерживается в текущем режиме речи |
| errRoomIdInvalid | -2105 | Недопустимое создание ID комнаты, пользовательский ID должен состоять из печатаемых символов ASCII (0x20-0x7e), максимум 48 байт |
| errRoomIdOccupied | -2106 | ID комнаты уже используется, пожалуйста, выберите другой ID комнаты |
| errRoomNameInvalid | -2107 | Недопустимое имя комнаты, имя должно содержать не более 30 байт, кодировка символов должна быть UTF-8, если содержит китайские символы |
| errAlreadyInOtherRoom | -2108 | Текущий пользователь уже находится в другой комнате, вам нужно сначала выйти из комнаты, чтобы присоединиться к новой комнате. Один экземпляр roomEngine поддерживает вход пользователя в одну комнату. Если вы хотите войти в другую комнату, пожалуйста, сначала выйдите из текущей комнаты или используйте новый экземпляр roomEngine |
| errUserNotExist | -2200 | Пользователь не существует |
| errUserNotEntered | -2201 | Пользователь не находится в текущей комнате |
| errUserNeedOwnerPermission | -2300 | Требуются права владельца комнаты для выполнения операции |
| errUserNeedAdminPermission | -2301 | Требуются права владельца комнаты или администратора для выполнения операции |
| errRequestNoPermission | -2310 | Нет прав на запрос сигнализации, например, отмена приглашения, инициированного не вами |
| errRequestIdInvalid | -2311 | Недействительный ID запроса сигнализации или уже обработан |
| errMaxSeatCountLimit | -2340 | Максимальное количество мест превышает лимит пакета |
| errAlreadyInSeat | -2341 | Текущий пользователь уже на месте |
| errSeatOccupied | -2342 | Текущее место уже занято |
| errSeatLocked | -2343 | Текущее место заблокировано |
| errSeatIndexNotExist | -2344 | Номер места не существует |
| errUserNotInSeat | -2345 | Текущий пользователь не на микрофоне |
| errAllSeatOccupied | -2346 | Количество людей на микрофоне заполнено |
| errOpenMicrophoneNeedSeatUnlock | -2360 | Текущее место заблокировано для аудио |
| errOpenMicrophoneNeedPermissionFromAdmin | -2361 | Требуется запрос к владельцу комнаты или администратору на открытие микрофона |
| errOpenCameraNeedSeatUnlock | -2370 | Текущее место заблокировано для видео, владельцу комнаты нужно разблокировать место перед открытием камеры |
| errOpenCameraNeedPermissionFromAdmin | -2371 | Требуется запрос к владельцу комнаты или администратору на открытие камеры |
| errSendMessageDisabledForAll | -2380 | В текущей комнате включена функция отключения звука для всех |
| errSendMessageDisabledForCurrent | -2381 | В текущей комнате вам отключен звук |

### TUINetworkQuality

Качество сети

| Перечисление | Значение | Описание |
| --- | --- | --- |
| qualityUnknown | 0 | Не определено |
| qualityExcellent | 1 | Текущая сеть очень хорошая |
| qualityGood | 2 | Текущая сеть хорошая |
| qualityPoor | 3 | Текущая сеть средняя |
| qualityBad | 4 | Текущая сеть плохая |
| qualityVeryBad | 5 | Текущая сеть очень плохая |
| qualityDown | 6 | Текущая сеть не соответствует минимальным требованиям TRTC |

### TUIRoomInfo

Данные комнаты

| Поле | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| roomType | [TUIRoomType](https://www.tencentcloud.com/document/product/647/57515#RoomType) | Тип комнаты |
| ownerId | String | ID хозяина, по умолчанию это создатель комнаты (только для чтения) |
| name | String | Имя комнаты, по умолчанию это ID комнаты |
| speechMode | [TUISpeechMode](https://www.tencentcloud.com/document/product/647/57515#SpeechMode) | Режим речи комнаты |
| createTime | int | Время создания комнаты (только для чтения) |
| memberCount | int | Количество членов в комнате (только для чтения) |
| maxSeatCount | int | Максимальное количество мест (поддерживается только при входе и создании комнаты) |
| isCameraDisableForAllUser | bool | Запретить открытие камеры (необязательный параметр при создании комнаты). Значение по умолчанию: false |
| isMicrophoneDisableForAllUser | bool | Запретить открытие микрофона (необязательный параметр при создании комнаты). Значение по умолчанию: false |
| isMessageDisableForAllUser | bool | Запретить отправку сообщений (необязательный параметр при создании комнаты). Значение по умолчанию: false |
| enableCDNStreaming | bool | Включить CDN прямую трансляцию (необязательный параметр при создании комнаты, для использования в комнате прямой трансляции). Значение по умолчанию: false |
| cdnStreamDomain | String | Домен для отправки прямого эфира (необязательный параметр при создании комнаты, для использования в комнате прямой трансляции). Значение по умолчанию: пусто |

### TUILoginUserInfo

Информация о входе пользователя

| Поле | Тип | Значение |
| --- | --- | --- |
| userId | String | ID пользователя |
| userName | String | Имя пользователя |
| avatarUrl | String | URL аватара пользователя |
| customInfo | Map<String, String> | Пользовательская информация |

### TUIUserInfo

Информация о пользователе в комнате

| Поле | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| userName | String | Имя пользователя |
| avatarUrl | String | URL аватара пользователя |
| userRole | [TUIRole](https://www.tencentcloud.com/document/product/647/57515#Role) | Тип роли пользователя |
| hasAudioStream | bool | Есть ли аудиопоток. Значение по умолчанию: false |
| hasVideoStream | bool | Есть ли видеопоток. Значение по умолчанию: false |
| hasScreenStream | bool | Есть ли поток совместного использования экрана. Значение по умолчанию: false |

### TUISeatInfo

Информация о месте в комнате

| Поле | Тип | Описание |
| --- | --- | --- |
| index | int | Номер места |
| userId | String | ID пользователя |
| isLocked | bool | Заблокировано ли место. Значение по умолчанию: false |
| isVideoLocked | bool | Запрещено ли открывать камеру на этом месте. Значение по умолчанию: false |
| isAudioLocked | bool | Запрещено ли открывать микрофон на этом месте. Значение по умолчанию: false |

### TUISeatLockParams

Параметры блокировки места

| Поле | Тип | Значение |
| --- | --- | --- |
| lockSeat | bool | Заблокировать место. Значение по умолчанию: false |
| lockVideo | bool | Заблокировать камеру места. Значение по умолчанию: false |
| lockAudio | bool | Заблокировать микрофон места. Значение по умолчанию: false |

### TUIUserVoiceVolume

Громкость пользователя в комнате

| Поле | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| volume | int | Громкость. Используется для передачи громкости всех говорящих пользователей, диапазон значений 0–100 |

### TUIRequest

Запрос сигнализации

| Поле | Тип | Описание |
| --- | --- | --- |
| requestId | String | ID запроса |
| requestAction | [TUIRequestAction](https://www.tencentcloud.com/document/product/647/57515#RequestAction) | Тип запроса |
| userId | String | ID пользователя |
| content | String | Содержание сигнализации |
| timestamp | int | Временная метка |

### TUIActionCallback

| Поле | Тип | Описание |
| --- | --- | --- |
| code | [TUIError](https://www.tencentcloud.com/document/product/647/57515#TUIError) | Код ошибки |
| message | String? | Информация об ошибке |

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
| onTimeout | (String requestId, String userId) {} | Обратный вызов истечения времени запроса |
| onError | (String requestId, String userId, TUIError error, String message) {} | Обратный вызов ошибки запроса |

### TUIUserListResult

| Поле | Тип | Описание |
| --- | --- | --- |
| nextSequence | int | Флаг для получения следующей страницы. Если возвращенный nextSequence не равен нулю, вам нужно использовать возвращенный nextSequence для повторного получения, пока он не вернет 0 |
| userInfoList | List<TUIUserInfo> | Список пользователей, возвращаемый этим вызовом |

### TUIUserVoiceVolume

| Поле | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| volume | int | Размер громкости пользователя |

### TUIValueCallBack<T>

| Поле | Тип | Описание |
| --- | --- | --- |
| code | [TUIError](https://www.tencentcloud.com/document/product/647/57515#TUIError) | Код ошибки |
| message | String? | Сообщение об ошибке |
| data | T? | Возвращаемые данные. Например, если T — это TUIUserInfo, то тип поля data в TUIValueCallBack<TUIUserInfo> — это TUIUserInfo |

### TUIRoomVideoEncoderParams

Параметры видеокодека

| Поле | Тип | Описание |
| --- | --- | --- |
| videoResolution | [TUIVideoQuality](https://www.tencentcloud.com/document/product/647/57515#74d0aadf-0c54-4a05-9e30-f40b427f1402) | Разрешение видео |
| resolutionMode | [TUIResolutionMode](https://www.tencentcloud.com/document/product/647/57515#TUIResolutionMode) | Режим разрешения видео |
| fps | int | Частота кадров захвата видео |
| bitrate | int | Целевой битрейт видео |

### TUINetwork

Информация о качестве сети

| Поле | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| quality | [TUINetworkQuality](https://www.tencentcloud.com/document/product/647/57515#NetworkQuality) | Качество сети |
| upLoss | int | Коэффициент потерь пакетов для восходящего потока |
| downLoss | int | Коэффициент потерь пакетов для нисходящего потока |
| delay | int | Задержка сети |

### TUIMessage

Сообщение

| Поле | Тип | Описание |
| --- | --- | --- |
| messageId | String | ID сообщения |
| message | String | Текст сообщения |
| timestamp | int | Временная метка сообщения |
| userId | String | Отправитель сообщения |
| userName | String | Имя отправителя сообщения |
| avatarUrl | String | Аватар отправителя сообщения |

### TUIImageBuffer

Информация об изображении

| Поле | Тип | Описание |
| --- | --- | --- |
| buffer | String | Адрес буфера данных изображения |
| length | int | Длина |
| width | int | Ширина |
| height | int | Высота |


---
*Источник: [https://trtc.io/document/57515](https://trtc.io/document/57515)*

---
*Источник (EN): [type-definition.md](./type-definition.md)*

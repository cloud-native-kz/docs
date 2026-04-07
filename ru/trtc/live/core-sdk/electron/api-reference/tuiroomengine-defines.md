# Определения TUIRoomEngine

Данный документ представляет определения типов для TUIRoomEngine на Electron.

## Перечисления

### TUIRole

Роли пользователей. TUIRoomEngine предоставляет три типа ролей пользователей: владелец, администратор и обычный пользователь.

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kRoomOwner | number | Роль владельца комнаты |
| kAdministrator | number | Роль администратора комнаты |
| kGeneralUser | number | Роль обычного пользователя |

### TUIVideoQuality

Разрешение видео.

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kVideoQuality_360p | number | Низкое качество, разрешение 640 * 360 |
| kVideoQuality_540p | number | Стандартное качество, разрешение 960 * 540 |
| kVideoQuality_720p | number | Высокое качество, разрешение 1280 * 720 |
| kVideoQuality_1080p | number | Очень высокое качество, разрешение 1920 * 1080 |

### TUIResolutionMode

Режим разрешения видео.

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kResolutionMode_Landscape | number | Режим альбомной ориентации |
| kResolutionMode_Portrait | number | Режим портретной ориентации |

### TUIAudioQuality

Разрешение аудио.

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kAudioProfileSpeech | number | Режим речи |
| kAudioProfileDefault | number | Стандартный режим (режим по умолчанию) |
| kAudioProfileMusic | number | Режим музыки |

### TUIVideoStreamType

Тип видеопотока.

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kCameraStream | number | Видеопоток высокого качества с камеры |
| kScreenStream | number | Видеопоток экрана/общего окна |
| kCameraStreamLow | number | Видеопоток низкого качества с камеры |

### TUINetworkQuality

Статус качества сети.

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kQualityUnknown | number | Неизвестное состояние сети |
| kQualityExcellent | number | Отличное состояние сети |
| kQualityGood | number | Хорошее состояние сети |
| kQualityPoor | number | Среднее состояние сети |
| kQualityBad | number | Плохое состояние сети |
| kQualityVeryBad | number | Очень плохое состояние сети |
| kQualityDown | number | Сетевое соединение разорвано |

### TUIRoomType

Тип комнаты.

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kConference | number | Конференц-зал: подходит для встреч, обучения и т.д. |
| kLive | number | Комната прямой трансляции: подходит для онлайн трансляций |

### TUISeatMode

Режим мест.

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kFreeToTake | number | Режим свободного захвата места, где члены аудитории могут свободно стать спикерами без подачи заявки. |
| kApplyToTake | number | Режим подачи заявки на место, где члены аудитории нуждаются в одобрении владельца или администратора, чтобы стать спикерами. |

### TUICaptureSourceType

Тип общего доступа к экрану.

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kWindow | number | Целью общего доступа является определенное окно Windows или Mac |
| kScreen | number | Целью общего доступа является весь рабочий стол Windows или экран Mac |

### TUIChangeReason

Причина изменения (причина изменения статуса аудио и видео пользователя: изменено самим собой или владельцем/администратором).

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kChangedBySelf | number | Самостоятельное действие |
| kChangedByAdmin | number | Действие владельца комнаты или администратора |

### TUIMediaDeviceState

Состояние медиа-устройства.

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kMediaDeviceStateAdd | number | Новое устройство добавлено |
| kMediaDeviceStateRemove | number | Устройство удалено |
| kMediaDeviceStateActive | number | Устройство активировано |
| kMediaDefaultDeviceChanged | number | Устройство по умолчанию системы изменилось |

### TUICameraCaptureMode

Режим захвата камеры

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kCameraResolutionStrategyAuto | number | Автоматически регулировать параметры захвата. SDK выбирает подходящие параметры вывода камеры на основе фактической производительности устройства захвата и условий сети, поддерживая баланс между производительностью устройства и качеством предпросмотра видео. |
| kCameraResolutionStrategyPerformance | number | Приоритет производительности устройства. SDK выбирает параметры вывода камеры, наиболее близкие к параметрам разрешения и частоты кадров энкодера, установленным пользователем, тем самым обеспечивая производительность устройства. |
| kCameraResolutionStrategyHighQuality | number | Приоритет качества видеопредпросмотра. SDK выбирает более высокие параметры вывода камеры для улучшения качества видео предпросмотра. В этом случае будет потреблено больше ресурсов ЦП и памяти для предварительной обработки видео. |
| kCameraCaptureManual | number | Позволяет пользователям установить ширину и высоту захвата видео локальной камеры. |

### TUIRequestAction

Тип операции запроса.

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kInvalidAction | number | Недействительная операция |
| kRequestToOpenRemoteCamera | number | Запрос на открытие удаленной камеры |
| kRequestToOpenRemoteMicrophone | number | Запрос на открытие удаленного микрофона |
| kRequestToConnectOtherRoom | number | Запрос на подключение микрофона удаленной комнаты |
| kRequestToTakeSeat | number | Запрос на выступление |
| kRequestRemoteUserOnSeat | number | Запрос на выступление удаленного пользователя |

### TUIRequestCallbackType

Тип обратного вызова запроса.

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kRequestAccepted | number | Запрос принят получателем |
| kRequestRejected | number | Запрос отклонен получателем |
| kRequestCancelled | number | Запрос отменен отправителем |
| kRequestTimeout | number | Истек тайм-аут запроса |
| kRequestError | number | Ошибка запроса |

### TUIKickedOutOfRoomReason

Причина исключения из комнаты.

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kKickedByAdmin | number | Удалено владельцем комнаты или администратором |
| kKickedByLoggedOnOtherDevice | number | Удалено при входе пользователя с тем же userId в ту же комнату с другого устройства |
| kKickedByServer | number | Удалено сервером |

### TUIConferenceStatus

Статус конференции.

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kConferenceStatusNone | number | Неизвестный статус |
| kConferenceStatusNotStarted | number | Конференция еще не началась |
| kConferenceStatusRunning | number | Конференция в процессе |

### TUIConferenceCancelReason

Причины отмены конференции

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kConferenceCancelReasonCancelledByAdmin | number | Отменено владельцем комнаты |
| kConferenceCancelReasonRemovedFromAttendees | number | Текущий пользователь был удален из списка участников |

### TUIMediaDeviceEventType

События медиа-устройства

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| onDeviceChanged | string | Имя события изменения состояния устройства |

### TUIVoiceReverbType

Эффекты голосовой реверберации

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kVoiceReverbType_0 | number | Выключено |
| kVoiceReverbType_1 | number | KTV |
| kVoiceReverbType_2 | number | Маленькая комната |
| kVoiceReverbType_3 | number | Аудитория |
| kVoiceReverbType_4 | number | Глубокий |
| kVoiceReverbType_5 | number | Громкий |
| kVoiceReverbType_6 | number | Металлический |
| kVoiceReverbType_7 | number | Магнитный |
| kVoiceReverbType_8 | number | Эфирный |
| kVoiceReverbType_9 | number | Студия |
| kVoiceReverbType_10 | number | Мягкий |
| kVoiceReverbType_11 | number | Студия 2 |

### TUIVoiceChangerType

Эффекты изменения голоса

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kVoiceChangerType_0 | number | Выключено |
| kVoiceChangerType_1 | number | Озорной ребенок |
| kVoiceChangerType_2 | number | Лолита |
| kVoiceChangerType_3 | number | Дядя |
| kVoiceChangerType_4 | number | Тяжелый металл |
| kVoiceChangerType_5 | number | Холодный |
| kVoiceChangerType_6 | number | Иностранный акцент |
| kVoiceChangerType_7 | number | Пойманный зверь |
| kVoiceChangerType_8 | number | Отаку |
| kVoiceChangerType_9 | number | Сильный ток |
| kVoiceChangerType_10 | number | Тяжелая техника |
| kVoiceChangerType_11 | number | Эфирный |

### TUIMediaRotation

Угол поворота

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kMediaRotation0 | number | Поворот на 0 градусов |
| kMediaRotation90 | number | Поворот на 90 градусов |
| kMediaRotation180 | number | Поворот на 180 градусов |
| kMediaRotation270 | number | Поворот на 270 градусов |

### TUIMediaFillMode

Режим заполнения для отображения медиа

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kMediaFillMode_Fill | number | Медиа заполняет область отображения, части видео, выходящие за границы окна отображения, будут обрезаны. Содержимое изображения может отображаться не полностью |
| kMediaFillMode_Fit | number | Длинная сторона медиа заполняет область отображения, короткая сторона будет заполнена черным. Содержимое изображения отображается полностью |

### TUIMediaMirrorType

Режим зеркалирования

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kMediaMirrorType_Auto | number | Автоматический режим. При локальном предпросмотре передняя камера зеркалирована, задняя камера не зеркалирована |
| kMediaMirrorType_Enable | number | Включить зеркалирование |
| kMediaMirrorType_Disable | number | Отключить зеркалирование |

### TUIVideoResolution

Разрешение видео. Здесь определены только разрешения в альбомной ориентации. Если вы хотите использовать разрешение в портретной ориентации, например 360 × 640, вам необходимо одновременно установить TUIResolutionMode в Portrait.

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kVideoResolution_120_120 | number | Рекомендуемый битрейт (VideoCall) 80kbps; Рекомендуемый битрейт (LIVE) 120kbps |
| kVideoResolution_160_160 | number | Рекомендуемый битрейт (VideoCall) 100kbps; Рекомендуемый битрейт (LIVE) 150kbps |
| kVideoResolution_270_270 | number | Рекомендуемый битрейт (VideoCall) 200kbps; Рекомендуемый битрейт (LIVE) 300kbps |
| kVideoResolution_480_480 | number | Рекомендуемый битрейт (VideoCall) 350kbps; Рекомендуемый битрейт (LIVE) 500kbps |
| kVideoResolution_160_120 | number | Рекомендуемый битрейт (VideoCall) 100kbps; Рекомендуемый битрейт (LIVE) 150kbps |
| kVideoResolution_240_180 | number | Рекомендуемый битрейт (VideoCall) 150kbps; Рекомендуемый битрейт (LIVE) 250kbps |
| kVideoResolution_280_210 | number | Рекомендуемый битрейт (VideoCall) 200kbps; Рекомендуемый битрейт (LIVE) 300kbps |
| kVideoResolution_320_240 | number | Рекомендуемый битрейт (VideoCall) 250kbps; Рекомендуемый битрейт (LIVE) 375kbps |
| kVideoResolution_400_300 | number | Рекомендуемый битрейт (VideoCall) 300kbps; Рекомендуемый битрейт (LIVE) 450kbps |
| kVideoResolution_480_360 | number | Рекомендуемый битрейт (VideoCall) 400kbps; Рекомендуемый битрейт (LIVE) 600kbps |
| kVideoResolution_640_480 | number | Рекомендуемый битрейт (VideoCall) 600kbps; Рекомендуемый битрейт (LIVE) 900kbps |
| kVideoResolution_960_720 | number | Рекомендуемый битрейт (VideoCall) 1000kbps; Рекомендуемый битрейт (LIVE) 1500kbps |
| kVideoResolution_160_90 | number | Рекомендуемый битрейт (VideoCall) 150kbps; Рекомендуемый битрейт (LIVE) 250kbps |
| kVideoResolution_256_144 | number | Рекомендуемый битрейт (VideoCall) 200kbps; Рекомендуемый битрейт (LIVE) 300kbps |
| kVideoResolution_320_180 | number | Рекомендуемый битрейт (VideoCall) 250kbps; Рекомендуемый битрейт (LIVE) 400kbps |
| kVideoResolution_480_270 | number | Рекомендуемый битрейт (VideoCall) 350kbps; Рекомендуемый битрейт (LIVE) 550kbps |
| kVideoResolution_640_360 | number | Рекомендуемый битрейт (VideoCall) 500kbps; Рекомендуемый битрейт (LIVE) 900kbps |
| kVideoResolution_960_540 | number | Рекомендуемый битрейт (VideoCall) 850kbps; Рекомендуемый битрейт (LIVE) 1300kbps |
| kVideoResolution_1280_720 | number | Рекомендуемый битрейт (VideoCall) 1200kbps; Рекомендуемый битрейт (LIVE) 1800kbps |
| kVideoResolution_1920_1080 | number | Рекомендуемый битрейт (VideoCall) 2000kbps; Рекомендуемый битрейт (LIVE) 3000kbpy |

### TUIMediaSourceType

Тип источника медиа

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| kCamera | number | Камера |
| kScreen | number | Экран/Окно |
| kImage | number | Изображение |

### TUIVideoPixelFormat

Формат видеоданных

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| TUIVideoPixelFormat_I420 | number | I420 |
| TUIVideoPixelFormat_BGRA32 | number | BGRA32 |
| TUIVideoPixelFormat_RGBA32 | number | RGBA32 |

## Определение типов

### TUILoginUserInfo

Информация о текущем вошедшем пользователе.

| Поле | Тип | Описание |
| --- | --- | --- |
| userId | string | ID вошедшего пользователя |
| userName | string | Имя вошедшего пользователя |
| avatarUrl | string | URL аватара вошедшего пользователя |

### TUIRoomInfo

Информация о комнате, которую можно получить с помощью roomEngine.fetchRoomInfo.

| Поле | Тип | Описание |
| --- | --- | --- |
| roomId | string | ID комнаты |
| roomName | string | Название комнаты |
| roomType | [TUIRoomType](#tuiroomtype) | Тип комнаты |
| isSeatEnabled | boolean | Включено ли управление местами (опциональный параметр при создании комнаты, значение по умолчанию false) |
| seatMode | [TUISeatMode](#tuiseatmode) | Режим мест в комнате (вступает в силу после включения управления местами, значение по умолчанию TUISeatMode.kFreeToTake) |
| isMicrophoneDisableForAllUser | boolean | Включено ли отключение микрофона для всех пользователей (опциональный параметр при создании комнаты, значение по умолчанию false) |
| isCameraDisableForAllUser | boolean | Включено ли отключение камеры для всех пользователей (опциональный параметр при создании комнаты, значение по умолчанию false) |
| isMessageDisableForAllUser | boolean | Разрешено ли всем пользователям отправлять сообщения (опциональный параметр при создании комнаты, значение по умолчанию false) |
| isScreenShareDisableForAllUser | boolean | Включено ли запрещение общего доступа к экрану (опциональный параметр при создании комнаты, значение по умолчанию false) |
| maxSeatCount | number | Максимальное количество мест, по умолчанию 6 |
| roomOwner | string | ID пользователя владельца комнаты, только для чтения |
| createTime | number | Время создания комнаты, только для чтения, точность в секундах |
| roomMemberCount | number | Количество членов комнаты, только для чтения |

### TUIUserInfo

Информация о пользователе.

| Поле | Тип | Описание |
| --- | --- | --- |
| userId | string | ID пользователя |
| userName | string | Имя пользователя |
| avatarUrl | string | URL аватара пользователя |
| userRole | [TUIRole](#tuirole) | Роль пользователя |
| hasAudioStream | boolean | Наличие аудиопотока |
| hasVideoStream | boolean | Наличие видеопотока |
| hasScreenStream | boolean | Наличие потока общего доступа к экрану |

### TUIMessage

Информация о сообщении.

| Поле | Тип | Описание |
| --- | --- | --- |
| messageId | string | ID сообщения |
| message | string | Сообщение |
| timestamp | number | Информация о временной метке, точность в секундах |
| userId | string | ID пользователя |
| userName | string | Имя пользователя |
| avatarUrl | string | URL аватара пользователя |

### TUIRequest

Информация о запросе.

| Поле | Тип | Описание |
| --- | --- | --- |
| requestAction | [TUIRequestAction](#tuirequestaction) | Тип запроса |
| timestamp | number | Время инициирования запроса |
| requestId | string | ID запроса |
| userId | string | ID пользователя, отправившего запрос |
| content | string | Другое содержимое |

### TUIRequestCallback

Информация об обратном вызове запроса.

| Поле | Тип | Описание |
| --- | --- | --- |
| requestCallbackType | [TUIRequestCallbackType](#tuirequestcallbacktype) | Тип обратного вызова запроса: принять/отклонить/отменить/тайм-аут/ошибка |
| requestId | string | ID запроса |
| userId | string | ID пользователя |
| code | number | Код ответа запроса |
| message | string | Дополнительное описание статуса запроса |

### TUISeatInfo

Информация о месте.

| Поле | Тип | Описание |
| --- | --- | --- |
| index | number | Индекс места |
| userId | string | ID пользователя, соответствующий месту |
| locked | boolean | Заблокировано ли текущее место |
| videoMuted | boolean | Отключено ли видео на текущем месте |
| audioMuted | boolean | Отключено ли аудио на текущем месте |

### TUISeatLockParams

Статус блокировки места.

| Поле | Тип | Описание |
| --- | --- | --- |
| lockSeat | boolean | Заблокировать место |
| lockVideo | boolean | Заблокировать видео места |
| lockAudio | boolean | Заблокировать аудио места |

### TUINetwork

Информация о сети.

| Поле | Тип | Описание |
| --- | --- | --- |
| userId | string | ID пользователя |
| quality | TUINetworkQuality | Качество сети |
| upLoss | number | Процент потери пакетов в восходящем направлении (%) Чем меньше значение, тем лучше. В настоящее время эта информация доступна только для локальных пользователей |
| downLoss | number | Процент потери пакетов в нисходящем направлении (%) Чем меньше значение, тем лучше. В настоящее время эта информация доступна только для локальных пользователей |
| delay | number | Задержка сети, единица ms, в настоящее время доступна только для локальных пользователей |

### TUIVideoEncoderParams

Параметры кодирования видео.

| Поле | Тип | Описание |
| --- | --- | --- |
| videoResolution | [TUIVideoResolution](#tuivideoresolution) | Разрешение видео |
| fps | number | Частота кадров видео |
| bitrate | number | Битрейт видео |
| resolutionMode | [TUIResolutionMode](#tuiresolutionmode) | Режим портретной/альбомной ориентации |

### TUIRect

Прямоугольная область координат

| Поле | Тип | Описание |
| --- | --- | --- |
| left | number | Координата левой линии |
| top | number | Координата верхней линии |
| right | number | Координата правой линии |
| bottom | number | Координата нижней линии |

### TUICameraCaptureParam

Параметры захвата камеры

| Элемент перечисления | Тип | Описание |
| --- | --- | --- |
| mode | [TUICameraCaptureMode](#tuicameracapturemode) | Режим захвата камеры |
| width | number | Ширина захватываемого изображения |
| height | number | Высота захватываемого изображения |

### TUIAudioMusicParam

Информация управления воспроизведением фоновой музыки

| Поле | Тип | Описание |
| --- | --- | --- |
| id | number | ID музыки. Допускается воспроизведение нескольких музыкальных дорожек, поэтому требуется ID для управления запуском, остановкой, громкостью и т.д. музыки. |
| path | string | Полный путь или URL-адрес аудиофайла. Поддерживаемые форматы аудио включают MP3, AAC, M4A, WAV. |
| loopCount | number | Количество повторений музыки. Диапазон от 0 до любого положительного целого числа, значение по умолчанию: 0. 0 означает воспроизведение музыки один раз; 1 означает воспроизведение музыки два раза и так далее. |
| publish | boolean | Передавать ли музыку на удаленную сторону. true: Музыка может быть услышана удаленными пользователями при воспроизведении локально; false: Якорь может слышать музыку только локально, удаленная аудитория не может ее слышать. Значение по умолчанию: false. |
| isShortFile | boolean | Является ли это коротким музыкальным файлом. true: Короткий музыкальный файл, который необходимо повторить; false: Обычный музыкальный файл. Значение по умолчанию: false. |
| startTimeMS | number | Точка начала воспроизведения музыки, единица: миллисекунды. |
| endTimeMS | number | Точка конца воспроизведения музыки, единица миллисекунды, 0 означает воспроизведение до конца файла. |

### TUIMusicPlayObserver

Определение типа слушателя событий воспроизведения фоновой музыки

| Поле | Тип | Описание |
| --- | --- | --- |
| onStart | Function \| null | Событие начала воспроизведения фоновой музыки |
| onPlayProgress | Function \| null | Событие прогресса воспроизведения фоновой музыки |
| onComplete | Function \| null | Событие завершения воспроизведения фоновой музыки |

### TUIScreenCaptureSourceInfo

Данные экрана/окна

| Поле | Тип | Описание |
| --- | --- | --- |
| type | [TUIMediaSourceType](#tuimediasourcetype) | Тип источника медиа: экран/окно |
| sourceId | number | Уникальный ID |
| sourceName | string | Имя |
| isMinimizeWindow | boolean | Свернуто ли окно |
| isMainScreen | boolean | Является ли это основным экраном |
| rect | [TUIRect](#tuirect) | Относительная позиция координат на экране отображения |

### TUIMediaSource

Данные источника медиа

| Поле | Тип | Описание |
| --- | --- | --- |
| sourceType | [TUIMediaSourceType

---
*Источник (EN): [tuiroomengine-defines.md](./tuiroomengine-defines.md)*

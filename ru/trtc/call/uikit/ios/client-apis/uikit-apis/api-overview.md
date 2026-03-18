# Обзор API

## TUICallKit (с интерфейсом)

TUICallKit — это компонент аудио/видеозвонков, который **включает элементы интерфейса**. Вы можете использовать его API для быстрой реализации приложения аудио/видеозвонков, похожего на WeChat.

| API | Описание |
| --- | --- |
| [createInstance](https://www.tencentcloud.com/document/product/647/51011#createInstance) | Создать экземпляр TUICallKit (режим синглтон). |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/51011#setSelfInfo) | Установить фотографию профиля и никнейм пользователя. |
| [calls](https://www.tencentcloud.com/document/product/647/51011#calls) | Инициировать один-к-одному или многопользовательский звонок |
| [join](https://www.tencentcloud.com/document/product/647/51011#join) | Активно присоединиться к звонку |
| [setCallingBell](https://www.tencentcloud.com/document/product/647/51011#setCallingBell) | Установить рингтон. |
| [enableMuteMode](https://www.tencentcloud.com/document/product/647/51011#enableMuteMode) | Установить, следует ли включать режим отключения звука. |
| [enableFloatWindow](https://www.tencentcloud.com/document/product/647/51011#enableFloatWindow) | Установить, следует ли включать плавающие окна. |
| [enableIncomingBanner](https://www.tencentcloud.com/document/product/647/51011#enableIncomingBanner) | Установить, следует ли отображать баннер входящего вызова. |

## TUICallEngine (без интерфейса)

`TUICallEngine` — это компонент аудио/видеозвонков, который **не включает элементы интерфейса**. Если `TUICallKit` не соответствует вашим требованиям, вы можете использовать API `TUICallEngine` для настройки вашего проекта.

| API | Описание |
| --- | --- |
| [createInstance](https://www.tencentcloud.com/document/product/647/51012#createInstance) | Создать экземпляр TUICallEngine (синглтон). |
| [destroyInstance](https://www.tencentcloud.com/document/product/647/51012#destroyInstance) | Уничтожить экземпляр TUICallEngine (синглтон). |
| [Init](https://www.tencentcloud.com/document/product/647/51012#Init) | Аутентифицирует основные возможности аудио/видеозвонков. |
| [addObserver](https://www.tencentcloud.com/document/product/647/51012#addObserver) | Добавить слушатель. |
| [removeObserver](https://www.tencentcloud.com/document/product/647/51012#removeObserver) | Удалить слушатель. |
| [calls](https://www.tencentcloud.com/document/product/647/51012#calls) | Инициировать один-к-одному или многопользовательский звонок |
| [join](https://www.tencentcloud.com/document/product/647/51012#join) | Активно присоединиться к звонку |
| [accept](https://www.tencentcloud.com/document/product/647/51012#accept) | Принять звонок. |
| [reject](https://www.tencentcloud.com/document/product/647/51012#reject) | Отклонить звонок. |
| [hangup](https://www.tencentcloud.com/document/product/647/51012#hangup) | Завершить звонок. |
| [ignore](https://www.tencentcloud.com/document/product/647/51012#hangup) | Игнорировать звонок. |
| [inviteUser](https://www.tencentcloud.com/document/product/647/51012#inviteUser) | Пригласить пользователей в текущий звонок. |
| [switchCallMediaType](https://www.tencentcloud.com/document/product/647/51012#switchCallMediaType) | Переключить тип медиа звонка, например с видеовызова на аудиовызов. |
| [startRemoteView](https://www.tencentcloud.com/document/product/647/51012#startRemoteView) | Подписаться на видеопоток удалённого пользователя. |
| [stopRemoteView](https://www.tencentcloud.com/document/product/647/51012#stopRemoteView) | Отписаться от видеопотока удалённого пользователя. |
| [openCamera](https://www.tencentcloud.com/document/product/647/51012#openCamera) | Включить камеру. |
| [closeCamera](https://www.tencentcloud.com/document/product/647/51012#closeCamera) | Отключить камеру. |
| [switchCamera](https://www.tencentcloud.com/document/product/647/51012#switchCamera) | Переключить камеру. |
| [openMicrophone](https://www.tencentcloud.com/document/product/647/51012#openMicrophone) | Включить микрофон. |
| [closeMicrophone](https://www.tencentcloud.com/document/product/647/51012#closeMicrophone) | Отключить микрофон. |
| [selectAudioPlaybackDevice](https://www.tencentcloud.com/document/product/647/51012#selectAudioPlaybackDevice) | Выбрать устройство воспроизведения звука (Наушник/Динамик). |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/51012#setSelfInfo) | Установить фотографию профиля и никнейм пользователя. |
| [enableMultiDeviceAbility](https://www.tencentcloud.com/document/product/647/51012#enableMultiDeviceAbility) | Установить, следует ли включать вход с нескольких устройств для TUICallEngine (поддерживается [пакетом Group Call](https://trtc.io/document/54632?platform=ios&product=call&menulabel=web)). |
| [setVideoRenderParams](https://www.tencentcloud.com/document/product/647/51012#setVideoRenderParams) | Установить режим отрисовки видео. |
| [setVideoEncoderParams](https://www.tencentcloud.com/document/product/647/51012#setVideoEncoderParams) | Установить параметры кодирования видеокодека. |
| [getTRTCCloudInstance](https://www.tencentcloud.com/document/product/647/51012#getTRTCCloudInstance) | Расширенные функции. |
| [setBeautyLevel](https://www.tencentcloud.com/document/product/647/51012#setBeautyLevel) | Установить уровень красоты, поддерживается отключение красоты по умолчанию. |

### TUICallObserver

`TUICallObserver` — это класс обратного вызова `TUICallEngine`. Вы можете использовать его для отслеживания событий.

| API | Описание |
| --- | --- |
| [onError](https://www.tencentcloud.com/document/product/647/51013#onError) | Во время звонка произошла ошибка. |
| [onCallReceived](https://www.tencentcloud.com/document/product/647/51013#onCallReceived) | Звонок получен. |
| [onCallCancelled](https://www.tencentcloud.com/document/product/647/51013#onCallCancelled) | Звонок был отменён. |
| [onCallBegin](https://www.tencentcloud.com/document/product/647/51013#onCallBegin) | Звонок был подключён. |
| [onCallEnd](https://www.tencentcloud.com/document/product/647/51013#onCallEnd) | Звонок завершился. |
| [onCallMediaTypeChanged](https://www.tencentcloud.com/document/product/647/51013#onCallMediaTypeChanged) | Тип звонка изменился. |
| [onUserReject](https://www.tencentcloud.com/document/product/647/51013#onUserReject) | Пользователь отклонил звонок. |
| [onUserNoResponse](https://www.tencentcloud.com/document/product/647/51013#onUserNoResponse) | Пользователь не ответил. |
| [onUserLineBusy](https://www.tencentcloud.com/document/product/647/51013#onUserLineBusy) | Пользователь занят. |
| [onUserJoin](https://www.tencentcloud.com/document/product/647/51013#onUserJoin) | Пользователь присоединился к звонку. |
| [onUserLeave](https://www.tencentcloud.com/document/product/647/51013#onUserLeave) | Пользователь покинул звонок. |
| [onUserVideoAvailable](https://www.tencentcloud.com/document/product/647/51013#onUserVideoAvailable) | Имеет ли пользователь видеопоток. |
| [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/51013#onUserAudioAvailable) | Имеет ли пользователь аудиопоток. |
| [onUserVoiceVolumeChanged](https://www.tencentcloud.com/document/product/647/51013#onUserVoiceVolumeChanged) | Уровни громкости всех пользователей. |
| [onUserNetworkQualityChanged](https://www.tencentcloud.com/document/product/647/51013#onUserNetworkQualityChanged) | Качество сети всех пользователей. |
| [onKickedOffline](https://www.tencentcloud.com/document/product/647/51013#onKickedOffline) | Текущий пользователь был отключён в сети. |
| [onUserSigExpired](https://www.tencentcloud.com/document/product/647/51013#onUserSigExpired) | User sig истёк. |

## Определения основных типов

| API | Описание |
| --- | --- |
| [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54902#MediaType) | Тип медиа звонка, тип перечисления: Unknown, Video и Audio. |
| [TUICallRole](https://www.tencentcloud.com/document/product/647/54902#Role) | Роль при звонке, тип перечисления: None, Call и Called. |
| [TUICallStatus](https://www.tencentcloud.com/document/product/647/54902#Status) | Статус звонка, тип перечисления: None, Waiting и Accept. |
| [TUIRoomId](https://www.tencentcloud.com/document/product/647/54902#RoomId) | Идентификатор комнаты, может быть числом или строкой. |
| [TUICallCamera](https://www.tencentcloud.com/document/product/647/54902#Camera) | Тип камеры. Тип перечисления: Front camera и Back camera. |
| [TUIAudioPlaybackDevice](https://www.tencentcloud.com/document/product/647/54902#AudioPlaybackDevice) | Тип устройства воспроизведения звука. Тип перечисления: Earpiece и Speakerphone. |
| [TUINetworkQualityInfo](https://www.tencentcloud.com/document/product/647/54902#NetworkQuality) | Текущее качество сети. |


---
*Источник: [https://trtc.io/document/51010](https://trtc.io/document/51010)*

---
*Источник (EN): [api-overview.md](./api-overview.md)*

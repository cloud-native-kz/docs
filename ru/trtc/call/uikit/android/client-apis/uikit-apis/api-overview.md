# Обзор API

## TUICallKit (с интерфейсом)

TUICallKit — это компонент для аудио- и видеозвонков, который **включает элементы UI**. Вы можете использовать его API для быстрого создания приложения для аудио- и видеозвонков, похожего на WeChat.

| API | Описание |
| --- | --- |
| [createInstance](https://www.tencentcloud.com/document/product/647/51005#createinstance) | Создать экземпляр TUICallKit (режим Singleton). |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/51005#setselfinfo) | Установить аватар и никнейм пользователя. |
| [calls](https://www.tencentcloud.com/document/product/647/51005#calls) | Инициировать один-к-одному или многопользовательский вызов. |
| [join](https://www.tencentcloud.com/document/product/647/51005#join) | Активно присоединиться к вызову. |
| [setCallingBell](https://www.tencentcloud.com/document/product/647/51005#setcallingbell) | Установить рингтон. |
| [enableMuteMode](https://www.tencentcloud.com/document/product/647/51005#enablemutemode) | Установить, включать ли режим без звука. |
| [enableFloatWindow](https://www.tencentcloud.com/document/product/647/51005#enablefloatwindow) | Установить, включать ли плавающие окна. |
| [enableIncomingBanner](https://www.tencentcloud.com/document/product/647/51005#enableIncomingBanner) | Установить, отображается ли баннер входящего вызова. |
| [disableControlButton](https://www.tencentcloud.com/document/product/647/51005#disableControlButton) | Скрыть указанную кнопку. |

## TUICallEngine (без интерфейса)

`TUICallEngine` — это компонент для аудио- и видеозвонков, который **не включает элементы UI**. Если `TUICallKit` не соответствует вашим требованиям, вы можете использовать API `TUICallEngine` для настройки своего проекта.

| API | Описание |
| --- | --- |
| [createInstance](https://www.tencentcloud.com/document/product/647/51006#createInstance) | Создать экземпляр `TUICallEngine` (Singleton). |
| [destroyInstance](https://www.tencentcloud.com/document/product/647/51006#destroyInstance) | Уничтожить экземпляр `TUICallEngine` (Singleton). |
| [init](https://www.tencentcloud.com/document/product/647/51006#init) | Аутентификация базовых возможностей аудио- и видеозвонков. |
| [addObserver](https://www.tencentcloud.com/document/product/647/51006#addObserver) | Добавить слушатель. |
| [removeObserver](https://www.tencentcloud.com/document/product/647/51006#removeObserver) | Удалить слушатель. |
| [calls](https://www.tencentcloud.com/document/product/647/51006#calls) | Инициировать один-к-одному или многопользовательский вызов. |
| [join](https://www.tencentcloud.com/document/product/647/51006#join) | Активно присоединиться к вызову. |
| [accept](https://www.tencentcloud.com/document/product/647/51006#accept) | Принять вызов. |
| [reject](https://www.tencentcloud.com/document/product/647/51006#reject) | Отклонить вызов. |
| [hangup](https://www.tencentcloud.com/document/product/647/51006#hangup) | Завершить вызов. |
| [ignore](https://www.tencentcloud.com/document/product/647/51006#ignore) | Игнорировать вызов. |
| [inviteUser](https://www.tencentcloud.com/document/product/647/51006#inviteUser) | Пригласить пользователей в текущий групповой вызов. |
| [switchCallMediaType](https://www.tencentcloud.com/document/product/647/51006#switchCallMediaType) | Переключить тип носителя вызова, например с видеовызова на аудиовызов. |
| [startRemoteView](https://www.tencentcloud.com/document/product/647/51006#startRemoteView) | Подписаться на видеопоток удаленного пользователя. |
| [stopRemoteView](https://www.tencentcloud.com/document/product/647/51006#stopRemoteView) | Отписаться от видеопотока удаленного пользователя. |
| [openCamera](https://www.tencentcloud.com/document/product/647/51006#openCamera) | Включить камеру. |
| [closeCamera](https://www.tencentcloud.com/document/product/647/51006#closeCamera) | Выключить камеру. |
| [switchCamera](https://www.tencentcloud.com/document/product/647/51006#switchCamera) | Переключить камеру. |
| [openMicrophone](https://www.tencentcloud.com/document/product/647/51006#openMicrophone) | Включить микрофон. |
| [closeMicrophone](https://www.tencentcloud.com/document/product/647/51006#openMicrophone) | Выключить микрофон. |
| [selectAudioPlaybackDevice](https://www.tencentcloud.com/document/product/647/51006#selectAudioPlaybackDevice) | Выбрать устройство воспроизведения звука (Наушник/Динамик). |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/51006#setSelfInfo) | Установить аватар и никнейм пользователя. |
| [enableMultiDeviceAbility](https://www.tencentcloud.com/document/product/647/51006#enableMultiDeviceAbility) | Установить, включать ли вход с нескольких устройств для `TUICallEngine` (поддерживается [пакетом Group Call](https://trtc.io/document/54632?platform=android&product=call&menulabel=web)). |
| [setVideoRenderParams](https://www.tencentcloud.com/document/product/647/51006#setVideoRenderParams) | Установить режим рендеринга видео. |
| [setVideoEncoderParams](https://www.tencentcloud.com/document/product/647/51006#setVideoEncoderParams) | Установить параметры кодирования видеоэнкодера. |
| [getTRTCCloudInstance](https://www.tencentcloud.com/document/product/647/51006#getTRTCCloudInstance) | Продвинутые функции. |
| [setBeautyLevel](https://www.tencentcloud.com/document/product/647/51006#setBeautyLevel) | Установить уровень красоты, поддерживается отключение красоты по умолчанию. |

## TUICallObserver

`TUICallObserver` — это класс обратного вызова `TUICallEngine`. Вы можете использовать его для прослушивания событий.

| API | Описание |
| --- | --- |
| [onError](https://www.tencentcloud.com/document/product/647/51007#onError) | Произошла ошибка во время вызова. |
| [onCallReceived](https://www.tencentcloud.com/document/product/647/51007#onCallReceived) | Был получен вызов. |
| [onCallCancelled](https://www.tencentcloud.com/document/product/647/51007#onCallCancelled) | Вызов был отменен. |
| [onCallBegin](https://www.tencentcloud.com/document/product/647/51007#onCallBegin) | Вызов был соединен. |
| [onCallEnd](https://www.tencentcloud.com/document/product/647/51007#onCallEnd) | Вызов завершился. |
| [onCallMediaTypeChanged](https://www.tencentcloud.com/document/product/647/51007#onCallMediaTypeChanged) | Тип вызова изменился. |
| [onUserReject](https://www.tencentcloud.com/document/product/647/51007#onUserReject) | Пользователь отклонил вызов. |
| [onUserNoResponse](https://www.tencentcloud.com/document/product/647/51007#onUserNoResponse) | Пользователь не ответил. |
| [onUserLineBusy](https://www.tencentcloud.com/document/product/647/51007#onUserLineBusy) | Пользователь был занят. |
| [onUserJoin](https://www.tencentcloud.com/document/product/647/51007#onUserJoin) | Пользователь присоединился к вызову. |
| [onUserLeave](https://www.tencentcloud.com/document/product/647/51007#onUserLeave) | Пользователь покинул вызов. |
| [onUserVideoAvailable](https://www.tencentcloud.com/document/product/647/51007#onUserVideoAvailable) | Есть ли у пользователя видеопоток. |
| [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/51007#onUserAudioAvailable) | Есть ли у пользователя аудиопоток. |
| [onUserVoiceVolumeChanged](https://www.tencentcloud.com/document/product/647/51007#onUserVoiceVolumeChanged) | Уровни громкости всех пользователей. |
| [onUserNetworkQualityChanged](https://www.tencentcloud.com/document/product/647/51007#onUserNetworkQualityChanged) | Качество сети всех пользователей. |
| [onKickedOffline](https://www.tencentcloud.com/document/product/647/51007#onKickedOffline) | Текущий пользователь был отключен. |
| [onUserSigExpired](https://www.tencentcloud.com/document/product/647/51007#onUserSigExpired) | Подпись пользователя истекла. |

## Определения основных типов

| API | Описание |
| --- | --- |
| [TUICallDefine.MediaType](https://www.tencentcloud.com/document/product/647/54900#MediaType) | Тип носителя вызова, тип перечисления: Unknown, Video и Audio. |
| [TUICallDefine.Role](https://www.tencentcloud.com/document/product/647/54900#Role) | Роль в вызове, тип перечисления: None, Caller и Called. |
| [TUICallDefine.Status](https://www.tencentcloud.com/document/product/647/54900#Status) | Статус вызова, тип перечисления: None, Waiting и Accept. |
| [TUICommonDefine.RoomId](https://www.tencentcloud.com/document/product/647/54900#RoomId) | ID комнаты, может быть числом или строкой. |
| [TUICommonDefine.Camera](https://www.tencentcloud.com/document/product/647/54900#Camera) | Тип камеры. Тип перечисления: Фронтальная камера и задняя камера. |
| [TUICommonDefine.AudioPlaybackDevice](https://www.tencentcloud.com/document/product/647/54900#AudioPlaybackDevice) | Тип устройства воспроизведения звука. Тип перечисления: Наушник и динамик. |
| [TUICommonDefine.NetworkQualityInfo](https://www.tencentcloud.com/document/product/647/54900#NetworkQualityInfo) | Текущее качество сети. |


---
*Источник: [https://trtc.io/document/51004](https://trtc.io/document/51004)*

---
*Источник (EN): [api-overview.md](./api-overview.md)*

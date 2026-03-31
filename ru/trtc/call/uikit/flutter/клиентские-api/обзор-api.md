# Обзор API

## TUICallKit (с включенным пользовательским интерфейсом)

TUICallKit — это компонент аудио- и видеовызова, который **включает элементы пользовательского интерфейса**. Вы можете использовать его API для быстрой реализации приложения аудио- и видеовызовов, аналогичного WeChat.

| API | Описание |
| --- | --- |
| [login](https://www.tencentcloud.com/document/product/647/54906#login) | Вход |
| [logout](#logout) | Выход |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/54906#setSelfInfo) | Устанавливает прозвище пользователя и фотографию профиля. |
| [calls](https://www.tencentcloud.com/document/product/647/54906#calls) | Начать вызов. |
| [join](https://www.tencentcloud.com/document/product/647/54906#join) | Присоединиться к вызову. |
| [enableMuteMode](https://www.tencentcloud.com/document/product/647/54906#enableMuteMode) | Устанавливает, включен ли режим беззвучности. |
| [enableFloatWindow](https://www.tencentcloud.com/document/product/647/54906#enableFloatWindow) | Устанавливает, включены ли плавающие окна. |
| [setCallingBell](https://www.tencentcloud.com/document/product/647/54906#setCallingBell) | Пользовательский рингтон. |
| [enableVirtualBackground](https://www.tencentcloud.com/document/product/647/54906#6f0d0f68-18bd-4a16-a074-6d7288dcd6dd) | Включить/Отключить функцию виртуального фона |

## TUICallEngine (без пользовательского интерфейса)

`TUICallEngine` — это компонент аудио- и видеовызова, который **не включает элементы пользовательского интерфейса**. Если `TUICallKit` не соответствует вашим требованиям, вы можете использовать API `TUICallEngine` для настройки вашего проекта.

| API | Описание |
| --- | --- |
| [init](https://www.tencentcloud.com/document/product/647/54907#init) | Аутентификация базовых возможностей аудио- и видеовызовов. |
|  |  |
| [unInit](https://www.tencentcloud.com/document/product/647/54907#unInit) | Функция деструктора, которая освобождает ресурсы, используемые TUICallEngine. |
| [addObserver](https://www.tencentcloud.com/document/product/647/54907#addobserver) | Регистрирует прослушиватель событий. |
| [removeObserver](https://www.tencentcloud.com/document/product/647/54907#removeobserver) | Отменяет регистрацию прослушивателя событий. |
| [calls](https://www.tencentcloud.com/document/product/647/54907#calls) | Начать вызов. |
| [accept](https://www.tencentcloud.com/document/product/647/54907#accept) | Принять вызов. |
| [reject](https://www.tencentcloud.com/document/product/647/54907#reject) | Отклонить вызов. |
| [hangup](https://www.tencentcloud.com/document/product/647/54907#hangup) | Завершить вызов. |
| [ignore](https://www.tencentcloud.com/document/product/647/54907#ignore) | Игнорировать вызов. |
| [inviteUser](https://www.tencentcloud.com/document/product/647/54907#inviteuser) | Пригласить других присоединиться к вызову. |
| [join](https://www.tencentcloud.com/document/product/647/54907#join) | Присоединиться к вызову. |
| [switchCallMediaType](https://www.tencentcloud.com/document/product/647/54907#switchcallmediatype) | Изменить тип вызова, например, с видеовызова на аудиовызов. |
| [startRemoteView](https://www.tencentcloud.com/document/product/647/54907#startremoteview) | Подписаться на видеопоток удаленного пользователя. |
| [stopRemoteView](https://www.tencentcloud.com/document/product/647/54907#stopremoteview) | Отписаться от видеопотока удаленного пользователя. |
| [openCamera](https://www.tencentcloud.com/document/product/647/54907#opencamera) | Включить камеру. |
| [closeCamera](https://www.tencentcloud.com/document/product/647/54907#closecamera) | Отключить камеру. |
| [switchCamera](https://www.tencentcloud.com/document/product/647/54907#switchcamera) | Переключение между передней и задней камерами. |
| [openMicrophone](https://www.tencentcloud.com/document/product/647/54907#openmicrophone) | Включить микрофон. |
| [closeMicrophone](https://www.tencentcloud.com/document/product/647/54907#closemicrophone) | Отключить микрофон. |
| [selectAudioPlaybackDevice](https://www.tencentcloud.com/document/product/647/54907#selectaudioplaybackdevice) | Выберите устройство воспроизведения звука (динамик или наушники). |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/54907#setselfinfo) | Устанавливает псевдоним и фотографию профиля. |
| [enableMultiDeviceAbility](https://www.tencentcloud.com/document/product/647/54907#enablemultideviceability) | Устанавливает, включена ли функция входа с нескольких устройств для TUICallEngine (поддерживается в премиум-пакете). |
| [setVideoRenderParams](https://www.tencentcloud.com/document/product/647/54907#setVideoRenderParams) | Установить режим отрисовки видеоизображения. |
| [setVideoEncoderParams](https://www.tencentcloud.com/document/product/647/54907#setVideoEncoderParams) | Установить параметры кодирования видеокодера. |
| [queryRecentCalls](https://www.tencentcloud.com/document/product/647/54907#queryRecentCalls) | Запросить историю вызовов. |
| [deleteRecordCalls](https://www.tencentcloud.com/document/product/647/54907#deleteRecordCalls) | Удалить историю вызовов. |
| [setBlurBackground](https://www.tencentcloud.com/document/product/647/54907#a84f7a0a-6a2a-47be-9a2b-dba02873f43a) | Установить размытый видеоэффект |
| [setVirtualBackground](https://www.tencentcloud.com/document/product/647/54907#9f5e78e9-0d3b-4534-b8db-3435db17d448) | Установить изображение виртуального фона |
| [setBeautyLevel](https://www.tencentcloud.com/document/product/647/54907#setBeautyLevel) | Установить уровень красоты, поддерживается отключение красоты по умолчанию. |

## TUICallObserver

`TUICallObserver` — это класс обратного вызова `TUICallEngine`. Вы можете использовать его для прослушивания событий.

| API | Описание |
| --- | --- |
| [onError](https://www.tencentcloud.com/document/product/647/54908#onError) | Во время вызова произошла ошибка. |
| [onUserInviting](https://www.tencentcloud.com/document/product/647/54908#onUserInviting) | Обратный вызов при приглашении пользователя присоединиться к вызову. |
| [onCallReceived](https://www.tencentcloud.com/document/product/647/54908#onCallReceived) | Приглашение на вызов было получено. |
| [onCallNotConnected](https://www.tencentcloud.com/document/product/647/54908#onCallNotConnected) | Обратный вызов при отмене вызова |
| [onCallBegin](https://www.tencentcloud.com/document/product/647/54908#onCallBegin) | Вызов был подключен. |
| [onCallEnd](https://www.tencentcloud.com/document/product/647/54908#onCallEnd) | Вызов завершился. |
| [onCallMediaTypeChanged](https://www.tencentcloud.com/document/product/647/54908#onCallMediaTypeChanged) | Тип вызова изменился. |
| [onUserReject](https://www.tencentcloud.com/document/product/647/54908#onUserReject) | Пользователь отклонил вызов. |
| [onUserNoResponse](https://www.tencentcloud.com/document/product/647/54908#onUserNoResponse) | Пользователь не ответил. |
| [onUserLineBusy](https://www.tencentcloud.com/document/product/647/54908#onUserLineBusy) | Пользователь был занят. |
| [onUserJoin](https://www.tencentcloud.com/document/product/647/54908#onUserJoin) | Пользователь присоединился к вызову. |
| [onUserLeave](https://www.tencentcloud.com/document/product/647/54908#onUserLeave) | Пользователь покинул вызов. |
| [onUserVideoAvailable](https://www.tencentcloud.com/document/product/647/54908#onUserVideoAvailable) | Есть ли у пользователя видеопоток. |
| [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/54908#onUserAudioAvailable) | Есть ли у пользователя аудиопоток. |
| [onUserVoiceVolumeChanged](https://www.tencentcloud.com/document/product/647/54908#onUserVoiceVolumeChanged) | Уровни громкости всех пользователей. |
| [onUserNetworkQualityChanged](https://www.tencentcloud.com/document/product/647/54908#onUserNetworkQualityChanged) | Качество сети всех пользователей. |
| [onKickedOffline](https://www.tencentcloud.com/document/product/647/54908#onKickedOffline) | Текущий пользователь отключен от сети |
| [onUserSigExpired](https://www.tencentcloud.com/document/product/647/54908#onUserSigExpired) | Билет истек во время подключения |

## Основные определения типов

| Тип | Описание |
| --- | --- |
| [VideoEncoderParams](https://www.tencentcloud.com/document/product/647/54909#VideoEncoderParams) | Параметры кодирования видео. |
| [VideoRenderParams](https://www.tencentcloud.com/document/product/647/54909#VideoRenderParams) | Параметры отрисовки видео. |
| [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54909#TUICallMediaType) | Тип носителя вызова. |
| [TUICallParams](https://www.tencentcloud.com/document/product/647/54909#TUICallParams) | Параметры расширения вызова. |
| [TUICamera](https://www.tencentcloud.com/document/product/647/54909#TUICamera) | Тип камеры. |
| [TUIAudioPlaybackDevice](https://www.tencentcloud.com/document/product/647/54909#TUIAudioPlaybackDevice) | Устройство воспроизведения звука. |
| [TUIRoomId](https://www.tencentcloud.com/document/product/647/54909#TUIRoomId) | Идентификатор комнаты для аудио- и видеовызовов. |


---
*Источник: [https://trtc.io/document/54905](https://trtc.io/document/54905)*

---
*Источник (EN): [api-overview.md](./api-overview.md)*

# TUICallEngine

## API-интерфейсы TUICallEngine

`TUICallEngine` — это компонент аудио-видео вызовов, который **не включает элементы пользовательского интерфейса**. Если `TUICallKit` не соответствует вашим требованиям, вы можете использовать API-интерфейсы `TUICallEngine` для настройки вашего проекта.

## Обзор

| API | Описание |
| --- | --- |
| [createInstance](https://www.tencentcloud.com/document/product/647/51012#createInstance) | Создать экземпляр TUICallEngine (singleton). |
| [destroyInstance](https://www.tencentcloud.com/document/product/647/51012#destroyInstance) | Уничтожить экземпляр TUICallEngine (singleton). |
| [init](https://www.tencentcloud.com/document/product/647/51012#init) | Аутентификация базовых возможностей аудио-видео вызовов. |
| [addObserver](https://www.tencentcloud.com/document/product/647/51012#addObserver) | Добавить слушатель. |
| [removeObserver](https://www.tencentcloud.com/document/product/647/51012#removeObserver) | Удалить слушатель. |
| [calls](https://www.tencentcloud.com/document/product/647/51012#calls) | Инициировать личный или групповой вызов |
| [join](https://www.tencentcloud.com/document/product/647/51012#join) | Активно присоединиться к вызову |
| [accept](https://www.tencentcloud.com/document/product/647/51012#accept) | Принять вызов. |
| [reject](https://www.tencentcloud.com/document/product/647/51012#reject) | Отклонить вызов. |
| [hangup](https://www.tencentcloud.com/document/product/647/51012#hangup) | Завершить вызов. |
| [ignore](https://www.tencentcloud.com/document/product/647/51012#ignore) | Игнорировать вызов. |
| [inviteUser](https://www.tencentcloud.com/document/product/647/51012#inviteUser) | Пригласить пользователей на текущий вызов. |
| [startRemoteView](https://www.tencentcloud.com/document/product/647/51012#startRemoteView) | Подписаться на видеопоток удаленного пользователя. |
| [stopRemoteView](https://www.tencentcloud.com/document/product/647/51012#stopRemoteView) | Отписаться от видеопотока удаленного пользователя. |
| [openCamera](https://www.tencentcloud.com/document/product/647/51012#openCamera) | Включить камеру. |
| [closeCamera](https://www.tencentcloud.com/document/product/647/51012#closeCamera) | Отключить камеру. |
| [switchCamera](https://www.tencentcloud.com/document/product/647/51012#switchCamera) | Переключить камеру. |
| [openMicrophone](https://www.tencentcloud.com/document/product/647/51012#openMicrophone) | Включить микрофон. |
| [closeMicrophone](https://www.tencentcloud.com/document/product/647/51012#closeMicrophone) | Отключить микрофон. |
| [selectAudioPlaybackDevice](https://www.tencentcloud.com/document/product/647/51012#selectAudioPlaybackDevice) | Выбрать устройство воспроизведения аудио (наушники/громкоговоритель). |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/51012#setSelfInfo) | Установить аватар и прозвище пользователя. |
| [enableMultiDeviceAbility](https://www.tencentcloud.com/document/product/647/51012#enableMultiDeviceAbility) | Установить, нужно ли включить вход с нескольких устройств для TUICallEngine (поддерживается [пакетом Group Call](https://trtc.io/document/54632?platform=ios&product=call&menulabel=web)). |
| [setVideoRenderParams](https://www.tencentcloud.com/document/product/647/51012#setVideoRenderParams) | Установить режим отрисовки видео. |
| [setVideoEncoderParams](https://www.tencentcloud.com/document/product/647/51012#setVideoEncoderParams) | Установить параметры кодирования видеокодека. |
| [getTRTCCloudInstance](https://www.tencentcloud.com/document/product/647/51012#getTRTCCloudInstance) | Продвинутые функции. |
| [setBeautyLevel](https://www.tencentcloud.com/document/product/647/51012#setBeautyLevel) | Установить уровень красоты, поддержка отключения красоты по умолчанию. |

## Детали

### createInstance

Этот API используется для создания синглтона `TUICallEngine`.

```
- (TUICallEngine *)createInstance;
```

### destroyInstance

Этот API используется для уничтожения синглтона `TUICallEngine`.

```
- (void)destroyInstance;
```

### init

Этот API используется для инициализации `TUICallEngine`. Вызовите его для аутентификации сервиса вызовов и выполнения других необходимых действий перед вызовом других API.

```
- (void)init:(NSString *)sdkAppID userId:(NSString *)userId userSig:(NSString *)userSig succ:(TUICallSucc)succ fail:(TUICallFail)fail;
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| sdkAppID | NSString | Вы можете просмотреть `SDKAppID` в консоли TRTC в разделе [Application Management](https://console.tencentcloud.com/trtc/app) > **Application Info**. |
| userId | NSString | ID текущего пользователя, строка, которая может содержать только буквы (a-z и A-Z), цифры (0-9), дефисы (-) и подчеркивания (_). |
| userSig | NSString | Защищенная подпись Tencent Cloud. О том, как её вычислить и использовать, см. [UserSig](https://www.tencentcloud.com/document/product/647/35166?lang=en&pg=). |

### addObserver

Этот API используется для регистрации слушателя событий для прослушивания событий [TUICallObserver](https://www.tencentcloud.com/document/product/647/51013).

```
- (void)addObserver:(id<TUICallObserver>)observer;
```

### removeObserver

Этот API используется для отмены регистрации слушателя событий.

```
- (void)removeObserver:(id<TUICallObserver>)observer;
```

### calls

Инициировать вызов.

```
- (void)calls:(NSArray<NSString *> *)userIdList callMediaType:(TUICallMediaType)callMediaType params:(TUICallParams *)params succ:(TUICallSucc)succ fail:(TUICallFail)fail;
```

Параметры описаны ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| userIdList | NSArray | Список ID целевых пользователей |
| callMediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54902#TUICallMediaType) | Тип медиа вызова, например видео вызов или голосовой вызов |
| params | [TUICallParams](https://www.tencentcloud.com/document/product/647/54902#TUICallParams) | Параметры расширения вызова, такие как номер комнаты, время ожидания приглашения, контент автономной отправки и т. д. |

### join

Активно присоединиться к вызову.

```
- (void)join:(NSString *)callId succ:(TUICallSucc)succ fail:(TUICallFail)fail
```

Параметры описаны ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| callId | NSString | Уникальный ID для этого вызова |

### accept

Этот API используется для принятия вызова. После получения обратного вызова `onCallReceived()` вы можете вызвать этот API для принятия вызова.

```
- (void)accept:(TUICallSucc)succ fail:(TUICallFail)fail;
```

### reject

Этот API используется для отклонения вызова. После получения обратного вызова `onCallReceived()` вы можете вызвать этот API для отклонения вызова.

```
- (void)reject:(TUICallSucc)succ fail:(TUICallFail)fail;
```

### ignore

Этот API используется для игнорирования вызова. После получения `onCallReceived()` вы можете вызвать этот API для игнорирования вызова. Вызывающий абонент получит обратный вызов `onUserLineBusy`.

Примечание: Если ваш проект предполагает трансляцию или конференцию, вы также можете использовать этот API для реализации функции «на встречу» или «в эфире».

```
- (void)ignore:(TUICallSucc)succ fail:(TUICallFail)fail;
```

### hangup

Этот API используется для завершения вызова.

```
- (void)hangup:(TUICallSucc)succ fail:(TUICallFail)fail;
```

### inviteUser

Этот API используется для приглашения пользователей на текущий вызов.

Этот API вызывается участником вызова для приглашения новых пользователей.

```
- (void)inviteUser:(NSArray<NSString *> *)userIdList params:(TUICallParams *)params succ:(void(^)(NSArray <NSString *> *userIdList))succ fail:(TUICallFail)fail
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userIdList | NSArray | ID целевых пользователей. |
| params | [TUICallParams](https://www.tencentcloud.com/document/product/647/54902#TUICallParams) | Дополнительный параметр, такой как roomID, время ожидания вызова, информация об автономной отправке и т. д. |

> **Примечание:** В этом случае пользовательский `RoomId` является недействительным. SDK пригласит других присоединиться к комнате, в которой находится приглашающий.

### startRemoteView

Этот API используется для установки объекта представления для отображения удаленного видео.

```
- (void)startRemoteView:(NSString *)userId videoView:(TUIVideoView *)videoView onPlaying:(void(^)(NSString *userId))onPlaying onLoading:(void(^)(NSString *userId))onLoading onError:(void(^)(NSString *userId, int code, NSString *errMsg))onError;
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | NSString | ID целевого пользователя. |
| videoView | TUIVideoView | Представление для отрисовки. |

### stopRemoteView

Этот API используется для отписки от видеопотока удаленного пользователя.

```
- (void)stopRemoteView:(NSString *)userId;
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | NSString | ID целевого пользователя. |

### openCamera

Этот API используется для включения камеры.

```
- (void)openCamera:(TUICamera)camera videoView:(TUIVideoView *)videoView succ:(TUICallSucc)succ fail:(TUICallFail)fail;
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| camera | [TUICamera](https://www.tencentcloud.com/document/product/647/54902#TUICamera) | Фронтальная или задняя камера. |
| videoView | TUIVideoView | Представление для отрисовки. |

### closeCamera

Этот API используется для отключения камеры.

```
- (void)closeCamera;
```

### switchCamera

Этот API используется для переключения между фронтальной и задней камерами.

```
- (void)switchCamera:(TUICamera)camera;
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| camera | [TUICamera](https://www.tencentcloud.com/document/product/647/54902#TUICamera) | Фронтальная или задняя камера. |

### openMicrophone

Этот API используется для включения микрофона.

```
- (void)openMicrophone:(TUICallSucc)succ fail:(TUICallFail)fail;
```

### closeMicrophone

Этот API используется для отключения микрофона.

```
- (void)closeMicrophone;
```

### selectAudioPlaybackDevice

Этот API используется для выбора устройства воспроизведения аудио (наушники и громкоговоритель). В сценариях вызовов вы можете использовать этот API для включения/отключения режима громкой связи.

```
- (void)selectAudioPlaybackDevice:(TUIAudioPlaybackDevice)device;
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| device | [TUIAudioPlaybackDevice](https://www.tencentcloud.com/document/product/647/54902#TUIAudioPlaybackDevice) | Наушники и громкоговоритель. |

### setSelfInfo

Этот API используется для установки прозвища и аватара. Прозвище не может превышать 500 байт, а аватар указывается через URL.

```
- (void)setSelfInfo:(NSString * _Nullable)nickName avatar:(NSString * _Nullable)avatar succ:(TUICallSucc)succ fail:(TUICallFail)fail;
```

### enableMultiDeviceAbility

Этот API используется для установки, нужно ли включить вход с нескольких устройств для `TUICallEngine` (поддерживается [пакетом Group Call](https://trtc.io/document/54632?platform=ios&product=call&menulabel=web)).

```
- (void)enableMultiDeviceAbility:(BOOL)enable succ:(TUICallSucc)succ fail:(TUICallFail)fail;
```

### setVideoRenderParams

Установить режим отрисовки видеоизображения.

```
- (void)setVideoRenderParams:(NSString *)userId params:(TUIVideoRenderParams *)params succ:(TUICallSucc)succ fail:(TUICallFail)fail;
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | NSString | ID целевого пользователя. |
| params | [TUIVideoRenderParams](https://www.tencentcloud.com/document/product/647/54902#TUIVideoRenderParams) | Параметры отрисовки видео. |

### setVideoEncoderParams

Установить параметры кодирования видеокодека.

Этот параметр может определить качество изображения, просматриваемого удаленными пользователями, что также является качеством изображения в облачных файлах записи.

```
- (void)setVideoEncoderParams:(TUIVideoEncoderParams *)params succ:(TUICallSucc)succ fail:(TUICallFail)fail;
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| params | [TUIVideoEncoderParams](https://www.tencentcloud.com/document/product/647/54902#TUIVideoEncoderParams) | Параметры кодирования видео |

### getTRTCCloudInstance

Продвинутые функции.

```
- (TRTCCloud *)getTRTCCloudInstance;
```

### setBeautyLevel

Установить уровень красоты, поддержка отключения красоты по умолчанию.

```
- (void)setBeautyLevel:(CGFloat)level succ:(TUICallSucc)succ fail:(TUICallFail)fail;
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| level | CGFloat | Уровень красоты, диапазон: 0 - 9, 0 означает отключение эффекта, 9 означает наиболее очевидный эффект. |

## Устаревший интерфейс

### call

Этот API используется для совершения личного вызова. **Примечание: рекомендуется использовать API calls.**

```
- (void)call:(NSString *)userId callMediaType:(TUICallMediaType)callMediaType params:(TUICallParams *)params succ:(TUICallSucc)succ fail:(TUICallFail)fail
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | NSString | ID целевого пользователя. |
| callMediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54902#TUICallMediaType) | Тип вызова, который может быть видео или аудио. |
| params | [TUICallParams](https://www.tencentcloud.com/document/product/647/54902#TUICallParams) | Дополнительный параметр, такой как roomID, время ожидания вызова, информация об автономной отправке и т. д. |

### groupCall

Этот API используется для совершения группового вызова. **Примечание: рекомендуется использовать API calls.**

```
- (void)groupCall:(NSString *)groupId userIdList:(NSArray <NSString *> *)userIdList callMediaType:(TUICallMediaType)callMediaType params:(TUICallParams *)params succ:(TUICallSucc)succ fail:(TUICallFail)fail
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| groupId | NSString | ID группы. |
| userIdList | NSArray | ID целевых пользователей. |
| callMediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54902#MediaType) | Тип вызова, который может быть видео или аудио. |
| params | [TUICallParams](https://www.tencentcloud.com/document/product/647/54902#TUICallParams) | Дополнительный параметр, такой как roomID, время ожидания вызова, информация об автономной отправке и т. д. |

### joinInGroupCall

Этот API используется для присоединения к групповому вызову.

Этот API вызывается членом группы для присоединения к групповому вызову. **Примечание: рекомендуется использовать API join.**

```
- (void)joinInGroupCall:(TUIRoomId *)roomId groupId:(NSString *)groupId callMediaType:(TUICallMediaType)callMediaType succ:(TUICallSucc)succ fail:(TUICallFail)fail;
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | [TUIRoomId](https://www.tencentcloud.com/document/product/647/54902#TUIRoomId) | ID комнаты. |
| groupId | NSString | ID группы. |
| callMediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54902#TUICallMediaType) | Тип вызова, который может быть видео или аудио. |

### switchCallMediaType

Этот API используется для изменения типа вызова.

```
- (void)switchCallMediaType:(TUICallMediaType)newType;
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| callMediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54902#TUICallMediaType) | Тип вызова, который может быть видео или аудио. |


---
*Источник: [https://trtc.io/document/51012](https://trtc.io/document/51012)*

---
*Источник (EN): [tuicallengine.md](./tuicallengine.md)*

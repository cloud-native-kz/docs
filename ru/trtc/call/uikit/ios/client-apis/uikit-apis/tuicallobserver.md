# TUICallObserver

## API интерфейсов TUICallObserver

`TUICallObserver` — это класс обратных вызовов `TUICallEngine`. Вы можете использовать его для отслеживания событий.

## Обзор

| API | Описание |
| --- | --- |
| [onError](https://www.tencentcloud.com/document/product/647/51013#onError) | Произошла ошибка во время звонка. |
| [onCallReceived](https://www.tencentcloud.com/document/product/647/51013#onCallReceived) | Поступил вызов. |
| [onCallBegin](https://www.tencentcloud.com/document/product/647/51013#onCallBegin) | Звонок установлен. |
| [onCallEnd](https://www.tencentcloud.com/document/product/647/51013#onCallEnd) | Звонок завершён. |
| [onCallNotConnected](https://www.tencentcloud.com/document/product/647/51013#onCallNotConnected) | Звонок не соединён. |
| [onUserReject](https://www.tencentcloud.com/document/product/647/51013#onUserReject) | Пользователь отклонил вызов. |
| [onUserNoResponse](https://www.tencentcloud.com/document/product/647/51013#onUserNoResponse) | Пользователь не ответил. |
| [onUserLineBusy](https://www.tencentcloud.com/document/product/647/51013#onUserLineBusy) | Пользователь занят. |
| [onUserInviting](https://www.tencentcloud.com/document/product/647/51013#onUserInviting) | Пользователь приглашён присоединиться к звонку. |
| [onUserJoin](https://www.tencentcloud.com/document/product/647/51013#onUserJoin) | Пользователь присоединился к звонку. |
| [onUserLeave](https://www.tencentcloud.com/document/product/647/51013#onUserLeave) | Пользователь покинул звонок. |
| [onUserVideoAvailable](https://www.tencentcloud.com/document/product/647/51013#onUserVideoAvailable) | Наличие видеопотока у пользователя. |
| [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/51013#onUserAudioAvailable) | Наличие аудиопотока у пользователя. |
| [onUserVoiceVolumeChanged](https://www.tencentcloud.com/document/product/647/51013#onUserVoiceVolumeChanged) | Уровни громкости всех пользователей. |
| [onUserNetworkQualityChanged](https://www.tencentcloud.com/document/product/647/51013#onUserNetworkQualityChanged) | Качество сети всех пользователей. |
| [onKickedOffline](https://www.tencentcloud.com/document/product/647/51013#onKickedOffline) | Текущий пользователь был отключён от системы. |
| [onUserSigExpired](https://www.tencentcloud.com/document/product/647/51013#onUserSigExpired) | Срок действия userSig истёк. |

## Подробное описание

### onError

Произошла ошибка.

> **Примечание:** Этот обратный вызов указывает, что SDK столкнулась с неустранимой ошибкой. Такие ошибки должны быть отслежены, и при необходимости пользователю следует показать сообщение об ошибке в интерфейсе.

```
- (void)onError:(int)code message:(NSString * _Nullable)message;
```

Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| code | int | Код ошибки. |
| message | NSString | Сообщение об ошибке. |

### onCallReceived

Было получено приглашение на звонок. Этот обратный вызов получает вызываемый. Вы можете прослушать это событие, чтобы определить, следует ли отображать представление входящего вызова.

```
- (void)onCallReceived:(NSString *)callId callerId:(NSString *)callerId calleeIdList:(NSArray<NSString *> *)calleeIdList mediaType:(TUICallMediaType)mediaType info:(TUICallObserverExtraInfo *)info;
```

Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| callId | NSString | Уникальный ID звонка |
| callerId | NSString | ID инициатора звонка |
| calleeIdList | NSArray | Список ID вызываемых |
| mediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54902#TUICallMediaType) | Тип вызова (видео или аудио). |
| info | [TUICallObserverExtraInfo](https://www.tencentcloud.com/document/product/647/54902#TUICallObserverExtraInfo) | Дополнительная информация |

### onCallBegin

Звонок установлен. Этот обратный вызов получают как инициатор, так и вызываемые. Вы можете прослушать это событие, чтобы определить, следует ли запустить облачную запись, модерацию контента или другие задачи.

```
- (void)onCallBegin:(NSString *)callId mediaType:(TUICallMediaType)mediaType info:(TUICallObserverExtraInfo *)info;
```

Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| callId | NSString | Уникальный ID звонка |
| mediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54902#TUICallMediaType) | Тип вызова (видео или аудио). |
| info | [TUICallObserverExtraInfo](https://www.tencentcloud.com/document/product/647/54902#TUICallObserverExtraInfo) | Дополнительная информация |

### onCallEnd

Звонок завершился. Этот обратный вызов получают как инициатор, так и вызываемые. Вы можете прослушать это событие, чтобы определить, когда отображать информацию о звонке (например, продолжительность и тип вызова) или остановить облачную запись.

```
- (void)onCallEnd:(NSString *)callId mediaType:(TUICallMediaType)mediaType reason:(TUICallEndReason)reason userId:(NSString *)userId totalTime:(float)totalTime info:(TUICallObserverExtraInfo *)info;
```

Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| callId | NSString | Уникальный ID звонка |
| mediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54902#TUICallMediaType) | Тип вызова (видео или аудио). |
| reason | [TUICallEndReason](https://www.tencentcloud.com/document/product/647/54902#TUICallEndReason) | Причина завершения звонка |
| userId | NSString | ID пользователя, завершившего звонок |
| totalTime | float | Продолжительность звонка. |
| info | [TUICallObserverExtraInfo](https://www.tencentcloud.com/document/product/647/54902#TUICallObserverExtraInfo) | Дополнительная информация |

> **Примечание:** Обратные вызовы на стороне клиента часто теряются при возникновении ошибок, например при закрытии процесса. Если вам нужно измерить продолжительность звонка для целей выставления счетов или других целей, рекомендуется использовать API RESTful.

### onCallNotConnected

Это указывает на то, что звонок был отменён инициатором, истекло время ожидания вызываемого, звонок был отклонён вызываемым или вызываемый был занят. Существует несколько различных сценариев. Вы можете прослушать это событие для реализации логики пользовательского интерфейса, такой как пропущенные вызовы и сброс состояния интерфейса.

- Отмена звонка инициатором: инициатор получает обратный вызов (userId — это его ID); вызываемый получает обратный вызов (userId — это ID инициатора)
- Истечение времени ожидания вызываемого: инициатор одновременно получит обратные вызовы [onUserNoResponse](#onUserNoResponse) и onCallNotConnected (userId — это его ID); вызываемый получает обратный вызов onCallNotConnected (userId — это его ID)
- Отклонение вызова вызываемым: инициатор одновременно получит обратные вызовы [onUserReject](#onUserReject) и onCallNotConnected (userId — это его ID); вызываемый получает обратный вызов onCallNotConnected (userId — это его ID)
- Вызываемый занят: инициатор одновременно получит обратные вызовы [onUserLineBusy](#onUserLineBusy) и onCallNotConnected (userId — это его ID);
- Аномальное прерывание: вызываемый не смог получить звонок, он получает этот обратный вызов (userId — это его ID).

```
- (void)onCallNotConnected:(NSString *)callId mediaType:(TUICallMediaType)mediaType reason:(TUICallEndReason)reaso userId:(NSString *)userId info:(TUICallObserverExtraInfo *)info
```

Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| callId | NSString | Уникальный ID звонка |
| mediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54902#TUICallMediaType) | Тип вызова (видео или аудио). |
| reason | [TUICallEndReason](https://www.tencentcloud.com/document/product/647/54902#TUICallEndReason) | Причина, по которой звонок не был соединён |
| userId | NSString | ID пользователя, который не соединился |
| info | [TUICallObserverExtraInfo](https://www.tencentcloud.com/document/product/647/54902#TUICallObserverExtraInfo) | Дополнительная информация |

### onUserReject

Звонок был отклонён. При одиночном звонке этот обратный вызов получит только инициатор. При групповом звонке этот обратный вызов получат все вызываемые.

```
- (void)onUserReject:(NSString *)userId;
```

Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | NSString | ID пользователя (вызываемого), который отклонил звонок. |

### onUserNoResponse

Пользователь не ответил.

```
- (void)onUserNoResponse:(NSString *)userId;
```

Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | NSString | ID пользователя (вызываемого), который не ответил. |

### onUserLineBusy

Пользователь занят.

```
- (void)onUserLineBusy:(NSString *)userId;
```

Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | NSString | ID пользователя (вызываемого), который занят. |

### onUserInviting

Пользователь приглашён присоединиться к звонку.

```
- (void)onUserInviting:(NSString *)userId;
```

Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | NSString | ID приглашённого пользователя. |

### onUserJoin

Пользователь присоединился к звонку.

```
- (void)onUserJoin:(NSString *)userId;
```

Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | NSString | ID пользователя, который присоединился к звонку. |

### onUserLeave

Пользователь покинул звонок.

```
- (void)onUserLeave:(NSString *)userId;
```

Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | NSString | ID пользователя, который покинул звонок. |

### onUserVideoAvailable

Отправляет ли пользователь видео.

```
- (void)onUserVideoAvailable:(NSString *)userId isVideoAvailable:(BOOL)isVideoAvailable;
```

Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | NSString | ID пользователя. |
| isVideoAvailable | BOOL | Наличие видео у пользователя. |

### onUserAudioAvailable

Отправляет ли пользователь аудио.

```
- (void)onUserAudioAvailable:(NSString *)userId isAudioAvailable:(BOOL)isAudioAvailable;
```

Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | NSString | ID пользователя. |
| isAudioAvailable | BOOL | Наличие аудио у пользователя. |

### onUserVoiceVolumeChanged

Громкость всех пользователей.

```
- (void)onUserVoiceVolumeChanged:(NSDictionary <NSString *, NSNumber *> *)volumeMap;
```

Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| volumeMap | NSDictionary | Таблица громкости, которая включает громкость каждого пользователя (`userId`). Диапазон значений: 0-100. |

### onUserNetworkQualityChanged

Качество сети всех пользователей.

```
- (void)onUserNetworkQualityChanged:(NSArray<TUINetworkQualityInfo *> *)networkQualityList;
```

Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| networkQualityList | NSArray | Текущие сетевые условия для всех пользователей (`userId`). |

### onKickedOffline

Текущий пользователь был отключён от системы. В этом случае вы можете показать пользователю сообщение в интерфейсе и затем снова вызвать `init`.

```
- (void)onKickedOffline;
```

### onUserSigExpired

Срок действия userSig истёк. В этом случае вам нужно сгенерировать новый `userSig`, а затем снова вызвать `init`.

```
- (void)onUserSigExpired;
```

## Устаревший интерфейс

### onCallCancelled

Звонок был отменён инициатором или истекло время ожидания. Этот обратный вызов получает вызываемый. Вы можете прослушать это событие, чтобы определить, следует ли показать сообщение о пропущенном звонке.

Это указывает на то, что звонок был отменён инициатором, истекло время ожидания вызываемого, звонок был отклонён вызываемым или вызываемый был занят. Существует несколько различных сценариев. Вы можете прослушать это событие для реализации логики пользовательского интерфейса, такой как пропущенные вызовы и сброс состояния интерфейса.

- Отмена звонка инициатором: инициатор получает обратный вызов (userId — это его ID); вызываемый получает обратный вызов (userId — это ID инициатора)
- Истечение времени ожидания вызываемого: инициатор одновременно получит обратные вызовы [onUserNoResponse](#onUserNoResponse) и onCallCancelled (userId — это его ID); вызываемый получает обратный вызов onCallCancelled (userId — это его ID)
- Отклонение вызова вызываемым: инициатор одновременно получит обратные вызовы [onUserReject](#onUserReject) и onCallCancelled (userId — это его ID); вызываемый получает обратный вызов onCallCancelled (userId — это его ID)
- Вызываемый занят: инициатор одновременно получит обратные вызовы [onUserLineBusy](#onUserLineBusy) и onCallCancelled (userId — это его ID);
- Аномальное прерывание: вызываемый не смог получить звонок, он получает этот обратный вызов (userId — это его ID).

```
- (void)onCallCancelled:(NSString *)callerId;
```

Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| callerId | NSString | ID пользователя инициатора. |

### onCallMediaTypeChanged

Тип вызова изменился.

```
- (void)onCallMediaTypeChanged:(TUICallMediaType)oldCallMediaType newCallMediaType:(TUICallMediaType)newCallMediaType;
```

Описание параметров:

| Параметр | Тип | Описание |
| --- | --- | --- |
| oldCallMediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54902#TUICallMediaType) | Тип вызова до изменения. |
| newCallMediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54902#TUICallMediaType) | Тип вызова после изменения. |


---
*Источник: [https://trtc.io/document/51013](https://trtc.io/document/51013)*

---
*Источник (EN): [tuicallobserver.md](./tuicallobserver.md)*

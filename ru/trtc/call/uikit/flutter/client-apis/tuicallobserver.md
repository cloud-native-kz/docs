# TUICallObserver

## API TUICallObserver

`TUICallObserver` — это класс обратного вызова для `TUICallEngine`. Вы можете использовать его для прослушивания событий.

## Обзор

| API | Описание |
| --- | --- |
| [onError](https://www.tencentcloud.com/document/product/647/54908#onError) | Во время вызова произошла ошибка. |
| [onUserInviting](https://www.tencentcloud.com/document/product/647/54908#onUserInviting) | Обратный вызов, когда пользователь приглашается присоединиться к вызову. |
| [onCallReceived](https://www.tencentcloud.com/document/product/647/54908#onCallReceived) | Получено приглашение на вызов. |
| [onCallNotConnected](https://www.tencentcloud.com/document/product/647/54908#onCallNotConnected) | Обратный вызов отмены вызова |
| [onCallBegin](https://www.tencentcloud.com/document/product/647/54908#onCallBegin) | Вызов подключен. |
| [onCallEnd](https://www.tencentcloud.com/document/product/647/54908#onCallEnd) | Вызов завершен. |
| [onCallMediaTypeChanged](https://www.tencentcloud.com/document/product/647/54908#onCallMediaTypeChanged) | Тип вызова изменился. |
| [onUserReject](https://www.tencentcloud.com/document/product/647/54908#onUserReject) | Пользователь отклонил вызов. |
| [onUserNoResponse](https://www.tencentcloud.com/document/product/647/54908#onUserNoResponse) | Пользователь не ответил. |
| [onUserLineBusy](https://www.tencentcloud.com/document/product/647/54908#onUserLineBusy) | Пользователь занят. |
| [onUserJoin](https://www.tencentcloud.com/document/product/647/54908#onUserJoin) | Пользователь присоединился к вызову. |
| [onUserLeave](https://www.tencentcloud.com/document/product/647/54908#onUserLeave) | Пользователь покинул вызов. |
| [onUserVideoAvailable](https://www.tencentcloud.com/document/product/647/54908#onUserVideoAvailable) | Доступен ли видеопоток пользователя. |
| [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/54908#onUserAudioAvailable) | Доступен ли аудиопоток пользователя. |
| [onUserVoiceVolumeChanged](https://www.tencentcloud.com/document/product/647/54908#onUserVoiceVolumeChanged) | Уровни громкости всех пользователей. |
| [onUserNetworkQualityChanged](https://www.tencentcloud.com/document/product/647/54908#onUserNetworkQualityChanged) | Качество сети всех пользователей. |
| [onKickedOffline](https://www.tencentcloud.com/document/product/647/54908#onKickedOffline) | Текущий пользователь был отключен. |
| [onUserSigExpired](https://www.tencentcloud.com/document/product/647/54908#onUserSigExpired) | Истек срок действия userSig. |

## Подробности

Прослушивайте события, генерируемые плагином Flutter через addObserver.

```
TUICallEngine.instance.addObserver(TUICallObserver(    onError: (int code, String message) {          },onCallCancelled: (String callerId) {           }, onCallBegin: (TUIRoomId roomId, TUICallMediaType callMediaType, TUICallRole callRole) {           }, onCallEnd: (TUIRoomId roomId, TUICallMediaType callMediaType, TUICallRole callRole, double totalTime) {           }, onCallMediaTypeChanged: (TUICallMediaType oldCallMediaType, TUICallMediaType newCallMediaType) {         }, onUserReject: (String userId) {        }, onUserNoResponse: (String userId) {         }, onUserLineBusy: (String onUserLineBusy) {        }, onUserJoin: (String userId) {      }, onUserLeave: (String userId) {           }, onUserVideoAvailable: (String userId, bool isVideoAvailable) {              }, onUserAudioAvailable: (String userId, bool isAudioAvailable) {             }, onUserNetworkQualityChanged: (List<TUINetworkQualityInfo> networkQualityList) {      }, onCallReceived: (String callerId, List<String> calleeIdList, String groupId, TUICallMediaType callMediaType) {      }, onUserVoiceVolumeChanged: (Map<String, int> volumeMap) {        }, onKickedOffline: () {        }, onUserSigExpired: () {         }  ));
```

### onError

Произошла ошибка.

> **Примечание:** Этот обратный вызов указывает на то, что SDK столкнулся с неустранимой ошибкой. Такие ошибки должны быть прослушаны, и при необходимости пользователям должны быть отправлены уведомления в интерфейс.

```
TUICallEngine.instance.addObserver(TUICallObserver(    onError: (int code, String message) {    }));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| code | int | Код ошибки. |
| message | String | Сообщение об ошибке. |

### onUserInviting

Обратный вызов, когда пользователь приглашается присоединиться к вызову.

```
TUICallEngine.instance.addObserver(TUICallObserver(    onUserInviting: (String userId) {      // TODO    }));
```

Параметры указаны в таблице ниже.

| Параметр | Тип | Значение |
| --- | --- | --- |
| userId | String | ID приглашенного пользователя |

### onCallReceived

Получено уведомление о новом входящем запросе вызова, его получит вызываемый. Вы можете прослушать это событие, чтобы определить, следует ли показывать интерфейс ответа на вызов.

```
TUICallEngine.instance.addObserver(TUICallObserver(    onCallReceived: (String callId, String callerId, List<String> calleeIdList, TUICallMediaType mediaType, CallObserverExtraInfo info) {      // TODO    }));
```

Параметры указаны в таблице ниже.

| Параметр | Тип | Значение |
| --- | --- | --- |
| callId | String | Уникальный ID этого вызова |
| callerId | String | ID звонящего (инициатор) |
| calleeIdList | List<String> | Список ID вызываемых (приглашенные) |
| mediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54909#TUICallMediaType) | Тип медиа вызова. Например: `TUICallMediaType.video` или `TUICallMediaType.audio` |
| info | [CallObserverExtraInfo](https://www.tencentcloud.com/document/product/647/54909#CallObserverExtraInfo) | Дополнительная информация |

### onCallNotConnected

Обратный вызов отмены вызова.

```
TUICallEngine.instance.addObserver(TUICallObserver(  onCallNotConnected: (String callId, TUICallMediaType mediaType, CallEndReason reason,    String userId, CallObserverExtraInfo info) {    // TODO  }));
```

Параметры указаны в таблице ниже.

| Параметр | Тип | Значение |
| --- | --- | --- |
| callId | String | Уникальный ID этого вызова |
| mediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54909#TUICallMediaType) | Тип медиа вызова. Например: `TUICallMediaType.video` или `TUICallMediaType.audio` |
| reason | [CallEndReason](https://www.tencentcloud.com/document/product/647/54909#CallEndReason) | Причины завершения вызова |
| userId | String | ID пользователя, завершившего вызов |
| info | [CallObserverExtraInfo](https://www.tencentcloud.com/document/product/647/54909#CallObserverExtraInfo) | Дополнительная информация |

### onCallBegin

Указывает на то, что вызов подключен, и оба участника (звонящий и вызываемый) могут его получить. Вы можете прослушать это событие, чтобы начать такие процессы, как облачная запись и проверка контента.

```
TUICallEngine.instance.addObserver(TUICallObserver(    onCallBegin: (String callId, TUICallMediaType mediaType, CallObserverExtraInfo info) {    // TODO  }));
```

Параметры указаны в таблице ниже.

| Параметр | Тип | Значение |
| --- | --- | --- |
| callId | String | Уникальный ID этого вызова |
| mediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54909#TUICallMediaType) | Тип медиа вызова. Например: `TUICallMediaType.video` или `TUICallMediaType.audio` |
| info | [CallObserverExtraInfo](https://www.tencentcloud.com/document/product/647/54909#CallObserverExtraInfo) | Дополнительная информация |

### onCallEnd

Указывает на то, что вызов завершен, и оба участника (звонящий и вызываемый) могут его получить. Вы можете прослушать это событие, чтобы отобразить информацию, такую как продолжительность вызова и тип вызова, или остановить процесс облачной записи.

```
TUICallEngine.instance.addObserver(TUICallObserver(    onCallEnd: (String callId, TUICallMediaType mediaType, CallEndReason reason,        String userId, double totalTime, CallObserverExtraInfo info) {    // TODO  }));
```

Параметры указаны в таблице ниже.

| Параметр | Тип | Значение |
| --- | --- | --- |
| callId | String | Уникальный ID этого вызова |
| mediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54909#TUICallMediaType) | Тип медиа вызова. Например: `TUICallMediaType.video` или `TUICallMediaType.audio` |
| reason | [CallEndReason](https://www.tencentcloud.com/document/product/647/54909#CallEndReason) | Причины завершения вызова |
| userId | String | ID пользователя, завершившего вызов |
| totalTime | double | Продолжительность этого вызова, единица измерения мс |
| info | [CallObserverExtraInfo](https://www.tencentcloud.com/document/product/647/54909#CallObserverExtraInfo) | Дополнительная информация |

> **Примечание:** События на стороне клиента обычно теряются из-за исключений, таких как завершение процесса. Если вам необходимо завершить логику выставления счетов путем мониторинга продолжительности вызова, рекомендуется использовать REST API для выполнения таких процессов.

### onCallMediaTypeChanged

Тип вызова изменился.

```
TUICallEngine.instance.addObserver(TUICallObserver(    onCallMediaTypeChanged: (TUICallMediaType oldCallMediaType, TUICallMediaType newCallMediaType) {      }));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| oldCallMediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54909#TUICallMediaType) | Тип вызова до изменения. |
| newCallMediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54909#TUICallMediaType) | Тип вызова после изменения. |

### onUserReject

Вызов был отклонен. В одноранговом вызове только инициатор получит этот обратный вызов. В групповом вызове все приглашенные получат этот обратный вызов.

```
TUICallEngine.instance.addObserver(TUICallObserver(    onUserReject: (String userId) {        }));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| res.userId | String | ID пользователя приглашенного, который отклонил вызов. |

### onUserNoResponse

Пользователь не ответил.

```
TUICallEngine.instance.addObserver(TUICallObserver(    onUserNoResponse: (String userId) {     }));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя приглашенного, который не ответил. |

### onUserLineBusy

Пользователь занят.

```
TUICallEngine.instance.addObserver(TUICallObserver(    onUserLineBusy: (String onUserLineBusy) {       },));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя приглашенного, который занят. |

### onUserJoin

Пользователь присоединился к вызову.

```
TUICallEngine.instance.addObserver(TUICallObserver(    onUserJoin: (String userId) {      }));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя, присоединившегося к вызову. |

### onUserLeave

Пользователь покинул вызов.

```
TUICallEngine.instance.addObserver(TUICallObserver(    onUserLeave: (String userId) {         }));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя, покинувшего вызов. |

### onUserVideoAvailable

Отправляет ли пользователь видео.

```
TUICallEngine.instance.addObserver(TUICallObserver(    onUserVideoAvailable: (String userId, bool isVideoAvailable) {       }));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя. |
| isVideoAvailable | bool | Доступно ли видео у пользователя. |

### onUserAudioAvailable

Отправляет ли пользователь аудио.

```
TUICallEngine.instance.addObserver(TUICallObserver(    onUserAudioAvailable: (String userId, bool isAudioAvailable) {           }));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя. |
| isAudioAvailable | bool | Доступно ли аудио у пользователя. |

### onUserVoiceVolumeChanged

Громкость всех пользователей.

```
TUICallEngine.instance.addObserver(TUICallObserver(    onUserVoiceVolumeChanged: (Map<String, int> volumeMap) {      }));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| volumeMap | Map<String, int> | Таблица громкости, которая включает громкость каждого пользователя (userId). Диапазон значений: 0-100. |

### onUserNetworkQualityChanged

Качество сети всех пользователей.

```
TUICallEngine.instance.addObserver(TUICallObserver(    onUserNetworkQualityChanged: (List<TUINetworkQualityInfo> networkQualityList) {    }));class TUINetworkQualityInfo {        String userId;      TUINetworkQuality quality;      TUINetworkQualityInfo({required this.userId, required this.quality});}enum TUINetworkQuality {    unknown,    excellent,  good,    poor,    bad,    vBad,    down}
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| networkQualityList | List<[TUINetworkQualityInfo](https://www.tencentcloud.com/document/product/647/54909#89efd105-cdee-4f3f-bde1-5db01af79d56)> | Текущие условия сети для всех пользователей (userId). |

### onKickedOffline

Текущий пользователь был отключен. В этом случае вы можете предупредить пользователя с помощью сообщения интерфейса, а затем вызвать `init` снова.

```
TUICallEngine.instance.addObserver(TUICallObserver(    onKickedOffline: () {     }));
```

### onUserSigExpired

Истек срок действия userSig. В этом случае вам необходимо создать новый `userSig`, а затем вызвать `init` снова.

```
TUICallEngine.instance.addObserver(TUICallObserver(    onUserSigExpired: () {        }  ));
```

## Устаревшие интерфейсы

### onCallCancelled

Вызов был отменен инициатором или истекло время ожидания. Этот обратный вызов получает вызываемый. Вы можете прослушать это событие, чтобы определить, следует ли показать сообщение о пропущенном вызове.

Это указывает на то, что вызов был отменен звонящим, истекло время ожидания вызываемого, вызов был отклонен вызываемым или вызываемый был занят. Задействовано несколько сценариев. Вы можете прослушать это событие, чтобы реализовать логику интерфейса, такую как пропущенные вызовы и сброс статуса интерфейса.

- Отмена вызова звонящим: звонящий получает обратный вызов (userId — сам звонящий); вызываемый получает обратный вызов (userId — ID звонящего).
- Истечение времени вызываемого: звонящий одновременно получит обратные вызовы [onUserNoResponse](https://www.tencentcloud.com/document/product/647/54908#onUserNoResponse) и onCallCancelled (userId — его собственный ID); вызываемый получит обратный вызов onCallCancelled (userId — его собственный ID).
- Отклонение вызываемым: звонящий одновременно получит обратные вызовы [onUserReject](https://www.tencentcloud.com/document/product/647/54908#onUserReject) и onCallCancelled (userId — его собственный ID); вызываемый получит обратный вызов onCallCancelled (userId — его собственный ID).
- Вызываемый занят: звонящий одновременно получит обратные вызовы [onUserLineBusy](https://www.tencentcloud.com/document/product/647/54908#onUserLineBusy) и onCallCancelled (userId — его собственный ID);
- Аномальное прерывание: вызываемый не смог получить вызов, он получает этот обратный вызов (userId — его собственный ID).

```
TUICallEngine.instance.addObserver(TUICallObserver(    onCallCancelled: (String userId) {        }));
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя инициатора. |


---
*Источник: [https://trtc.io/document/54908](https://trtc.io/document/54908)*

---
*Источник (EN): [tuicallobserver.md](./tuicallobserver.md)*

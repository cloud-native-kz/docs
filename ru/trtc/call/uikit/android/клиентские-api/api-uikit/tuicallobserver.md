# TUICallObserver

## API-интерфейсы TUICallObserver

`TUICallObserver` — это класс обратного вызова `TUICallEngine`. Его можно использовать для прослушивания событий.

## Обзор

| API | Описание |
| --- | --- |
| [onError](https://www.tencentcloud.com/document/product/647/51007#onError) | Произошла ошибка во время звонка. |
| [onCallReceived](https://www.tencentcloud.com/document/product/647/51007#onCallReceived) | Получлено приглашение на звонок. |
| [onCallBegin](https://www.tencentcloud.com/document/product/647/51007#onCallBegin) | Звонок подключен. |
| [onCallEnd](https://www.tencentcloud.com/document/product/647/51007#onCallEnd) | Звонок завершен. |
| [onCallNotConnected](https://www.tencentcloud.com/document/product/647/51007#onCallNotConnected) | Звонок не подключен. |
| [onUserReject](https://www.tencentcloud.com/document/product/647/51007#onUserReject) | Пользователь отклонил звонок. |
| [onUserNoResponse](https://www.tencentcloud.com/document/product/647/51007#onUserNoResponse) | Пользователь не ответил. |
| [onUserLineBusy](https://www.tencentcloud.com/document/product/647/51007#onUserLineBusy) | Пользователь занят. |
| [onUserInviting](https://www.tencentcloud.com/document/product/647/51007#onUserInviting) | Пользователь приглашен присоединиться к звонку. |
| [onUserJoin](https://www.tencentcloud.com/document/product/647/51007#onUserJoin) | Пользователь присоединился к звонку. |
| [onUserLeave](https://www.tencentcloud.com/document/product/647/51007#onUserLeave) | Пользователь покинул звонок. |
| [onUserVideoAvailable](https://www.tencentcloud.com/document/product/647/51007#onUserVideoAvailable) | Есть ли у пользователя видеопоток. |
| [onUserAudioAvailable](https://www.tencentcloud.com/document/product/647/51007#onUserAudioAvailable) | Есть ли у пользователя аудиопоток. |
| [onUserVoiceVolumeChanged](https://www.tencentcloud.com/document/product/647/51007#onUserVoiceVolumeChanged) | Уровни громкости всех пользователей. |
| [onUserNetworkQualityChanged](https://www.tencentcloud.com/document/product/647/51007#onUserNetworkQualityChanged) | Качество сети всех пользователей. |
| [onKickedOffline](https://www.tencentcloud.com/document/product/647/51007#onKickedOffline) | Текущий пользователь отключен от сети. |
| [onUserSigExpired](https://www.tencentcloud.com/document/product/647/51007#onUserSigExpired) | Истек срок действия userSig. |

## Подробное описание

### onError

Произошла ошибка.

> **Примечание:** Этот обратный вызов указывает на то, что SDK столкнулся с неустранимой ошибкой. Такие ошибки необходимо отслеживать, и при необходимости пользователю должно быть выведено уведомление в интерфейсе.

```
void onError(int code, String message);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| code | int | Код ошибки. |
| message | String | Сообщение об ошибке. |

### onCallReceived

Этот обратный вызов получает вызываемый абонент. Вы можете прослушать это событие, чтобы определить, следует ли показывать представление входящего вызова.

```
void onCallReceived(String callId, String callerId, List<String> calleeIdList,                     TUICallDefine.MediaType mediaType, TUICallDefine.CallObserverExtraInfo info);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| callId | String | Уникальный ID этого звонка |
| callerId | String | ID звонящего |
| calleeIdList | List<String> | Список ID вызываемых абонентов |
| mediaType | [TUICallDefine.MediaType](https://www.tencentcloud.com/document/product/647/54900#MediaType) | Тип звонка (видео или аудио). |
| info | [TUICallDefine.CallObserverExtraInfo](https://www.tencentcloud.com/document/product/647/54900#tuicallobserverextrainfo) | Дополнительная информация |

### onCallBegin

Звонок подключен. Этот обратный вызов получают как инициатор, так и вызываемые абоненты. Вы можете прослушать это событие, чтобы определить, следует ли запускать облачную запись, проверку контента или другие задачи.

```
void onCallBegin(String callId, TUICallDefine.MediaType mediaType, TUICallDefine.CallObserverExtraInfo info);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| callId | String | Уникальный ID этого звонка |
| mediaType | [TUICallDefine.MediaType](https://www.tencentcloud.com/document/product/647/54900#MediaType) | Тип звонка (видео или аудио). |
| info | [TUICallDefine.CallObserverExtraInfo](https://www.tencentcloud.com/document/product/647/54900#tuicallobserverextrainfo) | Дополнительная информация |

### onCallEnd

Звонок завершен. Этот обратный вызов получают как инициатор, так и вызываемые абоненты. Вы можете прослушать это событие, чтобы определить, когда следует отображать информацию о звонке (такую как длительность и тип звонка) или остановить облачную запись.

```
void onCallEnd(String callId, TUICallDefine.MediaType mediaType, TUICallDefine.CallEndReason reason,                String userId, long totalTime, TUICallDefine.CallObserverExtraInfo info);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| callId | String | Уникальный ID этого звонка |
| mediaType | [TUICallDefine.MediaType](https://www.tencentcloud.com/document/product/647/54900#MediaType) | Тип звонка (видео или аудио). |
| reason | [TUICallDefine.CallEndReason](https://www.tencentcloud.com/document/product/647/54900#tuicallendreason) | Причина окончания звонка |
| userId | String | ID пользователя, завершившего звонок |
| totalTime | long | Длительность звонка. |
| info | [TUICallDefine.CallObserverExtraInfo](https://www.tencentcloud.com/document/product/647/54900#tuicallobserverextrainfo) | Дополнительная информация |

> **Примечание:** Обратные вызовы на стороне клиента часто теряются при возникновении ошибок, например при закрытии процесса. Если вам нужно измерить длительность звонка в целях выставления счетов или по другим причинам, рекомендуется использовать REST API.

### onCallNotConnected

Звонок был отменен инициатором, истекло время ожидания ответа вызываемого, вызываемый отклонил звонок или был занят. Этот обратный вызов получает вызываемый абонент. Вы можете прослушать это событие, чтобы определить, следует ли показывать сообщение о пропущенном звонке.

Это указывает на то, что звонок был отменен звонящим, истекло время ожидания ответа вызываемого, вызываемый отклонил звонок или был занят. Задействовано несколько сценариев. Вы можете прослушать это событие, чтобы реализовать логику интерфейса пользователя, такую как пропущенные звонки и сброс статуса интерфейса.

- Отмена звонка звонящим: звонящий получает обратный вызов (userId — сам себе); вызываемый получает обратный вызов (userId — ID звонящего)
- Истечение времени ожидания вызываемого: звонящий одновременно получает обратные вызовы [onUserNoResponse](https://www.tencentcloud.com/document/product/647/51007#onusernoresponse) и onCallNotConnected (userId — собственный ID); вызываемый получает обратный вызов onCallNotConnected (userId — собственный ID)
- Отклонение вызываемым: звонящий одновременно получает обратные вызовы [onUserReject](https://www.tencentcloud.com/document/product/647/51007#onuserreject) и onCallNotConnected (userId — собственный ID); вызываемый получает обратный вызов onCallNotConnected (userId — собственный ID)
- Вызываемый занят: звонящий одновременно получает обратные вызовы [onUserLineBusy](https://www.tencentcloud.com/document/product/647/51007#onuserlinebusy) и onCallNotConnected (userId — собственный ID)
- Аномальное прерывание: вызываемый не смог получить звонок (получает этот обратный вызов с userId — собственный ID).

```
void onCallNotConnected(String callId, TUICallDefine.MediaType mediaType, TUICallDefine.CallEndReason reason,                         String userId, TUICallDefine.CallObserverExtraInfo info);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| callId | String | Уникальный ID этого звонка |
| mediaType | [TUICallDefine.MediaType](https://www.tencentcloud.com/document/product/647/54900#MediaType) | Тип звонка (видео или аудио). |
| reason | [TUICallDefine.CallEndReason](https://www.tencentcloud.com/document/product/647/54900#tuicallendreason) | Причина окончания звонка |
| userId | String | ID пользователя, не подключившегося к звонку |
| info | [TUICallDefine.CallObserverExtraInfo](https://www.tencentcloud.com/document/product/647/54900#tuicallobserverextrainfo) | Дополнительная информация |

### onUserReject

Пользователь отклонил звонок. В одноранговом звонке только инициатор получит этот обратный вызов. В групповом звонке все вызываемые абоненты получат этот обратный вызов.

```
void onUserReject(String userId);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя вызываемого абонента, отклонившего звонок. |

### onUserNoResponse

Пользователь не ответил.

```
void onUserNoResponse(String userId);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя вызываемого абонента, не ответившего на звонок. |

### onUserInviting

Пользователь приглашен присоединиться к звонку.

```
void onUserInviting(String userId);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID приглашенного пользователя. |

### onUserLineBusy

Пользователь занят.

```
void onUserLineBusy(String userId);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя вызываемого абонента, который занят. |

### onUserJoin

Пользователь присоединился к звонку.

```
void onUserJoin(String userId);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя, присоединившегося к звонку. |

### onUserLeave

Пользователь покинул звонок.

```
void onUserLeave(String userId);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя, покинувшего звонок. |

### onUserVideoAvailable

Передает ли пользователь видео.

```
void onUserVideoAvailable(String userId, boolean isVideoAvailable);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя. |
| isVideoAvailable | boolean | Есть ли у пользователя видео. |

### onUserAudioAvailable

Передает ли пользователь аудио.

```
void onUserAudioAvailable(String userId, boolean isAudioAvailable);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя. |
| isAudioAvailable | boolean | Есть ли у пользователя аудио. |

### onUserVoiceVolumeChanged

Уровни громкости всех пользователей.

```
void onUserVoiceVolumeChanged(Map<String, Integer> volumeMap);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| volumeMap | Map | Таблица громкости, которая включает уровень громкости каждого пользователя (`userId`). Диапазон значений: 0-100. |

### onUserNetworkQualityChanged

Качество сети всех пользователей.

```
void onUserNetworkQualityChanged(List<TUICallDefine.NetworkQualityInfo> networkQualityList);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| networkQualityList | List | Текущие сетевые условия для всех пользователей (`userId`). |

### onKickedOffline

Текущий пользователь отключен от сети. В этом случае вы можете вывести пользователю сообщение интерфейса, а затем снова вызвать `init`.

```
void onKickedOffline();
```

### onUserSigExpired

Истек срок действия userSig: в этом случае необходимо сгенерировать новый `userSig`, а затем снова вызвать `init`.

```
void onUserSigExpired();
```

## Устаревший интерфейс

### onCallCancelled

Это указывает на то, что звонок был отменен звонящим, истекло время ожидания ответа вызываемого, вызываемый отклонил звонок или был занят. Задействовано несколько сценариев. Вы можете прослушать это событие, чтобы реализовать логику интерфейса пользователя, такую как пропущенные звонки и сброс статуса интерфейса.

- Отмена звонка звонящим: звонящий получает обратный вызов (userId — сам себе); вызываемый получает обратный вызов (userId — ID звонящего)
- Истечение времени ожидания вызываемого: звонящий одновременно получает обратные вызовы [onUserNoResponse](https://www.tencentcloud.com/document/product/647/51007#onusernoresponse) и onCallCancelled (userId — собственный ID); вызываемый получает обратный вызов onCallCancelled (userId — собственный ID)
- Отклонение вызываемым: звонящий одновременно получает обратные вызовы [onUserReject](https://www.tencentcloud.com/document/product/647/51007#onuserreject) и onCallCancelled (userId — собственный ID); вызываемый получает обратный вызов onCallCancelled (userId — собственный ID)
- Вызываемый занят: звонящий одновременно получает обратные вызовы [onUserLineBusy](https://www.tencentcloud.com/document/product/647/51007#onuserlinebusy) и onCallCancelled (userId — собственный ID)
- Аномальное прерывание: вызываемый не смог получить звонок (получает этот обратный вызов с userId — собственный ID).

```
void onCallCancelled(String userId);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя инициатора звонка. |

### onCallMediaTypeChanged

Тип звонка изменился.

```
void onCallMediaTypeChanged(TUICallDefine.MediaType oldCallMediaType,TUICallDefine.MediaType newCallMediaType);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| oldCallMediaType | [TUICallDefine.MediaType](https://www.tencentcloud.com/document/product/647/54900#MediaType) | Тип звонка до изменения. |
| newCallMediaType | [TUICallDefine.MediaType](https://www.tencentcloud.com/document/product/647/54900#MediaType) | Тип звонка после изменения. |


---
*Источник: [https://trtc.io/document/51007](https://trtc.io/document/51007)*

---
*Источник (EN): [tuicallobserver.md](./tuicallobserver.md)*

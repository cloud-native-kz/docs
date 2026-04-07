# TUICallKit

## API TUICallKit

`TUICallKit` — компонент аудио/видеовызовов, **включающий элементы пользовательского интерфейса**. Вы можете использовать его API для быстрой реализации приложения аудио/видеовызовов, аналогичного WeChat. Инструкции по интеграции см. в разделе [Интеграция TUICallKit](https://www.tencentcloud.com/document/product/647/50992).

## Обзор

| API | Описание |
| --- | --- |
| [createInstance](#createInstance) | Создать экземпляр TUICallKit (режим singleton). |
| [setSelfInfo](#setSelfInfo) | Установить фотографию профиля и прозвище пользователя. |
| [calls](#calls) | Инициировать один-на-один или групповой вызов |
| [join](#join) | Активно присоединиться к вызову |
| [setCallingBell](#setCallingBell) | Установить рингтон. |
| [enableMuteMode](#enableMuteMode) | Установить режим отключения звука. |
| [enableFloatWindow](#enableFloatWindow) | Установить, включить ли плавающие окна. |
| [enableVirtualBackground](#enableVirtualBackground) | Установить размытый фон. |
| [enableIncomingBanner](#enableIncomingBanner) | Установить, отображать ли баннер входящего вызова. |
| [setScreenOrientation](#setScreenOrientation) | Установить ориентацию экрана. |

## Подробности

### createInstance

Этот API используется для создания singleton `TUICallKit`.

```
public static func createInstance() -> TUICallKit
```

### setSelfInfo

Этот API используется для установки фотографии профиля и прозвища пользователя. Прозвище не может превышать 500 байт, а фотография профиля указывается по URL.

```
public func setSelfInfo(nickname: String, avatar: String, completion: CompletionClosure?)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| nickname | String | Прозвище. |
| avatar | String | Фотография профиля. |
| completion | CompletionClosure | Обратный вызов результата асинхронной операции. |

### calls

Инициировать вызов.

Swift

```
public func calls(userIdList: [String], callMediaType: CallMediaType, params: CallParams?, completion: CompletionClosure?)
```

Параметры описаны ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| userIdList | [String] | Список ID целевых пользователей |
| mediaType | [CallMediaType](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/callmediatype) | Тип медиа вызова, например видеовызов, голосовой вызов |
| params | [CallParams](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/callparams) | Параметры расширения вызова, такие как номер комнаты, тайм-аут приглашения на вызов |
| completion | CompletionClosure | Обратный вызов результата асинхронной операции |

### join

Активно присоединиться к вызову.

Swift

```
public func join(callId: String, completion: CompletionClosure?)
```

Параметры описаны ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| callId | String | Уникальный ID данного вызова |
| completion | CompletionClosure | Обратный вызов результата асинхронной операции. |

### setCallingBell

Этот API используется для установки рингтона. `filePath` должен быть доступным локальным URL файла.

Установленный рингтон привязан к устройству и не меняется в зависимости от пользователя.

Чтобы сбросить рингтон, передайте пустую строку для `filePath`.

```
public func setCallingBell(filePath: String)
```

### enableMuteMode

Этот API используется для включения/отключения режима без звука.

Значение по умолчанию `false`. Этот API используется для установки, воспроизводить ли музыку при получении вызова пользователем.

```
public func enableMuteMode(enable: Bool)
```

### enableFloatWindow

Этот API используется для установки, включить ли плавающие окна.

Значение по умолчанию `false`, кнопка плавающего окна в верхнем левом углу представления вызова скрыта. Если установить на `true`, кнопка станет видимой.

```
public func enableFloatWindow(enable: Bool)
```

## enableVirtualBackground

Этот API используется для установки размытого фона.

Значение по умолчанию `false`.

```
public func enableVirtualBackground(enable: Bool)
```

### enableIncomingBanner

Этот API используется для установки, отображать ли баннер входящего вызова при получении нового приглашения на вызов.

Значение по умолчанию `false`. При получении приглашения вызываемый абонент по умолчанию видит полноэкранное представление вызова. Если установить на `true`, вызываемый абонент сначала увидит баннер.

```
public func enableIncomingBanner(enable: Bool)
```

### setScreenOrientation

Установить ориентацию экрана.

По умолчанию используется портретный режим; orientation: 0-Portrait, 1-Landscape, 2-Auto.

```
public func setScreenOrientation(orientation: Int, completion: CompletionClosure?)
```

## Устаревший интерфейс

### call

Этот API используется для выполнения один-на-один вызова.

> **Примечание:** Рекомендуется использовать API [calls](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/callstore/calls(participantids:callmediatype:params:completion:))

```
public func call(userId: String, callMediaType: TUICallMediaType)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID целевого пользователя. |
| callMediaType | [TUICallMediaType](https://trtc.io/document/54902?product=call&menulabel=uikit&platform=ios#TUICallMediaType) | Тип вызова, который может быть видео или аудио. |

### call

Этот API используется для выполнения один-на-один вызова с поддержкой пользовательского ID комнаты, тайм-аута вызова, содержимого оффлайн-уведомления и т. д.

> **Примечание:** Рекомендуется использовать API [calls](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/callstore/calls(participantids:callmediatype:params:completion:))

```
public func call(userId: String, callMediaType: TUICallMediaType, params: TUICallParams,                 succ: @escaping TUICallSucc, fail: @escaping TUICallFail)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID целевого пользователя. |
| callMediaType | [TUICallMediaType](https://trtc.io/document/54902?product=call&menulabel=uikit&platform=ios#TUICallMediaType) | Тип вызова, который может быть видео или аудио. |
| params | [TUICallParams](https://trtc.io/document/54902?product=call&menulabel=uikit&platform=ios#TUICallParams) | Параметры расширения вызова, такие как roomID, тайм-аут вызова, информация об оффлайн-уведомлении и т. д. |

### groupCall

Этот API используется для выполнения группового вызова.

> **Примечание:** Рекомендуется использовать API [calls](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/callstore/calls(participantids:callmediatype:params:completion:)). Перед выполнением группового вызова необходимо сначала создать группу Chat. Подробную информацию о создании группы см. в разделе [Управление группами Chat](https://www.tencentcloud.com/en/document/product/1047/48466#.E5.88.9B.E5.BB.BA.E7.BE.A4.E7.BB.84) или вы можете использовать [Chat UIKit](https://www.tencentcloud.com/document/product/1047/50056) для интеграции чата, вызовов и других сценариев.

```
public func groupCall(groupId: String, userIdList: [String], callMediaType: TUICallMediaType)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| groupId | String | ID группы. |
| userIdList | Array | ID целевых пользователей. |
| callMediaType | [TUICallMediaType](https://trtc.io/document/54902?product=call&menulabel=uikit&platform=ios#TUICallMediaType) | Тип вызова, который может быть видео или аудио. |

### groupCall

Этот API используется для выполнения группового вызова с поддержкой пользовательского ID комнаты, тайм-аута вызова, содержимого оффлайн-уведомления и т. д.

> **Примечание:** Рекомендуется использовать API [calls](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/callstore/calls(participantids:callmediatype:params:completion:)). Перед выполнением группового вызова необходимо сначала создать или присоединиться к группе Chat. Подробную информацию о создании группы см. в разделе [Управление группами Chat](https://www.tencentcloud.com/en/document/product/1047/48466#.E5.88.9B.E5.BB.BA.E7.BE.A4.E7.BB.84) или вы можете использовать [Chat UIKit](https://www.tencentcloud.com/document/product/1047/50056) для интеграции чата, вызовов и других сценариев.

```
public func groupCall(groupId: String, userIdList: [String], callMediaType: TUICallMediaType, params: TUICallParams,                      succ: @escaping TUICallSucc, fail: @escaping TUICallFail)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| groupId | String | ID группы. |
| userIdList | Array | ID целевых пользователей. |
| callMediaType | [TUICallMediaType](https://trtc.io/document/54902?product=call&menulabel=uikit&platform=ios#TUICallMediaType) | Тип вызова, который может быть видео или аудио. |
| params | [TUICallParams](https://trtc.io/document/54902?product=call&menulabel=uikit&platform=ios#TUICallParams) | Параметры расширения вызова, такие как roomID, тайм-аут вызова, информация об оффлайн-уведомлении и т. д. |

### joinInGroupCall

Этот API используется для присоединения к групповому вызову.

> **Примечание:** Рекомендуется использовать API [join](https://tencent-rtc.github.io/TUIKit_iOS/documentation/atomicxcore/callstore/join(callid:completion:)). Перед присоединением к групповому вызову необходимо предварительно создать или присоединиться к группе Chat, и в группе уже должны быть пользователи, участвующие в вызове. Подробную информацию о создании группы см. в разделе [Управление группами Chat](https://www.tencentcloud.com/document/product/1047/48466?lang=en&pg=#ordinary-api) или вы можете использовать [Chat UIKit](https://www.tencentcloud.com/document/product/1047/50056) для интеграции чата, вызовов и других сценариев.

```
public func joinInGroupCall(roomId: TUIRoomId, groupId: String, callMediaType: TUICallMediaType)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | [TUIRoomId](https://trtc.io/document/54902?product=call&menulabel=uikit&platform=ios#TUIRoomId) | ID комнаты. |
| groupId | String | ID группы. |
| callMediaType | [TUICallMediaType](https://trtc.io/document/54902?product=call&menulabel=uikit&platform=ios#TUICallMediaType) | Тип вызова, который может быть видео или аудио. |


---
*Источник: [https://trtc.io/document/51011](https://trtc.io/document/51011)*

---
*Источник (EN): [tuicallkit.md](./tuicallkit.md)*

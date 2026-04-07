# RoomKit API

## Введение

TUIRoomKit — это открытый набор UI-слоя для SDK конференций, в настоящее время поддерживает только язык Swift на платформе iOS. UI конференции можно вызвать через простые вызовы API.

## Интерфейс TUIRoomKit

| API | Описание |
| --- | --- |
| [createInstance](https://www.tencentcloud.com/document/product/647/54857#eeea9b0a-415a-4eb5-943b-0897122b85f4) | Инициализация объекта-синглтона TUIRoomKit |
| [destroyInstance](https://www.tencentcloud.com/document/product/647/54857#a07b9445-798a-4128-95d8-5eec3893dd63) | Удаление объекта-синглтона TUIRoomKit |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/54857#5b2593e4-ab4a-4e5c-a0a5-ae2e346456af) | Установка информации пользователя (аватар, имя) (опционально) |
| [createRoom](https://www.tencentcloud.com/document/product/647/54857#657af8a0-cbfa-4808-b122-3f32a4db025c) | Создание комнаты |
| [enterRoom](https://www.tencentcloud.com/document/product/647/54857#ca9fa33b-d588-4643-aece-df6e94a5d2b6) | Вход в комнату |

### createInstance

Инициализация объекта-синглтона TUIRoomKit.

```
public class func createInstance() -> TUIRoomKit
```

### destroyInstance

Удаление объекта-синглтона TUIRoomKit.

```
public class func destroyInstance() -> Void
```

### setSelfInfo(опционально)

Установка информации пользователя (аватар, имя).

```
public func setSelfInfo(userName: String,                        avatarURL: String,                        onSuccess: @escaping TUISuccessBlock,                          onError: @escaping TUIErrorBlock) -> Void
```

Параметры следующие:

| Параметр | Тип | Значение |
| --- | --- | --- |
| userName | String | Имя пользователя |
| avatarURL | String | URL аватара пользователя |
| onSuccess | TUISuccessBlock | Обратный вызов успеха |
| onError | TUIErrorBlock | Обратный вызов ошибки |

### createRoom

Создание комнаты.

```
public func createRoom(roomInfo: TUIRoomInfo,                       onSuccess: @escaping TUISuccessBlock,                         onError: @escaping TUIErrorBlock) -> Void
```

Параметры следующие:

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomInfo | [TUIRoomInfo](https://www.tencentcloud.com/document/product/647/54859#RoomInfo) | Данные комнаты |
| onSuccess | TUISuccessBlock | Обратный вызов успеха |
| onError | TUIErrorBlock | Обратный вызов ошибки |

### enterRoom

Вход в комнату.

```
public func enterRoom(roomId: String,                  enableAudio: Bool,                  enableVideo: Bool,             isSoundOnSpeaker: Bool,                   onSuccess: @escaping TUISuccessBlock,                      onError: @escaping TUIErrorBlock) -> Void
```

Параметры следующие:

| Параметр | Тип | Значение |
| --- | --- | --- |
| roomId | String | Строка ID комнаты |
| enableAudio | Bool | Включить ли аудио при входе в комнату |
| enableVideo | Bool | Включить ли видео при входе в комнату |
| isSoundOnSpeaker | Bool | Включить ли динамики при входе в комнату |
| onSuccess | TUISuccessBlock | Обратный вызов успеха |
| onError | TUIErrorBlock | Обратный вызов ошибки |


---
*Источник: [https://trtc.io/document/54857](https://trtc.io/document/54857)*

---
*Источник (EN): [roomkit-api.md](./roomkit-api.md)*

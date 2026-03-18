# RoomKit API

Module:   TUIRoomKit

Function: Интерфейс основной функции многопользовательского аудио и видео

Version: 2.1.0

**TUIRoomKit**

## TUIRoomKit

| список функций | описание |
| --- | --- |
| [createInstance](https://www.tencentcloud.com/document/product/647/54865#2a6a582a44072feeed27e5ac25531025) | Создать экземпляр TUIRoomKit (режим singleton). |
| [destroyInstance](https://www.tencentcloud.com/document/product/647/54865#a07b9445-798a-4128-95d8-5eec3893dd63) | Уничтожить экземпляр TUIRoomKit. |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/54865#9bd21648a95d07aa95e1b808cab6479b) | Установить личную информацию, включая имя пользователя и аватар. |
| [createRoom](https://www.tencentcloud.com/document/product/647/54865#6df5c9d6843d0aa619ef4e732b704cc4) | Создать комнату. |
| [enterRoom](https://www.tencentcloud.com/document/product/647/54865#1ba05215-2559-4df2-ba80-04de67a39f27) | Войти в комнату. |

## createInstance

Инициализировать объект singleton TUIRoomKit.

```
public static TUIRoomKit createInstance();
```

### destroyInstance

Уничтожить экземпляр TUIRoomKit.

```
public static void destroyInstance();
```

## setSelfInfo

Установить личную информацию, включая имя пользователя и аватар.

```
public abstract void setSelfInfo(String userName, String avatarURL,                                  TUIRoomDefine.ActionCallback callback);
```

| параметр | описание |
| --- | --- |
| userName | Имя пользователя. |
| avatarURL | Ссылка на личный аватар. |
| callback | Callback для успешной установки личной информации. |

## createRoom

Создать комнату.

```
public abstract void createRoom(TUIRoomDefine.RoomInfo roomInfo, TUIRoomDefine.ActionCallback callback);
```

| параметр | описание |
| --- | --- |
| roomInfo | Параметры для создания комнаты, включая номер комнаты, имя комнаты и т.д., где roomId является обязательным, остальные могут быть значениями по умолчанию. |
| callback | Callback для определения успешного создания комнаты. |

## enterRoom

Войти в комнату.

```
public abstract void enterRoom(String roomId,                                boolean enableAudio,                                boolean enableVideo,                                boolean isSoundOnSpeaker,
                               TUIRoomDefine.GetRoomInfoCallback callback);
```

| параметр | описание |
| --- | --- |
| roomId | Номер комнаты для входа в комнату. |
| enableAudio | true: При входе в комнату включить микрофон и отправлять локальные аудиоданные на удалённую сторону. Другие члены могут нормально услышать локальный звук; false: При входе в комнату микрофон включен, но локальные аудиоданные не отправляются на удалённую сторону. Другие члены не могут услышать локальный звук. |
| enableVideo | true: Войти в комнату, включить камеру и отправлять локальные видеоданные на удалённую сторону. Другие члены могут нормально видеть локальное изображение; false: При входе в комнату камера не будет включена и локальные видеоданные не будут отправляться на удалённую сторону. Другие члены не смогут видеть локальное видео. |
| isSoundOnSpeaker | Использовать ли динамик для воспроизведения звука, true для использования динамика, false для использования наушников. |
| callback | Callback для определения успешного входа в комнату. |


---
*Источник: [https://trtc.io/document/54865](https://trtc.io/document/54865)*

---
*Источник (EN): [roomkit-api.md](./roomkit-api.md)*

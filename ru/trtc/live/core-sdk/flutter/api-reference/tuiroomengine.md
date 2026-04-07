# TUIRoomEngine

## API TUIRoomEngine

API TUIRoomEngine — это интерфейс без UI для многопользовательских аудио и видео комнат. Вы можете использовать эти API для выполнения пользовательской инкапсуляции в соответствии с вашими бизнес-потребностями.

### sharedInstance

Создать экземпляр TUIRoomEngine.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
static TUIRoomEngine sharedInstance()
```

**Возвращаемое значение:** Экземпляр TUIRoomEngine.

### destroySharedInstance

Уничтожить экземпляр TUIRoomEngine.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
void destroySharedInstance()
```

### login

Вход в интерфейс roomEngine, необходимо сначала инициализировать информацию пользователя, а затем можно входить в комнату и выполнять ряд операций.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
static Future<TUIActionCallback> login(int sdkAppId,                                String userId,                               String userSig)
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| sdkAppId | int | Получите информацию sdkAppId из информации приложения |
| userId | String | ID пользователя |
| userSig | String | Подпись userSig. Методы расчёта userSig см. в [UserSig related](https://www.tencentcloud.com/document/product/647/35166#) |

### logout

Интерфейс выхода, который включает активное выхождение из комнаты и уничтожение ресурсов.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
static Future<TUIActionCallback> logout()
```

### setSelfInfo

Установить локальное имя пользователя и аватар.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
static Future<TUIActionCallback> setSelfInfo(String userName, String avatarURL)
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| userName | String | Имя пользователя |
| avatarUrl | String | Профильное фото пользователя |

### setLoginUserInfo

Установить информацию вошедшего пользователя.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
static Future<TUIActionCallback> setLoginUserInfo(TUILoginUserInfo userInfo)
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| userInfo | TUILoginUserInfo | Информация пользователя |

### **getSelfInfo**

Получить базовую информацию о локальном вошедшем пользователе.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
static TUILoginUserInfo getSelfInfo()
```

**Возвращаемое значение:** Информация входа пользователя.

### addObserver

Добавить обратный вызов события TUIRoomEngine.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
void addObserver(TUIRoomObserver observer)
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| observer | TUIRoomObserver | Обратный вызов события TUIRoomEngine |

### removeObserver

Удалить обратный вызов события TUIRoomEngine.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
void removeObserver(TUIRoomObserver observer)
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| observer | TUIRoomObserver | Обратный вызов события TUIRoomEngine |

### createRoom

Хост создаёт комнату, и пользователь, вызвавший createRoom, является владельцем комнаты. При создании комнаты можно установить ID комнаты, название комнаты, а также разрешить ли комнате пользователям инициировать аудио и видео, отправлять сообщения и другие функции.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
Future<TUIActionCallback> createRoom(TUIRoomInfo roomInfo)
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| roomInfo | [TUIRoomInfo](https://www.tencentcloud.com/document/product/647/67259#RoomInfo) | Базовая информация о комнате |

### destroyRoom

Интерфейс уничтожения комнаты. Комната должна быть уничтожена владельцем. После уничтожения комнаты невозможно в неё войти.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
Future<TUIActionCallback> destroyRoom()
```

### enterRoom

Интерфейс входа в комнату.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
Future<TUIValueCallBack<TUIRoomInfo>> enterRoom(String roomId,{TUIRoomType roomType = TUIRoomType.conference,TUIEnterRoomOptions? options})
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| roomId | String | Номер комнаты, строковый тип |
| roomType | TUIRoomType | Тип комнаты |
| options | TUIEnterRoomOptions | Опциональные параметры для входа в комнату |

### exitRoom

Интерфейс выхода из комнаты, пользователи могут выходить из комнаты через exitRoom после выполнения enterRoom.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
Future<TUIActionCallback> exitRoom(bool syncWaiting)
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| syncWaiting | bool | Выходить ли из комнаты синхронно |

### connectOtherRoom

Подключиться к другой комнате.

> **Примечание:** Используется для применения кроссрум-микрофонного подключения в сценариях прямой трансляции.

```
TUIRequest connectOtherRoom(String roomId,                             String userId,                             int timeout,                                TUIRequestCallback? requestCallback)
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| userId | String | ID пользователя |
| timeout | int | Время |
| callback | TUIRequestCallback | Обратный вызов для запроса подключения к другой комнате |

**Возвращаемое значение:** Тело запроса

### disconnectOtherRoom

Отключиться от другой комнаты.

> **Примечание:** Используется для отключения кроссрум-микрофонных подключений в сценариях прямой трансляции.

```
Future<TUIActionCallback> disconnectOtherRoom()
```

### fetchRoomInfo

Получить информацию о комнате.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
Future<TUIValueCallBack<TUIRoomInfo>> fetchRoomInfo()
```

### updateRoomNameByAdmin

Обновить название комнаты.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
Future<TUIActionCallback> updateRoomNameByAdmin(String roomName)
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| roomName | String | Название комнаты |

### updateRoomSeatModeByAdmin

Установить режим микрофона комнаты (могут вызывать только администраторы или владельцы группы).

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
Future<TUIActionCallback> updateRoomSeatModeByAdmin(TUISeatMode mode)
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| mode | [TUISeatMode](https://www.tencentcloud.com/document/product/647/67259#TUISeatMode) | Режим комнаты |

### setLocalVideoView

Установить элементы управления представлением для отрисовки локального видео пользователя.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
void setLocalVideoView(int viewId)
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| viewId | int | Значение типа int64 указателя на представление, этот viewId можно преобразовать в соответствующее представление собственной платформы, и видеоматериал будет отрисован на этом представлении |

### openLocalCamera

Включить локальную камеру и начать получение видеопотока.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
Future<TUIActionCallback> openLocalCamera(bool isFront,                                   TUIVideoQuality quality)
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| isFront | bool | Использовать ли фронтальную камеру |
| quality | [TUIVideoQuality](https://www.tencentcloud.com/document/product/647/67259#74d0aadf-0c54-4a05-9e30-f40b427f1402) | Качество видео |

### closeLocalCamera

Выключить локальную камеру.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
void closeLocalCamera()
```

### updateVideoQuality

Установить параметры локального видео.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
void updateVideoQuality(TUIVideoQuality quality)
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| quality | [TUIVideoQuality](https://www.tencentcloud.com/document/product/647/67259#74d0aadf-0c54-4a05-9e30-f40b427f1402) | Качество видео |

### updateVideoQualityEx

Установить параметры локального видеокодера.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
void updateVideoQualityEx(      TUIVideoStreamType streamType, TUIRoomVideoEncoderParams params);
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| streamType | TUIVideoStreamType | Тип видеопотока |
| params | TUIRoomVideoEncoderParams | Параметры видеокодера |

### setVideoResolutionMode

Установить режим разрешения видеокодера (альбомное разрешение или портретное разрешение).

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
void setVideoResolutionMode(      TUIVideoStreamType streamType, TUIResolutionMode resolutionMode);
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| streamType | TUIVideoStreamType | Тип видеопотока |
| resolutionMode | TUIResolutionMode | Режим разрешения |

### enableGravitySensor

Включить режим датчика гравитации.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
void enableGravitySensor(bool enable);
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| enable | bool | Включено ли |

### startPushLocalVideo

Начать отправку локального видеопотока на удаленный компьютер.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
void startPushLocalVideo()
```

### stopPushLocalVideo

Остановить отправку локального видеопотока на удаленный компьютер.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
void stopPushLocalVideo()
```

### startScreenSharing

Начать общее использование экрана

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
Future<void> startScreenSharing({String appGroup = ''})
```

### stopScreenSharing

Завершить общее использование экрана

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
Future<void> stopScreenSharing()
```

### openLocalMicrophone

Включить локальный микрофон.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
Future<TUIActionCallback> openLocalMicrophone(TUIAudioQuality quality)
```

| Параметры | Тип | Описание |
| --- | --- | --- |
| quality | [TUIAudioQuality](https://www.tencentcloud.com/document/product/647/67259#c079e8f9-62be-4ea2-b740-20658dcec529) | Качество звука |

### closeLocalMicrophone

Выключить локальный микрофон.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
void closeLocalMicrophone()
```

### updateAudioQuality

Обновить параметры кодирования локального звука.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
void updateAudioQuality(TUIAudioQuality quality)
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| quality | [TUIAudioQuality](https://www.tencentcloud.com/document/product/647/67259#c079e8f9-62be-4ea2-b740-20658dcec529) | Качество звука |

### muteLocalAudio

Остановить отправку локального аудиопотока на удаленный компьютер.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
Future<TUIActionCallback> muteLocalAudio()
```

### unMuteLocalAudio

Начать отправку локального аудиопотока на удаленный компьютер.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
Future<TUIActionCallback> unMuteLocalAudio()
```

### setRemoteVideoView

Установить элементы управления представлением для отрисовки удаленного видео пользователя.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
void setRemoteVideoView(String userId,                        TUIVideoStreamType streamType,                         int viewId)
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| streamType | [TUIVideoStreamType](https://www.tencentcloud.com/document/product/647/67259#VideoStreamType) | Тип потока пользователя |
| viewId | int | Значение типа int64 указателя на представление, этот viewId можно преобразовать в соответствующее представление собственной платформы, и видеоматериал будет отрисован на этом представлении |

### startPlayRemoteVideo

Начать воспроизведение видеопотока удаленного пользователя.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
void startPlayRemoteVideo(String userId,                                                        TUIVideoStreamType streamType,                                                               TUIPlayCallback? callback)
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| streamType | [TUIVideoStreamType](https://www.tencentcloud.com/document/product/647/67259#VideoStreamType) | Тип потока пользователя |
| callback | TUIPlayCallback? | Обратный вызов результата воспроизведения |

### stopPlayRemoteVideo

Остановить воспроизведение видеопотока удаленного пользователя.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
void stopPlayRemoteVideo(String userId,                         TUIVideoStreamType streamType)
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| streamType | [TUIVideoStreamType](https://www.tencentcloud.com/document/product/647/67259#VideoStreamType) | Тип потока пользователя |

### muteRemoteAudioStream

Выключить звук удаленного пользователя.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
void muteRemoteAudioStream(String userId, boolean isMute);
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| isMute | bool | Выключить ли звук |

### getUserList

Получить текущий список пользователей в комнате. Обратите внимание, что максимальное количество пользователей, которое можно получить одновременно, составляет 100.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
Future<TUIValueCallBack<TUIUserListResult>> getUserList(int nextSequence)
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| nextSequence | int | Флаг получения с разбиением на страницы. Введите 0 для первого получения. Если nextSeq не равен нулю в обратном вызове, необходимо разбиение на страницы. Передайте nextSeq снова, чтобы получить его, пока nextSeq не будет равен нулю в обратном вызове |

### getUserInfo

Получить подробную информацию о пользователях.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
Future<TUIValueCallBack<TUIUserInfo>> getUserInfo(String userId)
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| userId | String | Получить подробную информацию этого пользователя на основе userId |

### changeUserRole

Изменить роль пользователя. Могут вызывать только администраторы или владельцы группы.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
Future<TUIActionCallback> changeUserRole(String userId,                                  TUIRole role)
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| role | [TUIRole](https://www.tencentcloud.com/document/product/647/67259#Role) | Роль пользователя |

### changeUserNameCard

Изменить псевдоним пользователя в комнате.

> **Примечание:** Эта функция применяется только к типу конференц-комнаты ([conference](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
Future<TUIActionCallback> changeUserNameCard(String userId, String nameCard);
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| nameCard | String | Псевдоним пользователя |

### kickRemoteUserOutOfRoom

Удалить пользователя из комнаты. Могут вызывать только администраторы или владельцы группы.

> **Примечание:** Эта функция применяется к типу конференц-комнаты и типу прямой трансляции ([conference & livingRoom](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
Future<TUIActionCallback> kickRemoteUserOutOfRoom(String userId)
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |

### addCategoryTagForUsers

Добавить теги для пользователей. Может вызывать только владелец комнаты.

> **Примечание:** Эта функция применяется только к типу конференц-комнаты ([conference](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
Future<TUIActionCallback> addCategoryTagForUsers(int tag, List<String> userList);
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| tag | int | Тип метки. Числовой тип, больший или равный 1000. Вы можете определить его самостоятельно. |
| userList | List<String> | Список пользователей |

### removeCategoryTagForUsers

Удалить теги для пользователей. Может вызывать только владелец комнаты.

> **Примечание:** Эта функция применяется только к типу конференц-комнаты ([conference](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
Future<TUIActionCallback> removeCategoryTagForUsers(int tag, List<String> userList);
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| tag | int | Тип. Числовой тип, больший или равный 1000. Вы можете определить его самостоятельно. |
| userList | List<String> | Список пользователей |

### getUserListByTag

Получить информацию о пользователях в комнате на основе меток

Удалить теги для пользователей. Может вызывать только владелец комнаты.

> **Примечание:** Эта функция применяется только к типу конференц-комнаты ([conference](https://www.tencentcloud.com/document/product/647/67259#RoomType)).

```
Future<TUIValueCallBack<TUIUserListResult>> getUserListByTag(int tag, int nextSequence);
```

**Параметр:**

| Параметры | Тип | Описание |
| --- | --- | --- |
| tag | int | Тип. Числовой тип, больший или равный 1000. Вы можете определить его самостоятельно. |
| nextSequence | int | Флаг получения с разбиением на страницы. Введите 0 для первого получения. Если nextSequence не равен нулю в обратном вызове, необходимо разбиение на страницы. Передайте его снова, чтобы получить его, пока он не будет равен нулю |

### setCustomInfoFor

---
*Источник (EN): [tuiroomengine.md](./tuiroomengine.md)*

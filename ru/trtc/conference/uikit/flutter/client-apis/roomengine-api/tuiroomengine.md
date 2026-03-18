# TUIRoomEngine

## Введение в API TUIRoomEngine

API TUIRoomEngine — это интерфейс без UI для компонента конференции. Вы можете использовать этот API для пользовательской инкапсуляции в соответствии с потребностями вашего бизнеса.

### createInstance

Создать экземпляр TUIRoomEngine.

```
static TUIRoomEngine createInstance()
```

**Возвращаемое значение:** Экземпляр TUIRoomEngine

### destroyInstance

Уничтожить экземпляр TUIRoomEngine.

```
void destroyInstance()
```

### login

Интерфейс входа. Необходимо инициализировать информацию пользователя перед входом в комнату и выполнением серии операций.

```
static Future<TUIActionCallback> login(int sdkAppId,                                String userId,                               String userSig)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| sdkAppId | int | Получить информацию sdkAppId из Application Info |
| userId | String | ID пользователя |
| userSig | String | UserSig |

### logout

Интерфейс выхода. Произойдёт активный выход из комнаты, освобождение ресурсов.

```
static Future<TUIActionCallback> logout()
```

### setSelfInfo

Установить имя и аватар локального пользователя.

```
static Future<TUIActionCallback> setSelfInfo(String userName, String avatarURL)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| userName | String | Имя пользователя |
| avatarUrl | String | URL-адрес аватара пользователя |

### setLoginUserInfo

Установить информацию пользователя при входе.

```
static Future<TUIActionCallback> setLoginUserInfo(TUILoginUserInfo userInfo)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| userInfo | TUILoginUserInfo | Информация пользователя |

### **getSelfInfo**

Получить базовую информацию локального пользователя при входе.

```
static TUILoginUserInfo getSelfInfo()
```

**Возвращаемое значение:** базовая информация локального пользователя при входе

### addObserver

Добавить обратный вызов события TUIRoomEngine.

```
void addObserver(TUIRoomObserver observer)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| observer | TUIRoomObserver | Обратный вызов события TUIRoomEngine |

### removeObserver

Удалить обратный вызов события TUIRoomEngine.

```
void removeObserver(TUIRoomObserver observer)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| observer | TUIRoomObserver | Обратный вызов события TUIRoomEngine |

### createRoom

Хозяин создаёт комнату. Пользователь, вызывающий createRoom, становится владельцем комнаты. При создании комнаты можно установить ID комнаты, имя комнаты и разрешить пользователям присоединяться, включать видео и аудио, отправлять сообщения и другие функции.

```
Future<TUIActionCallback> createRoom(TUIRoomInfo roomInfo)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomInfo | [TUIRoomInfo](/document/product/647/57515#RoomInfo) | Данные комнаты |

### destroyRoom

Интерфейс уничтожения комнаты. Владелец комнаты должен инициировать уничтожение комнаты. После уничтожения комнаты она становится недоступной для входа.

```
Future<TUIActionCallback> destroyRoom()
```

### enterRoom

Вход в комнату.

```
Future<TUIValueCallBack<TUIRoomInfo>> enterRoom(String roomId)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |

### exitRoom

Интерфейс выхода из комнаты. После того как пользователь выполнит вход в комнату, он может выйти из комнаты через выход из комнаты.

```
Future<TUIActionCallback> exitRoom(bool syncWaiting)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| syncWaiting | bool | Синхронизировать выход из комнаты |

### connectOtherRoom

Подключиться к другим комнатам.

> **Описание:** Используется в сценариях прямой трансляции для применения кросс-комнатной трансляции

```
TUIRequest connectOtherRoom(String roomId,                             String userId,                             int timeout,                                TUIRequestCallback? requestCallback)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | String | ID комнаты |
| userId | String | ID пользователя |
| timeout | int | Время |
| callback | TUIRequestCallback | Обратный вызов подключения к другим комнатам |

**Возвращаемое значение:** Тело запроса

### disconnectOtherRoom

Отключиться от других комнат

> **Описание:** Используется в сценариях прямой трансляции для отключения кросс-комнатной трансляции

```
Future<TUIActionCallback> disconnectOtherRoom()
```

### fetchRoomInfo

Получить данные комнаты.

```
Future<TUIValueCallBack<TUIRoomInfo>> fetchRoomInfo()
```

### updateRoomNameByAdmin

Обновить ID комнаты.

```
Future<TUIActionCallback> updateRoomNameByAdmin(String roomName)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomName | String | ID комнаты |

### updateRoomSpeechModeByAdmin

Установить режим управления (только администратор или владелец группы могут вызывать).

```
Future<TUIActionCallback> updateRoomSpeechModeByAdmin(TUISpeechMode mode)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| mode | [TUISpeechMode](/document/product/647/57515#SpeechMode) | Режим управления |

### setLocalVideoView

Установить элемент управления видео-рендерингом локального пользователя.

```
void setLocalVideoView(TUIVideoStreamType streamType,                        int viewId)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| streamType | [TUIVideoStreamType](/document/product/647/57515#VideoStreamType) | Тип локальных потоков |
| viewId | int | Значение типа int64 указателя на представление для рендеринга. Через этот viewId можно преобразовать в соответствующее представление собственной платформы, и видео-изображение будет отображаться в этом представлении. |

### openLocalCamera

Открыть локальную камеру и начать захват видео.

```
Future<TUIActionCallback> openLocalCamera(bool isFront,                                   TUIVideoQuality quality)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| isFront | bool | Использовать ли фронтальную камеру |
| quality | [TUIVideoQuality](/document/product/647/57515#VideoQuality) | Качество видео |

### closeLocalCamera

Закрыть локальную камеру.

```
void closeLocalCamera()
```

### updateVideoQuality

Установить локальный видеопараметр.

```
void updateVideoQuality(TUIVideoQuality quality)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| quality | [TUIVideoQuality](/document/product/647/57515#VideoQuality) | Качество видео |

### updateVideoQualityEx

Установить параметры кодирования видеокодека.

```
void updateVideoQualityEx(      TUIVideoStreamType streamType, TUIRoomVideoEncoderParams params);
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| streamType | TUIVideoStreamType | Тип видеопотока |
| params | TUIRoomVideoEncoderParams | Параметры кодирования видеокодека |

### setVideoResolutionMode

Установить режим разрешения видеокодека

```
void setVideoResolutionMode(      TUIVideoStreamType streamType, TUIResolutionMode resolutionMode);
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| streamType | TUIVideoStreamType | Тип видеопотока |
| resolutionMode | TUIResolutionMode | Режим разрешения видео |

### enableGravitySensor

Включить датчик гравитации

```
void enableGravitySensor(bool enable);
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| enable | bool | Включить ли |

### startPushLocalVideo

Начать отправку локального видео-потока на удалённый компьютер.

```
void startPushLocalVideo()
```

### stopPushLocalVideo

Остановить отправку локального видео-потока на удалённый компьютер.

```
void stopPushLocalVideo()
```

### startScreenSharing

Начать общий доступ к экрану

```
Future<void> startScreenSharing({String appGroup = ''})
```

### stopScreenSharing

Остановить общий доступ к экрану

```
Future<void> stopScreenSharing()
```

### openLocalMicrophone

Открыть локальный микрофон.

```
Future<TUIActionCallback> openLocalMicrophone(TUIAudioQuality quality)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| quality | [TUIAudioQuality](/document/product/647/57515#AudioQuality) | Качество аудио |

### closeLocalMicrophone

Закрыть локальный микрофон.

```
void closeLocalMicrophone()
```

### updateAudioQuality

Обновить настройку качества локального аудио-кодека.

```
void updateAudioQuality(TUIAudioQuality quality)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| quality | [TUIAudioQuality](/document/product/647/57515#AudioQuality) | Качество аудио |

### muteLocalAudio

Отключить локальное аудио

```
Future<TUIActionCallback> muteLocalAudio()
```

### unMuteLocalAudio

Включить локальное аудио

```
Future<TUIActionCallback> unMuteLocalAudio()
```

### setRemoteVideoView

Установить элемент управления видео-рендерингом удалённого пользователя.

```
void setRemoteVideoView(String userId,                        TUIVideoStreamType streamType,                         int viewId)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| streamType | [TUIVideoStreamType](/document/product/647/57515#VideoStreamType) | Тип потоков пользователя |
| viewId | int | Значение типа int64 указателя на представление для рендеринга. Через этот viewId можно преобразовать в соответствующее представление собственной платформы, и видео-изображение будет отображаться в этом представлении. |

### startPlayRemoteVideo

Начать воспроизведение видео-потока удалённого пользователя.

```
void startPlayRemoteVideo(String userId,                                                        TUIVideoStreamType streamType,                                                               TUIPlayCallback? callback)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| streamType | [TUIVideoStreamType](/document/product/647/57515#VideoStreamType) | Тип потоков пользователя |
| callback | TUIPlayCallback? | Обратный вызов результата операции воспроизведения |

### stopPlayRemoteVideo

Остановить воспроизведение видео-потока удалённого пользователя.

```
void stopPlayRemoteVideo(String userId,                         TUIVideoStreamType streamType)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| streamType | [TUIVideoStreamType](/document/product/647/57515#VideoStreamType) | Тип потоков пользователя |

### muteRemoteAudioStream

Отключить звук удалённого пользователя.

```
void muteRemoteAudioStream(String userId, boolean isMute);
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| isMute | bool | Отключить ли звук |

### getUserList

Получить список текущих пользователей в комнате. Обратите внимание, что максимальное количество элементов в списке пользователей, полученном этим интерфейсом, составляет 100.

```
Future<TUIValueCallBack<TUIUserListResult>> getUserList(int nextSequence)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| nextSequence | int | Флаг получения с разбиением по страницам. Введите 0 для первого получения. Если nextSeq в обратном вызове не равен 0, требуется разбиение по страницам. Передайте nextSeq, чтобы получить снова, пока nextSeq в обратном вызове не станет 0 |

### getUserInfo

Получить дополнительную информацию о пользователе.

```
Future<TUIValueCallBack<TUIUserInfo>> getUserInfo(String userId)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | Получить дополнительную информацию о пользователе по userId |

### changeUserRole

Изменить роль пользователя. Только администратор или владелец группы могут вызывать.

```
Future<TUIActionCallback> changeUserRole(String userId,                                  TUIRole role)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| role | [TUIRole](/document/product/647/57515#Role) | Роль пользователя |

### kickRemoteUserOutOfRoom

Исключить пользователя из комнаты. Только администратор или владелец группы могут вызывать.

```
Future<TUIActionCallback> kickRemoteUserOutOfRoom(String userId)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |

### addCategoryTagForUsers

Добавить теги категорий к пользователям (только администратор или владелец группы могут вызывать)

```
Future<TUIActionCallback> addCategoryTagForUsers(int tag, List<String> userList);
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| tag | int | Тип тега. Числовой тип, больший или равный 1000, который можно настраивать |
| userList | List<String> | Список пользователей |

### removeCategoryTagForUsers

Удалить теги категорий у пользователей (только администратор или владелец группы могут вызывать)

```
Future<TUIActionCallback> removeCategoryTagForUsers(int tag, List<String> userList);
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| tag | int | Тип тега. Числовой тип, больший или равный 1000, который можно настраивать |
| userList | List<String> | Список пользователей |

### getUserListByTag

Получить информацию о пользователях в комнате на основе тегов

```
Future<TUIValueCallBack<TUIUserListResult>> getUserListByTag(int tag, int nextSequence);
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| tag | int | Тип тега. Числовой тип, больший или равный 1000, который можно настраивать |
| nextSequence | int | Флаг получения с разбиением по страницам. Введите 0 для первого получения. Если nextSeq в обратном вызове не равен 0, требуется разбиение по страницам. Передайте nextSeq, чтобы получить снова, пока nextSeq в обратном вызове не станет 0 |

### disableDeviceForAllUserByAdmin

Управлять устройствами мультимедиа для всех пользователей. Только администратор или владелец группы могут вызывать.

```
Future<TUIActionCallback> disableDeviceForAllUserByAdmin(TUIMediaDevice device,                                                  bool isDisable)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| device | [TUIMediaDevice](/document/product/647/57515#MediaDevice) | Устройство |
| isDisable | bool | Отключить ли |

### openRemoteDeviceByAdmin

Запросить у удалённого пользователя открыть устройство мультимедиа. Только администратор или владелец группы могут вызывать.

```
TUIRequest openRemoteDeviceByAdmin(String userId,                                    TUIMediaDevice device,                                       int timeout,                                    TUIRequestCallback? requestCallback)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| device | [TUIMediaDevice](/document/product/647/57515#MediaDevice) | Устройство |
| timeout | int | Тайм-аут в секундах. Если установить на 0, SDK не будет выполнять обнаружение тайм-аута и не будет запускать обратный вызов тайм-аута |
| requestCallback | TUIRequestCallback? | Обратный вызов результата операции |

### closeRemoteDeviceByAdmin

Закрыть устройство мультимедиа удалённого пользователя. Только администратор или владелец группы могут вызывать.

```
Future<TUIActionCallback> closeRemoteDeviceByAdmin(String userId,                                            TUIMediaDevice device)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| device | [TUIMediaDevice](/document/product/647/57515#MediaDevice) | Устройство |

### applyToAdminToOpenLocalDevice

Заблокировать управление устройствами мультимедиа всех пользователей.

```
TUIRequest applyToAdminToOpenLocalDevice(TUIMediaDevice device,                                          int timeout,                                          TUIRequestCallback? requestCallback)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| device | [TUIMediaDevice](/document/product/647/57515#MediaDevice) | Устройство |
| timeout | int | Длительность тайм-аута, единица измерения — секунды. Если установить на 0, SDK не будет выполнять обнаружение тайм-аута и не будет запускать обратный вызов тайм-аута |
| callback | TUIRequestCallback | Обратный вызов результата операции |

### setMaxSeatCount

Установить максимальное количество мест. Поддерживается только при входе в комнату и создании комнаты

Когда roomType имеет значение RoomType.CONFERENCE (сценарий образования и конференции), значение maxSeatCount не ограничено;

Когда roomType имеет значение RoomType.LIVE_ROOM (сценарий прямой трансляции), maxSeatCount ограничен до 16;

```
Future<TUIActionCallback> setMaxSeatCount(int maxSeatCount)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| maxSeatCount | int | Максимальное количество мест |

### lockSeatByAdmin

Заблокировать место (включая блокировку позиции, блокировку статуса аудио, блокировку статуса видео).

```
Future<TUIActionCallback> lockSeatByAdmin(int seatIndex,                                   TUISeatLockParams lockParams)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| seatIndex | int | Номер места |
| lockParams | [TUISeatLockParams](/document/product/647/57515#SeatLockParams) | Параметр блокировки микрофона |

### getSeatList

Получить список мест.

```
Future<TUIValueCallBack<List<TUISeatInfo>>> getSeatList()
```

### takeSeat

Локальное включение микрофона.

> **Объяснение:** Сценарий конференции: режим [applyToSpeak](/document/product/647/57515#SpeechMode) требует одобрения хозяина или администратора для включения, другие режимы не поддерживают включение. Сценарий прямой трансляции: режим [freeToSpeak](/document/product/647/57515#SpeechMode) может свободно включать и говорить после включения; режим [applySpeakAfterTakingSeat](/document/product/647/57515#SpeechMode) требует одобрения хозяина или администратора для включения; другие режимы не поддерживают включение.

```
TUIRequest takeSeat(int seatIndex,                     int timeout,                     TUIRequestCallback? requestCallback)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| seatIndex | int | Номер места |
| timeout | int | Тайм-аут в секундах. Если установить на 0, SDK не будет выполнять обнаружение тайм-аута и не будет запускать обратный вызов тайм-аута |
| requestCallback | TUIRequestCallback? | Обратный вызов интерфейса вызова, используется для уведомления статуса обратного вызова запроса |

**Возвращаемое значение:** Тело запроса

### leaveSeat

Локальное отключение микрофона.

```
Future<TUIActionCallback> leaveSeat()
```

### takeUserOnSeatByAdmin

Хозяин/администратор приглашает пользователя включить микрофон.

```
TUIRequest takeUserOnSeatByAdmin(int seatIndex,                                  String userId,                                  int timeout,                                     TUIRequestCallback? requestCallback)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| seatIndex | int | Номер места |
| userId | String | ID пользователя |
| timeout | int | Тайм-аут в секундах. Если установить на 0, SDK не будет выполнять обнаружение тайм-аута и не будет запускать обратный вызов тайм-аута |
| requestCallback | TUIRequestCallback? | Обратный вызов интерфейса вызова, используется для уведомления статуса обратного вызова запроса |

**Возвращаемое значение:** Тело запроса

### kickUserOffSeatByAdmin

Хозяин/администратор отключает микрофон пользователя.

```
Future<TUIActionCallback> kickUserOffSeatByAdmin(int seatIndex,                                          String userId)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| seatIndex | int | Номер места |
| userId | String | ID пользователя |

### sendTextMessage

Отправить текстовое сообщение.

```
Future<TUIActionCallback> sendTextMessage(String message)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| message | String | Содержимое текстового сообщения |

### sendCustomMessage

Отправить пользовательское сообщение

```
Future<TUIActionCallback> sendCustomMessage(String message)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| message | String | Содержимое пользовательского сообщения |

### disableSendingMessageByAdmin

Отключить возможность отправки текстовых сообщений удалённым пользователем (только администратор или владелец группы могут вызывать).

```
Future<TUIActionCallback> disableSendingMessageByAdmin(String userId,                                                bool isDisable)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID пользователя |
| isDisable | bool | Отключить ли |

### disableSendingMessageForAllUser

Отключить возможность отправки текстовых сообщений всем пользователям (только администратор или владелец группы могут вызывать).

```
Future<TUIActionCallback> disableSendingMessageForAllUser(bool isDisable)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| isDisable | bool | Отключить ли |

### cancelRequest

Отменить отправленный запрос.

```
Future<TUIActionCallback> cancelRequest(String requestId)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| requestId | String | ID запроса |

### responseRemoteRequest

Ответить на запрос удалённого пользователя.

```
Future<TUIActionCallback> responseRemoteRequest(String requestId,                                         bool agree)
```

**Параметры:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| requestId | String | ID запроса |
| agree | bool | Согласиться ли |

### switchCamera

Переключиться между фронтальной/тыловой камерой

```
Future<int?> switchCamera(bool isFrontCamera);
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| isFrontCamera | bool | Фронтальная ли камера |

### setBeautyLevel

Установить уровень красоты

```
void setBeautyLevel(int beautyStyle, int beautyLevel);
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| beautyStyle | int | стиль красоты |
| beautyLevel | int | уровень красоты |

### setWhitenessLevel

Установить уровень белизны

```
void setWhitenessLevel(int whitenessLevel);
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| whitenessLevel | int | уровень белизны |

### callExperimentalAPI

Вызвать экспериментальный API

```
void callExperimentalAPI(String jsonStr);
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| jsonStr | String | Информация API |


---
*Источник: [https://trtc.io/document/57514](https://trtc.io/document/57514)*

---
*Источник (EN): [tuiroomengine.md](./tuiroomengine.md)*

# TUICallEngine

## API TUICallEngine

`TUICallEngine` — это компонент аудио/видеозвонков, который **не включает элементы пользовательского интерфейса**. Если `TUICallKit` не соответствует вашим требованиям, вы можете использовать API `TUICallEngine` для настройки вашего проекта.

## Обзор

| API | Описание |
| --- | --- |
| [init](https://www.tencentcloud.com/document/product/647/54907#init) | Аутентифицирует базовые возможности аудио/видеозвонков. |
|  |  |
| [unInit](#unInit) | Функция деструктора, которая освобождает ресурсы, используемые TUICallEngine. |
| [addObserver](https://www.tencentcloud.com/document/product/647/54907#addObserver) | Регистрирует слушатель событий. |
| [removeObserver](https://www.tencentcloud.com/document/product/647/54907#removeObserver) | Отменяет регистрацию слушателя событий. |
| [calls](https://www.tencentcloud.com/document/product/647/54907#calls) | Начинает звонок. |
| [accept](https://www.tencentcloud.com/document/product/647/54907#accept) | Принимает звонок. |
| [reject](https://www.tencentcloud.com/document/product/647/54907#reject) | Отклоняет звонок. |
| [hangup](https://www.tencentcloud.com/document/product/647/54907#hangup) | Завершает звонок. |
| [ignore](https://www.tencentcloud.com/document/product/647/54907#ignore) | Игнорирует звонок. |
| [inviteUser](https://www.tencentcloud.com/document/product/647/54907#inviteUser) | Приглашает других присоединиться к звонку. |
| [join](https://www.tencentcloud.com/document/product/647/54907#join) | Присоединяется к звонку. |
| [startRemoteView](https://www.tencentcloud.com/document/product/647/54907#startRemoteView) | Подписывается на видеопоток удалённого пользователя. |
| [stopRemoteView](https://www.tencentcloud.com/document/product/647/54907#stopRemoteView) | Отписывается от видеопотока удалённого пользователя. |
| [openCamera](https://www.tencentcloud.com/document/product/647/54907#openCamera) | Включает камеру. |
| [closeCamera](https://www.tencentcloud.com/document/product/647/54907#closeCamera) | Отключает камеру. |
| [switchCamera](https://www.tencentcloud.com/document/product/647/54907#switchCamera) | Переключается между передней и задней камерами. |
| [openMicrophone](https://www.tencentcloud.com/document/product/647/54907#openMicrophone) | Включает микрофон. |
| [closeMicrophone](https://www.tencentcloud.com/document/product/647/54907#closeMicrophone) | Отключает микрофон. |
| [selectAudioPlaybackDevice](https://www.tencentcloud.com/document/product/647/54907#selectAudioPlaybackDevice) | Выбирает устройство воспроизведения звука (трубка или динамик). |
| [setSelfInfo](#setSelfInfo) | Устанавливает псевдоним и фотографию профиля. |
| [enableMultiDeviceAbility](https://www.tencentcloud.com/document/product/647/54907#enableMultiDeviceAbility) | Устанавливает, следует ли включить вход с нескольких устройств для TUICallEngine (поддерживается премиум-пакетом). |
| [setVideoRenderParams](https://www.tencentcloud.com/document/product/647/54907#setVideoRenderParams) | Устанавливает режим отрисовки видеоизображения. |
| [setVideoEncoderParams](https://www.tencentcloud.com/document/product/647/54907#setVideoEncoderParams) | Устанавливает параметры кодирования видеокодека. |
| [setBlurBackground](https://www.tencentcloud.com/document/product/647/54907#setBlurBackground) | Установить эффект размытого фона |
| [setVirtualBackground](https://www.tencentcloud.com/document/product/647/54907#setVirtualBackground) | Установить изображение виртуального фона |
| [setBeautyLevel](https://www.tencentcloud.com/document/product/647/54907#setBeautyLevel) | Установить уровень красоты, поддержка отключения красоты по умолчанию. |

## Подробности

### init

Этот API используется для инициализации `TUICallEngine`. Вызовите его для аутентификации сервиса вызовов и выполнения других необходимых действий перед вызовом других API.

```
Future<TUIResult> init(int sdkAppID, String userId, String userSig)
```

### unInit

Функция деструктора, которая освобождает ресурсы, используемые TUICallEngine.

```
Future<TUIResult> unInit()
```

### addObserver

Этот API используется для регистрации слушателя событий для прослушивания событий `TUICallObserver`.

```
Future<void> addObserver(TUICallObserver observer)
```

### removeObserver

Этот API используется для отмены регистрации слушателя событий.

```
Future<void> removeObserver(TUICallObserver observer)
```

### calls

Инициировать звонок. **Поддерживается в v2.9+.**

```
Future<TUIResult> calls(List<String> userIdList, TUICallMediaType mediaType, TUICallParams params)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userIdList | List<String> | ID целевых пользователей. |
| callMediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54909#TUICallMediaType) | Тип звонка, который может быть видеозвонком или аудиозвонком. |
| params | [TUICallParams](https://www.tencentcloud.com/document/product/647/54909#TUICallParams) | Дополнительный параметр, такой как roomID, timeout звонка, информация об офлайн-пуше и т. д. |

### accept

Этот API используется для принятия звонка. После получения обратного вызова `onCallReceived()` вы можете вызвать этот API для принятия звонка.

```
Future<TUIResult> accept()
```

### reject

Этот API используется для отклонения звонка. После получения обратного вызова `onCallReceived()` вы можете вызвать этот API для отклонения звонка.

```
Future<TUIResult> reject()
```

### ignore

Этот API используется для игнорирования звонка. После получения `onCallReceived()` вы можете вызвать этот API для игнорирования звонка. Инициатор звонка получит обратный вызов `onUserLineBusy`.

Примечание: Если ваш проект включает прямую трансляцию или конференцию, вы также можете использовать этот API для реализации функции «на встречу» или «в эфире».

```
Future<TUIResult> ignore()
```

### hangup

Этот API используется для завершения звонка.

```
Future<TUIResult> hangup()
```

### inviteUser

Этот API используется для приглашения пользователей в текущий групповой звонок.

Этот API вызывается участником группового звонка для приглашения новых пользователей.

```
Future<void> iniviteUser(List<String> userIdList, TUICallParams params, TUIValueCallback callback)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userIdList | List<String> | ID целевых пользователей. |
| params | [TUICallParams](https://www.tencentcloud.com/document/product/647/54909#TUICallParams) | Дополнительный параметр, такой как roomID, timeout звонка, информация об офлайн-пуше и т. д. |

### join

Активное присоединение к звонку. **Поддерживается в v2.9+.**

```
Future<void> join(String callId)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| callId | String | Уникальный идентификатор для этого звонка. |

### startRemoteView

Этот API используется для установки объекта представления для отображения видео удалённого пользователя.

```
Future<void> startRemoteView(String userId, intviewId)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID целевого пользователя. |
| intviewId | int | ID виджета на экране отрисовки видео |

### stopRemoteView

Этот API используется для отписки от видеопотока удалённого пользователя.

```
Future<void> stopRemoteView(String userId)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID целевого пользователя. |

### openCamera

Этот API используется для включения камеры.

```
Future<TUIResult> openCamera(TUICamera camera, int? viewId)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| camera | [TUICamera](https://www.tencentcloud.com/document/product/647/54909#TUICamera) | Передняя или задняя камера. |
| viewId | int | ID виджета на экране отрисовки видео |

### closeCamera

Этот API используется для отключения камеры.

```
Future<void> closeCamera()
```

### switchCamera

Этот API используется для переключения между передней и задней камерами.

```
Future<void> switchCamera(TUICamera camera)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| camera | [TUICamera](https://www.tencentcloud.com/document/product/647/54909#TUICamera) | Передняя или задняя камера. |

### openMicrophone

Этот API используется для включения микрофона.

```
Future<TUIResult> openMicrophone()
```

### closeMicrophone

Этот API используется для отключения микрофона.

```
Future<void> closeMicrophone()
```

### selectAudioPlaybackDevice

Этот API используется для выбора устройства воспроизведения звука (трубка или динамик). В сценариях вызовов вы можете использовать этот API для включения/отключения режима свободных рук.

```
Future<void> selectAudioPlaybackDevice(TUIAudioPlaybackDevice device)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| device | [TUIAudioPlaybackDevice](https://www.tencentcloud.com/document/product/647/54909#TUIAudioPlaybackDevice) | Динамик или трубка. |

### setSelfInfo

Этот API используется для установки псевдонима и фотографии профиля. Псевдоним не может превышать 500 байтов, а фотография профиля указывается URL.

```
Future<TUIResult> setSelfInfo(String nickname, String avatar)
```

### enableMultiDeviceAbility

Этот API используется для установки того, следует ли включить вход с нескольких устройств для `TUICallEngine` (поддерживается премиум-пакетом).

```
Future<TUIResult> enableMultiDeviceAbility(bool enable)
```

### setVideoRenderParams

Установить режим отрисовки видеоизображения.

```
Future<TUIResult> setVideoRenderParams(String userId, VideoRenderParams params)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID целевого пользователя. |
| params | [VideoRenderParams](https://www.tencentcloud.com/document/product/647/54909#VideoRenderParams) | Параметры отрисовки видео. |

### setVideoEncoderParams

Установить параметры кодирования видеокодека.

Этот параметр может определить качество изображения, видимого удалёнными пользователями, что также является качеством изображения файлов записи облака.

```
Future<TUIResult> setVideoEncoderParams(VideoEncoderParams params)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| params | [VideoEncoderParams](https://www.tencentcloud.com/document/product/647/54909#VideoEncoderParams) | Параметры кодирования видео |

### setBeautyLevel

Установить уровень красоты, поддержка отключения красоты по умолчанию.

```
Future<TUIResult> setBeautyLevel(double level)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| level | double | Уровень красоты, диапазон от 0.0 до 9.0. |

### setBlurBackground

Установить эффект размытого видео.

```
void setBlurBackground(int level, Function(int code, String message)? errorCallback)
```

Параметры описаны ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| level | int | 0: Отключено, 1: Низкое, 2: Среднее, 3: Высокое. |

### setVirtualBackground

Установить изображение виртуального фона.

```
void setVirtualBackground(String imagePath, Function(int code, String message)? errorCallback)
```

| Параметр | Тип | Значение |
| --- | --- | --- |
| imagePath | String | Имя файла изображения. Файл необходимо добавить в активы основного проекта. |

## Устаревшие интерфейсы

### call

Этот API используется для выполнения (одноранового) звонка.

> **Примечание:** Этот интерфейс устарел в v2.9+. Рекомендуется использовать интерфейс calls вместо него.

```
Future<TUIResult> call(String userId, TUICallMediaType mediaType, TUICallParams params)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID целевого пользователя. |
| mediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54909#TUICallMediaType) | Тип звонка, который может быть видеозвонком или аудиозвонком. |
| params | [TUICallParams](https://www.tencentcloud.com/document/product/647/54909#TUICallParams) | Дополнительный параметр, такой как roomID, timeout звонка, информация об офлайн-пуше и т. д. |

### groupCall

Этот API используется для выполнения группового звонка.

Перед выполнением группового звонка необходимо сначала создать группу IM.

> **Примечание:** Этот интерфейс устарел в v2.9+. Рекомендуется использовать интерфейс calls вместо него.

```
Future<TUIResult> groupCall(String groupId, List<String> userIdList, TUICallMediaType mediaType, TUICallParams params)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| groupId | String | ID группы. |
| userIdList | List<String> | ID целевых пользователей. |
| mediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54909#TUICallMediaType) | Тип звонка, который может быть видеозвонком или аудиозвонком. |
| params | [TUICallParams](https://www.tencentcloud.com/document/product/647/54909#TUICallParams) | Дополнительный параметр, такой как roomID, timeout звонка, информация об офлайн-пуше и т. д. |

### joinInGroupCall

Этот API используется для присоединения к групповому звонку.

Этот API вызывается членом группы для присоединения к звонку группы.

> **Примечание:** Этот интерфейс устарел в v2.9+. Рекомендуется использовать интерфейс join вместо него.

```
Future<TUIResult> joinInGroupCall(TUIRoomId roomId, String groupId, TUICallMediaType mediaType)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | [TUIRoomId](https://www.tencentcloud.com/document/product/647/54909#TUIRoomId) | ID комнаты. |
| groupId | String | ID группы. |
| mediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54909#TUICallMediaType) | Тип звонка, который может быть видеозвонком или аудиозвонком. |

### switchCallMediaType

Этот API используется для изменения типа звонка.

```
Future<void> switchCallMediaType(TUICallMediaType mediaType)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| mediaType | [TUICallMediaType](https://www.tencentcloud.com/document/product/647/54909#TUICallMediaType) | Тип звонка, который может быть видеозвонком или аудиозвонком. |


---
*Источник: [https://trtc.io/document/54907](https://trtc.io/document/54907)*

---
*Источник (EN): [tuicallengine.md](./tuicallengine.md)*

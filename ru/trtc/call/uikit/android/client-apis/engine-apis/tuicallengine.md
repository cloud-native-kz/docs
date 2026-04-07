# TUICallEngine

## API TUICallEngine

`TUICallEngine` — это компонент для аудио- и видеовызовов, который **не включает элементы пользовательского интерфейса**. Если `TUICallKit` не соответствует вашим требованиям, вы можете использовать API `TUICallEngine` для настройки вашего проекта.

## Обзор

| API | Описание |
| --- | --- |
| [createInstance](https://www.tencentcloud.com/document/product/647/51006#createInstance) | Создает экземпляр `TUICallEngine` (режим одиночного экземпляра). |
| [destroyInstance](https://www.tencentcloud.com/document/product/647/51006#destroyInstance) | Завершает экземпляр `TUICallEngine` (режим одиночного экземпляра). |
| [Init](https://www.tencentcloud.com/document/product/647/51006#Init) | Аутентифицирует базовые возможности аудио- и видеовызовов. |
| [addObserver](https://www.tencentcloud.com/document/product/647/51006#addObserver) | Регистрирует слушатель событий. |
| [removeObserver](https://www.tencentcloud.com/document/product/647/51006#removeObserver) | Отменяет регистрацию слушателя событий. |
| [calls](https://www.tencentcloud.com/document/product/647/51006#calls) | Инициирует один-на-один или многостороннее общение. |
| [join](https://www.tencentcloud.com/document/product/647/51006#join) | Активно присоединиться к вызову. |
| [accept](https://www.tencentcloud.com/document/product/647/51006#accept) | Принимает вызов. |
| [reject](https://www.tencentcloud.com/document/product/647/51006#reject) | Отклоняет вызов. |
| [hangup](https://www.tencentcloud.com/document/product/647/51006#hangup) | Завершает вызов. |
| [ignore](https://www.tencentcloud.com/document/product/647/51006#ignore) | Игнорирует вызов. |
| [inviteUser](https://www.tencentcloud.com/document/product/647/51006#inviteuser) | Приглашает пользователей в текущий групповой вызов. |
| [startRemoteView](https://www.tencentcloud.com/document/product/647/51006#startRemoteView) | Подписывает видеопоток удаленного пользователя. |
| [stopRemoteView](https://www.tencentcloud.com/document/product/647/51006#stopRemoteView) | Отписывает видеопоток удаленного пользователя. |
| [openCamera](https://www.tencentcloud.com/document/product/647/51006#openCamera) | Включает камеру. |
| [closeCamera](https://www.tencentcloud.com/document/product/647/51006#closeCamera) | Выключает камеру. |
| [switchCamera](https://www.tencentcloud.com/document/product/647/51006#switchCamera) | Переключается между передней и задней камерами. |
| [openMicrophone](https://www.tencentcloud.com/document/product/647/51006#openMicrophone) | Включает микрофон. |
| [closeMicrophone](https://www.tencentcloud.com/document/product/647/51006#closeMicrophone) | Выключает микрофон. |
| [selectAudioPlaybackDevice](https://www.tencentcloud.com/document/product/647/51006#selectAudioPlaybackDevice) | Выбирает устройство воспроизведения звука (трубка или динамик). |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/51006#setSelfInfo) | Устанавливает псевдоним и фотографию профиля. |
| [enableMultiDeviceAbility](https://www.tencentcloud.com/document/product/647/51006#enableMultiDeviceAbility) | Устанавливает, включить ли многоустройственный вход для `TUICallEngine` (поддерживается [пакетом Group Call](https://trtc.io/document/54632?platform=android&product=call&menulabel=web)). |
| [setVideoRenderParams](https://www.tencentcloud.com/document/product/647/51006#setVideoRenderParams) | Устанавливает режим рендеринга видеоизображения. |
| [setVideoEncoderParams](https://www.tencentcloud.com/document/product/647/51006#setVideoEncoderParams) | Устанавливает параметры кодирования видеокодека. |
| [getTRTCCloudInstance](https://www.tencentcloud.com/document/product/647/51006#getTRTCCloudInstance) | Расширенные функции. |
| [setBeautyLevel](https://www.tencentcloud.com/document/product/647/51006#setBeautyLevel) | Установить уровень красоты, поддерживается отключение красоты по умолчанию. |

## Детали

### createInstance

Этот API используется для создания одиночного экземпляра `TUICallEngine`.

```
TUICallEngine createInstance(Context context)
```

### destroyInstance

Этот API используется для завершения одиночного экземпляра `TUICallEngine`.

```
void destroyInstance();
```

### Init

Этот API используется для инициализации `TUICallEngine`. Вызовите его для аутентификации сервиса вызовов и выполнения других необходимых действий перед вызовом других API.

```
void init(int sdkAppId, String userId, String userSig, TUICommonDefine.Callback callback)
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| sdkAppId | int | Вы можете просмотреть `SDKAppID` в [Управление приложением](https://console.trtc.io/app) > **Информация о приложении** консоли TRTC. |
| userId | String | ID текущего пользователя, представляет собой строку, которая может содержать только буквы (a-z и A-Z), цифры (0-9), дефисы (-) и подчеркивания (_). |
| userSig | String | Собственная защищенная подпись Tencent Cloud. Для информации о том, как вычислять и использовать, см. [UserSig](https://www.tencentcloud.com/document/product/647/35166). |
| callback | TUICommonDefine.Callback | Обратный вызов инициализации. `onSuccess` указывает на успешную инициализацию. |

### addObserver

Этот API используется для регистрации слушателя событий для отслеживания событий `TUICallObserver`.

```
void addObserver(TUICallObserver observer);
```

### removeObserver

Этот API используется для отмены регистрации слушателя событий.

```
void removeObserver(TUICallObserver observer);
```

### calls

Инициирует один-на-один или многостороннее общение.

```
void calls(List<String> userIdList, TUICallDefine.MediaType mediaType,            TUICallDefine.CallParams params, TUICommonDefine.Callback callback)
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userIdList | List<String> | ID целевых пользователей. |
| callMediaType | [TUICallDefine.MediaType](https://www.tencentcloud.com/document/product/647/54900#MediaType) | Тип вызова, может быть видео или аудио. |
| params | [TUICallDefine.CallParams](https://www.tencentcloud.com/document/product/647/54900#CallParams) | Дополнительный параметр, такой как roomID, тайм-аут вызова, информация об оффлайн-уведомлении и т.д. |

### accept

Этот API используется для принятия вызова. После получения обратного вызова `onCallReceived()` вы можете вызвать этот API для принятия вызова.

```
void accept(TUICommonDefine.Callback callback);
```

### reject

Этот API используется для отклонения вызова. После получения обратного вызова `onCallReceived()` вы можете вызвать этот API для отклонения вызова.

```
void reject(TUICommonDefine.Callback callback);
```

### ignore

Этот API используется для игнорирования вызова. После получения обратного вызова `onCallReceived()` вы можете вызвать этот API для игнорирования вызова. Звонящий получит обратный вызов `onUserLineBusy`.

Примечание. Если ваш проект включает потоковую передачу или конференцию, вы также можете использовать этот API для реализации функции «на встречу» или «в эфире».

```
void ignore(TUICommonDefine.Callback callback);
```

### hangup

Этот API используется для завершения вызова.

```
void hangup(TUICommonDefine.Callback callback);
```

### inviteUser

Этот API используется для приглашения пользователей в текущий групповой вызов.

Этот API вызывается участником группового вызова для приглашения новых пользователей.

```
void inviteUser(List<String> userIdList, TUICallDefine.CallParams params,                 TUICommonDefine.ValueCallback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userIdList | List | ID целевых пользователей. |
| params | [TUICallDefine.CallParams](https://www.tencentcloud.com/document/product/647/54900#CallParams) | Дополнительный параметр, такой как roomID, тайм-аут вызова, информация об оффлайн-уведомлении и т.д. |

### join

Активно присоединиться к вызову.

```
void join(String callId, TUICommonDefine.Callback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| callId | String | Уникальный ID для этого вызова |

### startRemoteView

Этот API используется для подписки видеопотока удаленного пользователя. Чтобы он работал, убедитесь, что вы вызваете его после `setRenderView`.

```
void startRemoteView(String userId, TUIVideoView videoView, TUICommonDefine.PlayCallback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID целевого пользователя. |
| videoView | TUIVideoView | Представление для рендеринга. |

### stopRemoteView

Этот API используется для отписки видеопотока удаленного пользователя.

```
void stopRemoteView(String userId);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID целевого пользователя. |

### openCamera

Этот API используется для включения камеры.

```
void openCamera(TUICommonDefine.Camera camera, TUIVideoView videoView, TUICommonDefine.Callback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| camera | [TUICommonDefine.Camera](https://www.tencentcloud.com/document/product/647/54900#Camera) | Передняя или задняя камера. |
| videoView | TUIVideoView | Представление для рендеринга. |

### closeCamera

Этот API используется для выключения камеры.

```
void closeCamera();
```

### switchCamera

Этот API используется для переключения между передней и задней камерами.

```
void switchCamera(TUICommonDefine.Camera camera);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| camera | [TUICommonDefine.Camera](https://www.tencentcloud.com/document/product/647/54900#Camera) | Передняя или задняя камера. |

### openMicrophone

Этот API используется для включения микрофона.

```
void openMicrophone(TUICommonDefine.Callback callback);
```

### closeMicrophone

Этот API используется для выключения микрофона.

```
void closeMicrophone();
```

### selectAudioPlaybackDevice

Этот API используется для выбора устройства воспроизведения звука (трубка или динамик). В сценариях вызовов вы можете использовать этот API для включения/отключения режима громкой связи.

```
void selectAudioPlaybackDevice(TUICommonDefine.AudioPlaybackDevice device);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| device | [TUICommonDefine.AudioPlaybackDevice](https://www.tencentcloud.com/document/product/647/54900#AudioPlaybackDevice) | Динамик или трубка. |

### setSelfInfo

Этот API используется для установки псевдонима и фотографии профиля. Псевдоним не может превышать 500 байт, а фотография профиля указывается URL-адресом.

```
void setSelfInfo(String nickname, String avatar, TUICommonDefine.Callback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| nickname | String | Псевдоним. |
| avatar | String | URL фотографии профиля. |

### enableMultiDeviceAbility

Этот API используется для установки, включить ли многоустройственный вход для `TUICallEngine` (поддерживается [пакетом Group Call](https://trtc.io/document/54632?platform=android&product=call&menulabel=web)).

```
void enableMultiDeviceAbility(boolean enable, TUICommonDefine.Callback callback);
```

### setVideoRenderParams

Установить режим рендеринга видеоизображения.

```
void setVideoRenderParams(String userId, TUICommonDefine.VideoRenderParams params, TUICommonDefine.Callback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID целевого пользователя. |
| params | [TUICommonDefine.VideoRenderParams](https://www.tencentcloud.com/document/product/647/54900#VideoRenderParams) | Параметры рендеринга видео. |

### setVideoEncoderParams

Установить параметры кодирования видеокодека.

Эта настройка может определить качество изображения, просматриваемого удаленными пользователями, что также является качеством изображения файлов облачной записи.

```
void setVideoEncoderParams(TUICommonDefine.VideoEncoderParams params, TUICommonDefine.Callback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| params | [TUICommonDefine.VideoEncoderParams](https://www.tencentcloud.com/document/product/647/54900#VideoEncoderParams) | Параметры кодирования видео |

### getTRTCCloudInstance

Расширенные функции.

```
TRTCCloud getTRTCCloudInstance();
```

### setBeautyLevel

Установить уровень красоты, поддерживается отключение красоты по умолчанию.

```
void setBeautyLevel(float level, TUICommonDefine.Callback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| level | float | Уровень красоты, диапазон: 0 - 9, 0 означает отключение эффекта, 9 означает наиболее очевидный эффект. |

## Устаревший интерфейс

### call

Этот API используется для выполнения (один-на-один) вызова. **Примечание: рекомендуется использовать API calls.**

```
void call(String userId, TUICallDefine.MediaType callMediaType,          TUICallDefine.CallParams params, TUICommonDefine.Callback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID целевого пользователя. |
| callMediaType | [TUICallDefine.MediaType](https://www.tencentcloud.com/document/product/647/54900#MediaType) | Тип вызова, может быть видео или аудио. |
| params | [TUICallDefine.CallParams](https://www.tencentcloud.com/document/product/647/54900#CallParams) | Дополнительный параметр, такой как roomID, тайм-аут вызова, информация об оффлайн-уведомлении и т.д. |

### groupCall

Этот API используется для выполнения группового вызова. **Примечание: рекомендуется использовать API calls.**

> **Примечание:** перед выполнением группового вызова необходимо предварительно создать группу Chat.

```
void groupCall(String groupId, List<String> userIdList, TUICallDefine.MediaType callMediaType,                TUICallDefine.CallParams params, TUICommonDefine.Callback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| groupId | String | ID группы. |
| userIdList | List | ID целевых пользователей. |
| callMediaType | [TUICallDefine.MediaType](https://www.tencentcloud.com/document/product/647/54900#MediaType) | Тип вызова, может быть видео или аудио. |
| params | [TUICallDefine.CallParams](https://www.tencentcloud.com/document/product/647/54900#CallParams) | Дополнительный параметр, такой как roomID, тайм-аут вызова, информация об оффлайн-уведомлении и т.д. |

### joinInGroupCall

Этот API используется для присоединения к групповому вызову. **Примечание: рекомендуется использовать API join.**

Этот API вызывается членом группы для присоединения к групповому вызову.

```
void joinInGroupCall(TUICommonDefine.RoomId roomId, String groupId,                      TUICallDefine.MediaType callMediaType, TUICommonDefine.Callback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | [TUICommonDefine.RoomId](https://www.tencentcloud.com/document/product/647/54900#RoomId) | ID комнаты. |
| groupId | String | ID группы. |
| callMediaType | [TUICallDefine.MediaType](https://www.tencentcloud.com/document/product/647/54900#MediaType) | Тип вызова, может быть видео или аудио. |

### switchCallMediaType

Этот API используется для изменения типа вызова.

```
void switchCallMediaType(TUICallDefine.MediaType callMediaType);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| callMediaType | [TUICallDefine.MediaType](https://www.tencentcloud.com/document/product/647/54900#MediaType) | Тип вызова, может быть видео или аудио. |


---
*Источник: [https://trtc.io/document/51006](https://trtc.io/document/51006)*

---
*Источник (EN): [tuicallengine.md](./tuicallengine.md)*

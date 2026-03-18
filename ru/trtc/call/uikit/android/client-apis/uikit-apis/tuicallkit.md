# TUICallKit

## API TUICallKit

`TUICallKit` — это компонент аудио-/видеозвонков, который **включает элементы пользовательского интерфейса**. Вы можете использовать его API для быстрой реализации приложения аудио-/видеозвонков, аналогичного WeChat. Инструкции по интеграции см. в разделе [Интеграция TUICallKit](https://www.tencentcloud.com/document/product/647/50991).

## Обзор API

| API | Описание |
| --- | --- |
| [createInstance](https://www.tencentcloud.com/document/product/647/51005#createinstance) | Создает экземпляр `TUICallKit` (режим singleton). |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/51005#setSelfInfo) | Устанавливает псевдоним и фотографию профиля. |
| [calls](https://www.tencentcloud.com/document/product/647/51005#calls) | Инициирует односторонний или многостороний звонок. |
| [join](https://www.tencentcloud.com/document/product/647/51005#join) | Активно присоединяется к звонку. |
| [setCallingBell](https://www.tencentcloud.com/document/product/647/51005#setCallingBell) | Устанавливает мелодию звонка. |
| [enableMuteMode](https://www.tencentcloud.com/document/product/647/51005#enableMuteMode) | Устанавливает включение режима без звука. |
| [enableFloatWindow](https://www.tencentcloud.com/document/product/647/51005#enableFloatWindow) | Устанавливает включение плавающего окна. |
| [enableIncomingBanner](https://www.tencentcloud.com/document/product/647/51005#enableIncomingBanner) | Устанавливает отображение баннера входящего вызова. |
| [setScreenOrientation](#setScreenOrientation) | Устанавливает ориентацию экрана. |
| [enableVirtualBackground](#enableVirtualBackground) | Устанавливает размытый фон. |

## Подробности

### createInstance

Этот API используется для создания singleton `TUICallKit`.

Kotlin

Java

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKitfun createInstance(context: Context): TUICallKit
```

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKit;TUICallKit createInstance(Context context);
```

### setSelfInfo

Этот API используется для установки псевдонима и фотографии профиля. Псевдоним не может превышать 500 байт, фотография профиля указывается URL-адресом.

Kotlin

Java

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKitfun setSelfInfo(nickname: String?, avatar: String?, completion: CompletionHandler?);
```

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKit;TUICallKit createInstance(Context context);
```

Параметры описаны ниже:

| Параметр | Тип | Значение |
| --- | --- | --- |
| nickname | String | Имена целевого пользователя. |
| avatar | String | Аватар целевого пользователя. |
| completion | CompletionClosure | Обратный вызов результата асинхронной операции. |

### calls

Инициирует односторонний или многостороний звонок.

kotlin

Java

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKitimport io.trtc.tuikit.atomicxcore.api.call.CallMediaTypeimport io.trtc.tuikit.atomicxcore.api.call.CallParamsfun calls(    userIdList: List<String>, mediaType: CallMediaType,    params: CallParams?, completion: CompletionHandler?);
```

```
 import com.tencent.qcloud.tuikit.tuicallkit.TUICallKit;import io.trtc.tuikit.atomicxcore.api.call.CallMediaType;import io.trtc.tuikit.atomicxcore.api.call.CallParams;void calls(List<String> userIdList, CallMediaType mediaType, CallParams params, CompletionHandler completion);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userIdList | List<String> | Список ID целевых пользователей |
| mediaType | [CallMediaType](https://liteav.sdk.cloudcachetci.com/doc/product/tuikit/atomic-x/android/en/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.call/-call-media-type/index.html) | Тип медиа звонка, например видеозвонок, голосовой звонок |
| params | [CallParams](https://liteav.sdk.cloudcachetci.com/doc/product/tuikit/atomic-x/android/en/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.call/-call-params/index.html) | Параметры расширения звонка, такие как номер комнаты, время ожидания приглашения на звонок |
| completion | CompletionClosure | Обратный вызов результата асинхронной операции |

### join

Активно присоединяется к звонку.

Kotlin

Java

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKit fun join(callId: String?, completion: CompletionHandler?);
```

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKit; void join(String callId, CompletionHandler completion);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| callId | String | Уникальный ID для данного звонка |
| completion | CompletionClosure | Обратный вызов результата асинхронной операции. |

### setCallingBell

Этот API используется для установки мелодии звонка. `filePath` должен быть доступным локальным URL-адресом файла.

Установленная мелодия звонка связана с устройством и не меняется при смене пользователя.

Чтобы сбросить мелодию звонка, передайте пустую строку для `filePath`.

Kotlin

Java

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKitfun setCallingBell(filePath: String?);
```

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKit;void setCallingBell(String filePath);
```

### enableMuteMode

Этот API используется для включения/выключения режима без звука.

Значение по умолчанию — `false`. Этот API используется для установки воспроизведения звука при получении пользователем звонка.

Kotlin

Java

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKitfun enableMuteMode(enable: Boolean);
```

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKit;void enableMuteMode(boolean enable);
```

### enableFloatWindow

Этот API используется для установки включения плавающего окна.

Значение по умолчанию — `false`, и кнопка плавающего окна в верхнем левом углу представления вызова скрыта. Если установлено значение `true`, кнопка становится видимой.

Kotlin

Java

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKitfun enableFloatWindow(enable: Boolean);
```

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKit;void enableFloatWindow(boolean enable);
```

### enableIncomingBanner

Этот API используется для установки отображения баннера при получении пользователем нового приглашения на звонок.

Значение по умолчанию — `false`. По умолчанию получатель будет показывать полноэкранное представление звонка при получении приглашения. Если установлено значение `true`, получатель сначала отобразит баннер.

Kotlin

Java

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKitfun enableIncomingBanner(enable: Boolean);
```

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKit;void enableIncomingBanner(boolean enable);
```

### setScreenOrientation

Устанавливает ориентацию экрана.

По умолчанию используется портретный режим; ориентация: 0-Портрет, 1-Альбом, 2-Автоматически.

Kotlin

Java

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKitfun setScreenOrientation(orientation: Int);
```

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKit;void setScreenOrientation(int orientation);
```

### enableVirtualBackground

Этот API используется для установки размытого фона.

Значение по умолчанию — `false`.

```
import com.tencent.qcloud.tuikit.tuicallkit.TUICallKitfun enableVirtualBackground(enable: Boolean);
```

## Устаревший интерфейс

### call

Этот API используется для выполнения (одностороннего) звонка.

> **Примечание:** **Рекомендуется использовать API** [calls](https://liteav.sdk.cloudcachetci.com/doc/product/tuikit/atomic-x/android/en/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.call/-call-store/calls.html).

Kotlin

Java

```
fun call(userId: String, callMediaType: TUICallDefine.MediaType)
```

```
 void call(String userId, TUICallDefine.MediaType callMediaType)
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID целевого пользователя. |
| callMediaType | [TUICallDefine.MediaType](https://www.tencentcloud.com/document/product/647/54900#MediaType) | Тип звонка, который может быть видео или аудио. |

### call

Этот API используется для выполнения (одностороннего) звонка, поддерживает пользовательский ID комнаты, время ожидания звонка, содержание автономной отправки и т. д.

> **Примечание:** **Рекомендуется использовать API** [calls](https://liteav.sdk.cloudcachetci.com/doc/product/tuikit/atomic-x/android/en/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.call/-call-store/calls.html).

Kotlin

Java

```
fun call(    userId: String, callMediaType: TUICallDefine.MediaType,    params: CallParams?, callback: TUICommonDefine.Callback?)
```

```
 void call(String userId, TUICallDefine.MediaType callMediaType,            TUICallDefine.CallParams params, TUICommonDefine.Callback callback)
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| userId | String | ID целевого пользователя. |
| callMediaType | [TUICallDefine.MediaType](https://www.tencentcloud.com/document/product/647/54900#MediaType) | Тип звонка, который может быть видео или аудио. |
| params | [TUICallDefine.CallParams](https://www.tencentcloud.com/document/product/647/54900#CallParams) | Параметры расширения звонка, такие как roomID, время ожидания звонка, информация об автономной отправке и т. д. |

### groupCall

Этот API используется для выполнения группового звонка.

> **Примечание:** Рекомендуется использовать API [calls](https://liteav.sdk.cloudcachetci.com/doc/product/tuikit/atomic-x/android/en/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.call/-call-store/calls.html). Перед выполнением группового звонка необходимо сначала создать группу Chat. Подробнее о создании группы см. в разделе [Управление группой Chat](https://www.tencentcloud.com/zh/document/product/1047/48466#.E5.88.9B.E5.BB.BA.E7.BE.A4.E7.BB.84) или вы можете использовать [Chat UIKit](https://www.tencentcloud.com/en/document/product/1047/50057) для интеграции чата, звонков и других сценариев.

Kotlin

Java

```
fun groupCall(groupId: String, userIdList: List<String?>?, callMediaType: TUICallDefine.MediaType)
```

```
void groupCall(String groupId, List<String> userIdList, TUICallDefine.MediaType callMediaType);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| groupId | String | ID группы. |
| userIdList | List | ID целевых пользователей. |
| callMediaType | [TUICallDefine.MediaType](https://www.tencentcloud.com/document/product/647/54900#MediaType) | Тип звонка, который может быть видео или аудио. |

### groupCall

Этот API используется для выполнения группового звонка, поддерживает пользовательский ID комнаты, время ожидания звонка, содержание автономной отправки и т. д.

> **Примечание:** Рекомендуется использовать API [calls](https://liteav.sdk.cloudcachetci.com/doc/product/tuikit/atomic-x/android/en/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.call/-call-store/calls.html). Перед выполнением группового звонка необходимо сначала создать группу Chat. Подробнее о создании группы см. в разделе [Управление группой Chat](https://www.tencentcloud.com/zh/document/product/1047/48466#.E5.88.9B.E5.BB.BA.E7.BE.A4.E7.BB.84) или вы можете использовать [Chat UIKit](https://www.tencentcloud.com/en/document/product/1047/50057) для интеграции чата, звонков и других сценариев.

Kotlin

Java

```
fun groupCall(    groupId: String, userIdList: List<String?>?,    callMediaType: TUICallDefine.MediaType, params: CallParams?,    callback: TUICommonDefine.Callback?)
```

```
void groupCall(String groupId, List<String> userIdList, TUICallDefine.MediaType callMediaType,                TUICallDefine.CallParams params, TUICommonDefine.Callback callback);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| groupId | String | ID группы. |
| userIdList | List | ID целевых пользователей. |
| callMediaType | [TUICallDefine.MediaType](https://www.tencentcloud.com/document/product/647/54900#MediaType) | Тип звонка, который может быть видео или аудио. |
| params | [TUICallDefine.CallParams](https://www.tencentcloud.com/document/product/647/54900#CallParams) | Параметры расширения звонка, такие как roomID, время ожидания звонка, информация об автономной отправке и т. д. |

### joinInGroupCall

Этот API используется для присоединения к групповому звонку.

> **Примечание:** Рекомендуется использовать API [join](https://liteav.sdk.cloudcachetci.com/doc/product/tuikit/atomic-x/android/en/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.call/-call-store/join.html). Перед присоединением к групповому звонку необходимо заранее создать или присоединиться к группе Chat, и в группе уже должны быть пользователи, которые участвуют в звонке. Подробнее о создании группы см. в разделе [Управление группой Chat](https://www.tencentcloud.com/zh/document/product/1047/48466#.E5.88.9B.E5.BB.BA.E7.BE.A4.E7.BB.84) или вы можете использовать [Chat UIKit](https://www.tencentcloud.com/en/document/product/1047/50057) для интеграции чата, звонков и других сценариев.

Kotlin

Java

```
fun joinInGroupCall(roomId: RoomId?, groupId: String?, callMediaType: TUICallDefine.MediaType?)
```

```
void joinInGroupCall(TUICommonDefine.RoomId roomId, String groupId, TUICallDefine.MediaType callMediaType);
```

Параметры описаны ниже:

| Параметр | Тип | Описание |
| --- | --- | --- |
| roomId | [TUICommonDefine.RoomId](https://www.tencentcloud.com/document/product/647/54900#RoomId) | ID комнаты. |
| groupId | String | ID группы. |
| callMediaType | [TUICallDefine.MediaType](https://www.tencentcloud.com/document/product/647/54900#MediaType) | Тип звонка, который может быть видео или аудио. |

### disableControlButton

Скрывает указанную кнопку.

> **Примечание:** В настоящее время поддерживается скрытие следующих кнопок: Камера, Микрофон, Устройство аудио, Переключение камеры, Пригласить пользователя. Поддерживается в версии **v3.2.+**.

Kotlin

Java

```
fun disableControlButton(button: Constants.ControlButton?)
```

```
void disableControlButton(Constants.ControlButton button);
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| button | ControlButton | Кнопка скрытия. |


---
*Источник: [https://trtc.io/document/51005](https://trtc.io/document/51005)*

---
*Источник (EN): [tuicallkit.md](./tuicallkit.md)*

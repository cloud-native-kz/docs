# TUICallKit

TUICallKit API — это **компонент аудио и видеозвонков, включающий интерфейс пользователя**. С помощью API TUICallKit вы можете быстро разработать сценарии аудио и видеозвонков, похожие на WeChat, благодаря простым интерфейсам. Для получения дальнейших подробных инструкций по интеграции см.: [Интеграция TUICallKit](https://trtc.io/document/50993).

## Обзор API

| API | Описание |
| --- | --- |
| [<TUICallKit/>](https://www.tencentcloud.com/document/product/647/51015#TUICallKit) | Основной компонент UI звонков. |
| [init](https://www.tencentcloud.com/document/product/647/51015#init) | Инициализировать TUICallKit. |
| [calls](https://www.tencentcloud.com/document/product/647/51015#calls) | Инициировать один-к-одному или групповой звонок. |
| [join](https://www.tencentcloud.com/document/product/647/51015#join) | Активное присоединение к звонку. |
| [setCallingBell](https://www.tencentcloud.com/document/product/647/51015#setCallingBell) | Настроить рингтон звонка пользователя. |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/51015#setSelfInfo) | Установить свой никнейм и аватар. |
| [enableMuteMode](https://www.tencentcloud.com/document/product/647/51015#enableMuteMode) | Включить/отключить рингтон. |
| [enableFloatWindow](https://www.tencentcloud.com/document/product/647/51015#enableFloatWindow) | Включить/отключить функцию плавающего окна. |
| [enableVirtualBackground](https://www.tencentcloud.com/document/product/647/51015#enableVirtualBackground) | Включить/отключить кнопку функции размытого фона. |
| [setLanguage](https://www.tencentcloud.com/document/product/647/51015#setLanguage) | Установить язык звонков для компонента TUICallKit. |
| [hideFeatureButton](https://www.tencentcloud.com/document/product/647/51015#hideFeatureButton) | Скрытие кнопки. |
| [setLocalViewBackgroundImage](https://www.tencentcloud.com/document/product/647/51015#setLocalViewBackgroundImage) | Установить фоновое изображение для интерфейса звонков локального пользователя. |
| [setRemoteViewBackgroundImage](https://www.tencentcloud.com/document/product/647/51015#setRemoteViewBackgroundImage) | Установить фоновое изображение для интерфейса звонков удалённого пользователя. |
| [setLayoutMode](https://www.tencentcloud.com/document/product/647/51015#setLayoutMode) | Установить режим макета интерфейса звонков. |
| [setCameraDefaultState](https://www.tencentcloud.com/document/product/647/51015#setCameraDefaultState) | Установить, открывается ли камера по умолчанию. |
| [destroyed](https://www.tencentcloud.com/document/product/647/51015#destroyed) | Уничтожить TUICallKit. |
| [getTUICallEngineInstance](https://www.tencentcloud.com/document/product/647/51015#getTUICallEngineInstance) | Получить экземпляр TUICallEngine. |

## Атрибуты `<TUICallKit/>`

### Обзор атрибутов

| Атрибут | Описание | Тип | Обязательно | Значение по умолчанию | Vue | React |
| --- | --- | --- | --- | --- | --- | --- |
| allowedMinimized | Разрешено ли плавающее окно? | boolean | Нет | false | ✓ | ✓ |
| allowedFullScreen | Разрешить ли полноэкранный режим для интерфейса звонков | boolean | Нет | true | ✓ | ✓ |
| [videoDisplayMode](https://www.tencentcloud.com/document/product/647/51015#videoDisplayMode) | Режим отображения интерфейса звонков | VideoDisplayMode | Нет | VideoDisplayMode.COVER | ✓ | ✓ |
| [videoResolution](https://www.tencentcloud.com/document/product/647/51015#videoResolution) | Разрешение звонка | VideoResolution | Нет | VideoResolution.RESOLUTION_480P | ✓ | ✓ |
| beforeCalling | Эта функция будет выполнена перед совершением звонка и перед получением приглашения на разговор | function(type, error) | Нет | - | ✓ | ✓ |
| afterCalling | Эта функция будет выполнена после завершения звонка | function() | Нет | - | ✓ | ✓ |
| onMinimized | Эта функция будет выполнена, когда компонент переходит в минимизированное состояние. Объяснение [значения STATUS приведено здесь](https://www.tencentcloud.com/document/product/647/51015#STATUS) | function(oldStatus, newStatus) | Нет | - | ✓ | ✓ |
| kickedOut | События, выбрасываемые компонентом, возникают, когда текущий вошедший в систему пользователь исключён. Звонок также автоматически завершится | function() | Нет | - | ✓ | ✗ |
| statusChanged | Событие, выбрасываемое компонентом; это событие срабатывает при изменении статуса звонка. Для подробного описания типов статуса звонка см. [описание значения STATUS](https://www.tencentcloud.com/document/product/647/51015#STATUS) | function({oldStatus, newStatus}) | Нет | - | ✓ | ✗ |

### Пример кода

React

Vue3

```
import { TUICallKit, VideoDisplayMode, VideoResolution } from "@trtc/calls-uikit-react";<TUICallKit    videoDisplayMode={VideoDisplayMode.CONTAIN}    videoResolution={VideoResolution.RESOLUTION_1080P}    beforeCalling={handleBeforeCalling}     afterCalling={handleAfterCalling} />function handleBeforeCalling(type: string, error: any) {  console.log("[TUICallkit Demo] handleBeforeCalling:", type, error);}function handleAfterCalling() {  console.log("[TUICallkit Demo] handleAfterCalling");}
```

```
<template>   <TUICallKit    :allowedMinimized="true"    :allowedFullScreen="true"    :videoDisplayMode="VideoDisplayMode.CONTAIN"    :videoResolution="VideoResolution.RESOLUTION_1080P"    :beforeCalling="beforeCalling"    :afterCalling="afterCalling"    :onMinimized="onMinimized"    :kickedOut="handleKickedOut"    :statusChanged="handleStatusChanged"  /></template><script lang="ts" setup>import { TUICallKit, TUICallKitAPI, VideoDisplayMode, VideoResolution, STATUS } from "@trtc/calls-uikit-vue";function beforeCalling(type: string, error: any) {  console.log("[TUICallkit Demo] beforeCalling:", type, error);}function afterCalling() {  console.log("[TUICallkit Demo] afterCalling");}function onMinimized(oldStatus: string, newStatus: string) {  console.log("[TUICallkit Demo] onMinimized: " + oldStatus + " -> " + newStatus);}function kickedOut() {  console.log("[TUICallkit Demo] kickedOut");}function statusChanged(args: { oldStatus: string; newStatus: string; }) {  const { oldStatus, newStatus } = args;  if (newStatus === STATUS.CALLING_C2C_VIDEO) {    console.log(`[TUICallkit Demo] statusChanged: ${oldStatus} -> ${newStatus}`);  }}</script>
```

## Подробная информация об API TUICallKitAPI

React

Vue3

```
import { TUICallKitAPI } from "@trtc/calls-uikit-react";
```

```
import { TUICallKitAPI } from "@trtc/calls-uikit-vue";
```

### init

Инициализировать TUICallKit.

```
try {  await TUICallKitAPI.init({ SDKAppID, userID, userSig });  // Если у вас уже есть экземпляр tim в вашем проекте, вам нужно передать его сюда  // await TUICallKitAPI.init({ tim, SDKAppID, userID, userSig});   console.log("[TUICallKit] Initialization succeeds.");} catch (error: any) {  console.error(`[TUICallKit] Initialization failed. Reason: ${error}`);}
```

Описание параметров ниже:

| Параметр | Тип | Обязательно | Значение |
| --- | --- | --- | --- |
| SDKAppID | Number | Да | SDKAppID вашего приложения, вы можете найти свой SDKAppID в консоли Live Audio and Video. Подробнее см. [Активация услуг](https://www.tencentcloud.com/document/product/647/59832) |
| userID | String | Да | ID текущего пользователя имеет строковый тип, допускает только включение букв английского алфавита (a-z и A-Z), цифр (0-9), дефисов (-) и подчёркиваний (_) |
| userSig | String | Да | Используйте SDKSecretKey для шифрования SDKAppID, UserID и другой информации для получения userSig. Это билет аутентификации, используемый Tencent Cloud для определения того, может ли текущий пользователь использовать услуги TRTC. Информацию о способе получения см. в разделе [Как рассчитать UserSig](https://www.tencentcloud.com/document/product/647/51024#calc_UserSig) |
| tim | TencentCloudChat | Нет | tim — это экземпляр SDK [TencentCloudChat](https://www.npmjs.com/package/@tencentcloud/chat). |

### calls

Инициировать один-к-одному или групповой звонок.

```
try {  await TUICallKitAPI.calls({     userIDList: ['jack', 'tom'],     type: CallMediaType.VIDEO   });} catch (error: any) {  console.error(`[TUICallKit] Failed to call the groupCall API. Reason:${error}`);}
```

Описание параметров ниже:

| **Параметр** | **Тип** | **Обязательно** | **Значение** |
| --- | --- | --- | --- |
| userIDList | Array<String> | Да | Список вызываемых пользователей |
| type | [CallMediaType](https://www.tencentcloud.com/document/product/647/51015#Type) | Да | Тип медиа для звонка, см. [CallMediaType для объяснения значений параметров](https://www.tencentcloud.com/document/product/647/51015#TUICallType) |
| chatGroupID | String | Да | ID группы чата. |
| roomID | Number | Нет | Числовой ID комнаты, диапазон [1, 2147483647] |
| strRoomID | String | Нет | ID комнаты со строковым типом. **v3.3.1+ поддерживается****диапазон:** Ограничено 64 байтами длины. Поддерживаемый набор символов выглядит следующим образом (всего 89 символов): Буквы английского алфавита в нижнем и верхнем регистре (a-zA-Z), числа (0-9), пробелы, `!`, `#`, `$`, `%`, `&`, `(`, `)`, `+`, `-`, `:`, `;`, `<`, `=`, `.`, `>`, `?`, `@`, `[`, `]`, `^`, `_`, `{`, `}`, `\|`, `~`, `,`. roomID и strRoomID взаимно исключают друг друга, если вы используете strRoomID, то roomID должен быть 0. Если вы используете оба, SDK будет приоритизировать roomID. 2. не смешивайте roomID и strRoomID, так как они не взаимозаменяемы, например, число 123 и строка "123" — это два совершенно разных помещения. |
| timeout | Number | Нет | Время ожидания звонка, по умолчанию: 30с, единица: секунды. timeout = 0, устанавливает без таймаута |
| userData | String | Нет | Пользовательские расширенные поля при инициировании звонка. Вызываемый пользователь имеет этот параметр в событии [ON_CALL_RECEIVED](https://www.tencentcloud.com/document/product/647/51017#on_call_received). |
| [offlinePushInfo](https://www.tencentcloud.com/document/product/647/51015#offlinePushInfo) | Object | Нет | Пользовательские параметры для автономной отправки сообщений |

### join

Активное присоединение к звонку.

```
try {  await TUICallKitAPI.join({     callId: 'xx'  });} catch (error: any) {  console.error(`[TUICallKit] Failed to call the join API. Reason:${error}`);}
```

Описание параметров ниже:

| **Параметр** | **Тип** | **Обязательно** | **Значение** |
| --- | --- | --- | --- |
| callId | String | Да | Уникальный ID для этого звонка |

### setLanguage

Установить язык, в настоящее время поддерживает: китайский, английский, японский.

```
TUICallKitAPI.setLanguage("zh-cn"); // "en" | "zh-cn" | "ja_JP"
```

Описание параметров ниже:

| Параметр | Тип | Обязательно | Значение |
| --- | --- | --- | --- |
| lang | String | Да | Тип языка `en`, `zh-cn` и `ja_JP`. |

### setSelfInfo

Установить свой никнейм и аватар.

> **Примечание:** **Если вы используете этот интерфейс для изменения информации пользователя во время звонка, UI не будет обновлён немедленно, и вам нужно будет дождаться следующего звонка, чтобы увидеть изменения.**

```
try {  await TUICallKitAPI.setSelfInfo({ nickName: "xxx", avatar: "http://xxx" });} catch (error: any) {  console.error(`[TUICallKit] Failed to call the setSelfInfo API. Reason: ${error}`;}
```

Описание параметров ниже:

| Параметр | Тип | Обязательно | Значение |
| --- | --- | --- | --- |
| nickName | String | Да | свой никнейм |
| avatar | String | Да | адрес собственного аватара |

### setCallingBell

- Настроить входящий рингтон звонка пользователя.
- Вход ограничен адресом файла локального формата MP3. Необходимо убедиться, что приложение имеет доступ к этому каталогу файлов.
- Используйте метод импорта для импорта файла рингтона.
- Если вам нужно восстановить рингтон по умолчанию, просто передайте пустой filePath.

```
import filePath from '../assets/phone_ringing.mp3';try {  await TUICallKitAPI.setCallingBell(filePath);} catch (error: any) {  console.error(`[TUICallKit] Failed to call the setCallingBell API. Reason: ${error}`);}
```

Описание параметров ниже:

| Параметр | Тип | Обязательно | Значение |
| --- | --- | --- | --- |
| filePath | String | Да | Путь к файлу рингтона |

### enableFloatWindow

Включить/отключить функцию плавающего окна. По умолчанию false. Кнопка плавающего окна в верхнем левом углу интерфейса звонков скрыта. Она будет отображена после установки значения true.

```
try {  const enable = true;  await TUICallKitAPI.enableFloatWindow(enable);} catch (error: any) {  console.error(`[TUICallKit] Failed to call the enableFloatWindow API. Reason: ${error}`);}
```

Описание параметров ниже:

| Параметр | Тип | Обязательно | Значение |
| --- | --- | --- | --- |
| enable | Boolean | Да | Включить/отключить функцию плавающего окна. По умолчанию false. |

### enableMuteMode

Включить/отключить рингтон для входящих звонков. При включении рингтон входящего звонка не будет воспроизводиться при получении запроса на звонок.

```
try {  const enable = true;  await TUICallKitAPI.enableMuteMode(enable);} catch (error: any) {  console.error(`[TUICallKit] Failed to call the enableMuteMode API. Reason: ${error}`);}
```

### enableVirtualBackground

Включить/отключить функцию размытого фона. Если вы хотите установить фоновое изображение как размытое, см. [Web](https://www.tencentcloud.com/document/product/647/60487). Вызывая интерфейс, вы можете отобразить кнопку функции размытого фона на UI и нажать на кнопку, чтобы напрямую включить функцию размытого фона.

```
import { TUICallKitAPI } from "@trtc/calls-uikit-react";const enable = true;TUICallKitAPI.enableVirtualBackground(enable);
```

Описание параметров ниже:

| Параметр | Тип | Обязательно | Значение |
| --- | --- | --- | --- |
| enable | boolean | Да | enable = true, показать кнопку размытого фона; enable = false, не показывать кнопку размытого фона |

### destroyed

- Завершить экземпляр TUICallKit.
- Этот метод не будет автоматически выходить из `tim`, требуется ручной выход: `tim.logout();`.

```
try {  await TUICallKitAPI.destroyed();} catch (error: any) {  console.error(`[TUICallKit] Failed to call the destroyed API. Reason: ${error}`);}
```

### hideFeatureButton

Скрытие кнопок функций, в настоящее время поддерживает только кнопки Camera, Microphone и Switch Camera.

```
TUICallKitAPI.hideFeatureButton(buttonName: FeatureButton);
```

Описание параметров ниже:

| **Параметр** | **Тип** | **Обязательно** | **Значение** |
| --- | --- | --- | --- |
| buttonName | [FeatureButton](https://www.tencentcloud.com/document/product/647/51015#FeatureButton) | Да | Название кнопки |

### setLocalViewBackgroundImage

Установить фоновое изображение для интерфейса звонков локального пользователя.

```
TUICallKitAPI.setLocalViewBackgroundImage(url: string);
```

Описание параметров ниже:

| **Параметр** | **Тип** | **Обязательно** | **Значение** |
| --- | --- | --- | --- |
| url | string | Да | Адрес изображения (поддерживает локальный путь и адрес сети) |

### setRemoteViewBackgroundImage

Установить фоновое изображение для интерфейса звонков удалённого пользователя.

```
TUICallKitAPI.setRemoteViewBackgroundImage(userId: string, url: string);
```

Описание параметров ниже:

| **Параметр** | **Тип** | **Обязательно** | **Значение** |
| --- | --- | --- | --- |
| userId | string | Да | ID удалённого пользователя, установка на '*' означает применение ко всем удалённым пользователям |
| url | string | Да | Адрес изображения (поддерживает локальный путь и адрес сети) |

### setLayoutMode

Установить режим макета интерфейса звонков.

Vue

React

```
import { TUICallKitAPI, LayoutMode } from "@trtc/calls-uikit-vue";TUICallKitAPI.setLayoutMode(LayoutMode.LocalInLargeView);
```

```
import { TUICallKitAPI, LayoutMode } from "@trtc/calls-uikit-react";TUICallKitAPI.setLayoutMode(LayoutMode.LocalInLargeView);
```

Список параметров:

| **Параметр** | **Тип** | **Обязательно** | **Значение** |
| --- | --- | --- | --- |
| layoutMode | [LayoutMode](https://www.tencentcloud.com/document/product/647/51015#LayoutMode) | Да | Режим макета пользовательского потока |

### setCameraDefaultState

Установить, открывается ли камера по умолчанию.

```
TUICallKitAPI.setCameraDefaultState(true);
```

Список параметров:

| Параметр | Тип | Обязательно | Значение |
| --- | --- | --- | --- |
| isOpen | boolean | Да | Включить ли камеру |

### getTUICallEngineInstance

Получить экземпляр TUICallEngine.

```
TUICallKitAPI.getTUICallEngineInstance();
```

## Определение типов TUICallKit

### videoDisplayMode

Режим отображения `videoDisplayMode` имеет три значения:

- `VideoDisplayMode.CONTAIN`
- `VideoDisplayMode.COVER`
- `VideoDisplayMode.FILL`, значение по умолчанию — `VideoDisplayMode.COVER`.

| Атрибут | Значение | Описание |
| --- | --- | --- |
| videoDisplayMode | VideoDisplayMode.CONTAIN | Наивысший приоритет — обеспечить полное отображение содержимого видео. Размеры видео масштабируются пропорционально, пока одна сторона не совпадёт с рамкой окна просмотра. В случае несовпадения размеров видео и окна отображения видео масштабируется — при сохранении соотношения сторон — для заполнения окна, в результате чего вокруг масштабированного видео появляется чёрная рамка. |
|  | VideoDisplayMode.COVER | Приоритет отдаётся обеспечению заполнения окна просмотра. Размер видео масштабируется пропорционально, пока всё окно не будет заполнено. Если размеры видео отличаются от размеров окна отображения, видеопоток будет обрезан или растянут в соответствии с соотношением окна. |
|  | VideoDisplayMode.FILL | Обеспечение отображения всего содержимого видео при заполнении окна не гарантирует сохранение пропорции исходного видео. Размеры видео будут растянуты в соответствии с размерами окна. |

### videoResolution

Разрешение `videoResolution` имеет три возможных значения:

- `VideoResolution.RESOLUTION_480P`
- `VideoResolution.RESOLUTION_720P`
- `VideoResolution.RESOLUTION_1080P`, значение по умолчанию — `VideoResolution.RESOLUTION_480P`.

**Объяснение разрешения:**

| Профиль видео | Разрешение (Ш x В) | Частота кадров (fps) | Битрейт (Kbps) |
| --- | --- | --- | --- |
| 480p | 640 × 480 | 15 | 900 |
| 720p | 1280 × 720 | 15 | 1500 |
| 1080p | 1920 × 1080 | 15 | 2000 |

**Часто задаваемые вопросы:**

- iOS 13&14 не поддерживает кодирование видео выше 720P. Рекомендуется ограничить максимальную сбор на 720P в этих двух версиях операционной системы. См. [Известная проблема iOS Safari случай 12](https://web.sdk.qcloud.com/trtc/webrtc/doc/en/tutorial-02-info-webrtc-issues.html#h2-4).
- Firefox не позволяет настраивать частоту кадров видео (по умолчанию установлено 30fps).
- Из-за влияния использования производительности системы, возможностей сбора камеры, ограничений браузера и других факторов фактические значения разрешения видео, частоты кадров и битрейта могут не полностью совпадать с установленными значениями. В таких сценариях браузер автоматически отрегулирует профиль, чтобы получить значения как можно ближе к установленным.

### STATUS

| Значение атрибута STATUS | Описание |
| --- | --- |
| STATUS.IDLE | Состояние ожидания |
| STATUS.BE_INVITED | Получено приглашение на аудио/видеозвонок |
| STATUS.DIALING_C2C | Инициирование один-к-одному звонка |
| STATUS.DIALING_GROUP | Инициирование группового звонка |
| STATUS.CALLING_C2C_AUDIO | Участие в звонке 1v1 audio |
| STATUS.CALLING_C2C_VIDEO | Участие в видеозвонке один-к-одному |
| STATUS.CALLING_GROUP_AUDIO | Участие в групповом аудиообщении |
| STATUS.CALLING_GROUP_VIDEO | Участие в групповом видеозвонке |

### **CallMediaType**

| Тип CallMediaType | Описание |
| --- | --- |
| CallMediaType.AUDIO_CALL | Аудиозвонок |
| CallMediaType.VIDEO | Видеозвонок |

### **offlinePushInfo**

| Параметр | Тип | Обязательно | Значение |
| --- | --- | --- | --- |
| offlinePushInfo.title | String | Нет | Название автономной отправки (опционально) |
| offlinePushInfo.description | String | Нет | Содержание автономной отправки (опционально) |
| offlinePushInfo.androidOPPOChannelID | String | Нет | Установка ID канала для телефонов OPPO с системой 8.0 и выше для автономной отправки (опционально) |
| offlinePushInfo.extension | String | Нет | Содержание, передаваемое автономной отправкой. Можно использовать для установки [режима уведомления](https://www.tencentcloud.com/document/product/647/51015#Notification mode) и [режима VoIP](https://www.tencentcloud.com/document/product/647/51015#VoIP mode) Android. **По умолчанию:** режим уведомления, это будет уведомление от системы; режим VoIP требует передачи поля. |
| offlinePushInfo.ignoreIOSBadge | Boolean | Нет | Игнорировать количество значков для автономной отправки (только для iOS), если установлено значение true, сообщение не будет увеличивать количество непрочитанных сообщений значка приложения на стороне получателя iOS. |
| offlinePushInfo.iOSSound | String | Нет | Установка звука автономной отправки (только для iOS). |
| offlinePushInfo.androidSound | String | Нет | Установка звука автономной отправки. |
| offlinePushInfo.androidVIVOClassification | Number | Нет | Классификация сообщений VIVO при отправке (устаревший интерфейс, служба отправки VIVO будет оптимизировать правила классификации сообщений 3 апреля 2023 года. Рекомендуется использовать setAndroidVIVOCategory для установки категории сообщений). 0: операционные сообщения, 1: системные сообщения. Значение по умолчанию — 1. |
| offlinePushInfo.androidXiaoMiChannelID | String | Нет | Установка ID канала для телефонов Xiaomi с системой Android 8.0 и выше. |
| offlinePushInfo.androidFCMChannelID | String | Нет | Установка ID канала для телефонов Google с системой Android 8.0 и выше. |
| offlinePushInfo.androidHuaWeiCategory | String | Нет | Классификация сообщений при отправке Huawei. |
| offlinePushInfo.isDisablePush | Boolean | Нет | Отключить ли уведомления о отправке (по умолчанию включено). |
| offlinePushInfo.iOSPushType | Number | Н

---
*Источник (EN): [tuicallkit.md](./tuicallkit.md)*

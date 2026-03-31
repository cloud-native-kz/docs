# RoomKit API

## Введение в API

TUIRoomKit API — это многопользовательский компонент для проведения встреч с **включённым пользовательским интерфейсом**. С помощью API TUIRoomKit вы можете быстро реализовать сценарий, подобный встречам, через простой интерфейс. Более подробные инструкции по интеграции см. в разделе: [Быстрая интеграция с TUIRoomKit](https://www.tencentcloud.com/document/product/647/54844#).

## Обзор API

- `<ConferenceMainView />:` Основной компонент пользовательского интерфейса TUIRoomkit.
- Conference: API, предоставляемый зависимостью `ConferenceMainView`.

| API | Описание |
| --- | --- |
| [getRoomEngine](https://www.tencentcloud.com/document/product/647/54885#b3295cfe-067f-4193-96f6-4a829dcfcc15) | Доступ к экземпляру roomEngine. Если roomEngine не существует, возвращает null. |
| [on](https://www.tencentcloud.com/document/product/647/54885#54e35df8-f2db-4796-81ea-10f775e92e4c) | Прослушивание событий указанного типа. При возникновении события вызывается функция обратного вызова. |
| [off](https://www.tencentcloud.com/document/product/647/54885#fd92a726-7469-46ca-af7c-5a36636a2782) | Отмена прослушивания событий указанного типа. |
| [login](https://www.tencentcloud.com/document/product/647/54885#5a429689-e07a-4c01-bfc6-bfb67f7f5b7f) | Вход в систему конференций. |
| [logout](https://www.tencentcloud.com/document/product/647/54885#40f8261a-7135-4739-8149-9984c105678b) | Выход из системы встреч. |
| [start](https://www.tencentcloud.com/document/product/647/54885#b0bf2a3b-428c-474f-9a0e-271c7c3b6bfd) | Начать новую встречу. |
| [join](https://www.tencentcloud.com/document/product/647/54885#b08d0951-c1f4-4db4-a84d-8414b853d0f1) | Присоединиться к существующей встречи. |
| [leave](https://www.tencentcloud.com/document/product/647/54885#ffc266fb-4207-4e59-b664-82ce6046758b) | Покинуть текущую встречу. |
| [dismiss](https://www.tencentcloud.com/document/product/647/54885#31e2d7df-1c4d-449f-80fa-e6e50ebe0f6f) | Завершить текущую встречу. |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/54885#949c2101-7f9f-435a-8a60-294df8545620) | Установить информацию о пользователе. |
| [setLanguage](https://www.tencentcloud.com/document/product/647/54885#51991a76-0777-4773-a2dd-91ce51b92b18) | Установить язык интерфейса. |
| [setTheme](https://www.tencentcloud.com/document/product/647/54885#5bb291c2-edb5-48b0-968a-db52ed2252ae) | Установить тему интерфейса. |
| [enableWatermark](https://www.tencentcloud.com/document/product/647/54885#daceee1b-175d-41a1-b495-d158fe01d63c) | Включить функцию водяного знака в приложении. Подробнее см. в разделе: [Текстовый водяной знак](https://www.tencentcloud.com/document/product/647/60531#). |
| [disableScreenSharing](https://www.tencentcloud.com/document/product/647/54885#833fce4f-6e77-45bf-bea0-33a618b540fb) | Отключить функцию совместного использования экрана в приложении. После вызова этой функции пользователи не смогут делиться своим экраном с другими. |
| [disableTextMessaging](https://www.tencentcloud.com/document/product/647/54885#9ed81bb6-73a0-4b75-878e-22cc641b43bc) | Отключить функцию отправки текстовых сообщений в приложении. После вызова этой функции пользователи не смогут отправлять или получать текстовые сообщения. |
| [hideFeatureButton](https://www.tencentcloud.com/document/product/647/54885#49c62018-9bc4-4117-bf68-aa985b868890) | Скрыть определённые кнопки функций в приложении. Вызвав эту функцию и передав соответствующие значения перечисления [FeatureButton](https://www.tencentcloud.com/document/product/647/54885#6f28a0a9-c315-400e-a73f-b1fbd0b039eb), соответствующие кнопки будут скрыты из пользовательского интерфейса. |

## Введение в атрибуты ConferenceMainView

### Обзор атрибутов

| Атрибут | Описание | Тип | Обязательный | Значение по умолчанию |
| --- | --- | --- | --- | --- |
| displayMode | Управление режимом отображения компонента: permanent: режим постоянного отображения. Компонент всегда отображается; внутреннее управление видимостью компонента не применяется. Если не контролируется бизнесом, компонент всегда остаётся видимым. wake-up: режим активации. Компонент активируется только после вызова интерфейса [conference start/join](https://www.tencentcloud.com/document/product/647/54885#b0bf2a3b-428c-474f-9a0e-271c7c3b6bfd) и официального присоединения к конференции; он не будет отображаться заранее. | 'permanent' \| 'wake-up' | Нет | permanent |

### Примеры кода

Vue3

Vue2

```
<template>  <ConferenceMainView display-mode="permanent"></ConferenceMainView></template><script setup>import { ConferenceMainView, conference } from '@tencentcloud/roomkit-electron-vue3';const init = async () => {    await conference.login({          sdkAppId: 0,      userId: '',      userSig: '',     });    await conference.start('123456', {      isSeatEnable: false,      isOpenCamera: true,      isOpenMicrophone: true,    });}init();</script>
```

```
<template>  <ConferenceMainView display-mode="permanent"></ConferenceMainView></template><script>import { ConferenceMainView, conference } from '@tencentcloud/roomkit-electron-vue2.7';export default {  components: {    ConferenceMainView,  },  async created() {    await conference.login({      sdkAppId: 0,      userId: '',      userSig: '',    });    await conference.start('123456', {      isSeatEnable: false,      isOpenCamera: true,      isOpenMicrophone: true,    });  },};</script>
```

## Подробное описание API Conference

Conference предоставляет набор методов для управления и управления функциями онлайн-встреч. Реализовав этот интерфейс, разработчики могут легко интегрировать функции онлайн-встреч в свои приложения.

### getRoomEngine

Доступ к экземпляру roomEngine. Если roomEngine не существует, возвращает null.

```
// Обратите внимание на имя пакета. Если вы используете версию vue2, пожалуйста, измените имя пакета на @tencentcloud/roomkit-electron-vue2.7import { conference, TUIRoomEngine } from '@tencentcloud/roomkit-electron-vue3';TUIRoomEngine.once('ready', () => {    const roomEngine = conference.getRoomEngine();});
```

Возвращает: *TUIRoomEngine | null*

### on

Прослушивание события указанного типа. При возникновении события вызывается функция обратного вызова.

Параметры описаны следующим образом:

| Параметр | Тип | Значение по умолчанию | Значение |
| --- | --- | --- | --- |
| eventType | [RoomEvent](https://www.tencentcloud.com/document/product/647/54885#76598037-a787-4283-adc1-34dd4474fe33) | - | Тип события для прослушивания |
| callback | () => void | - | Функция обратного вызова, вызываемая при возникновении события |

```
// Обратите внимание на имя пакета. Если вы используете версию vue2, пожалуйста, измените имя пакета на @tencentcloud/roomkit-electron-vue2.7import { conference, RoomEvent } from '@tencentcloud/roomkit-electron-vue3';conference.on(RoomEvent.RoomStart, () => {  console.log('[conference] The meeting has already started.')});conference.on(RoomEvent.ROOM_DISMISS, () => {  console.log('[conference] The meeting has been dismissed')});
```

Возвращает: *void*

### off

Отмена прослушивания событий указанного типа.

Параметры описаны следующим образом:

| Параметр | Тип | Значение по умолчанию | Значение |
| --- | --- | --- | --- |
| eventType | [RoomEvent](https://www.tencentcloud.com/document/product/647/54885#76598037-a787-4283-adc1-34dd4474fe33) | - | Тип события для отмены прослушивания |
| callback | () => void | - | Функция обратного вызова, добавленная ранее |

```
// Обратите внимание на имя пакета. Если вы используете версию vue2, пожалуйста, измените имя пакета на @tencentcloud/roomkit-electron-vue2.7import { conference } from '@tencentcloud/roomkit-electron-vue3';conference.off('event', callback);
```

Возвращает: *void*

### login

Вход в систему конференций.

Параметры описаны следующим образом:

| Параметр | Тип | Значение по умолчанию | Значение |
| --- | --- | --- | --- |
| params | {sdkAppId: number; userId: string; userSig: string; tim?: ChatSDK} | - | Объект параметров входа |
| sdkAppId | number | - | В [консоли реального аудио и видео](https://console.tencentcloud.com/trtc) нажмите **Управление приложением** > **создать приложение**. После создания нового приложения вы можете получить информацию sdkAppId в разделе **Информация приложения**. |
| userId | string | - | Рекомендуется ограничить длину ID пользователя 32 байтами, разрешены только прописные и строчные буквы (a-zA-Z), цифры (0-9), подчёркивания и дефисы. |
| userSig | string | - | Подпись userSig. Для метода расчёта userSig см. раздел [Связанное с UserSig](https://www.tencentcloud.com/document/product/647/35166). |
| tim | ChatSDK (опционально) | - | Если вы хотите использовать больше возможностей SDK мгновенного обмена сообщениями при интеграции roomEngine, вы можете передать созданный экземпляр tim в TUIRoomEngine. Инструкции по созданию экземпляра tim см. в разделе [TIM.create](https://web.sdk.qcloud.com/im/doc/zh-cn/TIM.html#.create). |

```
// Обратите внимание на имя пакета. Если вы используете версию vue2, пожалуйста, измените имя пакета на @tencentcloud/roomkit-electron-vue2.7import { conference } from '@tencentcloud/roomkit-electron-vue3';conference.login({  sdkAppId: 123456,  userId: 'testUser',  userSig: 'testSig'});
```

Возвращает: *Promise<void>*

### logout

Выход из системы встреч.

```
// Обратите внимание на имя пакета. Если вы используете версию vue2, пожалуйста, измените имя пакета на @tencentcloud/roomkit-electron-vue2.7import { conference } from '@tencentcloud/roomkit-electron-vue3';conference.logout();
```

Возвращает: *Promise<void>*

### start

Начать новую встречу.

Параметры описаны следующим образом:

| Параметр | Тип | Значение по умолчанию | Значение |
| --- | --- | --- | --- |
| roomId | string | - | ID комнаты встречи |
| params | [StartParams](https://www.tencentcloud.com/document/product/647/54885#d48132a7-b92a-4122-a1b0-bc821dcbab11) | - | Параметры для начала встречи |

```
// Обратите внимание на имя пакета. Если вы используете версию vue2, пожалуйста, измените имя пакета на @tencentcloud/roomkit-electron-vue2.7import { conference } from '@tencentcloud/roomkit-electron-vue3';conference.start('123456', {  roomName: 'TestRoom',  isSeatEnabled: false,  isOpenCamera: false,  isOpenMicrophone: false,});
```

Возвращает: *Promise<void>*

### join

Присоединиться к существующей встречи.

Параметры описаны следующим образом:

| Параметр | Тип | Значение по умолчанию | Значение |
| --- | --- | --- | --- |
| roomId | string | - | ID комнаты встречи |
| params | [JoinParams](https://www.tencentcloud.com/document/product/647/54885#2497d39a-9a74-4b86-b13f-240ae30217db) | - | Параметры для присоединения к встречи |

```
// Обратите внимание на имя пакета. Если вы используете версию vue2, пожалуйста, измените имя пакета на @tencentcloud/roomkit-electron-vue2.7import { conference } from '@tencentcloud/roomkit-electron-vue3';conference.join('123456', {  isOpenCamera: false,  isOpenMicrophone: false,});
```

Возвращает: *Promise<void>*

### leave

Покинуть текущую встречу.

```
// Обратите внимание на имя пакета. Если вы используете версию vue2, пожалуйста, измените имя пакета на @tencentcloud/roomkit-electron-vue2.7import { conference } from '@tencentcloud/roomkit-electron-vue3';conference.leave();
```

Возвращает: *Promise<void>*

### dismiss

Завершить текущую встречу.

```
// Обратите внимание на имя пакета. Если вы используете версию vue2, пожалуйста, измените имя пакета на @tencentcloud/roomkit-electron-vue2.7import { conference } from '@tencentcloud/roomkit-electron-vue3';conference.dismiss();
```

Возвращает: *Promise<void>*

### setSelfInfo

Установить информацию о пользователе.

Параметры описаны следующим образом:

| Параметр | Тип | Значение по умолчанию | Значение |
| --- | --- | --- | --- |
| options | {userName: string; avatarUrl: string} | - | Объект информации о пользователе |
| userName | string (опционально) | - | Имя пользователя |
| avatarUrl | string (опционально) | - | Фотография профиля пользователя |

```
// Обратите внимание на имя пакета. Если вы используете версию vue2, пожалуйста, измените имя пакета на @tencentcloud/roomkit-electron-vue2.7import { conference } from '@tencentcloud/roomkit-electron-vue3';conference.setSelfInfo({  userName: 'test-name',  avatarUlr: 'https://avatar.png'});
```

Возвращает: *Promise<void>*

### setLanguage

Установить язык интерфейса.

Параметры описаны следующим образом:

| Параметр | Тип | Значение по умолчанию | Значение |
| --- | --- | --- | --- |
| language | 'zh-CN' \| 'en-US' | - | Язык |

```
// Обратите внимание на имя пакета. Если вы используете версию vue2, пожалуйста, измените имя пакета на @tencentcloud/roomkit-electron-vue2.7import { conference } from '@tencentcloud/roomkit-electron-vue3';conference.setLanguage('en-US');
```

Возвращает: *void*

### setTheme

Установить тему интерфейса.

Параметры описаны следующим образом:

| Параметр | Тип | Значение по умолчанию | Значение |
| --- | --- | --- | --- |
| theme | 'LIGHT' \| 'DARK' | - | Тип темы |

```
// Обратите внимание на имя пакета. Если вы используете версию vue2, пожалуйста, измените имя пакета на @tencentcloud/roomkit-electron-vue2.7import { conference } from '@tencentcloud/roomkit-electron-vue3';conference.setTheme('DARK');
```

Возвращает: *void*

### enableWatermark

Включить функцию водяного знака в приложении. Подробнее см. в разделе: [Текстовый водяной знак](https://www.tencentcloud.com/document/product/647/60531#).

```
// Обратите внимание на имя пакета. Если вы используете версию vue2, пожалуйста, измените имя пакета на @tencentcloud/roomkit-electron-vue2.7import { conference } from '@tencentcloud/roomkit-electron-vue3';conference.enableWatermark();
```

Возвращает: *void*

### disableTextMessaging

Отключить функцию отправки текстовых сообщений в приложении. После вызова этой функции пользователи не смогут отправлять или получать текстовые сообщения.

```
// Обратите внимание на имя пакета. Если вы используете версию vue2, пожалуйста, измените имя пакета на @tencentcloud/roomkit-electron-vue2.7import { conference } from '@tencentcloud/roomkit-electron-vue3';conference.disableTextMessaging();
```

Возвращает: *void*

### disableScreenSharing

Отключить функцию совместного использования экрана в приложении. После вызова этой функции пользователи не смогут делиться своим экраном с другими.

```
// Обратите внимание на имя пакета. Если вы используете версию vue2, пожалуйста, измените имя пакета на @tencentcloud/roomkit-electron-vue2.7import { conference } from '@tencentcloud/roomkit-electron-vue3';conference.disableScreenSharing();
```

Возвращает: *void*

### hideFeatureButton

Скрыть определённые кнопки функций в приложении. Вызвав эту функцию и передав соответствующие значения перечисления [FeatureButton](https://www.tencentcloud.com/document/product/647/54885#6f28a0a9-c315-400e-a73f-b1fbd0b039eb), соответствующие кнопки будут скрыты из пользовательского интерфейса.

Параметры описаны следующим образом:

| Параметр | Тип | Значение по умолчанию | Значение |
| --- | --- | --- | --- |
| name | [FeatureButton](https://www.tencentcloud.com/document/product/647/54885#6f28a0a9-c315-400e-a73f-b1fbd0b039eb) | - | Имена скрываемых кнопок |

```
// Обратите внимание на имя пакета. Если вы используете версию vue2, пожалуйста, измените имя пакета на @tencentcloud/roomkit-electron-vue2.7import { conference, FeatureButton } from '@tencentcloud/roomkit-electron-vue3';conference.hideFeatureButton(FeatureButton.SwitchTheme);
```

Возвращает: *void*

## Определение типов

### RoomEvent (перечисление)

| Параметр | Тип | Описание |
| --- | --- | --- |
| ROOM_START | string | Создание встречи |
| ROOM_JOIN | string | Присоединение к встречи |
| ROOM_LEAVE | string | Покидание встречи |
| ROOM_DISMISS | string | Встреча завершена |
| KICKED_OFFLINE | string | Пользователь отключен от сети |
| KICKED_OUT | string | Участник удален из встречи |
| USER_LOGOUT | string | Пользователь вышел |
| ROOM_ERROR | string | Ошибка встречи |
| ROOM_NEED_PASSWORD | string | Пароль встречи |

### FeatureButton (значения перечисления)

| Параметр | Тип | Описание |
| --- | --- | --- |
| SwitchTheme | string | Кнопка функции переключения темы |
| SwitchLayout | string | Кнопка функции переключения макета |
| SwitchLanguage | string | Кнопка функции переключения языка |
| FullScreen | string | Кнопка функции полноэкранного режима |
| Invitation | string | Кнопка функции приглашения |
| BasicBeauty | string | Кнопка базовой красоты |

### StartParams

| Параметр | Тип | Описание | Значение по умолчанию |
| --- | --- | --- | --- |
| roomName | string (опционально) | Имя комнаты | - |
| isSeatEnabled | boolean (опционально) | Включить места | false |
| isOpenCamera | boolean (опционально) | Включить ли камеру | false |
| isOpenMicrophone | boolean (опционально) | Включить ли микрофон | false |
| defaultCameraId | string (опционально) | ID камеры по умолчанию | - |
| defaultMicrophoneId | string (опционально) | ID микрофона по умолчанию | - |
| defaultSpeakerId | string (опционально) | ID динамика по умолчанию | - |
| password | string (опционально) | Пароль встречи | - |

### JoinParams

| Параметр | Тип | Описание | Значение по умолчанию |
| --- | --- | --- | --- |
| isOpenCamera | boolean (опционально) | Включить ли камеру | false |
| isOpenMicrophone | boolean (опционально) | Включить ли микрофон | false |
| defaultCameraId | string (опционально) | ID камеры по умолчанию | - |
| defaultMicrophoneId | string (опционально) | ID микрофона по умолчанию | - |
| defaultSpeakerId | string (опционально) | ID динамика по умолчанию | - |
| password | string (опционально) | Пароль встречи | - |


---
*Источник: [https://trtc.io/document/54885](https://trtc.io/document/54885)*

---
*Источник (EN): [roomkit-api.md](./roomkit-api.md)*

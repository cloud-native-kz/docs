# RoomKit API

## Введение в API

TUIRoomKit API — это компонент для многопользовательских встреч с **встроенным пользовательским интерфейсом**. С помощью TUIRoomKit API вы можете быстро реализовать сценарий встречи через простой интерфейс. Для получения более подробных инструкций по интеграции см.: [Быстрая интеграция с TUIRoomKit](https://www.tencentcloud.com/document/product/647/54845#).

## Обзор API

- `<ConferenceMainView />:` Основной компонент пользовательского интерфейса TUIRoomkit.
- Conference: API, предоставляемый `ConferenceMainView`.

| API | Описание |
| --- | --- |
| [getRoomEngine](https://www.tencentcloud.com/document/product/647/54880#b3295cfe-067f-4193-96f6-4a829dcfcc15) | Получить экземпляр roomEngine. Если roomEngine не существует, вернёт null. |
| [on](https://www.tencentcloud.com/document/product/647/54880#54e35df8-f2db-4796-81ea-10f775e92e4c) | Слушать события указанного типа. При возникновении события будет вызвана функция обратного вызова. |
| [off](https://www.tencentcloud.com/document/product/647/54880#fd92a726-7469-46ca-af7c-5a36636a2782) | Отменить прослушивание событий указанного типа. |
| [login](https://www.tencentcloud.com/document/product/647/54880#5a429689-e07a-4c01-bfc6-bfb67f7f5b7f) | Войти в систему конференций. |
| [logout](https://www.tencentcloud.com/document/product/647/54880#40f8261a-7135-4739-8149-9984c105678b) | Выйти из системы встреч. |
| [start](https://www.tencentcloud.com/document/product/647/54880#b0bf2a3b-428c-474f-9a0e-271c7c3b6bfd) | Начать новую встречу. |
| [join](https://www.tencentcloud.com/document/product/647/54880#b08d0951-c1f4-4db4-a84d-8414b853d0f1) | Присоединиться к существующей встречe. |
| [leave](https://www.tencentcloud.com/document/product/647/54880#ffc266fb-4207-4e59-b664-82ce6046758b) | Покинуть текущую встречу. |
| [dismiss](https://www.tencentcloud.com/document/product/647/54880#31e2d7df-1c4d-449f-80fa-e6e50ebe0f6f) | Завершить текущую встречу. |
| [setSelfInfo](https://www.tencentcloud.com/document/product/647/54880#949c2101-7f9f-435a-8a60-294df8545620) | Установить вашу информацию пользователя. |
| [setLanguage](https://www.tencentcloud.com/document/product/647/54880#51991a76-0777-4773-a2dd-91ce51b92b18) | Установить язык интерфейса. |
| [setTheme](https://www.tencentcloud.com/document/product/647/54880#5bb291c2-edb5-48b0-968a-db52ed2252ae) | Установить тему интерфейса. |
| [enableWatermark](https://www.tencentcloud.com/document/product/647/54880#daceee1b-175d-41a1-b495-d158fe01d63c) | Включить функцию текстового водяного знака в приложении. Подробнее см.: [Текстовый водяной знак](https://www.tencentcloud.com/document/product/647/60531#). |
| [enableVirtualBackground](https://www.tencentcloud.com/document/product/647/54880#ac620717-1b58-42ed-b8a3-589bf0ad545e) | Включить функцию виртуального фона в приложении. После вызова этой функции на пользовательском интерфейсе будет отображена кнопка функции виртуального фона. Подробнее см.: [Виртуальный фон](https://www.tencentcloud.com/document/product/647/60533#). |
| [disableTextMessaging](https://www.tencentcloud.com/document/product/647/54880#9ed81bb6-73a0-4b75-878e-22cc641b43bc) | Отключить функцию текстовых сообщений в приложении. После вызова этой функции пользователи не смогут отправлять и получать текстовые сообщения. |
| [disableScreenSharing](https://www.tencentcloud.com/document/product/647/54880#833fce4f-6e77-45bf-bea0-33a618b540fb) | Отключить функцию совместного использования экрана в приложении. После вызова этой функции пользователи не смогут делиться своим экраном с другими. |
| [hideFeatureButton](https://www.tencentcloud.com/document/product/647/54880#49c62018-9bc4-4117-bf68-aa985b868890) | Скрыть определённые кнопки функций в приложении. Вызвав эту функцию и передав соответствующие значения перечисления [FeatureButton](https://www.tencentcloud.com/document/product/647/54880#6f28a0a9-c315-400e-a73f-b1fbd0b039eb), соответствующие кнопки будут скрыты в пользовательском интерфейсе. |

## Введение в атрибуты ConferenceMainView

### Обзор атрибутов

| Атрибут | Описание | Тип | Обязательный | Значение по умолчанию |
| --- | --- | --- | --- | --- |
| displayMode | Управление режимом отображения компонента. permanent: режим постоянного отображения. Компонент всегда отображается; внутреннее управление видимостью компонента не применяется. Если не контролируется бизнес-стороной, компонент будет всегда видим. wake-up: режим пробуждения. Компонент активируется только после вызова интерфейса [conference start/join](https://www.tencentcloud.com/document/product/647/54880#b0bf2a3b-428c-474f-9a0e-271c7c3b6bfd) и официального присоединения к конференции; заранее он не отображается. | 'permanent' \| 'wake-up' | Нет | permanent |

### Пример кода

Vue3

Vue2

```
<template>  <ConferenceMainView display-mode="permanent"></ConferenceMainView></template><script setup>import { ConferenceMainView, conference } from '@tencentcloud/roomkit-web-vue3';const init = async () => {    await conference.login({          sdkAppId: 0,      userId: '',      userSig: '',     });    await conference.start('123456', {      isSeatEnable: false,      isOpenCamera: true,      isOpenMicrophone: true,    });}init();</script>
```

```
<template>  <ConferenceMainView display-mode="permanent"></ConferenceMainView></template><script>import { ConferenceMainView, conference } from '@tencentcloud/roomkit-web-vue2.7';export default {  components: {    ConferenceMainView,  },  async created() {    await conference.login({      sdkAppId: 0,      userId: '',      userSig: '',    });    await conference.start('123456', {      isSeatEnable: false,      isOpenCamera: true,      isOpenMicrophone: true,    });  },};</script>
```

## Подробное описание Conference API

Conference предоставляет ряд методов для управления функциями онлайн-встреч. Реализуя этот интерфейс, разработчики могут легко интегрировать функции онлайн-встреч в свои приложения.

### getRoomEngine

Получить экземпляр roomEngine. Если roomEngine не существует, вернёт null.

```
// Обратите внимание на название пакета. Если вы используете версию vue2, измените название пакета на @tencentcloud/roomkit-web-vue2.7import { conference, TUIRoomEngine } from '@tencentcloud/roomkit-web-vue3';TUIRoomEngine.once('ready', () => {    const roomEngine = conference.getRoomEngine();});
```

Возвращаемое значение: *TUIRoomEngine | null*

### on

Слушать события указанного типа. При возникновении события будет вызвана функция обратного вызова.

Параметры описаны следующим образом:

| Параметр | Тип | Значение по умолчанию | Смысл |
| --- | --- | --- | --- |
| eventType | [RoomEvent](https://www.tencentcloud.com/document/product/647/54880#76598037-a787-4283-adc1-34dd4474fe33) | - | Тип события для прослушивания |
| callback | () => void | - | Функция обратного вызова, вызываемая при возникновении события |

```
// Обратите внимание на название пакета. Если вы используете версию vue2, измените название пакета на @tencentcloud/roomkit-web-vue2.7import { conference, RoomEvent } from '@tencentcloud/roomkit-web-vue3';conference.on(RoomEvent.RoomStart, () => {  console.log('[conference] Встреча уже началась.')});conference.on(RoomEvent.ROOM_DISMISS, () => {  console.log('[conference] Встреча была завершена')});
```

Возвращаемое значение: *void*

### off

Отменить прослушивание событий указанного типа.

Параметры описаны следующим образом:

| Параметр | Тип | Значение по умолчанию | Смысл |
| --- | --- | --- | --- |
| eventType | [RoomEvent](https://www.tencentcloud.com/document/product/647/54880#76598037-a787-4283-adc1-34dd4474fe33) | - | Тип события, для которого отменяется прослушивание |
| callback | () => void | - | Функция обратного вызова, добавленная ранее |

```
// Обратите внимание на название пакета. Если вы используете версию vue2, измените название пакета на @tencentcloud/roomkit-web-vue2.7import { conference } from '@tencentcloud/roomkit-web-vue3';conference.off('event', callback);
```

Возвращаемое значение: *void*

### login

Войти в систему конференций.

Параметры описаны следующим образом:

| Параметр | Тип | Значение по умолчанию | Смысл |
| --- | --- | --- | --- |
| params | {sdkAppId: number; userId: string; userSig: string; tim?: ChatSDK} | - | Объект параметров для входа |
| sdkAppId | number | - | В [консоли Real-time Audio and Video](https://console.tencentcloud.com/trtc) нажмите **Управление приложениями** > **создать приложение**. После создания нового приложения вы сможете получить информацию sdkAppId в разделе **Информация о приложении**. |
| userId | string | - | Рекомендуется ограничить длину User ID до 32 байтов, допускаются только прописные и строчные буквы (a-zA-Z), цифры (0-9), подчеркивание и дефис. |
| userSig | string | - | Подпись userSig. Для получения информации о методе расчёта userSig см. [UserSig Related](https://www.tencentcloud.com/document/product/647/35166). |
| tim | ChatSDK (опционально) | - | Если вы хотите использовать больше возможностей SDK для обмена сообщениями при интеграции roomEngine, вы можете передать созданный экземпляр tim в TUIRoomEngine. О том, как создать экземпляр tim, см. [TIM.create](https://web.sdk.qcloud.com/im/doc/zh-cn/TIM.html#.create). |

```
// Обратите внимание на название пакета. Если вы используете версию vue2, измените название пакета на @tencentcloud/roomkit-web-vue2.7import { conference } from '@tencentcloud/roomkit-web-vue3';conference.login({  sdkAppId: 123456,  userId: 'testUser',  userSig: 'testSig'});
```

Возвращаемое значение: *Promise<void>*

### logout

Выйти из системы встреч.

```
// Обратите внимание на название пакета. Если вы используете версию vue2, измените название пакета на @tencentcloud/roomkit-web-vue2.7import { conference } from '@tencentcloud/roomkit-web-vue3';conference.logout();
```

Возвращаемое значение: *Promise<void>*

### start

Начать новую встречу.

Параметры описаны следующим образом:

| Параметр | Тип | Значение по умолчанию | Смысл |
| --- | --- | --- | --- |
| roomId | string | - | ID комнаты встречи |
| params | [StartParams](https://www.tencentcloud.com/document/product/647/54880#d48132a7-b92a-4122-a1b0-bc821dcbab11) | - | Параметры для начала встречи |

```
// Обратите внимание на название пакета. Если вы используете версию vue2, измените название пакета на @tencentcloud/roomkit-web-vue2.7import { conference } from '@tencentcloud/roomkit-web-vue3';conference.start('123456', {  roomName: 'TestRoom',  isSeatEnabled: false,  isOpenCamera: false,  isOpenMicrophone: false,});
```

Возвращаемое значение: *Promise<void>*

### join

Присоединиться к существующей встречe.

Параметры описаны следующим образом:

| Параметр | Тип | Значение по умолчанию | Смысл |
| --- | --- | --- | --- |
| roomId | string | - | ID комнаты встречи |
| params | [JoinParams](https://www.tencentcloud.com/document/product/647/54880#2497d39a-9a74-4b86-b13f-240ae30217db) | - | Параметры для присоединения к встречe |

```
// Обратите внимание на название пакета. Если вы используете версию vue2, измените название пакета на @tencentcloud/roomkit-web-vue2.7import { conference } from '@tencentcloud/roomkit-web-vue3';conference.join('123456', {  isOpenCamera: false,  isOpenMicrophone: false,});
```

Возвращаемое значение: *Promise<void>*

### leave

Покинуть текущую встречу.

```
// Обратите внимание на название пакета. Если вы используете версию vue2, измените название пакета на @tencentcloud/roomkit-web-vue2.7import { conference } from '@tencentcloud/roomkit-web-vue3';conference.leave();
```

Возвращаемое значение: *Promise<void>*

### dismiss

Завершить текущую встречу.

```
// Обратите внимание на название пакета. Если вы используете версию vue2, измените название пакета на @tencentcloud/roomkit-web-vue2.7import { conference } from '@tencentcloud/roomkit-web-vue3';conference.dismiss();
```

Возвращаемое значение: *Promise<void>*

### setSelfInfo

Установить вашу информацию пользователя.

Параметры описаны следующим образом:

| Параметр | Тип | Значение по умолчанию | Смысл |
| --- | --- | --- | --- |
| options | {userName: string; avatarUrl: string} | - | Объект информации пользователя |
| userName | string (опционально) | - | Никнейм пользователя |
| avatarUrl | string (опционально) | - | Фото профиля пользователя |

```
// Обратите внимание на название пакета. Если вы используете версию vue2, измените название пакета на @tencentcloud/roomkit-web-vue2.7import { conference } from '@tencentcloud/roomkit-web-vue3';conference.setSelfInfo({  userName: 'test-name',  avatarUlr: 'https://avatar.png'});
```

Возвращаемое значение: *Promise<void>*

### setLanguage

Установить язык интерфейса.

Параметры описаны следующим образом:

| Параметр | Тип | Значение по умолчанию | Смысл |
| --- | --- | --- | --- |
| language | 'zh-CN' \| 'en-US' | - | Язык |

```
// Обратите внимание на название пакета. Если вы используете версию vue2, измените название пакета на @tencentcloud/roomkit-web-vue2.7import { conference } from '@tencentcloud/roomkit-web-vue3';conference.setLanguage('en-US');
```

Возвращаемое значение: *void*

### setTheme

Установить тему интерфейса.

Параметры описаны следующим образом:

| Параметр | Тип | Значение по умолчанию | Смысл |
| --- | --- | --- | --- |
| theme | 'LIGHT' \| 'DARK' | - | Тип темы |

```
// Обратите внимание на название пакета. Если вы используете версию vue2, измените название пакета на @tencentcloud/roomkit-web-vue2.7import { conference } from '@tencentcloud/roomkit-web-vue3';conference.setTheme('DARK');
```

Возвращаемое значение: *void*

### enableWatermark

Включить функцию текстовых сообщений в приложении. Подробнее см.: [Текстовый водяной знак](https://www.tencentcloud.com/document/product/647/60531#).

```
// Обратите внимание на название пакета. Если вы используете версию vue2, измените название пакета на @tencentcloud/roomkit-web-vue2.7import { conference } from '@tencentcloud/roomkit-web-vue3';conference.enableWatermark();
```

Возвращаемое значение: *void*

### enableVirtualBackground

Включить функцию виртуального фона в приложении. После вызова этой функции на пользовательском интерфейсе будет отображена кнопка функции виртуального фона. Подробнее см.: [Виртуальный фон](https://www.tencentcloud.com/document/product/647/60533#).

```
// Обратите внимание на название пакета. Если вы используете версию vue2, измените название пакета на @tencentcloud/roomkit-web-vue2.7import { conference } from '@tencentcloud/roomkit-web-vue3';conference.enableVirtualBackground();
```

Возвращаемое значение: *void*

### disableTextMessaging

Отключить функцию текстовых сообщений в приложении. После вызова этой функции пользователи не смогут отправлять и получать текстовые сообщения.

```
// Обратите внимание на название пакета. Если вы используете версию vue2, измените название пакета на @tencentcloud/roomkit-web-vue2.7import { conference } from '@tencentcloud/roomkit-web-vue3';conference.disableTextMessaging();
```

Возвращаемое значение: *void*

### disableScreenSharing

Отключить функцию совместного использования экрана в приложении. После вызова этой функции пользователи не смогут делиться своим экраном с другими.

```
// Обратите внимание на название пакета. Если вы используете версию vue2, измените название пакета на @tencentcloud/roomkit-web-vue2.7import { conference } from '@tencentcloud/roomkit-web-vue3';conference.disableScreenSharing();
```

Возвращаемое значение: *void*

### hideFeatureButton

Скрыть определённые кнопки функций в приложении. Вызвав эту функцию и передав соответствующие значения перечисления [FeatureButton](https://www.tencentcloud.com/document/product/647/54880#6f28a0a9-c315-400e-a73f-b1fbd0b039eb), соответствующие кнопки будут скрыты в пользовательском интерфейсе.

Параметры описаны следующим образом:

| Параметр | Тип | Значение по умолчанию | Смысл |
| --- | --- | --- | --- |
| name | [FeatureButton](https://www.tencentcloud.com/document/product/647/54880#6f28a0a9-c315-400e-a73f-b1fbd0b039eb) | - | Названия кнопок для скрытия |

```
// Обратите внимание на название пакета. Если вы используете версию vue2, измените название пакета на @tencentcloud/roomkit-web-vue2.7import { conference, FeatureButton } from '@tencentcloud/roomkit-web-vue3';conference.hideFeatureButton(FeatureButton.SwitchTheme);
```

Возвращаемое значение: *void*

## Определение типов

### RoomEvent (перечисление)

| Параметр | Тип | Описание |
| --- | --- | --- |
| ROOM_START | string | Создание встречи |
| ROOM_JOIN | string | Присоединение к встречe |
| ROOM_LEAVE | string | Покидание встречи |
| ROOM_DISMISS | string | Встреча завершена |
| KICKED_OFFLINE | string | Пользователь был отключён |
| KICKED_OUT | string | Участник удалён из встречи |
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
| roomName | string (опционально) | Название комнаты | - |
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
*Источник: [https://trtc.io/document/54880](https://trtc.io/document/54880)*

---
*Источник (EN): [roomkit-api.md](./roomkit-api.md)*

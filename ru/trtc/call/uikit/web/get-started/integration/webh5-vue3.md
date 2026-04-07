# Web&H5 (Vue3)

Этот документ описывает, как быстро интегрировать компонент TUICallKit. Вы можете выполнить следующие ключевые шаги в течение 10 минут и получить полный интерфейс аудио и видеовызова.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4b85ededb32c11f099275254005ef0f7.png)

## Подготовка

### **Требования к окружению**

- [Node.js](https://nodejs.org/en/) версия 16+.
- Современный браузер с поддержкой WebRTC API.

## Активирование сервиса

Перед использованием аудио и видеосервиса, предоставляемого Tencent Cloud, перейдите в консоль и активируйте сервис для своего приложения. Подробные инструкции см. в разделе [активирование сервиса](https://www.tencentcloud.com/document/product/647/59832). После включения сервиса запишите `SDKAppID` и `SDKSecretKey`, которые будут использоваться на последующих этапах (вход).

## Реализация

### Загрузка TUICallKit

1. Загрузите компонент [@trtc/calls-uikit-vue](https://www.npmjs.com/package/@trtc/calls-uikit-vue). В существующих проектах или пустых проектах, созданных с помощью инструментов каркаса, таких как @vue/cli или Vite, далее демонстрируется пустой проект, созданный с помощью @vue/cli.

```
npm install @trtc/calls-uikit-vue
```

2. Скопируйте каталог `debug` в каталог проекта `src/debug`. Это необходимо при локальном создании userSig.

macOS

Windows

```
cp -r node_modules/@trtc/calls-uikit-vue/debug ./src
```

```
xcopy node_modules\\@trtc\\calls-uikit-vue\\debug .\\src\\debug /i /e
```

### Добавление компонента TUICallKit

Вы можете выбрать импорт примера кода в файл `src/App.vue`. Пример кода использует подход `Composition API`.

1. Использование [<TUICallKit />](https://trtc.io/document/51015#init#tuicallkit), которое содержит полное взаимодействие пользовательского интерфейса во время вызова.

```
<template>  <span> caller's ID: </span>  <input type="text" v-model="callerUserID">   <button @click="init"> step1. init </button> <br>  <span> callee's ID: </span>  <input type="text" v-model="calleeUserID">  <button @click="call"> step2. call </button>    <!--ã1ãImport the TUICallKit component: Call interface UI -->  <TUICallKit style="width: 650px; height: 500px " /></template>
```

2. Использование API [TUICallKitAPI.init](https://trtc.io/document/51015#init) для входа в компонент. Вам нужно **заполнить `SDKAppID` и `SDKSecretKey`** в качестве двух параметров в коде.

```
<script setup> // lang='ts'import { ref } from 'vue';import { TUICallKit, TUICallKitAPI } from "@trtc/calls-uikit-vue";import * as GenerateTestUserSig from "./debug/GenerateTestUserSig-es"; // Refer to Step 2.3const SDKAppID = 0;       // TODO: Replace with your SDKAppID (Notice: SDKAppID is of type numberï¼const SDKSecretKey = '';  // TODO: Replace with your SDKSecretKeyconst callerUserID = ref('');const calleeUserID = ref('');//ã2ãInitialize the TUICallKit componentconst init = async () => {  const { userSig } = GenerateTestUserSig.genTestUserSig({    userID: callerUserID.value,     SDKAppID,    SecretKey: SDKSecretKey   });  await TUICallKitAPI.init({    userID: callerUserID.value,     userSig,     SDKAppID,  });  alert('TUICallKit init succeed');}</script>
```

| **Параметр** | **Тип** | **Примечание** |
| --- | --- | --- |
| userID | String | **Уникальный идентификатор пользователя**, **определяемый вами**, может содержать только прописные и строчные буквы (a-z, A-Z), цифры (0-9), подчеркивания и дефисы. |
| SDKAppID | Number | Уникальный идентификатор аудио и видео приложения, созданного в [консоли Tencent RTC](https://console.trtc.io/). |
| SDKSecretKey | String | Ключ SDKSecretKey аудио и видео приложения, созданного в [консоли Tencent RTC](https://console.trtc.io/). |
| userSig | String | Подпись защиты безопасности, используемая для аутентификации входа пользователя, подтверждения идентичности пользователя и предотвращения перехвата прав использования облачного сервиса злоумышленниками. |

> **Объяснение userSig:** **Среда разработки:** Если вы запускаете демо локально и проводите отладку разработки, вы можете использовать функцию `genTestUserSig` (см. шаг 3.2) в файле отладки для создания `userSig`. При этом методе SDKSecretKey уязвим для декомпиляции и обратного инжиниринга. После утечки вашего ключа злоумышленники могут украсть ваш трафик Tencent Cloud. **Рабочая среда:** Если ваш проект запускается в продакшене, используйте метод [серверной генерации UserSig](https://trtc.io/document/35166).

### Установка ника и аватара (опционально)

Пользователь, входящий в первый раз, не имеет информации об аватаре и нике. Вы можете установить аватар и ник через API [setSelfInfo](https://www.tencentcloud.com/document/product/647/51015#setSelfInfo).

```
try {  await TUICallKitAPI.setSelfInfo({    nickName: "jack",    avatar: "http://xxx",  });} catch (error: any) {  alert(`[TUICallKit] Failed to call the setSelfInfo API. Reason: ${error}`);}
```

> **Примечание:** Из-за ограничений конфиденциальности пользователя при вызовах между незнакомцами может возникнуть задержка в обновлении ника и аватара получателя. Это будет обновляться плавно после первого успешного вызова.

### Инициирование вызова

Инициатор может инициировать голосовой или видеовызов, вызвав функцию [calls](https://www.tencentcloud.com/document/product/647/51015#calls) и указав тип вызова и userID получателя. API [calls](https://www.tencentcloud.com/document/product/647/51015#calls) одновременно поддерживает один-к-одному и групповые вызовы. Когда userIDList содержит один userID, это вызов один-к-одному; когда userIDList содержит несколько userID, это групповой вызов.

1. Использование [TUICallKitAPI.calls API](https://trtc.io/document/51015#calls) для совершения вызова.

```
import { TUICallKitAPI, CallMediaType } from "@trtc/calls-uikit-vue";//ã3ãMake a 1v1 video callconst call = async () => {  await TUICallKitAPI.calls({    userIDList: [calleeUserID.value],    type: CallMediaType.VIDEO,  }); };
```

2. Запустите проект.

> **Предупреждение:** **Для локальной среды, пожалуйста, получайте доступ по протоколу `localhost`. Для тестирования в публичной сети, пожалуйста, получайте доступ по протоколу HTTPS. Подробности см. в** [описании протокола сетевого доступа](https://web.sdk.qcloud.com/trtc/webrtc/doc/en/tutorial-05-info-browser.html#h2-3).

3. Откройте две страницы браузера, **введите разные userID (определяемые вами)**, нажмите `step1. init` для входа (инициатор и получатель).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/601ba223668811efbd54525400f69702.png)

4. **После успешной инициализации обоих userID**, нажмите `step2. call` для совершения вызова. Если у вас есть проблемы с вызовом, см. [часто задаваемые вопросы](https://trtc.io/document/51024?platform=android&product=call#create_userID).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5dbee027668811efbd54525400f69702.png)

### Ответ на вызов

После завершения входа получателя инициатор может инициировать вызов, и получатель получит приглашение на вызов со звуком и вибрацией.

## Дополнительные функции

### Включение плавающего окна

Вы можете включить/отключить функцию плавающего окна, вызвав [enableFloatWindow](https://www.tencentcloud.com/document/product/647/51015#enableFloatWindow). Включите эту функцию при инициализации компонента TUICallKit. По умолчанию функция отключена (false). Нажмите кнопку плавающего окна в левом верхнем углу интерфейса вызова, чтобы свернуть интерфейс вызова в формат плавающего окна.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/99450b5ab32b11f099275254005ef0f7.png)

Используйте `enableFloatWindow(enable: boolean)` для включения/отключения плавающего окна.

```
TUICallKitAPI.enableFloatWindow(true)
```

### Установка звука входящего вызова

Вы можете настроить звук по умолчанию и режим без звука для входящих вызовов следующими методами:

- **Установка звука по умолчанию:** Используйте интерфейс setCallingBell для установки звука, который получает получатель.
  - Могут использоваться только локальные адреса файлов в формате MP3, при этом файл должен быть доступен.
  - Для сброса звука передайте пустую строку для filePath.
  - Используйте метод импорта ES6 для импорта файла звука.

```
import
```

- **Режим без звука для входящих вызовов:** Используйте интерфейс enableMuteMode для его настройки.

```
try {  await TUICallKitAPI.enableMuteMode(enable: boolean);} catch (error: any) {  alert(`[TUICallKit] enableMuteMode API failed. Reason: ${error}`);}
```

## Настройка вашего пользовательского интерфейса

### Замена значков

Для замены значка сначала требуется импорт исходного кода. Скопируйте компонент в ваш проект (исходный код находится в версии TypeScript).

> **Примечание:** План замены значков интерфейса подходит для проектов `Vue3 + TypeScript` и версии `@trtc/calls-uikit-vue` 3.2.2 или более поздней. Если вы используете другие языки или стеки технологий, используйте пользовательскую реализацию интерфейса.

1. **Загрузка исходного кода**

Vue3

```
npm install @trtc/calls-uikit-vue
```

2. **Скопируйте исходный код в ваш собственный проект, на примере копирования в каталог `src/components/`:**

macOS + Vue3

Windows + Vue3

```
mkdir -p ./src/components/TUICallKit && cp -r ./node_modules/@trtc/calls-uikit-vue/* ./src/components/TUICallKit
```

```
xcopy .\\node_modules\\@trtc\\calls-uikit-vue  .\\src\\components\\TUICallKit /i /e
```

3. **Изменение пути импорта**

Необходимо изменить путь импорта CallKit для импорта из локального файла, как показано ниже. Подробную информацию см. в разделе [быстрая интеграция TUICallKit](https://trtc.io/document/58484?platform=web&product=call).

```
import { TUICallKit, TUICallKitAPI } from "./components/TUICallKit/src/index";
```

4. **Решение ошибок, которые могут быть вызваны копированием исходного кода**

Если вы столкнулись с ошибкой при использовании компонента TUICallKit, не волнуйтесь. В большинстве случаев это происходит из-за несоответствия конфигураций ESLint и TSConfig. Вы можете проконсультироваться с документацией и правильно настроить конфигурацию по мере необходимости. Если вам нужна помощь, пожалуйста, свяжитесь с нами, и мы обеспечим успешное использование этого компонента. Вот некоторые распространенные проблемы:

Ошибка ESLint

Ошибка TypeScript

Если TUICallKit вызывает ошибку из-за несоответствия стилю кода вашего проекта, вы можете заблокировать этот каталог компонента, добавив файл `.eslintignore` в корневой каталог вашего проекта, например:

```
# .eslintignoresrc/components/TUICallKit
```

1. Если вы столкнулись с ошибкой 'Cannot find module '../package.json'', это потому, что TUICallKit ссылается на файл JSON. Вы можете добавить соответствующую конфигурацию в tsconfig.json, пример:

```
{  "compilerOptions": {    "resolveJsonModule": true  }}
```

Для других проблем TSConfig см. [справочник TSConfig](https://www.typescriptlang.org/tsconfig).

2. Если вы столкнулись с ошибкой 'Uncaught SyntaxError: Invalid or unexpected token', это потому, что TUICallKit использует декораторы. Вы можете добавить соответствующую конфигурацию в tsconfig.json, пример:

```
{  "compilerOptions": {    "experimentalDecorators": true  }}
```

5. **Изменение компонентов значков в папке TUICallKit/Components/assets**

> **Примечание:** Для обеспечения согласованности цвета и стиля значков во всем приложении, пожалуйста, сохраняйте имя файла значка без изменений при замене.

Рабочий стол

Мобильное устройство

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/98a7f482b32b11f0bb7b525400bf7822.png)

| Серийный номер | Путь ресурса | Описание |
| --- | --- | --- |
| 1 | /TUICallKit/Components/assets/button/camera-close.svg | Значок отключения камеры |
| 2 | /TUICallKit/Components/assets/button/microphone-open.svg | Значок включения микрофона |
| 3 | /TUICallKit/Components/assets/button/speaker-open.svg | Значок включения динамика |
| 4 | /TUICallKit/Components/assets/button/desktop/inviteUser.svg | Значок приглашения пользователя во время вызова |
| 5 | /TUICallKit/Components/assets/button/hangup.svg | Значок завершения вызова |
| 6 | /TUICallKit/Components/assets/button/desktop/minimize.svg | Значок минимизации |
| 7 | /TUICallKit/Components/assets/button/desktop/fullScreen.svg | Значок полного экрана |

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/98926282b32b11f0995e525400454e06.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/98a6be1db32b11f0bd1d5254001c06ec.png)

| Серийный номер | Путь ресурса | Описание |
| --- | --- | --- |
| 1 | /TUICallKit/Components/assets/button/mobile/minimize.svg | Значок минимизации |
| 2 | /TUICallKit/Components/assets/button/hangup.svg | Значок завершения вызова |
| 3 | /TUICallKit/Components/assets/button/accept.svg | Значок принятия |
| 4 | /TUICallKit/Components/assets/button/microphone-open.svg | Значок включения микрофона |
| 5 | /TUICallKit/Components/assets/button/speaker-open.svg | Значок включения динамика |
| 6 | /TUICallKit/Components/assets/button/camera-close.svg | Значок отключения камеры |
| 7 | /TUICallKit/Components/assets/button/switchCamera.svg | Значок переключения камеры |

### Скрытие кнопок

Вызовите интерфейс [hideFeatureButton](https://www.tencentcloud.com/document/product/647/51015#hideFeatureButton) для скрытия кнопок. В настоящее время поддерживаются Camera, Microphone, SwitchCamera, InviteUser. Подробности см. в типе перечисления [FeatureButton](https://www.tencentcloud.com/document/product/647/51015#FeatureButton).

Принимая скрытие **кнопки Camera** в качестве примера.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/98a530ffb32b11f099275254005ef0f7.png)

Vue3

```
import { TUICallKitAPI, FeatureButton } from "@trtc/calls-uikit-vue";TUICallKitAPI.hideFeatureButton(FeatureButton.Camera);
```

### Пользовательское изображение фона вызова

Изображение фона вызова отображается, когда камера отключена во время голосового или видеовызова. Измените изображение фона интерфейса вызова локального пользователя, вызвав [setLocalViewBackgroundImage](https://www.tencentcloud.com/document/product/647/51015#setLocalViewBackgroundImage), и измените изображение фона интерфейса вызова удаленного пользователя с помощью [setRemoteViewBackgroundImage](https://www.tencentcloud.com/document/product/647/51015#setRemoteViewBackgroundImage).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9900bc1eb32b11f097b152540099c741.png)

Vue3

```
import { TUICallKitAPI } from "@trtc/calls-uikit-vue";TUICallKitAPI.setLocalViewBackgroundImage('http://xxx.png');TUICallKitAPI.setRemoteViewBackgroundImage('remoteUserId', 'http://xxx.png');
```

### Установка макета

> **Примечание:** **Доступно только для видеовызовов 1V1.**

Используйте [setLayoutMode](https://www.tencentcloud.com/document/product/647/51015#setLayoutMode) для установки макета интерфейса вызова. В настоящее время поддерживаются только LocalInLargeView и RemoteInLargeView. Подробности см. в перечислении [LayoutMode](https://www.tencentcloud.com/document/product/647/51015#LayoutMode).

1. Макет LocalInLargeView с локальным пользователем в большом окне:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9902171fb32b11f097b152540099c741.png)

2. Макет RemoteInLargeView с удаленным пользователем в большом окне:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/98b65d68b32b11f0a6a2525400e889b2.png)

Vue3

```
import { TUICallKitAPI, LayoutMode } from "@trtc/calls-uikit-vue";TUICallKitAPI.setLayoutMode(LayoutMode.LocalInLargeView);
```

### Установка начального состояния камеры

Используйте [setCameraDefaultState](https://www.tencentcloud.com/document/product/647/51015#setCameraDefaultState) для установки начального состояния кнопки камеры. В настоящее время поддерживаются Enabled и Off.

Принимая отключенное по умолчанию состояние камеры в качестве примера:

Vue3

```
import { TUICallKitAPI } from "@trtc/calls-uikit-vue";TUICallKitAPI.setCameraDefaultState(false);
```

## Часто задаваемые вопросы

Если у вас возникли проблемы при интеграции и использовании, пожалуйста, см. [часто задаваемые вопросы](https://www.tencentcloud.com/document/product/647/51022).

## Свяжитесь с нами

Если у вас есть какие-либо предложения или отзывы, пожалуйста, свяжитесь с `info_rtc@tencent.com`.


---
*Источник: [https://trtc.io/document/50993](https://trtc.io/document/50993)*

---
*Источник (EN): [webh5-vue3.md](./webh5-vue3.md)*

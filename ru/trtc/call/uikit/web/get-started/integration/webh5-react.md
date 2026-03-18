# Web&H5 (React)

В этом документе описано, как быстро интегрировать компонент TUICallKit. Вы можете выполнить следующие ключевые шаги в течение 10 минут и получить полный интерфейс аудио и видео вызовов.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1479ccaab32c11f0a6a2525400e889b2.png)

## Подготовка

### **Требования к окружению**

- Версия React 18+, **не поддерживается 19+**.
- [Node.js](https://nodejs.org/en/) версия 16+.
- Современный браузер с поддержкой WebRTC API.

### Активировать сервис

Перед использованием аудио и видео сервиса, предоставляемого Tencent Cloud, перейдите в консоль и активируйте сервис для вашего приложения. Подробные инструкции см. в разделе [активирование сервиса](https://www.tencentcloud.com/document/product/647/59832). После активации сервиса сохраните `SDKAppID` и `SDKSecretKey`, которые будут использованы на последующих этапах (вход в систему).

## Реализация

### Загрузите TUICallKit

1. Загрузите компонент [@trtc/calls-uikit-react](https://www.npmjs.com/package/@trtc/calls-uikit-react). В существующих проектах или пустых проектах, созданных с помощью инструментов шаблонизации, таких как Vite, ниже описывается пустой проект, созданный с помощью Vite.

```
npm install @trtc/calls-uikit-react
```

2. Скопируйте директорию `debug` в директорию вашего проекта `src/debug`. Это необходимо при локальном генерировании userSig.

macOS

Windows

```
cp -r node_modules/@trtc/calls-uikit-react/debug ./src
```

```
xcopy node_modules\\@trtc\\calls-uikit-react\\debug .\\src\\debug /i /e
```

### Добавьте компонент TUICallKit

Вы можете выбрать импорт примера кода в файл `/src/App.tsx`.

1. Импортируйте call uikit.

```
import { useState } from 'react';import { TUICallKit, TUICallKitAPI } from "@trtc/calls-uikit-react";import * as GenerateTestUserSig from "./debug/GenerateTestUserSig-es"; // Обратитесь к шагу 2.2
```

2. Используйте [<TUICallKit />](https://trtc.io/document/51015#call#tuicallkit), который содержит полное взаимодействие пользовательского интерфейса во время вызова.

```
return (  <>    <span> ID звонящего: </span>    <input type="text" placeholder='input caller userID' onChange={(event) => setCallerUserID(event.target.value)} />    <button onClick={init}> шаг 1. инициализация </button> <br />    <span> ID получателя: </span>    <input type="text" placeholder='input callee userID' onChange={(event) => setCalleeUserID(event.target.value)} />    <button onClick={call}> шаг 2. вызов </button>        {/* ①Импортируйте компонент TUICallKit: интерфейс вызова */}    <TUICallKit />  </>);
```

3. Используйте API [TUICallKitAPI.init](https://trtc.io/document/51015#call#init) для входа в компонент. Вам необходимо `заполнить` `SDKAppID` и `SDKSecretKey` как два параметра в коде.

```
const SDKAppID = 0;        // TODO: Замените на ваш SDKAppID (Примечание: SDKAppID имеет тип number)const SDKSecretKey = '';   // TODO: Замените на ваш SDKSecretKeyconst [callerUserID, setCallerUserID] = useState('');const [calleeUserID, setCalleeUserID] = useState('');  //②Инициализируйте компонент TUICallKitconst init = async () => {  const { userSig } = GenerateTestUserSig.genTestUserSig({     userID: callerUserID,    SDKAppID,    SecretKey: SDKSecretKey,  });  await TUICallKitAPI.init({    userID: callerUserID,    userSig,    SDKAppID,  });  alert('TUICallKit init succeed');}
```

| **Параметр** | **Тип** | **Примечание** |
| --- | --- | --- |
| userID | String | **Уникальный идентификатор пользователя**, **определяется вами**, может содержать только прописные и строчные буквы (a-z, A-Z), цифры (0-9), подчеркивания и дефисы. |
| SDKAppID | Number | Уникальный идентификатор приложения аудио и видео, созданного в [консоли Tencent RTC](https://console.trtc.io/). |
| SDKSecretKey | String | SDKSecretKey приложения аудио и видео, созданного в [консоли Tencent RTC](https://console.trtc.io/). |
| userSig | String | Подпись для защиты безопасности, используется для аутентификации при входе пользователя в систему, подтверждает личность пользователя и предотвращает кража прав на использование облачного сервиса злоумышленниками. |

> **Объяснение userSig:** **Среда разработки:** если вы запускаете демонстрацию локально и разрабатываете отладку, вы можете использовать функцию `genTestUserSig` (см. шаг 3.2) в файле отладки для генерирования `userSig`. При этом методе SDKSecretKey уязвима к декомпиляции и обратной инженерии. Если ваш ключ утечет, злоумышленники смогут украсть ваш трафик Tencent Cloud. **Рабочая среда:** если ваш проект готов к запуску, пожалуйста, используйте метод [серверной генерации UserSig](https://trtc.io/document/35166).

### Установите прозвище и аватар (необязательно)

Пользователь, вошедший в систему впервые, не имеет информации об аватаре и прозвище. Вы можете установить аватар и прозвище через API [setSelfInfo](https://www.tencentcloud.com/document/product/647/51015#setSelfInfo).

```
try {  await TUICallKitAPI.setSelfInfo({    nickName: "jack",    avatar: "http://xxx",  });} catch (error: any) {  alert(`[TUICallKit] Ошибка вызова API setSelfInfo. Причина: ${error}`);}
```

> **Примечание:** в связи с ограничениями конфиденциальности пользователей для вызовов между незнакомцами может быть задержка при обновлении прозвища и аватара получателя вызова. Это будет обновляться плавно после первого успешного вызова.

### Начните вызов

Звонящий может инициировать голосовой или видео вызов, вызвав функцию [calls](https://www.tencentcloud.com/document/product/647/51015#calls) и указав тип вызова и userID получателя вызова. API [calls](https://www.tencentcloud.com/document/product/647/51015#calls) одновременно поддерживает один-на-один вызовы и групповые вызовы. Когда userIDList содержит один userID, это один-на-один вызов; когда userIDList содержит несколько userID, это групповой вызов.

1. Используйте [TUICallKitAPI.calls API](https://trtc.io/document/51015#calls) для совершения вызова.

```
import { TUICallKitAPI, CallMediaType } from "@trtc/calls-uikit-react";//③Совершите один-на-один видео вызовconst call = async () => {  await TUICallKitAPI.calls({    userIDIDList: [calleeUserID],    type: CallMediaType.VIDEO,  });};
```

2. Запустите проект.

> **Предупреждение:** **для локальной среды, пожалуйста, получайте доступ по протоколу localhost. Для публичного сетевого опыта, пожалуйста, получайте доступ по протоколу HTTPS. Подробности см. в разделе** [Описание сетевого протокола доступа](https://web.sdk.qcloud.com/trtc/webrtc/doc/en/tutorial-05-info-browser.html#h2-3).

3. Откройте две страницы браузера, **введите разные userID (определяется вами)**, нажмите `шаг 1. инициализация` для входа (звонящий и получатель вызова).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0634dc1f668811ef9664525400d5f8ef.png)

4. **После успешной инициализации обоих userID**, нажмите `шаг 2. вызов` для совершения вызова. Если у вас возникли проблемы с вызовом, обратитесь к [часто задаваемым вопросам](https://trtc.io/document/51024?platform=android&product=call#create_userID).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1f3e8349668811ef86bb525400fdb830.png)

### Ответ на вызов

После того как получатель вызова завершит вход в систему, звонящий может инициировать вызов, и получатель вызова получит приглашение на вызов с рингтоном и вибрацией.

## Дополнительные функции

### Включение плавающего окна

Вы можете включить/отключить функцию плавающего окна, вызвав [enableFloatWindow](https://www.tencentcloud.com/document/product/647/51015#enableFloatWindow). Включите эту функцию при инициализации компонента TUICallKit, статус по умолчанию отключен (false). Нажмите кнопку плавающего окна в верхнем левом углу интерфейса вызова, чтобы свернуть интерфейс вызова в формат плавающего окна.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2e9af4ebb31d11f09e195254007c27c5.png)

Используйте `enableFloatWindow(enable: boolean)` для включения/отключения плавающего окна.

```
TUICallKitAPI.enableFloatWindow(true)
```

### Установка рингтона входящего вызова

Вы можете настроить рингтон по умолчанию и режим без звука для входящих вызовов, используя следующие методы:

- **Установите рингтон по умолчанию:** используйте интерфейс setCallingBell для установки рингтона, который получает получатель вызова.
  - Можно использовать только локальные адреса файлов в формате MP3, убедитесь, что файл доступен.
  - Чтобы сбросить рингтон, передайте пустую строку для filePath.
  - Используйте метод импорта ES6 для импорта файла рингтона.

```
import
```

- **Режим без звука для входящих вызовов:** используйте интерфейс enableMuteMode для его настройки.

```
try {  await TUICallKitAPI.enableMuteMode(enable: boolean);} catch (error: any) {  alert(`[TUICallKit] Ошибка API enableMuteMode. Причина: ${error}`);}
```

## Персонализация вашего пользовательского интерфейса

### Замена иконок

Для замены иконки сначала требуется импорт исходного кода. Скопируйте компонент в ваш проект (исходный код находится в версии TypeScript).

> **Примечание:** план замены иконок интерфейса подходит для проектов `Vue3 + TypeScript` и версии `@trtc/calls-uikit-react` 3.2.2 или выше. Если вы используете другие языки или технологические стеки, пожалуйста, используйте пользовательскую реализацию пользовательского интерфейса.

1. **Загрузите исходный код**

React

```
npm install @trtc/calls-uikit-react
```

2. **Скопируйте исходный код в ваш проект, на примере копирования в директорию** `src/components/`:

macOS + React

Windows + React

```
mkdir -p ./src/components/TUICallKit && cp -r ./node_modules/@trtc/calls-uikit-react/* ./src/components/TUICallKit
```

```
xcopy .\\node_modules\\@trtc\\calls-uikit-react  .\\src\\components\\TUICallKit /i /e
```

3. **Измените путь импорта**

Необходимо изменить импорт CallKit так, чтобы он импортировался из локального файла, как показано ниже. Для подробностей использования см. [быструю интеграцию TUICallKit](https://trtc.io/document/58484?platform=web&product=call).

```
import { TUICallKit, TUICallKitAPI } from "./components/TUICallKit/src/index";
```

4. **Решите ошибки, которые могут быть вызваны копированием исходного кода**

Если вы столкнулись с ошибкой при использовании компонента TUICallKit, не волнуйтесь. В большинстве случаев это происходит из-за несоответствия конфигураций ESLint и TSConfig. Вы можете обратиться к документации и настроить правильно по мере необходимости. Если вам нужна помощь, пожалуйста, свяжитесь с нами, и мы обеспечим, чтобы вы могли успешно использовать этот компонент. Вот некоторые распространенные проблемы:

Ошибка ESLint

Ошибка TypeScript

Если TUICallKit вызывает ошибку из-за несоответствия стилю кода вашего проекта, вы можете заблокировать эту директорию компонента, добавив файл `.eslintignore` в корневую директорию вашего проекта, например:

```
# .eslintignoresrc/components/TUICallKit
```

1. Если вы столкнулись с ошибкой «Cannot find module '../package.json'», это потому что TUICallKit ссылается на файл JSON. Вы можете добавить соответствующую конфигурацию в tsconfig.json, пример:

```
{  "compilerOptions": {    "resolveJsonModule": true  }}
```

Для других проблем TSConfig обратитесь к [справочнику TSConfig](https://www.typescriptlang.org/tsconfig).

2. Если вы столкнулись с ошибкой «Uncaught SyntaxError: Invalid or unexpected token», это потому что TUICallKit использует декораторы. Вы можете добавить соответствующую конфигурацию в tsconfig.json, пример:

```
{  "compilerOptions": {    "experimentalDecorators": true  }}
```

5. **Измените компоненты иконок в папке TUICallKit/Components/assets**

> **Примечание:** чтобы цвет и стиль иконок оставались консистентными во всем приложении, при замене сохраняйте имя файла иконки неизменным.

Рабочий стол

Мобильный телефон

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/57d1c9c6b32a11f0b96752540044a08e.png)

| Номер | Путь ресурса | Описание |
| --- | --- | --- |
| 1 | /TUICallKit/Components/assets/button/camera-close.svg | Иконка отключения камеры |
| 2 | /TUICallKit/Components/assets/button/microphone-open.svg | Иконка включения микрофона |
| 3 | /TUICallKit/Components/assets/button/speaker-open.svg | Иконка включения динамика |
| 4 | /TUICallKit/Components/assets/button/desktop/inviteUser.svg | Иконка приглашения пользователя во время вызова |
| 5 | /TUICallKit/Components/assets/button/hangup.svg | Иконка завершения вызова |
| 6 | /TUICallKit/Components/assets/button/desktop/minimize.svg | Иконка минимизации |
| 7 | /TUICallKit/Components/assets/button/desktop/fullScreen.svg | Иконка полноэкранного режима |

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/57a4a16eb32a11f09e195254007c27c5.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/57aba9deb32a11f0bb7b525400bf7822.png)

| Номер | Путь ресурса | Описание |
| --- | --- | --- |
| 1 | /TUICallKit/Components/assets/button/mobile/minimize.svg | Иконка минимизации |
| 2 | /TUICallKit/Components/assets/button/hangup.svg | Иконка завершения вызова |
| 3 | /TUICallKit/Components/assets/button/accept.svg | Иконка принятия |
| 4 | /TUICallKit/Components/assets/button/microphone-open.svg | Иконка включения микрофона |
| 5 | /TUICallKit/Components/assets/button/speaker-open.svg | Иконка включения динамика |
| 6 | /TUICallKit/Components/assets/button/camera-close.svg | Иконка отключения камеры |
| 7 | /TUICallKit/Components/assets/button/switchCamera.svg | Иконка переключения камеры |

### Скрытие кнопки

Вызовите интерфейс [hideFeatureButton](https://www.tencentcloud.com/document/product/647/51015#hideFeatureButton) для скрытия кнопок, в настоящее время поддерживаются Camera, Microphone, SwitchCamera, InviteUser. Подробности см. в типе перечисления [FeatureButton](https://www.tencentcloud.com/document/product/647/51015#FeatureButton).

Взяв в качестве примера скрытие **кнопки Camera**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/33caa241b32a11f0bd1d5254001c06ec.png)

React

```
import { TUICallKitAPI, FeatureButton } from "@trtc/calls-uikit-react";TUICallKitAPI.hideFeatureButton(FeatureButton.Camera);
```

### Пользовательское фоновое изображение вызова

Фоновое изображение вызова отображается, когда камера отключена во время голосового или видео вызова. Измените фоновое изображение интерфейса вызова локального пользователя, вызвав [setLocalViewBackgroundImage](https://www.tencentcloud.com/document/product/647/51015#setLocalViewBackgroundImage), и измените фоновое изображение интерфейса вызова удаленного пользователя с помощью [setRemoteViewBackgroundImage](https://www.tencentcloud.com/document/product/647/51015#setRemoteViewBackgroundImage).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3422a53cb32a11f099275254005ef0f7.png)

React

```
import { TUICallKitAPI } from "@trtc/calls-uikit-react";TUICallKitAPI.setLocalViewBackgroundImage('http://xxx.png');TUICallKitAPI.setRemoteViewBackgroundImage('remoteUserId', 'http://xxx.png');
```

### Установка макета

> **Примечание:** **доступно только для один-на-один видео вызовов.**

Используйте [setLayoutMode](https://www.tencentcloud.com/document/product/647/51015#setLayoutMode) для установки макета интерфейса вызова, в настоящее время поддерживаются только LocalInLargeView и RemoteInLargeView, см. перечисление [LayoutMode](https://www.tencentcloud.com/document/product/647/51015#LayoutMode) для деталей.

1. Макет LocalInLargeView с локальным пользователем в большом окне:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/33e4b05bb32a11f099275254005ef0f7.png)

2. Макет RemoteInLargeView с удаленным пользователем в большом окне:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/33d66e0db32a11f097b152540099c741.png)

React

```
import { TUICallKitAPI, LayoutMode } from "@trtc/calls-uikit-react";TUICallKitAPI.setLayoutMode(LayoutMode.LocalInLargeView);
```

### Установка начального состояния камеры

Используйте [setCameraDefaultState](https://www.tencentcloud.com/document/product/647/51015#setCameraDefaultState) для установки начального состояния кнопки камеры, в настоящее время поддерживаются Enabled и Off.

Взяв в качестве примера состояние OFF камеры по умолчанию:

React

```
import { TUICallKitAPI } from "@trtc/calls-uikit-react";TUICallKitAPI.setCameraDefaultState(false);
```

## Часто задаваемые вопросы

Если вы столкнулись с проблемами при интеграции и использовании, обратитесь к [часто задаваемым вопросам](https://www.tencentcloud.com/document/product/647/51022).

## Свяжитесь с нами

Если у вас есть какие-либо предложения или отзывы, пожалуйста, свяжитесь с `info_rtc@tencent.com`.


---
*Источник: [https://trtc.io/document/58484](https://trtc.io/document/58484)*

---
*Источник (EN): [webh5-react.md](./webh5-react.md)*

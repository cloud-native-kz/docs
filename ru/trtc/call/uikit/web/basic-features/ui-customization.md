# Настройка пользовательского интерфейса

Этот документ описывает, как настроить пользовательский интерфейс `TUICallKit` и предоставляет две схемы для настройки: **небольшая корректировка пользовательского интерфейса** и **пользовательская реализация пользовательского интерфейса**.

## Схема 1: Небольшая корректировка пользовательского интерфейса

### Скрытие кнопок

Вызовите интерфейс [hideFeatureButton](https://www.tencentcloud.com/document/product/647/51015#bc0bf579-f35b-483b-a1c7-ae098d2e0e48) для скрытия кнопок, в настоящее время поддерживаются Camera, Microphone, SwitchCamera, InviteUser. Дополнительные сведения см. в типе перечисления [FeatureButton](https://www.tencentcloud.com/document/product/647/51015#6e728b5d-c006-4ccd-93d2-6542835b6366).

Возьмем в качестве примера скрытие **кнопки Camera**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/393375281fdc11efb2cb5254006568c0.png)

Vue3

React

```
import { TUICallKitAPI, FeatureButton } from "@trtc/calls-uikit-vue";TUICallKitAPI.hideFeatureButton(FeatureButton.Camera);
```

```
import { TUICallKitAPI, FeatureButton } from "@trtc/calls-uikit-react";TUICallKitAPI.hideFeatureButton(FeatureButton.Camera);
```

### Пользовательское изображение фона вызова

Изображение фона вызова отображается, когда камера выключена во время голосового или видеовызова. Измените фоновое изображение интерфейса вызова локального пользователя, вызвав [setLocalViewBackgroundImage](https://www.tencentcloud.com/document/product/647/51015#becf0aa7-fc00-49da-81da-f96782bd8357), и измените фоновое изображение интерфейса вызова удаленного пользователя с помощью [setRemoteViewBackgroundImage](https://www.tencentcloud.com/document/product/647/51015#e02ee7dd-5bea-4396-bc86-522e332053b4).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/395800971fdc11ef91395254000a29ac.png)

Vue3

React

```
import { TUICallKitAPI } from "@trtc/calls-uikit-vue";TUICallKitAPI.setLocalViewBackgroundImage('http://xxx.png');TUICallKitAPI.setRemoteViewBackgroundImage('remoteUserId', 'http://xxx.png');
```

```
import { TUICallKitAPI } from "@trtc/calls-uikit-react";TUICallKitAPI.setLocalViewBackgroundImage('http://xxx.png');TUICallKitAPI.setRemoteViewBackgroundImage('remoteUserId', 'http://xxx.png');
```

### Установка макета

> **Примечание：****Доступно только для видеовызовов 1V1.**

Используйте [setLayoutMode](https://www.tencentcloud.com/document/product/647/51015#a5410b97-d61e-4628-b349-8a0d23dc5ce8) для установки макета интерфейса вызова, в настоящее время поддерживаются только LocalInLargeView и RemoteInLargeView, см. перечисление [LayoutMode](https://www.tencentcloud.com/document/product/647/51015#5cd991d8-2784-4616-9068-6501e7b8b464) для получения дополнительных сведений.

1. Макет LocalInLargeView с локальным пользователем в большом окне:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/287c075b2e0b11ef9bb3525400ab9413.png)

2. Макет RemoteInLargeView с удаленным пользователем в большом окне:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/278d8e002e0b11ef9bb3525400ab9413.png)

Vue3

React

```
import { TUICallKitAPI, LayoutMode } from "@trtc/calls-uikit-vue";TUICallKitAPI.setLayoutMode(LayoutMode.LocalInLargeView);
```

```
import { TUICallKitAPI, LayoutMode } from "@trtc/calls-uikit-react";TUICallKitAPI.setLayoutMode(LayoutMode.LocalInLargeView);
```

### Установка начального состояния камеры

Используйте [setCameraDefaultState](https://www.tencentcloud.com/document/product/647/51015#eb19b592-e938-40a9-a03d-4e2c45eb0aa5) для установки начального состояния кнопки камеры, в настоящее время поддерживаются Enabled и Off.

Возьмем в качестве примера начальное состояние Off для камеры:

Vue3

React

```
import { TUICallKitAPI } from "@trtc/calls-uikit-vue";TUICallKitAPI.setCameraDefaultState(false);
```

```
import { TUICallKitAPI } from "@trtc/calls-uikit-react";TUICallKitAPI.setCameraDefaultState(false);
```

### Замена значков

Для замены значка сначала требуется импорт исходного кода. Скопируйте компонент в ваш проект (исходный код находится в версии TypeScript).

> **Примечание：**План замены значков интерфейса подходит для проектов `Vue3 + TypeScript` и версии `@trtc/calls-uikit-vue` 3.2.2 или более поздней версии. Если вы используете другие языки или технологические стеки, используйте пользовательскую реализацию пользовательского интерфейса.

1. **Загрузка исходного кода**

Vue3

```
npm install @trtc/calls-uikit-vue
```

2. **Скопируйте исходный код в ваш проект, например скопирование в директорию**`src/components/`**:**

macOS + Vue3

Windows + Vue3

```
mkdir -p ./src/components/TUICallKit && cp -r ./node_modules/@trtc/calls-uikit-vue/* ./src/components/TUICallKit
```

```
xcopy .\\node_modules\\@trtc\\calls-uikit-vue  .\\src\\components\\TUICallKit /i /e
```

3. **Изменение пути импорта**

Необходимо изменить импорт CallKit на импорт из локального файла, как показано ниже. Для получения других сведений об использовании см. [TUICallKit Quick Integration](https://trtc.io/document/58484?platform=web&product=call).

```
import { TUICallKit, TUICallKitAPI } from "./components/TUICallKit/src/index";
```

4. **Решение ошибок, которые могут быть вызваны копированием исходного кода**

Если при использовании компонента TUICallKit возникла ошибка, не волнуйтесь. В большинстве случаев это связано с несоответствиями между конфигурациями ESLint и TSConfig. Вы можете обратиться к документации и правильно настроить параметры по мере необходимости. Если вам нужна помощь, пожалуйста, свяжитесь с нами, и мы обеспечим успешное использование этого компонента. Вот некоторые распространенные проблемы:

Ошибка ESLint

Ошибка TypeScript

Если TUICallKit вызывает ошибку из-за несоответствия стилю кода вашего проекта, вы можете заблокировать эту директорию компонента, добавив файл `.eslintignore` в корневую директорию вашего проекта, например:

```
# .eslintignoresrc/components/TUICallKit
```

1. Если вы столкнулись с ошибкой 'Cannot find module '../package.json'', это потому, что TUICallKit ссылается на JSON файл. Вы можете добавить соответствующую конфигурацию в tsconfig.json, пример:

```
{  "compilerOptions": {    "resolveJsonModule": true  }}
```

Для других проблем TSConfig см. [TSConfig Reference](https://www.typescriptlang.org/tsconfig).

2. Если вы столкнулись с ошибкой 'Uncaught SyntaxError: Invalid or unexpected token', это потому, что TUICallKit использует декораторы. Вы можете добавить соответствующую конфигурацию в tsconfig.json, пример:

```
{  "compilerOptions": {    "experimentalDecorators": true  }}
```

5. **Измените компоненты значков в папке TUICallKit/Components/assets**

> **Примечание:**Чтобы обеспечить согласованность цвета и стиля значка во всем приложении, сохраняйте имя файла значка без изменений при замене.

Рабочий стол

Мобильный

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f9383978fd4c11ee8fa7525400ae4d13.png)

| Порядковый номер | Путь ресурса |
| --- | --- |
| 1 | /TUICallKit/Components/assets/button/camera-close.svg |
| 2 | /TUICallKit/Components/assets/button/microphone-open.svg |
| 3 | /TUICallKit/Components/assets/button/speaker-open.svg |
| 4 | /TUICallKit/Components/assets/button/desktop/inviteUser.svg |
| 5 | /TUICallKit/Components/assets/button/hangup.svg |
| 6 | /TUICallKit/Components/assets/button/desktop/minimize.svg |
| 7 | /TUICallKit/Components/assets/button/desktop/fullScreen.svg |

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a70000fbfca311eea33752540095b445.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0cbeb8aefd4d11ee8fa7525400ae4d13.png)

| Порядковый номер | Путь ресурса |
| --- | --- |
| 1 | /TUICallKit/Components/assets/button/mobile/minimize.svg |
| 2 | /TUICallKit/Components/assets/button/hangup.svg |
| 3 | /TUICallKit/Components/assets/button/accept.svg |
| 4 | /TUICallKit/Components/assets/button/microphone-open.svg |
| 5 | /TUICallKit/Components/assets/button/speaker-open.svg |
| 6 | /TUICallKit/Components/assets/button/camera-close.svg |
| 7 | /TUICallKit/Components/assets/button/switchCamera.svg |

### Замена звуков вызова

Вы можете заменить звуки вызова, заменив три аудиофайла в папке `TUICallKit/src/TUICallService/assets/`.

| Имя файла | Описание |
| --- | --- |
| phone_dialing.mp3 | Звук совершения вызова |
| phone_ringing.mp3 | Сигнал входящего вызова |

## Схема 2: Пользовательская реализация пользовательского интерфейса

Функции `TUICallKit` реализованы на основе SDK `TUICallEngine`, который не включает элементы пользовательского интерфейса. Вы можете использовать `TUICallEngine` для реализации собственного пользовательского интерфейса. Для получения подробных указаний обратитесь к документам ниже:

- [TUICallEngine integration guide](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/en/tutorial-00-%E5%AE%9E%E7%8E%B0%E5%8F%8C%E4%BA%BA%E9%80%9A%E8%AF%9D.html)
- [TUICallEngine APIs](https://trtc.io/document/51016)


---
*Источник: [https://trtc.io/document/50997](https://trtc.io/document/50997)*

---
*Источник (EN): [ui-customization.md](./ui-customization.md)*

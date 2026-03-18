# Vue3

Путем интеграции Chat и CallKit вы сможете добиться следующих эффектов. Нажмите [Попробовать онлайн](https://trtc.io/document/50061?platform=web&product=chat&menulabel=uikit).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c08c4920d32611efa2ff52540044a08e.png)

## Требования к окружению

- TypeScript
- Sass (версия sass-loader должна быть ≤ 10.1.1)
- node (node.js ≥ 16.0.0)
- npm (используйте версию, соответствующую используемой версии Node)

## Шаг 1: Интеграция Chat

Подробные инструкции см. в разделе: [Быстрая интеграция Chat](https://trtc.io/document/58644?platform=web&product=chat&menulabel=uikit).

## Шаг 2: Активация возможности аудио- и видеозвонков

Перед использованием аудио- и видеосервисов Tencent Cloud вам необходимо перейти в консоль и активировать сервис для приложения. Подробные шаги см. в разделе [Активировать сервис](https://trtc.io/document/59832).

## Шаг 3: Загрузка компонента TUICallKit

Загрузите компонент TUICallKit через [npm](https://www.npmjs.com/package/@tencentcloud/chat-uikit-vue), версия 3.3.6 и выше:

```
npm i @tencentcloud/call-uikit-react
```

## Шаг 4: Импорт и вызов компонента TUICallKit

Следующим образом: Импортируйте `<TUICallKit />` там, где импортируется `<TUIKit />`.

```
<template>  <div id="app">    <TUIKit :SDKAppID="YOUR_SDKAPPID" userID="YOUR_USERID" userSig="YOUR_USERSIG" />    <TUICallKit class="callkit-container" :allowedMinimized="true" :allowedFullScreen="false" />  </div></template><script lang="ts" setup>import { TUIKit } from './TUIKit';import { TUICallKit } from '@tencentcloud/call-uikit-vue';</script><style lang="scss"></style>
```

## Шаг 5: Запуск проекта

vite

webpack

```
npm run dev
```

```
npm run serve
```

## Шаг 6: Отправка первого сообщения

Как показано на рисунке, вы можете отправлять сообщения от друзей и друзьям.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9e3613c9d32511ef81865254005ef0f7.png)

## Шаг 7: Совершите свой первый звонок

Как показано на рисунке, нажмите значок видео/аудио на панели инструментов, чтобы реализовать эффект звонка.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b20eb825d32511efa4a3525400bf7822.png)

## Часто задаваемые вопросы

- Если у вас возникнут проблемы с доступом и использованием, см. раздел [Часто задаваемые вопросы](https://trtc.io/document/53565?platform=web&product=call).
- Если у вас есть какие-либо требования или отзывы, вы можете связаться с нами: info_rtc@tencent.com.


---
*Источник: [https://trtc.io/document/67769](https://trtc.io/document/67769)*

---
*Источник (EN): [vue3.md](./vue3.md)*

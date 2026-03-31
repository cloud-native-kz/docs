# Интеграция

TUIKit — это библиотека UI-компонентов на основе Chat SDK. Она позволяет быстро реализовать функции чата, сессий, поиска, цепочки отношений, групп и других возможностей через UI-компоненты. Данная статья описывает, как быстро интегрировать TUIKit и реализовать основные функции.

Либо, если вы предпочитаете более быстрый и автоматизированный подход, вы можете обратиться к разделу [Начало работы с интеграцией AI](https://www.tencentcloud.com/document/product/1047/72277) для оптимизации процесса.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/71eafaeab5f611eeb395525400461a83.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/78f28c36b5f611ee9d74525400c26da5.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8380eff8b5f611eea201525400170219.png)

## Ключевые понятия

TUIKit в основном разделяется на несколько UI-подкомпонентов: TUIChat, TUIConversation, TUIGroup, TUIContact и TUISearch. Каждый UI-компонент отвечает за отображение различного контента.

1. TUIChat предоставляет страницу сессии, включая список сообщений, заголовок и поле ввода.
2. TUIConversation предоставляет страницу списка сессий, включая список бесед, создание группы и C2C Chat.
3. TUIGroup предоставляет страницу управления групповым чатом, включая управление групповым чатом и управление членами группы.
4. TUIContact предоставляет страницу контактов, включая список контактов и запросы дружбы.
5. TUISearch предоставляет страницу облачного поиска.

## Предварительные требования

- Vue (полная поддержка Vue2 и Vue3, выберите соответствующую версию Vue при доступе к руководству ниже)
- TypeScript (если ваш проект основан на JavaScript, обратитесь к разделу [Интеграция JS-проекта](https://www.tencentcloud.com/document/product/1047/58644#84b6b984-9573-4dd4-a2f8-bcdcd2cabce2) для постепенной поддержки TypeScript)
- sass (версия sass ≤ 1.77.4, версия sass-loader ≤ 10.1.1)
- node (node.js ≥ 18.0.0)
- npm (версия должна соответствовать версии node)

## Шаги интеграции

### Шаг 1. Создание проекта

TUIKit поддерживает использование vite или vue-cli для создания проектов, конфигурирующих Vue3/Vue2 с TypeScript и sass. Ниже приведены примеры настройки проекта:

vite

vue-cli

> **Примечание:** Vite требует версию [**Node.js**](https://nodejs.org/en/) 18+ или 20+. Когда ваш менеджер пакетов выдает предупреждение, обратите внимание на обновление версии Node. Подробнее см. на [официальном сайте vite](https://cn.vitejs.dev/guide/).

Создайте проект с помощью vite, настроив Vue + TypeScript, как показано на рисунке ниже.

```
npm create vite@5
```

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/769c3cdeb57411f09a6b525400454e06.png)

Перейдите в каталог проекта, затем установите зависимости проекта:

```
cd chat-examplenpm install
```

Установите необходимую зависимость окружения sass для TUIKit:

```
npm i -D sass@1.77.0 sass-loader@10.1.1
```

Добавьте следующее правило компиляции в файл корневого каталога `tsconfig.app.json`:

typescript ≥ 5.0.0

typescript < 5.0.0

```
{  ...  "compilerOptions": {    ...    "verbatimModuleSyntax": false,  }}
```

```
{  ...  "compilerOptions": {    ...    "importsNotUsedAsValues": "preserve",  }}
```

> **Примечание:** Если в вашем `tsconfig.json` уже есть конфигурация `references`, например автоматически настроенные vite `"./tsconfig.app.json"` и `"./tsconfig.node.json"`, из-за характеристик `references` сам `tsconfig.json` служит только файлом ссылки на правила. В этом случае прямая конфигурация следующих правил в `tsconfig.json` недействительна. Необходимо добавить правила в соответствующий файл `references`. Ниже приведен конкретный пример: Ошибочное форматированиеПравильный стиль записиКогда файл tsconfig.json имеет существующую конфигурацию references, объявление следующих правил непосредственно в tsconfig.json недействительно. Когда файл tsconfig.json имеет существующую конфигурацию references, следующие правила должны быть объявлены во внутреннем файле соответствующих references. Ниже приведена конфигурация следующих правил в файле корневого каталога `tsconfig.app.json` в рамках references ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/82641b72b57411f0a6c652540044a08e.png).

> **Примечание:** Обратите внимание на то, чтобы убедиться, что ваша **версия @vue/cli 5.0.0** или выше. Вы можете использовать следующий пример кода для обновления версии @vue/cli до v5.0.8.

Создайте проект с помощью vue-cli, настроив Vue2 / Vue3 + TypeScript + sass.

Если вы не установили vue-cli или версия ниже 5.0.0, вы можете установить его в терминал или cmd следующим образом:

```
npm install -g @vue/cli@5.0.8 sass@1.77.0 sass-loader@10.1.1
```

Создайте проект с помощью vue-cli и выберите указанную конфигурацию на рисунке ниже.

```
vue create chat-example
```

Убедитесь в выборе следующей конфигурации:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/76affbd2b57411f0a6c652540044a08e.png)

После создания перейдите в каталог проекта:

```
cd chat-example
```

Если вы используете vue 2, настройте окружение на основе вашей версии vue. Для проектов vue 3 пропустите это.

vue2.7

Vue 2.6 и ниже

```
npm i vue@2.7.9 vue-template-compiler@2.7.9
```

```
npm i @vue/composition-api unplugin-vue2-script-setup vue@2.6.14 vue-template-compiler@2.6.14
```

### Шаг 2. Загрузка компонента TUIKit

Загрузите компонент TUIKit через [npm](https://www.npmjs.com/package/@tencentcloud/chat-uikit-vue). Для облегчения последующего расширения рекомендуется скопировать компонент TUIKit в каталог src вашего проекта:

macOS

Windows

```
npm i @tencentcloud/chat-uikit-vuemkdir -p ./src/TUIKit && rsync -av --exclude={'node_modules','package.json','excluded-list.txt'} ./node_modules/@tencentcloud/chat-uikit-vue/ ./src/TUIKit
```

```
npm i @tencentcloud/chat-uikit-vue
```

```
xcopy .\\node_modules\\@tencentcloud\\chat-uikit-vue .\\src\\TUIKit /i /e /exclude:.\\node_modules\\@tencentcloud\\chat-uikit-vue\\excluded-list.txt
```

### Шаг 3. Импорт компонента TUIKit

##### На странице, где вы хотите его отобразить, просто импортируйте компонент TUIKit для его использования.

> **Примечание:** Чтобы соблюсти авторские права на дизайн эмодзи, проект Chat Demo/TUIKit не включает вырезки больших элементов эмодзи. Перед официальным запуском для коммерческого использования замените их на собственные дизайны или другие пакеты эмодзи, на которые вы имеете авторские права. **Показанный ниже пакет улыбающихся эмодзи по умолчанию защищен авторским правом Tencent RTC**, вы можете обновить до [Chat Pro Plus Edition и Enterprise Edition](https://console.trtc.io/subscription/buy/chat?packType=pro) для его бесплатного использования. ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6a1e26fb97f711ef967c525400a9236a.png)

##### Например, реализация следующего кода на странице App.vue позволяет быстро установить интерфейс чата (следующий пример кода поддерживает как Web, так и H5):

> **Примечание:** Приведенный ниже пример кода использует синтаксис setup. Если ваш проект не использует синтаксис setup, зарегистрируйте компоненты в соответствии со стандартными методами Vue3/Vue2.

vue3

vue2.7

vue2.6 и ниже

```
<template>  <div id="app">    <TUIKit :SDKAppID="YOUR_SDKAPPID" userID="YOUR_USERID" userSig="YOUR_USERSIG" />    <TUICallKit class="callkit-container" :allowedMinimized="true" :allowedFullScreen="false" />  </div></template><script lang="ts" setup>import { TUIKit } from './TUIKit';import { TUICallKit } from '@trtc/calls-uikit-vue';</script><style lang="scss"></style>
```

Если это проект, построенный с помощью vite, вы можете закомментировать неправильный стиль по умолчанию в проекте. При необходимости вы можете удалить ненужное содержимое.

src/style.css

```
#app {  /* max-width: 1280px; */  margin: 0 auto;  /* padding: 2rem; */  text-align: center;}
```

```
<template>  <div id="app">    <TUIKit :SDKAppID="YOUR_SDKAPPID" userID="YOUR_USERID" userSig="YOUR_USERSIG" />    <TUICallKit class="callkit-container" :allowedMinimized="true" :allowedFullScreen="false" />  </div></template><script lang="ts" setup>import { TUIKit } from './TUIKit';import { TUICallKit } from '@trtc/calls-uikit-vue2';</script><style lang="scss"></style>
```

Если это проект, построенный с помощью vite, вы можете закомментировать неправильный стиль по умолчанию в проекте. При необходимости вы можете удалить ненужное содержимое.

src/style.css

```
#app {  /* max-width: 1280px; */  margin: 0 auto;  /* padding: 2rem; */  text-align: center;}
```

```
<template>  <div id="app">   <TUIKit :SDKAppID="YOUR_SDKAPPID" userID="YOUR_USERID" userSig="YOUR_USERSIG" />    <TUICallKit class="callkit-container" :allowedMinimized="true" :allowedFullScreen="false" />  </div></template><script lang="ts" setup>import { TUIKit } from './TUIKit';import { TUICallKit } from '@trtc/calls-uikit-vue2.6';</script><style lang="scss"></style>
```

1. Установите зависимости, поддерживающие composition-api и script setup, а также зависимости, связанные с vue2.6.

```
npm i @vue/composition-api unplugin-vue2-script-setup vue@2.6.14 vue-template-compiler@2.6.14
```

2. Импортируйте VueCompositionAPI в `main.ts/main.js`.

```
import VueCompositionAPI from "@vue/composition-api";Vue.use(VueCompositionAPI);
```

3. Добавьте следующее в `vue.config.js`. Если файл не существует, создайте его.

```
const ScriptSetup = require("unplugin-vue2-script-setup/webpack").default;module.exports = {  parallel: false, // disable thread-loader, which is not compactible with this plugin  configureWebpack: {    plugins: [      ScriptSetup({        /* options */      }),    ],  },  chainWebpack(config) {    // disable type check and let `vue-tsc` handles it    config.plugins.delete("fork-ts-checker");  },};
```

4. В конце файла `src/TUIKit/adapter-vue.ts` замените источник экспорта:

```
// Исходное обозначениеexport * from "vue";// Замените наexport * from "@vue/composition-api";
```

Если это проект, построенный с помощью vite, вы можете закомментировать неправильный стиль по умолчанию в проекте. При необходимости вы можете удалить ненужное содержимое.

src/style.css

```
#app {  /* max-width: 1280px; */  margin: 0 auto;  /* padding: 2rem; */  text-align: center;}
```

### Шаг 4: Получение SDKAppID, userID и userSig

Установите соответствующие параметры SDKAppID, userID и соответствующий userSig в `<TUIKit>`:

- `SDKAppID` можно получить через [Chat Console](https://console.trtc.io/app) в разделе `Applications`:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2cdb24b2353011ef94925254002693fd.png)

- `userID`
  - Нажмите, чтобы войти в [Application](https://console.trtc.io/app), созданное выше. Вы увидите вход продукта `Chat` на левой боковой панели. Нажмите, чтобы войти.
  - После входа на подстраницу продукта Chat нажмите на `Users`, чтобы перейти на страницу управления пользователями.
  - Нажмите `Create account`, появится форма для создания информации учетной записи. Если вы просто обычный пользователь, мы рекомендуем вам выбрать тип `General`.
  - Чтобы улучшить ваш опыт с функциями отправки и получения сообщений, мы рекомендуем создать два userID.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2dc4eb43353011ef9c9c525400d5f8ef.png)

- `userSig` может быть создан в реальном времени с помощью инструментов разработки, предоставляемых консолью. Для доступа к инструментам разработки нажмите [Chat Console > Development Tools > UserSig Tools > Signature (UserSig) Generator](https://console.trtc.io/usersig).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2c01dfce353011ef94925254002693fd.png)

### Шаг 5. Запуск проекта

Выполните следующую команду для запуска проекта:

vite

vue-cli

```
npm run dev
```

> **Примечание:** Поскольку vue-cli по умолчанию включает глобальное сообщение об ошибке Webpack Global Overlay, для лучшего опыта **рекомендуется отключить глобальное оверлей-сообщение об ошибках**. Webpack4 и выше Webpack3 module.exports = defineConfig({  ...  // Добавьте новый код конфигурации overlay для закрытия  devServer: {    client: {      overlay: false,    },  },});module.exports = {  ...  // Добавьте новый код конфигурации overlay  devServer: {    overlay: false,  },};

```
npm run serve
```

### Дополнительный пункт: Переключение языков

`Vue TUIKit` поставляется с языковыми пакетами по умолчанию **Упрощенный китайский, английский**, которые служат языком отображения интерфейса.

Вы можете переключать языки следующим образом. Для дополнительных методов см. [Интернационализация](https://trtc.io/document/58652?platform=web&product=chat).

```
import { TUITranslateService } from "@tencentcloud/chat-uikit-engine";// изменить язык на китайскийTUITranslateService.changeLanguage("zh");// изменить язык на английскийTUITranslateService.changeLanguage("en");
```

### Шаг 6. Отправьте свое первое сообщение

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5b634712b4ec11ee9939525400461a83.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/27fca10ab4ec11eeb2a1525400170219.png)

### Шаг 7: Сделайте ваш первый звонок

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2518893ab50211ee9939525400461a83.png)

## Часто задаваемые вопросы

### Часто задаваемые вопросы о продукте и услуге

#### 1. Пакет возможности аудио/видео вызовов не активирован? Невозможно инициировать аудио/видео вызов?

Пожалуйста, нажмите [Audio/Video Call > Frequently Asked Questions](https://trtc.io/document/51024?platform=web&product=call), чтобы просмотреть решения.

#### 2. Что такое UserSig? Как создается UserSig?

UserSig — это пароль, с помощью которого вы можете войти и использовать услугу Chat. Это шифротекст, созданный путем шифрования информации, такой как userID.

Выдача UserSig достигается путем интеграции кода расчета UserSig в вашу серверную часть, при этом предоставляя интерфейс, предназначенный для вашего проекта. Когда требуется UserSig, ваш проект может запросить динамический UserSig на операционном сервере. Дополнительную информацию см. в разделе [Создание UserSig на серверной стороне](https://trtc.io/document/39074?product=consoleguide).

> **Осторожно:** Метод получения UserSig, описанный в этом документе, использует конфигурацию SECRETKEY в коде на стороне клиента. В этом процессе SECRETKEY особенно уязвим для декомпиляции и обратного инжиниринга. Если ваш SECRETKEY будет утечка, злоумышленники потенциально могут использовать ваш трафик Tencent Cloud. Следовательно, **эта техника подходит только для локальной работы и отладки функциональности**. Для правильного метода выдачи UserSig см. предыдущий текст.

### Часто задаваемые вопросы об ошибках подключения

#### 1. Ошибка во время выполнения: "TypeError: Cannot read properties of undefined (reading "getFriendList")"

Если при подключении в соответствии с описанными выше шагами возникают следующие ошибки, необходимо **удалить каталог node_modules в папке TUIKit** для обеспечения уникальности зависимостей TUIKit, предотвращая проблемы, вызванные несколькими копиями зависимостей.

![259937368-f7c85dfe-b4bd-4c73-88d9-3a9f0d7797f2.png (1186×550)](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ade11ffbb46211ee9939525400461a83.png)

#### 2. Как JS-проект интегрирует компонент TUIKit?

TUIKit исключительно поддерживает работу в среде TS. Вы можете обеспечить сосуществование существующего JS-кода в вашем проекте с TS-кодом в TUIKit путем постепенной конфигурации TypeScript.

vue-cli

vite

Выполните следующее в корневом каталоге вашего проекта, созданного с помощью скаффолда Vue CLI:

```
vue add typescript
```

Затем, пожалуйста, сделайте выборку в соответствии со следующими опциями конфигурации. Чтобы гарантировать, что мы можем поддерживать как существующий js-код, так и ts-код в TUIKit, крайне важно, чтобы вы строго придерживались пяти представленных ниже опций.

![260706614-5e2fc00b-ace5-4843-bef6-c0e234225b5d.png (1514×360)](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/adcb2b1bb46211eeb2a1525400170219.png)

**После завершения этих шагов пожалуйста перезапустите проект!**

Выполните следующую команду в корневом каталоге вашего проекта, созданного с помощью vite:

```
npm install -D typescript
```

#### 3. Ошибка во время выполнения: /chat-example/src/TUIKit/components/TUIChat/message-input/message-input-editor.vue .ts(8,23)TS1005: expected.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ade25c17b46211ee9fd6525400bb593a.png)

Вышеуказанное сообщение об ошибке появляется, потому что ваша установленная версия @vue/cli слишком низкая. **Вы должны убедиться, что ваша версия @vue/cli 5.0.0 или выше**. Метод обновления следующий:

```
npm install -g @vue/cli@5.0.8
```

#### 4. Ошибка во время выполнения: Failed to resolve loader: sass-loader

![260897345-1ba994d8-da51-4820-94e7-a7145b34750b.png (690×160)](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/adc33382b46211eeae9a525400c26da5.png)

Вышеуказанное сообщение об ошибке появляется, потому что окружение `sass` не установлено на вашем компьютере. Пожалуйста, выполните следующую команду для установки окружения `sass`:

```
npm i -D sass sass-loader@10.1.1
```

#### 5. Другие ошибки ESLint?

Если копирование chat-uikit-vue в каталог src привело к ошибке из-за несоответствия со стилем кода вашего локального проекта, вы можете игнорировать этот каталог компонентов. Это можно сделать, добавив файл .eslintignore в корневой каталог проекта:

```
# .eslintignoresrc/TUIKit
```

#### 6. Как отключить полноэкранное оверлей-сообщение об ошибке webpack в режиме dev в vue/cli?

Вы можете отключить это в файле vue.config.js в корневом каталоге вашего проекта:

webpack4

webpack3

```
module.exports = defineConfig({  ...  devServer: {    client: {      overlay: false,    },  },});
```

```
module.exports = {  ...  devServer: {    overlay: false,  },};
```

#### 7. Что делать при столкновении с 'Component name "XXXX" should always be multi-word'?

- Версия ESLint, используемая в Chat TUIKit web, — v6.7.2, которая не строго проверяет формат camelCase для имен модулей.
- Если вы столкнулись с этой дилеммой, вы можете настроить следующее в файле .eslintrc.js:

```
  module.exports = {    ...    rules: {        ...        'vue/multi-word-component-names': 'warn',    },  };
```

#### 8. Что я должен делать, если столкнусь с ERESOLVE unable to resolve dependency tree?

Если при запуске npm install появляется ERESOLVE unable to resolve dependency tree, это указывает на конфликт при установке зависимостей. Для установки может быть использован следующий метод:

```
npm install --legacy-peer-deps
```

#### 9. Как можно решить сообщение об ошибке 'vue packages version mismatch', возникающее при выполнении?

```
// Если вы используете проект vue2.7, пожалуйста выполните в корневом каталоге вашего проектаnpm i vue@2.7.9 vue-template-compiler@2.7.9// Если у вас есть проект Vue2.6, пожалуйста выполните в корневом каталоге вашего проектаnpm i vue@2.6.14 vue-template-compiler@2.6.14
```

#### 10. Почему TypeScript выдает ошибку после npm run build в проекте Vite?

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ae16b784b46211ee9939525400461a83.png)

**Причина**: Это вызвано командой vue-tsc в "build": "vue-tsc && vite build" в скрипте package.json.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/adabee49b46211eeb2a1525400170219.png)

**Решение**: Просто удалите vue-tsc. "build": "vite build"

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/add243e1b46211ee9939525400461a83.png)

## Общение и обратная связь

Присоединитесь к [Telegram Technical Exchange Group](https://t.me/tencent_imsdk) или [WhatsApp communication group](https://chat.whatsapp.com/IVa11ZkVmKTEwSWsAzSyik) для получения поддержки от профессиональных инженеров и решения ваших проблем.

## Ссылки

#### Vue2 и Vue3 UIKit с похожими возможностями

- [chat-uikit-vue npm](https://www.npmjs.com/package/@tencentcloud/chat-uikit-vue)
- [Исходный код Vue2 Demo и выполняемый пример](https://github.com/TencentCloud/chat-uikit-vue/tree/main/Vue2/Demo)
- [Исходный код Vue3 Demo и выполняемый пример](https://github.com/TencentCloud/chat-uikit-vue/tree/main/Vue3/Demo)

#### Vue2 и Vue3 UIKit Logic Layer: Engine Related

- [chat-uikit-engine npm репозиторий](https://www.npmjs.com/package/@tencentcloud/chat-uikit-engine)
- [Документация API chat-uikit-engine](https://web.sdk.qcloud.com/im/doc/chat-engine/index.html)


---
*Источник: [https://trtc.io/document/58644](https://trtc.io/document/58644)*

---
*Источник (EN): [integration.md](./integration.md)*

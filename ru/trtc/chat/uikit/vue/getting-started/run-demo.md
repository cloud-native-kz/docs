# Запуск демонстрационного приложения

TUIKit — это библиотека компонентов пользовательского интерфейса на основе Tencent Cloud Chat SDK. Она предоставляет универсальные компоненты интерфейса, включая чаты, диалоги, цепочки связей, группы, аудио/видео звонки и другие функции. С помощью этих компонентов интерфейса вы можете быстро создать собственное встроенное общение в приложении.

При реализации функций пользовательского интерфейса компоненты в TUIKit будут вызывать соответствующие интерфейсы Chat SDK для реализации логики, связанной с Chat, и обработки данных. Поэтому разработчикам нужно сосредоточиться только на своем собственном бизнесе или персонализированном расширении при использовании TUIKit.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/71eafaeab5f611eeb395525400461a83.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/78f28c36b5f611ee9d74525400c26da5.png)

## Предварительные требования

### Активация сервиса

1. Войдите в [Chat](https://console.trtc.io/) и создайте приложение. Нажмите `Create Application`, введите название приложения в диалоговое окно, выберите тип продукта и регион, затем нажмите `Create` для создания приложения.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ed981df2c06c11f09c26525400bf7822.png)

2. После создания вы сможете просмотреть `SDKAppID` и `SecretKey` вновь созданного приложения на странице обзора консоли. Эти две части информации требуются для последующего запуска демонстрационного приложения.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/edeb6a3cc06c11f0b4a7525400454e06.png)

3. Создайте 2-3 учетные записи для испытания функций общего чата (C2C) и группового чата.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ed59ce71c06c11f09c26525400bf7822.png)

4. Получите информацию userSig через [инструмент UserSign](https://console.trtc.io/usersig) для учетной записи входа.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ed228f5ec06c11f09c26525400bf7822.png)

### Требования к окружению

- Vue (полная совместимость с Vue 2 и Vue 3. При включении ниже выберите руководство по версии Vue, которое соответствует вашим потребностям)
- TypeScript (если ваш проект основан на JavaScript, перейдите к разделу [интеграция JS проекта](https://www.tencentcloud.com/document/product/1047/58645#84b6b984-9573-4dd4-a2f8-bcdcd2cabce2) для настройки прогрессивной поддержки TypeScript)
- Sass (sass-loader ≤ 10.1.1)
- node (node.js ≥ 16.0.0)
- npm (используйте версию, соответствующую используемой версии Node)

## Интеграция TUIKit

### Шаг 1: Создание проекта

TUIKit поддерживает использование vite или vue-cli для создания проекта, конфигурирование Vue 3/Vue 2 + TypeScript + sass. Ниже приведены несколько примеров настройки проекта:

vite

vue-cli

> **Примечание:** Vite требует [**Node.js**](https://nodejs.org/en/) версии 18+ или 20+. Когда ваш менеджер пакетов выдает предупреждение, пожалуйста, обновите версию Node. Для получения подробной информации обратитесь к [официальному сайту vite](https://cn.vitejs.dev/guide/).

Создайте проект, используя vite, и сконфигурируйте Vue + TypeScript, как показано на рисунке ниже.

```
npm create vite@5
```

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/715800d6c06d11f0b4a7525400454e06.png)

Затем перейдите в каталог проекта и установите зависимости проекта:

```
cd chat-examplenpm install
```

Установите зависимости окружения Sass, требуемые для TUIKit:

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

> **Примечание:** Если `tsconfig.json` использует `references`, правило должно быть написано в файле, на который указывается ссылка (например, `./tsconfig.app.json`), в противном случае запись в `tsconfig.json` не вступит в силу. Добавление правила должно быть выполнено в соответствующем файле `references`. Ниже приведен конкретный пример: Неправильный формат записиПравильный формат записиКогда файл tsconfig.json содержит существующую конфигурацию references, объявление следующих правил непосредственно в tsconfig.json недействительно.Когда файл tsconfig.json содержит существующую конфигурацию references, следующие правила должны быть объявлены в соответствующем внутреннем файле references. Ниже приведена конфигурация следующих правил в корневом файле каталога `tsconfig.app.json` в references.![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/714fcd63c06d11f0a6dd5254005ef0f7.png)
> ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/715bbce1c06d11f0b35752540099c741.png)

> **Примечание:** Обратите внимание: убедитесь, что ваша **версия @vue/cli составляет 5.0.0** или выше. Вы можете использовать следующий пример кода для обновления вашей версии @vue/cli до v5.0.8.

Создайте проект, используя vue-cli, и сконфигурируйте Vue 2/Vue 3 + TypeScript + sass.

Если вы не установили vue-cli или ваша версия vue-cli ниже 5.0.0, вы можете установить ее в терминал или cmd следующим способом:

```
npm install -g @vue/cli@5.0.8 sass@1.77.0 sass-loader@10.1.1
```

Создайте проект, используя vue-cli, и выберите выбранную конфигурацию на рисунке ниже.

```
vue create chat-example
```

Убедитесь в следующем выборе конфигурации:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/716192e6c06d11f0aa02525400e889b2.png)

После создания перейдите в каталог проекта:

```
cd chat-example
```

Если вы используете Vue 2, сконфигурируйте окружение в соответствии с вашей версией vue. Игнорируйте это для проектов vue 3.

vue 2.7

Vue 2.6 и ниже

```
npm i vue@2.7.9 vue-template-compiler@2.7.9
```

```
npm i @vue/composition-api unplugin-vue2-script-setup vue@2.6.14 vue-template-compiler@2.6.14Шаг 2: Загрузка компонента TUIKit
```

Загрузите компонент TUIKit через [npm](https://www.npmjs.com/package/@tencentcloud/chat-uikit-vue). Скопируйте компонент TUIKit в каталог src вашего проекта:

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

### Шаг 2: Импорт компонента TUIKit

На странице, которая должна быть отображена, импортируйте компонент TUIKit, и его можно использовать.

> **Примечание:** Чтобы уважать авторские права на дизайн эмодзи, в проектах Chat Demo/TUIKit не включены большие нарезки элементов эмодзи. Перед официальным коммерческим запуском замените его другими наборами эмодзи, разработанными или принадлежащими вам. По умолчанию **набор маленьких желтых смайликов принадлежит Tencent Cloud**, как показано ниже. Вы можете перейти на [Chat Pro Edition Plus и Enterprise Edition](https://console.trtc.io/subscription/buy/chat?packType=pro), чтобы попробовать его бесплатно.![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a45748f8c06d11f083155254001c06ec.png)

Например: реализуйте следующий код на странице App.vue для быстрого создания интерфейса чата (пример кода ниже поддерживает как Web, так и H5):

> **Примечание:** Следующий пример кода использует синтаксис setup. Если ваш проект больше не использует синтаксис setup, зарегистрируйте компонент согласно стандартному методу для Vue 3/Vue 2.

vue 3

vue 2.7

Vue 2.6 и ниже

```
<template>  <div id="app">    <TUIKit :SDKAppID="0" userID="xxx" userSig="xxx" />    <TUICallKit class="callkit-container" :allowedMinimized="true" :allowedFullScreen="false" />  </div></template><script lang="ts" setup>import { TUIKit } from './TUIKit';import { TUICallKit } from '@trtc/calls-uikit-vue';</script><style lang="scss"></style>
```

Если это проект, созданный с помощью Vite, вы можете закомментировать стиль по умолчанию, который не используется в проекте. Вы можете удалить ненужный контент в зависимости от ситуации.

src/style.css

```
#app {  /* max-width: 1280px; */  margin: 0 auto;  /* padding: 2rem; */  text-align: center;}
```

```
<template>  <div id="app">    <TUIKit :SDKAppID="0" userID="xxx" userSig="xxx" />    <TUICallKit class="callkit-container" :allowedMinimized="true" :allowedFullScreen="false" />  </div></template><script lang="ts" setup>import { TUIKit } from './TUIKit';import { TUICallKit } from '@trtc/calls-uikit-vue2';</script><style lang="scss"></style>
```

Если это проект, созданный с помощью vite, вы можете закомментировать стиль по умолчанию в проекте. Вы можете удалить ненужный контент в зависимости от ситуации.

src/style.css

```
#app {  /* max-width: 1280px; */  margin: 0 auto;  /* padding: 2rem; */  text-align: center;}
```

```
<template>  <div id="app">    <TUIKit :SDKAppID="0" userID="xxx" userSig="xxx" />    <TUICallKit class="callkit-container" :allowedMinimized="true" :allowedFullScreen="false" />  </div></template><script lang="ts" setup>import { TUIKit } from './TUIKit';import { TUICallKit } from '@trtc/calls-uikit-vue2.6';</script><style lang="scss"></style>
```

1. Установите зависимости, связанные с composition-api и script setup, а также зависимости для vue 2.6.

```
npm i @vue/composition-api unplugin-vue2-script-setup vue@2.6.14 vue-template-compiler@2.6.14
```

2. Введите VueCompositionAPI в `main.ts/main.js`.

```
import VueCompositionAPI from "@vue/composition-api";Vue.use(VueCompositionAPI);
```

3. Добавьте следующее в `vue.config.js`. Если файл не существует, создайте его.

```
const ScriptSetup = require("unplugin-vue2-script-setup/webpack").default;module.exports = {  parallel: false, // disable thread-loader, which is not compactible with this plugin  configureWebpack: {    plugins: [      ScriptSetup({        /* options */      }),    ],  },  chainWebpack(config) {    // disable type check and let `vue-tsc` handles it    config.plugins.delete("fork-ts-checker");  },};
```

4. В конце файла `src/TUIKit/adapter-vue.ts` замените источник экспорта:

```
// исходная записьexport * from "vue";// замените напиши export * from "@vue/composition-api";
```

Если это проект, созданный с помощью Vite, вы можете закомментировать стиль по умолчанию в проекте. Вы можете удалить ненужный контент в зависимости от ситуации.

src/style.css

```
#app {  /* max-width: 1280px; */  margin: 0 auto;  /* padding: 2rem; */  text-align: center;}
```

### Шаг 3: Конфигурация информации аутентификации

Установите свойства `App.vue` в компоненте TUIKit: SDKAppID, userID, userSig.

> **Примечание:** UserSig — это пароль для входа пользователя в Chat, который по сути является зашифрованным шифротекстом UserID и другой информации. Метод выдачи UserSig интегрирует код расчета UserSig в ваш сервер и предоставляет API, ориентированный на проект. Когда требуется UserSig, ваш проект инициирует запрос к бизнес-серверу для получения динамического UserSig. Пример кода в этом документе использует метод получения UserSig путем конфигурирования SECRETKEY в коде на стороне клиента. При таком методе SECRETKEY можно легко декомпилировать и провести обратное проектирование. Если ваш ключ будет скомпрометирован, злоумышленники смогут неправомерно использовать ваш трафик Tencent Cloud. **Поэтому этот метод подходит только для локальной отладки функций.** Для получения дополнительной информации см. [генерирование UserSig на сервере](https://www.tencentcloud.com/document/product/1047/34385).

```
<TUIKit  :SDKAppID="0" // number  userID="xxx"  // string  userSig="xxx" // string/>
```

### Шаг 4: Построение и запуск демонстрационного приложения

Выполните следующую команду для запуска проекта:

vite

vue-cli

```
npm run dev
```

> **Примечание:** Поскольку vue-cli по умолчанию включает глобальное сообщение об ошибке оверлея, для лучшего опыта **рекомендуется отключить глобальное сообщение об ошибке оверлея в vue.config.js или других файлах конфигурации webpack в вашем проекте**.Webpack 4 и вышеWebpack 3module.exports = defineConfig({  ...  // Добавьте новый код конфигурации для отключения overlay  devServer: {    client: {      overlay: false,    },  },});module.exports = {  ...  // Добавьте новый код конфигурации для отключения overlay  devServer: {    overlay: false,  },};

```
npm run serve
```

## Опробование базовых функций

### Отправка вашего первого сообщения

1. После запуска проекта нажмите **Инициировать личный чат** в верхнем левом углу.
2. Введите **Инициировать личный чат** во всплывающее окно. В поле поиска введите userID, созданный в разделе "**Активация сервиса**", затем нажмите **Завершить** после выбора.
3. Введите сообщение в поле ввода и нажмите **Отправить**.

Пример шагов отправки вашего первого сообщения в Web:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/33e21aaac06e11f0a0935254007c27c5.png)

Шаги H5 к "отправке вашего первого сообщения":

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/33eddfd4c06e11f09c26525400bf7822.png)

### Совершение вашего первого телефонного звонка

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/33d9a963c06e11f0b4a7525400454e06.png)

### Дополнительно: переключение языка

Web & H5 `Vue TUIKit` поставляется с встроенными языковыми пакетами **Упрощенный китайский, английский** в качестве языков отображения интерфейса.

Вы можете переключать язык следующими способами. Для получения дополнительных методов переключения см. [интернационализированный язык интерфейса](https://www.tencentcloud.com/document/product/1047/58652).

```
import { TUITranslateService } from "@tencentcloud/chat-uikit-engine";// переключить язык на китайскийTUITranslateService.changeLanguage("zh");// переключить язык на английскийTUITranslateService.changeLanguage("en");
```

## Часто задаваемые вопросы

### Часто задаваемые вопросы о продукте и услуге

#### 1. Пакет функций аудио/видео звонков не активирован? Не удается инициировать аудио/видео звонок?

Пожалуйста, нажмите [Аудио/видео звонки > Часто задаваемые вопросы](https://www.tencentcloud.com/document/product/647/53565) для просмотра решений.

#### 2. Что такое UserSig? Как создается UserSig?

UserSig — это пароль, с помощью которого вы можете войти для использования сервиса IM. Это шифротекст, созданный путем шифрования информации, такой как userID.

Выдача UserSig осуществляется путем интеграции кода расчета UserSig в ваш серверный код, при этом предоставляя интерфейс, разработанный для вашего проекта. Когда требуется UserSig, ваш проект может запросить операционный сервер для получения динамического UserSig. Для получения дополнительной информации см. [Генерирование UserSig на сервере](https://www.tencentcloud.com/en/document/product/1047/34385).

> **Осторожно** Метод получения UserSig, продемонстрированный в этом документе, использует конфигурирование SECRETKEY внутри кода на стороне клиента. В этой процедуре SECRETKEY явно подвержен декомпиляции и обратному проектированию. Если ваш SECRETKEY будет скомпрометирован, злоумышленники могут потенциально использовать ваш трафик Tencent Cloud. Поэтому **эта техника подходит только для локальной работы и отладки функций**. Для правильного метода выдачи UserSig см. предыдущий текст.

### Часто задаваемые вопросы об ошибках соединения

#### Ошибка во время выполнения: "TypeError: Cannot read properties of undefined (reading "getFriendList")"

Если приведенные выше ошибки возникают во время выполнения после подключения в соответствии с изложенными выше шагами, необходимо **удалить каталог node_modules в папке TUIKit** для обеспечения уникальности зависимостей TUIKit, предотвращая проблемы, вызванные несколькими копиями зависимостей.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ade11ffbb46211ee9939525400461a83.png)

#### Как проект JS интегрирует компонент TUIKit?

TUIKit эксклюзивно поддерживает работу в среде TS. Вы можете включить сосуществование существующего кода JS в вашем проекте с кодом TS в TUIKit путем прогрессивной конфигурации TypeScript.

vue-cli

vite

Пожалуйста, выполните следующее в корневом каталоге вашего инженерного проекта, созданного при помощи леса Vue CLI:

```
vue add typescript
```

Впоследствии, пожалуйста, сделайте выборы в соответствии со следующими опциями конфигурации. Чтобы обеспечить, что мы можем поддерживать как существующий js код, так и ts код в TUIKit, необходимо строго придерживаться пяти приведенных ниже опций.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/adcb2b1bb46211eeb2a1525400170219.png)

**После выполнения этих шагов, пожалуйста, перезапустите проект!**

Пожалуйста, выполните следующую команду в корневом каталоге вашего проекта, созданного с помощью vite:

```
npm install -D typescript
```

#### Сообщено об ошибке во время выполнения: /chat-example/src/TUIKit/components/TUIChat/message-input/message-input-editor.vue .ts(8,23)TS1005: expected.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ade25c17b46211ee9fd6525400bb593a.png)

Приведенное выше сообщение об ошибке появляется потому, что ваша установленная версия @vue/cli слишком низкая. **Вы должны убедиться, что ваша версия @vue/cli составляет 5.0.0 или выше**. Метод обновления выглядит следующим образом:

```
npm install -g @vue/cli@5.0.8
```

#### Ошибка во время выполнения: Failed to resolve loader: sass-loader

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/adc33382b46211eeae9a525400c26da5.png)

Приведенное выше сообщение об ошибке появляется потому, что окружение `sass` не установлено на вашей машине, пожалуйста, выполните следующую команду для установки окружения `sass`:

```
npm i -D sass sass-loader@10.1.1
```

#### Другие ошибки ESLint?

Если копирование chat-uikit-vue в каталог src приводит к ошибке из-за несовместимости с стилем кода вашего локального проекта, вы можете игнорировать этот каталог компонентов. Это можно осуществить путем добавления файла .eslintignore в корневой каталог проекта:

```
# .eslintignoresrc/TUIKit
```

#### Как отключить полноэкранное сообщение об ошибке оверлея webpack в режиме разработки в vue/cli?

Вы можете отключить его в файле vue.config.js в корневом каталоге вашего проекта:

webpack 4

webpack 3

```
module.exports = defineConfig({  ...  devServer: {    client: {      overlay: false,    },  },});
```

```
module.exports = {  ...  devServer: {    overlay: false,  },};
```

#### Что делать при столкновении с ошибкой 'Component name "XXXX" should always be multi-word'?

- Версия ESLint, используемая в IM TUIKit web, составляет v6.7.2, которая не строго проверяет формат camelCase для имен модулей.
- Если вы столкнулись с этой дилеммой, вы можете сконфигурировать следующее в файле .eslintrc.js:

```
  module.exports = {    ...    rules: {        ...        'vue/multi-word-component-names': 'warn',    },  };
```

#### Что мне делать, если я столкнулся с ERESOLVE unable to resolve dependency tree?

Если ERESOLVE unable to resolve dependency tree появляется при запуске npm install, это указывает на конфликт при установке зависимостей. Можно применить следующий метод установки:

```
npm install --legacy-peer-deps
```

#### Как можно решить сообщение об ошибке 'vue packages version mismatch', которое возникает во время выполнения?

```
// Если вы используете проект vue 2.7, пожалуйста, выполните в корневом каталоге вашего проектаnpm i vue@2.7.9 vue-template-compiler@2.7.9// Если у вас есть проект Vue 2.6, пожалуйста, выполните в корневом каталоге вашего проектаnpm i vue@2.6.14 vue-template-compiler@2.6.14
```

#### Почему TypeScript выдает ошибку после npm run build в проекте Vite?

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ae16b784b46211ee9939525400461a83.png)

**Причина**: это вызвано командой vue-tsc в "build": "vue-tsc && vite build" в скрипте package.json.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/adabee49b46211eeb2a1525400170219.png)

**Решение**: Просто удалите vue-tsc. "build": "vite build"

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/add243e1b46211ee9939525400461a83.png)

## Свяжитесь с нами

Присоединитесь к [группе технических обсуждений Telegram](https://t.me/tencent_imsdk) или [группе обсуждений WhatsApp](https://chat.whatsapp.com/IVa11ZkVmKTEwSWsAzSyik), пользуйтесь поддержкой профессиональных инженеров и решайте ваши трудности.

## Документация

#### Связано с Vue 2 & Vue 3 UIKit:

- [chat-uikit-vue npm](https://www.npmjs.com/package/@tencentcloud/chat-uikit-vue)
- [исходный код демонстрационного приложения Vue 2 и пример выполнения](https://github.com/TencentCloud/chat-uikit-vue/tree/main/Vue2/Demo)
- [исходный код демонстрационного приложения Vue 3 и пример выполнения](https://github.com/TencentCloud/chat-uikit-vue/tree/main/Vue3/Demo)

#### Механизм Vue 2 & Vue 3 UIKit:

- [chat-uikit-engine npm](https://www.npmjs.com/package/@tencentcloud/chat-uikit-engine)
- [интерфейс chat-u

---
*Источник (EN): [run-demo.md](./run-demo.md)*

# Настройка пользовательского интерфейса

В этой статье подробно описано, как настроить пользовательский интерфейс TUIRoomkit. TUIRoomkit предлагает два способа настройки: первый — через простой API настройки пользовательского интерфейса, второй — путём замены существующих компонентов пользовательского интерфейса. Ниже подробно описан каждый способ.

## Способ 1: Тонкая настройка интерфейса

TUIRoomkit предоставляет серию [API](https://www.tencentcloud.com/document/product/647/54880#), которые упрощают настройку пользовательского интерфейса. В таблице ниже перечислены основные API и их функции:

| API | Описание |
| --- | --- |
| [setLanguage](https://www.tencentcloud.com/document/product/647/54880#51991a76-0777-4773-a2dd-91ce51b92b18) | Установить язык интерфейса. |
| [setTheme](https://www.tencentcloud.com/document/product/647/54880#5bb291c2-edb5-48b0-968a-db52ed2252ae) | Установить тему интерфейса. |
| [enableWatermark](https://www.tencentcloud.com/document/product/647/54880#daceee1b-175d-41a1-b495-d158fe01d63c) | Включить функцию текстового водяного знака в приложении. Подробнее см.: [Text Watermark](https://www.tencentcloud.com/document/product/647/60531#). |
| [enableVirtualBackground](https://www.tencentcloud.com/document/product/647/54880#ac620717-1b58-42ed-b8a3-589bf0ad545e) | Включить функцию виртуального фона в приложении. После вызова этой функции на интерфейсе отобразится кнопка функции виртуального фона. Подробнее см.: [Virtual Background](https://www.tencentcloud.com/document/product/647/60533#). |
| [disableTextMessaging](https://www.tencentcloud.com/document/product/647/54880#9ed81bb6-73a0-4b75-878e-22cc641b43bc) | Отключить функцию отправки текстовых сообщений в приложении. После вызова этой функции пользователи не смогут отправлять или получать текстовые сообщения. |
| [disableScreenSharing](https://www.tencentcloud.com/document/product/647/54880#833fce4f-6e77-45bf-bea0-33a618b540fb) | Отключить функцию совместного использования экрана в приложении. После вызова этой функции пользователи не смогут делиться своим экраном с другими. |
| [hideFeatureButton](https://www.tencentcloud.com/document/product/647/54880#49c62018-9bc4-4117-bf68-aa985b868890) | Скрыть определённые кнопки функций в приложении. После вызова этой функции с передачей соответствующего значения перечисления [FeatureButton](https://www.tencentcloud.com/document/product/647/54880#6f28a0a9-c315-400e-a73f-b1fbd0b039eb) соответствующая кнопка будет скрыта от пользовательского интерфейса. |

## Способ 2: Изменение исходного кода UIKit

Вы можете напрямую изменить предоставленный исходный код пользовательского интерфейса, чтобы настроить пользовательский интерфейс TUIRoomKit в соответствии с вашими требованиями.

### Шаг 1: Экспорт исходного кода UIKit

Vue3

Vue2

1. Выполните скрипт экспорта исходного кода. Путь копирования по умолчанию — `./src/components/TUIRoom`

```
  node ./node_modules/@tencentcloud/roomkit-web-vue3/scripts/eject.js
```

2. Следуя подсказкам скрипта, подтвердите, что вы хотите скопировать исходный код TUIRoomKit в каталог `./src/components/TUIRoom`. Введите «y», если вы хотите настроить каталог копирования, в противном случае введите «n».

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9c0479792c9e11ef918f52540005b090.png)

3. После экспорта исходного кода исходный код TUIRoomKit будет добавлен в указанный вами путь проекта. На этом этапе необходимо вручную изменить ссылку на компонент ConferenceMainView и объект conference с адреса пакета npm на адрес относительного пути исходного кода TUIRoom.

```
- import { ConferenceMainView, conference } from '@tencentcloud/roomkit-web-vue3';//  Замените путь ссылки на реальный путь исходного кода TUIRoomKit.+ import { ConferenceMainView, conference } from './src/components/TUIRoom/index.ts';
```

1. Выполните скрипт экспорта исходного кода. Путь копирования по умолчанию — `./src/components/TUIRoom`

```
  node ./node_modules/@tencentcloud/roomkit-web-vue2.7/scripts/eject.js
```

2. Следуя подсказкам скрипта, подтвердите, что вы хотите скопировать исходный код TUIRoomKit в каталог ./src/components/TUIRoom. Введите «y», если вы хотите настроить каталог копирования, в противном случае введите «n».

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9c0697892c9e11efb8c45254005a8b94.png)

3. После экспорта исходного кода исходный код TUIRoomKit будет добавлен в указанный вами путь проекта. На этом этапе необходимо вручную изменить ссылку на компонент ConferenceMainView и объект conference с адреса пакета npm на адрес относительного пути исходного кода TUIRoom.

```
- import { ConferenceMainView, conference } from '@tencentcloud/roomkit-web-vue2.7';// Замените путь ссылки на реальный путь исходного кода TUIRoomKit.+ import { ConferenceMainView, conference } from './src/components/TUIRoom/index.ts';
```

### Шаг 2: Настройка среды разработки исходного кода UIKIT

Конфигурация для Vue3 + Vite + TS

Конфигурация для Vue3 + Webpack + TS

Конфигурация для Vue2 + Webpack + TS

1. **Установка зависимостей среды разработки**

```
npm install typescript -S -D
```

2. **Регистрация Pinia**

TUIRoom использует Pinia для управления данными комнаты. Вам нужно зарегистрировать Pinia в файле точки входа проекта, который находится в файле src/main.ts.

```
// src/main.tsimport { createPinia } from 'pinia';const app = createApp(App);// register for Piniaapp.use(createPinia()); app.mount('#app');
```

3. **Настройка проверки esLint**

Если вы не хотите, чтобы правила esLint компонента TUIRoomKit конфликтовали с локальными правилами и вызывали ошибки во время выполнения, вы можете добавить игнорирование папки TUIRoom в `.eslintignore`.

```
// Пожалуйста, добавьте реальный путь к исходному коду TUIRoomsrc/components/TUIRoom
```

Если при сборке проекта возникают ошибки TypeScript, рекомендуется проверить файл `package.json` проекта. Удалите сегмент `vue-tsc` в соответствующей команде сборки, как показано ниже:

```
// package.json{    "scripts": {        // "build": "vue-tsc --noEmit --skipLibCheck && vite build",        "build": "vite build"    }}
```

4. На этом этапе вы можете запустить проект, чтобы увидеть эффект импорта исходного кода.

```
npm run dev
```

1. **Установка зависимостей среды разработки**

```
npm install typescript -S -D
```

2. **Регистрация Pinia**
TUIRoom использует Pinia для управления данными комнаты. Вам нужно зарегистрировать Pinia в файле точки входа проекта, который находится в файле src/main.ts.

```
// src/main.tsimport { createPinia } from 'pinia';const app = createApp(App);// register for Piniaapp.use(createPinia()); app.mount('#app');
```

3. **Настройка проверки esLint**

Если вы не хотите, чтобы правила esLint компонента TUIRoomKit конфликтовали с локальными правилами и вызывали ошибки во время выполнения, вы можете добавить игнорирование папки TUIRoom в `.eslintignore`.

```
// Пожалуйста, добавьте реальный путь к исходному коду TUIRoomsrc/components/TUIRoom
```

4. На этом этапе вы можете запустить проект, чтобы увидеть эффект импорта исходного кода.

```
npm run serve
```

> **Примечание:** Компонент TUIRoomKit требует установки vue2.7 в проекте vue2 и поддерживает среду typescript. Если ваш текущий проект находится в среде vue2.6 + js, выполните следующие шаги для обновления до среды vue2.7 + ts. Обновление с vue2.6 на vue2.7 — это плавное обновление, которое не влияет на существующий код. После настройки среды ts существующий код js не будет затронут. Смело выполняйте обновление.

1. **Обновление vue2 до версии v2.7+. Если версия vue в вашем проекте уже v2.7+, пропустите этот шаг.**

```
npm install vue@2 -S
```

2. **Настроить typescript для поддержки загрузки компонента TUIRoom.**

```
vue add typescript
```

Параметры для настройки среды разработки TS можно найти на изображении:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3d612fe52c9f11efa01d5254005235d8.png)

****

3. **Регистрация Pinia**

TUIRoom использует Pinia для управления данными комнаты. Вам нужно зарегистрировать Pinia в файле точки входа проекта, который находится в файле src/main.ts.

```
import { createPinia, PiniaVuePlugin } from 'pinia';Vue.use(PiniaVuePlugin);const pinia = createPinia();new Vue({  pinia,  render: h => h(App),}).$mount('#app');
```

4. **Настройка проверки esLint**

Если вы не хотите, чтобы правила esLint компонента TUIRoomKit конфликтовали с локальными правилами и вызывали ошибки во время выполнения, вы можете добавить игнорирование папки TUIRoom в `.eslintignore`.

```
// Пожалуйста, добавьте реальный путь к исходному коду TUIRoomsrc/components/TUIRoom
```

5. На этом этапе вы можете запустить проект, чтобы увидеть эффект импорта исходного кода.

```
npm run serve
```

### Шаг 3: Изменение исходного кода согласно требованиям

#### 1. Замена значков

Вы можете напрямую изменять компоненты значков в папке `/TUIRoom/components/common/icons`, чтобы обеспечить согласованность цвета и стиля значков во всём приложении. Сохраняйте имена файлов значков неизменными при замене.

#### 2. Регулировка макета пользовательского интерфейса

Вы можете отрегулировать макет пользовательского интерфейса конференции видео между несколькими людьми, изменяя различные компоненты в папке `/TUIRoom/components/`:

```
- components/        - Chat                Чат    - common              Компоненты общих значков    - ManageMember        Управление участниками    - RoomContent         Видео комнаты    - RoomFooter          Раздел Footer комнаты    - RoomHeader          Раздел Header комнаты    - RoomHome            Главная страница    - RoomInvite          Приглашение участников    - RoomLogin           Страница входа    - RoomMore            Больше    - RoomSetting         Параметры    - RoomSidebar         Компонент Drawer
```

## Способ 3: Реализация собственного интерфейса

Общая функциональность TUIRoomKit основана на TUIRoomEngine, SDK без пользовательского интерфейса. Вы можете полностью реализовать свой собственный пользовательский интерфейс на основе TUIRoomEngine. Для получения дополнительной информации см.:

- [Руководство интеграции TUIRoomEngine](https://www.tencentcloud.com/document/product/647/54845#)
- [Адрес интерфейса API TUIRoomEngine](https://www.tencentcloud.com/document/product/647/54878#)


---
*Источник: [https://trtc.io/document/54851](https://trtc.io/document/54851)*

---
*Источник (EN): [ui-customization.md](./ui-customization.md)*

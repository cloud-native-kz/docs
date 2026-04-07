# Список прямых трансляций

## Обзор

Этот документ содержит подробное введение в **страницу списка прямых трансляций** в демонстрационном приложении TUILiveKit. Вы можете напрямую интегрировать нашу предварительно разработанную страницу списка прямых трансляций в ваш существующий проект в соответствии с этим документом или настроить стиль страницы, макет и элементы функций в соответствии с вашими потребностями.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d86cf0b8986011f0b5725254001c06ec.png)

## Быстрое подключение

### Шаг 1: Настройка окружения и активация сервиса

Перед выполнением быстрого подключения необходимо обратиться к разделу [Подготовка](https://www.tencentcloud.com/document/product/647/66938) для выполнения требуемой конфигурации окружения и активации соответствующего сервиса.

### Шаг 2: Установка зависимостей

Вы можете выбрать любой из приведенных ниже методов для установки зависимостей:

npm

pnpm

yarn

```
npm install tuikit-atomicx-vue3 @tencentcloud/uikit-base-component-vue3 --save
```

```
pnpm add tuikit-atomicx-vue3 @tencentcloud/uikit-base-component-vue3
```

```
yarn add tuikit-atomicx-vue3 @tencentcloud/uikit-base-component-vue3
```

### Шаг 3: Интеграция страницы списка прямых трансляций

Создайте файл **live-list.vue** в вашем проекте. Вы можете скопировать приведенный ниже код непосредственно в свой проект для беспрепятственной интеграции со **страницей списка прямых трансляций**.

```
<template>  <UIKitProvider language="zh-CN">    <div class="container">      <header class="header">        <h1 class="title">Online Live Streaming</h1>      </header>      <main class="main">        <LiveList @live-room-click="handleLiveRoomClick" />      </main>    </div>  </UIKitProvider></template><script setup lang="ts">import { onMounted } from 'vue';import { LiveList, type LiveInfo, useLoginState } from 'tuikit-atomicx-vue3';import { UIKitProvider } from '@tencentcloud/uikit-base-component-vue3';const { login } = useLoginState();async function initLogin() {  try {    await login({      sdkAppId: 0,        // SDKAppID, see Step 1 to obtain      userId: '',         // UserID, see Step 1 to obtain      userSig: '',        // userSig, see Step 1 to obtain    });  } catch (error) {    console.error('login error:', error);  }}onMounted(async () => {  await initLogin();});</script><style>:global(*),:global(::after),:global(::before){box-sizing:border-box;margin:0}.container{display:flex;flex-direction:column;height:100vh;width:100vw;background:var(--bg-color-default)}.header{display:flex;align-items:center;flex-shrink:0}.title{margin:0;font-size:24px;font-weight:600;color:var(--text-color-primary);letter-spacing:-.5px}.main{flex:1;padding:24px;overflow-y:auto;min-height:0}</style>
```

### Шаг 4: Запуск проекта

Выполните команду для создания страницы списка прямых трансляций. Вы можете выбрать соответствующую комнату прямой трансляции для просмотра.

```
npm run dev
```

## Адаптация под ваши нужды

Как показано на диаграмме функций выше, мы также поддерживаем настройку интерфейса веб-страницы списка прямых трансляций в соответствии с требованиями проекта. Основные параметры настройки приведены в таблице ниже.

| **Категория** | **Функция** | **Описание** |
| --- | --- | --- |
| **Список комнат прямых трансляций** | Пользовательское отображение списка комнат прямых трансляций | **Поддерживается:****Отображение/скрытие текста информации о комнате прямой трансляции, настройка интерфейса****Пользовательское отображение фиксированного количества в строке/столбце комнаты прямой трансляции** |
| **Личная информация** | Пользовательское отображение личной информации | **Поддерживается:****Показать/скрыть личную информацию****Настройка интерфейса шрифта и цвета личной информации** |

## Переход к определенной комнате прямой трансляции

Для обработки логики перенаправления со списка прямых трансляций (или главной страницы) на комнату прямой трансляции необходимо настроить Vue Router. В директории `src` вашего проекта создайте новую папку `router` и создайте файл `index.ts`. Затем в вашем главном файле (например, **main.ts** или **index.ts**) импортируйте и используйте маршрутизатор. Смотрите [пример кода на GitHub](https://github.com/Tencent-RTC/TUILiveKit/blob/main/Web/web-vite-vue3/src/main.ts). Если вам нужен список прямых трансляций, см. документацию по [странице списка прямых трансляций](#).

```
// live-list.vue can be incrementally added to your code
```

### Следующие шаги

Поздравляем! Вы успешно интегрировали страницу списка прямых трансляций. Далее вы можете реализовать страницу запуска вещания, страницу просмотра аудиторией и другой контент. Пожалуйста, обратитесь к таблице ниже:

| **Функция** | **Описание** | **Ссылка на демонстрацию** |
| --- | --- | --- |
| **Вещание хостом** | Поддерживается весь процесс прямого вещания, включая подготовку перед вещанием и взаимодействие после вещания. | [Вещание хостом](https://www.tencentcloud.com/document/product/647/73741) |
| **Просмотр аудиторией** | Зрители могут входить в комнату вещателя для просмотра прямой трансляции, подключаться к микрофону, просматривать информацию о комнате прямой трансляции, просматривать онлайн-зрителей и отображать комментарии. | [Просмотр аудиторией](https://www.tencentcloud.com/document/product/647/73747) |

#### 

#### 

#### 

#### 

####


---
*Источник: [https://trtc.io/document/73760](https://trtc.io/document/73760)*

---
*Источник (EN): [live-stream-list.md](./live-stream-list.md)*

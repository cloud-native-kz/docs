# Панель управления ссылками

Этот документ содержит подробное введение в **Панель управления ссылками (CoGuestPanel)**. Вы можете использовать примеры кода в этом документе для беспрепятственной интеграции наших предварительно разработанных компонентов в ваш существующий проект, либо настроить стиль и макет в соответствии с вашими потребностями, следуя разделу настройки компонентов в документе.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/37463362991511f0961e52540099c741.png)

## Основные возможности

| **Название функции** | **Подробное описание** |
| --- | --- |
| **Переключение вкладок** | Интерфейс предлагает две вкладки, позволяя пользователям быстро переключаться между модулями функций запроса подключения микрофона и управления подключением микрофона. Поддерживает запоминание статуса и уведомления о сообщениях. |
| **Список приложений** | Отображает все ожидающие запросы подключения микрофона в режиме реального времени, показывая аватары пользователей, ники и статус. Поддерживает сортировку по времени и функцию фильтрации. |
| **Операции ведущего** | Предоставляет множество кнопок одним щелчком мыши, поддерживает принятие приложения, отклонение приложения, отключение и другие функции с обратной связью о результатах операции в режиме реального времени. |

## Интеграция компонента

### Шаг 1: Настройка среды и активация сервиса

Перед выполнением быстрой интеграции вам необходимо обратиться к разделу [подготовка](https://www.tencentcloud.com/document/product/647/73731), чтобы выполнить соответствующую конфигурацию среды и активировать соответствующий сервис.

### Шаг 2: Установка зависимостей

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

### Шаг 3: Интеграция панели управления ссылками

Введите **Панель управления ссылками** в ваш проект и используйте её. Вы можете напрямую скопировать следующий пример кода в ваш проект, чтобы отобразить панель управления ссылками.

```
<template>  <UIKitProvider theme="light" language="en-US">    <div class="app">      <CoGuestPanel class="co-guest-panel" />    </div>  </UIKitProvider></template><script setup lang="ts">import { onMounted, ref } from 'vue';import { UIKitProvider } from '@tencentcloud/uikit-base-component-vue3';import { CoGuestPanel, useLoginState, useLiveState } from 'tuikit-atomicx-vue3';const { login, loginUserInfo } = useLoginState();const { joinLive } = useLiveState();async function initLogin() {  try {    await login({      sdkAppId: 0,        // SDKAppID, see Step 1 to get      userId: '',         // UserID, see Step 1 to get      userSig: '',        // userSig, see Step 1 to get    });  } catch (error) {    console.error('login error:', error);  }}onMounted(async () => {  await initLogin();  // enter live room by inputting corresponding liveId  await joinLive({    liveId: 'input corresponding live streaming room LiveId',       });});</script><style scoped>.app{width:100vw;height:100vh;display:flex;justify-content:center;align-items:center;padding:20px;box-sizing:border-box}.co-guest-panel{width:100%;max-width:500px;padding: 24px;height:600px;background:rgba(255,255,255,0.9);border-radius:12px;box-shadow:0 8px 32px rgba(0,0,0,0.1);overflow:hidden}</style>
```

## Настройка пользовательского стиля

Панель управления ссылками поддерживает настройку стиля через переменные CSS. Вы можете переопределить следующие переменные, чтобы отрегулировать внешний вид компонента. После завершения **Шага 3** см. следующий пример, чтобы отрегулировать пользовательский интерфейс панели управления ссылками, или напрямую скопируйте пример кода в ваш компонент, чтобы получить эффект примера.

```
<template>   <CoGuestPanel class="co-guest-panel" /></template><style>.co-guest-panel{--text-color-primary:#2d3748;--text-color-secondary:#93a3bb;--text-color-link:#20c9e7;--bg-color-primary:#ffffff;--bg-color-hover:#d6e7f3;--stroke-color-primary:#8bb6ef;--stroke-color-secondary:#90c0f4;--shadow-light:0 2px 8px rgba(69,67,67,0.08);--shadow-medium:0 4px 16px rgba(93,87,87,0.12);--transition:all 0.3s ease;}.co-guest-panel .panel-content{background:var(--bg-color-primary);border-radius:16px;border:1px solid var(--stroke-color-primary);box-shadow:var(--shadow-medium);transition:var(--transition);overflow:hidden;}.co-guest-panel .panel-content:hover{box-shadow:0 8px 24px rgba(0,0,0,0.15);transform:translateY(-2px);border-color:var(--stroke-color-secondary);}.co-guest-panel .user-item{padding:16px;margin:8px 0;background:var(--bg-color-primary);border:1px solid var(--stroke-color-primary);border-radius:12px;transition:var(--transition);cursor:pointer;}.co-guest-panel .user-item:hover{background:var(--bg-color-hover);border-color:var(--text-color-link);box-shadow:var(--shadow-light);transform:translateY(-1px);}.co-guest-panel .user-item:active{transform:translateY(0);transition:all 0.15s ease;}.co-guest-panel .user-item.selected{background:rgba(102,126,234,0.08);border-color:var(--text-color-link);box-shadow:var(--shadow-light);}</style>
```

| **До изменения** | **После изменения** |
| --- | --- |
|  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e2fef49f991611f0b38f5254001c06ec.png) |  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1b99086e991711f0b38f5254001c06ec.png) |


---
*Источник: [https://trtc.io/document/74041](https://trtc.io/document/74041)*

---
*Источник (EN): [link-management-panel.md](./link-management-panel.md)*

# Панель конфигурации источника медиа

Этот документ содержит подробное введение в **Панель конфигурации источника медиа (LiveScenePanel)**. Вы можете ссылаться на примеры кода в этом документе для беспрепятственной интеграции наших предварительно разработанных компонентов в ваш существующий проект или настроить стиль и макет в соответствии с вашими потребностями, следуя разделу настройки компонента в документе.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3c146f8f991211f0aa4252540044a08e.png)

## Основные возможности

| **Категория функции** | **Конкретная возможность** |
| --- | --- |
| **Поддержка нескольких типов материалов** | Камера, общий доступ к экрану, изображение, видео, текст и несколько типов материалов, поддержка выбора устройства и конфигурации параметров. |
| **Интеллектуальный режим отображения** | Отображение полной панели при отсутствии материала и автоматическое переключение в компактный режим кнопки при наличии материала с адаптивной подстройкой макета. |
| **Операции управления материалами** | Полный набор функций управления материалами, включая добавление, редактирование, переименование, удаление и сортировку с поддержкой массовых операций. |
| **Конфигурация предпросмотра в реальном времени** | Всплывающее окно конфигурации камеры обеспечивает предпросмотр в реальном времени, поддерживает регулировку параметров и тестирование устройства. |
| **Обработка прав доступа и ошибок** | Автоматическая проверка разрешений, понятные сообщения об ошибках и механизм повторных попыток для гарантии пользовательского опыта. |

## Интеграция компонента

### Шаг 1: Конфигурирование окружения и активация сервиса

Перед выполнением быстрой интеграции необходимо ознакомиться с [подготовкой](https://www.tencentcloud.com/document/product/647/73731) для соответствия требуемой конфигурации окружения и активации соответствующего сервиса.

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

### Шаг 3: Интеграция **Панели конфигурации источника медиа**

Добавьте **Панель конфигурации источника медиа** в ваш проект и используйте её. Скопируйте следующий пример кода непосредственно в ваш проект для отображения панели конфигурации источника медиа.

```
<template>  <UIKitProvider theme="dark" language="en-US">    <div class="app-container">      <LiveScenePanel class="live-scene-panel" />    </div>  </UIKitProvider></template><script setup lang="ts">import { onMounted } from 'vue';import { UIKitProvider } from '@tencentcloud/uikit-base-component-vue3';import { LiveScenePanel, useLoginState } from 'tuikit-atomicx-vue3';const { login } = useLoginState();async function initLogin() {  try {    await login({      sdkAppId: 0,        // SDKAppID, see Step 1 to get it      userId: '',         // UserID, see Step 1 to get it      userSig: '',        // userSig, see Step 1 to get it    });  } catch (error) {    console.error('login error:', error);  }}onMounted(async () => {  await initLogin();});</script><style scoped>.app-container{width:100vw;height:100vh;display:flex;justify-content:center;align-items:center;padding:20px;box-sizing:border-box}.live-scene-panel{width:20%;height:80vh;background:rgba(0,0,0,0.8);border-radius:16px}</style>
```

## Настройка компонента

Панель конфигурации источника медиа предоставляет пользователям различные и многомерные API функций для пользовательской настройки, позволяя пользователям настраивать типы материалов, поведение операций, стилевые темы и т. д. После завершения **Шага 3** выше см. следующий пример для регулировки интерфейса панели конфигурации источника медиа или непосредственно скопируйте пример кода поэтапно в компонент для создания примера эффекта.

### Настройка стиля

Настройка внешнего вида компонента через имена CSS классов и переменные, поддерживая комплексную настройку цветов темы, стилей макета, эффектов анимации и многого другого.

```
<template>  <LiveScenePanel class="custom-live-scene-panel" /></template><style>.app-container{width:100vw;height:100vh;display:flex;justify-content:center;align-items:center;padding:20px;box-sizing:border-box}.custom-live-scene-panel{width:100%;max-width:300px;height:80vh;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);border:2px solid #4c63d2;border-radius:16px;padding:24px;box-shadow:0 8px 32px rgba(0,0,0,0.1);color:white}.custom-live-scene-panel .add-material-item{background-color:#147fcb!important;color:white;border:none;border-radius:0!important;padding:12px 24px;font-weight:600;transition:all 0.3s ease}.custom-live-scene-panel .materials-list{margin-top:20px;gap:16px;display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr))}.custom-live-scene-panel .material-item{background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.2);border-radius:12px;padding:16px;backdrop-filter:blur(10px);transition:all 0.3s ease}.custom-live-scene-panel .material-item:hover{background:rgba(255,255,255,0.2);transform:scale(1.02)}</style>
```

| **До изменения** |  | **После изменения** |  |
| --- | --- | --- | --- |
| **Интерфейс добавления источника медиа** | **Интерфейс настроек источника медиа** | **Интерфейс добавления источника медиа** | **Интерфейс настроек источника медиа** |
|  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ac5eab64991011f0a3b8525400e889b2.png) |  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d16d5660991011f0a207525400bf7822.png) |  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3f2a9ff2991011f0a3b8525400e889b2.png) |  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/62a92cae991011f08bb25254005ef0f7.png) |

### Прослушивание статуса и масштабирование

Используя Hooks управления состоянием, вы можете отслеживать изменения внутреннего состояния панели конфигурации источника медиа и реализовать адекватную обработку внешней бизнес-логики. Этот подход позволяет вам контролировать и реагировать на операции, такие как добавление, удаление и обновление материалов, без изменения внутреннего кода компонента, достигая тем самым синхронизации данных, статистики сервиса, подсказок пользователю и других расширенных функций.

```
<template>    <!-- status display -->    <div class="status-info">      <span>Number of materials: {{ materialCount }}</span>      <span>Last operation: {{ lastOperation }}</span>    </div>    <LiveScenePanel />    <LiveScenePanel />    <StreamMixer /></template><script setup lang="ts">import { ref, computed, watch } from 'vue';import { LiveScenePanel, useVideoMixerState, StreamMixer } from 'tuikit-atomicx-vue3';
```


---
*Источник: [https://trtc.io/document/74040](https://trtc.io/document/74040)*

---
*Источник (EN): [media-source-configuration-panel.md](./media-source-configuration-panel.md)*

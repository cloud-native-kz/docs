# Компонент для трансляции видео в прямом эфире

Этот документ содержит подробное введение в **компонент для трансляции видео в прямом эфире (LiveView)**. Вы можете ссылаться на примеры кода в этом документе для интеграции наших предварительно разработанных компонентов в ваш существующий проект или настроить стиль и макет в соответствии с вашими потребностями, следуя разделу о настройке компонента в документе.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7120df7bb00111f0bd1d5254001c06ec.png)

## Основные возможности

| **Категория функции** | **Конкретная возможность** |
| --- | --- |
| **Интеллектуальное переключение потока** | LiveView может автоматически переключать типы потоков на основе текущего статуса пользователя (зритель или ведущий). Режим зрителя: компонент воспроизводит видеопотоки с ультранизкой задержкой, обеспечивая плавный просмотр для миллионов зрителей и значительно снижая затраты на трафик. Режим подключения: компонент автоматически переключается на потоковую передачу TRTC, обеспечивая ультранизкую задержку на уровне миллисекунд для обеспечения реального, четкого взаимодействия между подключенными пользователями. |
| **Настраиваемый интерфейс** | Чтобы удовлетворить разнообразные бизнес-сценарии, LiveView предоставляет пользовательские слоты интерфейса, обеспечивая полный контроль над областью видеопотока пользователя при совместной трансляции. Вы можете переписать отображение интерфейса, гибко определить аватар пользователя, псевдоним, статус и другую информацию, а также легко создать уникальный визуальный опыт, соответствующий стилю вашего бренда. |

## Интеграция компонента

### Шаг 1: Настройка окружения и активация сервиса

Перед быстрой интеграцией вам необходимо обратиться к [подготовке](https://www.tencentcloud.com/document/product/647/73731), соответствовать соответствующей конфигурации окружения и активировать соответствующий сервис.

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

### Шаг 3: Присоединение к комнате трансляции и голосовой чат

Введите и используйте LiveView в вашем проекте. Скопируйте следующий пример кода непосредственно в ваш проект, чтобы присоединиться к соответствующей комнате прямой трансляции для совместной трансляции.

```
<template>  <UIKitProvider theme="dark" language="zh-CN">    <div class="app">      <LiveView />    </div>  </UIKitProvider></template><script setup lang="ts">import { onMounted } from 'vue';import { UIKitProvider } from '@tencentcloud/uikit-base-component-vue3';import { LiveView, useLoginState, useLiveState, useCoGuestState } from 'tuikit-atomicx-vue3';const { login } = useLoginState();const { joinLive } = useLiveState();const { sendCoGuestRequest } = useCoGuestState();async function initLogin() {  try {    await login({      sdkAppId: 0,        // SDKAppID, see Step 1 to get      userId: '',         // UserID, see Step 1 to get      userSig: '',        // userSig, see Step 1 to get    });  } catch (error) {    console.error('login error:', error);  }}onMounted(async () => {  await initLogin();                      // After the audience enters the live room  // LiveView starts VOD automatically with ultra-low latency  await joinLive({    liveId: 'existing live streaming room Id',     })  // The client can join the live room by calling the corresponding method and switch mic as needed.   // After the audience successfully goes on mic, LiveView autoplays TRTC streaming.  await sendCoGuestRequest();});</script><style>.app {width: 100vw; height: 100vh; display: flex; justify-content: center; align-items: center}</style>
```

## Настройка компонента

LiveView предоставляет гибкие слоты настройки компонента. Эти слоты поддерживают регулирование стиля и макета элементов, таких как аватары, псевдонимы и статус, в соответствии с вашими потребностями, а также позволяют настраивать интерфейс области видеопотока для совместной трансляции. Ниже приведены примеры использования слотов.

#### Слот компонента

| **Имя** | **Параметр** | **Описание** |
| --- | --- | --- |
| seatViewUI | seatInfo: SeatInfo | Отображение пользовательского интерфейса для пользовательского места |

```
// Example of using the seatViewUI slot<LiveView>  <CustomSeatViewUI #seatViewUI></CustomSeatViewUI></LiveView>
```

1. `SeatInfo` определяет базовую информацию и статус каждого места в комнате прямой трансляции:

| Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- |
| `index` | `number` | Обязательный | Номер индекса места, который начинает увеличиваться с 0 и используется для определения положения места в комнате. |
| `isLocked` | `boolean` | Обязательный | Статус блокировки места: `true` означает, что место заблокировано и другие пользователи не могут войти; `false` означает, что место открыто. |
| `userInfo` | `SeatUserInfo` | опциональный | Информация о пользователе, который в настоящее время занимает это место. Если место пустое, это `undefined`. |
| `region` | `RegionInfo` | опциональный | Область отображения места в видеоканве для многоканального макета видео |

```
interface SeatInfo {  index: number;           // Seat index  isLocked: boolean;       // Whether the seat is locked  userInfo?: SeatUserInfo; // User info on the seat (optional)  region?: RegionInfo;     // Region info of the seat in the canvas (optional)}
```

2. `SeatUserInfo` определяет детали пользователя каждого места в комнате прямой трансляции:

| Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- |
| `roomId` | `string` | Обязательный | Уникальный идентификатор текущей комнаты прямой трансляции, используется для различения различных комнат прямой трансляции |
| `userId` | `string` | Обязательный | Уникальный идентификатор пользователя, должен быть уникален во всей системе |
| `userName` | `string` | Обязательный | Имя, отображаемое для пользователей в трансляциях, поддерживает китайские и английские символы. |
| `avatarUrl` | `string` | Обязательный | Полный URL-адрес фотографии профиля пользователя, поддерживающий протокол HTTPS |
| `microphoneStatus` | `DeviceStatus` | Обязательный | Статус микрофона |
| `microphoneStatusReason` | `DeviceStatusReason` | Обязательный | Причина изменения статуса микрофона, чтобы различать инициативу пользователя и операцию администратора |
| `cameraStatus` | `DeviceStatus` | Обязательный | Статус камеры |
| `cameraStatusReason` | `DeviceStatusReason` | Обязательный | Причина изменения статуса камеры, чтобы различать инициативу пользователя и операцию администратора |

```
interface SeatUserInfo {  roomId: string;                    // Live streaming room ID  userId: string;                    // Unique user ID  userName: string;                  // User Display Name  avatarUrl: string;                 // User Avatar URL  microphoneStatus: DeviceStatus;    // Microphone Status  allowOpenMicrophone: boolean;      // Whether to allow turning on microphone  cameraStatus: DeviceStatus;        // Camera Status  allowOpenCamera: boolean;          // Whether to allow turning on camera}export type SeatUserInfo = {  liveId: string;                                // Live streaming room ID  userId: string;                                // Unique user ID  userName: string;                              // User Display Name  avatarUrl: string;                             // User Avatar URL  microphoneStatus: DeviceStatus;                // Microphone Status  microphoneStatusReason: DeviceStatusReason;    // Reason for the modification  cameraStatus: DeviceStatus;                    // Camera Status  cameraStatusReason: DeviceStatusReason;        // Reason for the modification}
```

3. `RegionInfo` определяет область отображения и информацию об иерархии места в видеоканве:

| Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- |
| `x` | `number` | Обязательный | X-координата верхнего левого угла области относительно канвы (значение в пикселях) |
| `y` | `number` | Обязательный | Y-координата верхнего левого угла области относительно канвы (значение в пикселях) |
| `w` | `number` | Обязательный | Ширина области (значение в пикселях), должна быть больше 0 |
| `h` | `number` | Обязательный | Высота области (значение в пикселях), должна быть больше 0 |
| `zOrder` | `number` | Обязательный | Z-порядок, чем больше значение, тем больше позиционирование в переднюю часть, для обработки приоритета отображения областей перекрытия |

```
interface RegionInfo {  x: number;      // Top-left X-axis coordinate of the region  y: number;      // Top-left Y-axis coordinate of the region  w: number;      // Region width  h: number;      // Region height  zOrder: number; // Z-order}
```

#### Пример пользовательского слота

Чтобы помочь вам лучше испытать и понять возможности настройки слота seatViewUI компонента LiveView, мы предоставляем пример **сценария прямой трансляции и подключения микрофона** для вашей ссылки. Вы можете обратиться к вышеуказанному **Шагу 3** для постепенного копирования следующего кода в ваш проект для достижения эффекта аналогичного сценария.

```
<template>  <LiveView>    <template #seatViewUI="{ userInfo }">      <div         class="live-stream-view"        :class="{ 'is-anchor': isAnchor(userInfo), 'is-guest': !isAnchor(userInfo) }"      >        <!-- Video stream area -->        <div class="video-area">          <!-- The video stream will be rendered automatically -->        </div>                <!-- User information overlay -->        <div class="user-overlay">          <div class="user-badge" :class="{ 'anchor-badge': isAnchor(userInfo) }">            {{ isAnchor(userInfo) ? 'Anchor' : 'Audience' }}          </div>          <div class="user-name">{{ userInfo.userName }}</div>          <div class="device-status">            <span :class="['mic', userInfo.microphoneStatus]"></span>            <span :class="['camera', userInfo.cameraStatus]"></span>          </div>        </div>      </div>    </template>  </LiveView></template><script setup lang="ts">import { LiveView } from 'tuikit-atomicx-vue3';import type { SeatUserInfo } from 'tuikit-atomicx-vue3';// Determine whether it is an anchor (based on business logic)const isAnchor = (userInfo: SeatUserInfo) => {  // Here you can judge based on uid and role  return userInfo.userId.includes('anchor') || userInfo.userName.includes('Anchor');};</script><style scoped>.live-stream-view{position:relative;width:100%;height:100%;border-radius:8px;overflow:hidden}.live-stream-view.is-anchor{border:3px solid #ff6b35;box-shadow:0 0 20px rgba(255,107,53,.3)}.live-stream-view.is-guest{border:1px solid #ddd}.video-area{width:100%;height:100%;background:#000}.user-overlay{position:absolute;bottom:0;left:0;right:0;background:linear-gradient(transparent,rgba(0,0,0,.8));padding:10px;color:#fff}.user-badge{display:inline-block;padding:2px 8px;border-radius:10px;font-size:12px;margin-bottom:5px;background:#666}.anchor-badge{background:#ff6b35;color:#fff}.user-name{font-weight:700;margin-bottom:5px}.device-status span{margin-right:5px;opacity:.8}.device-status .camera.Off,.device-status .mic.Off{opacity:.3}</style>
```


---
*Источник: [https://trtc.io/document/74036](https://trtc.io/document/74036)*

---
*Источник (EN): [live-stream-video-component.md](./live-stream-video-component.md)*

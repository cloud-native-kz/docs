# Холст редактирования видеоисточника

Этот документ содержит подробное введение в **Холст редактирования видеоисточника (StreamMixer)**. Вы можете обратиться к примерам кода в этом документе для интеграции наших предварительно разработанных компонентов в ваш существующий проект или настроить стиль и макет в соответствии с вашими потребностями, следуя разделу персонализации компонентов в документе.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/245486a898f311f0a207525400bf7822.png)

## Основные возможности

| **Категория функций** | **Конкретные возможности** |
| --- | --- |
| **Предпросмотр в реальном времени** | Обеспечивает интерфейс редактирования WYSIWYG, позволяя вещающим интуитивно видеть эффект смешанного потока с поддержкой операций поворота, перемещения, масштабирования, зеркального отражения и изменения иерархии. |
| **Макеты на основе шаблонов** | Встроенные шаблоны макетов для трансляций поддерживают автоматическую адаптацию к различным сценариям с подключенными микрофонами, включая девятиячеистую сетку, формат 1v6, плавающее окно, что позволяет быстро переключаться между различными стилями трансляций. |
| **Управление статусом пользователей** | Интеллектуальное обнаружение присоединения и отключения пользователей при совместной трансляции, автоматическое изменение макета без необходимости ручного вмешательства, обеспечивающее плавную трансляцию и предоставляющее безупречный опыт для вещающих. |
| **Настраиваемый интерфейс** | Для удовлетворения различных бизнес-сценариев холст редактирования видеоисточника предоставляет слоты настройки компонента интерфейса, обеспечивая полный контроль над областями видеопотоков пользователей при совместной трансляции. Переписывайте отображение их интерфейса, гибко определяйте аватары, прозвища, статус и другую информацию, а также легко создавайте уникальный визуальный опыт, соответствующий стилю вашего интерфейса. |

## Интеграция компонента

### Шаг 1: Настройка среды и активация сервиса

Перед быстрой интеграцией вам необходимо обратиться к [Подготовке](https://www.tencentcloud.com/document/product/647/73731), удовлетворить связанные конфигурации среды и активировать соответствующий сервис.

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

### Шаг 3: Присоединение к комнате трансляции

Используйте и интегрируйте **Холст редактирования видеоисточника** в вашем проекте. Вы можете скопировать следующий пример кода непосредственно в ваш проект и добавить соответствующую комнату трансляции.

```
<template>  <UIKitProvider theme="dark" language="zh-CN">    <div class="app">      <LiveScenePanel class="live-scene-panel" />      <StreamMixer class="live-stream-mixer" />    </div>  </UIKitProvider></template><script setup lang="ts">import { onMounted } from 'vue';import { UIKitProvider } from '@tencentcloud/uikit-base-component-vue3';import { LiveScenePanel, StreamMixer, useLoginState, useLiveState, useCoGuestState } from 'tuikit-atomicx-vue3';const { login } = useLoginState();const { createLive } = useLiveState();const { sendCoGuestRequest } = useCoGuestState();async function initLogin() {  try {    await login({      sdkAppId: 0,        // SDKAppID, see Step 1 to get      userId: '',         // UserID, see Step 1 to get      userSig: '',        // userSig, see Step 1 to get    });  } catch (error) {    console.error('login error:', error);  }}onMounted(async () => {  await initLogin();                                                            // After the anchor creates a live streaming room  // StreamMixer automatically pushes the local composite video stream to the room  await createLive({                   liveId: `live_${loginUserInfo.value.userId}`,    liveName: `${loginUserInfo.value?.userName}'s live streaming room`,  });  // The client can join the live room by calling the method and switch on/off mic as needed.   // After the audience succeeds in going on mic, StreamMixer starts TRTC streaming automatically  await sendCoGuestRequest();     });</script><style>.app {width: 100vw; height: 100vh; display: flex; justify-content: center; align-items: center}</style>
```

```
npm run dev
```

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/671e3f42ad8e11f08bcc5254007c27c5.gif)

## Персонализация компонента

**Холст редактирования видеоисточника** предоставляет гибкий слот персонализации компонента, поддерживающий корректировку стиля и макета элементов, таких как аватар, прозвище и статус, в соответствии с вашими потребностями. Он также поддерживает персонализацию области видеопотока для интерфейса совместной трансляции. Ниже приведены примеры использования слотов.

### Слот компонента

| **Имя** | **Параметр** | **Описание** |
| --- | --- | --- |
| seatViewUI | seatInfo: SeatInfo | Пользовательский интерфейс отображения места |

```
// Пример использования слота seatViewUI<StreamMixer>  <CustomSeatViewUI #seatViewUI></CustomSeatViewUI></StreamMixer>
```

1. `SeatInfo` определяет основную информацию и статус каждого места в комнате трансляции:

| Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- |
| `index` | `number` | Обязательный | Номер индекса места начинается с 0, используется для определения позиции места в комнате. |
| `isLocked` | `boolean` | Обязательный | Статус блокировки места, `true` означает, что место заблокировано и другие пользователи не могут входить; `false` означает, что место открыто. |
| `userInfo` | `SeatUserInfo` | Необязательный | Информация пользователя текущего занимающего это место. Если место пусто, это `undefined`. |
| `region` | `RegionInfo` | Необязательный | Информация об области отображения места на холсте видео для макета видео с несколькими потоками. |

```
interface SeatInfo {  index: number;           // Индекс места  isLocked: boolean;       // Заблокировано ли место  userInfo?: SeatUserInfo; // Информация пользователя на месте (необязательно)  region?: RegionInfo;     // Информация области места на холсте (необязательно)}
```

2. `SeatUserInfo` определяет детали пользователя каждого места в комнате трансляции:

| Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- |
| `roomId` | `string` | Обязательный | Текущий уникальный идентификатор комнаты трансляции, используется для различения различных комнат трансляции |
| `userId` | `string` | Обязательный | Уникальный идентификатор пользователя, должен быть уникален во всей системе |
| `userName` | `string` | Обязательный | Имя, отображаемое для пользователей в трансляциях, поддерживает китайский, английский и другие символы. |
| `avatarUrl` | `string` | Обязательный | Полный URL фотографии профиля пользователя поддерживает протокол HTTPS. |
| `microphoneStatus` | `DeviceStatus` | Обязательный | Статус микрофона |
| `microphoneStatusReason` | `DeviceStatusReason` | Обязательный | Причины изменения статуса микрофона для различения между активной операцией пользователя и операцией администратора |
| `cameraStatus` | `DeviceStatus` | Обязательный | Статус камеры |
| `cameraStatusReason` | `DeviceStatusReason` | Обязательный | Причины изменения статуса камеры для различения между активной операцией пользователя и операцией администратора |

```
interface SeatUserInfo {  roomId: string;                    // ID комнаты трансляции  userId: string;                    // ID пользователя  userName: string;                  // Отображаемое имя пользователя  avatarUrl: string;                 // URL аватара пользователя  microphoneStatus: DeviceStatus;    // статус микрофона  allowOpenMicrophone: boolean;      // разрешено ли включать микрофон  cameraStatus: DeviceStatus;        // статус камеры  allowOpenCamera: boolean;          // разрешено ли включать камеру}export type SeatUserInfo = {  liveId: string;                                // ID комнаты трансляции  userId: string;                                // ID пользователя  userName: string;                              // Отображаемое имя пользователя  avatarUrl: string;                             // URL аватара пользователя  microphoneStatus: DeviceStatus;                // статус микрофона  microphoneStatusReason: DeviceStatusReason;    // причина изменения  cameraStatus: DeviceStatus;                    // статус камеры  cameraStatusReason: DeviceStatusReason;        // причина изменения}
```

3. `RegionInfo` определяет область отображения и информацию иерархии места на холсте видео:

| Параметр | Тип | Обязательный | Описание |
| --- | --- | --- | --- |
| `x` | `number` | Обязательный | X-координата верхнего левого угла области относительно холста (значение в пикселях) |
| `y` | `number` | Обязательный | Y-координата верхнего левого угла области относительно холста (значение в пикселях) |
| `w` | `number` | Обязательный | Ширина области (значение в пикселях), должна быть больше 0 |
| `h` | `number` | Обязательный | Высота области (значение в пикселях), должна быть больше 0 |
| `zOrder` | `number` | Обязательный | Z-порядок, чем больше значение, тем более расположено спереди для обработки приоритета отображения перекрытия |

```
interface RegionInfo {  x: number;      // X-координата верхнего левого угла области  y: number;      // Y-координата верхнего левого угла области  w: number;      // Ширина области  h: number;      // Высота области  zOrder: number; // Z-порядок}
```

### Пример пользовательского слота

Чтобы помочь вам лучше испытать и понять возможности персонализации слота seatViewUI в компоненте холста редактирования видеоисточника, мы предоставляем пример **сценария трансляции и микрофонного подключения** для вашей ссылки. Вы можете обратиться к **шагу 3** выше и поэтапно скопировать следующий код в ваш проект для достижения аналогичного эффекта.

```
<template>  <StreamMixer>    <template #seatViewUI="{ userInfo }">      <div         class="live-stream-view"        :class="{ 'is-anchor': isAnchor(userInfo), 'is-guest': !isAnchor(userInfo) }"      >        User information overlay        <div class="user-overlay">          <div class="user-badge" :class="{ 'anchor-badge': isAnchor(userInfo) }">            {{ isAnchor(userInfo) ? 'Anchor' : 'Audience' }}          </div>          <div class="user-name">{{ userInfo.userName }}</div>          <div class="device-status">            <span :class="['mic', userInfo.microphoneStatus]"></span>            <span :class="['camera', userInfo.cameraStatus]"></span>          </div>        </div>      </div>    </template>  </StreamMixer></template><script setup lang="ts">import { StreamMixer } from 'tuikit-atomicx-vue3';import type { SeatUserInfo } from 'tuikit-atomicx-vue3';// Determine whether it is an anchor (based on business logic)const isAnchor = (userInfo: SeatUserInfo) => {  // Here access can be judged based on uid and role  return userInfo.userId.includes('anchor') || userInfo.userName.includes('Anchor');};</script><style scoped>.live-stream-view{position:relative;width:100%;height:100%;border-radius:8px;overflow:hidden}.live-stream-view.is-anchor{border:3px solid #ff6b35;box-shadow:0 0 20px rgba(255,107,53,.3)}.live-stream-view.is-guest{border:1px solid #ddd}.video-area{width:100%;height:100%;background:#000}.user-overlay{position:absolute;bottom:0;left:0;right:0;background:linear-gradient(transparent,rgba(0,0,0,.8));padding:10px;color:#fff}.user-badge{display:inline-block;padding:2px 8px;border-radius:10px;font-size:12px;margin-bottom:5px;background:#666}.anchor-badge{background:#ff6b35;color:#fff}.user-name{font-weight:700;margin-bottom:5px}.device-status span{margin-right:5px;opacity:.8}.device-status .camera.Off,.device-status .mic.Off{opacity:.3}</style>
```


---
*Источник: [https://trtc.io/document/74037](https://trtc.io/document/74037)*

---
*Источник (EN): [video-source-editing-canvas.md](./video-source-editing-canvas.md)*

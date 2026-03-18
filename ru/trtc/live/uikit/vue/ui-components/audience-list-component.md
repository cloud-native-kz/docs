# Компонент списка аудитории

Этот документ содержит подробное введение в **компонент списка аудитории (LiveAudienceList)**. Вы можете использовать примеры кода в этом документе для беспрепятственной интеграции в существующий проект или настроить стиль и макет в соответствии с вашими потребностями, следуя разделу кастомизации компонента в документе.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/254194d798f511f081465254007c27c5.png)

## Основные возможности

| **Категория функции** | **Конкретные возможности** |
| --- | --- |
| **Отображение аудитории в реальном времени** | Отображение списка онлайн-аудитории в прямой трансляции в реальном времени, поддержка отображения аватара и прозвища, предоставление четкого просмотра информации об аудитории, позволяя хостам интуитивно понять состав аудитории. |
| **Адаптивный дизайн** | Поддержка компонентом решений UI для настольных и мобильных устройств, автоматическая адаптация к различным размерам экранов устройств для обеспечения единообразного пользовательского опыта и удовлетворения потребностей многоплатформенной прямой трансляции. |
| **Настраиваемый пользовательский интерфейс** | Предоставление гибкого механизма слотов, поддержка кастомизации тегов аудитории, стиля фото профиля и других элементов, что позволяет вам настроить эффект отображения списка аудитории в соответствии с потребностями бизнеса и создать уникальный визуальный опыт. |

## Интеграция компонента

### Шаг 1: Настройка окружения и активация сервиса

Перед выполнением быстрой интеграции вам необходимо обратиться к [подготовке](https://www.tencentcloud.com/document/product/647/73731), выполнить требуемую конфигурацию окружения и активировать соответствующий сервис.

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

### Шаг 3: Интеграция компонента списка аудитории

Импортируйте и используйте **компонент списка аудитории** в вашем проекте. Вы можете скопировать следующий пример кода непосредственно для отображения списка аудитории прямой трансляции в вашем проекте.

```
<template>  <UIKitProvider theme="dark" language="zh-CN">    <div class="app">        <div class="live-audience-container">          <LiveAudienceList class="live-audience-list"/>      </div>    </div>  </UIKitProvider></template><script setup lang="ts">import { onMounted } from 'vue';import { UIKitProvider } from '@tencentcloud/uikit-base-component-vue3';import { LiveAudienceList, useLoginState, useLiveState } from 'tuikit-atomicx-vue3';const { login } = useLoginState();const { joinLive } = useLiveState();async function initLogin() {  try {    await login({      sdkAppId: 0,        // SDKAppID, see Step 1 to get      userId: '',         // UserID, see Step 1 to get      userSig: '',        // userSig, see Step 1 to get    });  } catch (error) {    console.error('login error:', error);  }}onMounted(async () => {  await initLogin();                      await joinLive({    liveId: 'input the corresponding live streaming room LiveId',     // enter live room  });});</script><style>.live-audience-container{display:flex;height:100%;width:300px;padding:20px}.live-audience-list{width:100%;height:100%}</style>
```

## Кастомизация компонента

**Компонент списка аудитории** предоставляет гибкие пользовательские слоты, поддерживающие регулировку стиля и макета тегов аудитории, уникальных идентификаторов и других элементов в соответствии с вашими потребностями. Ниже приведены примеры использования слотов.

### Слоты компонента

| **Название** | **Параметр** | **Описание** |
| --- | --- | --- |
| **customAudienceInfo** | **audience: AudienceInfo** | **Кастомизировать отображение пользовательского интерфейса информации об аудитории** |

```
// Example of using the customAudienceInfo slot<LiveAudienceList>   <CustomAudienceInfo #customAudienceInfo /></LiveAudienceList>
```

`AudienceInfo` определяет основную информацию и статус каждого члена аудитории в комнате прямой трансляции:

| **Параметр** | **Тип** | **Описание** |
| --- | --- | --- |
| `userId` | `string` | Уникальный идентификатор аудитории, который должен быть уникальным во всей системе. |
| `userName` | `string` | Имя, отображаемое для аудитории в прямой трансляции, поддерживает китайские и английские символы. Если пусто, отображается userId. |
| `avatarUrl` | `string` | Полный URL аватара аудитории, поддерживает протокол HTTPS. |
| `isMessageDisabled` | `boolean` | Отключена ли аудитория. true означает отключено, false означает нормальное говорение. |
| `joinTime` | `number` | Отметка времени входа аудитории в комнату прямой трансляции для сортировки и статистики |

```
interface AudienceInfo {  userId: string;              // Audience unique ID  userName?: string;           // Audience display name (optional)  avatarUrl?: string;          // Audience avatar URL (optional)  isMessageDisabled?: boolean; // Whether muted (optional)  joinTime?: number;           // Entry timestamp (optional)}
```

### Свойства компонента

| **Название атрибута** | **Тип** | **Значение по умолчанию** | **Описание** |
| --- | --- | --- | --- |
| `height` | `string` | **'500px'** | Высота компонента, поддерживает единицы CSS (px, %, vh) |
| `style` | `CSSProperties` | **{}** | Пользовательский объект стиля, используемый для переопределения стиля компонента по умолчанию |

#### Пример пользовательского слота

Чтобы помочь вам лучше использовать и понять возможности кастомизации слота **customAudienceInfo** **компонента списка аудитории**, мы предоставляем пример сценария **пользовательской личной информации** для вашей справки. Вы можете обратиться к описанному выше **шагу 3** и постепенно скопировать следующий код в ваш проект для достижения аналогичного эффекта.

```
<template>  <LiveAudienceList>    <template #customAudienceInfo="{ audience }">      <div class="custom-audience-info">        avatar        <img           :src="audience.avatarUrl || defaultAvatar"           :alt="audience.userName || audience.userId"          class="audience-avatar"        />                audience information        <div class="audience-details">          <span class="audience-name">{{ audience.userName || audience.userId }}</span>          <span class="join-time">{{ formatJoinTime(audience.joinTime) }}</span>        </div>                status indicator        <div v-if="audience.isMessageDisabled" class="muted-indicator">ð</div>      </div>    </template>  </LiveAudienceList></template><script setup lang="ts">import { LiveAudienceList } from 'tuikit-atomicx-vue3';const defaultAvatar = 'xxx'; // Input default avatar Urlconst formatJoinTime = (timestamp?: number) => {  // Format join time  if (!timestamp) return 'just now join';    const now = Date.now();  const diff = now - timestamp;  const minutes = Math.floor(diff / (1000 * 60));  const hours = Math.floor(diff / (1000 * 60 * 60));  const days = Math.floor(diff / (1000 * 60 * 60 * 24));    if (days > 0) return `${days} days ago join`;  if (hours > 0) return `${hours} hours ago join`;  if (minutes > 0) return `${minutes} minutes ago join`;  return 'just now join';};</script><style scoped>.custom-audience-info{display:flex;align-items:center;gap:12px;padding:8px;border-radius:8px;transition:background-color .2s ease}.custom-audience-info:hover{background-color:var(--uikit-color-gray-1)}.audience-avatar{width:40px;height:40px;border-radius:50%;object-fit:cover;border:2px solid var(--uikit-color-gray-3)}.audience-details{flex:1;display:flex;flex-direction:column;gap:4px}.audience-name{font-size:14px;font-weight:500;color:var(--text-color-primary);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.join-time{font-size:12px;color:var(--text-color-secondary)}.muted-indicator{font-size:16px;opacity:.6}</style>
```


---
*Источник: [https://trtc.io/document/74038](https://trtc.io/document/74038)*

---
*Источник (EN): [audience-list-component.md](./audience-list-component.md)*

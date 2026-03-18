# Компонент Barrage

Этот документ содержит подробное введение в **компонент barrage**, включая **компонент сообщений barrage (BarrageList)** и **компонент отправки сообщений (BarrageInput)**. Вы можете обратиться к примерам кода в этом документе для беспрепятственной интеграции наших предварительно разработанных компонентов в ваш существующий проект или настроить стиль и макет в соответствии с вашими потребностями, следуя разделу настройки компонентов в документе.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9de2371a98f611f0b38f5254001c06ec.png)

## Состав компонента

| **Название компонента** | **Подробное описание** |
| --- | --- |
| **Компонент сообщений Barrage (BarrageList)** | Компонент, отвечающий за отображение и управление потоками сообщений barrage в реальном времени, предоставляющий полное решение для отображения сообщений, включающее **отрисовку списка сообщений, временную агрегацию, взаимодействие пользователя и адаптивную адаптацию**. |
| **Компонент отправки сообщений (BarrageInput)** | Компонент ввода, предоставляющий функции расширенного редактирования текста и отправки сообщений с беспрепятственной интеграцией **селектора эмодзи, ограничения количества символов, управления состоянием и кроссплатформенной адаптации**, обеспечивающий пользователям плавный опыт ввода. |

## Интеграция компонента

### Шаг 1: Настройка окружения и активация сервиса

Перед выполнением быстрой интеграции необходимо обратиться к [подготовке](https://www.tencentcloud.com/document/product/647/73731), удовлетворить связанную конфигурацию окружения и активировать соответствующий сервис.

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

### Шаг 3: Интеграция компонента Barrage

Введите и используйте компонент barrage в вашем проекте. Вы можете скопировать следующий пример прямо, чтобы показать **полный компонент сообщений barrage комнаты прямой трансляции и компонент отправки сообщений** в вашем проекте.

```
<template>  <UIKitProvider theme="dark" language="en-US">    <div class="app">      <div class="chat-container">        <div class="chat-content">          <BarrageList class="barrage-list" />        </div>        <div class="chat-input">          <BarrageInput class="barrage-input" />        </div>      </div>    </div>  </UIKitProvider></template><script setup lang="ts">import { onMounted, ref } from 'vue';import { UIKitProvider } from '@tencentcloud/uikit-base-component-vue3';import { BarrageList, BarrageInput, useLoginState, useLiveState } from 'tuikit-atomicx-vue3';const { login, loginUserInfo } = useLoginState();const { joinLive } = useLiveState();async function initLogin() {  try {    await login({      sdkAppId: 0,        // SDKAppID, see Step 1 to get      userId: '',         // UserID, see Step 1 to get      userSig: '',        // userSig, see Step 1 to get    });  } catch (error) {    console.error('login error:', error);  }}onMounted(async () => {  await initLogin();  await joinLive({    liveId: 'input corresponding live streaming room LiveId',     // enter live room by inputting corresponding liveId  });});</script><style scoped>.app{width:100vw;height:100vh;display:flex;justify-content:center;align-items:center;padding:20px;box-sizing:border-box}.chat-container{width:100%;max-width:500px;height:600px;border-radius:16px;display:flex;flex-direction:column;overflow:hidden}.chat-content{flex:1;overflow:hidden}.barrage-list{width:100%;height:100%}.chat-input{background-color:var(--bg-color-dialog);padding:16px}.barrage-input{width:100%}</style>
```

## Настройка компонента

**Компонент сообщений Barrage** предоставляет пользователям различные и многомерные `Props` API для пользовательских требований, позволяя пользователям настраивать функции или пользовательский интерфейс. Содержание параметра показано в таблице ниже.

> **Примечание:** Примечание: для прямого ознакомления с деталями настройки компонента сообщений Barrage (BarrageList) быстро перейдите по следующей ссылке: [Настройка компонента сообщений Barrage](#872b809d-0251-49c3-8b4c-4c97b2801bdf); Примечание: для прямого ознакомления с деталями настройки компонента отправки сообщений (BarrageInput) быстро перейдите по следующей ссылке: [Настройка компонента отправки сообщений](#566ae5d7-6c69-4ba1-858a-bf839428b171);

### Настройка компонента сообщений Barrage (BarrageList)

#### **Props**

| **Название параметра** | **Тип параметра** | **Значение по умолчанию** | **Описание** |
| --- | --- | --- | --- |
| messageAggregationTime | Number | 300 | Максимальный временной интервал для группировки сообщений (в секундах). |
| filter | (message: IMessageModel) => boolean | - | Функции для фильтрации сообщений. |
| Message | Component | Message | Пользовательский компонент сообщений |
| MessageTimeDivider | Component | MessageTimeDivider | Пользовательский компонент сегментации времени сообщений. |
| LocalNoticeMessage | Component | LocalNoticeMessage | Пользовательский компонент локального уведомления. |
| containerStyle | CSSProperties | - | Пользовательский стиль контейнера списка сообщений. |
| itemStyle | CSSProperties | - | Пользовательский стиль элемента отдельного сообщения. |
| height | String | - | Высота компонента, поддерживает единицы CSS. |
| style | CSSProperties | - | Указать пользовательский стиль корневого элемента. |

Как указано в таблице выше, пользовательская часть Props компонента сообщений Barrage состоит из трех разделов: **свойства компонента, заменяемые подкомпоненты и пользовательские стили.** Конкретное содержание показано в таблице ниже.

| **Содержание** | **Параметр** |
| --- | --- |
| **Свойство компонента** | `filter`,`messageAggregationTime` |
| **Заменяемый подкомпонент** | `Message`,`MessageTimeDivider`,`LocalNoticeMessage` |
| **Пользовательский стиль** | `ContainerStyle`,`ItemStyle`,`height`,`style` |

#### Фильтрация сообщений

Установив параметр `filter`, вы можете гибко контролировать содержимое сообщений, отображаемых в компоненте сообщений barrage.

```
<BarrageList :filter="(message) => message.type === 'TIMTextElem'" />
```

#### Время агрегации сообщений

Установив параметр `messageAggregationTime`, вы можете контролировать временной интервал группировки.

```
<BarrageList :messageAggregationTime="300" />
```

#### Пользовательский стиль

Компонент сообщений Barrage предоставляет `containerStyle`, `itemStyle`, `пользовательский дочерний компонент` и т. д. для настройки стилей компонента.

1. Для настройки стиля контейнера списка сообщений вы можете передать объект стиля атрибуту `containerStyle`.

**Пример: пользовательское заполнение контейнера**

```
<BarrageList :containerStyle="{ padding: '0px' }" />
```

2. Для настройки стиля отдельного сообщения вы можете передать объект стиля атрибуту `itemStyle`.

**Пример: пользовательское расстояние элемента сообщения, граница и цвет пузыря сообщения**

```
<BarrageList :itemStyle="{ borderRadius: '10px', background: '#1C66e5', padding: '10px', boxSizing: 'border-box'}" />
```

3. Компонент сообщений barrage поддерживает пользовательские компоненты отображения сообщений, и вы можете полностью контролировать способ отрисовки.

**Пример: пользовательский компонент сообщений**

```
MyCustomMessage.vue
```

| **До изменения** | **После изменения** |  |  |
| --- | --- | --- | --- |
|  | **Пользовательское заполнение контейнера** | **Пользовательское расстояние элемента сообщения и граница** | **Пользовательский компонент сообщений** |
|  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bfe98f52991711f0961e52540099c741.png) |  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dc2f7512991711f0961e52540099c741.png) |  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ecaf4bfc991711f0a207525400bf7822.png) |  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/83c99885991b11f0961e52540099c741.png) |

### Настройка компонента отправки сообщений (BarrageInput)

#### **Props**

| **Название параметра** | **Тип** | **Значение по умолчанию** | **Описание** |
| --- | --- | --- | --- |
| containerClass | String | '' | Пользовательское имя класса CSS контейнера. |
| containerStyle | Record | {} | Встроенный стиль пользовательского контейнера. |
| width | String | - | Ширина компонента, поддерживает единицы CSS. |
| height | String | - | Высота компонента, поддерживает единицы CSS. |
| minHeight | String | '40px' | Минимальная высота компонента, поддерживает единицы CSS. |
| maxHeight | String | '140px' | Максимальная высота компонента, поддерживает единицы CSS. |
| placeholder | String | - | Текст заполнителя в поле ввода. |
| disabled | Boolean | false | Отключен ли поле ввода. |
| autoFocus | Boolean | true | Автоматически ли фокусироваться на поле ввода. |
| maxLength | Number | 80 | Максимальное ограничение количества символов для содержимого ввода. |

#### **События**

| **Название события** | **Параметр** | **Описание** |
| --- | --- | --- |
| focus | - | Срабатывает, когда поле ввода получает фокус. |
| blur | - | Срабатывает, когда поле ввода теряет фокус. |

Как указано в таблице выше, пользовательская часть Props компонента отправки сообщений состоит из трех разделов: **управление размером, ограничение ввода и пользовательские стили.** Конкретное содержание показано в таблице ниже.

| **Содержание** | **Параметр** |
| --- | --- |
| **Управление размером** | `width`,`height`,`minHeight`,`minWidth` |
| **Ограничение ввода** | `maxLength` |
| **Пользовательский стиль** | `ContainerStyle`,`ContainerClass` |

#### Управление размером

Установив параметры `width`, `height`, `minHeight`, `maxHeight`, вы можете гибко контролировать размер **BarrageInput**.

```
<BarrageInput width="400px" height="60px" minHeight="40px" maxHeight="120px" />
```

#### Ограничение ввода

Установив параметр `maxLength`, вы можете контролировать максимальное количество символов для содержимого ввода.

```
<BarrageInput :maxLength="100" />
```

#### Пользовательский стиль

Компонент отправки сообщений предоставляет атрибуты `containerStyle` и `containerClass` для настройки стиля компонента.

1. Для настройки стиля контейнера поля ввода вы можете передать объект стиля атрибуту `containerStyle`.

**Пример: пользовательский фон контейнера и скругленные углы границы**

```
<BarrageInput :containerStyle="{ backgroundColor: '#a8abb2', borderRadius: '0 0', boxShadow: '0 2px 8px rgba(0,0,0,0.1)'}" />
```

2. Для настройки имени класса контейнера поля ввода вы можете передать строку имени класса атрибуту `containerClass`.

**Пример: пользовательское имя класса контейнера**

```
<template>  <BarrageInput containerClass="my-custom-input-container" /></template><style>.my-custom-input-container {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);border: none;border-radius: 20px;padding: 8px 20px;}.my-custom-input-container:focus-within {box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.3);}</style>
```

| **До изменения** | **После изменения** |  |
| --- | --- | --- |
|  | **Пользовательский фон контейнера и скругленные углы границы** | **Пользовательское расстояние элемента сообщения и граница** |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9c1eca1e991b11f0961e52540099c741.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bd9f3926991b11f0a207525400bf7822.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e1d02d0f991b11f081465254007c27c5.png) |


---
*Источник: [https://trtc.io/document/74039](https://trtc.io/document/74039)*

---
*Источник (EN): [barrage-component.md](./barrage-component.md)*

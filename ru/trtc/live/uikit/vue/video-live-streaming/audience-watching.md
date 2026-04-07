# Просмотр трансляции

В этой статье подробно описана страница просмотра в демонстрации **TUILiveKit**. Вы можете напрямую обратиться к этому документу для интеграции разработанной нами страницы просмотра в ваш существующий проект или глубоко настроить стиль страницы, макет и функциональные элементы в соответствии с содержанием документа в соответствии с вашими потребностями.

### Обзор функций

| **Функциональная классификация** | **Конкретные возможности** |
| --- | --- |
| **Воспроизведение видеотрансляции** | HD и плавная трансляция в прямом эфире |
| **Взаимодействие через сообщения** | Чат в реальном времени |
| **Список зрителей** | Просмотр информации об онлайн-зрителях |
| **Подписка на транслятора** | Подпишитесь на своих любимых трансляторов одним щелчком |
| **Полноэкранное воспроизведение** | Погружающийся опыт просмотра |

## Демонстрация функций

Страница просмотра предоставляет поведение и стиль по умолчанию, но если стиль и поведение по умолчанию полностью не соответствуют вашим потребностям, вы также можете настроить пользовательский интерфейс. Номера на рисунке соответствуют категориям в списке конкретных функций. К ним в основном относятся отображение информации о трансляции, область воспроизведения видео, онлайн-аудитория, операции с аудио и видео, продолжительность трансляции, переключение разрешения экрана, функция полноэкранного режима, взаимодействие чата, список сообщений и т. д.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7a5f3ab9982c11f0af98525400454e06.png)

## Быстрый старт

### Шаг 1: Конфигурация окружения и активация сервиса

Перед использованием быстрого старта вам необходимо обратиться к требованиям конфигурации в разделе [Подготовка](https://www.tencentcloud.com/document/product/647/66938) и активировать соответствующие сервисы.

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

### Шаг 2: Доступ к странице просмотра

Создайте файл live-player.vue в вашем проекте и скопируйте следующий код для интеграции страницы просмотра в ваш проект.

```
<template>  <UIKitProvider language="zh-CN">    <div class="container">      <!-- Live core area -->      <section class="live">        <header class="header">          <IconArrowStrokeBack class="back-btn" size="20" />          <Avatar :src="currentLive?.liveOwner.avatarUrl" :size="32" class="avatar" />          <span class="user-name">{{ currentLive?.liveOwner.userName || currentLive?.liveOwner.userId }}</span>        </header>        <LiveCoreView class="player" />      </section>      <div class="sidebar">        <!-- Online viewers list -->        <section class="audience">          <header class="section-header">            <h3> online viewers <span>({{ audienceList.length }})</span></h3>          </header>          <LiveAudienceList class="list" />        </section>        <!-- Message List & Message List -->        <section class="barrage">          <header class="section-header">            <h3>MessageList</h3>          </header>          <BarrageList class="list" />          <BarrageInput class="input" height="48px" />        </section>      </div>    </div>  </UIKitProvider></template><script setup lang="ts">import { LiveAudienceList, BarrageList, BarrageInput, useLiveAudienceState, LiveCoreView, useLiveState, Avatar, useLoginState } from 'tuikit-atomicx-vue3';import { UIKitProvider, IconArrowStrokeBack } from '@tencentcloud/uikit-base-component-vue3';const { audienceList } = useLiveAudienceState();const { currentLive } = useLiveState();const { login } = useLoginState();async function initLogin() {  try {    await login({      sdkAppId: 0,        // SDKAppId, refer to step 1 to obtain      userId: '',         // UserID, refer to step 1 to obtain      userSig: '',        // userSig, refer to step 1 to obtain    });  } catch (error) {    console.error('Login Failed:', error);  }}onMounted(async () => {  await initLogin();});</script><style>:global(body){height:100vh;width:100vw;margin:0;padding:0;overflow:hidden;font-size:15px;line-height:1.6;text-rendering:optimizeLegibility;}:global(*),:global(*::before),:global(*::after){box-sizing:border-box;margin:0;}.container{display:grid;grid-template-columns:70% 30%;height:100vh;width:100vw;gap:16px;padding:16px;background:var(--bg-color-default);box-sizing:border-box;overflow:hidden;}.live{display:flex;flex-direction:column;background:var(--bg-color-operate);border-radius:12px;overflow:hidden;box-shadow:0 2px 8px var(--shadow-color);}.header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--stroke-color-primary);}.back-btn{cursor:pointer;color:var(--text-color-tertiary);transition:color 0.2s;}.back-btn:hover{color:var(--text-color-link-hover);}.avatar{border:1px solid var(--uikit-color-white-7);}.user-name{color:var(--text-color-primary);font-weight:500;}.player{flex:1;background:var(--uikit-color-black-1);}.sidebar{display:flex;flex-direction:column;gap:16px;height:100%;overflow:hidden;}.audience{display:flex;flex-direction:column;background:var(--bg-color-operate);border-radius:12px;overflow:hidden;box-shadow:0 2px 8px var(--shadow-color);flex:1;min-height:0;}.barrage{display:flex;flex-direction:column;background:var(--bg-color-operate);border-radius:12px;overflow:hidden;box-shadow:0 2px 8px var(--shadow-color);flex:1;min-height:0;}.section-header{padding:16px;border-bottom:1px solid var(--stroke-color-primary);background:var(--bg-color-operate);}.section-header h3{margin:0;font-size:16px;font-weight:600;color:var(--text-color-primary);}.section-header span{font-weight:400;color:var(--text-color-secondary);font-size:14px;}.list{flex:1;min-height:0;overflow-y:auto;}.input{border-top:1px solid var(--stroke-color-primary);flex-shrink:0;height:48px;}@media (max-width:1200px){.container{grid-template-columns:1fr;grid-template-rows:60% 20% 20%;gap:12px;}.sidebar{gap:12px;}.audience,.barrage{min-height:200px;}}@media (max-width:768px){.container{padding:8px;gap:8px;grid-template-rows:50% 25% 25%;}.header,.section-header{padding:12px;}.sidebar{gap:8px;}}</style>
```

### Шаг 3: Запуск проекта

```
npm run dev
```

## Настраиваемость

Как показано на функциональной диаграмме выше, мы также поддерживаем настройку пользовательского интерфейса страницы просмотра в соответствии с потребностями вашего проекта. В следующей таблице перечислены основные настраиваемые функции.

| **Категория** | **Функция** | **Описание** |
| --- | --- | --- |
| **Отображение информации о трансляции** | Настройте отображение области информации на странице просмотра | **Поддерживается:****Показать/скрыть логотип, заменить его на нужный логотип****Настройка пользовательского интерфейса, показать/скрыть кнопку подписки и заменить её на нужный стиль кнопки** |
| **Онлайн-зрители** | Настройте отображение информации об аудитории | **Поддерживается:****Показать/скрыть уровень аудитории****Настройка шрифта и цвета информации об аудитории в пользовательском интерфейсе****Замена стиля значка на нужный стиль** |
| **Список сообщений** | Настройка отображения области сообщений чата | **Поддерживается:****Показать/скрыть область ввода чата****Поддержка настройки пользовательского интерфейса для стиля чат-пузырьков, уровня аудитории и т. д.** |

## Воспроизведение прямой трансляции

#### Способ 1: Воспроизведение путём указания LiveId

Если вам нужно указать LiveId для воспроизведения, вам нужно добавить следующий код на основе кода в [шаг 3](#c1b852bc-da02-4c9f-bb11-2a63582ce978) раздела быстрого старта выше. Метод ссылки выглядит следующим образом:

```
live-player.vue
```

#### Способ 2: Конфигурация маршрутизации

Из-за логики, связанной с перенаправлением со списка трансляций (или домашней страницы) в комнату трансляции, вам потребуется настроить Vue Router. Создайте новую папку router в каталоге src проекта и создайте файл index.ts. Затем импортируйте и используйте маршрутизатор в своём основном файле (например, main.ts или index.ts). Дополнительную информацию см. в [примерах кода GitHub](https://github.com/Tencent-RTC/TUILiveKit/blob/main/Web/web-vite-vue3/src/main.ts). Список трансляций см. в документации по списку трансляций.

```
src/router/index.ts
```

### Следующие шаги

Поздравляем! Вы успешно интегрировали страницу просмотра. Далее вы можете реализовать содержание, такое как страница запуска трансляции и страница списка трансляций. Пожалуйста, обратитесь к таблице ниже:

| **Функция** | **Описание** | **Руководство по интеграции** |
| --- | --- | --- |
| **Трансляция от хоста** | Полный рабочий процесс для хоста по запуску потока, включая подготовку перед потоком и различные взаимодействия во время потока. | [Трансляция от хоста](https://www.tencentcloud.com/document/product/647/73741) |
| **Список трансляций** | Отображение интерфейса и функций списка трансляций, включая функцию отображения списка трансляций и информации о комнате | [Список трансляций](https://www.tencentcloud.com/document/product/647/73760) |


---
*Источник: [https://trtc.io/document/73747](https://trtc.io/document/73747)*

---
*Источник (EN): [audience-watching.md](./audience-watching.md)*

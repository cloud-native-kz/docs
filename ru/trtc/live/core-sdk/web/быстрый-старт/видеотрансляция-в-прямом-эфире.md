# Видеотрансляция в прямом эфире

Этот документ поможет вам использовать основной компонент `LiveView` SDK `AtomicXCore` для быстрого создания базового веб-приложения для прямой трансляции с возможностями трансляции хоста и просмотра аудиторией.

## Основные функции

`LiveView` — это основной компонент отображения видео, специально разработанный для сценариев прямой трансляции. Он обеспечивает основу для создания интерфейсов прямых трансляций, абстрагируя все базовые технологии потоковой передачи, включая публикацию и воспроизведение потоков, совместное ведение и рендеринг аудио/видео. Рассматривайте `LiveView` как «холст» для вашего прямого видео, позволяя вам сосредоточиться на разработке вашего пользовательского интерфейса и интерактивных функций. Следующая диаграмма иерархии представлений иллюстрирует роль и место `LiveView` в типичном интерфейсе прямой трансляции:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5eacce42d18211f0b1675254001c06ec.png)

## Пример проекта

Ознакомьтесь с нашим компонентом [LiveView](https://github.com/Tencent-RTC/TUIKit_Vue3/blob/main/packages/tuikit-atomicx-vue3/src/components/LiveView/index.vue) на GitHub для полного примера реализации.

## Подготовка

### Шаг 1: Активация сервиса

См. [Activate Service](https://www.tencentcloud.com/document/product/647/60033) для получения пробной или платной версии SDK.

> **Примечание:** `AtomicXCore SDK` разработан для проектов Vue 3. Убедитесь, что ваша среда разработки совместима с Vue 3 перед началом работы.

### Шаг 2: Импорт AtomicXCore в ваш проект

1. **Установка компонента:**
2. Установите пакет `tuikit-atomicx-vue3` одной из следующих команд:

npm

pnpm

yarn

```
npm install tuikit-atomicx-vue3 --save
```

```
pnpm add tuikit-atomicx-vue3
```

```
yarn add tuikit-atomicx-vue3
```

3. **Конфигурация прав браузера:** Убедитесь, что ваше веб-приложение запрашивает разрешение на использование камеры и микрофона. Современные браузеры обычно запрашивают эти разрешения при первом доступе.

### Шаг 3: Реализация логики входа

Вызовите метод `login` из `useLoginState()` в вашем проекте для аутентификации. **Вход обязателен перед использованием любой функциональности AtomicXCore.**

> **Примечание:** Вызывайте метод `login` в `useLoginState` только после успешного входа в вашу учетную запись. Это обеспечивает ясность и согласованность логики аутентификации.

```
import { useLoginState } from 'tuikit-atomicx-vue3';const { login } = useLoginState();async function initLogin() {  try {    await login({      sdkAppId: 0,   // Замените на ваш sdkAppId      userId: "",    // Замените на ваш userId      userSig: ""    // Замените на ваш userSig    });  } catch (error) {    console.error("login failed:", error);  }}initLogin(); // Вызовите initLogin при монтировании компонента или в подходящий момент
```

**Описание параметров API входа:**

| Параметр | Тип | Описание |
| --- | --- | --- |
| `sdkAppId` | `int` | ID приложения прямой трансляции, созданного в [Console](https://console.trtc.io/app). |
| `userId` | `string` | Уникальный идентификатор текущего пользователя. Используйте только буквы, цифры, дефисы и подчеркивания. Избегайте простых ID типа `1`, `123` и т. д., чтобы предотвратить конфликты входа с нескольких устройств. |
| `userSig` | `string` | Билет для аутентификации Tencent Cloud. Примечание: Среда разработки: Вы можете использовать локальную функцию `GenerateTestUserSig.genTestSig` для генерации `UserSig` или сгенерировать временный UserSig через [UserSig Generation Tool](https://console.trtc.io/usersig). Производственная среда: Чтобы предотвратить утечку ключа, вы должны использовать серверный метод для генерации `UserSig`. Для деталей см. [Generating UserSig on the Server](https://www.tencentcloud.com/document/product/647/35166). |

## Создание базовой комнаты прямой трансляции

### Шаг 1: Реализация видеотрансляции хоста

Следуйте этим шагам для быстрого настройки потоковой передачи видео хоста

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/444b96b5d1a811f0b1675254001c06ec.png)

1. **Инициализация представления трансляции хоста**

В компоненте Vue вашего хоста импортируйте и используйте компонент `StreamMixer`:

```
<template>   <StreamMixer /></template><script setup lang="ts">import { StreamMixer } from 'tuikit-atomicx-vue3';</script>
```

2. **Включение камеры и микрофона**

Используйте методы `openLocalCamera` и `openLocalMicrophone` из `useDeviceState` для включения камеры и микрофона. `StreamMixer` будет автоматически предпросматривать текущий видеопоток камеры.

```
import { onMounted } from 'vue';import { useDeviceState } from 'tuikit-atomicx-vue3';const { openLocalCamera, openLocalMicrophone } = useDeviceState();onMounted(() => {     openLocalMicrophone();  openLocalCamera();})
```

3. **Начало прямой трансляции**

Вызовите метод `createLive` из `useLiveListState` для начала трансляции:

```
import { useLiveListState } from 'tuikit-atomicx-vue3';const { createLive } = useLiveListState();// Определите ID комнаты прямой трансляции, обычно генерируется бэкендом или передается через параметр маршрутаconst liveId = ref('test_live_room_001');async function startLive() {  try {    await createLive({      liveId: liveId.value, // Установите ID комнаты прямой трансляции      liveName: 'test Live', // Установите имя комнаты прямой трансляции    });  } catch (error) {    console.error('Failed to create live:', error);  }}
```

**Описание параметров LiveInfo:**

| **Название параметра** | **Тип** | **Атрибут** | **Описание** |
| --- | --- | --- | --- |
| `liveId` | `string` | Обязательный | Уникальный идентификатор комнаты прямой трансляции |
| `liveName` | `string` | Обязательный | Название комнаты прямой трансляции |
| `notice` | `string` | Опциональный | Объявление для комнаты прямой трансляции |
| `isMessageDisableForAllUser` | `boolean` | Опциональный | Отключить звук всех пользователей (`true`: да, `false`: нет) |
| `isPublicVisible` | `boolean` | Опциональный | Публично видимый (`true`: да, `false`: нет) |
| `isSeatEnabled` | `boolean` | Опциональный | Включить функцию мест (`true`: да, `false`: нет) |
| `keepOwnerOnSeat` | `boolean` | Опциональный | Оставить хоста на месте |
| `maxSeatCount` | `number` | Опциональный | Максимальное количество мест |
| `seatMode` | `string` | Опциональный | Режим мест (`'FREE'`: свободно стать соведущим, `'APPLY'`: запросить доступ для того, чтобы стать соведущим) |
| `seatLayoutTemplateId` | `number` | Опциональный | ID шаблона расположения мест |
| `coverUrl` | `string` | Опциональный | URL изображения обложки для комнаты прямой трансляции |
| `backgroundUrl` | `string` | Опциональный | URL изображения фона для комнаты прямой трансляции |
| `categoryList` | `number[]` | Опциональный | Список тегов категорий для комнаты прямой трансляции |
| `activityStatus` | `number` | Опциональный | Статус активности прямой трансляции |
| `isGiftEnabled` | `boolean` | Опциональный | Включить функцию подарков (`true`: да, `false`: нет) |
| `isLikeEnabled` | `boolean` | Опциональный | Включить лайки (`true`: да, `false`: нет) |

4. **Завершение прямой трансляции**

Чтобы завершить прямую трансляцию, вызовите метод `endLive` из `useLiveListState`. SDK автоматически остановит поток и уничтожит комнату.

```
import { useLiveListState } from 'tuikit-atomicx-vue3';const { endLive } = useLiveListState();// Завершить прямую трансляциюasync function stopLive() {  try {    await endLive();  } catch (error) {    console.error('Failed to end live:', error);  }}
```

### Шаг 2: Реализация входа аудитории в комнату прямой трансляции

Позвольте членам аудитории смотреть прямую трансляцию, следуя этим шагам:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9dc0302bd1a811f09975525400bf7822.png)

1. **Добавление страницы воспроизведения для аудитории**

В компоненте Vue вашей аудитории импортируйте и используйте компонент `LiveView`:

```
<template>   <LiveView /></template><script setup lang="ts">import { LiveView } from 'tuikit-atomicx-vue3';</script>
```

2. **Вход в комнату прямой трансляции для просмотра**

Вызовите метод `joinLive` из `useLiveListState` для входа в комнату прямой трансляции. `LiveView` будет автоматически воспроизводить видеопоток текущей комнаты.

```
import { useLiveListState } from 'tuikit-atomicx-vue3';const { joinLive } = useLiveListState();// Определите ID комнаты прямой трансляции для входаconst liveId = ref('test_live_room_001');// Войдите в комнату прямой трансляцииasync function joinLiveRoom() {  try {    await joinLive({ liveId: liveId.value }); // Используйте тот же liveId, что и хост  } catch (error) {    console.error('Failed to enter live room:', error);  }}
```

3. **Выход из прямой трансляции**

Когда член аудитории покидает комнату прямой трансляции, вызовите метод `leaveLive` из `useLiveListState`. SDK автоматически остановит воспроизведение и выйдет из комнаты.

```
import { useLiveListState } from 'tuikit-atomicx-vue3';const { leaveLive } = useLiveListState();// Выход из прямой трансляцииasync function exitLive() {  try {    await leaveLive();     // Здесь вы можете выполнить навигацию страницы  } catch (error) {    console.error('Failed to leave live room:', error);  }}
```

### Шаг 3: Прослушивание событий прямой трансляции

После входа члена аудитории в комнату прямой трансляции обрабатывайте пассивные события, такие как завершение трансляции хостом или удаление пользователей за нарушения. Без обработки событий пользовательский интерфейс может остаться на черном экране, что повлияет на пользовательский опыт. Подпишитесь на события, используя `subscribeEvent` из `useLiveListState`:

```
import { useLiveListState, LiveListEvent } from "tuikit-atomicx-vue3";import { onMounted, onUnmounted } from 'vue';const { subscribeEvent, unsubscribeEvent } = useLiveListState();const handleKickedOutOfLive = () => {  console.log('You have been removed from the live room');};const handleLiveEnded = () => {  console.log('Live has ended');};onMounted(() => {  subscribeEvent(LiveListEvent.onLiveEnded, handleLiveEnded);  subscribeEvent(LiveListEvent.onKickedOutOfLive, handleKickedOutOfLive);});onUnmounted(() => {  unsubscribeEvent(LiveListEvent.onLiveEnded, handleLiveEnded);  unsubscribeEvent(LiveListEvent.onKickedOutOfLive, handleKickedOutOfLive);});
```

### Эффект во время выполнения

После интеграции `LiveView` вы будете иметь чистую область рендеринга видео с полными возможностями прямой трансляции, но без интерактивного пользовательского интерфейса. См. следующий раздел, **Enhancing the Live Experience**, для добавления интерактивных функций в вашу прямую трансляцию.

## Улучшение опыта прямой трансляции

После реализации базовой прямой трансляции обратитесь к следующим руководствам функций для добавления интерактивных элементов в вашу прямую трансляцию.

| **Функция прямой трансляции** | **Описание функции** | **Состояние функции** | **Руководство по реализации** |
| --- | --- | --- | --- |
| Включение аудиолинии/видеолинии аудитории | Аудитория может запросить присоединение к трансляции и взаимодействовать с хостом в режиме реального времени видео. | [CoGuestState](https://web.sdk.qcloud.com/trtc/live/web/doc/en/index.html#module-CoGuestState) | Реализация связывания аудитории |
| Включение кросс-рум PK хоста | Хосты из двух разных комнат могут подключиться для взаимодействия или PK. | [CoHostState](https://web.sdk.qcloud.com/trtc/live/web/doc/en/index.html#module-CoHostState) | Реализация связывания PK хоста |
| Добавление функции пуль-чата | Аудитория может отправлять и получать сообщения в режиме реального времени в комнате прямой трансляции. | [BarrageState](https://web.sdk.qcloud.com/trtc/live/web/doc/en/index.html#module-BarrageState) | Реализация пуль-чата |

## Документация API

| **Состояние** | **Описание функции** | **Документация API** |
| --- | --- | --- |
| LiveListState | Полное управление жизненным циклом комнат прямой трансляции: создание, вход, выход, уничтожение комнаты, запрос списка комнат, изменение информации прямой трансляции (имя, объявление и т. д.), прослушивание статуса прямой трансляции (такого как удаление, завершение). | [Документация API](https://web.sdk.qcloud.com/trtc/live/web/doc/en/index.html#module-LiveListState) |
| DeviceState | Управление устройствами аудио/видео: микрофон (переключение, громкость), камера (переключение, переключение камеры, качество видео), общий доступ к экрану, мониторинг состояния устройства в режиме реального времени. | [Документация API](https://web.sdk.qcloud.com/trtc/live/web/doc/en/index.html#module-DeviceState) |
| CoGuestState | Управление связыванием аудитории: запрос связывания, приглашение, одобрение, отклонение, управление правами членов (микрофон, камера), синхронизация статуса. | [Документация API](https://web.sdk.qcloud.com/trtc/live/web/doc/en/index.html#module-CoGuestState) |
| CoHostState | Кросс-рум связывание хоста: поддерживает несколько шаблонов компоновки (динамическая сетка и т. д.), инициирование, принятие, отклонение связывания, управление взаимодействием соведущих. | [Документация API](https://web.sdk.qcloud.com/trtc/live/web/doc/en/index.html#module-CoHostState) |
| BarrageState | Функция пуль-чата: отправка текста или пользовательского пуль-чата, ведение списка пуль-чата, мониторинг статуса пуль-чата в режиме реального времени. | [Документация API](https://web.sdk.qcloud.com/trtc/live/web/doc/en/index.html#module-BarrageState) |
| LiveAudienceState | Управление аудиторией: получение списка аудитории в режиме реального времени (ID, имя, аватар), подсчет количества аудитории, прослушивание событий входа/выхода аудитории. | [Документация API](https://web.sdk.qcloud.com/trtc/live/web/doc/en/index.html#module-LiveAudienceState) |

## Часто задаваемые вопросы

### Почему экран черный и нет видео после вызова хостом createLive или аудиторией joinLive?

- **Проверьте статус входа:** Убедитесь, что вы успешно вызвали метод `login` перед вызовом интерфейсов трансляции или просмотра.
- **Проверьте разрешения браузера:** Убедитесь, что браузер имеет разрешение на использование камеры и микрофона. Современные браузеры запрашивают разрешение при первом доступе.
- **Проверьте сторону хоста:** Убедитесь, что хост вызвал `openLocalCamera()` для включения камеры.
- **Проверьте сеть:** Убедитесь, что устройство имеет стабильное сетевое соединение и может получить доступ к услугам TRTC.
- **Проверьте HTTPS:** В производстве ваше веб-приложение должно работать через HTTPS, так как браузеры требуют защищенный контекст для доступа к камере и микрофону.

### Почему хост видит локальный предпросмотр видео после начала трансляции, но предпросмотр черный перед выходом в эфир?

- **Проверьте сторону хоста:** Убедитесь, что представление трансляции хоста использует компонент `StreamMixer`.
- **Проверьте сторону аудитории:** Убедитесь, что представление воспроизведения аудитории использует компонент `LiveView`.
- **Проверьте импорты компонентов:** Подтвердите, что соответствующие компоненты импортированы из `tuikit-atomicx-vue3`.

### Проблемы, специфичные для веб-версии

- **Совместимость браузера:** Используйте современный браузер, поддерживающий WebRTC. Рекомендуется: Chrome 70+, Firefox 65+, Safari 12+ или Edge 79+.
- **Локальная среда разработки:** Для локальной разработки используйте `localhost` или `127.0.0.1`. В производстве используйте HTTPS.
- **Брандмауэр и прокси:** В корпоративных сетях убедитесь, что брандмауэр разрешает порты и протоколы, связанные с WebRTC.


---
*Источник: [https://trtc.io/document/74840](https://trtc.io/document/74840)*

---
*Источник (EN): [video-live-streaming.md](./video-live-streaming.md)*

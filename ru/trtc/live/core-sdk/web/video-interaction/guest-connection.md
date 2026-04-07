# Подключение гостя

**AtomicXCore** предоставляет модуль [CoGuestState](https://web.sdk.qcloud.com/trtc/live/web/doc/en/index.html#module-CoGuestState), специально разработанный для управления полным процессом подключения зрителей в качестве гостей в сценариях прямого эфира. Вам не нужно самостоятельно обрабатывать сложную синхронизацию состояния или логику сигнализации — просто вызовите несколько простых методов, чтобы обеспечить беспрепятственное взаимодействие по аудио/видео между ведущим и аудиторией.

## Основные сценарии

`CoGuestState` охватывает два наиболее распространённых процесса подключения гостя:

- **Запрос аудитории на присоединение**: Члены аудитории могут активно запросить присоединение к потоку в качестве гостя. Ведущий может принять или отклонить эти запросы.
- **Ведущий приглашает аудиторию присоединиться**: Ведущий может пригласить любого члена аудитории в прямую трансляцию присоединиться в качестве гостя.

## Пример проекта

Посмотрите компонент [CoGuestPanel](https://github.com/Tencent-RTC/TUIKit_Vue3/blob/main/packages/tuikit-atomicx-vue3/src/components/CoGuestPanel/CoGuestPanel.vue) на GitHub для полного примера реализации.

## Реализация

### Интеграция компонента

Следуйте [руководству быстрого старта](https://www.tencentcloud.com/document/product/647/74840) для интеграции **AtomicXCore** и настройки `LiveCoreView`.

> **Примечание:** Перед продолжением убедитесь, что вы создали или присоединились к комнате, как описано в [руководстве быстрого старта](https://www.tencentcloud.com/document/product/647/74840). Затем выполните приведённые ниже шаги.

### Запрос аудитории на присоединение

#### Реализация со стороны аудитории

Как член аудитории, вам потребуется отправить запрос на подключение в качестве гостя, обработать ответ ведущего и отключиться при необходимости.

##### **Инициирование запроса на совместное ведение**

Вызовите метод `applyForSeat` когда пользователь нажимает кнопку "Запросить присоединение" в вашем пользовательском интерфейсе.

```
import { useCoGuestState } from "tuikit-atomicx-vue3";const { applyForSeat } = useCoGuestState();// User clicks "Request to Join"const handleRequestToConnect = async () => {    try {        await applyForSeat({           seatIndex: -1, // -1 assigns a seat randomly          timeout: 30,   // Timeout in seconds; if TS expects ms, use 30000        });        console.log('Request sent');    } catch (error) {        console.error('Request failed', error);    }}
```

##### Обработка ответа ведущего

Подпишитесь на событие `CoGuestEvent.onGuestApplicationResponded` с помощью `subscribeEvent` для получения решения ведущего.

```
import { onMounted, onUnmounted } from 'vue';import { useCoGuestState, useDeviceState, CoGuestEvent } from "tuikit-atomicx-vue3";const { subscribeEvent, unsubscribeEvent } = useCoGuestState();const { openLocalMicrophone, openLocalCamera } = useDeviceState();const handleGuestApplicationResponded = (eventInfo: any) => {    if (eventInfo.isAccept) {        console.log('Guest request accepted');        // Enable microphone and camera        openLocalMicrophone();        openLocalCamera();        // Update UI to indicate guest connection is active    } else {        console.log('Guest request rejected');        // Notify user that the request was rejected    }};onMounted(() => {    subscribeEvent(CoGuestEvent.onGuestApplicationResponded, handleGuestApplicationResponded);});onUnmounted(() => {    unsubscribeEvent(CoGuestEvent.onGuestApplicationResponded, handleGuestApplicationResponded);});
```

##### Отключение от режима гостя

Когда гость хочет уйти, вызовите метод `disConnect` чтобы вернуться в статус зрителя.

```
import { useCoGuestState } from "tuikit-atomicx-vue3";const { disConnect } = useCoGuestState();// User clicks "Leave Seat"const leaveSeat = async () => {    try {        await disConnect();        console.log('Disconnected successfully');    } catch (error) {        console.log('Disconnect failed', error);    }}
```

##### Отмена ожидающего запроса (опционально)

Если член аудитории хочет отозвать свой запрос до того, как ведущий ответит, используйте `cancelApplication`.

```
import { useCoGuestState } from "tuikit-atomicx-vue3";const { cancelApplication } = useCoGuestState();// User clicks "Cancel Request" while waitingconst handleCancelRequest = async () => {    await cancelApplication();    console.log('Request cancelled successfully');}
```

#### Реализация со стороны ведущего

Как ведущий, вам потребуется прослушивать входящие запросы, отображать список запросов и обработать каждый запрос.

##### Прослушивание новых запросов от гостей

Подпишитесь на событие `CoHostEvent.onGuestApplicationReceived` чтобы получить уведомление когда член аудитории запрашивает присоединение.

```
import { onMounted, onUnmounted } from 'vue';import { useCoGuestState, CoHostEvent } from "tuikit-atomicx-vue3";const { subscribeEvent, unsubscribeEvent } = useCoGuestState();const handleGuestApplicationReceived = (eventInfo: any) => {    console.log('Received guest request from audience:', eventInfo.guestUser);    // Update UI, e.g., show a notification badge on the "Request List" button};onMounted(() => {    subscribeEvent(CoHostEvent.onGuestApplicationReceived, handleGuestApplicationReceived);});onUnmounted(() => {    unsubscribeEvent(CoHostEvent.onGuestApplicationReceived, handleGuestApplicationReceived);});
```

##### Отображение списка запросов

`CoGuestState` предоставляет список актуальных претендентов через Vue `ComputedRef` `applicants`. Каждый претендент включает поля такие как `userId` и `userName`. Используйте это напрямую в вашем шаблоне:

```
<template>    <div v-for="audience in applicants" :key="audience.userId" class="applicant-item">      <span>{{ audience.userName }}</span>      <button @click="handleAccept(audience.userId)">Accept</button>      <button @click="handleReject(audience.userId)">Reject</button>    </div></template><script setup lang="ts">import { useCoGuestState } from "tuikit-atomicx-vue3";const { applicants, acceptApplication, rejectApplication } = useCoGuestState();const handleAccept = async (userId: string) => {    await acceptApplication({ userId });};const handleReject = async (userId: string) => {    await rejectApplication({ userId });};</script>
```

### Ведущий приглашает аудиторию присоединиться

#### Реализация со стороны ведущего

##### Пригласить члена аудитории

Когда ведущий выбирает члена аудитории и нажимает "Пригласить присоединиться", вызовите `inviteToSeat`.

```
import { useCoGuestState } from "tuikit-atomicx-vue3";const { inviteToSeat } = useCoGuestState();// Host selects an audience member and sends an invitationconst handleInviteToSeat = async (userId: string) => {    try {        await inviteToSeat({            userId,            seatIndex: -1, // Assign seat randomly            timeout: 30,        });        console.log(`Sent guest invitation to audience ${userId}`);    } catch (error) {        console.error('Invitation failed', error);    }}
```

##### Обработка ответа аудитории

Подпишитесь на событие `CoHostEvent.onHostInvitationResponded` чтобы отследить, принял или отклонил ли член аудитории приглашение.

```
import { onMounted } from 'vue';import { useCoGuestState, CoHostEvent } from "tuikit-atomicx-vue3";const { subscribeEvent } = useCoGuestState();onMounted(() => {    subscribeEvent(CoHostEvent.onHostInvitationResponded, (eventInfo) => {        if(eventInfo.isAccept){            console.log(`Audience ${eventInfo.guestUser.userName} accepted your invitation`);        } else {            console.log(`Audience ${eventInfo.guestUser.userName} rejected your invitation`);        }    });});
```

#### Реализация со стороны аудитории

##### Получение приглашения от ведущего

Подпишитесь на событие `CoGuestEvent.onHostInvitationReceived` чтобы обнаружить когда ведущий отправляет приглашение.

```
import { onMounted } from 'vue';import { useCoGuestState, CoGuestEvent } from "tuikit-atomicx-vue3";const { subscribeEvent } = useCoGuestState();onMounted(() => {    subscribeEvent(CoGuestEvent.onHostInvitationReceived, (eventInfo) => {        // Show a modal dialog for the user to accept or reject        // Save eventInfo.hostUser.userId as inviterId        showInviteDialog(eventInfo.hostUser.userId);    });});
```

##### Ответ на приглашение

Когда пользователь выбирает принять или отклонить в диалоговом окне, вызовите соответствующий метод.

```
import { useCoGuestState, useDeviceState } from "tuikit-atomicx-vue3";const { acceptInvitation, rejectInvitation } = useCoGuestState();const { openLocalMicrophone, openLocalCamera } = useDeviceState();// User clicks "Accept"const handleAccept = async (inviterId: string) => {    try {        await acceptInvitation({ inviterId });        // Automatically enable microphone and camera after accepting        openLocalMicrophone();        openLocalCamera();    } catch (error) {        console.error('Failed to accept invitation', error);    }}// User clicks "Reject"const handleReject = async (inviterId: string) => {    await rejectInvitation({ inviterId });}
```

### Демонстрация функции

После интеграции этих функций вы можете протестировать подключение гостей с двумя членами аудитории и одним ведущим: аудитория A включает как камеру, так и микрофон, в то время как аудитория B включает только микрофон. Функция работает как показано ниже.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/61a4781fd1a911f0931a5254005ef0f7.png)

## Документация API

Для полной информации по всем общедоступным интерфейсам, свойствам и методам для [CoGuestState](https://web.sdk.qcloud.com/trtc/live/web/doc/en/index.html#module-CoGuestState) и связанных классов, обратитесь к официальной документации API для платформы [AtomicXCore](https://web.sdk.qcloud.com/trtc/live/web/doc/en/index.html). Основные состояния, используемые в этом руководстве, включают:

| **Состояние** | **Описание** | **Документация API** |
| --- | --- | --- |
| DeviceState | Управление устройствами аудио/видео: микрофон (включение/выключение / громкость), камера (включение/выключение / переключение / качество), общее использование экрана, мониторинг состояния устройства в реальном времени. | [Документация API](https://web.sdk.qcloud.com/trtc/live/web/doc/en/index.html#module-DeviceState) |
| CoGuestState | Управление гостями из аудитории: запрос гостя / приглашение / принятие / отклонение, управление разрешениями членов гостя (микрофон / камера), синхронизация состояния. | [Документация API](https://web.sdk.qcloud.com/trtc/live/web/doc/en/index.html#module-CoGuestState) |
| LiveSeatState | Управление информацией о местах: управление списком мест, управление порядком мест. | [Документация API](https://web.sdk.qcloud.com/trtc/live/web/doc/en/index.html#module-LiveSeatState) |

## Часто задаваемые вопросы

### Подключение гостя не работает (запрос/приглашение/принятие/отклонение не выполняется)

- **Проблема:** Методы такие как `applyForSeat`, `acceptApplication` или `inviteToSeat` не работают.
- **Причина:** `CoGuestState` зависит от состояния базового движка комнаты. Это обычно происходит если пользователь не присоединился к комнате или контекст `useCoGuestState` не инициализирован.
- **Решение:** Убедитесь, что пользователь успешно присоединился к комнате прямой трансляции перед вызовом этих методов.

### Отсутствуют уведомления о событиях подключения гостя

- **Проблема:** Аудитория не получает приглашения от ведущего или ведущий не получает запросы от аудитории.
- **Причина:**
  - `subscribeEvent` был вызван неправильно.
  - Использовано неправильное значение перечисления событий (например, смешивание `CoHostEvent` и `CoGuestEvent`).
- **Решение:**
  - **Ведущий:** Подпишитесь на `CoHostEvent.onGuestApplicationReceived` и `CoHostEvent.onHostInvitationResponded`.
  - **Аудитория:** Подпишитесь на `CoGuestEvent.onGuestApplicationResponded` и `CoGuestEvent.onHostInvitationReceived`.

### Нет видео или аудио после подключения гостя

- **Проблема:** После присоединения в качестве гостя список мест обновляется, но видео или аудио отсутствуют.
- **Причина:** `CoGuestState` обрабатывает только сигнализацию для подключения гостей (назначение места). Трансляция (включение микрофона/камеры) требует явных вызовов методов `DeviceState`.
- **Решение:** В обратном вызове для "принятия запроса" или "принятия приглашения" убедитесь, что вызвали `openLocalMicrophone` и `openLocalCamera`. Также проверьте политики автозапуска браузера и убедитесь, что пользователь взаимодействовал со страницей.


---
*Источник: [https://trtc.io/document/74842](https://trtc.io/document/74842)*

---
*Источник (EN): [guest-connection.md](./guest-connection.md)*

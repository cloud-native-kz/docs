# Список аудитории

`LiveAudienceState` — это специализированный модуль в составе **AtomicXCore**, предназначенный для управления информацией об аудитории в комнатах прямых трансляций. С помощью `LiveAudienceState` вы можете создать надежную систему списка и управления аудиторией для приложения прямой трансляции.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/69fc33b5d18911f0b1675254001c06ec.png)

## Основные возможности

- **Список аудитории в реальном времени**: получение и отображение информации обо всех текущих зрителях в комнате трансляции.
- **Статистика количества аудитории**: получение точного количества зрителей в комнате трансляции в реальном времени.
- **Мониторинг активности аудитории**: подписка на события для мгновенного обнаружения входа и выхода зрителей.
- **Права администратора**: хосты могут предоставлять или отзывать права администратора.
- **Управление комнатой**: хосты или администраторы могут удалять обычных зрителей из комнаты трансляции.

## Пример проекта

Ознакомьтесь с компонентом [LiveAudienceList](https://github.com/Tencent-RTC/TUIKit_Vue3/blob/main/packages/tuikit-atomicx-vue3/src/components/LiveAudienceList/LiveAudienceList.vue) на **GitHub** для получения полного примера реализации.

## Этапы реализации

### Шаг 1: интеграция компонента

Следуйте руководству [Quick Start](https://www.tencentcloud.com/document/product/647/74840), чтобы интегрировать **AtomicXCore** и завершить начальную настройку.

### Шаг 2: инициализация и получение списка аудитории

Получите экземпляр `LiveAudienceState` и активно получите текущий список аудитории для начального отображения. Модуль автоматически прослушивает изменения состояния комнаты трансляции и обновляет список аудитории при переключении между комнатами.

```
import { onMounted, watch } from 'vue';import { useLiveAudienceState } from "tuikit-atomicx-vue3";// Get an instance of LiveAudienceStateconst { fetchAudienceList, audienceList } = useLiveAudienceState();onMounted(async () => {  try {    // Fetch the audience list, returns a Promise    await fetchAudienceList();    console.log('Successfully fetched the initial audience list');  } catch (error) {    console.error('Failed to fetch the initial audience list', error);  }});// Watch for real-time changes in audienceList to drive UI updateswatch(audienceList, (newVal) => {  console.log('Audience list updated:', newVal);});
```

### Шаг 3: прослушивание состояния списка аудитории и действий в реальном времени

Подпишитесь на события `audienceState` и реактивные данные, чтобы получать полные снимки списка и события входа/выхода аудитории в реальном времени, обеспечивая динамические обновления пользовательского интерфейса.

```
import { onMounted, onUnmounted, watch } from 'vue';import { useLiveAudienceState, LiveAudienceEvent } from "tuikit-atomicx-vue3";const {   audienceList,   audienceCount,   subscribeEvent,   unsubscribeEvent } = useLiveAudienceState();// Watch for real-time changes in audienceCount to update the UI displaywatch(audienceCount, (newCount) => {  console.log(`Current online audience: ${newCount}`);});// Define callback functionsconst onAudienceJoined = (eventInfo) => {  console.log(`Audience member ${eventInfo.audience.userName} joined the live room`);};const onAudienceLeft = (eventInfo) => {  console.log(`Audience member ${eventInfo.audience.userName} left the live room`);};onMounted(() => {  // Subscribe to audience join event  subscribeEvent(LiveAudienceEvent.onAudienceJoined, onAudienceJoined);  // Subscribe to audience leave event  subscribeEvent(LiveAudienceEvent.onAudienceLeft, onAudienceLeft);});onUnmounted(() => {  // Unsubscribe when the component is unmounted  unsubscribeEvent(LiveAudienceEvent.onAudienceJoined, onAudienceJoined);  unsubscribeEvent(LiveAudienceEvent.onAudienceLeft, onAudienceLeft);});
```

### Шаг 4: управление аудиторией (удаление из комнаты и назначение администратора)

Хосты и администраторы могут управлять зрителями в комнате трансляции.

#### 4.1 Удаление обычных зрителей из комнаты трансляции

Используйте API `kickUserOutOfRoom` для удаления указанного пользователя из комнаты трансляции.

```
import { useLiveAudienceState } from "tuikit-atomicx-vue3";const { kickUserOutOfRoom } = useLiveAudienceState();const handleKickUser = async (targetUserId: string) => {  try {    await kickUserOutOfRoom({ userId: targetUserId });    console.log(`Host or administrator removed ${targetUserId} from the live room`);  } catch (error) {    console.error(`Failed to remove ${targetUserId} from the live room`, error);  }};
```

#### 4.2 Предоставление или отзыв прав администратора

Используйте API `setAdministrator` и `revokeAdministrator` для управления статусом администратора пользователя.

```
import { useLiveAudienceState } from "tuikit-atomicx-vue3";const { setAdministrator, revokeAdministrator } = useLiveAudienceState();const promoteToAdmin = async (targetUserId: string) => {  try {    await setAdministrator({ userId: targetUserId });    console.log(`Successfully assigned administrator privileges to user ${targetUserId}`);  } catch (error) {    console.error(`Failed to assign administrator privileges to user ${targetUserId}`, error);  }};const revokeAdmin = async (targetUserId: string) => {  try {    await revokeAdministrator({ userId: targetUserId });    console.log(`Successfully revoked administrator privileges from user ${targetUserId}`);  } catch (error) {    console.error(`Failed to revoke administrator privileges from user ${targetUserId}`, error);  }};
```

#### 4.3 Отключение звука и включение звука для членов аудитории

Администраторы могут запретить или разрешить пользователю доступ к отправке сообщений в комнате.

```
import { useLiveAudienceState } from "tuikit-atomicx-vue3";const { disableSendMessage } = useLiveAudienceState();// Mute userconst muteUser = async (targetUserId: string) => {    await disableSendMessage({ userId: targetUserId, isDisable: true });};// Unmute userconst unmuteUser = async (targetUserId: string) => {    await disableSendMessage({ userId: targetUserId, isDisable: false });};
```

## Расширенное использование

### Отображение приветственного сообщения в области баража при входе аудитории

Автоматически отобразить локальное приветственное сообщение в области баража/чата при входе нового члена аудитории в комнату трансляции, например: "Добро пожаловать `ник пользователя` в комнату трансляции".

#### Реализация

Подпишитесь на событие `onAudienceJoined` и отобразите приветственное сообщение в области баража/чата.

```
import { onMounted, onUnmounted } from 'vue';import { useLiveAudienceState, useBarrageState, LiveAudienceEvent } from "tuikit-atomicx-vue3";const { subscribeEvent, unsubscribeEvent } = useLiveAudienceState();// Assume useBarrageState provides the appendLocalTip methodconst { appendLocalTip } = useBarrageState();const handleAudienceJoin = (eventInfo) => {  const { audience } = eventInfo;    // Create a local tip message  const welcomeTip = {    messageType: 'text',    textContent: `Welcome ${audience.userName || audience.userId} to the live room!`  };    // Insert local barrage message  appendLocalTip({ message: welcomeTip });  console.log(`Audience member ${audience.userName} joined the live room`);};onMounted(() => {  subscribeEvent(LiveAudienceEvent.onAudienceJoined, handleAudienceJoin);});onUnmounted(() => {  unsubscribeEvent(LiveAudienceEvent.onAudienceJoined, handleAudienceJoin);});
```

## Документация по API

Подробную информацию о всех открытых API, свойствах и методах [LiveAudienceState](https://web.sdk.qcloud.com/trtc/live/web/doc/en/index.html#module-LiveAudienceState) и связанных классов см. в официальной документации по API для фреймворка [AtomicXCore](https://web.sdk.qcloud.com/trtc/live/web/doc/en/index.html). Модули State, упомянутые в этом руководстве:

| **State** | **Описание возможностей** | **Документация по API** |
| --- | --- | --- |
| LiveAudienceState | Управление аудиторией: получение списка аудитории в реальном времени (ID / имя / аватар), подсчет количества аудитории, мониторинг событий входа/выхода аудитории. | [Документация по API](https://web.sdk.qcloud.com/trtc/live/web/doc/en/index.html#module-LiveAudienceState) |
| BarrageState | Функции баража: отправка текстовых / пользовательских сообщений баража, ведение списка баража, мониторинг статуса баража в реальном времени. | [Документация по API](https://web.sdk.qcloud.com/trtc/live/web/doc/en/index.html#module-BarrageState) |

## Часто задаваемые вопросы

### Как обновляется количество онлайн-аудитории (`audienceCount`) в `LiveAudienceState`? Каковы сроки и частота?

`audienceCount` обновляется с высокой точностью близко к реальному времени, но не всегда мгновенно. Механизм обновления выглядит следующим образом:

- **Активный вход/выход из комнаты**: когда пользователь активно присоединяется или покидает комнату трансляции, количество аудитории обновляется немедленно. Изменения в `audienceCount` в LiveAudienceState отражаются почти мгновенно.
- **Неожиданное отключение**: если пользователь отключается из-за проблем с сетью, сбоя приложения или других аномальных причин, система использует механизм проверки пульса для проверки их статуса. Пользователь считается оффлайн и количество аудитории обновляется только после потери пульса в течение 90 последовательных секунд.
- **Механизм обновления и контроль частоты:**
  - Все уведомления об изменении количества аудитории, независимо от того, являются ли они мгновенными или отложенными, передаются в виде сообщений в комнате.
  - Существует ограничение в **40 сообщений в секунду** на комнату.
- **Важно**: в сценариях с экстремально высоким трафиком сообщений (например, штормы баража, быстрая отправка подарков), если комната превышает порог 40 сообщений/сек, сообщения об изменении количества аудитории могут быть отброшены для приоритизации основных сообщений (таких как бараж).
- **Что это означает для разработчиков?**
  - `audienceCount` обеспечивает высокоточную оценку близко к реальному времени. Однако в сценариях с экстремальной высокой параллельностью могут возникнуть кратковременные задержки или потери данных. Рекомендуем использовать `audienceCount` **только для целей отображения пользовательского интерфейса**, а не в качестве единственного источника для выставления счетов, аналитики или других вариантов использования, требующих абсолютной точности.


---
*Источник: [https://trtc.io/document/74841](https://trtc.io/document/74841)*

---
*Источник (EN): [audience-list.md](./audience-list.md)*

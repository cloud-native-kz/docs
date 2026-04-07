# Планирование конференций

## Введение в функцию

TUIRoomKit представляет новую функцию для планирования комнат, которая позволяет пользователям зарезервировать комнату и запланировать встречу по расписанию.

> **Примечание:** **Начиная с версии v2.5.0, TUIRoomKit поддерживает возможность** планирования **комнат, просмотра списка комнат, изменения информации о комнате и т. д. Интегрируйте последнюю версию TUIRoomKit, чтобы получить опыт процесса** планирования **комнаты.**

## Как запланировать комнату

1. На экране предпросмотра TUIRoomKit нажмите **Schedule** > Заполните информацию о резервировании комнаты и установите связанные привилегии > Завершите настройку и нажмите **Schedule**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6f3a165c584b11ef8357525400bdab9d.png)

2. Результат расписания будет синхронизирован с результатом расписания в списке **запланированных комнат** справа от страницы предпросмотра, и он поддерживает операции, такие как **просмотр деталей, изменение комнат, отмена комнат, копирование информации о приглашении** и т. д. Кроме того, вы можете нажать **join**, чтобы войти в запланированную комнату.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ac7bf642584c11efb927525400fdb830.png)

## Условия подготовки

Прежде чем использовать функцию планирования комнат, предоставляемую Tencent Cloud, необходимо перейти в консоль и включить [конференц-сервис для приложения](https://trtc.io/document/59973?platform=web&product=conference). Дополнительные сведения о том, как это сделать, см. в разделе "Включение сервиса". Далее необходимо подключить компонент TUIRoomKit, как описано в разделе [Быстрый запуск](https://trtc.io/document/60441?platform=web&product=conference).

### Пример запуска комнаты планирования

> **Примечание:** Необходимо подключить **PreConferenceView (компонент предварительного просмотра конференции)** и **ConferenceMainView (основной элемент компонента пользовательского интерфейса TUIRoomkit)**. В примере используются директивы **v-if** и **v-else** для управления отображением и скрытием двух компонентов, также можно использовать переход маршрута для переключения между компонентами. В компоненте **PreConferenceView** вы контролируете, отображаются ли функции запланированной комнаты, установив значение свойства **enable-scheduled-conference**. Кроме того, компонент прослушивает событие on-enter-room, поэтому когда пользователь нажимает на вход в комнату, вызывается интерфейс [join](https://trtc.io/document/54880#b08d0951-c1f4-4db4-a84d-8414b853d0f1) путем запуска метода **handleEnterRoom**. В компоненте **ConferenceMainView** прослушивается событие **on-destroy-room** и вызывается метод **onDestroyRoom** при уничтожении комнаты.

Web

Electron

```
<template>  <PreConferenceView    v-if="isShowPreConferenceView"    :enable-scheduled-conference="true" // Setting whether to enable the schedule room feature display    @on-enter-room="handleEnterRoom"  ></PreConferenceView>  <ConferenceMainView    v-else    display-mode="permanent"    @on-destroy-room="onDestroyRoom"  ></ConferenceMainView></template><script setup lang="ts">import { ref } from 'vue'; // Note the package name, if you are using the vue2 version change the package name to @tencentcloud/roomkit-web-vue2.7import { PreConferenceView, conference, ConferenceMainView } from '@tencentcloud/roomkit-web-vue3';const isShowPreConferenceView = ref(true);const init = async () => {  conference.login({          sdkAppId: 0,  // Replace with your sdkAppId      userId: '',  // Replace with your userId      userSig: '',  // Replace with your userSig  });}init();async function handleEnterRoom(roomOption: Record<string, any>) {  const { roomId } = roomOption;  await conference.join(roomId, {    isOpenCamera: false,    isOpenMicrophone: false,  });  isShowPreConferenceView.value = false;}function onDestroyRoom() {  isShowPreConferenceView.value = true;  init();}</script>
```

```
<template>  <PreConferenceView    v-if="isShowPreConferenceView"    :enable-scheduled-conference="true" // Setting whether to enable the schedule room feature display    @on-enter-room="handleEnterRoom"  ></PreConferenceView>  <ConferenceMainView    v-else    display-mode="permanent"    @on-destroy-room="onDestroyRoom"  ></ConferenceMainView></template><script setup lang="ts">import { ref } from 'vue';  // Note the package name, if you are using the vue2 version change the package name to @tencentcloud/roomkit-electron-vue2.7import { PreConferenceView, conference, ConferenceMainView } from '@tencentcloud/roomkit-electron-vue3';const isShowPreConferenceView = ref(true);const init = async () => {  conference.login({          sdkAppId: 0,  // Replace with your sdkAppId      userId: '',  // Replace with your userId      userSig: '',  // Replace with your userSig  });}init();async function handleEnterRoom(roomOption: Record<string, any>) {  const { roomId } = roomOption;  await conference.join(roomId, {    isOpenCamera: false,    isOpenMicrophone: false,  });  isShowPreConferenceView.value = false;}function onDestroyRoom() {  isShowPreConferenceView.value = true;  init();}</script>
```

## Управление запланированной комнатой

## Планирование комнаты

После нажатия кнопки **Schedule** на странице предпросмотра открывается диалоговое окно параметров планирования комнаты, в котором пользователи могут установить информацию о комнате в соответствии со своими потребностями, которая может включать: **название комнаты, тип комнаты, время начала, длительность комнаты, часовой пояс, участники, безопасность (код доступа), управление (отключить всем звук, остановить видео для всех)** и т. д.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3ec1ac91584e11efb36952540075b605.png)

> **Примечание:** **Список членов приглашения TUIRoomKit** берется из **контактов IM**, поэтому необходимо использовать **IM для добавления друзей**. Вы можете заменить данные пользователя, **добавив друзей IM**. В этом случае необходимо использовать **REST API** IM для получения данных цепочки друзей IM, добавив отношение дружбы. Если вы импортируете данные из адресной книги участников или добавляете пользователей, см. раздел [Добавление друзей](https://trtc.io/document/34902?product=chat&menulabel=serverapis). Если вы хотите удалить участника, вы можете удалить отношение ассоциированного контакта в цепочке отношений IM, см. раздел [Удаление контактов](https://trtc.io/document/34905?product=chat&menulabel=serverapis).

### Просмотр деталей

Пользователи могут нажать **View Details**, чтобы просмотреть детали соответствующей запланированной комнаты.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/545eb527585011efb66652540055f650.png)

### Изменение информации о комнате

Владелец комнаты может изменить информацию о запланированной комнате, после изменения нажмите **Schedule**, чтобы скорректировать информацию текущей запланированной комнаты в соответствии с измененной информацией о комнате.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/72c3d1dd584f11efb927525400fdb830.png)

### Приглашение в комнату

Пользователи могут нажать

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7119856c585811ef81cf525400d5f8ef.png)

"Invite" (Пригласить), чтобы открыть диалоговое окно приглашения информации о встречи, и

**Скопировать номер конференции и ссылку**

в буфер обмена, чтобы поделиться с другими пользователями, нажав на кнопку "Copy Meeting Number & Link" (Скопировать номер встречи и ссылку).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f23d150e585011ef8357525400bdab9d.png)

## Оговорки

- Резервирование комнаты не может начаться раньше текущего времени, но количество дней заранее не ограничено.
- Если вы хотите запланировать комнаты на разные даты/время одновременно, просто выберите время и отправьте их одновременно.
- После резервирования комнаты номер комнаты будет зарезервирован на 6 часов с момента начала резервирования, если комната не занята, в течение этого времени вы можете вернуться в комнату в любое время.
- Номер комнаты и информация о резервировании будут доступны после успешного резервирования комнаты.

## Связь и обратная связь

Если у вас есть какие-либо вопросы или предложения, вы можете связаться с: info_rtc@tencent.com.


---
*Источник: [https://trtc.io/document/63275](https://trtc.io/document/63275)*

---
*Источник (EN): [conference-scheduling.md](./conference-scheduling.md)*

# Рабочий стол

В данном документе описано, как установить стили пользовательского интерфейса для веб-версии.

## Установка стилей пользовательского интерфейса списка разговоров

TUIConversation предоставляет функцию списка разговоров. Список разговоров состоит главным образом из области списка разговоров, которая предоставляет стили пользовательского интерфейса, которые могут быть изменены.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/38339715bc1611ee9000525400461a83.png)

### Установка стиля элемента списка разговоров

После входа пользователя в систему TUIKit считывает список разговоров пользователя из SDK на основе имени пользователя. Вы можете настроить общие функции для списка разговоров. Например, вы можете настроить стиль фотографии профиля, фон, размер шрифта, событие клика и событие долгого нажатия для списка разговоров.

Вы можете настроить отображение элементов списка для списка разговоров в `TUIKit/components/TUIConversation/conversation-list/index.vue`
Пример кода:

```
<template>  <div class="tui-conversation-list">    <!-- Conversation List operation panel -->    <ActionsMenu .../>    <!-- Conversation List Main -->    <div v-for="(conversation, index) in conversationList" ...>      <!-- Conversation List Item -->      <div :class="['TUI-conversation-item']">        <aside class="left">          <!-- Avatar -->          <img class="avatar" :src="conversation.getAvatar()" />          <!-- User Online Status -->          <div ... :class="['online-status']"></div>          <!-- Conversation Unread Count -->          <span class="num" ...>...</span>          <!-- Conversation Unread Red Dot(displayed in Do Not Disturb mode) -->          <span class="num-notify" ...>...</span>        </aside>        <div class="content">          <div class="content-header">            <!-- Conversation Name -->            <label class="content-header-label">              <p class="name">{{ conversation.getShowName() }}</p>            </label>            <!-- Conversation Last Message  -->            <div class="middle-box">              <!-- Conversation Last Message When Mentiond  -->              <span class="middle-box-at" ...>{{ conversation.getGroupAtInfo() }}</span>              <!-- Conversation Last Message Content  -->              <p class="middle-box-content">{{ conversation.getLastMessage("text") }}</p>            </div>          </div>          <div class="content-footer">            <!-- Conversation Lastest Message Time -->            <span class="time">{{ conversation.getLastMessage("time") }}</span>            <!-- Conversation Muted Flag -->            <Icon v-if="conversation.isMuted" :file="muteIcon"></Icon>          </div>      ...</template>
```

Вы можете установить стиль элементов списка в списке разговоров по пути `TUIKit/components/TUIConversation/conversation-list/style/web.scss`.
Ниже приведен пример кода для установки стиля аватара в списке разговоров:

```
.TUI-conversation {    &-item {        .left {            .avatar {                width: 30px; // avatar width                height: 30px; // avatar height                border-radius: 5px; // avatar border radius            }        }    }}
```

## Установка стилей пользовательского интерфейса чата

TUIChat предоставляет окно чата, состоящее из трех разделов сверху вниз: панель заголовка, область сообщений и область ввода, как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f88f61ebbc2d11ee9976525400c26da5.png)

Конфигурации, связанные с окном чата, главным образом находятся в пути `src/TUIKit/components/TUIChat` в директории файлов.

### Установка стиля панели заголовка

Панель заголовка состоит из двух областей (слева и справа), как показано на рисунке ниже:

Панель заголовка состоит из трех разделов, как показано ниже:

Основной код, связанный с панелью заголовка пользовательского интерфейса чата, находится в файле по пути `src/TUIKit/components/TUIChat/chat-header/index.vue`. Панель заголовка пользовательского интерфейса чата предоставляет различные функции для настройки, такие как фон, размер шрифта, значки кнопок, события клика, переключение функций и т.д.
Иллюстративный код выглядит следующим образом:

```
<template>  <div :class="['chat-header', !isPC && 'chat-header-h5']">    ...    <!-- Chat name / [Typing...] status prompt-->    <div :class="['chat-header-content', ...]">      {{ currentConversationName }}    </div>    <!-- Group chat settings extension -->    <div :class="['chat-header-setting', ...]">      <div v-for="(item, index) in extensions" :key="index" @click.stop="handleExtensions(item)">        <Icon :file="item.icon"></Icon>      </div>    </div>  </div></template>
```

Вы можете настроить стиль панели заголовка окна чата в файле `src/TUIKit/components/TUIChat/chat-header/index.vue`.
Пример кода для установки размера шрифта и цвета фона панели заголовка окна чата выглядит следующим образом:

```
.chat-header {   background-color: #147AFF;// chat background color   &-content{      font-size: 16px;// chat name font size   }}
```

### Установка стиля списка сообщений

#### Установка фона окна чата

Вы можете настроить цвет фона чата или фоновое изображение по пути `src/TUIKit/components/TUIChat/message-list/style/web.scss`.
Пример кода для установки цвета фона области сообщений окна чата выглядит следующим образом:

```
.TUI-chat {  ...  &-message-list {     background-color: #006eff;  }}
```

Пример кода для установки фонового изображения области сообщений окна чата выглядит следующим образом:

```
.TUI-chat {  ...  &-message-list {      background-image: url(https://qcloudimg.tencent-cloud.cn/raw/176cddbfb778a4bb26a5d423056efe1d.png);  }}
```

#### Установка стиля аватара

Код, связанный с аватаром в области сообщений, главным образом находится в пути файла `src/TUIKit/components/TUIChat/message-list/message-elements/message-bubble.vue`, и он реализуется с использованием общего компонента Avatar. Если пользователь не установил аватар, отображается аватар по умолчанию. Вы имеете возможность персонализировать аватар по умолчанию, решить, закруглен ли аватар, или заполнить другие спецификации размера.

**Компонент <Avatar>:**

| Имя параметра | Тип параметра | Обязателен | Значение по умолчанию | Описание параметра |  |
| --- | --- | --- | --- | --- | --- |
| url | string | Да | "https://web.sdk.qcloud.com/component/TUIKit/assets/avatar_21.png" | URL фотографии профиля |  |
| size | string | Нет | "36px" | Размеры фотографии профиля |  |
| borderRadius | string | Нет | "5px" | Закругленные углы для границы фотографии профиля |  |
| useSkeletonAnimation | boolean | Нет | false | Используется ли скелетонный экран? |  |

Пример кода для установки аватара по умолчанию вместе со скелетонным экраном выглядит следующим образом:

```
<Avatar   useSkeletonAnimation   :url="message.avatar || ''"/>
```

Пример кода для установки формы и размера фотографии профиля выглядит следующим образом:

```
<Avatar   useSkeletonAnimation   :url="message.avatar || ''"   size="40px"   borderRadius="0px"/>
```

#### Установка цветов фона пузырьков

В области сообщений каждое сообщение состоит из трех частей: `avatar` (фотография профиля), `messageArea` (область содержимого) и `messageLabel` (область метки). Подробная структура выглядит следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/37f1ccb9bc1911ee9976525400c26da5.png)

В области сообщений окна чата пузырьки слева принадлежат получателям, а справа — вам. Вы можете настроить фоны пузырьков обеих сторон в файле `src/TUIKit/components/TUIChat/message-list/message-elements/message-bubble.vue`.
Вот пример кода для установки цвета пузырьков сообщений:

```
.message-bubble {  .message-bubble-main-content {    .message-body {      .message-body-main {        .content-in {          background: #fbfbfb; // Set the color of the receiving message bubble          border-radius: 0px 10px 10px 10px;        }        .content-out {          background: #dceafd; // Set the color of the sender message bubble          border-radius: 10px 0px 10px 10px;        }      }    }  }}
```

#### Установка стиля никнейма отправителя

Вы можете настроить стиль никнейма отправителя, включая размер шрифта и цвет в файле `src/TUIKit/components/TUIChat/message-list/message-elements/message-bubble.vue`.
Следующий пример кода показывает, как установить стиль никнейма отправителя:

```
.message-bubble {  .message-bubble-main-content {    .message-body {      .message-body-nickName {        font-weight: 500; // Set the font weight of the sender's nickname        font-size: 14px; // Set sender nickname font size        color: #999999; // Set the font color of the sender's nickname      }    }  }}
```

#### Установка стиля содержимого сообщения

Вы можете настроить стиль содержимого чата, включая размер шрифта, цвет шрифта и размер эмодзи для обеих сторон в файле `src/TUIKit/components/TUIChat/message-list/message-elements/message-text.vue`.
Следующий пример кода показывает, как установить стиль содержимого чата:

```
.emoji {    width: 20px;// emoji width    height: 20px;// emoji height}.text {    white-space: pre-wrap;    font-size: 14px;// text message font size    color: #999999;// text message font color}
```

#### Установка стиля служебного сообщения

Вы можете настроить фон, размер шрифта и цвет шрифта служебных сообщений в файле по пути `src/TUIKit/components/TUIChat/message-list/message-elements/message-tip.vue`.
Вот пример кода для справки:

```
.message-tip {    margin: 0 auto;    color: #999999;// message tip font color    font-size: 14px;// message tip font size    background: red;// message tip background color}
```

### Установка области ввода InputView

Область ввода предоставляет различные функции, включая ввод текста и эмодзи, отправку изображений, видео, файлов, оценок и часто используемых выражений.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0453c5b6bc1a11eebdbe525400170219.png)

#### Скрытие ненужных функций

Вы можете настроить скрытие функций, таких как отправка изображений, файлов и оценок, модуля функций области ввода.
Этот модуль функций загружает функции, получая модуль функций, зарегистрированный в `src/TUIKit/components/TUIChat/message-input-toolbar/index.vue`. Вы можете удалить ненужные функции из файла.
Пример кода выглядит следующим образом:

```
  <div>    <div>      <!-- Emoji Picker -->      <EmojiPicker v-if="!isUniFrameWork"></EmojiPicker>      <!-- Taking photos, only available on uniapp -->      <ImageUpload v-if="isUniFrameWork" imageSourceType="camera"></ImageUpload>      <!-- Image Upload -->      <ImageUpload imageSourceType="album"></ImageUpload>      <!-- File Upload -->      <FileUpload v-if="!isUniFrameWork"></FileUpload>      <!-- Video Upload -->      <VideoUpload videoSourceType="album"></VideoUpload>      <!-- Taking videos, only available on uniapp -->      <VideoUpload v-if="isUniFrameWork" videoSourceType="camera"></VideoUpload>      <!-- Evaluate -->      <Evaluate></Evaluate>      <!-- Commonly Used Phrases -->      <!-- <Words></Words> -->    </div>  </div>
```

## Свяжитесь с нами

Присоединитесь к [группе технического обмена в Telegram](https://t.me/tencent_imsdk) или [группе обсуждения WhatsApp](https://chat.whatsapp.com/IVa11ZkVmKTEwSWsAzSyik), получайте поддержку профессиональных инженеров и решайте свои самые сложные задачи.


---
*Источник: [https://trtc.io/document/50047](https://trtc.io/document/50047)*

---
*Источник (EN): [desktop.md](./desktop.md)*

# Статус ввода текста

## Описание

@tencentcloud/chat-uikit-vue поддерживает функцию "Ввод..." для C2C-диалогов с версии v2.0.0

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ec8b80e61cc011ef9b9e5254002977b6.png)

Правила отображения "Ввод...":

1. Активируйте переключатель "Ввод..." (включен по умолчанию).
2. В текущем C2C-диалоге, если другой пользователь отправил вам сообщение в течение последних 30 секунд и в данный момент вводит текст.

## Активация/деактивация состояния ввода текста другой стороной

Функция "Собеседник вводит текст..." включена по умолчанию, поэтому нет необходимости повторять следующие шаги для её активации.

```
import { TUIStore, StoreName } from "@tencentcloud/chat-uikit-engine";// Включить функцию 'Typing'TUIStore.update(StoreName.APP, "enableTyping", true);// Отключить функцию 'Typing'TUIStore.update(StoreName.APP, "enableTyping", false);
```

## Дополнительная информация: как реализована функция "ввод ..." в TUIKit?

> **Примечание:** Следующий материал предназначен только для дополнительного чтения. Функция "ввод" уже включена в TUIKit по умолчанию и не требует ручной реализации.

##### 1. Отправитель: мониторит начало и конец ввода, отправляет сообщение о статусе другой стороне

В `TUIKit/components/TUIChat/message-input/index.vue` вы можете отправить сообщение о начале ввода текста через `TUIChatService.enterTypingState()`, а завершение ввода — через `TUIChatService.leaveTypingState()`.

```
// TUIKit/components/TUIChat/message-input/index.vueimport { TUIChatService } from "@tencentcloud/chat-uikit-engine";const onTyping = (inputContentEmpty: boolean, inputBlur: boolean) => {  sendTyping(inputContentEmpty, inputBlur);};// TUIKit/components/TUIChat/utils/sendMessage.tsexport const sendTyping = (inputContentEmpty: boolean, inputBlur: boolean) => {  if (!inputContentEmpty && !inputBlur) {    TUIChatService.enterTypingState();  } else {    TUIChatService.leaveTypingState();  }};
```

##### 2. Получатель: мониторит статус ввода отправителя и отображает его

В `TUIKit/components/TUIChat/chat-header/index.vue` осуществляется мониторинг статуса ввода в C2C-диалоге через прослушивание `typingStatus`.

```
TUIStore.watch(StoreName.CHAT, {  typingStatus: (status: boolean) => {    typingStatus.value = status;    switch (typingStatus.value) {      case true:        currentConversationName.value = "Ввод...";        break;      case false:        currentConversationName.value =          currentConversation?.value?.getShowName();        break;    }  },});
```

## Часто задаваемые вопросы

### Почему нет указания на ввод текста от другой стороны после включения переключателя? Каковы правила отображения "Ввод..."?

1. Включите переключатель "Ввод..." (он включен по умолчанию)
2. В текущем C2C-диалоге, если другой пользователь отправил вам сообщение в течение последних 30 секунд и в данный момент вводит текст.

## Свяжитесь с нами

Присоединитесь к [технической группе обмена Telegram](https://t.me/tencent_imsdk) или [группе обсуждения WhatsApp](https://chat.whatsapp.com/IVa11ZkVmKTEwSWsAzSyik), получите поддержку от профессиональных инженеров и решите ваши сложные задачи.


---
*Источник: [https://trtc.io/document/58663](https://trtc.io/document/58663)*

---
*Источник (EN): [typing-status.md](./typing-status.md)*

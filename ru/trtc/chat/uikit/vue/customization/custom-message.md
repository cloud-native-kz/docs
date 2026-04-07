# Пользовательское сообщение

TUIKit реализует отправку и отображение основных типов сообщений, таких как текстовые, изображения, аудио, видео и файловые сообщения, по умолчанию. Если эти типы сообщений не соответствуют вашим требованиям, вы можете добавить пользовательские типы сообщений.

## Основные типы сообщений

| Тип сообщения | Отображение |
| --- | --- |
| Текстовое сообщение | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fcf03273b12e11ee9939525400461a83.png) |
| Сообщение с изображением | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ac20bec2b44611eeae9a525400c26da5.png) |
| Аудиосообщение | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/89ca08d4b44711eeae9a525400c26da5.png) |
| Видеосообщение | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0705b39cb12f11eeb2a1525400170219.png) |
| Файловое сообщение | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0afe02b6b12f11ee9fd6525400bb593a.png) |

## Пользовательское сообщение

Если основные типы сообщений не соответствуют вашим требованиям, вы можете настроить сообщения в соответствии с фактическими бизнес-потребностями.

TUIKit включает несколько встроенных стилей пользовательских сообщений, как показано на следующем рисунке:

| Предустановленные стили пользовательских сообщений | Отображение |
| --- | --- |
| Гипертекстовое сообщение | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/977385f2b44211eeae9a525400c26da5.png) |
| Сообщение об оценке | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6b385bbab34d11eeae9a525400c26da5.png) |
| Сообщение о заказе | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/34180b8eb44211eeb2a1525400170219.png) |

Далее на примере отправки пользовательского гипертекстового сообщения, которое может перенаправлять в браузер, помогает вам быстро понять процесс реализации.

## Отображение пользовательского сообщения

Элемент ячейки пользовательского гипертекстового сообщения (XML), встроенный в TUIKit, изображён на рисунке ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3df05402b44611ee9fd6525400bb593a.png)

Пользовательские сообщения и другие распространённые типы сообщений принимаются одинаковым образом; все типы сообщений отслеживаются для доступа через `TUIStore.watch(StoreName.CHAT, { messageList: onMessageListUpdated })`.
Полученные пользовательские сообщения представляются в списке сообщений в различных формах в соответствии с их соответствующими полями типа.
Далее будет объяснено, как отображать пользовательские сообщения.

### Создание структуры отображения для пользовательского сообщения

Отображение пользовательских сообщений осуществляется в основном путём отрисовки `messageCustom` в области содержимого типа пользовательского сообщения `messageBubble`.
Вы можете добавить структуру отображения стиля, которая вам нужна для пользовательских сообщений, в файл `src/TUIKit/components/TUIChat/message-list/message-elements/message-custom.vue`.
Например, следующий код демонстрирует структуру отображения для гипертекстового сообщения:

```
<template v-else-if="isCustom.businessID === 'text_link'">  <div class="textLink">    <p>{{ isCustom.text }}</p>    <a :href="isCustom.link" target="view_window">      {{        TUITranslateService.t("message.custom.peekDetails>>")      }}    </a>  </div></template>
```

## Отправка пользовательских сообщений

Вы можете отправить пользовательское сообщение, вызвав метод `TUIChatService.sendCustomMessage` в логическом уровне механизма TUIKit. Подробнее см.: [SendCustomMessage](https://web.sdk.qcloud.com/im/doc/chat-engine/en/ITUIChatService.html#sendCustomMessage).

Вот несколько примеров отправки встроенных стилей пользовательских сообщений в TUIKit:

#### **sendCustomMessage(options, sendMessageOptions) → {Promise.<any>}**

**Пример 1: Отправка пользовательского сообщения об оценке**

```
import { TUIChatService } from "@tencentcloud/chat-uikit-engine";let promise = TUIChatService.sendCustomMessage({  payload: {    data: JSON.stringify({      businessID: "evaluation",      version: 1,      score: 5,      comment: "so pretty!!!"    }),    description: "Evaluation of this service",    extension: "Evaluation of this service"  }});promise.catch((error) => {   ...});
```

**Пример 2: Отправка пользовательского гипертекстового сообщения**

```
import { TUIChatService } from "@tencentcloud/chat-uikit-engine";let promise = TUIChatService.sendCustomMessage({  payload: {    data: JSON.stringify({      businessID: "text_link",      text: "Welcome to Chat. Let's chat!",      link: "https://web.sdk.qcloud.com/im/demo/intl/index.html?scene=social"    }),    description: "",    extension: ""  }});promise.catch((error) => {   ...});
```

**Пример 3: Отправка пользовательского сообщения о заказе**

```
import { TUIChatService } from "@tencentcloud/chat-uikit-engine";let promise = TUIChatService.sendCustomMessage({  payload: {    data: JSON.stringify({      businessID: "order",      title: "Chat",      description: "Standard Edition",      price: "399 USD/month",      link: "https://buy.tencentcloud.com/avc",      imageUrl: "https://1302445663.vod2.myqcloud.com/cea47bfavodsgp1302445663/fd67ff345576678022395175485/2lCqNHbz5aYA.png",    }),    description: "",    extension: ""  }});promise.catch((error) => {   ...});
```

**Описание параметров:**

| Имя | Тип | Необязательный тип | Описание |
| --- | --- | --- | --- |
| options | [SendMessageParams](https://web.sdk.qcloud.com/im/doc/chat-engine/en/SendMessageParams.html) | Обязательный | Параметры, относящиеся к пользовательским сообщениям |
| sendMessageOptions | [SendMessageOptions](https://web.sdk.qcloud.com/im/doc/chat-engine/en/SendMessageOptions.html) | Необязательный | Параметры отправки сообщения |

**Возвращаемые значения**

- `Promise.<any>`

## Свяжитесь с нами

Присоединяйтесь к [группе технического обмена Telegram](https://t.me/tencent_imsdk) или [группе обсуждения WhatsApp](https://chat.whatsapp.com/IVa11ZkVmKTEwSWsAzSyik), воспользуйтесь поддержкой профессиональных инженеров и решите ваши самые сложные задачи.


---
*Источник: [https://trtc.io/document/50042](https://trtc.io/document/50042)*

---
*Источник (EN): [custom-message.md](./custom-message.md)*

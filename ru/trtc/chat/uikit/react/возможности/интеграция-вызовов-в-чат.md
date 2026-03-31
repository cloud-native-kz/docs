# Интеграция вызовов в чат

TUICallKit — это компонент UI для аудио и видеовызовов, запущенный Tencent Cloud. Интегрировав этот компонент, вы сможете использовать функцию аудио и видеовызовов в приложении чата всего с несколькими строками кода.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e21dfd61765d11ef8829525400fdb830.png)

- React версии 18+ (версии 17.x не поддерживаются)
- TypeScript
- [Node.js](https://nodejs.org/en/) версии 16+
- npm (используйте версию, соответствующую используемой версии Node)

## Шаг 1: Включение возможности аудио и видеовызовов

Прежде чем использовать услуги аудио и видео, предоставляемые Tencent Cloud, вам необходимо перейти в консоль и включить услуги аудио и видео для вашего приложения. Подробные инструкции см. в разделе [Активация сервиса.](https://www.tencentcloud.com/document/product/647/59832)

## Шаг 2: Загрузка компонента TUICallKit

Загрузите компонент `TUICallKit` через [npm](https://www.npmjs.com/package/@tencentcloud/chat-uikit-vue), версия 3.3.6 и выше:

```
npm i @tencentcloud/call-uikit-react
```

## Шаг 3: Импорт и вызов компонента TUICallKit

- Вам нужно добавить всего две строки кода, чтобы использовать функцию вызовов. Импортируйте `TUICallKit` и вызовите компонент `TUICallKit`.
- В компоненте `<ChatHeader />` включите Call, отображение значка и установите `enableCall` в `true`.

> **Примечание:** Если вы еще не интегрировали TUIKit, следуйте документации [Интеграция TUIKit](https://www.tencentcloud.com/document/product/1047/50055?lang=en&pg=) для первоначальной интеграции TUIKit. Версия TUIKit должна быть обновлена до v2.2.7 или выше. Компонент TUICallKit позволяет добавлять стили для управления позицией, шириной и высотой TUICallKit.

```
// Импорт TUICallKitimport { TUICallKit } from '@tencentcloud/call-uikit-react';
```

```
// Если вы отображаете на ПК, добавьте стили для инициализации позиции TUICallKit. Для отображения на H5 это не требуетсяconst callStyle: React.CSSProperties = {  position: 'fixed',  top: '50%',  left: '50%',  zIndex: '999',  transform: 'translate(-50%, -50%)',};
```

```
// Пожалуйста, используйте компонент TUICallKit внутри UIKitProviderreturn (  <div style={{display: 'flex', height: '100vh'}}>    <UIKitProvider language={"en-US"}>      <TUICallKit style={callStyle} />       <div style={{maxWidth: '400px'}}>         <Profile />         <ConversationList />      </div>      <Chat>        <ChatHeader enableCall={true}/>         <MessageList />        <MessageInput />      </Chat>      <ChatSetting />    </UIKitProvider>  </div>);
```

## Шаг 4: Запуск проекта

```
 npm run start
```

## Шаг 5: Совершите свой первый вызов

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e218ec5b765d11ef82535254002693fd.png)

## Часто задаваемые вопросы

#### Как отключить функцию аудио/видеовызовов?

- Чтобы отключить кнопку аудио/видеовызова, установите атрибут `enableCall` в `false` в компоненте `<ChatHeader />`. Если `enableCall` не указан, по умолчанию используется значение `false`.

```
return (  <div style={{display: 'flex', height: '100vh'}}>    <UIKitProvider language={"en-US"}>      <TUICallKit style={callStyle} />      <div style={{maxWidth: '400px'}}>         <Profile />         <ConversationList />      </div>      <Chat>        <ChatHeader enableCall={false}/>         <MessageList />        <MessageInput />      </Chat>      <ChatSetting />    </UIKitProvider>  </div>);
```

### Как приобрести пакет?

Пожалуйста, обратитесь к ссылке на покупку для [приобретения официальной версии](https://www.tencentcloud.com/document/product/1047/34577).

## Техническая консультация

Если вам что-то нужно или у вас есть отзывы, вы можете связаться со следующими контактами: info_rtc@tencent.com. Или присоединитесь к [технической группе Telegram](https://t.me/tencent_imsdk) или [группе WhatsApp](https://chat.whatsapp.com/IVa11ZkVmKTEwSWsAzSyik) для получения поддержки от профессиональных инженеров в решении ваших проблем.


---
*Источник: [https://trtc.io/document/64468](https://trtc.io/document/64468)*

---
*Источник (EN): [calls-integration-to-chat.md](./calls-integration-to-chat.md)*

# Прочитанные квитанции

## Обзор

Компонент React MessageList поддерживает функцию уведомления о прочтении, определяя, было ли одно сообщение прочитано адресатом в персональных чатах. В групповых чатах он независимо определяет, было ли отдельное сообщение прочитано членом группы.

## Отображение эффекта

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a64f6ccc61f511f0ad0f5254005ef0f7.png)

## Использование

React UIKit предоставляет компонент MessageList. Установка свойства `enableReadReceipt` в значение `true` в компоненте MessageList включает функцию уведомления о прочтении (если оставить пустым, значение по умолчанию — false).

```
import {  Chat,  ChatHeader,  ConversationList,  MessageInput,  MessageList,} from '@tencentcloud/chat-uikit-react';function App() {  return (    <UIKitProvider>      <div style={{ display: 'flex', height: '100vh' }}>        <ConversationList style={{ minWidth: '30%' }} />        <Chat>          <ChatHeader />          // Enable read receipt          <MessageList enableReadReceipt={true} />          <MessageInput />        </Chat>      </div>    </UIKitProvider>  );}export default App;
```


---
*Источник: [https://trtc.io/document/72001](https://trtc.io/document/72001)*

---
*Источник (EN): [read-receipt.md](./read-receipt.md)*

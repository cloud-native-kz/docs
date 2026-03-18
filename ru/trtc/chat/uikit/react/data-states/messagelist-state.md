# MessageList State

## Обзор MessageListState

`MessageListState` — это центр управления статусом, связанный с построением списков сообщений, специализирующийся на управлении статусом и операциями над списком сообщений. Он предоставляет основные функции, такие как управление данными списка сообщений, загрузка по страницам, параметры уведомлений о прочтении и управление прокруткой, что делает его важным инструментом для построения интерфейса чата.

`MessageListState` использует реактивный дизайн, может автоматически прослушивать изменения базовых данных и обновлять статус компонента, а также предоставляет различные методы бизнес-операций для удовлетворения разных сценариев использования.

## Когда использовать MessageListState

Когда текущая емкость MessageList не соответствует требованиям, или если вы хотите переразработать MessageList с помощью базовых данных, вы можете использовать `useMessageListState()` для получения исходного источника данных и выполнить переразработку.

## Список атрибутов

| Поле | Тип | Описание |
| --- | --- | --- |
| messageList | readonly MessageModel[] \| undefined | Данные списка сообщений |
| hasMoreOlderMessage | boolean \| undefined | Можно ли загрузить больше исторических сообщений |
| enableReadReceipt | boolean \| undefined | Включена ли функция уведомлений о прочтении |
| isDisableScroll | boolean | Отключить прокрутку |
| setIsDisableScroll | (isDisableScroll: boolean) => void | Метод установки статуса прокрутки |
| loadMoreMessage | () => Promise<any> | Метод для загрузки большего количества сообщений |
| setEnableReadReceipt | (enableReadReceipt: boolean \| undefined) => void | Метод установки статуса уведомлений о прочтении |

## Подробное описание атрибутов

### messageList

- **Тип**: `readonly MessageModel[] | undefined`
- **Описание**: Данные списка сообщений текущего сеанса. Это доступный только для чтения массив, содержащий все загруженные объекты сообщений. Каждый объект сообщения содержит полную информацию, такую как содержание сообщения, отправитель, временная метка и статус. Когда базовые данные не полностью загружены, значение равно `undefined`.

### hasMoreOlderMessage

- **Тип**: `boolean | undefined`
- **Описание**: Указывает, есть ли больше исторических сообщений для загрузки. Когда значение равно `true`, это означает, что более ранние сообщения можно получить через метод `loadMoreMessage`; когда значение равно `false`, это означает, что все исторические сообщения уже загружены; когда значение равно `undefined`, это означает, что статус загрузки не определен.

### enableReadReceipt

- **Тип**: `boolean | undefined`
- **Описание**: Контролирует, включена ли функция уведомлений о прочтении. Если установлено значение `true`, сообщение будет отображать статус прочтения; если установлено значение `false`, статус прочтения не будет показан; когда значение равно `undefined`, это означает, что пользователь не указал, включить ли уведомления о прочтении.

### isDisableScroll

- **Тип**: `boolean`
- **Описание**: Контролирует поведение прокрутки списка сообщений. Если установлено значение `true`, отключается функция автоматической прокрутки; если установлено значение `false`, разрешается нормальная прокрутка. Обычно установляется значение `true` при ручной прокрутке пользователем исторических сообщений, чтобы избежать того, чтобы автоматическая прокрутка влияла на пользовательский опыт при поступлении новых сообщений. Установка этого поля не отключает прокрутку страницы. Пожалуйста, используйте это поле для управления на стороне DOM.

### setIsDisableScroll

- **Тип**: `(isDisableScroll: boolean) => void`
- **Описание**: Метод, используемый для установки статуса прокрутки. Принимает логический параметр для управления тем, следует ли отключить функцию прокрутки.

### loadMoreMessage

- **Тип**: `() => Promise<any>`
- **Описание**: Метод асинхронной загрузки большего количества исторических сообщений. Вызов этого метода отправляет запрос на сервер для получения данных более ранних сообщений и автоматически обновляет статус `messageList` и `hasMoreOlderMessage`.

### setEnableReadReceipt

- **Тип**: `(enableReadReceipt: boolean | undefined) => void`
- **Описание**: Метод, используемый для установки переключателя функции уведомлений о прочтении. Принимает логическое значение или параметр `undefined` для управления включением уведомлений о прочтении.

## Примеры использования

Вот полный пример компонента MessageList, который показывает, как использовать `messageList`, `hasMoreOlderMessage` и `loadMoreMessage` для построения списка сообщений с загрузкой по страницам:

```
import React, { useEffect, useRef, useState } from 'react';import { useMessageListState } from '@tencentcloud/chat-uikit-react';import type { MessageModel } from '@tencentcloud/chat-uikit-react';import './MessageList.scss';interface MessageListProps {  className?: string;}const MessageList: React.FC<MessageListProps> = ({ className }) => {  const {    messageList,    hasMoreOlderMessage,    loadMoreMessage,    isDisableScroll,    setIsDisableScroll,  } = useMessageListState();  const [isLoading, setIsLoading] = useState(false);  const messageListRef = useRef<HTMLDivElement>(null);  const prevScrollHeight = useRef<number>(0);  // load more messages  const handleLoadMore = async () => {    if (isLoading || !hasMoreOlderMessage) return;    setIsLoading(true);    try {      // Record the current scroll height      if (messageListRef.current) {        prevScrollHeight.current = messageListRef.current.scrollHeight;      }      await loadMoreMessage();    } catch (error) {      console.error('Failed to load more messages:', error);    } finally {      setIsLoading(false);    }  };  // Handle scroll event  const handleScroll = (e: React.UIEvent<HTMLDivElement>) => {    const target = e.target as HTMLDivElement;    const { scrollTop, scrollHeight, clientHeight } = target;    // Detect whether scrolled to top, trigger loading more    if (scrollTop === 0 && hasMoreOlderMessage && !isLoading) {      handleLoadMore();    }    // detect whether users are viewing historical message    const isAtBottom = scrollTop + clientHeight >= scrollHeight - 10;    setIsDisableScroll(!isAtBottom);  };  // Keep scroll position (after loading more messages)  useEffect(() => {    if (messageListRef.current && prevScrollHeight.current > 0) {      const newScrollHeight = messageListRef.current.scrollHeight;      const scrollDiff = newScrollHeight - prevScrollHeight.current;      messageListRef.current.scrollTop = scrollDiff;      prevScrollHeight.current = 0;    }  }, [messageList]);  // Auto-scroll to bottom (on message arrival)  useEffect(() => {    if (messageListRef.current && !isDisableScroll) {      messageListRef.current.scrollTop = messageListRef.current.scrollHeight;    }  }, [messageList, isDisableScroll]);  // Render a single message  const renderMessage = (message: MessageModel) => (    <div key={message.ID} className="message-item">      <div className="message-sender">{message.nick || message.from}</div>      <div className="message-content">        {          (() => {            if (message.type === 'TIMTextElem') {              return  <span className="text-message">{message.payload.text}</span>;            } else {              return <span>other message</span>;            }          })()        }      </div>      <div className="message-time">        {new Date(message.time * 1000).toLocaleTimeString()}      </div>    </div>  );  return (    <div className={`im-message-list-container ${className || ''}`}>      {/* load more indicator */}      {hasMoreOlderMessage && (        <div className="load-more-indicator">          {isLoading ? (            <div className="loading">loading...</div>          ) : (            <button onClick={handleLoadMore} className="load-more-btn">              load more messages            </button>          )}        </div>      )}      {/* message list */}      <div        ref={messageListRef}        className="message-list"        onScroll={handleScroll}      >        {messageList?.map(renderMessage)}      </div>      {/* empty state */}      {messageList?.length === 0 && (        <div className="empty-state">          No Messages        </div>      )}    </div>  );};export default MessageList;
```

### Справка по стилям

```
.im-message-list-container {  display: flex;  flex-direction: column;  flex: 1 1 auto;  overflow: auto hidden;    .load-more-indicator {    padding: 10px;    text-align: center;    border-bottom: 1px solid #eee;        .loading {      color: #666;      font-size: 14px;    }        .load-more-btn {      padding: 8px 16px;      background: #007bff;      color: white;      border: none;      border-radius: 4px;      cursor: pointer;            &:hover {        background: #0056b3;      }    }  }    .message-list {    flex: 1;    overflow-y: auto;    min-height: 0;    padding: 10px;        .message-item {      margin-bottom: 15px;      padding: 10px;      background: #f5f5f5;      border-radius: 8px;            .message-sender {        font-weight: bold;        color: #333;        margin-bottom: 5px;      }            .message-content {        color: #666;        line-height: 1.5;        margin-bottom: 5px;      }            .message-time {        font-size: 12px;        color: #999;        text-align: right;      }    }  }    .empty-state {    flex: 1;    display: flex;    align-items: center;    justify-content: center;    color: #999;    font-size: 14px;  }}
```

В этом примере показано, как:

1. Использовать `messageList` для отрисовки списка сообщений.
2. Определить, следует ли отображать кнопку загрузки дополнительных сообщений через `hasMoreOlderMessage`.
3. Вызвать `loadMoreMessage` для загрузки по страницам.
4. Комбинировать `isDisableScroll` и `setIsDisableScroll` для оптимизации опыта прокрутки.
5. Обрабатывать отображение состояния загрузки и пустого состояния.


---
*Источник: [https://trtc.io/document/72086](https://trtc.io/document/72086)*

---
*Источник (EN): [messagelist-state.md](./messagelist-state.md)*

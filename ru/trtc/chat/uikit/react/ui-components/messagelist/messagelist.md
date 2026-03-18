# MessageList

## Обзор компонента

MessageList — это мощный компонент списка сообщений чата, предоставляющий полное отображение сообщений, взаимодействие и пользовательские функции. Он поддерживает основные функции чата, такие как агрегация сообщений, квитанции доставки, операции с сообщениями и управление прокруткой, а также предлагает различные параметры персонализации для удовлетворения различных бизнес-потребностей.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7c3b8073617111f097ec52540044a08e.png)

## Свойства Props

| Поле | Тип | Значение по умолчанию | Описание |
| --- | --- | --- | --- |
| [alignment](#bb86a868-3c04-4a23-a55d-41434f0eb6b0) | 'left' \| 'right' \| 'two-sided' | 'two-sided' | Режим выравнивания сообщений. Left: выравнивание всех сообщений влево. Right: выравнивание всех сообщений вправо. two-sided: отправленные сообщения выравниваются вправо, полученные сообщения выравниваются влево. |
| [enableReadReceipt](#74454dca-9a23-4c52-8182-089dc4287c05) | boolean | false | Включение функции квитанции доставки. |
| [messageActionList](#8467b7d4-9519-4bf2-b932-726db7b78ff6) | IMessageAction[] | undefined | Пользовательский список операций сообщений, такие как копирование, отзыв, удаление. |
| [messageAggregationTime](#aea3b710-1bc0-4c49-bc63-e5328a5b2631) | number | 300 | Интервал агрегации сообщений (секунды). Последовательные сообщения от одного отправителя в течение этого периода будут агрегированы и отображены. |
| [filter](#15a53ab6-197e-48af-aab6-c08231344b93) | (message: IMessageModel) => boolean | undefined | Функция фильтрации сообщений для управления тем, какие сообщения отображать. |
| [className](#425502cf-5987-415f-85cd-807c82cfec6d) | string | undefined | Имя пользовательского CSS класса. |
| [style](https://www.tencentcloud.com/document/product/1047/72084#cda58725-6b80-455d-84a2-e69a7b758f09) | React.CSSProperties | undefined | Пользовательский встроенный стиль. |
| [Message](#5a133d44-be95-424a-926e-8214994872dc) | React.ComponentType | Message | Пользовательский компонент сообщения. |
| [MessageTimeDivider](#d5ff2021-e852-4210-9040-0f882c5d6d4a) | React.ComponentType | MessageTimeDivider | Пользовательский компонент разделителя времени. |

## Объяснение свойств

### alignment

Тип параметра: `'left' | 'right' | 'two-sided'`

alignment используется для установки режима выравнивания сообщений, поддерживая три режима: `left`, `right` и `two-sided`. Значение по умолчанию — `'two-sided'`.

- `two-sided`: сообщения от других выравниваются влево, ваши сообщения выравниваются вправо.
- `left`: все сообщения выравниваются влево.
- `right`: все сообщения выравниваются вправо.

### enableReadReceipt

Тип параметра: `boolean`

enableReadReceipt используется для установки, включена ли функция квитанции доставки сообщения. Значение по умолчанию: `false`.

### messageActionList

Тип параметра: `IMessageAction[]`

messageActionList используется для установки списка операций с сообщениями, таких как копирование, отзыв, удаление. Значение по умолчанию — полный список операций с сообщениями `['copy', 'recall', 'quote', 'forward', 'delete']`.

```
interface IMessageAction {  key: 'copy' | 'recall' | 'quote' | 'forward' | 'delete' | string;  label?: string;  icon?: React.ReactNode;  onClick?: (message: IMessageModel) => void;  visible?: ((message: IMessageModel) => boolean) | boolean;  component?: React.ComponentType<{ message: IMessageModel }>;  style?: React.CSSProperties;}
```

`useMessageAction` можно использовать для получения полного списка операций с сообщениями, а затем настроить его по мере необходимости.

#### Пример 1: Изменение порядка списка операций сообщений

Предположим, что список операций сообщений отображается в порядке `forward`, `copy`, `recall`, `quote`, `delete`.

```
import { Chat, MessageList, useMessageActions } from '@tencentcloud/chat-uikit-react';const App = () => {  const actions = useMessageActions(['forward', 'copy', 'recall', 'quote', 'delete']);  return (    <Chat>      <MessageList messageActionList={actions} />    </Chat>  );}
```

#### Пример 2: Отображение только некоторых операций сообщений

Предположим, что показываются только операции `forward`, `copy` и `recall`.

```
import { Chat, MessageList, useMessageActions } from '@tencentcloud/chat-uikit-react';const App = () => {  const actions = useMessageActions(['forward', 'copy', 'recall']);  return (    <Chat>      <MessageList messageActionList={actions} />    </Chat>  );}
```

#### Пример 3: Изменение существующих операций сообщений

Вот пример пользовательской операции отзыва:

1. Изменить ярлык на 'Recall ⏮️'
2. Изменить цвет на оранжевый
3. Отозвать можно только текстовые сообщения
4. Ключ должен совпадать с исходной операцией, используйте `recall`

```
import TUIChatEngine from '@tencentcloud/chat-uikit-engine';import { Chat, MessageList, useMessageActions } from '@tencentcloud/chat-uikit-react';const ChatApp = () => {  const actions = useMessageActions(['copy', {    key: 'recall',    label: 'Recall ⏮️',    style: {      color: 'orange'    },    visible: (message) => message.type === TUIChatEngine.TYPES.MSG_TEXT,  }, 'quote', 'forward', 'delete']);  return (    <Chat>      <MessageList messageActionList={actions} />    </Chat>  );}
```

Эффект показан ниже.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7c235d22617111f0bac1525400454e06.png)

#### Пример 4: Добавление новых пользовательских операций сообщений

Если требуются пользовательские операции сообщений, например, только сообщения, отправленные другими, могут быть помечены как 'like' и вставлены после операции 'recall'.

```
import { useMessageAction } from '@tencentcloud/chat-uikit-react';import { yourApi } from '@/api/yourApi';const customActions = {  key: 'like',  label: 'Like',  icon: <span>👍</span>,  style: {    color: '#E53888',  },  visible: (message) => message.flow === 'in',  onClick: (message) => {    yourApi.likeMessage(message.ID);  }}function ChatApp() {  const actions = useMessageAction(['forward', 'copy', 'recall', customActions, 'quote', 'delete']);  return <MessageList messageActionList={actions} />;}
```

Эффект показан ниже.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7c2f4eb5617111f092fe525400bf7822.png)

### messageAggregationTime

Тип параметра: `number`

messageAggregationTime используется для установки интервала агрегации сообщений, агрегируя последовательные сообщения от одного отправителя для отображения. Значение по умолчанию: `300` (секунды).

### filter

Тип параметра: `(message: IMessageModel) => boolean`

filter используется для установки функции фильтрации сообщений для управления тем, какие сообщения отображать. Значение по умолчанию: `undefined`.

#### Пример: Фильтрация сообщений об ошибках, отправленных ботами

```
import { MessageList } from '@/components/MessageList';import TUIChatEngine from '@tencentcloud/chat-uikit-engine';const messageFilter = (message) => {  // Фильтрация текстовых сообщений, где псевдоним отправителя содержит '_robot' и содержание включает 'operation-failed'  if (    message.nick?.includes('_robot')     && message.type === TUIChatEngine.TYPES.MSG_TEXT    && message.payload?.text?.includes('operation-failed')  ) {    return false;  }  return true;};function ChatApp() {  return <MessageList filter={messageFilter} />;}
```

### className

Тип параметра: `string`

className используется для установки имени пользовательского CSS класса корневого контейнера, значение по умолчанию `undefined`.

### style

Тип параметра: `React.CSSProperties`

style используется для установки пользовательского встроенного стиля корневого контейнера, значение по умолчанию `undefined`.

### Message

Тип параметра: `React.ComponentType`

Message используется для установки пользовательского компонента сообщения, замены компонента отображения сообщения по умолчанию, значение по умолчанию встроенный компонент `Message`.

#### Пример: Пользовательский компонент сообщения с перенаправлением при клике на CUSTOM сообщение

```
import TUIChatEngine from '@tencentcloud/chat-uikit-engine';import { Chat, MessageList, Message } from '@tencentcloud/chat-uikit-react';function CustomMessage(props) {  const { message } = props;  if (message.type === TUIChatEngine.TYPES.MSG_CUSTOM) {    const { businessID, ...restData } = JSON.parse(message.payload.data);    if (businessID === 'text_link') {      return (        <div>          <div>{restData.text}</div>          <a href={restData.link}>            перенаправить на общедоступный адрес веб-сайта {restData.link}          </a>        </div>      );    }  } else {    // Используйте компонент сообщения по умолчанию для других типов сообщений    return <Message {...props} />;  }}function ChatApp() {  return (    <Chat>      <MessageList Message={CustomMessage} />    </Chat>  );}
```

### MessageTimeDivider

Тип параметра: `React.ComponentType`

MessageTimeDivider используется для установки пользовательского компонента разделителя времени, значение по умолчанию встроенный компонент `MessageTimeDivider`.

#### Пример: Разделитель времени для рабочих часов

```
import { Chat, MessageList, MessageTimeDivider } from '@tencentcloud/chat-uikit-react';const BusinessTimeDivider = (props: React.ComponentProps<typeof MessageTimeDivider>) => {  const { prevMessage, currentMessage } = props;  if (!prevMessage || !currentMessage) return null;    // Для каждого сообщения, которое будет отображаться, получите время текущего сообщения и предыдущего сообщения, преобразуйте их в объекты даты и определите, пересекают ли они день или превышают 4-часовой интервал  const currentTime = new Date(currentMessage.time * 1000);  const prevTime = new Date(prevMessage.time * 1000);    // Отображение только при переходе дня или при превышении 4-часового интервала  const shouldShow = currentTime.toDateString() !== prevTime.toDateString() ||                    (currentTime.getTime() - prevTime.getTime()) > 4 * 60 * 60 * 1000;    if (!shouldShow) return null;    // Проверка рабочего времени (9:00-18:00, понедельник-пятница)  const isWorkingTime = () => {    const hour = currentTime.getHours();    const day = currentTime.getDay();    return day >= 1 && day <= 5 && hour >= 9 && hour <= 18;  };    const timeLabel = isWorkingTime() ? 'рабочие часы' : 'нерабочее время';  const timeColor = isWorkingTime() ? '#52c41a' : '#faad14';    return (    <div style={{ textAlign: 'center', margin: '16px 0' }}>      <span style={{        backgroundColor: timeColor,        color: 'white',        padding: '2px 8px',        borderRadius: '12px',        marginRight: '8px'      }}>        {timeLabel}      </span>      {currentTime.toLocaleString()}    </div>  );};function ChatApp() {  return (    <Chat>      <MessageList MessageTimeDivider={BusinessTimeDivider} />    </Chat>  );}
```

Эффект показан ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7c2ac958617111f091585254001c06ec.png)

## Итоговое резюме

Компонент MessageList предоставляет полную функциональность списка сообщений и различные параметры персонализации. Правильно настроив Props и персонализировав компоненты, вы можете создать интерфейс чата, соответствующий бизнес-требованиям. Рекомендуется выбирать соответствующую конфигурацию в зависимости от конкретного сценария при фактическом использовании.


---
*Источник: [https://trtc.io/document/72085](https://trtc.io/document/72085)*

---
*Источник (EN): [messagelist.md](./messagelist.md)*

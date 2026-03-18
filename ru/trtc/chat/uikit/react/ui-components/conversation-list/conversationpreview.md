# ConversationPreview

`ConversationPreview` используется для предпросмотра содержимого сеанса в списке. Компонент отображает информацию о сеансе, счетчик непрочитанных сообщений и предоставляет функцию действий с беседой.

С помощью атомарных компонентов отображения информации вы можете свободно проектировать и комбинировать желаемый макет `ConversationPreview`.

Кроме того, вы можете использовать функцию `onConversationSelect` для определения поведения при выборе сеанса.

### Базовое использование

Вы можете использовать свойство `Preview` компонента `ConversationList` для настройки элемента предпросмотра для каждой отдельной беседы в списке. Если свойство `Preview` не указано, система автоматически примет компонент `ConversationPreviewUI` в качестве значения по умолчанию.

```
import { ConversationList, ConversationPreviewUI } from '@tencentcloud/chat-uikit-react';import type { ConversationPreviewUIProps } from '@tencentcloud/chat-uikit-react';const CustomConversationPreview = (props: ConversationPreviewUIProps) => {  const { Title } = props;  return (    <ConversationPreviewUI {...props}>      {Title}      <div>Your custom preview UI</div>    </ConversationPreviewUI>  );};<ConversationList Preview={CustomConversationPreviewUI}></ConversationList>
```

### Props

| **Имя параметра** | **Тип** | **Значение по умолчанию** | **Описание** |
| --- | --- | --- | --- |
| **conversation*****(Обязательно)*** | ConversationModel | - | Обязательный параметр, указывающий текущий элемент списка беседы для отображения. |
| isSelected | Boolean | false | Управляет выбранным статусом пользовательского интерфейса элемента списка беседы. |
| enableActions | Boolean | true | Управляет отображением функции операции беседы. |
| actionsConfig | [ConversationActionsConfig](https://www.tencentcloud.com/document/product/1047/64707#4cc59d08-632e-4817-a124-cf1fcb8de3c3) | - | Для пользовательской конфигурации операции сеанса. |
| highlightMatchString | String | - | Выделение совпадающих ключевых слов в заголовке элемента списка беседы, обычно используется для результатов поиска беседы. |
| Title | `String ï½ JSX.Element` | ConversationPreviewTitle | Отображение области заголовка элемента списка беседы. |
| LastMessageAbstract | `String ï½ JSX.Element` | ConversationPreviewAbstract | Отображение области тезиса последнего сообщения элемента списка беседы. |
| LastMessageTimestamp | `String ï½ JSX.Element` | ConversationPreviewTimestamp | Отображение области временной метки последнего сообщения элемента списка беседы. |
| Unread | `String ï½ JSX.Element` | ConversationPreviewUnread | Отображение области индикатора непрочитанных сообщений элемента списка беседы. |
| ConversationActions | `ReactElement` | ConversationActions | Отображение области операций беседы элемента списка беседы. |
| Avatar | ReactElement | Avatar | Отображение области аватара элемента списка беседы. |
| onConversationSelect | (conversation: ConversationModel) => void; | - | Укажите атрибуты для получения обратного вызова при выборе беседы в списке бесед. |
| className | String | - | Установите пользовательское имя класса CSS для корневого элемента. |
| style | React.CSSProperties | - | Установите пользовательские стили для корневого элемента. |

## Пример пользовательской настройки

### Стиль в стиле Discord

Discord — это популярное приложение для чатов, похожее на Skype или Telegram. Содержимое сообщений в Discord выглядит следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/656b6c8c5e3011f0b30d5254007c27c5.png)

Путем настройки макета, функций и стиля `ConversationPreview`, мы можем быстро достичь эффекта, похожего на Discord.

React

CSS

1. Настройте `ConversationListPreview`
2. Переключитесь на темный режим

```
import { UIKitProvider, ConversationList, ConversationPreviewUI } from '@tencentcloud/chat-uikit-react';import type { ConversationPreviewUIProps } from '@tencentcloud/chat-uikit-react';const CustomConversationPreview = (props: ConversationPreviewUIProps) => {  const { Title } = props;  return (    <ConversationPreviewUI {...props}>      <span> # </span>      <span>{Title}</span>    </ConversationPreviewUI>  );};const App = () => {    <UIKitProvider theme={'dark'}>      <ConversationList         style={{ maxWidth: '300px', height: '600px' }}         Preview={CustomConversationPreviewUI}       />      ...    </UIKitProvider>}
```

```
.custom-preview-ui {  height: 34px;  border-radius: 6px;  padding: 10px;  margin: 0 10px;  .custom-preview-ui__tag {    margin-right: 10px;    font-size: 16px;    color: #b3b3b4;  }  .custom-preview-ui__title {    font-size: 14px;    color: #b3b3b4;  }  &.uikit-conversation-preview--active {    background-color: #3b3d43;    .custom-preview-ui__tag {      color: #ffffff;    }    .custom-preview-ui__title {      .uikit-conversation-preview__title {        color: #ffffff;      }    }  }}
```

Эффект `ConversationListPreview` после настройки выглядит следующим образом:

| **Перед изменением** | **После изменения** |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6545c5575e3011f091585254001c06ec.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6544f8a25e3011f0bac1525400454e06.png) |

###


---
*Источник: [https://trtc.io/document/64705](https://trtc.io/document/64705)*

---
*Источник (EN): [conversationpreview.md](./conversationpreview.md)*

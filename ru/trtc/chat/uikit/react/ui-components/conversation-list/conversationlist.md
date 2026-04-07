# ConversationList

`ConversationList` в первую очередь отвечает за функцию List. Он содержит часть Header и часть List и имеет такие функции, как поиск сеанса, создание сеанса, закрепление сеанса и удаление беседы.

В этом документе подробно описаны базовое использование, настройка, свободное объединение компонентов и список параметров свойств.

| **Список сеансов** | **Операции с сеансом** | **Поиск беседы** | **Создание сеанса** |
| --- | --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/74642fd95e3211f091585254001c06ec.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/746758725e3211f092fe525400bf7822.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/74592b105e3211f0b324525400e889b2.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/747058dc5e3211f0b324525400e889b2.png) |

## Базовое использование

Компонент `ConversationList` не имеет обязательных свойств. Вы можете использовать `ConversationList` через следующий код.

```
import { UIKitProvider, ConversationList } from '@tencentcloud/chat-uikit-react';const App = () => {  return (    <UIKitProvider>      <ConversationList />    </UIKitProvider>  );};
```

## Настройка компонента

`ConversationList` предоставляет пользовательский многомерный API Props, позволяя пользователям настраивать функции, интерфейс, модули и многое другое.

`ConversationList` предоставляет несколько заменяемых подкомпонентов, позволяя пользователям настраивать `Header`, `List`, `ConversationPreview`, `ConversationCreate`, `ConversationSearch`, `ConversationActions`, `Avatar`, `Placeholder` и другие. При этом пользователи также могут использовать компоненты по умолчанию для вторичной разработки и настройки.

### Переключение базовых функций

Установив параметры `enableSearch`, `enableCreate` и `enableActions`, вы можете гибко управлять отображением функций поиска беседы, создания сеанса и действий с беседой в `ConversationList`.

```
<ConversationList enableSearch={false} />
```

```
<ConversationList enableCreate={false} />
```

```
<ConversationList enableActions={false} />
```

| `enableSearch={false}` | `enableCreate={false}` | `enableActions={false}` |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/74a4eca35e3211f097ec52540044a08e.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7484876b5e3211f0ad0f5254005ef0f7.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/747e33d25e3211f097ec52540044a08e.png) |

### Фильтрация и сортировка данных

Компонент ConversationList предоставляет атрибуты `filterConversation` и `sortConversation`, позволяя вам фильтровать и сортировать данные списка беседы.

#### Фильтрация беседы

Для фильтрации данных списка беседы вы можете передать функцию фильтра атрибуту `filterConversation`. Эта функция получает массив ConversationModel в качестве параметра и должна вернуть новый массив, содержащий только беседы, соответствующие вашим критериям.

Вот пример использования атрибута `filterConversation` для отображения только беседы с "непрочитанными сообщениями":

```
import { ConversationList } from '@tencentcloud/chat-uikit-react';import type { ConversationModel } from '@tencentcloud/chat-uikit-react';<ConversationList  filter={(conversationList: ConversationModel[]) =>    conversationList.filter(conversation => conversation.unreadCount > 0)}/>
```

#### Сортировка беседы

Для сортировки данных списка беседы вы можете передать функцию сортировки атрибуту `sortConversation`. Эта функция получает массив ConversationModel в качестве параметра и должна вернуть новый массив с беседой, отсортированной в соответствии с вашими критериями.

Вот пример использования свойства `sortConversation` для сортировки списка беседы в порядке убывания по "времени последнего сообщения":

```
import { ConversationList } from '@tencentcloud/chat-uikit-react';import type { ConversationModel } from '@tencentcloud/chat-uikit-react';<ConversationList  sort={(conversationList: ConversationModel[]) =>    conversationList.sort(      (a, b) => (+(b?.lastMessage?.lastTime || 0)) - (+(a?.lastMessage?.lastTime || 0)),    )}/>
```

Используя атрибуты `filter` и `sort`, вы можете эффективно фильтровать и сортировать данные списка беседы в соответствии с вашими потребностями.

### Пользовательская конфигурация ActionsConfig

Используйте [actionsConfig](https://www.tencentcloud.com/document/product/1047/64707#4cc59d08-632e-4817-a124-cf1fcb8de3c3) для управления базовой функцией ConversationActions.

Для получения дополнительной информации о настройке см. раздел [ConversationActions](https://www.tencentcloud.com/document/product/1047/64707).

```
import { ConversationList } from '@tencentcloud/chat-uikit-react';import type { ConversationModel } from '@tencentcloud/chat-uikit-react';<ConversationList  actionsConfig={{    enablePin: false,    onConversationDelete: (conversation: ConversationModel) => { console.log('Delete conversation success'); },    customConversationActions: {      'custom-actions-1': {        label: 'custom-actions',        onClick: (conversation: ConversationModel) => { console.log(conversation); },      },    },  }}/>
```

| `enablePin: false` | `enableDelete: false` | `enableMute: false` | `customConversationActions` |
| --- | --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/74a4b1275e3211f0ad0f5254005ef0f7.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/748d36085e3211f091585254001c06ec.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/74c567db5e3211f0ad0f5254005ef0f7.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/747dcfd85e3211f092fe525400bf7822.png) |

### Пользовательский заполнитель

Вы можете настроить отображение списка в разных статусах, импортировав `PlaceholderEmptyList`, `PlaceholderLoading` и `PlaceholderLoadError`.

Вот пример настройки новой `PlaceholderLoading`:

```
<ConversationList  PlaceholderEmptyList={<div>Empty List!!!</div>}/>
```

### Пользовательский Header

`ConversationListHeader` отвечает за отображение части заголовка ConversationList, выступая в качестве обертки для визуализации по умолчанию `ConversationSearch` и `ConversationCreate`. Вы можете настроить его, импортировав такие атрибуты, как left и right, и также можете настроить весь компонент.

#### Props

| **Имя параметра** | **Тип** | **Значение по умолчанию** | **Описание** |
| --- | --- | --- | --- |
| children | `ReactNode` | - | Пользовательский компонент центра заголовка списка сеансов. При использовании в `<ConversationList>` по умолчанию импортирует `<ConversationSearch>` и `<ConversationCreate>`. |
| left | `ReactElement` | - | Пользовательский компонент левой части заголовка списка сеансов. |
| right | `ReactElement` | - | Пользовательский компонент правой части заголовка списка сеансов. |
| className | `String` | - | Укажите пользовательское имя для класса CSS корневого элемента. |
| style | `React.CSSProperties` | - | Укажите пользовательский стиль для корневого элемента. |

#### Базовая настройка

Ниже приведен пример добавления новой кнопки функции на правой стороне компонента Header.

```
import {   ConversationList,  ConversationListHeader,} from '@tencentcloud/chat-uikit-react';import type { ConversationListHeaderProps } from '@tencentcloud/chat-uikit-react';const CustomConversationListHeader = (props: ConversationListHeaderProps) => {    const CustomIcon = <div>Custom Icon</div>;    return (      <ConversationListHeader {...props} right={CustomIcon} />    );};	     <ConversationList Header={CustomConversationListHeader} />
```

#### Расширенная настройка

Вот упрощенная функция группировки беседы, которая различает четыре ключевых измерения: All (Все), unread conversation (Непрочитанная беседа), one-on-one chat session (Односторонний чат) и group chat (Групповой чат). Нажав на кнопки разных групп, вы выполняете разные правила фильтрации.

| **До изменения** | **После изменения** |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/74a1c6005e3211f0bac1525400454e06.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/748025d85e3211f0ad0f5254005ef0f7.png)![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/74ae6e765e3211f0b324525400e889b2.png)![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7490a0435e3211f092fe525400bf7822.png)![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7497c74c5e3211f092fe525400bf7822.png) |

React

CSS

```
import { useState } from 'react';import TUIChatEngine from '@tencentcloud/chat-uikit-engine';import { ConversationList, UIKitProvider } from '@tencentcloud/chat-uikit-react';import type { ConversationListHeaderProps, ConversationModel } from '@tencentcloud/chat-uikit-react';const App = () => {  const [currentFilter, setCurrentFilter] = useState<string>('all');  const conversationGroupFilter: Record<string, (conversationList: ConversationModel[]) => ConversationModel[]> = {    all: (conversationList: ConversationModel[]) => conversationList,    unread: (conversationList: ConversationModel[]) => conversationList?.filter((item: ConversationModel) => item.unreadCount > 0),    c2c: (conversationList: ConversationModel[]) => conversationList?.filter((item: ConversationModel) => item.type === TUIChatEngine.TYPES.CONV_C2C),    group: (conversationList: ConversationModel[]) => conversationList?.filter((item: ConversationModel) => item.type === TUIChatEngine.TYPES.CONV_GROUP),  };  const CustomConversationListHeader = (props: IConversationListHeaderProps) => {    return (      <div className="conversation-group-wrapper">        <button className={currentFilter === 'all' ? 'btn-active' : 'btn-default'} onClick={() => setCurrentFilter('all')}>All</button>        <button className={currentFilter === 'unread' ? 'btn-active' : 'btn-default'} onClick={() => setCurrentFilter('unread')}>Unread</button>        <button className={currentFilter === 'c2c' ? 'btn-active' : 'btn-default'} onClick={() => setCurrentFilter('c2c')}>C2C</button>        <button className={currentFilter === 'group' ? 'btn-active' : 'btn-default'} onClick={() => setCurrentFilter('group')}>Group</button>      </div>    );  };  return (    <UIKitProvider>      <ConversationList        style={{ maxWidth: '300px', height: '600px' }}        Header={CustomConversationListHeader}        filter={conversationGroupFilter[currentFilter]}      />    </UIKitProvider>  );};
```

```
.conversation-group-wrapper {  display: flex;  justify-content: space-around;  align-items: center;  margin: 10px;  font-size: 14px;  .btn-default{    display: flex;    padding: 5px 10px;    border: 1px solid #b3b3b4;    color: #3b3d43;    background-color: transparent;    border-radius: 2px;  }  .btn-active{    display: flex;    padding: 5px 10px;    border: 1px solid #1c66e5;    color: #1c66e5;    background-color: transparent;    border-radius: 2px;  }}
```

### Пользовательский List

`ConversationListContent` отвечает за работу отображения основного списка в ConversationList.

По умолчанию отображает предварительно вычисленные данные отображения списка текущего сеанса из Context как оборочный слой `filteredAndSortedConversationList`.

#### Props

| **Имя параметра** | **Тип** | **Значение по умолчанию** | **Описание** |
| --- | --- | --- | --- |
| children | `ReactNode` | - | Пользовательский компонент области содержимого списка сеансов. При использовании в `<ConversationList>` по умолчанию импортирует список `<Preview>`, пройденный filteredAndSortedConversationList. |
| empty | `Boolean` | `false` | Бит идентификатора списка беседы, при использовании в `<ConversationList>` судит filteredAndSortedConversationList.length === 0 и импортирует. |
| loading | `Boolean` | `false` | Бит идентификатора загрузки списка беседы, при использовании в `<ConversationList>` использует `useConversationList()` для получения `isLoading` и импорта. |
| error | `Boolean` | `false` | Бит идентификатора ошибки загрузки списка беседы, при использовании в `<ConversationList>` использует `useConversationList()` для получения `isLoadError` и импорта. |
| PlaceholderEmptyList | `ReactNode` | `<PlaceHolder type={PlaceHolderTypes.NO_CONVERSATIONS} />` | Элемент заполнителя, когда пользовательский список сеансов пуст. |
| PlaceholderLoading | `ReactNode` | `<PlaceHolder type={PlaceHolderTypes.LOADING} />` | Элемент заполнителя для загрузки пользовательского списка сеансов. |
| PlaceholderLoadError | `ReactNode` | `<PlaceHolder type={PlaceHolderTypes.WRONG} />` | Элемент заполнителя для пользовательского списка ошибок загрузки сеансов. |
| className | `String` | - | Укажите пользовательское имя для класса CSS корневого элемента. |
| style | `React.CSSProperties` | - | Укажите пользовательский стиль для корневого элемента. |

#### Базовая настройка

Эффекты интерфейса компонента `List` в разных статусах показаны ниже. Время срабатывания каждого состояния обрабатывается внутри `ConversationList`.

При этом вы можете управлять статусом компонента через пользовательский ввод `empty`, `loading` и `error`.

```
import { ConversationList, ConversationListContent } from '@tencentcloud/chat-uikit-react';import type { ConversationListContentProps } from '@tencentcloud/chat-uikit-react';const CustomConversationListContent = (props: ConversationListContentProps) => {    return <ConversationListContent {...props} loading={true} />;};<ConversationList  List={CustomConversationListContent} />
```

| `default` | `empty={true}` | `loading={true}` | `error={true}` |
| --- | --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/749d0b835e3211f0bac1525400454e06.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/74b0a29d5e3211f0b324525400e889b2.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/74a5f5df5e3211f097ec52540044a08e.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/74b4d8ab5e3211f08e9352540099c741.png) |

### Пользовательский просмотр беседы

Подробнее см. раздел [ConversationPreview](https://www.tencentcloud.com/document/product/1047/64705).

```
<ConversationList ConversationPreview={CustomConversationPreview} />
```

### Пользовательские действия с беседой

Подробнее см. раздел [ConversationActions](https://www.tencentcloud.com/document/product/1047/64707).

```
  <ConversationList ConversationActions={CustomConversationActions} />
```

### Настройка ConversationSearch

Подробнее см. раздел [ConversationSearch](https://www.tencentcloud.com/document/product/1047/64706).

```
<ConversationList ConversationSearch={CustomConversationSearch} />
```

### Настройка ConversationCreate

```
<ConversationList ConversationCreate={CustomConversationCreate} />
```

### Пользовательский аватар

```
<ConversationList Avatar={CustomAvatar} />
```

## Props

| **Имя параметра** | **Тип** | **Значение по умолчанию** | **Описание** |
| --- | --- | --- | --- |
| enableSearch | `Boolean` | `true` | Управление отображением функции поиска беседы. |
| enableCreate | `Boolean` | `true` | Управление отображением функции создания сеанса. |
| enableActions | `Boolean` | `true` | Управление отображением функции действия с беседой. |
| actionsConfig | `ConversationActionsConfig` | - | Используется для пользовательской конфигурации операции сеанса. |
| Header | `ReactElement` | `Header` | Пользовательский компонент Header. |
| List | `ReactElement` | `List` | Пользовательский компонент списка сеансов. |
| Preview | `ReactElement` | [ConversationPreview](https://www.tencentcloud.com/document/product/1047/64705) | Пользовательский компонент предварительного просмотра сеанса. |
| ConversationCreate | `ReactElement` | `ConversationCreate` | Пользовательский компонент беседы. |
| ConversationSearch | `ReactElement` | [ConversationSearch](https://www.tencentcloud.com/document/product/1047/64706) | Пользовательский компонент поиска сеанса. |
| ConversationActions | `ReactElement` | [ConversationActions](https://www.tencentcloud.com/document/product/1047/64707) | Пользовательский компонент операции с беседой. |
| Avatar | `ReactElement` | `Avatar` | Пользовательский компонент аватара. |
| PlaceholderEmptyList | `ReactNode` | `<PlaceHolder type={PlaceHolderTypes.NO_CONVERSATIONS} />` | Элемент заполнителя, когда пользовательский список сеансов пуст. |
| PlaceholderLoading | `ReactNode` | `<PlaceHolder type={PlaceHolderTypes.LOADING} />` | Элемент заполнителя для загрузки пользовательского списка сеансов. |
| PlaceholderLoadError | `ReactNode` | `<PlaceHolder type={PlaceHolderTypes.WRONG} />` | Элемент заполнителя для пользовательского списка ошибок загрузки сеансов. |
| filter | `(conversationList: ConversationModel[]) => ConversationModel[]` | - | Функции для фильтрации списка сеансов. |
| sort | `(conversationList: ConversationModel[]) => ConversationModel[]` | - | Функции для сортировки списка сеансов. |
| onConversationSelect | `(conversation: ConversationModel) => void;` | `-` | `Функция обратного вызова после нажатия на сеанс с параметром, представляющим объект нажатого сеанса.` |
| `onBeforeCreateConversation` | `(params: CreateParams) => CreateParams;` | `-` | `Пользовательское действие, выполняемое перед созданием сеанса, с параметром, представляющим необходимые параметры для создания сеанса.` |
| `onConversationCreate` | `(conversation: ConversationModel)  => void;` | - | Функция обратного вызова после создания сеанса с параметром, представляющим созданный объект сеанса. |
| className | `String` | - | Укажите пользовательское имя для класса CSS корневого элемента. |
| style | `React.CSSProperties` | - | Укажите пользовательский стиль для корневого элемента. |


---
*Источник: [https://trtc.io/document/64703](https://trtc.io/document/64703)*

---
*Источник (EN): [conversationlist.md](./conversationlist.md)*

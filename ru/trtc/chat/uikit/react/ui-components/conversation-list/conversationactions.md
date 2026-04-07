# ConversationActions

Компонент `ConversationActions` отвечает за операции со строками в одной сессии. По умолчанию поддерживает удаление диалога, закрепление диалога вверху/открепление и отключение/включение звука.

## Основное использование

При использовании `ConversationActions` в `ConversationList` вы можете настроить его напрямую через параметр `actionsConfig` верхнего уровня в `ConversationList`. `actionsConfig` поддерживает переключатели функций операций диалога по умолчанию, обработку событий, добавление новых пользовательских элементов действий и базовую настройку интерфейса.

Для продвинутой настройки вы можете создать новые компоненты через `ConversationActions`.

### Использование базовой настройки ActionsConfig

```
import { UIKitProvider, ConversationList } from "@tencentcloud/chat-uikit-react";import type { ConversationModel } from "@tencentcloud/chat-uikit-react";const App = () => {  return (    <UIKitProvider>      <ConversationList        actionsConfig={{          enablePin: false,          onConversationDelete: (conversation: ConversationModel) => { console.log('Delete conversation success'); },          customConversationActions: {            'custom-actions-1': {               label: 'custom-actions',               onClick: (conversation: ConversationModel) => { console.log(conversation); },             },          },      }}/>    </UIKitProvider>  );}
```

### Пользовательский компонент ConversationActions

```
import { UIKitProvider, ConversationList, ConversationActions } from "@tencentcloud/chat-uikit-react";import type { ConversationActionsProps } from '@tencentcloud/chat-uikit-react';const CustomConversationActions = (props: ConversationActionsProps) => {  return <ConversationActions {...props} enableDelete={false} />;};const App = () => {  return (    <UIKitProvider>      <ConversationList        style={{ maxWidth: '300px', height: '600px' }}        ConversationActions={CustomConversationActions}      />    </UIKitProvider>  );}
```

## Props

API типа компонента `ConversationActions` `ConversationActionsProps` основан на API `ConversationActionsConfig` и расширен.

| **ConversationActionsProps** |  |  |  |
| --- | --- | --- | --- |
| **Название параметра** | **Тип** | **Значение по умолчанию** | **Примечание** |
| **conversation*****(Обязательно)*** | ConversationModel | - | Этот параметр обязателен и представляет сессию для текущей отображаемой операции диалога. |
| className | String | - | Название класса пользовательского корневого элемента. |
| style | React.CSSProperties | - | Стиль пользовательского корневого элемента. |
| ConversationActionsConfig |  |  |  |
| **Название параметра** | **Тип** | **Значение по умолчанию** | **Примечание** |
| enablePin | Boolean | true | Отображать ли кнопку функции закрепления вверху. |
| enableMute | Boolean | true | Отображать ли кнопку функции "не беспокоить". |
| enableDelete | Boolean | true | Отображать ли кнопку функции удаления. |
| onConversationPin | (conversation: ConversationModel, e?: React.MouseEvent) => void | - | Настройте поведение закрепления/открепления диалогов. |
| onConversationMute | (conversation: ConversationModel, e?: React.MouseEvent)=> void | - | Настройте поведение функции "не беспокоить"/отмены "не беспокоить" для сессии. |
| onConversationDelete | (conversation: ConversationModel, e?: React.MouseEvent) => void | - | Настройте поведение удаления диалогов. |
| customConversationActions | Record<string, [ConversationActionItem](#96079c71-233e-442e-96ef-ba91fbd5e201)> | - | Пользовательские элементы операций сессии. |
| PopupIcon | ReactElement | - | Пользовательский значок всплывающего окна действия. |
| PopupElements | ReactElement[] | - | Содержимое пользовательского всплывающего окна действия. |
| onClick | (e: React.MouseEvent, key?: string, conversation?: ConversationModel) => void | - | Функция обратного вызова для действия щелчка. |

## Настройка компонента

### Переключатель основных функций

Установив параметры `enablePin`, `enableDelete` и `enableMute`, вы можете гибко управлять отображением закрепления диалога, отключения звука уведомления и удаления диалога в `ConversationActions`.

```
<ConversationActions enablePin={false} />
```

```
enableDelete
```

```
enableMute
```

| `enablePin={false}` | `enableDelete={false}` | `enableMute={false} ` |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e7be41055e2f11f091585254001c06ec.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e7baa5d75e2f11f0b324525400e889b2.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e7be68215e2f11f091585254001c06ec.png) |

### Обработка событий

Компонент `ConversationActions` по умолчанию поддерживает удаление диалога, закрепление диалога вверху/открепление и отключение/включение звука. Если обработка событий существующей функциональности не соответствует вашим потребностям, вы можете настроить функцию обработки ответа события и переопределить её. Помимо настройки ответов на события функций, вы также можете получить ответ на базовое событие щелчка через onClick.

```
import { ConversationList, ConversationActions, Toast } from '@tencentcloud/chat-uikit-react';import type { ConversationActionsProps, ConversationModel } from '@tencentcloud/chat-uikit-react';const CustomConversationActions = (props: ConversationActionsProps) => {  return (    <ConversationActions      {...props}      onConversationDelete={(conversation: ConversationModel) => {        conversation.deleteConversation().then(() => {          Toast({ text: 'delete conversation successfully!', type: 'info' });        }).catch(() => {          Toast({ text: 'delete conversation failed!', type: 'error' });        });      }}    />  );};<ConversationList ConversationActions={CustomConversationActions} />
```

### customConversationActions

`customConversationActions` используется для добавления новых пользовательских элементов действий в список ConversationActions.

| ConversationActionItem |  |  |  |
| --- | --- | --- | --- |
| **Название параметра** | **Тип** | **Значение по умолчанию** | **Примечание** |
| enable | Boolean | true | Включить ли пользовательские элементы действий. |
| label | String | - | Содержимое отображения пользовательского элемента действия. |
| onClick | (conversation: ConversationModel, e?: React.MouseEvent) => void | - | Функция обратного вызова при нажатии на пользовательский элемент действия. |

Вот пример добавления новых пользовательских элементов действий с помощью `customConversationActions`:

```
import { ConversationList, ConversationActions } from '@tencentcloud/chat-uikit-react';import type { ConversationActionsProps, ConversationModel } from '@tencentcloud/chat-uikit-react';const CustomConversationActions = (props: ConversationActionsProps) => {  return (    <ConversationActions       {...props}       customConversationActions={{        'custom-actions-1': {           label: 'custom-actions',           onClick: (conversation: ConversationModel) => { console.log(conversation); },         },      }}    />  );};     <ConversationList ConversationActions={CustomConversationActions} />
```

| **До изменения** | **После изменения** |
| --- | --- |
| ****![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e7c05dbf5e2f11f097ec52540044a08e.png)**** | ****![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e7c27bfd5e2f11f097ec52540044a08e.png)**** |

### Настройка пользовательского интерфейса

Вы можете настроить стиль кнопки всплывающего окна пробуждения через параметр `PopupIcon` и содержимое всплывающего окна через `PopupElements`.

Ниже приведен пример кода для вторичной разработки на основе компонента `ConversationActions` по умолчанию для настройки нового стиля кнопки пробуждения:

```
import { ConversationList, ConversationActions, ConversationActionsProps } from '@tencentcloud/chat-uikit-react';import type { ConversationActionsProps } from '@tencentcloud/chat-uikit-react';const CustomConversationActions = (props: ConversationActionsProps) => {  const customIcon = <div>Custom Icon</div>  return (    <ConversationActions {...props} PopupIcon={customIcon} />  );};     <ConversationList ConversationActions={CustomConversationActions} />
```

| **До изменения** | **После изменения** |
| --- | --- |
| ****![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e7bc736e5e2f11f092fe525400bf7822.png) | ****![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e7cccf8a5e2f11f0b30d5254007c27c5.png) |


---
*Источник: [https://trtc.io/document/64707](https://trtc.io/document/64707)*

---
*Источник (EN): [conversationactions.md](./conversationactions.md)*

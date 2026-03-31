# ChatSetting

## Обзор компонента

`ChatSetting` — это интеллектуальный компонент настроек чата, который может автоматически отображать соответствующий интерфейс настроек на основе текущего активного типа сеанса. Этот компонент внутренне интегрирует два режима: настройки чата C2C (один-на-один) и настройки группового чата, предоставляя пользователям единый портал настроек чата.

Основные возможности компонента:

- **Автоматическая адаптация** — интерфейс настроек автоматически переключается в зависимости от типа сеанса
- **Управление состоянием** — автоматическое обновление содержимого на основе текущего активного сеанса

## Параметры Props

| Параметр | Тип | Значение по умолчанию | Описание |
| --- | --- | --- | --- |
| className | string \| undefined | undefined | Пользовательское имя CSS класса |
| style | React.CSSProperties \| undefined | undefined | Пользовательский встроенный стиль |

## Быстрое использование

`ChatSetting` — это независимый компонент, который можно использовать свободно. По умолчанию элемент управления переключением находится на компоненте ChatHeader. Альтернативно используйте Hook `useUIOpenControlState` для настройки переключателя ChatSetting.

```
function App() {  const { isChatSettingOpen, setChatSettingOpen } = useUIOpenControlState();    function toggleChatSettingOpen() {    setChatSettingOpen(!isChatSettingOpen);  }    return (     <UIKitProvider>        <div style={{ maxWidth: '300px' }}>          <ConversationList />        </div>        <Chat          PlaceholderEmpty={null}          style={{            display: 'flex',            flexDirection: 'row',            flex: 1,            maxHeight: '100vh',          }}        >          <div style={{            display: 'flex',            flexDirection: 'column',            flex: 1,            minWidth: '0',          }}          >            <button onClick={toggleChatSetting}>toggle</button>            <MessageList />            <MessageInput />          </div>          {isChatSettingOpen && <ChatSetting style={{ width: '350px' }} />}        </Chat>      </UIKitProvider>  );}
```


---
*Источник: [https://trtc.io/document/72094](https://trtc.io/document/72094)*

---
*Источник (EN): [chatsetting.md](./chatsetting.md)*

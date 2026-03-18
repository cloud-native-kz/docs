# Интеграция

TUIKit — это библиотека компонентов пользовательского интерфейса на основе Chat SDK. Она позволяет быстро реализовать функции чата, сеансов, поиска, цепочки отношений, групп и другие возможности через компоненты пользовательского интерфейса. В этой статье описано, как быстро интегрировать TUIKit и реализовать основные функции.

Кроме того, если вы предпочитаете более быстрый и автоматизированный подход, вы можете обратиться к [Начало работы с интеграцией AI](https://www.tencentcloud.com/document/product/1047/72277) для оптимизации процесса.

## Предварительные требования

- Node.js v18 или выше (рекомендуется версия LTS v22)
- React^18.2.0 || React^19.0.0

## Создание проекта

Создайте новый проект React с именем **chat-app** и завершите инициализацию проекта по подсказкам scaffolder.

```
npm create rsbuild@latest
```

## Установка и импорт компонентов

### Шаг 1: Установка зависимостей

Загрузите [chat-uikit-react](https://www.npmjs.com/package/@tencentcloud/chat-uikit-react) через npm и используйте его в проекте.

```
npm i @tencentcloud/chat-uikit-react
```

### Шаг 2: Введение компонента chat UIKit react

> **Примечание:** Следующий код не содержит `SDKAppID`, `userID` и `UserSig`. Вам необходимо заменить их на соответствующую информацию, полученную на [Шаге 4](https://www.tencentcloud.com/document/product/1047/50055#.E6.AD.A5.E9.AA.A44.EF.BC.9A.E8.8E.B7.E5.8F.96-sdkappid.E3.80.81userid-.E5.92.8C-usersig). Чтобы уважать авторские права на дизайн эмодзи, проект Chat Demo/TUIKit не содержит больших графических файлов эмодзи. Пожалуйста, замените их на свои разработки или другие пакеты эмодзи, на которые вы имеете авторские права, перед официальным запуском в коммерческих целях. **Стандартный пакет эмодзи смайликов, показанный ниже, защищен авторским правом Tencent RTC**, вы можете перейти на [Chat Pro Plus Edition и Enterprise Edition](https://console.trtc.io/subscription/buy/chat?packType=pro) для его бесплатного использования. ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a7c853cf981a11ef834b525400f69702.png)

Скопируйте следующий код `App.tsx` и замените исходное содержимое в `App.tsx`.

Скопируйте следующий код `App.css` и замените файл стилей `App.css` в том же каталоге.

App.tsx

App.css

```
import {  UIKitProvider,  useLoginState,  LoginStatus,  ConversationList,  Chat,  ChatHeader,  MessageList,  MessageInput,  ContactList,  ContactInfo,  useUIKit,  useConversationListState,} from "@tencentcloud/chat-uikit-react";import { useEffect, useState } from "react";import './App.css';function App() {  // Language support en-US(default) / zh-CN / ja-JP / ko-KR / zh-TW  // Theme supports light(default) / dark  return (    <UIKitProvider theme={'light'} language={'en-US'}>      <ChatApp />    </UIKitProvider>  );}function ChatApp() {  const [activeTab, setActiveTab] = useState('chats');    const { language } = useUIKit();  const texts = language === 'zh-CN'    ? { chats: 'ä¼è¯', contacts: 'èç³»äºº', emptyTitle: 'ææ ä¼è¯', emptySub: 'éæ©ä¸ä¸ªä¼è¯å¼å§èå¤©', error: 'è¯·æ£æ¥ SDKAppID, userID, userSig, éè¿å¼åäººåå·¥å·(F12)æ¥çå·ä½çéè¯¯ä¿¡æ¯', loading: 'ç»å½ä¸­...' }    : { chats: 'Chats', contacts: 'Contacts', emptyTitle: 'No conversation', emptySub: 'Select a conversation to start chatting', error: 'Please check the SDKAppID, userID, and userSig. View the specific error information through the developer tools (F12).', loading: 'Logging in...'};  const { status } = useLoginState({    SDKAppID: 0, // type: number    userID: '',  // type: string    userSig: '', // type: string  })  const { setActiveConversation } = useConversationListState();  useEffect(() => {    async function init() {      // You can switch to another created userID      const userID = 'administrator';      const conversationID = `C2C${userID}`;      setActiveConversation(conversationID);    }    if (status === LoginStatus.SUCCESS) {      init();    }  }, [status]);  if (status === LoginStatus.ERROR) {    return (      <div className="loading-container">        <div className="loading-spinner"></div>        <div className="loading-text">{texts.error}</div>      </div>    )  }  if (status !== LoginStatus.SUCCESS) {    return (      <div className="loading-container">        <div className="loading-spinner"></div>        <div className="loading-text">{texts.loading}</div>      </div>    )  }  return (    <div className="chat-app">      <ul className="vertical-tabs">        <li           className={`tab-item ${activeTab === 'chats' ? 'active' : ''}`}          onClick={() => {setActiveTab('chats')}}        >          {texts.chats}        </li>        <li           className={`tab-item ${activeTab === 'contacts' ? 'active' : ''}`}          onClick={() => {setActiveTab('contacts')}}        >          {texts.contacts}        </li>      </ul>      {        activeTab === 'chats' && (          <>            <ConversationList style={{ flex: '0 0 300px'}}/>            <Chat              className="chat-box"              PlaceholderEmpty={                <div className="empty-chat">                  <div className="empty-icon">ð¬</div>                  <div className="empty-title">{texts.emptyTitle}</div>                  <div className="empty-subtitle">{texts.emptySub}</div>                </div>              }            >              <ChatHeader />              <MessageList />              <MessageInput />            </Chat>          </>        )      }      {        activeTab === 'contacts' && (          <>            <ContactList style={{ flex: '0 0 300px'}}/>            <ContactInfo              style={{ flex: '1'}}              onSendMessage={() => {setActiveTab('chats')}}              onEnterGroup={() => {setActiveTab('chats')}}            />          </>        )      }    </div>  );}export default App;
```

```
body {  margin: 0;  padding: 20px;  font-family: Inter, Avenir, Helvetica, Arial, sans-serif;  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);  min-height: 100vh;  box-sizing: border-box;}.chat-app {  height: calc(100vh - 40px);  max-width: 1400px;  margin: 0 auto;  display: flex;  flex-direction: row;  background: #ffffff;  border-radius: 16px;  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3),              0 0 0 1px rgba(0, 0, 0, 0.1);  overflow: hidden;  backdrop-filter: blur(10px);}.vertical-tabs {  list-style: none;  margin: 0;  padding: 0;  width: 100px;  background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);  border-right: 1px solid rgba(0, 0, 0, 0.08);}.tab-item {  padding: 16px 20px;  cursor: pointer;  background: transparent;  color: #495057;  font-size: 14px;  text-align: center;  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);  position: relative;}.tab-item::before {  content: '';  position: absolute;  left: 0;  top: 50%;  transform: translateY(-50%);  width: 3px;  height: 0;  background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);  border-radius: 0 3px 3px 0;  transition: height 0.3s cubic-bezier(0.4, 0, 0.2, 1);}.tab-item:hover {  background: rgba(102, 126, 234, 0.08);  color: #667eea;}.tab-item.active {  background: linear-gradient(90deg, rgba(102, 126, 234, 0.15) 0%, rgba(102, 126, 234, 0.05) 100%);  color: #667eea;}.tab-item.active::before {  height: 60%;}.chat-box {  flex: 1;  border-left: 1px solid rgba(0, 0, 0, 0.08);}.empty-chat {  display: flex;  flex: 1;  flex-direction: column;  align-items: center;  justify-content: center;  height: 100%;  color: #adb5bd;  gap: 12px;  text-align: center;  border-left: 1px solid rgba(0, 0, 0, 0.08);}.empty-icon {  font-size: 64px;  opacity: 0.3;  animation: float 3s ease-in-out infinite;}.empty-title {  font-size: 16px;  font-weight: 600;  color: #6c757d;}.empty-subtitle {  font-size: 14px;  color: #868e96;}@keyframes float {  0%, 100% {    transform: translateY(0px);  }  50% {    transform: translateY(-10px);  }}.loading-container {  display: flex;  flex-direction: column;  align-items: center;  justify-content: center;  height: 100vh;  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);  gap: 24px;}.loading-spinner {  width: 60px;  height: 60px;  border: 4px solid rgba(255, 255, 255, 0.2);  border-top-color: #ffffff;  border-radius: 50%;  animation: spin 1s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite;  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);}.loading-text {  color: #ffffff;  font-size: 18px;  font-weight: 500;  letter-spacing: 0.5px;  animation: pulse 2s ease-in-out infinite;}@keyframes spin {  0% {    transform: rotate(0deg);  }  100% {    transform: rotate(360deg);  }}@keyframes pulse {  0%, 100% {    opacity: 1;  }  50% {    opacity: 0.6;  }}
```

Вот перевод. Я заменил пример **Ant Design** на **Material UI (MUI)**, который широко используется в международном сообществе React.

---

**Поддерживает ли он React 17?**

React v17.x в настоящее время не поддерживается. Мы поддерживаем только React v18.2 или выше.

**Могу ли я использовать библиотеки сторонних компонентов, такие как Material UI?**

Да, вы можете использовать другие библиотеки для "клеевого кода", связывающего основные компоненты. Вы можете увидеть это в примере ниже, где `<ChatSetting />` инкапсулирован внутри компонента Drawer. Однако обратите внимание, что внутренние элементы основных компонентов в настоящее время не могут быть изменены.

```javascript
import Drawer from '@mui/material/Drawer';
import { useState } from 'react';
// ... внутри вашего компонента
const [isChatSettingShow, setIsChatSettingShow] = useState(false);
const onChatSettingClose = () => {
  setIsChatSettingShow(false);
};
<Drawer
  anchor="right"
  open={isChatSettingShow}
  onClose={onChatSettingClose}>
  {/* Material UI Drawers оборачивают содержимое напрямую */}
  <h3>Settings</h3>
  <ChatSetting />
</Drawer>
```

### Шаг 3: Получение SDKAppID, UserID и UserSig

В скопированном ранее коде `App.tsx` информация для аутентификации входа пуста. Вам необходимо заполнить информацию аутентификации приложения Tencent Cloud в хуке `useLoginState`, как показано ниже:

| Параметр | Тип | Примечание |
| --- | --- | --- |
| userID | String | Уникальный идентификатор пользователя, определяется вами, может содержать только прописные и строчные буквы (a-z, A-Z), цифры (0-9), подчеркивания и дефисы. |
| SDKAppID | Number | Уникальный идентификатор приложения для аудио и видео, созданного в [Консоли Tencent RTC](https://console.trtc.io/). |
| SDKSecretKey | String | SDKSecretKey приложения для аудио и видео, созданного в [Консоли Tencent RTC](https://console.trtc.io/). |
| userSig | String | Подпись защиты безопасности, используемая для аутентификации входа пользователя, для подтверждения личности пользователя и предотвращения кража прав на использование облачных услуг злоумышленниками. |

> **Пояснение UserSig:** **Среда разработки**: Если вы запускаете демо локально и занимаетесь разработкой или отладкой, вы можете использовать функцию `genTestUserSig` (см. Шаг 3.2) в файле отладки для создания "userSig". При этом методе SDKSecretKey уязвим для декомпиляции и обратного проектирования. Если ваш ключ будет скомпрометирован, злоумышленники смогут украсть трафик вашей Tencent Cloud. **Производственная среда**: Если ваш проект готов к запуску, используйте метод [Генерирование UserSig на стороне сервера](https://trtc.io/document/34385).

1. Войдите в [Консоль Chat](https://console.trtc.io/).
2. Нажмите **Create Application**, введите имя приложения, затем нажмите **Create**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/cdc5fdb411ec11efa2935254005ac0ca.png)

3. После создания вы можете просмотреть статус приложения, версию сервиса, SDKAppID, время создания, теги и время истечения срока действия нового приложения на странице обзора консоли.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c73f215c7cf411f0914f52540099c741.png)

4. [Перейдите на страницу управления пользователями](https://console.trtc.io/chat/account-management), создайте 2–3 тестовых аккаунта для проверки в чатах C2C и групповых чатах.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0be64336adb311f096c2525400454e06.png)

5. Информация UserSig. Нажмите [IM console > development tool > UserSig tool](https://console.trtc.io/usersig), заполните созданный userID и создайте userSig.

### Шаг 4: Запуск проекта

Замените SDKAppID, UserID и UserSig в App.tsx, затем выполните следующую команду:

```
 npm run dev
```

> **Примечание:** Убедитесь, что в коде Шага 3 SDKAppID, UserID и UserSig успешно заменены. Если они не будут заменены, проект будет работать неправильно. Один `userID` соответствует одному `userSig`, для получения дополнительной информации см. [Генерирование UserSig](https://trtc.io/document/39074?product=consoleguide). Если проект не запускается, проверьте, соответствуют ли [требования среды разработки](https://www.tencentcloud.com/document/product/1047/50055#.E5.BC.80.E5.8F.91.E7.8E.AF.E5.A2.83.E8.A6.81.E6.B1.82).

### Шаг 5: Отправьте свое первое сообщение

Введите сообщение в поле ввода и нажмите Enter для отправки.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/efc5e925595711efb36952540075b605.png)

## Часто задаваемые вопросы

### Что такое UserSig?

UserSig — это пароль для входа пользователей в Chat. По сути, это зашифрованный текст, полученный путем шифрования информации, такой как UserID.

### Как создать UserSig?

Метод выдачи UserSig включает интеграцию кода расчета UserSig на ваш сервер и предоставление интерфейса, ориентированного на ваш проект. Когда требуется UserSig, ваш проект отправляет запрос на бизнес-сервер для получения динамического UserSig. Для получения дополнительной информации см. [Как создать UserSig на сервере](https://trtc.io/document/39074?product=consoleguide).

> **Примечание:** Пример кода, приведенный в этом документе, извлекает UserSig путем встраивания SECRETKEY в код клиента. Этот подход делает SECRETKEY очень восприимчивым к декомпиляции и обратному проектированию. Если ваш ключ шифрования скомпрометирован, злоумышленники могут неправомерно присвоить трафик Tencent Cloud. Поэтому **эта процедура рекомендуется исключительно для локальной отладки функций**. Для правильной выдачи UserSig обратитесь к предыдущим разделам.

### Поддерживает ли он React 17?

React v17.x в настоящее время не поддерживается. Мы поддерживаем только React v18.2 или выше.

### Могу ли я использовать библиотеки сторонних компонентов, такие как Material UI?

Да, вы можете использовать другие библиотеки для "клеевого кода", связывающего основные компоненты. Вы можете увидеть это в примере ниже, где `<ChatSetting />` инкапсулирован внутри компонента Drawer. Однако обратите внимание, что внутренние элементы основных компонентов в настоящее время не могут быть изменены.

```
import Drawer from '@mui/material/Drawer';
import { useState } from 'react';
// ... внутри вашего компонента
const [isChatSettingShow, setIsChatSettingShow] = useState(false);
const onChatSettingClose = () => {
  setIsChatSettingShow(false);
};
<Drawer
  anchor="right"
  open={isChatSettingShow}
  onClose={onChatSettingClose}>
  {/* Material UI Drawers оборачивают содержимое напрямую */}
  <h3>Settings</h3>
  <ChatSetting />
</Drawer>
```

## Связь с нами

Присоединитесь к [Telegram технической группе обмена](https://t.me/tencent_imsdk) или [WhatsApp группе обмена](https://chat.whatsapp.com/IVa11ZkVmKTEwSWsAzSyik), чтобы получить поддержку от профессиональных инженеров и решить ваши проблемы.

## Справочник

- [chat-uikit-react npm](https://www.npmjs.com/package/@tencentcloud/chat-uikit-react)
- [Исходный код демо и пример запуска](https://github.com/TencentCloud/chat-uikit-react)

Дополнительные функции см. в документации ChatEngine API:

- [Справочник API chat-uikit-engine](https://web.sdk.qcloud.com/im/doc/chat-engine/index.html)
- [chat-uikit-engine npm](https://www.npmjs.com/package/@tencentcloud/chat-uikit-engine)


---
*Источник: [https://trtc.io/document/50055](https://trtc.io/document/50055)*

---
*Источник (EN): [integration.md](./integration.md)*

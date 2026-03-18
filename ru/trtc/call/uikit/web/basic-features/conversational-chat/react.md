# React

Интегрируя Chat и CallKit, вы можете достичь следующих эффектов. Нажмите

Попробовать в интернете

.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0643a621bb5c11efb5b052540055f650.png)

## Требования к окружению

- React версии 18+ (версии 17.x не поддерживаются)
- TypeScript
- [Node.js](https://nodejs.org/en/) версии 16+
- npm (используйте версию, соответствующую используемой версии Node)

## Шаг 1: Интеграция Chat

Для получения подробных инструкций обратитесь к: [Быстрая интеграция Chat](https://trtc.io/document/50055?platform=web&product=chat&menulabel=uikit).

## Шаг 2: Активация возможности аудио и видео звонков

Перед использованием услуг аудио и видео, предоставляемых Tencent Cloud, вам необходимо перейти в консоль и активировать услугу для приложения. Обратитесь к конкретным шагам в [Активация услуги](https://trtc.io/document/59832).

## Шаг 3: Загрузка компонента TUICallKit

Загрузите компонент TUICallKit через [npm](https://www.npmjs.com/package/@tencentcloud/chat-uikit-vue), версии 3.3.6 и выше:

```
npm i @tencentcloud/call-uikit-react
```

## Шаг 4: Импорт и вызов компонента TUICallKit

- Просто добавьте две строки кода, чтобы испытать функцию звонков. Импортируйте TUICallKit и вызовите компонент TUICallKit.
- Включите Call в компоненте <ChatHeader />, отобразите Icon и установите enableCall в true.

> **Примечание:** Если вы еще не интегрировали TUIKit, следуйте документации [Интеграция TUIKit](https://trtc.io/document/50055?lang=zh&pg=) для интеграции TUIKit. Версия TUIKit 2.2.8 и выше. Компонент TUICallKit может добавить стиль для отображения и управления позицией, шириной, высотой и другими стилями TUICallKit.

```
// 1. Import TUICallKitimport { TUICallKit } from '@tencentcloud/call-uikit-react';
```

```
// 2. If you are displaying on a PC, please add style to initialize the position of TUICallKit. If it is displayed on H5, it is not needed.const callStyle: React.CSSProperties = {  position: 'fixed',  top: '50%',  left: '50%',  zIndex: '999',  transform: 'translate(-50%, -50%)',};
```

```
// 3. Please use the TUICallKit component in UIKitProviderreturn (  <div style={{display: 'flex', height: '100vh'}}>    <UIKitProvider language={"en-US"}>      <TUICallKit style={callStyle} />       <div style={{maxWidth: '400px'}}>         <Profile />         <ConversationList />      </div>      <Chat>        <ChatHeader enableCall={true}/>         <MessageList />        <MessageInput />      </Chat>      <ChatSetting />    </UIKitProvider>  </div>);
```

## Шаг 5: Запуск проекта

```
 npm run start
```

## Шаг 6: Отправка первого сообщения

Введите ваше сообщение в поле ввода и нажмите Enter для отправки.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e819f27dd32511efa4a3525400bf7822.png)

## Шаг 7: Совершите первый звонок

Как показано на рисунке, нажмите на значок видео/аудио на панели инструментов, чтобы реализовать функцию звонков.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0cfeeaa5d32611ef82a5525400e889b2.png)

## Часто задаваемые вопросы

- Если у вас возникли проблемы с доступом и использованием, обратитесь к [Часто задаваемые вопросы](https://trtc.io/document/53565?platform=web&product=call).
- Если у вас есть какие-либо требования или отзывы, вы можете связаться с: info_rtc@tencent.com.


---
*Источник: [https://trtc.io/document/67768](https://trtc.io/document/67768)*

---
*Источник (EN): [react.md](./react.md)*

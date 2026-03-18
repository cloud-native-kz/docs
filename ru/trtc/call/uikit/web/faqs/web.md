# Web

### Что мне делать, если я получу сообщение об ошибке "The package you purchased does not support this ability"?

Если вы столкнулись с приведённым выше сообщением об ошибке, это означает, что пакет Audio and Video Calling Capability вашего текущего приложения истёк или не был активирован. Обратитесь к [Activate Service](https://trtc.io/document/59832?platform=web&product=call) чтобы получить или активировать возможность аудио- и видеозвонков, и продолжите использование компонента TUICallKit.

### Как мне приобрести пакет?

Пожалуйста, перейдите по ссылке [Purchase Official Version](https://trtc.io/document/59832?platform=web&product=call#4662020f-9958-4144-b900-73f97127327e).

### Как мне создать UserSig?

UserSig — это тип цифровой подписи, разработанный Tencent Cloud для своих облачных сервисов. Она служит учётными данными для входа и создаётся на основе зашифрованной комбинации информации, такой как SDKAppID и SecretKey.

- **Способ 1:** Получение через панель управления, см. [How to Obtain a Temporary UserSig](https://console.trtc.io/usersig).
- **Способ 2:** Развёртывание скрипта временной генерации.

> **Предупреждение:** Этот подход предполагает наличие SecretKey в коде фронтенда. К сожалению, при использовании этого способа SecretKey можно легко расшифровать посредством обратного инжиниринга. Если ваш ключ будет скомпрометирован, злоумышленники смогут использовать ваш трафик Tencent Cloud. Поэтому **этот способ подходит только для локальной отладки функций**. Для production-окружения, пожалуйста, используйте способ 3.

Для более удобной начальной отладки функция `genTestUserSig(params)` в файле `GenerateTestUserSig-es.js` может быть временно использована для расчёта userSig, например:

```
import { genTestUserSig } from "./debug/GenerateTestUserSig-es.js";const { userSig } = genTestUserSig({ userID: "Alice", SDKAppID: 0, SecretKey: "YOUT_SECRETKEY" });
```

- **Способ 3:** Использование в official-окружении.

Правильный способ выдачи UserSig заключается в интеграции кода расчёта UserSig на сервер вашего проекта, предоставляя специальные интерфейсы. Когда требуется UserSig, ваш проект может отправлять запросы на бизнес-сервер для получения динамического UserSig. Подробнее см. [Generating UserSig on Server-side](https://trtc.io/document/35166?platform=web&product=rtcengine).

### Как создаётся groupID в групповом вызове?

Создание groupID требует интеграции пакета [@tencentcloud/chat](https://www.npmjs.com/package/@tencentcloud/chat). Подробности см. в документации [createGroup API](https://trtc.io/document/48465?platform=web&product=chat#creating-a-group); ниже приведён пример кода для создания groupID.

```
import Chat from "@tencentcloud/chat";   // npm i @tencentcloud/chatconst userIDList: string[] = ['user1', 'user2'];async function createGroupID() {  const chat = Chat.create({ SDKAppID });  const memberList: any[] = userIDList.map(userId => ({ userID: userId }));  const res = await chat.createGroup({    type: Chat.TYPES.GRP_PUBLIC,    name: 'WebSDK',    memberList  });  return res.data.group.groupID;}
```

### Как мне создать userID?

**Уникальный идентификатор пользователя,** **определяемый вами,** может содержать только прописные и строчные буквы (a-z, A-Z), цифры (0-9), подчёркивания и дефисы.

- Первоначальный вход с использованием userID и userSig автоматически создаст пользователя.
- Создание и получение через [Tencent RTC Console](https://console.trtc.io/chat/account-management).

## Ошибка <call>: failed Invalid sender or receiver identifier

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/925174be198411ef8a48525400762795.png)

Эта ошибка возникает потому, что вызваемый userID не существует; убедитесь, что userID вошёл в систему хотя бы один раз. Подробности см. в разделе [How do I create a userID](https://trtc.io/document/51024?platform=android&product=call#create_userID).

## Ошибка [CallService]API<init>: sdkAppID is required

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ac5619e1198411ef8bfe5254002fd0a8.png)

- Эта ошибка возникает потому, что вы не указали информацию SDKAppID при [TUICallKitServer.init](https://trtc.io/document/51015#init)/ `GenerateTestUserSig.genTestUserSig`
- Пожалуйста, получите и заполните информацию из [Tencent RTC Console](https://trtc.io/document/59832?platform=android&product=call).

## Ошибка npm install -g create-react-app: errno -13

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/68f3e847198511efa1975254005ac0ca.png)

Если возникает эта ошибка, это означает, что текущий пользователь не имеет прав на глобальную установку scaffolding. Пожалуйста, используйте `sudo npm install -g create-react-app`**.**

## **Ошибка npm install -g @vue/cli package: errno -13**

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ca82ea7c198511ef87e352540019e87e.png)

Если возникает эта ошибка, это означает, что текущий пользователь не имеет прав на глобальную установку scaffolding. Пожалуйста, используйте `sudo npm install -g @vue/cli`**.**


---
*Источник: [https://trtc.io/document/51024](https://trtc.io/document/51024)*

---
*Источник (EN): [web.md](./web.md)*

# Статус онлайн

## Описание

UIKit поддерживает отображение статуса онлайн пользователей в списке диалогов и списке контактов.

Когда включена опция "Показывать статус онлайн пользователя", статус онлайн каждого пользователя будет отображаться на его аватаре в списке чатов и списке контактов.

Когда опция "Показывать статус онлайн пользователя" отключена, статус онлайн пользователя не будет отображаться.

> **Примечание:** Эта функция поддерживается только в изданиях Pro, Pro Plus и Enterprise. Пожалуйста, [приобретите издание Pro, Pro Plus или Enterprise](https://trtc.io/buy/chat) для использования этой функции. Включите переключатель статуса пользователя в [Консоли Chat](https://console.trtc.io/). Убедитесь, что переключатель включен перед использованием.

## Эффект отображения

### Список диалогов

| Включить "Показывать статус онлайн пользователя" | Отключить "Показывать статус онлайн пользователя" |
| --- | --- |
|  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/669a1843ed1511ef840e52540044a08e.jpg) |  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/68a70813ed1511ef93475254005ef0f7.jpg) |

### Список контактов

| Включить "Показывать статус онлайн пользователя" | Отключить "Показывать статус онлайн пользователя" |
| --- | --- |
|  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7731e24fed1511efa1f2525400bf7822.jpg) |  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7887e288ed1511ef93475254005ef0f7.jpg) |

## Обзор функции

При инициализации UIKit настройте `useUserOnlineStatus` в `TencentCloudChatUserConfig` для включения этой функции.

```
final bool initRes = await TencentCloudChat.controller.initUIKit(  config: TencentCloudChatConfig(    userConfig: TencentCloudChatUserConfig(      useUserOnlineStatus: true,      // ... other UIKit configurations    ),  ),);
```

## Часто задаваемые вопросы

- **При вызове API подписки/отписки интерфейс выдает ошибку "Error Code 72001".**

Код ошибки 72001 указывает на то, что соответствующая функция не включена в Консоли. Пожалуйста, войдите в [Консоль Chat](https://console.trtc.io/) и включите соответствующий переключатель функции.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bf08ba1c855511ef8829525400fdb830.png)

- **Ошибка: Пакет не поддерживает использование этого интерфейса. Пожалуйста, перейдите на продвинутый пакет.**

Эта функция поддерживается только в изданиях Pro, Pro Plus и Enterprise. Сообщение об ошибке указывает на то, что ваш текущий пакет не поддерживает эту возможность. Пожалуйста, войдите в [Страницу покупки Chat](https://console.trtc.io/buy/active) для активации Premium Edition и попробуйте эту функцию.

## Свяжитесь с нами

Если у вас есть вопросы во время процесса интеграции и использования, свяжитесь с нами одним из следующих способов.

- [Группа Telegram](https://t.me/+1doS9AUBmndhNGNl)
- [Группа WhatsApp](https://chat.whatsapp.com/Gfbxk7rQBqc8Rz4pzzP27A)


---
*Источник: [https://trtc.io/document/52884](https://trtc.io/document/52884)*

---
*Источник (EN): [online-status.md](./online-status.md)*

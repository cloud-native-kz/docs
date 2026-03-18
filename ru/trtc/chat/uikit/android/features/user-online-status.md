# Статус онлайн пользователя

## Описание

TUIKit поддерживает отображение статуса онлайн пользователя, начиная с версии [6.5.2803](https://www.tencentcloud.com/document/product/1047/34282?lang=en&pg=#6.5.2803-.402022.07.15---enhanced-edition).

Когда функция "Показывать статус онлайн пользователя" включена, статус онлайн пользователя будет отображаться на аватаре каждого пользователя в списке чатов и списке контактов. Зелёный круг указывает на то, что пользователь в сети; отсутствие зелёного круга указывает на то, что пользователь в сети.

Когда функция "Показывать статус онлайн пользователя" отключена, статус онлайн пользователя отображаться не будет.

> **Примечание:** Функция "Статус онлайн пользователя" поддерживается только [Pro ãPro Plus ãEnterprise](https://www.tencentcloud.com/document/product/1047/34350?lang=en&pg=). Убедитесь, что пакет Pro ãPro Plus или Enterprise активирован перед использованием этой функции. Функция "Статус онлайн пользователя" требует включения переключателя статуса пользователя в [консоли Chat](https://console.trtc.io/). Убедитесь, что переключатель включён перед использованием этой функции. Только друзья в списке разговоров поддерживают отображение их статуса онлайн. Если вам нужна поддержка для не-друзей, вы должны вызвать API для подписки на статус не-друзей и реализовать пользовательский интерфейс самостоятельно. Справка по API: [User Status](https://trtc.io/document/49562?platform=android&product=chat&menulabel=coresdk#change-in-a-non-friend-user&).

## Включение статуса онлайн пользователя в списке чатов

В компоненте `TUIConversation`, в файле [TUIConversationConfig.java](https://github.com/TencentCloud/chat-uikit-android/blob/main/TUIKit/TUIConversation/tuiconversation/src/main/java/com/tencent/qcloud/tuikit/tuiconversation/config/TUIConversationConfig.java), предоставляется переключатель для функции "Статус онлайн пользователя", названный **isShowUserStatus**. Его тип — boolean, значение по умолчанию — false.

```
public class TUIConversationConfig {    private boolean isShowUserStatus;}
```

Чтобы включить отображение статуса онлайн пользователя в списке чатов, сначала подпишитесь на пакет Pro ãPro Plus или Enterprise, затем включите переключатель функции статуса пользователя в [консоли Chat](https://console.trtc.io/), и измените значение по умолчанию **isShowUserStatus** на `true`, или вызовите следующий метод перед инициализацией страницы чата.

```
TUIConversationConfig.getInstance().setShowUserStatus(true);
```

### Результат в списке чатов

| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0d1f84db129c11efa2935254005ac0ca.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/21324f1a129c11efaa1c525400f65c2a.png) |
| --- | --- |

## Включение статуса онлайн пользователя в списке контактов

В компоненте `TUIContact`, в файле [TUIContactConfig.java](https://github.com/TencentCloud/chat-uikit-android/blob/main/TUIKit/TUIContact/tuicontact/src/main/java/com/tencent/qcloud/tuikit/tuicontact/config/TUIContactConfig.java), предоставляется переключатель для функции "Статус онлайн пользователя", названный **isShowUserStatus**. Его тип — boolean, значение по умолчанию — false.

```
public class TUIContactConfig {    private boolean isShowUserStatus;}
```

Чтобы включить отображение статуса онлайн пользователя в списке контактов, сначала подпишитесь на пакет Pro ãPro Plus или Enterprise, затем включите переключатель функции статуса пользователя в [консоли Chat](https://console.trtc.io/), и измените значение по умолчанию **isShowUserStatus** на `true`, или вызовите следующий метод перед инициализацией страницы списка контактов.

```
TUIContactConfig.getInstance().setShowUserStatus(true);
```

### Результат в списке контактов

| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/f96b167a129c11efaa1c525400f65c2a.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0e99b4a8129d11efbf645254007bbd8c.png) |
| --- | --- |

## Часто задаваемые вопросы

### При вызове API подписки/отписки API возвращает код ошибки "72001".

Код ошибки 72001 указывает на то, что соответствующая возможность не активирована в консоли. Пожалуйста, войдите в [консоль Chat](https://console.trtc.io/) и включите соответствующий переключатель функции.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/6376f3ff129e11ef89cc5254002fd0a8.png)

### Ошибка: Пакет не поддерживает использование этого API. Пожалуйста, обновитесь до пакета Pro ãPro Plus или Enterprise.

Функция "Статус онлайн пользователя" поддерживается только пакетом Pro ãPro Plus или Enterprise. Это сообщение об ошибке указывает на то, что ваш текущий пакет не поддерживает эту функцию. Пожалуйста, войдите на [страницу покупки Chat](https://console.trtc.io/buy/active), чтобы активировать пакет Pro ãPro Plus или Enterprise и опробовать его.

## Обмен и обратная связь

Присоединитесь к [группе технического обмена Telegram](https://t.me/+1doS9AUBmndhNGNl) или [группе обсуждения WhatsApp](https://chat.whatsapp.com/Gfbxk7rQBqc8Rz4pzzP27A), получайте поддержку профессиональных инженеров и решайте ваши самые сложные задачи.


---
*Источник: [https://trtc.io/document/59435](https://trtc.io/document/59435)*

---
*Источник (EN): [user-online-status.md](./user-online-status.md)*

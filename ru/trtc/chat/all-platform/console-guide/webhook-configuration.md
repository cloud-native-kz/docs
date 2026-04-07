# Конфигурация Webhook

Войдите в [консоль Chat](https://console.trtc.io/), выберите **Chat >**[**Webhook**](https://console.trtc.io/chat/callback-setting) на левой боковой панели и **выберите целевое приложение** вверху. Вы можете настроить URL обратного вызова и включить необходимые обратные вызовы в соответствии с потребностями вашего бизнеса.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/010d0928cb3d11f08942525400e889b2.png)

## Конфигурация URL-адресов Webhook

1. На странице **Webhook Configuration**, нажмите **Edit** в области конфигурации URL webhook.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0947d5bdcb3d11f08942525400e889b2.png)

2. В открывшемся диалоговом окне конфигурации URL webhook введите URL webhook.

> **Примечание:** URL webhook должен начинаться с `http://` или `https://`. Если вы еще не зарегистрировали доменное имя, вы можете напрямую настроить IP-адрес, например `http://123.123.123.123/imcallback`. Можно использовать только буквы (`a–z`, без учета регистра), цифры (0–9) и дефисы (-). Пробелы и следующие символы не поддерживаются: `!$&?`. Дефис (-) не может встречаться подряд, регистрироваться независимо или находиться в начале или конце. Длина доменного имени не может превышать 63 символа. URL webhook Chat по умолчанию использует порты 80/443. При замене URL webhook требуются изменения портов. Избегайте ситуации, когда порты до и после замены являются взаимными префиксами; например, избегайте изменения `https://xxx:443` на `https://xxx:4433` или изменения `https://xxx` на `https://xxx:4433`.

3. Нажмите **OK** для сохранения конфигурации.

## Конфигурация Event Webhook

1. На странице **Webhook Configuration**, нажмите **Edit** в области конфигурации webhook. В открывшемся окне редактирования выберите функцию для настройки.
2. В открывшемся диалоговом окне конфигурации webhook установите флажки для нужных webhook.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/707d5c0dcb3e11f0a7775254005ef0f7.png)

> **Примечание:** Некоторые функции Webhook требуют предварительного включения соответствующей функции в консоли перед их запуском. Для получения подробной информации см. Руководство по активации событий Webhook.

3. Нажмите **Confirm** для сохранения конфигурации.

## Последующие операции

После настройки URL-адресов webhook и включения соответствующих event webhook вы можете обратиться к [Webhooks](https://intl.cloud.tencent.com/document/product/1047/34354), чтобы использовать соответствующие webhook для получения информации о пользователях и операциях в режиме реального времени.

## **Руководство по активации событий Webhook**

#### Webhook онлайн-статуса участников Live Group

Чтобы включить обратный вызов онлайн-статуса для участников AVChatRoom, сначала включите переключатель онлайн-статуса участника группы в **Chat > Configuration >**[**Custom User Field**](https://console.trtc.io/chat/user-data).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a5ac81cbcb3e11f087ad52540099c741.png)

#### Webhook изменения профиля пользователя

Чтобы включить Webhook изменения профиля пользователя, сначала включите переключатель подписки на изменение профиля пользователя в **Chat > Configuration >** [**Login and Message**](https://console.trtc.io/chat/login-message).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b1b3506acb3e11f0a93d52540044a08e.png)

#### Обратный вызов онлайн-статуса

Чтобы включить обратный вызов онлайн-статуса, сначала включите переключатель конфигурации запроса статуса пользователя и уведомления об изменении статуса в **Chat > Configuration >** [**Login and Message**](https://console.trtc.io/chat/login-message).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b8206f1acb3e11f087ad52540099c741.png)


---
*Источник: [https://trtc.io/document/34520](https://trtc.io/document/34520)*

---
*Источник (EN): [webhook-configuration.md](./webhook-configuration.md)*

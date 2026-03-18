# Генерация и проверка UserSig

Вы можете генерировать UserSig онлайн в консоли TRTC, но это следует использовать только для быстрого тестирования на этапе разработки. Это предотвращает утечку ключей и предотвращает кражу трафика злоумышленниками.

## Генератор подписей (UserSig)

Подписи (UserSig) позволяют вам установить доверие с Tencent Cloud.

1. Войдите в [Chat консоль > Development Tools > UserSig Tools](https://console.trtc.io/usersig).
2. В области Signature (UserSig) Generator **выберите приложение**, **вручную введите UserID**.
3. Нажмите **Generate UserSig** для генерации подписи, которая истекает через 180 дней.
4. Нажмите **Copy UserSig** для копирования подписи, а затем вставьте и сохраните подпись.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/23b0a1e0cb6b11f084a45254005ef0f7.png)

## Проверитель подписей (UserSig)

Система автоматически получает ключ текущего приложения. После ввода UserID и UserSig вы можете использовать инструмент для быстрой проверки действительности UserSig.

1. Войдите в [Chat консоль > Development Tools > UserSig Tools](https://console.trtc.io/usersig).
2. В области Signature (UserSig) Verifier **выберите приложение**, **вручную введите UserID** и **UserSig**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/23ce87d5cb6b11f08942525400e889b2.png)

3. Нажмите **Verify** для просмотра результата проверки.
  - Если проверка успешна, вы можете просмотреть SDKAppID, UserID, время генерации, время обслуживания и время истечения UserSig в результатах проверки.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/23ce98e9cb6b11f08942525400e889b2.png)

  - Если проверка не пройдена, вы можете просмотреть причину сбоя и решение в результатах проверки.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/23cecff5cb6b11f091ab5254007c27c5.png)


---
*Источник: [https://trtc.io/document/39074](https://trtc.io/document/39074)*

---
*Источник (EN): [usersig-generation-and-verification.md](./usersig-generation-and-verification.md)*

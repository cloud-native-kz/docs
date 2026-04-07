# Генерация UserSig

UserSig — это пароль для входа пользователя и одновременно подпись для использования RestAPI. По сути это зашифрованный текст, полученный путем шифрования UserID и другой информации. В этой статье описано, как генерировать UserSig.

> **Примечание:** Система Live и система обмена мгновенными сообщениями (Chat) используют один и тот же метод генерации usersig.

## Получение ключа

1. Войдите в [консоль Chat](https://console.trtc.io/chat).

> **Примечание:** Если у вас нет приложения, пожалуйста, [активируйте сервис](https://www.tencentcloud.com/document/product/647/60033) для создания приложения.

2. Нажмите на карточку целевого приложения, чтобы перейти на страницу его базовой конфигурации.
3. В разделе **Основная информация** нажмите **Показать ключ** справа от **Ключ**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d83717db256d11f091625254001c06ec.png)

4. Нажмите **Копировать**, чтобы скопировать и сохранить информацию ключа.

> **Примечание:** Храните информацию ключа надлежащим образом, чтобы предотвратить утечку.

## Расчет UserSig на клиенте

Модуль с открытым исходным кодом `GenerateTestUserSig`, предоставленный в примере кода Chat SDK, поможет вам быстро сгенерировать UserSig. Вам нужно только настроить три переменные-члены: SDKAPPID (SDKAppID приложения), EXPIRETIME (время истечения UserSig) и SECRETKEY (информация о ключе), а затем вызвать функцию genTestUserSig() для быстрого получения UserSig.

Чтобы упростить этот процесс, мы предоставляем исходный код для расчета UserSig для следующих языков и платформ. Вы можете напрямую загрузить и интегрировать исходный код в ваш клиент.

| Язык программирования | Платформа | Исходный код GenerateTestUserSig |
| --- | --- | --- |
| Java | Android | [GenerateTestUserSig.java](https://github.com/tencentyun/TIMSDK/blob/master/Android/Demo/app/src/main/java/com/tencent/qcloud/tim/demo/signature/GenerateTestUserSig.java) |
| Objective-C | iOS | [GenerateTestUserSig.h](https://github.com/tencentyun/TIMSDK/blob/master/iOS/Demo/TUIKitDemo/Private/GenerateTestUserSig.h) |
| Objective-C | Mac | [GenerateTestUserSig.h](https://github.com/tencentyun/TIMSDK/blob/master/Mac/Demo/TUIKitDemo/Debug/GenerateTestUserSig.h) |
| C++ | Windows | [GenerateTestUserSig.h](https://github.com/tencentyun/TIMSDK/blob/master/Windows/Demo/IMApp/GenerateTestUserSig.h) |
| Javascript | Web | [GenerateTestUserSig.js](https://github.com/TencentCloud/chat-uikit-vue/blob/main/Vue3/TUIKit/debug/GenerateTestUserSig.js) |
| Dart | Flutter | [GenerateTestUserSig.dart](https://github.com/TencentCloud/chat-demo-flutter/blob/main/lib/utils/GenerateTestUserSig.dart ) |

> **Примечание:** При использовании этого метода `SECRETKEY` уязвим к декомпиляции и обратной инженерии. После разглашения `SECRETKEY` злоумышленники смогут украсть ваш трафик Tencent Cloud. Поэтому **этот метод подходит только для локального запуска демонстрационного проекта и отладки функций**. Правильный способ выдачи UserSig — это интеграция кода расчета UserSig на ваш сервер и предоставление приложению API. Когда требуется UserSig, ваше приложение отправляет запрос на бизнес-сервер для получения динамического UserSig. Дополнительную информацию см. в разделе [Как рассчитать UserSig](#GeneratingdynamicUserSig).

## Расчет UserSig на сервере

Расчет на сервере обеспечивает максимальную защиту от раскрытия ключа, используемого для расчета UserSig. Вам нужно только развернуть код расчета UserSig на своем сервере и предоставить приложению API. Когда требуется UserSig, ваше приложение отправляет запрос на бизнес-сервер для получения динамического UserSig.

Чтобы упростить этот процесс, мы предоставляем исходный код для расчета UserSig для следующих языков и платформ. Вы можете напрямую загрузить и интегрировать исходный код на ваш сервер.

| Язык программирования | Ключевая функция | URL загрузки |
| --- | --- | --- |
| Java | HMAC-SHA256 | [genSig](https://github.com/Tencent-RTC/tls-sig-api-v2-java/blob/main/src/main/java/com/tencentcloud/TLSSigAPIv2.java) |
| GO | HMAC-SHA256 | [GenSig](https://github.com/Tencent-RTC/tls-sig-api-v2-golang/blob/main/tencentyun/TLSSigAPI.go) |
| PHP | HMAC-SHA256 | [genSig](https://github.com/Tencent-RTC/tls-sig-api-v2-php/blob/main/src/TLSSigAPIv2.php) |
| Nodejs | HMAC-SHA256 | [genSig](https://github.com/Tencent-RTC/tls-sig-api-v2-node/blob/main/TLSSigAPIv2.js) |
| Python | HMAC-SHA256 | [gen_sig](https://github.com/Tencent-RTC/tls-sig-api-v2-python/blob/main/TLSSigAPIv2.py) |
| C# | HMAC-SHA256 | [GenSig](https://github.com/Tencent-RTC/tls-sig-api-v2-cs/blob/main/tls-sig-api-v2-cs/TLSSigAPIv2.cs) |
| C++ | HMAC-SHA256 | [gen_sig](https://github.com/Tencent-RTC/tls-sig-api-v2-cpp) |

Ключевые поля в функции расчета UserSig включают SDKAppID, UserID и период действия UserSig, как описано в следующей таблице.

> **Примечание:** В следующей таблице используются имена полей исходного кода Java в качестве примера. Имена полей могут отличаться в других языках.

| Имя поля (пример) | Описание |
| --- | --- |
| sdkappid | SDKAppID приложения. SDKAppID можно получить на карточке приложения в [консоли Chat](https://console.trtc.io/chat). |
| userId | ID пользователя (старое название: `Identifier`). |
| expire | Период действия UserSig в секундах. Рекомендуется, чтобы период действия UserSig был не менее 24 часов и не более 50 лет. Для безопасности вашей учетной записи рекомендуется установить период действия UserSig на два месяца. |
| userbuf | По умолчанию это поле устанавливается на `null`, так как в Chat используются API без UserBuf. |
| key | Ключ. Ключ можно получить на странице сведений о приложении в [консоли Chat](https://console.trtc.io/chat). |

## Старая версия алгоритма

Чтобы упростить вычисление подписи, позволив клиентам удобно и быстро использовать услуги Tencent Cloud, алгоритм подписи сервиса Chat был обновлен с ECDSA-SHA256 на HMAC-SHA256 с 19 июля 2019 года. Это означает, что все SDKAppID, созданные после 19 июля 2019 года, будут использовать новый алгоритм HMAC-SHA256.

Если ваш SDKAppID был создан до 19 июля 2019 года, мы рекомендуем обновить алгоритм подписи на [HMAC-SHA256](#GeneratingdynamicUserSig). Обновление не повлияет на вашу работу. Кроме того, вы можете продолжать использовать алгоритм подписи более ранней версии. URL-адреса для загрузки исходного кода алгоритма ECDSA-SHA256 приведены ниже:

| Язык программирования | Алгоритм подписи | Ссылка на загрузку |
| --- | --- | --- |
| Java | ECDSA-SHA256 | [GitHub](https://github.com/tencentyun/tls-sig-api-java) |
| GO | ECDSA-SHA256 | [GitHub](https://github.com/tencentyun/tls-sig-api-golang) |
| PHP | ECDSA-SHA256 | [GitHub](https://github.com/tencentyun/tls-sig-api-php) |
| Nodejs | ECDSA-SHA256 | [GitHub](https://github.com/tencentyun/tls-sig-api-node) |
| Python | ECDSA-SHA256 | [GitHub](https://github.com/tencentyun/tls-sig-api-python) |
| C# | ECDSA-SHA256 | [GitHub](https://github.com/tencentyun/tls-sig-api-cs) |
| C++ | ECDSA-SHA256 | [GitHub](https://github.com/tencentyun/tls-sig-api) |

## Получение UserSig из консоли

- Войдите в консоль Tencent-RTC, перейдите в раздел Инструменты разработки > [Инструменты UserSig](https://console.trtc.io/usersig).
- В разделе Инструмент генерации UserSig выберите соответствующие SDKAppID и UserID.
- Нажмите кнопку Генерировать, чтобы рассчитать соответствующий UserSig.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d835f280256d11f091625254001c06ec.png)


---
*Источник: [https://trtc.io/document/69883](https://trtc.io/document/69883)*

---
*Источник (EN): [generate-usersig.md](./generate-usersig.md)*

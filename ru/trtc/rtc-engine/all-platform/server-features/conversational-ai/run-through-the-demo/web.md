# Веб

Этот документ в основном описывает, как быстро запустить демо-проект AIConversationKit и получить опыт работы с высококачественным проектом диалогового AI. Следуя этой документации, вы можете запустить демо в течение 20 минут и в конечном итоге получить опыт работы с проектом диалогового AI с полным интерфейсом пользователя.

| **Интерфейс диалогового AI** |
| --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/cf3749c0139311f08c275254001c06ec.png) |

## Конфигурация демо

Сначала перейдите на [console](https://console.trtc.io/) для создания приложения, затем [активируйте соответствующую услугу](https://www.tencentcloud.com/document/product/647/69002#).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/33e61e9821a811f0a62e525400454e06.png)

## Запуск демо

1. После создания перейдите на страницу сведений о приложении, выберите **RTC-Engine** **> Conversational AI**, обратитесь к [No-Code Quick Integration Of Conversational AI Feature](https://www.tencentcloud.com/document/product/647/68137) для конфигурации параметров диалогового AI, нажмите **Quick Integration** в нижнем правом углу, переключитесь на Web и получите параметры SecretId, SecretKey и Config.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d656f3b212e511f0a9cd5254007c27c5.png)

2. При запуске серверного кода сначала установите соответствующие зависимости и замените соответствующие secretId и secretKey.

```
npm i express tencentcloud-sdk-nodejs-trtc
```

3. Запустите код фронтенда.
4. Запустите ваш проект диалогового AI.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8971a335137711f0a63e5254005ef0f7.png)


---
*Источник: [https://trtc.io/document/68999](https://trtc.io/document/68999)*

---
*Источник (EN): [web.md](./web.md)*

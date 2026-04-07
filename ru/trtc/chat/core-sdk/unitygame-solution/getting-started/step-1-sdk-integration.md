# Шаг 1: Интеграция SDK

Этот документ описывает способ быстрой интеграции Chat SDK для Unity в ваши проекты. Для настройки и интеграции SDK выполните следующие шаги.

## Требования к окружению

| Платформа | Версия |
| --- | --- |
| Unity | 2019.4.15f1 или новее |
| Android | Android Studio 3.5 или новее; устройства с Android 4.1 или новее для приложений |
| iOS | Xcode 11.0 или новее. Убедитесь, что ваш проект имеет действительную подпись разработчика. |

## Интеграция через UPM (рекомендуется)

1. Найдите файл `manifest.json`:
![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/48db71a0966911ef992f52540075b605.png)
2. Измените его следующим образом:

```
{  "dependencies":{    "com.tencent.imsdk.unity":"https://github.com/TencentCloud/chat-sdk-unity.git#unity"  }}
```

3. Откройте проект в Unity Editor, дождитесь загрузки зависимостей и убедитесь, что Tencent Cloud Chat успешно загружен.
![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/48dd1bef966911efa04c52540055f650.jpeg)
4. Это тестовый шаг. Вы можете загрузить [IM_Api_Example](https://github.com/TencentCloud/tc-chat-sdk-unity/tree/main/Assets/IM_Api_Example) и поместить его в ваш проект после распаковки.
![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/48d55b0a966911ef992f52540075b605.png)

> **Примечание:** IM_Api_Example — это демонстрационное приложение, используемое для тестирования данных обратного вызова API SDK. Вы также можете вызывать API на ранних этапах разработки проекта для управления вашим проектом.

Перетащите все сцены в папке

`IM_Api_Example/Assets`

в

`Build Settings`

и убедитесь, что сцена

`Main`

находится на первом месте.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/48d66fd6966911ef967c525400a9236a.jpeg)

Дважды щелкните сцену

`Main`

в папке

`IM_Api_Example/Assets`

, чтобы запустить демонстрацию. Здесь вы можете выбрать язык.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/48d3a04d966911ef834b525400f69702.jpeg)

Щелкните

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/48ba3aff966911efaaca525400fdb830.png)

справа от заголовка и введите информацию.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/48d64327966911efa04c52540055f650.jpeg)

Щелкните

**InitSDK**

и

**Login**

в

**Base Module**

для инициализации и входа. После этого вы сможете вызывать API-интерфейсы, доступные в IM_Api_Example.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/48c795e0966911ef820f525400d5f8ef.jpeg)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/48dd47ad966911ef992f52540075b605.jpeg)


---
*Источник: [https://trtc.io/document/46263](https://trtc.io/document/46263)*

---
*Источник (EN): [step-1-sdk-integration.md](./step-1-sdk-integration.md)*

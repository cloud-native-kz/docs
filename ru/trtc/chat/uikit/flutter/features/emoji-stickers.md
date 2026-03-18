# Emoji & Stickers

Этот документ описывает, как реализовать модуль стикеров в Tencent Cloud Chat Flutter UIKit.

В виджете Message доступны два типа стикеров, которые показаны в следующем списке:

| Тип стикера | MessageType | Интеграция в текст | Схема отправки | Схема отображения | Использование | По умолчанию |
| --- | --- | --- | --- | --- | --- | --- |
| Маленькое изображение | Text Message | Да | Имя изображения | Изображение автоматически сопоставляется с локальными ресурсами активов по имени. | **Включено по умолчанию**, с одним набором стандартных пакетов, при этом добавление новых пакетов и настройка также поддерживаются. | Предоставляется один набор стандартных пакетов, показанный на скриншотах ниже. |
| Большое изображение | Sticker Message | Нет | `baseURL` плюс имя файла изображения, которые образуют путь к ресурсу эмодзи | Ресурсы активов анализируются на основе пути. | Изображения хранятся как активы и определяются в `List` | - |

| **Название** | Маленькое изображение (разработано нами) | Большое изображение Tencent |
| --- | --- | --- |
| **Тип** | Маленькое изображение | Большое изображение |
| **Описание** | **Включено по умолчанию**, расположено в первую очередь | Не предоставляется по умолчанию, этот пакет поступает из конфигурации настройки нашего [примера приложения](https://github.com/TencentCloud/chat-demo-flutter/tree/v2). |
| **Скриншоты** | ![Figure 1](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/646d5566416511ee96d3525400088f3a.jpeg) | ![Figure 2](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/64a6dd21416511eeb231525400c56988.jpeg) |

## Использование

Сначала установите плагин [tencent_cloud_chat_sticker](https://pub.dev/packages/tencent_cloud_chat_sticker):

```
flutter pub add tencent_cloud_chat_sticker
```

Чтобы включить плагин, добавьте следующий код в список `plugins` в `initUIKit`:

```
TencentCloudChatPluginItem(  name: "sticker",  initData: TencentCloudChatStickerInitData(    userID: TencentCloudChatLoginData.userID,  ).toJson(),  pluginInstance: TencentCloudChatStickerPlugin(    context: context,  ),)
```

В объекте `TencentCloudChatStickerInitData` вы можете выбрать, какие стандартные наборы стикеров включить, и добавить дополнительные наборы стикеров в соответствии с вашими потребностями.


---
*Источник: [https://trtc.io/document/52227](https://trtc.io/document/52227)*

---
*Источник (EN): [emoji-stickers.md](./emoji-stickers.md)*

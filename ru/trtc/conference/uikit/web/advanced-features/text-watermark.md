# Текстовый водяной знак

TUIRoomKit запустил функцию текстового водяного знака, позволяющую пользователям устанавливать текстовые водяные знаки во время групповых встреч. В этой статье подробно описано, как использовать эту функцию в компоненте TUIRoomKit.

## Эффект интеграции

После интеграции функции текстового водяного знака в компонент TUIRoomKit эффект отображения выглядит следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ddfb5b621bf211ef942e525400720cb5.png)

## Требования к подготовке

Перед использованием функции текстового водяного знака Tencent Cloud необходимо перейти в консоль и активировать сервис Group Meeting для вашего приложения. Для получения конкретных инструкций см. раздел [Активация сервиса](https://www.tencentcloud.com/document/product/647/59973#).

## Включение текстового водяного знака

> **Примечание:****Платформа Mini Program пока не поддерживает эту функцию, но поддерживаются версии Electron и Web.****Требуется TUIRoomKit v2.3.3 или более поздней версии.**

TUIRoomKit предлагает функцию текстового водяного знака. Вы можете включить эту функцию, вызвав интерфейс [enableWatermark](https://www.tencentcloud.com/document/product/647/54880#daceee1b-175d-41a1-b495-d158fe01d63c).

Web

Electron

```
// Note the package name. If you are using the vue2 version, please change the package name to @tencentcloud/roomkit-web-vue2.7import { conference } from '@tencentcloud/roomkit-web-vue3';conference.enableWatermark();
```

```
// Note the package name. If you are using the vue2 version, please change the package name to @tencentcloud/roomkit-electron-vue2.7import { conference } from '@tencentcloud/roomkit-electron-vue3';conference.enableWatermark();
```

## Часто задаваемые вопросы

### 1. Почему стиль страницы выглядит неправильно после включения текстового водяного знака?

Пожалуйста, проверьте родительский элемент с **id 'roomContainer'** и убедитесь, что его `style` установлен на: `width: 100%; height: 100%; overflow: hidden;`.

Web

Electron

```
// Note the package name. If you are using the vue2 version, please change the package name to @tencentcloud/roomkit-web-vue2.7import { conference } from '@tencentcloud/roomkit-web-vue3';conference.enableWatermark();
```

```
// Note the package name. If you are using the vue2 version, please change the package name to @tencentcloud/roomkit-electron-vue2.7import { conference } from '@tencentcloud/roomkit-electron-vue3';conference.enableWatermark();
```


---
*Источник: [https://trtc.io/document/60531](https://trtc.io/document/60531)*

---
*Источник (EN): [text-watermark.md](./text-watermark.md)*

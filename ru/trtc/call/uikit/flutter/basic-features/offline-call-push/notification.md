# Уведомления

Чтобы помочь разработчикам легко реализовать функцию автономной отправки уведомлений в проектах Flutter, мы рекомендуем использовать плагин TIMPush (платный). По сравнению с отдельной интеграцией на Android и iOS, использование плагина TIMPush предлагает следующие преимущества:

- Короткий период интеграции — интеграция со всеми поставщиками услуг займет примерно 30 минут.
- Поддерживает статистику данных и отслеживание ссылок, что облегчает просмотр различных показателей, таких как уровень охвата, коэффициент кликов и коэффициент конверсии.
- Поддерживает отправку для всего персонала/по тегам, что упрощает отправку маркетинговых объявлений, уведомлений, новостей и другой информации всем пользователям или определенным группам.
- Поддерживает кроссплатформенные фреймворки, такие как uni-app и Flutter.

В этом документе подробно описано, как интегрировать плагин TIMPush в компонент TUICallKit для реализации возможности автономной отправки уведомлений для аудио- и видеозвонков.

| Android | iOS |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2ff7194e390311efb89a52540075b605.jpeg) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2ff94cbb390311ef9c9c525400d5f8ef.jpeg) |

## Руководство по интеграции

Перейдите к [методу интеграции TIMPush](https://trtc.io/document/50032?platform=flutter&product=chat&menulabel=uikit).

## Осуществление автономного отправки уведомления о вызове

Если вы хотите осуществить автономную отправку уведомления о вызове, необходимо установить OfflinePushInfo при вызове [calls](https://www.tencentcloud.com/document/product/647/54906#calls).

```
TUIOfflinePushInfo offlinePushInfo = TUIOfflinePushInfo(); offlinePushInfo.title = "Flutter TUICallKit"; offlinePushInfo.desc = "This is an incoming call from Flutter TUICallkit"; offlinePushInfo.ignoreIOSBadge = false; offlinePushInfo.iOSSound = "phone_ringing.mp3"; offlinePushInfo.androidSound = "phone_ringing"; offlinePushInfo.androidOPPOChannelID = "Flutter TUICallKit"; offlinePushInfo.androidVIVOClassification = 1; offlinePushInfo.androidFCMChannelID = "fcm_push_channel"; offlinePushInfo.androidHuaWeiCategory = "Flutter TUICallKit"; offlinePushInfo.iOSPushType = TUICallIOSOfflinePushType.APNs; TUICallParams params = TUICallParams(offlinePushInfo: offlinePushInfo);   TUICallKit.instance.calls(callUserIdList, TUICallMediaType.audio, params);
```

> **Примечание:** Если ваше приложение Android столкнулось с проблемами при получении уведомлений об отправке или открытии страниц, вы можете обратиться к [политике отображения вызовов для вызываемой стороны](https://trtc.io/document/51022?platform=flutter&product=call&menulabel=flutter#bfe2ed33-0611-4ca2-9aa8-f75b2a443e4a) для устранения неполадок.


---
*Источник: [https://trtc.io/document/60457](https://trtc.io/document/60457)*

---
*Источник (EN): [notification.md](./notification.md)*

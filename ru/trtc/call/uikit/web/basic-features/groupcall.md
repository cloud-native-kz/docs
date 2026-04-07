# Групповой вызов

Данная статья описывает использование функции группового вызова, такой как инициирование группового вызова и присоединение к групповому вызову.

## Ожидаемый результат

TUICallKit поддерживает групповые вызовы (до 9 человек). Ожидаемый результат показан на рисунке ниже.

| **Web** | **Мобильный клиент** |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c0ee84111bdd11ef88ad5254002977b6.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/719237f0ec0b11ee896d5254005cb287.png) |

## Инициирование многопользовательского вызова

Инициируйте групповой вызов, вызвав API `groupCall`.

```
import { TUICallKitAPI, CallMediaType } from "@trtc/calls-uikit-react";try {   const params = {     userIDList: ['user1', 'user2'],      type: CallMediaType.VIDEO,   }  await TUICallKitAPI.calls(params);} catch (error: any) {  console.error(`[TUICallKit] calls failed. Reason:${error}`);}
```

### Присоединение к групповому вызову

Присоединитесь к существующему аудио- и видеовызову в группе, вызвав API `join`.

```
try {  const params = {    callId: 'xxx'  };  await TUICallKitAPI.join(params);} catch (error: any) {  console.error(`[TUICallKit] join failed. Reason: ${error}`);}
```


---
*Источник: [https://trtc.io/document/59838](https://trtc.io/document/59838)*

---
*Источник (EN): [groupcall.md](./groupcall.md)*

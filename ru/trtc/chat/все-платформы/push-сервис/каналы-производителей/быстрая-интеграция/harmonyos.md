# HarmonyOS

## Этапы операции

### Этап 1: Интеграция TIMPush

```
// For the version number "VERSION", please refer to the changelog for configuration.// Configure the integration package in oh-package.json5dependencies: {    "@tencentcloud/timpush": "^VERSION",    "@tencentcloud/imsdk": "^VERSION",}
```

### Этап 2: Регистрация для получения услуг Push

Вызовите API для отправки после успешной регистрации, и вы сможете получать автономные уведомления Push.

```
import { TIMPushListener, TIMPushManager, TIMPushMessage } from '@tencentcloud/timpush';TIMPushManager.getInstance()  .registerPush(context, your sdkAppId, "client secret", Chat console certificate ID)  .then((result) => {    HiLog("registerPush success:", result.message);  })  .catch((error: Error) => {    HiLog("registerPush failed", error.code, error.message);  })
```

### Этап 3: Конфигурация статистики доставки сообщений

Если вам требуется статистика по данным охвата, выполните следующую конфигурацию:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/059565fc7f2011f0b3fe525400bf7822.png)

Адрес квитанции: `https://api.im.qcloud.com/v3/offline_push_report/harmony`

### Этап 4: Отправка Push-уведомлений

Подробные инструкции API см. в разделе [RESTful APIs - Initiate Push to All Users/Tag Push](https://www.tencentcloud.com/document/product/1047/60561).

### Этап 5: Разбор автономных Push-сообщений

После получения Push-сообщения и нажатия на уведомление компонент будет выполнять Webhook для события клика и сквозной передачи автономного сообщения.

> **Примечание:** Зарегистрируйте время обратного вызова в функции oncreate() приложения [UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-lifecycle). Конфигурируйте последующие действия при клике в консоли со следующей конфигурацией, выберите **open specified in-app page**, не изменяйте значения по умолчанию. ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5f199a167da111f0bda35254007c27c5.png)

```
let pushListener: TIMPushListener = {  onNotificationClicked: (data) => {    HiLog("onNotificationClicked", data);  }}TIMPushManager.getInstance().addPushListener(pushListener);
```

Поздравляем с завершением интеграции Push Plugin. Напоминаем вам: **По истечении пробного периода или срока действия подписки Push Plugin автоматически прекратит предоставление услуги push (включая автономную push для обычных сообщений, Tag Push и т.д.)**. Чтобы избежать нарушения нормального функционирования вашего бизнеса, пожалуйста, [приобретите](https://buy.tencentcloud.com/avc?activeId=plugin&position=20012840&regionId=9) или [обновите подписку](https://buy.tencentcloud.com/avc?activeId=plugin&position=20012840&regionId=9) заранее.

> **Примечание:** Интеграция завершена, но вы не получаете Push-уведомления? Сначала используйте [инструмент для устранения неполадок](https://www.tencentcloud.com/document/product/1047/60541) для проверки причины. Для просмотра данных метрик push используйте [статистику данных](https://www.tencentcloud.com/document/product/1047/60540) для запроса. Для функции push-уведомления для всех пользователей/Tag Push обратитесь к: [RESTful APIs - Initiate Push to All Users/Tag Push](https://www.tencentcloud.com/document/product/1047/60561).

---
*Источник: [https://trtc.io/document/72701](https://trtc.io/document/72701)*

---
*Источник (EN): [harmonyos.md](./harmonyos.md)*

# Поиск сообщений

Локальный поиск реализован в компоненте TUISearch TUIKit. Он позволяет пользователям быстро найти нужную информацию в больших объёмах сложных данных, таких как история чатов, контакты и групповые чаты. Его также можно использовать как инструмент управления для удобной и эффективной навигации по обширному контенту.

> **Примечание:** Функция локального поиска доступна только в Chat Ultimate edition. Чтобы её использовать, [приобретите Pro edition, Pro Plus edition или Enterprise edition](https://intl.cloud.tencent.com/document/product/1047/34577). Дополнительные сведения см. в разделе [Тарифы](https://intl.cloud.tencent.com/document/product/1047/34350).

## Демонстрация возможностей

Пользовательский интерфейс API поиска состоит из трёх частей: первая часть предназначена для поиска друзей, вторая часть — для поиска групп и членов групп, третья часть — для поиска сообщений, где сообщения классифицируются по беседе.

## Руководство по интеграции

Ниже представлена информация о том, как интегрировать компонент TUISearch.

### Покупка пакета

[Приобретите Pro edition, Pro Plus edition или Enterprise edition](https://intl.cloud.tencent.com/document/product/1047/34577).

### Интеграция TUISearch

Добавьте зависимость `tuisearch` в файл `build.gradle` в `APP`:

```
api project(':tuisearch')
```

### Вход в TUIKit

Вам необходимо вызвать `TUILogin` из `TUICore` для входа в TUIKit. Инициализация выполняется по умолчанию внутри API входа, и дополнительный вызов API инициализации не требуется.

```
TUILogin.login(this, SDKAPPID, userID, userSig, new TUICallback() {    @Override    public void onError(final int code, final String desc) {        // Ошибка входа.    }    @Override    public void onSuccess() {        // Вход выполнен успешно    }});
```

### Запуск пользовательского интерфейса поиска

1. Если вы интегрируете компоненты TUIConversation и TUISearch, на этом этапе дополнительная обработка не требуется, так как панель поиска по умолчанию отображается в верхней части списка бесед, как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/8bf85082129a11efaa1c525400f65c2a.png)

2. Если вы решили интегрировать только TUISearch, необходимо создать собственное представление поиска. Затем достаточно запустить SearchMainMinimalistActivity (для классического пользовательского интерфейса см. SearchMainActivity).

## Часто задаваемые вопросы

1. Как выполнить поиск по пользовательским сообщениям?
Для пользовательских сообщений, созданных и отправленных через API [createCustomMessage (byte[] data, String description, byte[] extension)](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a313b1ea616f082f535946c83edd2cc7f), укажите текст для поиска в параметре `description`.
Пользовательские сообщения, созданные через API [createCustomMessage (byte[] data)](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a5c2495d4b7ecd66e5636aeb865c17efd), не могут быть найдены, так как потоки двоичных данных сохраняются локально.

Если вы настроите функцию автономной отправки уведомлений и параметр `description`, пользовательские сообщения также будут отправлены в автономном режиме, а содержимое, указанное в параметре `description`, будет отображено в панели уведомлений.
Если вам не требуется функция автономной отправки уведомлений, используйте [disablePush](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#a5d0ea30668513f45eda447875528b9c7) в [V2TIMOfflinePushInfo](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html) из API [sendMessage](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a28e01403acd422e53e999f21ec064795), чтобы отключить её.
Если вы не хотите, чтобы содержимое, отправленное в панели уведомлений, отображалось как текст для поиска, вы можете использовать [setDesc](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html#a78c8e202aa4e0859468ce40bde6fd602) в [V2TIMOfflinePushInfo](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMOfflinePushInfo.html), чтобы установить содержимое отправляемого уведомления.

2. Как выполнить поиск по сообщениям с мультимедийным содержимым?
Сообщения с мультимедийным содержимым включают сообщения с файлами, изображениями, аудио и видео.
Для сообщения с файлом имя файла обычно отображается на пользовательском интерфейсе. Поэтому при создании сообщения с файлом вы можете установить параметр `fileName` как содержимое поиска. Если `fileName` не установлен, система получает имя файла из `filePath` и сохраняет его как на локальном устройстве, так и на сервере.
Для сообщения с изображением, аудио или видео на пользовательском интерфейсе обычно отображается эскиз или продолжительность. В этом случае вы можете указать тип сообщения для поиска, но не можете указать ключевые слова для поиска.


---
*Источник: [https://trtc.io/document/50038](https://trtc.io/document/50038)*

---
*Источник (EN): [search-messages.md](./search-messages.md)*

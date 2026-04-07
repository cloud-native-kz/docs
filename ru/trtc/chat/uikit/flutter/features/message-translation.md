# Перевод сообщений

## Обзор функции

Функция перевода текстовых сообщений позволяет пользователям переводить текстовые сообщения непосредственно в интерфейсе чата. Чтобы использовать эту функцию, нажмите и удерживайте любое текстовое сообщение в списке сообщений и выберите **Translate** из меню, чтобы просмотреть переведённый текст.

> **Примечание:** Функция перевода текстовых сообщений доступна для клиентов **Pro Plus и Enterprise edition**. Чтобы включить эту функцию, [приобретите Pro Plus или Enterprise edition](https://console.trtc.io/subscription/buy/chat?packType=pro&language=en). Trial Edition предлагает [ограниченное бесплатное использование](https://www.tencentcloud.com/document/product/1047/67651#0182a443-4747-42cb-b5de-ad165eb5a2ff) на один месяц.

## Перевод текстовых сообщений

| Кнопка перевода | Результат перевода текстового сообщения |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/488d9239025b11f18e6252540073fd3b.jpeg) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4f788704025b11f18e6252540073fd3b.jpeg) |

## Настройка целевого языка

Целевой язык для перевода управляется `AppBuilder`. Чтобы задать или получить целевой язык, обратитесь к [демо](https://github.com/Tencent-RTC/TUIKit_Flutter/blob/main/chat/demo/lib/pages/settings_page.dart):

```
// Set the target language for translationAppBuilder.getInstance().translateConfig.setTargetLanguage('zh');// Get the current target language for translationfinal currentLanguage = AppBuilder.getInstance().translateConfig.targetLanguage;
```

## Включение или отключение перевода текстовых сообщений

Виджет `MessageList` включает переключатель для функции **Text Message Translation** в параметре `config`. По умолчанию эта функция включена (`true`). Чтобы отключить её, установите значение `false`:

```
MessageList(  config: ChatMessageListConfig(isSupportTranslate: false),),
```

> **Примечание:** Поддерживаются только текстовые сообщения и текстовые сообщения-ссылки или ответы. Перевод изображений, голосовых сообщений, видео, файлов, эмодзи, пользовательских сообщений и других форматов не поддерживается. Максимальная частота запросов перевода составляет 5 раз в секунду.


---
*Источник: [https://trtc.io/document/61682](https://trtc.io/document/61682)*

---
*Источник (EN): [message-translation.md](./message-translation.md)*

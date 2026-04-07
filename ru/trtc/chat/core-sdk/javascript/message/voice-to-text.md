# Голос в текст

## Обзор функции

Функция преобразования речи в текст поддерживает распознавание голосовых сообщений, которые вы **успешно отправили или получили**, и преобразование их в текст.

> **Примечание:** Преобразование речи в текст является **платной функцией с добавленной стоимостью**, в настоящее время находится на этапе бесплатного тестирования. Вы можете связаться с нами через [группу технической поддержки в Telegram](https://t.me/+EPk6TMZEZMM5OGY1), чтобы активировать полный доступ к функции. Поддерживается версией v3.1.3 и выше.

## Отображение в интерфейсе

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e5c3cb681f2c11efafe1525400db4520.png)

## convertVoiceToText

Интерфейс преобразования речи в текст. Поддерживаемые форматы аудио включают wav, pcm, ogg-opus, speex, silk, mp3, m4a, aac, amr.

##### API

```
chat.convertVoiceToText(options);
```

##### Параметры

Параметр options имеет тип Object и содержит следующие значения атрибутов:

| Название | Тип | Описание |
| --- | --- | --- |
| message | Message | Голосовое сообщение |
| language | String \| undefined | Тип языка, по умолчанию преобразование речи в текст для китайского-английского-кантонского. Другие доступные типы: zh (cmn-Hans-CN), китайский; en-US, английский; yue-Hant-HK, кантонский; ja-JP, японский |

##### Возвращаемое значение

`Promise`

##### Примеры

```
// Наиболее часто используемое преобразование речи в текст для китайского-английского-кантонского, параметр language можно опустить
let promise = chat.convertVoiceToText({ message });
promise.then(function(imResponse)) {
  // Преобразование речи в текст выполнено успешно
  const { result } = imResponse.data;
}).catch(function(imError) {
  // Ошибка преобразования речи в текст
  console.warn('convertVoiceToText error:', imError);
});
```

```
// Преобразование речи в текст для японского языка
let promise = chat.convertVoiceToText({ message, language: 'ja-JP'});
promise.then(function(imResponse)) {
  // Преобразование речи в текст выполнено успешно
  const { result } = imResponse.data;
}).catch(function(imError) {
  // Ошибка преобразования речи в текст
  console.warn('convertVoiceToText error:', imError);
});
```


---
*Источник: [https://trtc.io/document/60751](https://trtc.io/document/60751)*

---
*Источник (EN): [voice-to-text.md](./voice-to-text.md)*

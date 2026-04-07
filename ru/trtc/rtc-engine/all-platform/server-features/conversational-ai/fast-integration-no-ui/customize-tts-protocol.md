# Настройка протокола TTS

## Режим вызова

POST : http://xxxxxxxxxxxx/api/v1/tts/stream

## Пример

### Заголовок HTTP-запроса

```
Content-Type: application/json;charset=UTF-8
X-Task-Id: task_id_value
X-Rquest-Id: request_id
X-Sdk-App-Id: SdkAppId
X-User-Idï¼UserId
X-Room-Idï¼RoomId 
X-Room-Id-Type: "0" 
Authorization: Bearer "API-KEY"
```

### Пример запроса

```
{
  "Text": "Hello, world! This is a test for the streaming TTS API.ã",
  "Format": "wav",
  "SampleRate": 16000,
  "Channel": 1
}
```

## Заголовок HTTP-запроса

| Поле | Описание |
| --- | --- |
| Content-Type | application/json |
| charset | UTF-8 |
| X-Task-Id | ID задачи диалога |
| X-Rquest-Id | ID запроса, при повторной попытке будет передан тот же RequestId |
| X-Sdk-App-Id | AppId для SDK |
| X-User-Id | UserId |
| X-Room-Id | Romm Id |
| X-Room-Id-Type | Тип RommId, 0 - числовой номер комнаты, 1 - строковый номер комнаты |
| Authorization | Аутентификация в формате Bearer "API-KEY" |

## Параметры запроса

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Text | да | String | Текст голоса |
| Format | нет | String | Желаемый формат аудиовыхода, например Mp3, ogg_opus, pcm, wav, по умолчанию wav. Поддерживаются только PCM и WAV. |
| SampleRate | нет | Integer | Частота дискретизации аудио, по умолчанию 16000 (16k), рекомендуется 16000 |
| Channel | нет | Integer | Аудиоканал, значение: 1 или 2. По умолчанию 1 |

## Ответ

Значение Content-Type необходимо использовать для определения успешности синтеза.

- **В случае успеха** возвращается бинарная речь, различные форматы аудиочастоты Content-Type выглядят следующим образом, необходимо установить в заголовке HTTP-ответа Transfer-Encoding: chunkedã

| Формат аудио | Content-Type |
| --- | --- |
| mp3 | audio/mpeg |
| ogg_opus | audio/ogg |
| pcm | audio/L16 |
| wav | audio/wav |

- **В случае ошибки** возвращается результат JSON с информацией заголовка: Content-type: application/json. Ответ:

```
  {
  "error": {
    "code": "ERROR_CODE",
    "message": "A description of the error"
  }
}
```


---
*Источник: [https://trtc.io/document/65315](https://trtc.io/document/65315)*

---
*Источник (EN): [customize-tts-protocol.md](./customize-tts-protocol.md)*

# Конфигурация преобразования речи в текст

В этом документе описывается, как настроить стороннее решение `STT` в API [StartAIConversation](https://trtc.io/document/64963?product=rtcengine&menulabel=serverfeaturesapis). В настоящее время мы поддерживаем интеграцию с Azure и Deepgram. Если у вас есть другие требования, пожалуйста, [свяжитесь с нами](https://trtc.io/contact).

## Пример запроса

`STTConfig` поддерживает параметр `CustomParam`. См. следующий пример для настройки стороннего решения `STT`:

```
"STTConfig": {    "Language": "zh",    "VadSilenceTime": 1200,    "CustomParam": "{\\"STTType\\": \\"azure\\",                      \\"SubscriptionKey\\": \\"xxxxx\\",                      \\"Region\\": \\"chinanorth3\\"}",  },}
```

## Поддерживаемые конфигурации стороннего STT

### Azure STT

```
{    "STTType": "azure", // required: String STT type    "SubscriptionKey": "xxxxx", // required: String Subscription key    "Region": "chinanorth3" // required: String region}
```

**Пример:**

```
"CustomParam": "{\\"STTType\\": \\"azure\\", \\"SubscriptionKey\\": \\"xxxxx\\", \\"Region\\": \\"chinanorth3\\"}"
```

Дополнительные сведения см. в документации: [https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-to-text](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-to-text).

### Deepgram STT

```
{    "STTType": "deepgram", // required: String STT type    "ApiKey": "XXXXXX", // required: String Authentication    "Model": "nova-2" // required: String Select STT Model}
```

**Пример:**

```
"CustomParam": "{\\"STTType\\": \\"deepgram\\", \\"AppKey\\": \\"xxxxx\\", \\"Model\\": \\"nova-2\\"}"
```

Дополнительные сведения см. в документации: [https://developers.deepgram.com/docs/models-languages-overview](https://developers.deepgram.com/docs/models-languages-overview).


---
*Источник: [https://trtc.io/document/69592](https://trtc.io/document/69592)*

---
*Источник (EN): [speech-to-text-configuration.md](./speech-to-text-configuration.md)*

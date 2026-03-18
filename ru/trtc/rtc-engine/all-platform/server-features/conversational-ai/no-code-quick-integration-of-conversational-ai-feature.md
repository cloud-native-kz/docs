# Быстрая интеграция функции разговорного ИИ без кода

Tencent RTC предоставляет удобную платформу для тестирования и проверки, поддерживающую подключение к возможностям STT, LLM и TTS третьих сторон для быстрой настройки. Она позволяет быстро реализовать услуги разговорного ИИ без написания кода для проверочного тестирования, облегчая эффективную разработку и развертывание. В этой статье описано, как использовать этот инструмент.

## Вход в консоль

1. Создайте приложение RTC Engine: [Консоль Tencent RTC > Создать приложение RTC Engine](https://console.trtc.io/app).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/26eb84e5211111f0a62e525400454e06.png)

2. Нажмите: Начать настройку разговорного ИИ.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/489fb14b211111f0b0b1525400e889b2.png)

3. Выберите No-Code Playground.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/81fb4d73211111f0b47352540044a08e.png)

## Конфигурация ресурсов

Разговорный ИИ поддерживает интеграцию с несколькими поставщиками STT, LLM и TTS. Нажмите **Начать работу**, чтобы быстро настроить, протестировать и интегрировать услуги разговорного ИИ здесь, добиваясь эффективной разработки и развертывания.

> **Примечание:** Нажмите [Попробовать демо](https://trtc.io/demo/homepage/#/detail?scene=ai), чтобы оценить возможности разговорного ИИ. Использование инструмента быстрого тестирования разговорного ИИ будет влечь за собой плату за использование. Дополнительные сведения о биллинге см. в разделе [Биллинг услуг разговорного ИИ](https://trtc.io/document/67833?product=pricing).

## Шаг 1: базовая конфигурация

### 1. Выбор приложения

На странице **Базовая конфигурация** сначала необходимо выбрать приложение, которое вы хотите протестировать. Вы можете включить услугу STT для приложения, чтобы использовать услугу ИИ и функцию автоматического распознавания речи STT путем перехода к **покупке** [**пакетов RTC-Engine Monthly**](https://trtc.io/document/56025?product=pricing) **(включая план Starter)**.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2a43acccedad11efaef452540099c741.png)

### 2. Элементы базовой конфигурации

Мы предоставляем параметры по умолчанию, которые вы можете настроить по своим потребностям. После завершения конфигурации нажмите **Далее**.

- Заполните приветственное сообщение бота.
- Выберите режим прерывания. Он может автоматически прерывать речь робота на основе определённых правил. Этот режим поддерживает как автоматические, так и ручные прерывания. Для подробного описания см. [Интеллектуальное прерывание](https://www.tencentcloud.com/document/product/647/65319).
- Выберите продолжительность прерывания.

## Шаг 2: конфигурация STT (преобразование речи в текст)

Модель конфигурации распознавания речи STT может выбирать между Tencent, Azure и Deepgram. Поддерживает несколько языков, и длительность VAD можно регулировать. Диапазон установки составляет 240-2000. Меньшее значение сделает сегментацию предложений при распознавании речи быстрее. После завершения конфигурации нажмите **Далее**.

Tencent

Azure

Deepgram

При выборе Tencent в качестве поставщика STT мы предоставляем параметры по умолчанию для других конфигураций, которые вы можете настроить по своим потребностям.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/940b3cd6e9b511ef9e13525400454e06.png)

При выборе Azure в качестве поставщика STT:

- APIKey можно получить из [документа с инструкциями](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-recognize-speech?pivots=programming-language-csharp).
- Для региона см. [Поддержка регионов](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/regions).
- Мы предоставляем параметры по умолчанию для других конфигураций; вы можете настроить их по своим потребностям.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/36be7290ed2411efaef452540099c741.png)

При выборе Deepgram в качестве поставщика STT мы предоставляем параметры по умолчанию для других конфигураций; вы можете настроить их по своим потребностям. APIKey можно получить из [Deepgram](https://console.deepgram.com/project/52991c8c-2c62-4492-ba6d-88ca33be6a7b/keys).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4519148fed2411efab2f5254007c27c5.png)

## Шаг 3: конфигурация LLM (большая языковая модель)

На этой странице вам необходимо подать заявку на ресурсы третьих сторон для конфигурации: поставщики LLM поддерживают OpenAI, Deepseek, Minimax, Tencent Hunyuan, Coze и Dify. После завершения конфигурации нажмите **Далее**.

OpenAI

Deepseek

Minimax

Tencent Hunyuan

Coze

Dify

При выборе OpenAI в качестве поставщика LLM это место поддерживает **любую модель LLM, соответствующую стандартному протоколу OpenAI**, такую как Google, Anthropic и т.д. Вы можете самостоятельно настроить параметры модели, URL и ключ для вызова. Когда вы выбираете использование модели, предоставляемой OpenAI, API Key можно получить из [OpenAI](https://platform.openai.com/api-keys).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4ed84befe8e311ef9e13525400454e06.png)

При выборе Deepseek в качестве поставщика LLM мы предоставляем параметры по умолчанию для других конфигураций; вы можете настроить их по своим потребностям. Модель LLM можно просмотреть на [Deepseek](https://api-docs.deepseek.com/zh-cn/), проверив список поддерживаемых моделей, а API Key можно получить из [Deepseek](https://platform.deepseek.com/api_keys).

Кроме официального Deepseek, вы также можете выбрать вызов услуги Deepseek, развёрнутой на платформах облачных сервисов третьих сторон. В соответствии с протоколом OpenAI просто замените параметры модели LLM, URL и ключ ниже.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/67899cd6e8e311efab2f5254007c27c5.png)

При выборе Minimax в качестве поставщика LLM мы предоставляем параметры по умолчанию; вы можете настроить их по своим потребностям. Модель LLM можно свободно выбирать из выпадающего списка, а API Key можно получить из [консоли управления Minimax](https://platform.minimaxi.com/user-center/basic-information/interface-key).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7b3008fce8e311ef922c5254001c06ec.png)

При выборе Hunyuan в качестве поставщика LLM мы предоставляем параметры по умолчанию для других конфигураций; вы можете настроить их по своим потребностям. Модель LLM можно свободно выбирать из выпадающего списка, а API Key можно получить из [управления токенами API](https://console.tencentcloud.com/hunyuan/api-key).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9e53f6eee8e311efaef452540099c741.png)

При выборе Coze в качестве поставщика LLM мы предоставляем параметры по умолчанию для других конфигураций; вы можете настроить их по своим потребностям. API Key можно получить, перейдя на [Coze](https://www.coze.com/open/oauth/pats), чтобы получить маркер Secret, и см. [документ с инструкциями](https://www.coze.com/open/docs/developer_guides/coze_api_overview) для получения BotId.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/aa2802e7e8e311ef93475254005ef0f7.png)

При выборе Dify в качестве поставщика LLM мы предоставляем параметры по умолчанию для других конфигураций; вы можете настроить их по своим потребностям. API Key можно получить из [Dify](https://cloud.dify.ai/datasets?category=api).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b7d81268e8e311ef922c5254001c06ec.png)

## Шаг 4: конфигурация TTS (преобразование текста в речь)

На странице конфигурации TTS (преобразование текста в речь): поставщик TTS поддерживает Tencent, Minimax, Azure, Cartesia, Elevenlabs и пользовательский. После завершения конфигурации нажмите **Подключить**; если информация о конфигурации верна, вы перейдёте на страницу начала разговора.

Cartesia

Azure

Elevenlabs

Пользовательский

Tencent

Minimax

При выборе Cartesia в качестве поставщика TTS:

- APIKey можно получить из [Cartesia](https://play.cartesia.ai/keys).
- Voice ID можно получить из [Cartesia](https://play.cartesia.ai/voices).
- Мы предоставляем параметры по умолчанию для других конфигураций; вы можете настроить их по своим потребностям.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/daec134ee8e511ef9e13525400454e06.png)

При выборе Azure в качестве поставщика TTS:

- SubscriptionKey можно получить, обратившись к [документу с инструкциями](https://learn.microsoft.com/en-us/azure/ai-services/multi-service-resource?pivots=azportal).
- Для региона см. [Поддержка регионов](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/regions).
- Для языка см. [Поддержка языков и звуков](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=stt).
- Мы предоставляем параметры по умолчанию для других конфигураций; вы можете настроить их по своим потребностям.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/dc41de3a88bd11f0bd05525400454e06.png)

При выборе Elevenlabs в качестве поставщика TTS:

- APIKey можно получить из [ElevenLabs](https://elevenlabs.io/app/settings/api-keys).
- Voice ID можно получить из [ElevenLabs](https://elevenlabs.io/app/voice-lab).
- Мы предоставляем параметры по умолчанию для других конфигураций; вы можете настроить их по своим потребностям.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ebc775c8e8ea11efab2f5254007c27c5.png)

- Вы можете обратиться к [пользовательскому протоколу TTS](https://www.tencentcloud.com/document/product/647/65315) для конфигурации.
- Когда поставщик TTS установлен на пользовательский, вы можете заполнить API Key и API Url в соответствии с вашей ситуацией.
- Мы предоставляем параметры по умолчанию для других конфигураций; вы можете настроить их по своим потребностям.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fd1044f9e8ef11ef840e52540044a08e.png)

- При выборе Tencent в качестве поставщика TTS необходимо [активировать услугу TTS приложения](https://console.tencentcloud.com/tts?lang=en), чтобы использовать функцию синтеза речи TTS.
- SecretId можно получить из [документа с инструкциями](https://console.tencentcloud.com/cam/capi?lang=en).
- SecretKey можно получить из [документа с инструкциями](https://console.tencentcloud.com/cam/capi?lang=en). SecretKey можно просмотреть только при создании ключа, пожалуйста, сохраните его вовремя.
- Тип голоса можно получить из [списка голосов](https://www.tencentcloud.com/document/product/1154/48916?lang=en).

Мы предоставляем параметры по умолчанию для других конфигураций; вы можете настроить их по своим потребностям.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/cdebb9bc211311f0948f52540099c741.png)

При выборе Minimax в качестве поставщика TTS:

- APIKey можно получить из [консоли управления Minimax](https://platform.minimaxi.com/user-center/basic-information/interface-key).
- GroupID можно получить из [консоли управления Minimax](https://platform.minimaxi.com/user-center/basic-information).
- Voice ID можно получить, обратившись к [документу с инструкциями](https://platform.minimaxi.com/document/T2A%20V2?key=66719005a427f0c8a5701643).

Мы предоставляем параметры по умолчанию для других конфигураций; вы можете настроить их по своим потребностям.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e9b10911211311f08caa5254005ef0f7.png)

## Описание главной страницы

### Начало разговора

- Подавление шума ИИ: чтобы использовать эту функцию, необходимо активировать [пакеты RTC-Engine Monthly](https://www.tencentcloud.com/document/product/647/56025) версии standard или pro.
- Во время разговора поддерживается редактирование и изменение продолжительности прерывания, конфигурации LLM и конфигурации TTS для облегчения оценки эффектов.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9086cc17e8f411efb98e525400e889b2.png)

- Регион: система по умолчанию выбирает ближайший регион доступа для уменьшения задержки. Вы также можете выбрать регион вручную.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/40e7f810edf511ef840e52540044a08e.png)

- Во время разговора при **отображении кодов ошибок**: обратите внимание, что некоторые коды ошибок могут заблокировать диалог. Измените конфигурацию в соответствии с подсказкой об ошибке своевременно. Если это не может быть разрешено, **скопируйте информацию Task ID и Round ID** и [свяжитесь с нами](https://t.me/+EPk6TMZEZMM5OGY1) для запроса. Некоторые коды ошибок не влияют на нормальный ход диалога, например истечение времени ответа, которое вы можете обработать в соответствии с фактической ситуацией.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/bfc3f27fed2511efab2f5254007c27c5.png)

### Просмотр метрик задержки

Вы можете проверить коэффициент задержки в любой момент во время разговора, чтобы выбрать модель с низкой задержкой.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c2dbe993e8f411efab2f5254007c27c5.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/68cb4d47ed0f11efa1f2525400bf7822.png)

### Быстрая интеграция

Мы поддерживаем быструю реализацию разговорного ИИ в локальной среде пользователей. Параметры, заполненные во время системной конфигурации, были предустановлены и не требуют повторного заполнения (в настоящее время поддерживается веб).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b2c71551e8f411efab2f5254007c27c5.png)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7f4317cce8f411ef93475254005ef0f7.png)


---
*Источник: [https://trtc.io/document/68137](https://trtc.io/document/68137)*

---
*Источник (EN): [no-code-quick-integration-of-conversational-ai-feature.md](./no-code-quick-integration-of-conversational-ai-feature.md)*

# CreateWordSamples

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для массового создания образцов ключевых слов для операций обработки видео, таких как распознавание контента и обнаружение неприемлемой информации с помощью технологий OCR и ASR.

Для этого API можно инициировать максимум 100 запросов в секунду.

Мы рекомендуем вам использовать API Explorer

Попробовать

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: CreateWordSamples. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Usages.N | Да | Array of String | **Использование ключевого слова. Допустимые значения:** 1. Recognition.Ocr: распознавание контента на основе OCR 2. Recognition.Asr: распознавание контента на основе ASR 3. Review.Ocr: распознавание неприемлемой информации на основе OCR 4. Review.Asr: распознавание неприемлемой информации на основе ASR **Допустимы также значения:** 5. Recognition: распознавание контента на основе ASR и OCR; эквивалентно 1+2 6. Review: распознавание неприемлемой информации на основе ASR и OCR; эквивалентно 3+4 7. All: распознавание контента и обнаружение неприемлемой информации на основе ASR и OCR; эквивалентно 1+2+3+4 |
| Words.N | Да | Array of [AiSampleWordInfo](https://www.tencentcloud.com/document/api/1041/33690#AiSampleWordInfo) | Ключевое слово. Ограничение длины массива: 100. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для локализации проблемы. |

## 4. Пример

### Пример1 Создание образца ключевого слова - `All`

Если `Usages` равно `All`, ключевое слово может использоваться для распознавания контента и обнаружения неприемлемой информации на основе OCR и ASR.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=CreateWordSamples
&Usages.0=All
&Words.0.Keyword=Internet celebrity
&Words.0.Tags.0=Entertainment
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

### Пример2 Создание образца ключевого слова - `Review`

Если `Usages` равно `Review`, ключевое слово может использоваться для обнаружения неприемлемой информации на основе OCR и ASR.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=CreateWordSamples
&Usages.0=Review
&Words.0.Keyword=Zhang San
&Words.0.Tags.0=Politics
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

### Пример3 Создание образца ключевого слова - `Recognition`

Если `Usages` равно ["Recognition.Ocr","Review.Ocr"], ключевое слово может использоваться для распознавания контента и обнаружения неприемлемой информации на основе OCR.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=CreateWordSamples
&Usages.0=Recognition.Ocr
&Usages.1=Review.Ocr
&Words.0.Keyword=Internet celebrity
&Words.0.Tags.0=Entertainment
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

## 5. Ресурсы для разработчиков

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы облегчить вам вызов API.

Tencent Cloud SDK 3.0 для Python
Tencent Cloud SDK 3.0 для Java
Tencent Cloud SDK 3.0 для PHP
Tencent Cloud SDK 3.0 для Go
Tencent Cloud SDK 3.0 для Node.js
Tencent Cloud SDK 3.0 для .NET
Tencent Cloud SDK 3.0 для C++

### Интерфейс командной строки

Tencent Cloud CLI 3.0

## 6. Коды ошибок

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Ошибка операции: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue | Некорректное значение параметра. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33688](https://www.tencentcloud.com/document/product/1041/33688)*

---
*Источник (EN): [createwordsamples.md](./createwordsamples.md)*

# ModifyWordSample

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для изменения варианта использования и тега ключевого слова. Само ключевое слово невозможно изменить, но вы можете удалить его и создать новое при необходимости.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызов, проверку подписи, генерацию кода SDK и быстрый поиск API. Он позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: ModifyWordSample. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Keyword | Да | String | Ключевое слово. Ограничение по длине: 128 символов. |
| Usages.N | Нет | Array of String | **Вариант использования ключевого слова. Допустимые значения:** 1. Recognition.Ocr: распознавание содержимого на основе OCR 2. Recognition.Asr: распознавание содержимого на основе ASR 3. Review.Ocr: распознавание неуместной информации на основе OCR 4. Review.Asr: распознавание неуместной информации на основе ASR **Допустимые значения также могут быть:** 5. Recognition: распознавание содержимого на основе ASR и OCR; эквивалентно 1+2 6. Review: распознавание неуместной информации на основе ASR и OCR; эквивалентно 3+4 7. All: эквивалентно 1+2+3+4 |
| TagOperationInfo | Нет | [AiSampleTagOperation](https://www.tencentcloud.com/document/api/1041/33690#AiSampleTagOperation) | Информация об операции с тегом. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, созданный сервером, будет возвращен для каждого запроса (если запрос не достигает сервера по другим причинам, запрос не получит RequestId). RequestId необходим для выявления проблемы. |

## 4. Пример

### Пример 1. Изменение образца ключевого слова

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=ModifyWordSample
&Keyword=Fight
&Usages.0=Review
&TagOperationInfo.Type=reset
&TagOperationInfo.Tags.0=Sensitive information
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

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы упростить вызов API.

Tencent Cloud SDK 3.0 для Python
Tencent Cloud SDK 3.0 для Java
Tencent Cloud SDK 3.0 для PHP
Tencent Cloud SDK 3.0 для Go
Tencent Cloud SDK 3.0 для Node.js
Tencent Cloud SDK 3.0 для .NET
Tencent Cloud SDK 3.0 для C++

### Интерфейс командной строки

Tencent Cloud CLI 3.0

## 6. Код ошибки

Ниже представлены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Ошибка операции: несанкционированный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue | Некорректное значение параметра. |
| ResourceNotFound.Word | Ресурс не найден: ключевое слово. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33682](https://www.tencentcloud.com/document/product/1041/33682)*

---
*Источник (EN): [modifywordsample.md](./modifywordsample.md)*

# CreateAIAnalysisTemplate

## 1. Описание API

Имя домена для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для создания пользовательского шаблона анализа содержимого. Можно создать до 50 шаблонов.

Для этого API можно инициировать максимум 10 запросов в секунду.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: CreateAIAnalysisTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Name | Нет | String | Имя шаблона анализа содержимого видео. Ограничение по длине: 64 символа. |
| Comment | Нет | String | Описание шаблона анализа содержимого видео. Ограничение по длине: 256 символов. |
| ClassificationConfigure | Нет | [ClassificationConfigureInfo](https://www.tencentcloud.com/document/api/1041/33690#ClassificationConfigureInfo) | Параметр управления задачей интеллектуальной категоризации. |
| TagConfigure | Нет | [TagConfigureInfo](https://www.tencentcloud.com/document/api/1041/33690#TagConfigureInfo) | Параметр управления задачей интеллектуального тегирования. |
| CoverConfigure | Нет | [CoverConfigureInfo](https://www.tencentcloud.com/document/api/1041/33690#CoverConfigureInfo) | Параметр управления задачей интеллектуального создания обложки. |
| FrameTagConfigure | Нет | [FrameTagConfigureInfo](https://www.tencentcloud.com/document/api/1041/33690#FrameTagConfigureInfo) | Параметр управления задачей интеллектуального тегирования конкретного кадра. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Уникальный ID шаблона анализа содержимого видео. |
| RequestId | String | Уникальный ID запроса, генерируется сервером и будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример1 Создание шаблона со всеми включенными задачами анализа содержимого

В этом примере показано, как создать пользовательский шаблон анализа содержимого видео со всеми включенными задачами интеллектуального анализа.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=CreateAIAnalysisTemplate
&Name=Intelligent analysis template.
&Comment=Template 3.
&ClassificationConfigure.Switch=ON
&TagConfigure.Switch=ON
&CoverConfigure.Switch=NO
&FrameTagConfigure.Switch=ON
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "Definition": 33,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

### Пример2 Создание шаблона для указания задачи анализа

В этом примере показано, как создать пользовательский шаблон анализа содержимого видео с включенной задачей интеллектуальной классификации.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=CreateAIAnalysisTemplate
&Name=Intelligent analysis template.
&Comment=Template 1.
&ClassificationConfigure.Switch=ON
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "Definition": 30,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

### Пример3 Создание шаблона для указания нескольких задач анализа

В этом примере показано, как создать пользовательский шаблон анализа содержимого видео с включенными задачами интеллектуальной классификации и интеллектуального тегирования.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=CreateAIAnalysisTemplate
&Name=Intelligent analysis template.
&Comment=Template 2.
&ClassificationConfigure.Switch=ON
&TagConfigure.Switch=ON
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "Definition": 31,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

## 5. Ресурсы разработчика

### SDK

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, что облегчает вызов API.

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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Ошибка операции: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue | Неверное значение параметра. |
| InvalidParameterValue.ClassifcationConfigure | Неверное значение параметра: параметр управления для интеллектуальной категоризации неверен. |
| InvalidParameterValue.Comment | Ошибка параметра: описание шаблона. |
| InvalidParameterValue.CoverConfigure | Неверное значение параметра: параметр управления для интеллектуального создания обложки неверен. |
| InvalidParameterValue.Definition | Ошибка параметра: Definition. |
| InvalidParameterValue.FrameTagConfigure | Неверное значение параметра: параметр управления для интеллектуального тегирования конкретного кадра неверен. |
| InvalidParameterValue.Name | Неверное значение параметра: `Name` превышает ограничение по длине. |
| InvalidParameterValue.TagConfigure | Неверное значение параметра: параметр управления для интеллектуального тегирования неверен. |
| LimitExceeded.TooMuchTemplate | Достигнут лимит: количество шаблонов превышает ограничение. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/37470](https://www.tencentcloud.com/document/product/1041/37470)*

---
*Источник (EN): [createaianalysistemplate.md](./createaianalysistemplate.md)*

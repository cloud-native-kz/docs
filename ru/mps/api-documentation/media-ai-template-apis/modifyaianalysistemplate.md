# ModifyAIAnalysisTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для изменения пользовательского шаблона анализа содержимого.

Примечание: шаблоны с ID ниже 10000 являются предустановленными и не могут быть изменены.

Максимум 10 запросов в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Общих параметрах запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: ModifyAIAnalysisTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definition | Да | Integer | Уникальный ID шаблона анализа содержимого видео. |
| Name | Нет | String | Имя шаблона анализа содержимого видео. Ограничение по длине: 64 символа. |
| Comment | Нет | String | Описание шаблона анализа содержимого видео. Ограничение по длине: 256 символов. |
| ClassificationConfigure | Нет | [ClassificationConfigureInfoForUpdate](https://www.tencentcloud.com/document/api/1041/33690#ClassificationConfigureInfoForUpdate) | Параметр управления задачей интеллектуальной категоризации. |
| TagConfigure | Нет | [TagConfigureInfoForUpdate](https://www.tencentcloud.com/document/api/1041/33690#TagConfigureInfoForUpdate) | Параметр управления задачей интеллектуального тегирования. |
| CoverConfigure | Нет | [CoverConfigureInfoForUpdate](https://www.tencentcloud.com/document/api/1041/33690#CoverConfigureInfoForUpdate) | Параметр управления задачей интеллектуального создания обложки. |
| FrameTagConfigure | Нет | [FrameTagConfigureInfoForUpdate](https://www.tencentcloud.com/document/api/1041/33690#FrameTagConfigureInfoForUpdate) | Параметр управления задачей интеллектуального тегирования кадров. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1: Отключение задачи интеллектуального создания обложки

Этот пример показывает, как изменить пользовательский шаблон анализа содержимого видео для отключения задачи интеллектуального создания обложки.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=ModifyAIAnalysisTemplate
&Definition=30
&CoverConfigure.Switch=OFF
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

### Пример 2: Одновременное включение и отключение задач анализа содержимого

Этот пример показывает, как изменить пользовательский шаблон анализа содержимого видео для включения задачи интеллектуального тегирования и отключения задачи интеллектуального создания обложки.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=ModifyAIAnalysisTemplate
&Definition=30
&TagConfigure.Switch=ON
&CoverConfigure.Switch=OFF
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

### Пример 3: Включение задачи интеллектуального создания обложки

Этот пример показывает, как изменить пользовательский шаблон анализа содержимого видео для включения задачи интеллектуального создания обложки.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=ModifyAIAnalysisTemplate
&Definition=30
&CoverConfigure.Switch=ON
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

TencentCloud API 3.0 интегрирует SDK, поддерживающие различные языки программирования, чтобы упростить вызовы API.

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

Ниже приведены только коды ошибок, относящиеся к бизнес-логике API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameterValue.ClassifcationConfigure | Неверное значение параметра: параметр управления для интеллектуальной категоризации некорректен. |
| InvalidParameterValue.Comment | Ошибка параметра: описание шаблона. |
| InvalidParameterValue.CoverConfigure | Неверное значение параметра: параметр управления для интеллектуального создания обложки некорректен. |
| InvalidParameterValue.FrameTagConfigure | Неверное значение параметра: параметр управления для интеллектуального тегирования кадров некорректен. |
| InvalidParameterValue.Name | Неверное значение параметра: `Name` превышает ограничение по длине. |
| InvalidParameterValue.TagConfigure | Неверное значение параметра: параметр управления для интеллектуального тегирования некорректен. |
| ResourceNotFound | Ресурс не существует. |
| ResourceNotFound.TemplateNotExist | Ресурс не существует: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/37464](https://www.tencentcloud.com/document/product/1041/37464)*

---
*Источник (EN): [modifyaianalysistemplate.md](./modifyaianalysistemplate.md)*

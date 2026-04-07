# ModifyContentReviewTemplate

## 1. Описание API

Имя домена для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для изменения пользовательского шаблона модерации контента.

Максимум 10 запросов можно инициировать в секунду для этого API.

Мы рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Он позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: ModifyContentReviewTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definition | Да | Integer | Уникальный идентификатор шаблона модерации контента. |
| Name | Нет | String | Имя шаблона модерации контента. Ограничение длины: 64 символа. |
| Comment | Нет | String | Описание шаблона. Ограничение длины: 256 символов. |
| PornConfigure | Нет | [PornConfigureInfoForUpdate](https://www.tencentcloud.com/document/api/1041/33690#PornConfigureInfoForUpdate) | Контрольный параметр для информации о порнографии |
| TerrorismConfigure | Нет | [TerrorismConfigureInfoForUpdate](https://www.tencentcloud.com/document/api/1041/33690#TerrorismConfigureInfoForUpdate) | Контрольный параметр для информации о терроризме |
| PoliticalConfigure | Нет | [PoliticalConfigureInfoForUpdate](https://www.tencentcloud.com/document/api/1041/33690#PoliticalConfigureInfoForUpdate) | Контрольный параметр для политически чувствительной информации |
| ProhibitedConfigure | Нет | [ProhibitedConfigureInfoForUpdate](https://www.tencentcloud.com/document/api/1041/33690#ProhibitedConfigureInfoForUpdate) | Контрольный параметр обнаружения запрещённой информации. Запрещённая информация включает: Abusive;Drug-related. Примечание: этот параметр пока не поддерживается. |
| UserDefineConfigure | Нет | [UserDefineConfigureInfoForUpdate](https://www.tencentcloud.com/document/api/1041/33690#UserDefineConfigureInfoForUpdate) | Параметры пользовательской модерации контента. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный идентификатор запроса, созданный сервером, будет возвращён для каждого запроса (если запрос не достигнет сервер по другим причинам, запрос не получит RequestId). RequestId необходим для локализации проблемы. |

## 4. Примеры

### Пример 1. Изменение шаблона модерации контента для включения обнаружения порнографии

Этот пример показывает, как изменить пользовательский шаблон модерации контента AI для включения обнаружения порнографии. Используются пороги по умолчанию для нарушения правил и ручного распознавания, и теги не указаны.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=ModifyContentReviewTemplate
&Definition=30
&PornConfigure.ImgReviewInfo.Switch=ON
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "67ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

### Пример 2. Изменение шаблона модерации контента для включения обнаружения порнографии с указанными порогами и тегами

Этот пример показывает, как изменить пользовательский шаблон модерации контента AI для включения обнаружения порнографии. Пороги для нарушения правил и ручного распознавания устанавливаются на 90 и 60 соответственно, и тег указывается как `sexy`.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=ModifyContentReviewTemplate
&Definition=30
&PornConfigure.ImgReviewInfo.Switch=ON
&PornConfigure.ImgReviewInfo.LabelSet.0=sexy
&PornConfigure.ImgReviewInfo.BlockConfidence=90
&PornConfigure.ImgReviewInfo.ReviewConfidence=60
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "82ae8d8e-dce3-4151-9d4b-5594145223e1"
    }
}
```

### Пример 3. Изменение шаблона модерации контента для включения обнаружения порнографии с указанными порогами

Этот пример показывает, как изменить пользовательский шаблон модерации контента AI для включения обнаружения порнографии. Пороги для нарушения правил и ручного распознавания устанавливаются на 90 и 60 соответственно, и теги не указаны.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=ModifyContentReviewTemplate
&Definition=30
&PornConfigure.ImgReviewInfo.Switch=ON
&PornConfigure.ImgReviewInfo.BlockConfidence=90
&PornConfigure.ImgReviewInfo.ReviewConfidence=60
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Для других кодов ошибок см. [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| InternalError | Внутренняя ошибка. |
| InvalidParameter | Ошибка параметра. |
| InvalidParameterValue.BlockConfidence | Неправильное значение параметра: значение параметра `BlockConfidence` недействительно. |
| InvalidParameterValue.Comment | Ошибка параметра: описание шаблона. |
| InvalidParameterValue.LabelSet | Неправильное значение параметра: недействительное значение `LabelSet`. |
| InvalidParameterValue.Name | Неправильное значение параметра: `Name` превышает ограничение длины. |
| InvalidParameterValue.ReviewConfidence | Неправильное значение параметра: значение параметра `ReviewConfidence` недействительно. |
| InvalidParameterValue.Switch | Неправильное значение параметра: недействительное значение `Switch`. |
| ResourceNotFound.TemplateNotExist | Ресурс не существует: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33651](https://www.tencentcloud.com/document/product/1041/33651)*

---
*Источник (EN): [modifycontentreviewtemplate.md](./modifycontentreviewtemplate.md)*

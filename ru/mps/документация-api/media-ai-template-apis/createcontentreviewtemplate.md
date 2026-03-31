# CreateContentReviewTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для создания пользовательского шаблона модерации контента. Всего можно создать до 50 шаблонов.

Максимум 10 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробовать

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически созданные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: CreateContentReviewTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Name | Нет | String | Имя шаблона модерации контента. Ограничение длины: 64 символа. |
| Comment | Нет | String | Описание шаблона. Ограничение длины: 256 символов. |
| PornConfigure | Нет | [PornConfigureInfo](https://www.tencentcloud.com/document/api/1041/33690#PornConfigureInfo) | Параметр управления для задачи обнаружения порнографического контента. |
| TerrorismConfigure | Нет | [TerrorismConfigureInfo](https://www.tencentcloud.com/document/api/1041/33690#TerrorismConfigureInfo) | Параметр управления для задачи обнаружения насилия. |
| PoliticalConfigure | Нет | [PoliticalConfigureInfo](https://www.tencentcloud.com/document/api/1041/33690#PoliticalConfigureInfo) | Параметр управления для задачи обнаружения чувствительного контента. |
| ProhibitedConfigure | Нет | [ProhibitedConfigureInfo](https://www.tencentcloud.com/document/api/1041/33690#ProhibitedConfigureInfo) | Параметр управления обнаружением запрещённой информации. Запрещённая информация включает: оскорбления; наркотики. Примечание: этот параметр пока не поддерживается. |
| UserDefineConfigure | Нет | [UserDefineConfigureInfo](https://www.tencentcloud.com/document/api/1041/33690#UserDefineConfigureInfo) | Параметры пользовательской модерации контента. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Уникальный ID шаблона модерации контента. |
| RequestId | String | Уникальный ID запроса, создаваемый сервером, будет возвращён для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1. Создание шаблона модерации контента для выполнения нескольких задач модерации

Этот пример показывает, как создать пользовательский шаблон AI модерации контента для обнаружения порнографического, террористического и политически чувствительного контента в изображениях, используя пороги по умолчанию для нарушения правил и ручного распознавания, без указания тега фильтра.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=CreateContentReviewTemplate
&Name=Content Moderation Template
&Comment=Template 3
&PornConfigure.ImgReviewInfo.Switch=ON
&TerrorismConfigure.ImgReviewInfo.Switch=ON
&TerrorismConfigure.OcrReviewInfo.Switch=OFF
&PoliticalConfigure.ImgReviewInfo.Switch=ON
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "Definition": 31,
        "RequestId": "97aee3e9-2qd3-4151-9d4b-9730a45227a9"
    }
}
```

### Пример 2. Создание шаблона модерации контента для обнаружения порнографического контента

Этот пример показывает, как создать пользовательский шаблон AI модерации контента для обнаружения порнографического контента в изображениях, используя пороги по умолчанию для нарушения правил и ручного распознавания, без указания тега фильтра.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=CreateContentReviewTemplate
&Name=Content Moderation Template
&Comment=Template 1
&PornConfigure.ImgReviewInfo.Switch=ON
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

### Пример 3. Создание шаблона модерации контента для обнаружения порнографического контента с указанными тегами

Этот пример показывает, как создать пользовательский шаблон AI модерации контента для обнаружения порнографического контента в изображениях, используя пороги по умолчанию для нарушения правил и ручного распознавания, с указанными тегами `porn` и `sexy`.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=CreateContentReviewTemplate
&Name=Content Moderation Module
&Comment=Template 1
&PornConfigure.ImgReviewInfo.Switch=ON
&PornConfigure.ImgReviewInfo.LabelSet.0=porn
&PornConfigure.ImgReviewInfo.LabelSet.1=sexy
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "Definition": 32,
        "RequestId": "88aee3e9-2qd3-4151-9d4b-4390a45227a9"
    }
}
```

### Пример 4. Создание шаблона модерации контента для обнаружения порнографического контента с указанием порога и интервала перехвата кадров

Этот пример показывает, как создать пользовательский шаблон AI модерации контента для обнаружения порнографического контента в изображениях, с пороги для нарушения правил и ручного распознавания установлены на 80 и 30 соответственно.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=CreateContentReviewTemplate
&Name=Content Moderation Template
&Comment=Template 2
&PornConfigure.ImgReviewInfo.Switch=ON
&PornConfigure.ImgReviewInfo.BlockConfidence=80
&PornConfigure.ImgReviewInfo.ReviewConfidence=30
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "Definition": 33,
        "RequestId": "67aee3e9-2qd3-2395-9d4b-4390a96837a7"
    }
}
```

## 5. Ресурсы разработчика

### SDK

TencentCloud API 3.0 интегрирует SDK, которые поддерживают различные языки программирования, чтобы облегчить вызов API.

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
| FailedOperation.InvalidMpsUser | Операция не выполнена: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InternalError.GenDefinition | Внутренняя ошибка: не удалось создать ID шаблона. |
| InvalidParameterValue.BlockConfidence | Некорректное значение параметра: значение параметра `BlockConfidence` недействительно. |
| InvalidParameterValue.Comment | Ошибка параметра: описание шаблона. |
| InvalidParameterValue.LabelSet | Некорректное значение параметра: недействительное значение `LabelSet`. |
| InvalidParameterValue.Name | Некорректное значение параметра: `Name` превышает ограничение длины. |
| InvalidParameterValue.ReviewConfidence | Некорректное значение параметра: значение параметра `ReviewConfidence` недействительно. |
| InvalidParameterValue.Switch | Некорректное значение параметра: недействительное значение `Switch`. |
| LimitExceeded.TooMuchTemplate | Ограничение достигнуто: количество шаблонов превышает лимит. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33675](https://www.tencentcloud.com/document/product/1041/33675)*

---
*Источник (EN): [createcontentreviewtemplate.md](./createcontentreviewtemplate.md)*

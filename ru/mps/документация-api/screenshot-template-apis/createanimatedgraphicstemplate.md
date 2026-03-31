# CreateAnimatedGraphicsTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для создания пользовательского шаблона генерирования анимированного изображения. Можно создать до 16 шаблонов.

Максимум 100 запросов могут быть инициированы в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просматривать запрос, ответ и автоматически генерируемые примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: CreateAnimatedGraphicsTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Fps | Да | Integer | Частота кадров видео в Гц. Диапазон значений: [1, 30]. |
| Width | Нет | Integer | Максимальное значение ширины (или длинной стороны) анимированного изображения в пиксельях. Диапазон значений: 0 и [128, 4096]. Если оба параметра `Width` и `Height` равны 0, разрешение будет таким же, как у исходного видео; если `Width` равен 0, но `Height` не равен 0, `Width` будет масштабирован пропорционально; если `Width` не равен 0, но `Height` равен 0, `Height` будет масштабирован пропорционально; если оба параметра `Width` и `Height` не равны 0, будет использовано пользовательское разрешение. Значение по умолчанию: 0. |
| Height | Нет | Integer | Максимальное значение высоты (или короткой стороны) видеопотока в пиксельях. Диапазон значений: 0 и [128, 4096]. Если оба параметра `Width` и `Height` равны 0, разрешение будет таким же, как у исходного видео; если `Width` равен 0, но `Height` не равен 0, `Width` будет масштабирован пропорционально; если `Width` не равен 0, но `Height` равен 0, `Height` будет масштабирован пропорционально; если оба параметра `Width` и `Height` не равны 0, будет использовано пользовательское разрешение. Значение по умолчанию: 0. |
| ResolutionAdaptive | Нет | String | Адаптация разрешения. Допустимые значения: open: включено. В этом случае `Width` представляет длинную сторону видео, а `Height` — короткую сторону; close: отключено. В этом случае `Width` представляет ширину видео, а `Height` — высоту. Значение по умолчанию: open. |
| Format | Нет | String | Формат анимированного изображения. Допустимые значения: gif; webp. Значение по умолчанию: gif. |
| Quality | Нет | Float | Качество изображения. Диапазон значений: [1, 100]. Значение по умолчанию: 75. |
| Name | Нет | String | Имя шаблона генерирования анимированного изображения. Ограничение по длине: 64 символа. |
| Comment | Нет | String | Описание шаблона. Ограничение по длине: 256 символов. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Уникальный ID шаблона генерирования анимированного изображения. |
| RequestId | String | Уникальный ID запроса, сгенерированный сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1. Создание шаблона генерирования анимированного изображения

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=CreateAnimatedGraphicsTemplate
&Name=Animated image generating template 1
&Width=540
&Height=960
&Format=gif
&Fps=30
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "Definition": 1008,
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Другие коды ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Ошибка операции: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue.Comment | Ошибка параметра: описание шаблона. |
| InvalidParameterValue.Format | Неверное значение параметра: Format. |
| InvalidParameterValue.FormatWebpLackWidthAndHeight | Неверное значение параметра: `Format` — это `webp`, но оба параметра `Width` и `Height` не заполнены. |
| InvalidParameterValue.FormatWebpWidthAndHeightBothZero | Неверное значение параметра: когда `Format` — это `webp`, `Width` и `Height` не могут быть оба 0. |
| InvalidParameterValue.Fps | Ошибка параметра: частота кадров видео. |
| InvalidParameterValue.Name | Неверное значение параметра: `Name` превышает ограничение по длине. |
| InvalidParameterValue.Quality | Неверное значение параметра: Quality. |
| InvalidParameterValue.Resolution | Ошибка параметра: неверное разрешение. |
| LimitExceeded.TooMuchTemplate | Достигнут лимит: количество шаблонов превышает лимит. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33676](https://www.tencentcloud.com/document/product/1041/33676)*

---
*Источник (EN): [createanimatedgraphicstemplate.md](./createanimatedgraphicstemplate.md)*

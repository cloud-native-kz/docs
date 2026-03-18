# ModifyAnimatedGraphicsTemplate

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для изменения пользовательского шаблона генерации анимированного изображения.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуем вам использовать API Explorer

Попробуйте

API Explorer предоставляет широкий спектр возможностей, включая онлайн-вызов, проверку подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: ModifyAnimatedGraphicsTemplate. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| Definition | Да | Integer | Уникальный ID шаблона генерации анимированного изображения. |
| Name | Нет | String | Имя шаблона генерации анимированного изображения. Ограничение по длине: 64 символа. |
| Width | Нет | Integer | Максимальное значение ширины (или длинной стороны) анимированного изображения в px. Диапазон значений: 0 и [128, 4,096]. Если `Width` и `Height` равны 0, разрешение будет таким же, как у исходного видео; Если `Width` равен 0, но `Height` не равен 0, `Width` будет масштабирован пропорционально; Если `Width` не равен 0, но `Height` равен 0, `Height` будет масштабирован пропорционально; Если `Width` и `Height` не равны 0, будет использовано пользовательское разрешение. Значение по умолчанию: 0. |
| Height | Нет | Integer | Максимальное значение высоты (или короткой стороны) видеопотока в px. Диапазон значений: 0 и [128, 4,096]. Если `Width` и `Height` равны 0, разрешение будет таким же, как у исходного видео; Если `Width` равен 0, но `Height` не равен 0, `Width` будет масштабирован пропорционально; Если `Width` не равен 0, но `Height` равен 0, `Height` будет масштабирован пропорционально; Если `Width` и `Height` не равны 0, будет использовано пользовательское разрешение. Значение по умолчанию: 0. |
| ResolutionAdaptive | Нет | String | Адаптация разрешения. Допустимые значения: open: включено. В этом случае `Width` представляет длинную сторону видео, а `Height` — короткую сторону; close: отключено. В этом случае `Width` представляет ширину видео, а `Height` — высоту. Значение по умолчанию: open. |
| Format | Нет | String | Формат анимированного изображения. Допустимые значения: gif, webp. |
| Fps | Нет | Integer | Частота кадров видео в Гц. Диапазон значений: [1, 30]. |
| Quality | Нет | Float | Качество изображения. Диапазон значений: [1, 100]. Значение по умолчанию: 75. |
| Comment | Нет | String | Описание шаблона. Ограничение по длине: 256 символов. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не дошел до сервера по другим причинам, запрос не получит RequestId). RequestId требуется для поиска проблемы. |

## 4. Пример

### Пример1 Изменение шаблона генерации анимированного изображения

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=ModifyAnimatedGraphicsTemplate
&Definition=10001
&Name=Animated image generating template 1
&Width=540
&Height=960
&Fps=30
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

Ниже приведены только коды ошибок, связанные с деловой логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Ошибка операции: неавторизованный пользователь MPS. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue.Comment | Ошибка параметра: описание шаблона. |
| InvalidParameterValue.Format | Некорректное значение параметра: Format. |
| InvalidParameterValue.FormatWebpLackWidthAndHeight | Некорректное значение параметра: `Format` — `webp`, но оба `Width` и `Height` пусты. |
| InvalidParameterValue.FormatWebpWidthAndHeightBothZero | Некорректное значение параметра: когда `Format` — `webp`, `Width` и `Height` не могут быть оба равны 0. |
| InvalidParameterValue.Fps | Ошибка параметра: частота кадров видео. |
| InvalidParameterValue.Name | Некорректное значение параметра: `Name` превышает ограничение по длине. |
| InvalidParameterValue.Quality | Некорректное значение параметра: Quality. |
| InvalidParameterValue.Resolution | Ошибка параметра: Некорректное разрешение. |
| ResourceNotFound.TemplateNotExist | Ресурс не существует: шаблон не существует. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33652](https://www.tencentcloud.com/document/product/1041/33652)*

---
*Источник (EN): [modifyanimatedgraphicstemplate.md](./modifyanimatedgraphicstemplate.md)*

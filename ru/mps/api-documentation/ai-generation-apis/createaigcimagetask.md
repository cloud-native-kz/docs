# CreateAigcImageTask

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для создания задач генерации изображений AIGC.

Максимум 20 запросов можно инициировать в секунду для этого API.

Рекомендуем использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, проверку подписи, генерацию кода SDK и быстрый поиск API. Позволяет просматривать запрос, ответ и автоматически создаваемые примеры.

## 2. Входные параметры

Следующий список параметров запроса предоставляет только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: CreateAigcImageTask. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| ModelName | Нет | String | Имя модели. Поддерживаемые модели: Hunyuan, GEM, Qwen. |
| ModelVersion | Нет | String | Номер конкретной версии модели. По умолчанию система использует поддерживаемую стабильную версию модели. 1. GEM: [2.5 и 3.0]. |
| Prompt | Нет | String | Описание генерируемого изображения. (Примечание: поддерживается максимум 1000 символов.) Этот параметр требуется, если не указано эталонное изображение. |
| NegativePrompt | Нет | String | Указывает содержимое, которое вы хотите предотвратить от создания моделью. Примечание: не все модели это поддерживают. Например: верхнее освещение, яркие цвета, люди, животные, несколько транспортных средств и ветер. |
| EnhancePrompt | Нет | Boolean | Значение по умолчанию — False, что означает, что модель строго следует инструкциям. Для получения лучших результатов с более нюансированными подсказками установите этот параметр в True, чтобы автоматически оптимизировать входную подсказку и улучшить качество генерации. |
| ImageInfos.N | Нет | Массив [AigcImageInfo](https://www.tencentcloud.com/document/api/1041/33690#AigcImageInfo) | Эталонные изображения ресурсов. По умолчанию можно указать одно изображение. Модель, поддерживающая несколько изображений: 1. GEM поддерживает до 3 эталонных изображений. Примечание: 1. Рекомендуемый размер изображения менее 7 МБ. Разные модели имеют разные ограничения. 2. Поддерживаемые форматы изображений: JPEG, PNG и WebP. |
| ExtraParameters | Нет | [AigcImageExtraParam](https://www.tencentcloud.com/document/api/1041/33690#AigcImageExtraParam) | Дополнительные параметры, необходимые для модели. |
| StoreCosParam | Нет | [AigcStoreCosParam](https://www.tencentcloud.com/document/api/1041/33690#AigcStoreCosParam) | Информация о бакете COS для результата файла. Примечание: COS требуется, и необходимо создать и авторизовать роль MPS_QcsRole. |
| Operator | Нет | String | Имя оператора API. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| TaskId | String | Возвращаемый идентификатор задачи. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Пример

### Пример1 Пример запроса

#### Пример входных данных

```
POST / HTTP/1.1
Host:mps.intl.tencentcloudapi.com
Content-Type:application/json
X-TC-Action: CreateAigcImageTask
<Common request parameters>

{
    "Prompt": "draw a cat",
    "Operator": "admin"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e",
        "TaskId": "4-AigcImage-c3b145ec76****94ac55b9e63be17d"
    }
}
```

## 5. Ресурсы для разработчиков

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

Нет кодов ошибок, связанных с бизнес-логикой API. Для других кодов ошибок см. раздел [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).


---
*Источник: [https://www.tencentcloud.com/document/product/1041/76488](https://www.tencentcloud.com/document/product/1041/76488)*

---
*Источник (EN): [createaigcimagetask.md](./createaigcimagetask.md)*

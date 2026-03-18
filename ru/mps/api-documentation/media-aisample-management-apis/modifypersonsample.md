# ModifyPersonSample

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для изменения образцов изображений по ID изображения. Вы можете использовать его для изменения имени и описания образца изображения, а также добавления/удаления/сброса черт лица или тегов. После удаления черт лица должно остаться по крайней мере одно изображение; в противном случае используйте сброс вместо удаления черт лица.

Для этого API можно инициировать максимум 100 запросов в секунду.

Мы рекомендуем вам использовать API Explorer

Попробуйте

API Explorer предоставляет ряд возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет вам просматривать запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательно | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: ModifyPersonSample. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение, используемое для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| PersonId | Да | String | ID изображения |
| Name | Нет | String | Имя. Ограничение по длине: 128 символов. |
| Description | Нет | String | Описание. Ограничение по длине: 1024 символа. |
| Usages.N | Нет | Array of String | Использование изображения. Допустимые значения: 1. Recognition: используется для распознавания контента; эквивалентно `Recognition.Face` 2. Review: используется для распознавания неприемлемой информации; эквивалентно `Review.Face` 3. All: используется для распознавания контента и распознавания неприемлемой информации; эквивалентно 1+2 |
| FaceOperationInfo | Нет | [AiSampleFaceOperation](https://www.tencentcloud.com/document/api/1041/33690#AiSampleFaceOperation) | Информация об операциях над чертами лица |
| TagOperationInfo | Нет | [AiSampleTagOperation](https://www.tencentcloud.com/document/api/1041/33690#AiSampleTagOperation) | Информация об операции с тегом. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Person | [AiSamplePerson](https://www.tencentcloud.com/document/api/1041/33690#AiSamplePerson) | Информация об изображении |
| FailFaceInfoSet | Array of [AiSampleFailFaceInfo](https://www.tencentcloud.com/document/api/1041/33690#AiSampleFailFaceInfo) | Указывает информацию о чертах лица с ошибкой обработки. |
| RequestId | String | Уникальный ID запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не достигнет сервера по другим причинам, запрос не получит RequestId). RequestId требуется для определения проблемы. |

## 4. Примеры

### Пример 1: Изменение образца изображения

Этот пример показывает, как изменить имя и описание образца изображения.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=ModifyPersonSample
&PersonId=10569
&Name=Zhang San
&Description=Chinese-language film and television male actor, Director, Producer
&Usages.0=All
&<Common request parameters>
```

#### Пример выходных данных

```json
{
    "Response": {
        "Person": {
            "PersonId": "10569",
"Name": "Zhang San",
"Description": "Chinese-language film and television male actor, director, producer",
            "FaceInfoSet": [
                {
                    "FaceId": "10046",
                    "Url": "http://www.test.com/9b9e480fe6dd-495e-87a2-b6e01de6492b.png"
                }
            ],
            "TagSet": [
China
star
            ],
            "UsageSet": [
                "All"
            ],
            "CreateTime": "2024-05-18T06:38:18Z",
            "UpdateTime": "2024-05-18T06:38:18Z"
        },
        "FailFaceInfoSet": [
            {
                "Index": 1,
                "ErrCode": 0,
                "Message": "SUCCESS"
            }
        ],
        "RequestId": "240d82aa-3**********60949f7"
    }
}
```

### Пример 2: Изменение образца изображения — `add`

Этот пример показывает, как добавить изображение черты лица и теги к образцу изображения.

#### Пример входных данных

```
https://mps.intl.tencentcloudapi.com/?Action=ModifyPersonSample
&PersonId=10569
&Name=Zhang San
&Description=Chinese-language film and television male actor, Director, Producer
&FaceOperationInfo.Type=add
&FaceOperationInfo.FaceContents.0=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

---
*Источник (EN): [modifypersonsample.md](./modifypersonsample.md)*

# DescribeUsageData

## 1. Описание API

Доменное имя для запроса API: mps.intl.tencentcloudapi.com.

Этот API используется для получения ежедневной информации об использовании Media Processing Service (MPS) в указанном диапазоне времени запроса.

Можно запрашивать статистические данные MPS за последние 365 дней.
Диапазон времени запроса не должен превышать 90 дней.

Максимум 100 запросов можно инициировать в секунду для этого API.

Рекомендуется использовать API Explorer

Попробуйте

API Explorer предоставляет набор возможностей, включая онлайн-вызов, аутентификацию подписи, генерацию кода SDK и быстрый поиск API. Это позволяет просмотреть запрос, ответ и автоматически сгенерированные примеры.

## 2. Входные параметры

Следующий список параметров запроса содержит только параметры запроса API и некоторые общие параметры. Полный список общих параметров см. в разделе [Общие параметры запроса](https://www.tencentcloud.com/document/api/1041/33628).

| Имя параметра | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| Action | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: DescribeUsageData. |
| Version | Да | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Значение для этого API: 2019-06-12. |
| Region | Нет | String | [Общие параметры](https://www.tencentcloud.com/document/api/1041/33628). Этот параметр не требуется для этого API. |
| StartTime | Да | String | Дата начала. Используйте формат даты ISO. |
| EndTime | Да | String | Дата окончания, которая должна быть больше или равна дате начала. Используйте [формат даты и времени ISO](https://www.tencentcloud.comom/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |
| Types.N | Нет | Array of String | Тип задач MPS для запроса. По умолчанию запрашиваются задачи транскодирования.Transcode: транскодирование.Enhance: улучшение.AIAnalysis: интеллектуальный анализ.AIRecognition: интеллектуальное распознавание.AIReview: модерация контента.Snapshot: снимок экрана.AnimatedGraphics: анимированная графика.AiQualityControl: проверка качества.Evaluation: оценка видео.ImageProcess: обработка изображений.AddBlindWatermark: добавление базового цифрового водяного знака авторских прав.AddNagraWatermark: добавление цифровых водяных знаков NAGRA.ExtractBlindWatermark: извлечение базового цифрового водяного знака авторских прав.AIGC: AIGC |
| ProcessRegions.N | Нет | Array of String | Парк MPS. По умолчанию возвращается парк ap-guangzhou. ap-guangzhou: Гуанчжоу.ap-hongkong: Гонконг (Китай).ap-taipei: Тайбэй (Китай).ap-singapore: Сингапур.ap-mumbai: Индия.ap-jakarta: Джакарта.ap-seoul: Сеул.ap-bangkok: Таиланд.ap-tokyo: Япония.na-siliconvalley: Кремниевая долина.na-ashburn: Виргиния.na-toronto: Торонто.sa-saopaulo: Сан-Паулу.eu-frankfurt: Франкфурт.eu-moscow: Россия.aws: AWS. |

## 3. Выходные параметры

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| Data | Array of [TaskStatData](https://www.tencentcloud.com/document/api/1041/33690#TaskStatData) | Обзор статистических данных MPS, в котором отображается обзор и подробные данные запрашиваемой задачи. |
| RequestId | String | Уникальный идентификатор запроса, генерируемый сервером, будет возвращен для каждого запроса (если запрос не доходит до сервера по другим причинам, запрос не получит RequestId). RequestId необходим для определения проблемы. |

## 4. Пример

### Пример1 Запрос использования MPS

Этот пример показывает, как запросить использование.

#### Пример входных данных

```
POST / HTTP/1.1
Host: mps.intl.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeUsageData
<Common request parameters>

{
    "EndTime": "2019-07-03T00:00:00+08:00",
    "StartTime": "2019-07-02T00:00:00+08:00"
}
```

#### Пример выходных данных

```json
{
    "Response": {
        "Data": [
            {
                "TaskType": "Transcode",
                "Summary": [
                    {
                        "Time": "2019-07-02T00:00:00+08:00",
                        "Count": 22,
                        "Usage": 2200
                    },
                    {
                        "Time": "2019-07-03T00:00:00+08:00",
                        "Count": 22,
                        "Usage": 2200
                    }
                ],
                "Details": [
                    {
                        "Specification": "Audio",
                        "Data": [
                            {
                                "Time": "2019-07-02T00:00:00+08:00",
                                "Count": 1,
                                "Usage": 10
                            },
                            {
                                "Time": "2019-07-03T00:00:00+08:00",
                                "Count": 1,
                                "Usage": 10
                            }
                        ]
                    },
                    {
                        "Specification": "Standard.H265.4K",
                        "Data": [
                            {
                                "Time": "2019-07-02T00:00:00+08:00",
                                "Count": 1,
                                "Usage": 10
                            },
                            {
                                "Time": "2019-07-03T00:00:00+08:00",
                                "Count": 1,
                                "Usage": 10
                            }
                        ]
                    },
                    {
                        "Specification": "TESHD-10.H265.4K",
                        "Data": [
                            {
                                "Time": "2019-07-02T00:00:00+08:00",
                                "Count": 1,
                                "Usage": 10
                            },
                            {
                                "Time": "2019-07-03T00:00:00+08:00",
                                "Count": 1,
                                "Usage": 10
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "requestId"
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

Ниже приведены только коды ошибок, связанные с бизнес-логикой API. Другие коды ошибок см. в разделе [Общие коды ошибок](https://www.tencentcloud.com/document/api/1041/33691#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.InvalidMpsUser | Ошибка операции: неавторизованный пользователь MPS. |
| FailedOperation.NetWorkError | Ошибка операции из-за ошибки сети. |
| InternalError | Внутренняя ошибка. |
| InvalidParameterValue | Неверное значение параметра. |
| InvalidParameterValue.Service | Ошибка значения параметра услуги. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/75556](https://www.tencentcloud.com/document/product/1041/75556)*

---
*Источник (EN): [describeusagedata.md](./describeusagedata.md)*

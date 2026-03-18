# Руководство по суммаризации LLM

## Бесплатный пробный период

> **Примечание:** Функциональность MPS Demo относительно проста и предназначена только для ознакомления с базовым эффектом. Для тестирования полной функциональности используйте доступ через API.

1. Откройте [MPS.LIVE](https://mps.live/demo/ai/llm), перейдите на страницу опыта LLM Summarize, выберите Offline Video (Offline File) или Live Streaming и нажмите **One-Click Processing**.
2. После завершения обработки вы сможете просмотреть результаты.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/aa381fcba27a11efa04c5254002693fd.png)

## Интеграция API

### Инициирование задачи суммаризации

Вызовите [API Media Processing Service (MPS)](https://www.tencentcloud.com/document/product/1041/33640), выберите [AiAnalysisTask](https://www.tencentcloud.com/document/api/1041/33690#AiAnalysisTaskInput), установите **Definition** на **22 (предустановленный шаблон суммаризации на основе большой языковой модели (LLM)), и введите параметры расширения в ExtendedParameter** для специальных возможностей. Подробнее см. [Описание параметров расширения](#notes) ниже.

![](https://staticintl.cloudcachetci.com/cms/backend-cms/53be998fa19611efa04c5254002693fd.png)

Пример:

```
{    "InputInfo": {        "Type": "URL",        "UrlInputInfo": {            "Url": "https://facedetectioncos-1251132611.cos.ap-guangzhou.myqcloud.com/video/xxx.mp4" // Replace it with the URL of the video to be summarized.        }    },    "AiAnalysisTask": {        "Definition": 22, //Preset LLM summarize template ID.        "ExtendedParameter": "{\\"des\\":{\\"split\\":{\\"method\\":\\"llm\\",\\"model\\":\\"deepseek-v3\\"}}}"    },    "OutputStorage": {        "CosOutputStorage": {            "Bucket": "test-mps-123456789",            "Region": "ap-guangzhou"        },        "Type": "COS"    },    "OutputDir": "/output/",    "TaskNotifyConfig": {        "NotifyType": "URL",        "NotifyUrl": "http://qq.com/callback/qtatest/?token=xxxxxx"    },    "Action": "ProcessMedia",    "Version": "2019-06-12"}
```

### Быстрая проверка через API Explorer

Вы можете выполнить быструю проверку через [API Explorer](https://console.intl.cloud.tencent.com/api/explorer?Product=mps&Version=2019-06-12&Action=ProcessMedia). После заполнения соответствующей информации параметров на странице вы можете инициировать онлайн-вызов API.

### Описание параметров расширения

ExtendedParameter используется для персонализации задачи суммаризации, может быть оставлен пустым, комбинироваться с эффектом по умолчанию и использоваться по мере необходимости для направлений, которые требуют улучшения.

> **Примечание:** API Explorer автоматически преобразует формат. Вам нужно только ввести соответствующий ExtendedParameter в формате JSON без преобразования его в строку. При прямом вызове API необходимо экранировать строку JSON.

Полный список дополнительных параметров ExtendedParameter и их описания приведены в следующей таблице:

```
{    "des": {      "split": {          "method": "llm",           "model": "deepseek-v3",           "max_split_time_sec": 100,           "extend_prompt": "This video is a medical scenario video, which is segmented according to domain-specific medical knowledge points."      },      "need_ocr": true,      "ocr_type": "ppt",      "only_segment": 0,      "text_requirement": "summary is within 40 characters",      "dstlang": "zh"    }}
```

| Параметр | Обязателен | Тип | Описание |
| --- | --- | --- | --- |
| split.method | Нет | string | Метод сегментации: llm означает сегментацию на основе большой языковой модели, nlp означает традиционную сегментацию на основе NLP. Значение по умолчанию — **llm**. |
| split.model | Нет | string | Сегментация llm: Доступные опции включают Hunyuan, DeepSeek-V3, DeepSeek-R1. Значение по умолчанию — **DeepSeek-V3**. |
| split.max_split_time_sec | Нет | int | Принудительно задает максимальное время сегментации в секундах. Рекомендуется использовать только при необходимости, так как это может повлиять на результат сегментации. Значение по умолчанию — 3600. |
| split.extend_prompt | Нет | string | Требования к подсказкам задачи сегментации. Например: "This instructional video is segmented by knowledge points". Рекомендуется первоначально оставить пустым для тестирования и дополнить подсказки только при неудовлетворительных результатах. |
| need_ocr | Нет | bool | Использовать ли оптическое распознавание символов (OCR) для помощи в сегментации, **true** означает включено. Значение по умолчанию — **false**. Если отключено, система только распознает речевое содержимое видео для помощи в сегментации видео; если включено, она также распознает текстовое содержимое на изображении видео для помощи в сегментации видео. |
| ocr_type | Нет | string | Тип вспомогательного OCR: ppt: Обрабатывает содержимое на экране как слайды PowerPoint и сегментирует видео на основе переходов между слайдами. other: Применяет альтернативные методы сегментации. Значение по умолчанию — **ppt**. |
| only_segment | Нет | int | Выполнять ли только сегментацию без создания резюме. Значение по умолчанию — 0. 1: Только сегментация без создания резюме. 0: Сегментация и создание резюме. |
| text_requirement | Нет | string | Требования к созданию резюме. Например, ограничение по символам "summary is within 40 characters". |
| dstlang | Нет | string | Язык заголовка и резюме. Значение по умолчанию — "zh". "zh": Китайский. "en": Английский. |

### Запрос результатов задачи

- Обратные вызовы задачи: При инициировании задачи MPS с помощью [ProcessMedia](https://www.tencentcloud.com/document/product/1041/33640) вы можете установить информацию об обратном вызове через параметр TaskNotifyConfig. После завершения задачи результаты задачи будут переданы через настроенную информацию об обратном вызове. Вы можете разобрать результаты уведомлений о событиях через [ParseNotification](https://www.tencentcloud.com/document/product/1041/33679).
- Используйте TaskId, возвращаемый [ProcessMedia](https://www.tencentcloud.com/document/product/1041/33640), чтобы вызвать API [DescribeTaskDetail](https://www.tencentcloud.com/document/product/1041/33644) для запроса результатов обработки задачи. Разберите **WorkflowTask > AiAnalysisResultSet > DescriptionTask > Output > DescriptionSet >**[MediaAiAnalysisDescriptionItem](https://www.tencentcloud.com/document/product/1041/33690#mediaaianalysisdescriptionitem).

![](https://staticintl.cloudcachetci.com/cms/backend-cms/9a85c68bee8f11efaef452540099c741.png)

Description соответствует резюме всего видео, а Paragraphs соответствует результатам интеллектуальной сегментации всего видео и резюме каждого сегмента.


---
*Источник: [https://www.tencentcloud.com/document/product/1041/66042](https://www.tencentcloud.com/document/product/1041/66042)*

---
*Источник (EN): [llm-summarize-tutorial.md](./llm-summarize-tutorial.md)*

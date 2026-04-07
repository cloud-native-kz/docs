# Типы данных

## AIAnalysisTemplateItem

Детали интеллектуального аналитического шаблона на основе ИИ

Используется действиями: DescribeAIAnalysisTemplates.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Уникальный ID интеллектуального аналитического шаблона. |
| Name | String | Имя интеллектуального аналитического шаблона. |
| Comment | String | Описание интеллектуального аналитического шаблона. |
| ClassificationConfigure | [ClassificationConfigureInfo](#ClassificationConfigureInfo) | Параметр управления задачей интеллектуальной категоризации. |
| TagConfigure | [TagConfigureInfo](#TagConfigureInfo) | Параметр управления задачей интеллектуального тегирования. |
| CoverConfigure | [CoverConfigureInfo](#CoverConfigureInfo) | Параметр управления задачей интеллектуального создания обложки. |
| FrameTagConfigure | [FrameTagConfigureInfo](#FrameTagConfigureInfo) | Параметр управления задачей интеллектуального тегирования отдельных кадров. |
| CreateTime | String | Время создания шаблона в [формате даты ISO](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52). |
| UpdateTime | String | Время последнего изменения шаблона в [формате даты ISO](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52). |
| Type | String | Тип шаблона. Допустимые значения: * Preset * Custom Примечание: это поле может возвращать `null`, что означает, что допустимое значение получить невозможно. |

## AIRecognitionTemplateItem

Детали шаблона распознавания содержимого видео

Используется действиями: DescribeAIRecognitionTemplates.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Уникальный ID шаблона распознавания содержимого видео. |
| Name | String | Имя шаблона распознавания содержимого видео. |
| Comment | String | Описание шаблона распознавания содержимого видео. |
| FaceConfigure | [FaceConfigureInfo](#FaceConfigureInfo) | Параметр управления распознаванием лиц. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| OcrFullTextConfigure | [OcrFullTextConfigureInfo](#OcrFullTextConfigureInfo) | Параметр управления распознаванием полного текста. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| OcrWordsConfigure | [OcrWordsConfigureInfo](#OcrWordsConfigureInfo) | Параметр управления распознаванием текстовых ключевых слов. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| AsrFullTextConfigure | [AsrFullTextConfigureInfo](#AsrFullTextConfigureInfo) | Параметр управления распознаванием полной речи. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| AsrWordsConfigure | [AsrWordsConfigureInfo](#AsrWordsConfigureInfo) | Параметр управления распознаванием ключевых слов речи. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| TranslateConfigure | [TranslateConfigureInfo](#TranslateConfigureInfo) | Параметры управления переводом голоса. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| CreateTime | String | Время создания шаблона в [формате даты ISO](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |
| UpdateTime | String | Время последнего изменения шаблона в [формате даты ISO](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |
| Type | String | Тип шаблона. Допустимые значения: * Preset * Custom Примечание: это поле может возвращать `null`, что означает, что допустимое значение получить невозможно. |

## Activity

Подзадача схемы.

Используется действиями: CreateSchedule, DescribeSchedules, ModifySchedule.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| ActivityType | String | Да | Тип атомарной задачи. input: начальный узел.. output: узел завершения.. action-trans: указывает транскодирование.. action-samplesnapshot: указывает создание снимков по образцам.. action-AIAnalysis: анализ.. action-AIRecognition: распознавание.. action-aiReview: указывает действие проверки.. action-animated-graphics: указывает анимированное изображение.. action-image-sprite: указывает лист спрайтов.. action-snapshotByTimeOffset: указывает создание снимков по времени.. action-adaptive-substream: указывает потоковое адаптивное кодирование.. action-AIQualityControl: проверка качества медиа.. action-SmartSubtitles: интеллектуальное создание субтитров.. action-exec-rules: правило судства.. action-SmartErase: интеллектуальное стирание.. |
| ReardriveIndex | Array of Integer | Нет | Массив индексов заднего узла. |
| ActivityPara | [ActivityPara](#ActivityPara) | Нет | Параметры подзадачи. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |

## ActivityPara

Подзадача схемы.

Используется действиями: CreateSchedule, ModifySchedule.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| TranscodeTask | [TranscodeTaskInput](#TranscodeTaskInput) | Нет | Задача транскодирования. |
| AnimatedGraphicTask | [AnimatedGraphicTaskInput](#AnimatedGraphicTaskInput) | Нет | Задача создания анимированного снимка. |
| SnapshotByTimeOffsetTask | [SnapshotByTimeOffsetTaskInput](#SnapshotByTimeOffsetTaskInput) | Нет | Задача снимка по времени. |
| SampleSnapshotTask | [SampleSnapshotTaskInput](#SampleSnapshotTaskInput) | Нет | Задача снимка по образцу. |
| ImageSpriteTask | [ImageSpriteTaskInput](#ImageSpriteTaskInput) | Нет | Задача снимка спрайта изображения. |
| AdaptiveDynamicStreamingTask | [AdaptiveDynamicStreamingTaskInput](#AdaptiveDynamicStreamingTaskInput) | Нет | Задача потокового адаптивного кодирования. |
| AiContentReviewTask | [AiContentReviewTaskInput](#AiContentReviewTaskInput) | Нет | Задача модерации содержимого. |
| AiAnalysisTask | [AiAnalysisTaskInput](#AiAnalysisTaskInput) | Нет | Задача анализа содержимого. |
| AiRecognitionTask | [AiRecognitionTaskInput](#AiRecognitionTaskInput) | Нет | Задача распознавания содержимого. |
| QualityControlTask | [AiQualityControlTaskInput](#AiQualityControlTaskInput) | Нет | Задача проверки качества медиа. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| ExecRulesTask | [ExecRulesTask](#ExecRulesTask) | Нет | Условное судство задачи. Примечание: это поле может возвращать null, что означает, что допустимое значение получить невозможно. |
| SmartSubtitlesTask | [SmartSubtitlesTaskInput](#SmartSubtitlesTaskInput) | Нет | Задача интеллектуальных субтитров. Примечание: это поле может возвращать null, что означает, что допустимое значение получить невозможно. |
| SmartEraseTask | [SmartEraseTaskInput](#SmartEraseTaskInput) | Нет | Задача интеллектуального стирания. Примечание: это поле может возвращать null, что означает, что допустимое значение получить невозможно. |

## ActivityResItem

Результаты выполнения подзадач схемы.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| TranscodeTask | [MediaProcessTaskTranscodeResult](#MediaProcessTaskTranscodeResult) | Результат задачи транскодирования. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| AnimatedGraphicTask | [MediaProcessTaskAnimatedGraphicResult](#MediaProcessTaskAnimatedGraphicResult) | Результат задачи создания анимированного изображения. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| SnapshotByTimeOffsetTask | [MediaProcessTaskSnapshotByTimeOffsetResult](#MediaProcessTaskSnapshotByTimeOffsetResult) | Результат задачи снимка по времени. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| SampleSnapshotTask | [MediaProcessTaskSampleSnapshotResult](#MediaProcessTaskSampleSnapshotResult) | Результат задачи снимка по образцу. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| ImageSpriteTask | [MediaProcessTaskImageSpriteResult](#MediaProcessTaskImageSpriteResult) | Результат задачи спрайта изображения. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| AdaptiveDynamicStreamingTask | [MediaProcessTaskAdaptiveDynamicStreamingResult](#MediaProcessTaskAdaptiveDynamicStreamingResult) | Результат задачи потокового адаптивного кодирования. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| RecognitionTask | [ScheduleRecognitionTaskResult](#ScheduleRecognitionTaskResult) | Результат задачи распознавания содержимого. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| ReviewTask | [ScheduleReviewTaskResult](#ScheduleReviewTaskResult) | Результат задачи модерации содержимого. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| AnalysisTask | [ScheduleAnalysisTaskResult](#ScheduleAnalysisTaskResult) | Результат задачи анализа содержимого. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| QualityControlTask | [ScheduleQualityControlTaskResult](#ScheduleQualityControlTaskResult) | Выходные данные задачи проверки качества медиа. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| ExecRuleTask | [ScheduleExecRuleTaskResult](#ScheduleExecRuleTaskResult) | Выходные данные задачи условного судства. Примечание: это поле может возвращать null, что означает, что допустимое значение получить невозможно. |
| SmartSubtitlesTask | [ScheduleSmartSubtitleTaskResult](#ScheduleSmartSubtitleTaskResult) | Выходные данные задачи интеллектуальных субтитров. Примечание: это поле может возвращать null, что означает, что допустимое значение получить невозможно. |
| SmartEraseTask | [SmartEraseTaskResult](#SmartEraseTaskResult) | Выходные данные задачи интеллектуального стирания. Примечание: это поле может возвращать null, что означает, что допустимое значение получить невозможно. |

## ActivityResult

Результат выполнения схемы.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| ActivityType | String | Тип атомарной задачи. Transcode: транскодирование.. SampleSnapshot: указывает создание снимков по образцам.. AnimatedGraphics: указывает анимированное изображение.. SnapshotByTimeOffset: указывает создание снимков по времени.. ImageSprites: указывает лист спрайтов.. AdaptiveDynamicStreaming: потоковое адаптивное кодирование.. AiContentReview: указывает модерацию содержимого.. AIRecognition: интеллектуальное распознавание.. AIAnalysis: указывает анализ ИИ.. AiQualityControl: проверка качества медиа  SmartSubtitles: интеллектуальные субтитры  SmartErase: интеллектуальное стирание.. |
| ActivityResItem | [ActivityResItem](#ActivityResItem) | Результаты выполнения подзадач схемы. |

## AdaptiveDynamicStreamingInfoItem

Информация о потоковом адаптивном кодировании

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Спецификация потокового адаптивного кодирования. |
| Package | String | Формат контейнера. Допустимые значения: HLS, MPEG-DASH. |
| Path | String | Адрес воспроизведения. |
| Storage | [TaskOutputStorage](#TaskOutputStorage) | Место хранения файлов потокового адаптивного кодирования. |

## AdaptiveDynamicStreamingTaskInput

Тип входного параметра потокового адаптивного кодирования

Используется действиями: CreateSchedule, CreateWorkflow, DescribeTaskDetail, ModifySchedule, ParseNotification, ProcessMedia, ResetWorkflow.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Definition | Integer | Да | ID шаблона динамического адаптивного потокового кодирования. |
| WatermarkSet | Array of [WatermarkInput](#WatermarkInput) | Нет | Список водяных знаков. Поддерживается не более 10 водяных знаков (изображение или текст). |
| BlindWatermark | [BlindWatermarkInput](#BlindWatermarkInput) | Нет | Параметр цифрового водяного знака.     Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| OutputStorage | [TaskOutputStorage](#TaskOutputStorage) | Нет | Целевое хранилище файлов после динамического адаптивного потокового кодирования. Если оставить пусто, наследует значение OutputStorage верхнего уровня. Примечание: это поле может возвращать null, что означает, что допустимое значение получить невозможно. |
| OutputObjectPath | String | Нет | Выходной путь для файла манифеста после динамического адаптивного потокового кодирования. Может быть относительным или абсолютным путем. Если необходимо определить выходной путь, путь должен заканчиваться на `.{format}`. Ссылайтесь на [Описание переменных имени файла](https://intl.cloud.tencent.com/document/product/862/37039?from_cn_redirect=1) для имен переменных. Пример относительного пути: filename_{variable name}.{format}filename.{format} Пример абсолютного пути: /custom path/filename_{variable name}.{format} Если не заполнено, по умолчанию используется относительный путь: {inputName}_adaptiveDynamicStreaming_{definition}.{format}. |
| SubStreamObjectName | String | Нет | После динамического адаптивного потокового кодирования выходной путь файлов подпотока может быть только относительным путем. Если не заполнено, по умолчанию используется относительный путь: `{inputName}_adaptiveDynamicStreaming_{definition}_{subStreamNumber}.{format}`. |
| SegmentObjectName | String | Нет | После динамического адаптивного потокового кодирования (только для HLS) выходной путь файлов сегмента может быть только относительным путем. Если не заполнено, по умолчанию используется относительный путь: `{inputName}_adaptiveDynamicStreaming_{definition}_{subStreamNumber}_{segmentNumber}.{format}`. |
| AddOnSubtitles | Array of [AddOnSubtitle](#AddOnSubtitle) | Нет | Функция внешних субтитров указывает файл субтитров для вставки. Примечание: это поле может возвращать null, что означает, что допустимое значение получить невозможно. |
| DrmInfo | [DrmInfo](#DrmInfo) | Нет | Указывает информацию Drm. Примечание: это поле может возвращать null, что означает, что допустимое значение получить невозможно. |
| DefinitionType | String | Нет | Тип шаблона адаптивного транскодирования. Common: тип аудио/видео. PureAudio: только аудио. |
| SubtitleTemplate | [SubtitleTemplate](#SubtitleTemplate) | Нет | Функция жестких субтитров (субтитры подавления), укажите источник субтитров, размер шрифта, позицию и другие параметры субтитров. Примечание: это поле может возвращать null, что означает, что допустимое значение получить невозможно. |
| StdExtInfo | String | Нет | Поле расширения параметра транскодирования. |
| KeyPTSList | Array of Integer | Нет | Указывает кадр в заданное время pts как ключевой кадр и разделяет его на сегменты. единица: миллисекунды (допускается относительное отклонение <=1мс). когда одновременно указаны gop и длительность сегмента, они функционируют вместе. примечание: включите RawPts, сохраняйте частоту кадров как источник и убедитесь, что переданное время pts соответствует кадру в источнике. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |

## AdaptiveDynamicStreamingTemplate

Детали шаблона потокового адаптивного кодирования

Используется действиями: DescribeAdaptiveDynamicStreamingTemplates.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Уникальный ID шаблона потокового адаптивного кодирования. |
| Type | String | Тип шаблона. Допустимые значения: Preset: предустановленный шаблон;Custom: пользовательский шаблон. |
| Name | String | Имя шаблона потокового адаптивного кодирования. |
| Comment | String | Описание шаблона потокового адаптивного кодирования. |
| Format | String | Формат потокового адаптивного кодирования. Допустимые значения: HLS;MPEG-DASH. |
| StreamInfos | Array of [AdaptiveStreamTemplate](#AdaptiveStreamTemplate) | Информация параметра входных потоков для транскодирования в потоковое адаптивное кодирование. Может быть введено до 10 потоков. |
| DisableHigherVideoBitrate | Integer | Запретить ли транскодирование с низкого битрейта на высокий. Допустимые значения: 0: нет,1: да. |
| DisableHigherVideoResolution | Integer | Запретить ли транскодирование с низкого разрешения на высокое. Допустимые значения: 0: нет,1: да. |
| CreateTime | String | Время создания шаблона в [формате даты ISO](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I). |
| UpdateTime | String | Время последнего изменения шаблона в [формате даты ISO](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#I). |
| PureAudio | Integer | Является ли это шаблоном только для аудио. 0: видео-шаблон. 1: шаблон только для аудио.Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| SegmentType | String | Тип сегмента HLS. Допустимые значения: ts-segment: HLS+TS сегмент.ts-byterange: HLS+TS диапазон байтов.mp4-segment: HLS+MP4 сегмент.mp4-byterange: HLS+MP4 диапазон байтов.ts-packed-audio: TS+Упакованный аудио.mp4-packed-audio: MP4+Упакованный аудио. Значение по умолчанию: ts-segment.  Примечание: формат сегмента HLS для потокового адаптивного кодирования основан на этом поле.Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |

## AdaptiveStreamTemplate

Шаблон параметра потокового адаптивного кодирования

Используется действиями: CreateAdaptiveDynamicStreamingTemplate, DescribeAdaptiveDynamicStreamingTemplates, ModifyAdaptiveDynamicStreamingTemplate.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Audio | [AudioTemplateInfo](#AudioTemplateInfo) | Да | Информация параметра аудио. |
| Video | [VideoTemplateInfo](#VideoTemplateInfo) | Нет | Информация параметра видео. |
| RemoveAudio | Integer | Нет | Удалять ли поток аудио. Допустимые значения: 0: нет,1: да. |
| RemoveVideo | Integer | Нет | Удалять ли поток видео. Допустимые значения: 0: нет,1: да. |
| AudioList | Array of [AudioTemplateInfo](#AudioTemplateInfo) | Нет | Список информации параметра аудио. Параметр используется только при объединении нескольких аудиодорожек в адаптивное транскодирование. максимальная длина массива параметров составляет 64.  Примечание: это поле может возвращать null, что означает, что допустимое значение получить невозможно. |

## AddOnSubtitle

Информация о субтитрах для добавления.

Используется действиями: CreateWorkflow, ProcessMedia, ResetWorkflow.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Type | String | Нет | Режим. Допустимые значения: `subtitle-stream`: добавить дорожку субтитров.`close-caption-708`: встроить субтитры CEA-708 в кадры SEI.`close-caption-608`: встроить субтитры CEA-608 в кадры SEI. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| Subtitle | [MediaInputInfo](#MediaInputInfo) | Нет | Файл субтитров. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| SubtitleName | String | Нет | Имя субтитров. Примечание: поддерживает китайские иероглифы, буквы, цифры, пробелы, подчеркивания (_), дефисы (-), точки (.) и скобки. Макс. 64 символа. Примечание: это поле может возвращать null, что означает, что допустимое значение получить невозможно. |
| OutputFormat | String | Нет | Формат вывода субтитров. допустимые значения: "WebVTT", "TTML". Значение по умолчанию: "WebVTT". |
| DefaultTrack | Boolean | Нет | Дорожка субтитров по умолчанию. указывает текущие субтитры как дорожку по умолчанию, когда true. можно указать максимум 1 дорожку субтитров по умолчанию. Значение по умолчанию: `false`. |

## AdvancedSuperResolutionConfig

Конфигурация сверхвысокого разрешения.

Используется действиями: CreateProcessImageTemplate, ModifyProcessImageTemplate, ProcessImage.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Switch | String | Нет | Переключатель конфигурации возможности. Допустимые значения: ON: включено.OFF: отключено. Значение по умолчанию: ON. |
| Type | String | Нет | Тип. Допустимые значения:standard: стандартное сверхвысокое разрешение.super: супер продвинутое сверхвысокое разрешение.ultra: ультра продвинутое сверхвысокое разрешение.Значение по умолчанию: standard. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| Mode | String | Нет | Режим вывода изображения. Значение по умолчанию: percent. aspect: получить большой прямоугольник с указанной шириной и высотой через сверхвысокое разрешение.fixed: получить изображения фиксированной ширины и высоты через сверхвысокое разрешение с поддержкой принудительного масштабирования.percent: коэффициент увеличения сверхвысокого разрешения, который может быть десятичным. Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| Percent | Float | Нет | Коэффициент масштабирования сверхвысокого разрешения, который может быть десятичным.Примечание: используется, когда Mode равен percent.Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| Width | Integer | Нет | Ширина целевого изображения. Значение не может превышать 4096.Примечание: когда Mode равен aspect или fixed, эта конфигурация имеет приоритет.Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| Height | Integer | Нет | Высота целевого изображения. Значение не может превышать 4096.Примечание: когда Mode равен aspect или fixed, эта конфигурация имеет приоритет.Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| LongSide | Integer | Нет | Длина длинной стороны целевого изображения. Значение не может превышать 4096.Примечание: эта конфигурация используется, когда Mode равен aspect или fixed и поля Width и Height не указаны.Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |
| ShortSide | Integer | Нет | Длина короткой стороны целевого изображения. Значение не может превышать 4096.Примечание: эта конфигурация используется, когда Mode равен aspect или fixed и поля Width и Height не указаны.Примечание: это поле может возвращать null, что означает, что допустимые значения получить невозможно. |

## AiAnalysisResult

Результаты интеллектуального анализа

## AiAnalysisTaskDelLogoInput

Тип входных данных задачи интеллектуального удаления.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона интеллектуального удаления. |

## AiAnalysisTaskDelLogoOutput

Результат интеллектуального удаления.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Path | String | Путь файла после удаления. |
| OutputStorage | [TaskOutputStorage](#TaskOutputStorage) | Расположение хранилища файла после удаления. |
| OriginSubtitlePath | String | Путь файла субтитров, извлеченного из видео. |
| TranslateSubtitlePath | String | Путь файла перевода субтитров, извлеченного из видео. |
| SubtitlePos | [SubtitlePosition](#SubtitlePosition) | Положение удаленного субтитра. Примечание: это поле действительно только при извлечении субтитров, когда включена опция возврата позиций субтитров. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |
| VoiceClonedVideo | String | Указывает URL файла видео после клонирования голоса. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |
| VoiceClonedMarkFile | String | Указывает адрес файла аннотации клона типа голоса. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |

## AiAnalysisTaskDelLogoResult

Тип результата интеллектуального удаления.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи, включая PROCESSING, SUCCESS и FAIL. |
| ErrCode | Integer | Код ошибки. `0`: задача выполнена успешно. Другие значения: задача не выполнена. |
| Message | String | Сообщение об ошибке. |
| Input | [AiAnalysisTaskDelLogoInput](#AiAnalysisTaskDelLogoInput) | Входные данные задачи интеллектуального удаления. |
| Output | [AiAnalysisTaskDelLogoOutput](#AiAnalysisTaskDelLogoOutput) | Выходные данные задачи интеллектуального удаления. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |

## AiAnalysisTaskDescriptionInput

Тип входных данных задачи интеллектуальной классификации.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона интеллектуального описания. |

## AiAnalysisTaskDescriptionOutput

Информация о результате интеллектуального описания.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| DescriptionSet | Array of [MediaAiAnalysisDescriptionItem](#MediaAiAnalysisDescriptionItem) | Список интеллектуальных описаний видео. |

## AiAnalysisTaskDescriptionResult

Тип результата интеллектуального описания.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи, включая PROCESSING, SUCCESS и FAIL. |
| ErrCode | Integer | Код ошибки. `0`: задача выполнена успешно. Другие значения: задача не выполнена. |
| Message | String | Сообщение об ошибке. |
| Input | [AiAnalysisTaskDescriptionInput](#AiAnalysisTaskDescriptionInput) | Входные данные задачи интеллектуального описания. |
| Output | [AiAnalysisTaskDescriptionOutput](#AiAnalysisTaskDescriptionOutput) | Выходные данные задачи интеллектуального описания. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |

## AiAnalysisTaskDubbingInput

Тип входных данных задачи интеллектуального перевода.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона перевода видео. |

## AiAnalysisTaskDubbingOutput

Информация о результате интеллектуального перевода.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| VideoPath | String | Указывает путь видео для перевода. |
| SpeakerPath | String | Указывает путь файла тега. |
| VoiceId | String | ID типа голоса. |
| OutputStorage | [TaskOutputStorage](#TaskOutputStorage) | Указывает расположение хранилища перекодированного видео. |

## AiAnalysisTaskDubbingResult

Тип результата интеллектуального перевода.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи, включая PROCESSING, SUCCESS и FAIL. |
| ErrCode | Integer | Код ошибки. `0`: задача выполнена успешно. Другие значения: задача не выполнена. |
| Message | String | Сообщение об ошибке. |
| Input | [AiAnalysisTaskDubbingInput](#AiAnalysisTaskDubbingInput) | Описывает входные данные задачи интеллектуального перевода. |
| Output | [AiAnalysisTaskDubbingOutput](#AiAnalysisTaskDubbingOutput) | Описывает выходные данные задачи интеллектуального перевода. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |

## AiAnalysisTaskFrameTagInput

Тип входных данных задачи интеллектуального теггирования кадров

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона интеллектуального теггирования видео по кадрам. |

## AiAnalysisTaskFrameTagOutput

Информация о результате интеллектуального теггирования кадров

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| SegmentSet | Array of [MediaAiAnalysisFrameTagSegmentItem](#MediaAiAnalysisFrameTagSegmentItem) | Список тегов видео по кадрам. |

## AiAnalysisTaskFrameTagResult

Тип результата интеллектуального теггирования кадров

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: PROCESSING, SUCCESS, FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи; любое другое возвращаемое значение указывает на ошибку задачи. Подробнее см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/1041/40249). |
| ErrCode | Integer | Код ошибки. 0 указывает на успешное выполнение задачи; в противном случае задача не выполнена. Этот параметр больше не рекомендуется. Рекомендуется использовать новый параметр кода ошибки ErrCodeExt. |
| Message | String | Сообщение об ошибке. |
| Input | [AiAnalysisTaskFrameTagInput](#AiAnalysisTaskFrameTagInput) | Входные данные задачи интеллектуального теггирования кадров. |
| Output | [AiAnalysisTaskFrameTagOutput](#AiAnalysisTaskFrameTagOutput) | Выходные данные задачи интеллектуального теггирования кадров. |

## AiAnalysisTaskHeadTailInput

Тип входных данных задачи распознавания открывающих и закрывающих сегментов.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона распознавания открывающих и закрывающих сегментов. |

## AiAnalysisTaskHeadTailOutput

Результат распознавания открывающих и закрывающих сегментов.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| HeadTimeOffset | Float | PTS открывающего сегмента. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |
| TailTimeOffset | Float | PTS закрывающего сегмента. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |

## AiAnalysisTaskHeadTailResult

Тип результата распознавания открывающих и закрывающих сегментов.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи, включая PROCESSING, SUCCESS и FAIL. |
| ErrCode | Integer | Код ошибки. `0`: задача выполнена успешно. Другие значения: задача не выполнена. |
| Message | String | Сообщение об ошибке. |
| Input | [AiAnalysisTaskHeadTailInput](#AiAnalysisTaskHeadTailInput) | Входные данные задачи распознавания открывающих и закрывающих сегментов. |
| Output | [AiAnalysisTaskHeadTailOutput](#AiAnalysisTaskHeadTailOutput) | Выходные данные задачи распознавания открывающих и закрывающих сегментов. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |

## AiAnalysisTaskHighlightInput

Входные данные задачи интеллектуального создания выделений.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона интеллектуального создания выделений. |

## AiAnalysisTaskHighlightOutput

Выходные данные задачи интеллектуального создания выделений.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| HighlightSet | Array of [MediaAiAnalysisHighlightItem](#MediaAiAnalysisHighlightItem) | Список сегментов выделений. |
| OutputStorage | [TaskOutputStorage](#TaskOutputStorage) | Расположение хранилища сегментов выделений. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |

## AiAnalysisTaskHighlightResult

Результат задачи интеллектуального создания выделений.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: `PROCESSING`, `SUCCESS`, `FAIL`. |
| ErrCode | Integer | Код ошибки. `0`: задача выполнена успешно; другие значения: задача не выполнена. |
| Message | String | Сообщение об ошибке. |
| Input | [AiAnalysisTaskHighlightInput](#AiAnalysisTaskHighlightInput) | Входные данные задачи интеллектуального создания выделений. |
| Output | [AiAnalysisTaskHighlightOutput](#AiAnalysisTaskHighlightOutput) | Выходные данные задачи интеллектуального создания выделений. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |

## AiAnalysisTaskHorizontalToVerticalInput

Тип входных данных задачи интеллектуального преобразования альбомной в портретную ориентацию.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона интеллектуального преобразования альбомной в портретную ориентацию. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |

## AiAnalysisTaskHorizontalToVerticalOutput

Результат интеллектуального преобразования альбомной в портретную ориентацию.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Path | String | Список видео с интеллектуальным преобразованием альбомной в портретную ориентацию. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |
| OutputStorage | [TaskOutputStorage](#TaskOutputStorage) | Расположение хранилища видео с интеллектуальным преобразованием альбомной в портретную ориентацию. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |
| Confidence | Float | Уверенность.       Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |

## AiAnalysisTaskHorizontalToVerticalResult

Тип результата интеллектуального преобразования альбомной в портретную ориентацию.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи, включая PROCESSING, SUCCESS и FAIL. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |
| ErrCode | Integer | Код ошибки. 0: задача выполнена успешно. Другие значения: задача не выполнена.  Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |
| Message | String | Сообщение об ошибке  Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |
| Input | [AiAnalysisTaskHorizontalToVerticalInput](#AiAnalysisTaskHorizontalToVerticalInput) | Входные данные задачи интеллектуального преобразования альбомной в портретную ориентацию. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |
| Output | [AiAnalysisTaskHorizontalToVerticalOutput](#AiAnalysisTaskHorizontalToVerticalOutput) | Выходные данные задачи интеллектуального преобразования альбомной в портретную ориентацию. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |

## AiAnalysisTaskInput

Типы входных параметров для интеллектуального анализа видео ИИ

Используется действиями: CreateSchedule, CreateWorkflow, DescribeTaskDetail, DescribeWorkflows, ModifySchedule, ParseNotification, ProcessLiveStream, ProcessMedia, ResetWorkflow.

| Имя | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| Definition | Integer | Да | ID шаблона анализа содержимого видео. |
| ExtendedParameter | String | Нет | Дополнительный параметр. Его значение представляет собой сериализованную строку JSON. Примечание: этот параметр используется для соответствия требованиям индивидуализации. Ссылки: [Руководство Smart Erase]: https://intl.cloud.tencent.com/document/product/862/101530?from_cn_redirect=1 [Разделение видео (длинные видео в короткие видео) Руководство](https://intl.cloud.tencent.com/document/product/862/112098?from_cn_redirect=1) [Руководство по интеллектуальным выделениям](https://intl.cloud.tencent.com/document/product/862/107280?from_cn_redirect=1) [Руководство по преобразованию альбомной в портретную ориентацию](https://intl.cloud.tencent.com/document/product/862/112112?from_cn_redirect=1) Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |

## AiAnalysisTaskReelInput

Тип входных данных задачи интеллектуального редактирования видео.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона интеллектуального редактирования видео. |

## AiAnalysisTaskReelOutput

Информация о результате переозвучивания и пересоздания видео ИИ.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| VideoPath | String | Путь выходного видео. |
| VideoPaths | Array of String | Список путей выходных видео.  **Примечание**:. 1. при возврате файла `VideoPath` возвращает путь файла, и `VideoPaths` аналогично заполняет элемент с тем же путем. 2. при возврате нескольких файлов `VideoPath` возвращает пустую строку, и `VideoPaths` возвращает список путей файлов. |
| ScriptPath | String | Путь файла сценария. |
| OutputStorage | [TaskOutputStorage](#TaskOutputStorage) | Расположение хранилища выходного видео. |

## AiAnalysisTaskReelResult

Тип результата переозвучивания и пересоздания видео ИИ.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: PROCESSING, SUCCESS и FAIL. |
| ErrCode | Integer | Код ошибки. 0: задача выполнена успешно. Другие значения: задача не выполнена. |
| Message | String | Сообщение об ошибке. |
| Input | [AiAnalysisTaskReelInput](#AiAnalysisTaskReelInput) | Входные данные задачи переозвучивания и пересоздания видео ИИ. |
| Output | [AiAnalysisTaskReelOutput](#AiAnalysisTaskReelOutput) | Выходные данные задачи переозвучивания и пересоздания видео ИИ. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи, а другие значения указывают на ошибку задачи. Допустимые значения см. в списке кодов ошибок MPS. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |
| Progress | Integer | Ход выполнения задачи. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |
| BeginProcessTime | String | Время начала задачи в формате даты и времени ISO. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |
| FinishTime | String | Время завершения задачи в формате даты и времени ISO. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |

## AiAnalysisTaskSegmentInput

Тип входных данных задачи разделения.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона задачи разделения. |

## AiAnalysisTaskSegmentOutput

Результат интеллектуального разделения.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| SegmentSet | Array of [SegmentRecognitionItem](#SegmentRecognitionItem) | Список подсегментов интеллектуального разделения. |
| Abstract | String | Аннотация видео, используется для автономных сценариев. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |

## AiAnalysisTaskSegmentResult

Тип результата разделения.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи, включая PROCESSING, SUCCESS и FAIL. |
| ErrCode | Integer | Код ошибки. `0`: задача выполнена успешно. Другие значения: задача не выполнена. |
| Message | String | Сообщение об ошибке. |
| Input | [AiAnalysisTaskSegmentInput](#AiAnalysisTaskSegmentInput) | Входные данные задачи разделения. |
| Output | [AiAnalysisTaskSegmentOutput](#AiAnalysisTaskSegmentOutput) | Выходные данные задачи разделения. Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |

## AiAnalysisTaskTagInput

Тип входных данных задачи интеллектуального теггирования

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона интеллектуального теггирования видео. |

## AiAnalysisTaskTagOutput

Информация о результате интеллектуального теггирования

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| TagSet | Array of [MediaAiAnalysisTagItem](#MediaAiAnalysisTagItem) | Список интеллектуально созданных тегов видео. |

## AiAnalysisTaskTagResult

Тип результата задачи интеллектуального теггирования

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: PROCESSING, SUCCESS, FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи; любое другое возвращаемое значение указывает на ошибку задачи. Подробнее см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/1041/40249). |
| ErrCode | Integer | Код ошибки. 0 указывает на успешное выполнение задачи; в противном случае задача не выполнена. Этот параметр больше не рекомендуется. Рекомендуется использовать новый параметр кода ошибки ErrCodeExt. |
| Message | String | Сообщение об ошибке. |
| Input | [AiAnalysisTaskTagInput](#AiAnalysisTaskTagInput) | Входные данные задачи интеллектуального теггирования. |
| Output | [AiAnalysisTaskTagOutput](#AiAnalysisTaskTagOutput) | Выходные данные задачи интеллектуального теггирования. |

## AiAnalysisTaskVideoComprehensionInput

Входной файл задачи распознавания видео (аудио).

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона распознавания видео (аудио). |

## AiAnalysisTaskVideoComprehensionOutput

Информация о результате выходных данных задачи распознавания видео (аудио).

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| VideoComprehensionAnalysisResult | String | Детали выходных данных задачи распознавания видео (аудио). |
| VideoComprehensionExtInfo | String | Расширенная информация видео (аудио). |
| VideoComprehensionResultList | Array of [VideoComprehensionResultItem](#VideoComprehensionResultItem) | Результат понимания видеоклипа. |

## AiAnalysisTaskVideoComprehensionResult

Результат распознавания видео (аудио).

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: `PROCESSING`, `SUCCESS` и `FAIL`. |
| ErrCode | Integer | Код ошибки. 0: успешно; другие значения: ошибка. |
| Message | String | Сообщение об ошибке. |
| Input | [AiAnalysisTaskVideoComprehensionInput](#AiAnalysisTaskVideoComprehensionInput) | Входной файл для распознавания видео (аудио). |
| Output | [AiAnalysisTaskVideoComprehensionOutput](#AiAnalysisTaskVideoComprehensionOutput) | Выходной файл для распознавания видео (аудио). Примечание: это поле может возвращать null, указывая, что получено никакого действительного значения. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи, а другие значения указывают на ошибку задачи. Допустимые значения см. в списке кодов ошибок MPS. |
| Progress | Integer | Ход выполнения задачи |
| BeginProcessTime | String | Время начала выполнения задачи в формате даты и времени ISO. |
| FinishTime | String | Время завершения выполнения задачи в формате даты и времени ISO. |

## AiAnalysisTaskVideoRemakeInput

Тип входных данных задачи удаления дубликатов видео.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона интеллектуального удаления дубликатов. |

## AiAnalysisTaskVideoRemakeOutput

Информация о результате удаления дубликатов видео.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Path | String | Указывает путь файла для интеллектуального удаления дубликатов видео. |
| OutputStorage | [TaskOutputStorage](#TaskOutputStorage) | Указывает расположение хранилища для интеллектуального удаления дубликатов видео. |

## AiAnalysisTaskVideoRemakeResult

Структура данных результата удаления дубликатов видео.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Указывает статус задачи. допустимые значения: `PROCESSING`, `SUCCESS` и `FAIL`. |
| ErrCode | Integer | Код ошибки. 0: успешно. другие значения: ошибка. |
| Message | String | Сообщение об ошибке. |
| Input | [AiAnalysisTaskVideoRemake

## AiRecognitionTaskAsrFullTextResultOutput

Полный результат распознавания речи.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| SegmentSet | Array of [AiRecognitionTaskAsrFullTextSegmentItem](#AiRecognitionTaskAsrFullTextSegmentItem) | Список сегментов полного распознавания речи. |
| SubtitlePath | String | Адрес файла субтитров. |

## AiRecognitionTaskAsrFullTextSegmentItem

Сегмент полного распознавания речи.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Confidence | Float | Уверенность сегмента распознавания. Диапазон значений: 0–100. |
| StartTimeOffset | Float | Временное смещение начала сегмента распознавания в секундах. |
| EndTimeOffset | Float | Временное смещение конца сегмента распознавания в секундах. |
| Text | String | Распознанный текст. |
| Wordlist | Array of [WordResult](#WordResult) | Информация о временных метках слов. |

## AiRecognitionTaskAsrWordsResult

Результат распознавания ключевых слов речи.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: PROCESSING, SUCCESS, FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи; любое другое значение указывает на сбой. Подробнее см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1041/40249). |
| ErrCode | Integer | Код ошибки. 0 указывает на успешное выполнение задачи; в противном случае произошел сбой. Этот параметр больше не рекомендуется. Рекомендуется использовать новый параметр кода ошибки ErrCodeExt. |
| Message | String | Сообщение об ошибке. |
| Input | [AiRecognitionTaskAsrWordsResultInput](#AiRecognitionTaskAsrWordsResultInput) | Входная информация задачи распознавания ключевых слов речи. |
| Output | [AiRecognitionTaskAsrWordsResultOutput](#AiRecognitionTaskAsrWordsResultOutput) | Выходная информация задачи распознавания ключевых слов речи. Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |

## AiRecognitionTaskAsrWordsResultInput

Входные данные для распознавания ключевых слов речи.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона распознавания ключевых слов речи. |

## AiRecognitionTaskAsrWordsResultItem

Результат распознавания ключевых слов речи.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Word | String | Ключевое слово речи. |
| SegmentSet | Array of [AiRecognitionTaskAsrWordsSegmentItem](#AiRecognitionTaskAsrWordsSegmentItem) | Список временных сегментов, содержащих ключевое слово речи. |

## AiRecognitionTaskAsrWordsResultOutput

Выходные данные распознавания ключевых слов речи.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| ResultSet | Array of [AiRecognitionTaskAsrWordsResultItem](#AiRecognitionTaskAsrWordsResultItem) | Набор результатов распознавания ключевых слов речи. |

## AiRecognitionTaskAsrWordsSegmentItem

Сегмент распознавания речи.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| StartTimeOffset | Float | Временное смещение начала сегмента распознавания в секундах. |
| EndTimeOffset | Float | Временное смещение конца сегмента распознавания в секундах. |
| Confidence | Float | Уверенность сегмента распознавания. Диапазон значений: 0–100. |

## AiRecognitionTaskFaceResult

Результат распознавания лиц.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: PROCESSING, SUCCESS, FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи; любое другое значение указывает на сбой. Подробнее см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1041/40249). |
| ErrCode | Integer | Код ошибки. 0 указывает на успешное выполнение задачи; в противном случае произошел сбой. Этот параметр больше не рекомендуется. Рекомендуется использовать новый параметр кода ошибки ErrCodeExt. |
| Message | String | Сообщение об ошибке. |
| Input | [AiRecognitionTaskFaceResultInput](#AiRecognitionTaskFaceResultInput) | Входная информация задачи распознавания лиц. |
| Output | [AiRecognitionTaskFaceResultOutput](#AiRecognitionTaskFaceResultOutput) | Выходная информация задачи распознавания лиц. Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |

## AiRecognitionTaskFaceResultInput

Входные данные для распознавания лиц.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона распознавания лиц. |

## AiRecognitionTaskFaceResultItem

Результат распознавания лиц

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Id | String | Уникальный ID лица. |
| Type | String | Тип библиотеки лиц, указывающий на принадлежность распознанного лица: Default: Библиотека лиц по умолчанию; UserDefine: Пользовательская библиотека лиц. |
| Name | String | Имя лица. |
| SegmentSet | Array of [AiRecognitionTaskFaceSegmentItem](#AiRecognitionTaskFaceSegmentItem) | Набор результатов сегментов, содержащих лицо. |
| Gender | String | Пол человека. Male: мужчина. Female: женщина. |
| Birthday | String | Дата рождения. |
| Profession | String | Профессия или должность человека. |
| SchoolOfGraduation | String | Учебное заведение, окончившее лицо. |
| Abstract | String | Описание человека. |
| PlaceOfBirth | String | Место рождения или происхождения. |
| PersonType | String | Тип человека. Politician: государственное лицо. Artist: артист. |
| Remark | String | Отметка чувствительности. Normal: нормально. Sensitive: чувствительно. |
| Url | String | Ссылка на снимок экрана. |

## AiRecognitionTaskFaceResultOutput

Выходные данные интеллектуального распознавания лиц.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| ResultSet | Array of [AiRecognitionTaskFaceResultItem](#AiRecognitionTaskFaceResultItem) | Набор результатов интеллектуального распознавания лиц. |

## AiRecognitionTaskFaceSegmentItem

Сегмент результата распознавания лиц

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| StartTimeOffset | Float | Временное смещение начала сегмента распознавания в секундах. |
| EndTimeOffset | Float | Временное смещение конца сегмента распознавания в секундах. |
| Confidence | Float | Уверенность сегмента распознавания. Диапазон значений: 0–100. |
| AreaCoordSet | Array of Integer | Координаты зоны результата распознавания. Массив содержит четыре элемента: [x1,y1,x2,y2], т. е. горизонтальные и вертикальные координаты верхнего левого и нижнего правого углов. |

## AiRecognitionTaskInput

Тип входного параметра распознавания содержимого видео

Используется действиями: CreateSchedule, CreateWorkflow, DescribeTaskDetail, DescribeWorkflows, ModifySchedule, ParseNotification, ProcessLiveStream, ProcessMedia, ResetWorkflow.

| Имя | Тип | Обязательный | Описание |
| --- | --- | --- | --- |
| Definition | Integer | Да | ID шаблона интеллектуального распознавания видео. |
| UserExtPara | String | Нет | Поле расширения пользователя, которое не требуется заполнять в общих сценариях. |

## AiRecognitionTaskObjectResult

Результат распознавания объектов.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи, включая PROCESSING, SUCCESS и FAIL. |
| ErrCode | Integer | Код ошибки. `0`: Задача выполнена успешно. Другие значения: Задача не выполнена. |
| Message | String | Сообщение об ошибке. |
| Input | [AiRecognitionTaskObjectResultInput](#AiRecognitionTaskObjectResultInput) | Входные данные задачи распознавания объектов. |
| Output | [AiRecognitionTaskObjectResultOutput](#AiRecognitionTaskObjectResultOutput) | Выходные данные задачи распознавания объектов. Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |

## AiRecognitionTaskObjectResultInput

Тип входных данных задачи распознавания объектов.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона распознавания объектов. |

## AiRecognitionTaskObjectResultItem

Результат распознавания одного объекта.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Name | String | Имя распознанного объекта. |
| SegmentSet | Array of [AiRecognitionTaskObjectSeqmentItem](#AiRecognitionTaskObjectSeqmentItem) | Список сегментов, содержащих объект. |

## AiRecognitionTaskObjectResultOutput

Выходные данные интеллектуального распознавания объектов.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| ResultSet | Array of [AiRecognitionTaskObjectResultItem](#AiRecognitionTaskObjectResultItem) | Набор результатов интеллектуального распознавания объектов. |

## AiRecognitionTaskObjectSeqmentItem

Сегмент результата распознавания объектов.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| StartTimeOffset | Float | Временное смещение начала распознанного сегмента в секундах. |
| EndTimeOffset | Float | Временное смещение конца распознанного сегмента в секундах. |
| Confidence | Float | Уверенность распознанного сегмента. Диапазон значений: 0–100. |
| AreaCoordSet | Array of Integer | Координаты зоны результата распознавания. Массив содержит четыре элемента: [x1, y1, x2, y2], представляющие горизонтальные и вертикальные координаты верхнего левого и нижнего правого углов соответственно. |

## AiRecognitionTaskOcrFullTextResult

Результат полного распознавания текста.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: PROCESSING, SUCCESS, FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи; любое другое значение указывает на сбой. Подробнее см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1041/40249). |
| ErrCode | Integer | Код ошибки. 0 указывает на успешное выполнение задачи; в противном случае произошел сбой. Этот параметр больше не рекомендуется. Рекомендуется использовать новый параметр кода ошибки ErrCodeExt. |
| Message | String | Сообщение об ошибке. |
| Input | [AiRecognitionTaskOcrFullTextResultInput](#AiRecognitionTaskOcrFullTextResultInput) | Входная информация задачи полного распознавания текста. |
| Output | [AiRecognitionTaskOcrFullTextResultOutput](#AiRecognitionTaskOcrFullTextResultOutput) | Выходная информация задачи полного распознавания текста. Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |

## AiRecognitionTaskOcrFullTextResultInput

Входные данные для полного распознавания текста.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона полного распознавания текста. |

## AiRecognitionTaskOcrFullTextResultOutput

Выходные данные полного распознавания текста.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| SegmentSet | Array of [AiRecognitionTaskOcrFullTextSegmentItem](#AiRecognitionTaskOcrFullTextSegmentItem) | Набор результатов полного распознавания текста. |

## AiRecognitionTaskOcrFullTextSegmentItem

Сегмент полного распознавания текста.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| StartTimeOffset | Float | Временное смещение начала сегмента распознавания в секундах. |
| EndTimeOffset | Float | Временное смещение конца сегмента распознавания в секундах. |
| TextSet | Array of [AiRecognitionTaskOcrFullTextSegmentTextItem](#AiRecognitionTaskOcrFullTextSegmentTextItem) | Набор результатов сегмента распознавания. |

## AiRecognitionTaskOcrFullTextSegmentTextItem

Сегмент полного распознавания текста.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Confidence | Float | Уверенность сегмента распознавания. Диапазон значений: 0–100. |
| AreaCoordSet | Array of Integer | Координаты зоны результата распознавания. Массив содержит четыре элемента: [x1,y1,x2,y2], т. е. горизонтальные и вертикальные координаты верхнего левого и нижнего правого углов. |
| Text | String | Распознанный текст. |

## AiRecognitionTaskOcrWordsResult

Результат распознавания ключевых слов текста.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: PROCESSING, SUCCESS, FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи; любое другое значение указывает на сбой. Подробнее см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1041/40249). |
| ErrCode | Integer | Код ошибки. 0 указывает на успешное выполнение задачи; в противном случае произошел сбой. Этот параметр больше не рекомендуется. Рекомендуется использовать новый параметр кода ошибки ErrCodeExt. |
| Message | String | Сообщение об ошибке. |
| Input | [AiRecognitionTaskOcrWordsResultInput](#AiRecognitionTaskOcrWordsResultInput) | Входная информация задачи распознавания ключевых слов текста. |
| Output | [AiRecognitionTaskOcrWordsResultOutput](#AiRecognitionTaskOcrWordsResultOutput) | Выходная информация задачи распознавания ключевых слов текста. Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |

## AiRecognitionTaskOcrWordsResultInput

Входные данные для распознавания ключевых слов текста.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона распознавания ключевых слов текста. |

## AiRecognitionTaskOcrWordsResultItem

Результат распознавания ключевых слов текста.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Word | String | Ключевое слово текста. |
| SegmentSet | Array of [AiRecognitionTaskOcrWordsSegmentItem](#AiRecognitionTaskOcrWordsSegmentItem) | Список сегментов, содержащих ключевое слово текста. |

## AiRecognitionTaskOcrWordsResultOutput

Выходные данные распознавания ключевых слов текста.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| ResultSet | Array of [AiRecognitionTaskOcrWordsResultItem](#AiRecognitionTaskOcrWordsResultItem) | Набор результатов распознавания ключевых слов текста. |

## AiRecognitionTaskOcrWordsSegmentItem

Сегмент распознавания текста.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| StartTimeOffset | Float | Временное смещение начала сегмента распознавания в секундах. |
| EndTimeOffset | Float | Временное смещение конца сегмента распознавания в секундах. |
| Confidence | Float | Уверенность сегмента распознавания. Диапазон значений: 0–100. |
| AreaCoordSet | Array of Integer | Координаты зоны результата распознавания. Массив содержит четыре элемента: [x1,y1,x2,y2], т. е. горизонтальные и вертикальные координаты верхнего левого и нижнего правого углов. |

## AiRecognitionTaskTransTextResult

Результат перевода.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: PROCESSING, SUCCESS, FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи; любое другое значение указывает на сбой. Подробнее см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1041/40249). |
| ErrCode | Integer | Код ошибки. `0` указывает на успешное выполнение задачи; другие значения указывают на сбой. Этот параметр не рекомендуется. Используйте вместо этого `ErrCodeExt`. |
| Message | String | Сообщение об ошибке. |
| Input | [AiRecognitionTaskTransTextResultInput](#AiRecognitionTaskTransTextResultInput) | Входные данные задачи перевода. |
| Output | [AiRecognitionTaskTransTextResultOutput](#AiRecognitionTaskTransTextResultOutput) | Выходные данные задачи перевода. Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| Progress | Integer | Прогресс выполнения задачи. Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |

## AiRecognitionTaskTransTextResultInput

Входные данные для перевода.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона перевода. |

## AiRecognitionTaskTransTextResultOutput

Результат перевода.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| SegmentSet | Array of [AiRecognitionTaskTransTextSegmentItem](#AiRecognitionTaskTransTextSegmentItem) | Переведенные сегменты. |
| SubtitlePath | String | URL субтитров. |

## AiRecognitionTaskTransTextSegmentItem

Переведенные сегменты.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Confidence | Float | Оценка уверенности для сегмента. Диапазон значений: 0–100. |
| StartTimeOffset | Float | Временное смещение начала сегмента в секундах. |
| EndTimeOffset | Float | Временное смещение конца сегмента в секундах. |
| Text | String | Транскрипция текста. |
| Trans | String | Перевод. |
| Wordlist | Array of [WordResult](#WordResult) | Информация о временных метках слов. |

## AiReviewPoliticalAsrTaskInput

Входные параметры для обнаружения политически чувствительной информации на основе ASR.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона. |

## AiReviewPoliticalAsrTaskOutput

Информация о чувствительном контенте, обнаруженном на основе ASR.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Confidence | Float | Оценка уверенности обнаружения политически чувствительной информации на основе ASR. Диапазон значений: 0–100. |
| Suggestion | String | Рекомендация по обработке политически чувствительной информации, обнаруженной на основе ASR. Допустимые значения: passreviewblock |
| SegmentSet | Array of [MediaContentReviewAsrTextSegmentItem](#MediaContentReviewAsrTextSegmentItem) | Видеосегменты, содержащие политически чувствительную информацию, обнаруженную на основе ASR. |

## AiReviewPoliticalOcrTaskInput

Входные параметры для обнаружения политически чувствительной информации на основе OCR.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона. |

## AiReviewPoliticalOcrTaskOutput

Информация о чувствительном контенте, обнаруженном на основе OCR.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Confidence | Float | Оценка уверенности обнаружения политически чувствительной информации на основе OCR. Диапазон значений: 0–100. |
| Suggestion | String | Рекомендация по обработке политически чувствительной информации, обнаруженной на основе OCR. Допустимые значения: passreviewblock |
| SegmentSet | Array of [MediaContentReviewOcrTextSegmentItem](#MediaContentReviewOcrTextSegmentItem) | Видеосегменты, содержащие политически чувствительную информацию, обнаруженную на основе OCR. |

## AiReviewPoliticalTaskInput

Входные параметры для обнаружения политически чувствительной информации.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона. |

## AiReviewPoliticalTaskOutput

Обнаруженная чувствительная информация.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Confidence | Float | Оценка уверенности обнаружения чувствительной информации. Диапазон значений: 0–100. |
| Suggestion | String | Рекомендация по обработке обнаруженной чувствительной информации. Допустимые значения: passreviewblock |
| Label | String | Метки для обнаруженного чувствительного контента. Связь между значениями этого параметра и значениями параметра `LabelSet` в [PoliticalImgReviewTemplateInfo](https://intl.cloud.tencent.com/document/api/862/37615?from_cn_redirect=1#AiReviewPoliticalTaskOutput) выглядит следующим образом: violation_photo: violation_photo (запрещенные значки) Другие значения (politician/entertainment/sport/entrepreneur/scholar/celebrity/military): politician |
| SegmentSet | Array of [MediaContentReviewPoliticalSegmentItem](#MediaContentReviewPoliticalSegmentItem) | Видеосегменты, содержащие чувствительную информацию. |

## AiReviewPornAsrTaskInput

Тип входного параметра задачи обнаружения порнографической информации в тексте на основе ASR во время проверки контента

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона обнаружения порнографической информации. |

## AiReviewPornAsrTaskOutput

Порнографическая информация в тексте, обнаруженная на основе ASR

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Confidence | Float | Оценка порнографической информации в тексте, обнаруженной на основе ASR, от 0 до 100. |
| Suggestion | String | Рекомендация для порнографической информации в тексте, обнаруженной на основе ASR. Допустимые значения: pass.review.block. |
| SegmentSet | Array of [MediaContentReviewAsrTextSegmentItem](#MediaContentReviewAsrTextSegmentItem) | Список видеосегментов, содержащих порнографическую информацию в тексте, обнаруженную на основе ASR. |

## AiReviewPornOcrTaskInput

Тип входного параметра задачи обнаружения порнографической информации в тексте на основе OCR во время проверки контента

Используется действиями: DescribeTaskDetail, ParseNotification

## AiReviewTaskPornResult

Тип результата задачи обнаружения порнографического контента при проверке содержимого

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: PROCESSING, SUCCESS, FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи; любое другое значение указывает на ошибку. Подробнее см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1041/40249). |
| ErrCode | Integer | Код ошибки. 0 указывает на успешное выполнение задачи; иное значение указывает на ошибку. Данный параметр больше не рекомендуется. Используйте новый параметр кода ошибки ErrCodeExt. |
| Message | String | Сообщение об ошибке. Примечание: это поле может возвращать null, что указывает на то, что допустимые значения не могут быть получены. |
| Input | [AiReviewPornTaskInput](#AiReviewPornTaskInput) | Входные данные для задачи обнаружения порнографического контента при проверке содержимого. |
| Output | [AiReviewPornTaskOutput](#AiReviewPornTaskOutput) | Выходные данные задачи обнаружения порнографического контента при проверке содержимого. Примечание: это поле может возвращать null, что указывает на то, что допустимые значения не могут быть получены. |

## AiReviewTaskProhibitedAsrResult

Тип результата задачи обнаружения запрещённой информации в речи на основе ASR при проверке содержимого

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: PROCESSING, SUCCESS, FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи; любое другое значение указывает на ошибку. Подробнее см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1041/40249). |
| ErrCode | Integer | Код ошибки. 0: успех; другие значения: ошибка. 40000: неверный входной параметр. Проверьте его;60000: неверный исходный файл (например, повреждённые данные видео). Проверьте, является ли исходный файл нормальным;70000: внутренняя ошибка сервиса. Попробуйте ещё раз. |
| Message | String | Сообщение об ошибке. |
| Input | [AiReviewProhibitedAsrTaskInput](#AiReviewProhibitedAsrTaskInput) | Входные данные для задачи обнаружения запрещённой информации в речи на основе ASR при проверке содержимого |
| Output | [AiReviewProhibitedAsrTaskOutput](#AiReviewProhibitedAsrTaskOutput) | Выходные данные задачи обнаружения запрещённой информации в речи на основе ASR при проверке содержимого |

## AiReviewTaskProhibitedOcrResult

Тип результата задачи обнаружения запрещённой информации в тексте на основе OCR при проверке содержимого

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: PROCESSING, SUCCESS, FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи; любое другое значение указывает на ошибку. Подробнее см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1041/40249). |
| ErrCode | Integer | Код ошибки. 0: успех; другие значения: ошибка. 40000: неверный входной параметр. Проверьте его;60000: неверный исходный файл (например, повреждённые данные видео). Проверьте, является ли исходный файл нормальным;70000: внутренняя ошибка сервиса. Попробуйте ещё раз. |
| Message | String | Сообщение об ошибке. |
| Input | [AiReviewProhibitedOcrTaskInput](#AiReviewProhibitedOcrTaskInput) | Входные данные для задачи обнаружения запрещённой информации в тексте на основе OCR при проверке содержимого |
| Output | [AiReviewProhibitedOcrTaskOutput](#AiReviewProhibitedOcrTaskOutput) | Выходные данные задачи обнаружения запрещённой информации в тексте на основе OCR при проверке содержимого |

## AiReviewTaskTerrorismOcrResult

Результат обнаружения террористического контента на основе OCR.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: PROCESSING, SUCCESS, FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи; любое другое значение указывает на ошибку. Подробнее см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1041/40249). |
| ErrCode | Integer | Код ошибки. 0: успех; другие значения: ошибка. 40000: неверный входной параметр. Проверьте его;60000: неверный исходный файл (например, повреждённые данные видео). Проверьте, является ли исходный файл нормальным;70000: внутренняя ошибка сервиса. Попробуйте ещё раз. |
| Message | String | Сообщение об ошибке. |
| Input | [AiReviewTerrorismOcrTaskInput](#AiReviewTerrorismOcrTaskInput) | Входной параметр для обнаружения террористического контента на основе OCR. |
| Output | [AiReviewTerrorismOcrTaskOutput](#AiReviewTerrorismOcrTaskOutput) | Выходные данные обнаружения террористического контента на основе OCR. Примечание: это поле может возвращать `null`, что указывает на то, что допустимые значения не могут быть получены. |

## AiReviewTaskTerrorismResult

Результат обнаружения конфиденциальной информации.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: PROCESSING, SUCCESS, FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи; любое другое значение указывает на ошибку. Подробнее см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1041/40249). |
| ErrCode | Integer | Код ошибки. 0 указывает на успешное выполнение задачи; иное значение указывает на ошибку. Данный параметр больше не рекомендуется. Используйте новый параметр кода ошибки ErrCodeExt. |
| Message | String | Сообщение об ошибке. |
| Input | [AiReviewTerrorismTaskInput](#AiReviewTerrorismTaskInput) | Входной параметр для обнаружения конфиденциальной информации. |
| Output | [AiReviewTerrorismTaskOutput](#AiReviewTerrorismTaskOutput) | Выходные данные обнаружения конфиденциальной информации. Примечание: это поле может возвращать `null`, что указывает на то, что допустимые значения не могут быть получены. |

## AiReviewTerrorismOcrTaskInput

Входной параметр для обнаружения конфиденциальной информации на основе OCR.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона. |

## AiReviewTerrorismOcrTaskOutput

Информация о конфиденциальном контенте, обнаруженном на основе OCR.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Confidence | Float | Оценка уверенности для обнаружения конфиденциальной информации на основе OCR. Диапазон значений: 1-100. |
| Suggestion | String | Рекомендация по обработке конфиденциальной информации, обнаруженной на основе OCR. Допустимые значения: passreviewblock |
| SegmentSet | Array of [MediaContentReviewOcrTextSegmentItem](#MediaContentReviewOcrTextSegmentItem) | Сегменты видео, содержащие конфиденциальную информацию, обнаруженную на основе OCR. |

## AiReviewTerrorismTaskInput

Входной параметр для обнаружения конфиденциальной информации.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона. |

## AiReviewTerrorismTaskOutput

Информация о конфиденциальном контенте, обнаруженном.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Confidence | Float | Оценка уверенности для обнаружения конфиденциальной информации. Диапазон значений: 0-100. |
| Suggestion | String | Рекомендация по обработке обнаруженной конфиденциальной информации. Допустимые значения: passreviewblock |
| Label | String | Метки обнаруженного конфиденциального контента. Допустимые значения: gunscrowdpolicebloodybanners (чувствительные флаги)militantexplosionterroristsscenario (чувствительные сцены) |
| SegmentSet | Array of [MediaContentReviewSegmentItem](#MediaContentReviewSegmentItem) | Сегменты видео, содержащие конфиденциальную информацию. |

## AiSampleFaceInfo

Управление образцами на основе ИИ - информация о лице.

Используется действиями: CreatePersonSample, DescribePersonSamples, ModifyPersonSample.

| Имя | Тип | Описание |
| --- | --- | --- |
| FaceId | String | ID изображения лица. |
| Url | String | Адрес изображения лица. |

## AiSampleFaceOperation

Управление образцами на основе ИИ - операция с данными лица.

Используется действиями: ModifyPersonSample.

| Имя | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| Type | String | Да | Тип операции. Допустимые значения: add, delete, reset. Операция `reset` очистит существующие данные лица персоны и добавит `FaceContents` как указанные данные лица. |
| FaceIds | Array of String | Нет | Набор ID лиц. Это поле требуется, когда `Type` имеет значение `delete`. |
| FaceContents | Array of String | Нет | Набор строк, полученных с помощью [Base64-кодирования](https://tools.ietf.org/html/rfc4648) изображения лица. Это поле требуется, когда `Type` имеет значение `add` или `reset`;Предел длины массива: 5 изображений. Примечание: изображение должно быть достаточно чётким полнолицевым фото персоны размером не менее 200 * 200 пк. |

## AiSampleFailFaceInfo

Управление образцами на основе ИИ - информация о лице, обработка которого не удалась.

Используется действиями: CreatePersonSample, ModifyPersonSample.

| Имя | Тип | Описание |
| --- | --- | --- |
| Index | Integer | Соответствует индексу неправильного изображения во входном параметре `FaceContents`, начиная с 0. |
| ErrCode | Integer | Код ошибки. Допустимые значения: 0: успешно;Другие значения: ошибка. |
| Message | String | Описание ошибки. |

## AiSamplePerson

Управление образцами на основе ИИ - информация о персоне.

Используется действиями: CreatePersonSample, DescribePersonSamples, ModifyPersonSample.

| Имя | Тип | Описание |
| --- | --- | --- |
| PersonId | String | ID персоны. |
| Name | String | Имя персоны. |
| Description | String | Описание персоны. |
| FaceInfoSet | Array of [AiSampleFaceInfo](#AiSampleFaceInfo) | Информация о лице. |
| TagSet | Array of String | Тег персоны. |
| UsageSet | Array of String | Вариант использования. |
| CreateTime | String | Время создания в [формате ISO даты](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |
| UpdateTime | String | Время последнего изменения в [формате ISO даты](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |

## AiSampleTagOperation

Управление образцами на основе ИИ - операция с тегом.

Используется действиями: ModifyPersonSample, ModifyWordSample.

| Имя | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| Type | String | Да | Тип операции. Допустимые значения: add, delete, reset. |
| Tags | Array of String | Да | Тег. Предел длины: 128 символов. |

## AiSampleWord

Управление образцами на основе ИИ - информация вывода ключевого слова.

Используется действиями: DescribeWordSamples.

| Имя | Тип | Описание |
| --- | --- | --- |
| Keyword | String | Ключевое слово. |
| TagSet | Array of String | Тег ключевого слова. |
| UsageSet | Array of String | Вариант использования ключевого слова. |
| CreateTime | String | Время создания в [формате ISO даты](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |
| UpdateTime | String | Время последнего изменения в [формате ISO даты](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |

## AiSampleWordInfo

Управление образцами на основе ИИ - информация ввода ключевого слова.

Используется действиями: CreateWordSamples.

| Имя | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| Keyword | String | Да | Ключевое слово. Предел длины: 20 символов. |
| Tags | Array of String | Нет | Тег ключевого слова Предел длины массива: 20 тегов;Предел длины тега: 128 символов. |

## AigcImageExtraParam

Расширенные параметры для создания изображения AIGC.

Используется действиями: CreateAigcImageTask.

| Имя | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| AspectRatio | String | Нет | Соотношение сторон сгенерированного видео.Поддерживаемые соотношения сторон для разных моделей:1. GEM: 1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9 и 21:9.Примечание: для получения дополнительной информации о соотношениях сторон конкретных моделей см. веб-сайт модели. |
| Resolution | String | Нет | Разрешение выходного изображения.Модели, поддерживающие этот параметр:Допустимые значения: 720P, 1080P, 2K и 4K. |

## AigcImageInfo

Информация об изображении для создания AIGC.

Используется действиями: CreateAigcImageTask.

| Имя | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| ImageUrl | String | Нет | URL изображения для создания видео. URL должен быть доступен из общедоступной сети и должен быть доступен для краулеров. |
| ReferenceType | String | Нет | Тип ссылки. Примечание:1. Когда модель использует многоссылочное создание изображения Vidu q2, это также можно использовать для указания ID субъекта.2. Если используется модель GV, это служит методом ссылки. Допустимые значения: asset и style. |

## AigcStoreCosParam

Информация, необходимая для загрузки результатов файлов AIGC в COS. Необходимо создать и авторизовать роль LVB_QCSRole.

Используется действиями: CreateAigcImageTask, CreateAigcVideoTask.

| Имя | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| CosBucketName | String | Нет | Имя бакета COS для сохранения. Это значение требуется, если нужно сохранить результаты в COS. Пример значения: bucket. |
| CosBucketRegion | String | Нет | Регион бакета COS для сохранения. Это требуется, если нужно загрузить результаты в COS. Пример значения: ap-guangzhou. |
| CosBucketPath | String | Нет | Путь бакета COS для сохранения.Опционально.Пример значения: my_file. |

## AigcVideoExtraParam

Расширенные параметры для создания видео AIGC.

Используется действиями: CreateAigcVideoTask.

| Имя | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| Resolution | String | Нет | Разрешение сгенерированного видео, которое связано с выбранной моделью и заданной длительностью видео.Поддерживаемые опции разрешения для разных моделей:1. Kling: 720P (по умолчанию) и 1080P.2. Hailuo: 768P (по умолчанию) и 1080P.3. Vidu: 720P (по умолчанию) и 1080P.4. GV: 720P (по умолчанию) и 1080P.5. OS: 720P. Для изображений поддерживаются только 1280x720 и 720x1280. Разрешение не может быть указано.Примечание: в дополнение к разрешению, поддерживаемому моделью, также доступны разрешения 2K и 4K. |
| AspectRatio | String | Нет | Соотношение сторон сгенерированного видео.Поддержка этого параметра различными моделями:1. Kling поддерживает этот параметр только для текста в видео, с соотношением сторон 16:9 (по умолчанию), 9:16 и 1:1.2. Hailuo не поддерживает этот параметр.3. Vidu поддерживает [16:9, 9:16, 4:3, 3:4, 1:1] для текста в видео и только для видео с использованием эталонного изображения. Только q2 поддерживает 4:3 и 3:4.4. GV поддерживает 16:9 (по умолчанию) и 9:16.5. OS поддерживает этот параметр только для текста в видео, с соотношением сторон 16:9 (по умолчанию) и 9:16.Примечание: для получения дополнительной информации о поддерживаемых соотношениях сторон конкретных моделей см. веб-сайт модели. |
| LogoAdd | Integer | Нет | Указывает, нужно ли добавлять логотип водяного знака.1. Hailuo поддерживает этот параметр.2. Kling поддерживает этот параметр. 3. Vidu поддерживает этот параметр. |
| EnableAudio | Boolean | Нет | Указывает, нужно ли создавать аудио для видео. Допустимые значения: true или false.Модели, поддерживающие этот параметр:1. GV. Значение по умолчанию: true.2. OS. Значение по умолчанию: true. |
| OffPeak | Boolean | Нет | Указывает, нужно ли использовать режим планирования в непиковые часы. Только Vidu поддерживает этот параметр.Задачи, отправленные в режиме непиковых часов, будут обработаны в течение 48 часов. Незавершённые задачи будут отменены. |

## AigcVideoReferenceImageInfo

Информация об эталонном изображении для создания видео AIGC.

Используется действиями: CreateAigcVideoTask.

| Имя | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| ImageUrl | String | Нет | URL изображения для создания видео. URL должен быть доступен из общедоступной сети и должен быть доступен для краулеров. |
| ReferenceType | String | Нет | Тип ссылки. Примечание:1. Если используется модель GV, это служит методом ссылки. Допустимые значения: asset и style. |

## AigcVideoReferenceVideoInfo

Используется действиями: CreateAigcVideoTask.

| Имя | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| VideoUrl | String | Нет |  |
| ReferType | String | Нет |  |
| KeepOriginalSound | String | Нет |  |

## AnimatedGraphicTaskInput

Тип задачи создания анимированного изображения.

Используется действиями: CreateSchedule, CreateWorkflow, DescribeTaskDetail, ModifySchedule, ParseNotification, ProcessMedia, ResetWorkflow.

| Имя | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| Definition | Integer | Да | ID шаблона создания анимированного изображения. |
| StartTimeOffset | Float | Да | Время начала анимированного изображения в видео в секундах. |
| EndTimeOffset | Float | Да | Время завершения анимированного изображения в видео в секундах. |
| OutputStorage | [TaskOutputStorage](#TaskOutputStorage) | Нет | Целевой бакет для созданного файла анимированного изображения. Если этот параметр оставлен пустым, будет унаследовано значение `OutputStorage` родительской папки. Примечание: это поле может возвращать null, что указывает на то, что допустимые значения не могут быть получены. |
| OutputObjectPath | String | Нет | Выходной путь файла после создания анимированного изображения, который может быть относительным или абсолютным путём. Если нужно определить выходной путь, путь должен заканчиваться на `.{format}`. Для имён переменных см. [Переменная имени файла](https://intl.cloud.tencent.com/document/product/862/37039?from_cn_redirect=1). Пример относительного пути: Filename_{Variable name}.{format}.Filename.{format}. Пример абсолютного пути: /Custom path/Filename_{Variable name}.{format}. Если оставлено пустым, по умолчанию используется относительный путь: `{inputName}_animatedGraphic_{definition}.{format}`. |

## AnimatedGraphicsTemplate

Детали шаблона создания анимированного изображения.

Используется действиями: DescribeAnimatedGraphicsTemplates.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Уникальный ID шаблона создания анимированного изображения. |
| Type | String | Тип шаблона. Допустимые значения: Preset: встроенный шаблон;Custom: пользовательский шаблон. |
| Name | String | Имя шаблона создания анимированного изображения. |
| Comment | String | Описание шаблона создания анимированного изображения. |
| Width | Integer | Максимальное значение ширины (или длинной стороны) анимированного изображения в пк. Диапазон значений: 0 и [128, 4,096]. Если оба `Width` и `Height` равны 0, разрешение будет таким же, как у исходного видео;Если `Width` равен 0, но `Height` не равен 0, `Width` будет масштабироваться пропорционально;Если `Width` не равен 0, но `Height` равен 0, `Height` будет масштабироваться пропорционально;Если оба `Width` и `Height` не равны 0, будет использовано пользовательское разрешение. Значение по умолчанию: 0. |
| Height | Integer | Максимальное значение высоты (или короткой стороны) анимированного изображения в пк. Диапазон значений: 0 и [128, 4,096]. Если оба `Width` и `Height` равны 0, разрешение будет таким же, как у исходного видео;Если `Width` равен 0, но `Height` не равен 0, `Width` будет масштабироваться пропорционально;Если `Width` не равен 0, но `Height` равен 0, `Height` будет масштабироваться пропорционально;Если оба `Width` и `Height` не равны 0, будет использовано пользовательское разрешение. Значение по умолчанию: 0. |
| ResolutionAdaptive | String | Адаптивность разрешения. Допустимые значения: open: включено. В этом случае `Width` обозначает длинную сторону видео, а `Height` — короткую;close: отключено. В этом случае `Width` обозначает ширину видео, а `Height` — высоту. Значение по умолчанию: open. |
| Format | String | Формат анимированного изображения. |
| Fps | Integer | Частота кадров. |
| Quality | Float | Качество изображения. |
| CreateTime | String | Время создания шаблона в [формате ISO даты](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |
| UpdateTime | String | Время последнего изменения шаблона в [формате ISO даты](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |

## ArtifactRepairConfig

Кон

## AudioTemplateInfoForUpdate

Параметр конфигурации аудиопотока

Используется действиями: CreateWorkflow, ModifyTranscodeTemplate, ProcessMedia, ResetWorkflow.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Codec | String | Нет | Формат кодирования аудиопотока. Если транскодирование аудио не требуется, значение: copy. Если внешний параметр Container — mp3, значение: mp3. Если внешний параметр Container — ogg или flac, значение: flac. Если внешний параметр Container — m4a, допустимые значения: aac;ac3. Если внешний параметр Container — mp4 или flv, допустимые значения: aac: более подходит для mp4;mp3: более подходит для flv;mp2. Если внешний параметр Container — hls, допустимые значения: aac;mp3. Примечание: это поле может возвращать null, что указывает на невозможность получения допустимых значений. |
| Bitrate | Integer | Нет | Битрейт аудиопотока в кбит/с. Диапазон значений: 0 и [26, 256]. Если значение равно 0, битрейт аудиопотока будет совпадать с битрейтом исходного аудио. |
| SampleRate | Integer | Нет | Частота дискретизации аудиопотока. Разные стандарты кодирования поддерживают разные варианты частоты дискретизации. Значение 0 указывает на использование значения частоты дискретизации исходного аудио. Подробнее см. [Поддерживаемый диапазон частоты дискретизации аудио](https://www.tencentcloud.comom/document/product/862/77166?from_cn_redirect=1#f3b039f1-d817-4a96-b4e4-90132d31cd53). Единица: Гц. Примечание: убедитесь, что частота дискретизации исходного аудиопотока находится в списке указанных выше вариантов. В противном случае транскодирование может не пройти успешно. Примечание: это поле может возвращать null, что указывает на невозможность получения допустимых значений. |
| AudioChannel | Integer | Нет | Режим канала аудио. Допустимые значения: 1: моноканальный режим. 2: двухканальный режим. 6: объемный звук 5.1. Если формат контейнера — аудио (flac, ogg, mp3 и m4a), канал аудио нельзя установить на объемный звук 5.1. Примечание: это поле может возвращать null, что указывает на невозможность получения допустимых значений. |
| StreamSelects | Array of Integer | Нет | Дорожки аудио для сохранения. По умолчанию сохраняются все дорожки аудио. |

## AudioTrackChannelInfo

Информация аудиодорожки.

Используется действиями: CreateTranscodeTemplate.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| ChannelsRemix | Integer | Нет | Включить ли функцию микширования нескольких аудиодорожек. Допустимые значения: 0: отключить функцию микширования нескольких аудиодорожек. 1: включить функцию микширования нескольких аудиодорожек. Значение по умолчанию: 0. Примечание: это поле может возвращать null, что указывает на невозможность получения допустимого значения. |
| SelectType | String | Нет | Установить тип селектора для входной аудиодорожки. Допустимые значения: track: указывает на использование идентификатора аудиодорожки для идентификации используемой дорожки. track_channel: указывает на использование как идентификатора аудиодорожки, так и идентификатора звукового канала для идентификации используемых дорожки и канала. Значение по умолчанию: track. Если исходная аудиодорожка имеет несколько звуковых каналов, используйте track_channel. Примечание: это поле может возвращать null, что указывает на невозможность получения допустимого значения. |
| InputTrackInfo | Array of [TrackInfo](#TrackInfo) | Нет | Информация аудиодорожки. Примечание: это поле может возвращать null, что указывает на невозможность получения допустимого значения. |

## AwsS3FileUploadTrigger

Триггер загрузки файла AWS S3.

Используется действиями: CreateSchedule, CreateWorkflow, ModifySchedule, ResetWorkflow.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| S3Bucket | String | Да | Корзина AWS S3, привязанная к схеме. |
| S3Region | String | Да | Регион корзины AWS S3. |
| Dir | String | Нет | Привязанная директория корзины. Это должен быть абсолютный путь, начинающийся и заканчивающийся на `/`, например `/movie/201907/`. Если вы не указали это, будет привязана корневая директория. |
| Formats | Array of String | Нет | Форматы файлов, которые будут запускать схему, например ["mp4", "flv", "mov"]. Если вы не указали это, загрузка файлов любого формата будет запускать схему. |
| S3SecretId | String | Нет | Идентификатор ключа корзины AWS S3. Примечание: это поле может возвращать null, что указывает на невозможность получения допустимых значений. |
| S3SecretKey | String | Нет | Ключ корзины AWS S3. Примечание: это поле может возвращать null, что указывает на невозможность получения допустимых значений. |
| AwsSQS | [AwsSQS](#AwsSQS) | Нет | Очередь SQS корзины AWS S3. Примечание: очередь должна находиться в том же регионе, что и корзина. Примечание: это поле может возвращать null, что указывает на невозможность получения допустимых значений. |

## AwsSQS

Информация об очереди AWS SQS.

Используется действиями: BatchProcessMedia, CreateSchedule, CreateWorkflow, DescribeBatchTaskDetail, DescribeTaskDetail, EditMedia, ExtractBlindWatermark, ModifySchedule, ProcessMedia, ResetWorkflow.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| SQSRegion | String | Да | Регион очереди SQS. Примечание: это поле может возвращать null, что указывает на невозможность получения допустимых значений. |
| SQSQueueName | String | Да | Имя очереди SQS. Примечание: это поле может возвращать null, что указывает на невозможность получения допустимых значений. |
| S3SecretId | String | Нет | Идентификатор ключа, необходимый для чтения из/записи в очередь SQS. Примечание: это поле может возвращать null, что указывает на невозможность получения допустимых значений. |
| S3SecretKey | String | Нет | Ключ, необходимый для чтения из/записи в очередь SQS. Примечание: это поле может возвращать null, что указывает на невозможность получения допустимых значений. |

## BatchSmartSubtitlesResult

Результат задачи интеллектуальных субтитров.

Используется действиями: DescribeBatchTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Input | [SmartSubtitleTaskResultInput](#SmartSubtitleTaskResultInput) | Входная информация для задач интеллектуальных субтитров. Примечание: это поле может возвращать null, что указывает на невозможность получения допустимого значения. |
| Outputs | Array of [SmartSubtitleTaskBatchOutput](#SmartSubtitleTaskBatchOutput) | Выходная информация для задач интеллектуальных субтитров. Примечание: это поле может возвращать null, что указывает на невозможность получения допустимого значения. |

## BatchSubTaskResult

Результаты подзадач для пакетной задачи.

Используется действиями: DescribeBatchTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| InputInfos | Array of [MediaInputInfo](#MediaInputInfo) | Входная информация для пакетной задачи. Примечание: это поле может возвращать null, что указывает на невозможность получения допустимого значения. |
| Metadatas | Array of [MediaMetaData](#MediaMetaData) | Метаданные исходного видео. Примечание: это поле может возвращать null, что указывает на невозможность получения допустимого значения. |
| SmartSubtitlesTaskResult | [BatchSmartSubtitlesResult](#BatchSmartSubtitlesResult) | Результат выполнения задачи интеллектуальных субтитров. Примечание: это поле может возвращать null, что указывает на невозможность получения допустимого значения. |

## BlindWatermarkInput

Параметр цифрового водяного знака в задаче MPS.

Используется действиями: CreateWorkflow, ProcessMedia, ResetWorkflow.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Definition | Integer | Да | Идентификатор шаблона цифрового водяного знака. |

## BlindWatermarkTemplate

Детали шаблона цифрового водяного знака.

Используется действиями: DescribeBlindWatermarkTemplates.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Уникальный идентификатор шаблона цифрового водяного знака. |
| Type | String | Тип цифрового водяного знака. Допустимые значения: blind-basic: базовый водяной знак авторских прав; blind-nagra: водяной знак судебно-медицинской экспертизы NAGRA. |
| Name | String | Имя шаблона цифрового водяного знака. |
| TextContent | String | Текстовое содержание шаблона цифрового водяного знака. Длина не может превышать 64 символа. |
| Comment | String | Описание информации о шаблоне цифрового водяного знака. |
| CreateTime | String | Время создания шаблона цифрового водяного знака в [формате даты и времени ISO](https://www.tencentcloud.comom/document/product/862/37710?from_cn_redirect=1#52). |
| UpdateTime | String | Время последнего изменения шаблона цифрового водяного знака в [формате даты и времени ISO](https://www.tencentcloud.comom/document/product/862/37710?from_cn_redirect=1#52). |
| Strength | String | Прочность цифрового водяного знака. default: по умолчанию, баланс между качеством видео HD и устойчивостью. stronger: четкое качество изображения, сильная устойчивость. strongest: нормальное качество видео, максимальная устойчивость. |

## ClassificationConfigureInfo

Управляющий параметр задачи интеллектуальной категоризации

Используется действиями: CreateAIAnalysisTemplate, DescribeAIAnalysisTemplates.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Switch | String | Да | Переключатель задачи интеллектуальной категоризации. Допустимые значения: ON: включить задачу интеллектуальной категоризации;OFF: отключить задачу интеллектуальной категоризации. |

## ClassificationConfigureInfoForUpdate

Управляющий параметр задачи интеллектуальной категоризации

Используется действиями: ModifyAIAnalysisTemplate.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Switch | String | Нет | Переключатель задачи интеллектуальной категоризации. Допустимые значения: ON: включить задачу интеллектуальной категоризации;OFF: отключить задачу интеллектуальной категоризации. |

## ColorEnhanceConfig

Конфигурация улучшения цвета.

Используется действиями: CreateProcessImageTemplate, CreateTranscodeTemplate, ModifyProcessImageTemplate, ModifyTranscodeTemplate, ProcessImage.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Switch | String | Нет | Включить ли функцию. Допустимые значения: ON, OFF. Значение по умолчанию: ON. |
| Type | String | Нет | Интенсивность. Допустимые значения: weak, normal, strong. Значение по умолчанию: weak. Примечание: это поле может возвращать null, что указывает на невозможность получения допустимых значений. |

## ComposeAudioItem

Информация аудиоэлемента задачи видеоредактирования/композитинга.

Используется действиями: EditMedia.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| SourceMedia | [ComposeSourceMedia](#ComposeSourceMedia) | Да | Информация о материале элемента. |
| TrackTime | [ComposeTrackTime](#ComposeTrackTime) | Нет | Время элемента на шкале времени. Если это не указано, элемент будет следовать за предыдущим элементом. |
| AudioOperations | Array of [ComposeAudioOperation](#ComposeAudioOperation) | Нет | Выполняемые операции, такие как отключение звука. |

## ComposeAudioOperation

Аудиооперации задачи видеоредактирования/композитинга.

Используется действиями: EditMedia.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Type | String | Да | Тип операции. Допустимые значения: `Volume`: регулировка громкости. |
| Volume | Float | Нет | Уровень громкости. Этот параметр действителен, если `Type` — `Volume`. Диапазон значений: 0–5. Если значение параметра равно `0`, видео будет отключено. Если значение параметра меньше 1, громкость будет снижена. Если значение параметра равно `1`, исходная громкость будет сохранена. Если значение параметра больше 1, громкость будет увеличена. |

## ComposeAudioStream

Информация аудиопотока задачи видеоредактирования/композитинга.

Используется действиями: EditMedia.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Codec | String | Нет | Кодек аудиопотока. Допустимые значения: `AAC`: AAC (по умолчанию), используется для контейнера MP4. `MP3`: кодек MP3, используется для контейнера MP3. |
| SampleRate | Integer | Нет | Частота дискретизации (Гц) аудиопотока. 16000 (по умолчанию), 32000, 44100, 48000. |
| AudioChannel | Integer | Нет | Количество звуковых каналов. Допустимые значения: `1`: моно. `2`: стерео (по умолчанию). |
| Bitrate | Integer | Нет | Эталонный битрейт в кбит/с. Диапазон значений: 26–10000. Если установлено, кодировщик попытается кодировать с этим битрейтом. Если не установлено, сервис автоматически выберет подходящий битрейт на основе параметров аудио. |

## ComposeCanvas

Информация холста задачи видеоредактирования/композитинга.

Используется действиями: EditMedia.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Color | String | Нет | Значение RGB цвета фона. Формат: #RRGGBB, например `#F0F0F0`. Значение по умолчанию: `#000000` (черный). |
| Width | Integer | Нет | Ширина холста (пиксели), которая является шириной выходного видео. Диапазон значений: 0–3840. Значение по умолчанию — `0`, что означает, что ширина холста совпадает с шириной первого видео. |
| Height | Integer | Нет | Высота холста (пиксели), которая является высотой выходного видео. Диапазон значений: 0–3840. Значение по умолчанию — `0`, что означает, что высота холста совпадает с высотой первого видео. |

## ComposeEmptyItem

Информация элемента-заполнителя задачи видеоредактирования/композитинга.

Используется действиями: EditMedia.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Duration | String | Да | Длительность элемента. Значение этого параметра заканчивается на `s`, что означает секунды. Например, `3.5s` указывает 3,5 секунды. |

## ComposeImageItem

Информация элемента изображения задачи видеоредактирования/композитинга.

Используется действиями: EditMedia.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| SourceMedia | [ComposeSourceMedia](#ComposeSourceMedia) | Да | Информация о материале элемента. |
| TrackTime | [ComposeTrackTime](#ComposeTrackTime) | Нет | Время элемента на шкале времени. Если это не указано, элемент будет следовать за предыдущим элементом. |
| XPos | String | Нет | Горизонтальное расстояние от центра элемента до начала координат холста. Поддерживаются два формата: если значение заканчивается на %, оно указывает расстояние как процент от ширины холста. Например, `10%` означает, что расстояние составляет 10% от ширины холста. Если значение заканчивается на px, оно указывает расстояние в пикселях. Например, `100px` означает, что расстояние составляет 100 пикселей. Значение по умолчанию: `50%`. |
| YPos | String | Нет | Вертикальное расстояние от центра элемента до начала координат холста. Поддерживаются два формата: если значение заканчивается на %, оно указывает расстояние как процент от высоты холста. Например, `10%` означает, что расстояние составляет 10% от высоты холста. Если значение заканчивается на px, оно указывает расстояние в пикселях. Например, `100px` означает, что расстояние составляет 100 пикселей. Значение по умолчанию: `50%`. |
| Width | String | Нет | Ширина видеосегмента. Поддерживаются два формата: если значение заканчивается на %, оно указывает ширину как процент от ширины холста. Например, `10%` означает, что ширина видео составляет 10% от ширины холста. Если значение заканчивается на px, оно указывает ширину в пикселях. Например, `100px` означает, что ширина видео составляет 100 пикселей. Если один или оба параметра пусты или установлены в `0`: если оба `Width` и `Height` пусты, исходные ширина и высота элемента будут сохранены. Если `Width` пуст, а `Height` — нет, ширина будет автоматически масштабироваться. Если `Width` не пуст, а `Height` — пуст, высота будет автоматически масштабироваться. |
| Height | String | Нет | Высота элемента. Поддерживаются два формата: если значение заканчивается на %, оно указывает высоту как процент от высоты холста. Например, `10%` означает, что высота составляет 10% от высоты холста. Если значение заканчивается на px, оно указывает высоту в пикселях. Например, `100px` означает, что высота составляет 100 пикселей. Если один или оба параметра пусты или установлены в `0`: если оба `Width` и `Height` пусты, исходные ширина и высота видео будут сохранены. Если `Width` пуст, а `Height` — нет, ширина будет автоматически масштабироваться. Если `Width` не пуст, а `Height` — пуст, высота будет автоматически масштабироваться. |
| ImageOperations | Array of [ComposeImageOperation](#ComposeImageOperation) | Нет | Операции с изображением, такие как вращение изображения. |

## ComposeImageOperation

Операции с изображением задачи видеоредактирования/композитинга.

Используется действиями: EditMedia.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Type | String | Да | Тип. Допустимые значения: `Rotate`: вращение изображения. `Flip`: отражение изображения. |
| RotateAngle | Float | Нет | Действительно, если `Type` — `Rotate`. Угол поворота вокруг центра изображения. Диапазон значений: 0–360. |
| FlipType | String | Нет | Действительно, если `Type` — `Flip`. Способ отражения изображения. Допустимые значения: `Horizental`: отразить горизонтально. `Vertical`: отразить вертикально. |

## ComposeMediaConfig

Информация задачи видеоредактирования/композитинга.

На рисунке ниже показаны связи между дорожками, элементами и шкалой времени.

![image](https://ie-mps-1258344699.cos.ap-nanjing.tencentcos.cn/common/cloud/EditMedia-Compose-Track-Item-en.png)

Используется действиями: EditMedia.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| TargetInfo | [ComposeTargetInfo](#ComposeTargetInfo) | Нет | Информация о выходном видео. |
| Canvas | [ComposeCanvas](#ComposeCanvas) | Нет | Информация холста выходного видео. |
| Styles | Array of [ComposeStyles](#ComposeStyles) | Нет | Глобальные стили. Этот параметр используется вместе с `Tracks` для указания стилей, таких как стиль субтитров. |
| Tracks | Array of [ComposeMediaTrack](#ComposeMediaTrack) | Нет | Информация медиадорожек (состоящих из видео, аудио, изображения и текстовых элементов), используемых для композитинга видео. О дорожках и шкале времени: шкала времени дорожки совпадает со шкалой времени выходного видео. Элементы различных дорожек накладываются в одной и той же точке на шкале времени. Видео, изображение и текстовые элементы накладываются в соответствии с номером их дорожки, первая дорожка находится сверху. Аудиоэлементы смешиваются. Примечание: различные элементы одной дорожки не могут быть наложены (за исключением субтитров). |

## ComposeMediaItem

Информация элемента задачи видеоредактирования/композитинга.

Используется действиями: EditMedia.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Type | String | Да | Тип элемента. Допустимые значения: `Video` `Audio` `Image` `Transition` `Subtitle` `Empty` |
| Video | [ComposeVideoItem](#ComposeVideoItem) | Нет | Информация видеоэлемента, действительна, если `Type` — `Video`. |
| Audio | [ComposeAudioItem](#ComposeAudioItem) | Нет | Информация аудиоэлемента, действительна, если `Type` — `Audio`. |
| Image | [ComposeImageItem](#ComposeImageItem) | Нет | Информация элемента изображения, действительна, если `Type` — `Image`. |
| Transition | [ComposeTransitionItem](#ComposeTransitionItem) | Нет | Информация элемента переходов, действительна, если `Type` — `Transition`. |
| Subtitle | [ComposeSubtitleItem](#ComposeSubtitleItem) | Нет | Информация элемента субтитров, действительна, если `Type` — `Subtitle`. |
| Empty | [ComposeEmptyItem](#ComposeEmptyItem) | Нет | Информация элемента-заполнителя, действительна, если `Type` — `Empty`. Элемент-заполнитель используется как заполнитель на шкале времени. |

## ComposeMediaTrack

Информация дорожки задачи видеоредактирования/композитинга.

Используется действиями: EditMedia.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Type | String | Да | Тип дорожки. Допустимые значения: Video: видеодорожка. Может состоять из следующих элементов: видеоэлементов, элементов изображения, элементов переходов, элементов-заполнителей. Audio: аудиодорожка. Может состоять из следующих элементов: аудиоэлементов, элементов переходов, элементов-заполнителей. Title: текстовая дорожка. Может состоять из следующих элементов: элементов субтитров. |
| Items | Array of [ComposeMediaItem](#ComposeMediaItem) | Да | Элементы дорожки. |

## ComposeSourceMedia

Материальный источник задачи видеоредактирования/композитинга.

Используется действиями: EditMedia.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| FileId | String | Да | Идентификатор материала, который можно найти в `FileInfos`. |
| StartTime | String | Нет | Время начала материала. Поддерживаются два следующих формата. Если значение этого параметра заканчивается на `s`, оно указывает время в секундах. Например, `3.5s` указывает время, когда прошло 3,5 секунды материала. Если значение этого параметра заканчивается на `%`, оно указывает время как процент от длительности материала. Например, `10%` указывает время, когда прошло 10% от длительности материала. Значение по умолчанию: `0s`. |
| EndTime | String | Нет | Время окончания материала. Этот параметр и `StartTime` определяют, какой временной сегмент материала будет использован. Поддерживаются два следующих формата: если значение этого параметра заканчивается на `s`, оно указывает время в секундах. Например, `3.5s` указывает время, когда прошло 3,5 секунды материала. Если значение этого параметра заканчивается на `%`, оно указывает время как процент от длительности материала. Например, `10%` указывает время, когда прошло 10% от длительности материала. Если установлена длительность дорожки, значение по умолчанию — `StartTime` плюс длительность дорожки. Если нет, значение по умолчанию — `StartTime` плюс 1 секунда. Примечание: `EndTime` должно быть как минимум на 0,02 секунды позже `StartTime`. |

## ComposeStyles

Информация

## ComposeVideoStream

Информация о видеопотоке задачи редактирования/compositing видео.

Используется действиями: EditMedia.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Codec | String | No | Кодек. Допустимые значения: `H.264` (по умолчанию) |
| Fps | Integer | No | Частота кадров видео (Гц). Диапазон значений: 0–60. Значение по умолчанию — `0`, что означает, что частота кадров будет такой же, как частота первого видео. |
| Bitrate | Integer | No | Эталонный битрейт в кбит/с. Диапазон значений: 50-35000. Если установлено, кодер попытается кодировать с этим битрейтом. Если не установлено, сервис автоматически выберет подходящий битрейт на основе сложности изображения. |

## ContainerDiagnoseResultItem

Результат диагностики формата контейнера.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| Category | String | Категория диагностированного исключения. Допустимые значения: DecodeParamException: исключение параметра декодирования. TimeStampException: исключение временной метки. FrameException: исключение частоты кадров. StreamStatusException: исключение статуса потока. StreamInfo: исключение информации потока. StreamAbnormalCharacteristics: исключение характеристик потока. DecodeException: исключение декодирования. HLSRequirements: исключение формата HLS. Примечание: это поле может возвращать null, что указывает на то, что допустимые значения не могут быть получены. |
| Type | String | Диагностированный конкретный тип исключения. Допустимые значения: VideoResolutionChanged: изменение разрешения видео. AudioSampleRateChanged: изменение частоты дискретизации аудио. AudioChannelsChanged: изменение количества каналов аудио. ParameterSetsChanged: изменение информации набора параметров потока. DarOrSarInvalid: исключение соотношения сторон видео. TimestampFallback: откат временной метки DTS. DtsJitter: слишком высокий дрожание DTS. PtsJitter: слишком высокий дрожание PTS. AACDurationDeviation: неправильный интервал временной метки кадра AAC. AudioDroppingFrames: отсечение кадров аудио. VideoDroppingFrames: отсечение кадров видео. AVTimestampInterleave: неправильное чередование аудио-видео. PtsLessThanDts: PTS меньше DTS для потоков мультимедиа. ReceiveFpsJitter: значительное дрожание в частоте кадров приема сети. ReceiveFpsTooSmall: слишком низкая частота кадров видео приема сети. FpsJitter: значительное дрожание в частоте кадров потока, рассчитанной через PTS. StreamOpenFailed: сбой открытия потока. StreamEnd: конец потока. StreamParseFailed: сбой разбора потока. VideoFirstFrameNotIdr: первый кадр не является IDR кадром. StreamNALUError: ошибка кода начала NALU. TsStreamNoAud: отсутствует NALU AUD в потоке H26x MPEG-TS. AudioStreamLack: отсутствует поток аудио. VideoStreamLack: отсутствует поток видео. LackAudioRecover: восстановление отсутствующего потока аудио. LackVideoRecover: восстановление отсутствующего потока видео. VideoBitrateOutofRange: битрейт видеопотока (кбит/с) выходит за пределы диапазона. AudioBitrateOutofRange: битрейт аудиопотока (кбит/с) выходит за пределы диапазона. VideoDecodeFailed: ошибка декодирования видео. AudioDecodeFailed: ошибка декодирования аудио. AudioOutOfPhase: противофаза в двухканальном аудио. VideoDuplicatedFrame: дублирующиеся кадры в видеопотоках. AudioDuplicatedFrame: дублирующиеся кадры в аудиопотоках. VideoRotation: поворот видео. TsMultiPrograms: несколько программ в потоках MPEG2-TS. Mp4InvalidCodecFourcc: кодек FourCC в MP4 не соответствует требованиям Apple HLS. HLSBadM3u8Format: неправильный формат файла M3U8. HLSInvalidMasterM3u8: неправильный основной файл M3U8. HLSInvalidMediaM3u8: неправильный медиа файл M3U8. HLSMasterM3u8Recommended: отсутствуют параметры, рекомендуемые стандартом, в основном M3U8. HLSMediaM3u8Recommended: отсутствуют параметры, рекомендуемые стандартом, в медиа M3U8. HLSMediaM3u8DiscontinuityExist: EXT-X-DISCONTINUITY в медиа M3U8. HLSMediaSegmentsStreamNumChange: изменилось количество потоков в сегментах. HLSMediaSegmentsPTSJitterDeviation: скачки PTS между сегментами без EXT-X-DISCONTINUITY. HLSMediaSegmentsDTSJitterDeviation: скачки DTS между сегментами без EXT-X-DISCONTINUITY. TimecodeTrackExist: дорожка TMCD в MP4. Примечание: это поле может возвращать null, что указывает на то, что допустимые значения не могут быть получены. |
| SeverityLevel | String | Диагностированный уровень исключения. Допустимые значения: Fatal: влияет на последующее воспроизведение и разбор. Error: может повлиять на воспроизведение. Warning: потенциальный риск, который может не обязательно повлиять на воспроизведение. Notice: важная информация о потоке. Info: общая информация о потоке. Примечание: это поле может возвращать null, что указывает на то, что допустимые значения не могут быть получены. |
| DateTimeSet | Array of String | Временная метка предупреждения в формате 2022-12-25T13:14:16Z. Примечание: это поле может возвращать null, что указывает на то, что допустимые значения не могут быть получены. |
| TimestampSet | Array of Float | Временная метка. Примечание: это поле может возвращать null, что указывает на то, что допустимые значения не могут быть получены. |

## ContentReviewTemplateItem

Подробные сведения о шаблоне проверки содержимого

Используется действиями: DescribeContentReviewTemplates.

| Name | Type | Description |
| --- | --- | --- |
| Definition | Integer | Уникальный ID шаблона проверки содержимого. |
| Name | String | Имя шаблона проверки содержимого. Ограничение длины: 64 символа. |
| Comment | String | Описание шаблона проверки содержимого. Ограничение длины: 256 символов. |
| PornConfigure | [PornConfigureInfo](#PornConfigureInfo) | Параметр управления обнаружением содержимого для взрослых. Примечание: это поле может возвращать null, что указывает на то, что допустимые значения не могут быть получены. |
| TerrorismConfigure | [TerrorismConfigureInfo](#TerrorismConfigureInfo) | Параметры для обнаружения конфиденциальной информации. Примечание: это поле может возвращать `null`, что указывает на то, что допустимые значения не могут быть получены. |
| PoliticalConfigure | [PoliticalConfigureInfo](#PoliticalConfigureInfo) | Параметры для обнаружения конфиденциальной информации. Примечание: это поле может возвращать `null`, что указывает на то, что допустимые значения не могут быть получены. |
| ProhibitedConfigure | [ProhibitedConfigureInfo](#ProhibitedConfigureInfo) | Параметр управления обнаружением запрещенной информации. Запрещенная информация включает: оскорбления, наркотики. Примечание: это поле может возвращать null, что указывает на то, что допустимые значения не могут быть получены. |
| UserDefineConfigure | [UserDefineConfigureInfo](#UserDefineConfigureInfo) | Параметр управления проверкой пользовательского содержимого. Примечание: это поле может возвращать null, что указывает на то, что допустимые значения не могут быть получены. |
| CreateTime | String | Время создания шаблона в [формате даты ISO](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |
| UpdateTime | String | Время последнего изменения шаблона в [формате даты ISO](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |
| Type | String | Тип шаблона. Допустимые значения: * Preset * Custom Примечание: это поле может возвращать `null`, что указывает на то, что допустимые значения не могут быть получены. |

## CosFileUploadTrigger

Правило ввода, связанное с COS.

Используется действиями: CreateSchedule, CreateWorkflow, ModifySchedule, ResetWorkflow.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Bucket | String | Yes | Имя бакета COS, связанного с рабочим процессом, например `TopRankVideo-125xxx88`. |
| Region | String | Yes | Регион бакета COS, связанного с рабочим процессом, например `ap-chongiqng`. |
| Dir | String | No | Входной путь каталога, связанный с рабочим процессом, например `/movie/201907/`. Если этот параметр оставить пустым, будет использован корневой каталог `/`. |
| Formats | Array of String | No | Все поддерживаемые форматы: - Расширение видеофайла. Поддерживаются следующие 15 вариантов: `.mp4`, `.avi`, `.mov`, `.wmv`, `.flv`, `.mkv`, `.mpg`, `.mpeg`, `.rm`, `.rmvb`, `.asf`, `.3gp`, `.webm`, `.ts` и `.m4v`. - Расширение аудиофайла. Поддерживаются следующие 7 вариантов: `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`, `.m4a` и `.amr`. - Расширение файла субтитров. Поддерживаются следующие 2 варианта: `.vtt` и `.srt`. - `*`: поддерживается любой формат файла. - Не указано или введен пустой список: система поддерживает следующие предустановленные форматы файлов: видео (`.mp4`, `.ts`, `.flv`, `.wmv`, `.asf`, `.rm`, `.rmvb`, `.mpg`, `.mpeg`, `.3gp`, `.mov`, `.webm`, `.mkv`, `.avi` и `.m4v`); аудио (`.mp3`, `.m4a`, `.flac`, `.ogg`, `.wav`, `.amr` и `.aac`); субтитры (`.vtt` и `.srt`). **Примечание**: 1. Если список входных форматов включает `*`, это означает, что поддерживается любой формат файла. 2. Расширения файлов можно указывать с `.` или без него, например `.mp4` или `mp4`, оба варианта поддерживаются. 3. Пользовательские расширения файлов должны состоять из цифр, букв и символов, иметь длину от 1 до 64 символов. |

## CosInputInfo

Информация об объекте COS для обработки.

Используется действиями: BatchProcessMedia, DescribeMediaMetaData, ExtractBlindWatermark, ProcessImage, ProcessMedia.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Bucket | String | Yes | Бакет COS объекта для обработки, например `TopRankVideo-125xxx88`. |
| Region | String | Yes | Регион бакета COS, например `ap-chongqing`. |
| Object | String | Yes | Путь объекта для обработки, например `/movie/201907/WildAnimal.mov`. |

## CosOutputStorage

Информация об объекте COS вывода после обработки мультимедиа.

Используется действиями: BatchProcessMedia, CreateSchedule, CreateWorkflow, EditMedia, ModifySchedule, ProcessImage, ProcessLiveStream, ProcessMedia, ResetWorkflow.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Bucket | String | No | Бакет, в который сохраняется выходной файл обработки мультимедиа, например `TopRankVideo-125xxx88`. Если этот параметр оставить пустым, будет унаследовано значение верхнего уровня. |
| Region | String | No | Регион выходного бакета, например `ap-chongqing`. Если этот параметр оставить пустым, будет унаследовано значение верхнего уровня. |

## CoverConfigureInfo

Параметр управления задачей интеллектуального создания обложки

Используется действиями: CreateAIAnalysisTemplate, DescribeAIAnalysisTemplates.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Switch | String | Yes | Переключатель задачи интеллектуального создания обложки. Допустимые значения: ON: включить задачу интеллектуального создания обложки; OFF: отключить задачу интеллектуального создания обложки. |

## CoverConfigureInfoForUpdate

Параметр управления задачей интеллектуального создания обложки

Используется действиями: ModifyAIAnalysisTemplate.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Switch | String | No | Переключатель задачи интеллектуального создания обложки. Допустимые значения: ON: включить задачу интеллектуального создания обложки; OFF: отключить задачу интеллектуального создания обложки. |

## DiagnoseResult

Используется действиями: ParseLiveStreamProcessNotification.

| Name | Type | Description |
| --- | --- | --- |
| Category | String | Категория диагностированного исключения. Допустимые значения: DecodeParamException: исключение параметра декодирования. TimeStampException: исключение временной метки. FrameException: исключение частоты кадров. StreamStatusException: исключение статуса потока. StreamInfo: исключение информации потока. StreamAbnormalCharacteristics: исключение характеристик потока. DecodeException: исключение декодирования. HLSRequirements: исключение формата HLS. Примечание: это поле может возвращать null, что указывает на то, что допустимые значения не могут быть получены. |
| Type | String | Диагностированный конкретный тип исключения. Допустимые значения: VideoResolutionChanged: изменение разрешения видео. AudioSampleRateChanged: изменение частоты дискретизации аудио. AudioChannelsChanged: изменение количества каналов аудио. ParameterSetsChanged: изменение информации набора параметров потока. DarOrSarInvalid: исключение соотношения сторон видео. TimestampFallback: откат временной метки DTS. DtsJitter: слишком высокий дрожание DTS. PtsJitter: слишком высокий дрожание PTS. AACDurationDeviation: неправильный интервал временной метки кадра AAC. AudioDroppingFrames: отсечение кадров аудио. VideoDroppingFrames: отсечение кадров видео. AVTimestampInterleave: неправильное чередование аудио-видео. PtsLessThanDts: PTS меньше DTS для потоков мультимедиа. ReceiveFpsJitter: значительное дрожание в частоте кадров приема сети. ReceiveFpsTooSmall: слишком низкая частота кадров видео приема сети. FpsJitter: значительное дрожание в частоте кадров потока, рассчитанной через PTS. StreamOpenFailed: сбой открытия потока. StreamEnd: конец потока. StreamParseFailed: сбой разбора потока. VideoFirstFrameNotIdr: первый кадр не является IDR кадром. StreamNALUError: ошибка кода начала NALU. TsStreamNoAud: отсутствует NALU AUD в потоке H26x MPEG-TS. AudioStreamLack: отсутствует поток аудио. VideoStreamLack: отсутствует поток видео. LackAudioRecover: восстановление отсутствующего потока аудио. LackVideoRecover: восстановление отсутствующего потока видео. VideoBitrateOutofRange: битрейт видеопотока (кбит/с) выходит за пределы диапазона. AudioBitrateOutofRange: битрейт аудиопотока (кбит/с) выходит за пределы диапазона. VideoDecodeFailed: ошибка декодирования видео. AudioDecodeFailed: ошибка декодирования аудио. AudioOutOfPhase: противофаза в двухканальном аудио. VideoDuplicatedFrame: дублирующиеся кадры в видеопотоках. AudioDuplicatedFrame: дублирующиеся кадры в аудиопотоках. VideoRotation: поворот видео. TsMultiPrograms: несколько программ в потоках MPEG2-TS. Mp4InvalidCodecFourcc: кодек FourCC в MP4 не соответствует требованиям Apple HLS. HLSBadM3u8Format: неправильный формат файла M3U8. HLSInvalidMasterM3u8: неправильный основной файл M3U8. HLSInvalidMediaM3u8: неправильный медиа файл M3U8. HLSMasterM3u8Recommended: отсутствуют параметры, рекомендуемые стандартом, в основном M3U8. HLSMediaM3u8Recommended: отсутствуют параметры, рекомендуемые стандартом, в медиа M3U8. HLSMediaM3u8DiscontinuityExist: EXT-X-DISCONTINUITY в медиа M3U8. HLSMediaSegmentsStreamNumChange: изменилось количество потоков в сегментах. HLSMediaSegmentsPTSJitterDeviation: скачки PTS между сегментами без EXT-X-DISCONTINUITY. HLSMediaSegmentsDTSJitterDeviation: скачки DTS между сегментами без EXT-X-DISCONTINUITY. TimecodeTrackExist: дорожка TMCD в MP4. Примечание: это поле может возвращать null, что указывает на то, что допустимые значения не могут быть получены. |
| Timestamp | Float |  |
| Description | String |  |
| DateTime | String |  |
| SeverityLevel | String | Диагностированный уровень исключения. Допустимые значения: Fatal: влияет на последующее воспроизведение и разбор. Error: может повлиять на воспроизведение. Warning: потенциальный риск, который может не обязательно повлиять на воспроизведение. Notice: важная информация о потоке. Info: общая информация о потоке. Примечание: это поле может возвращать null, что указывает на то, что допустимые значения не могут быть получены. |

## DiffusionEnhanceConfig

Улучшение на основе LLM.

Используется действиями: CreateTranscodeTemplate, ModifyTranscodeTemplate.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Switch | String | No | Переключатель конфигурации возможностей. Допустимые значения: ON: включено. OFF: отключено. Значение по умолчанию: OFF. |
| Type | String | No | Тип прочности. Допустимые значения: weak normal strong Значение по умолчанию: normal. Примечание: это поле может возвращать null, что указывает на то, что допустимые значения не могут быть получены. |

## DrmInfo

Подробные сведения о DRM-шифровании.

Используется действиями: CreateWorkflow, ProcessMedia, ResetWorkflow.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Type | String | Yes | Тип шифрования. - simpleaes Может использоваться только для HLS. поддерживаемые форматы: ts и mp4. Может использоваться только в режиме нарезки. не может использоваться в режиме singlefile. - fairplay: Может использоваться только для HLS. формат сегментов может быть только mp4. Поддерживает режим нарезки или режим singlefile. - widevine: Может использоваться для HLS и DASH. формат нарезки может быть только mp4. Выходной HLS: можно использовать режим нарезки или singlefile. Выходной DASH: может использоваться только режим singlefile. - playready: Может использоваться для HLS и DASH. формат нарезки может быть только mp4. Выходной HLS: можно использовать режим нарезки или singlefile. Выходной DASH: может использоваться только режим singlefile. - widevine+fairplay, playready+fairplay, widevine+playready+fairplay: Может использоваться только для HLS. допустимые значения: mp4. Поддерживает режим нарезки или режим singlefile. - widevine+playready: Применимо к HLS и MPEG-DASH. формат может быть только mp4. Формат HLS может использовать режим нарезки или режим singlefile. Указано, что только режим singlefile может использоваться для MPEG-DASH. |
| SimpleAesDrm | [SimpleAesDrm](#SimpleAesDrm) | No | Подробные сведения о шифровании AES-128. Примечание: это поле может возвращать null, что указывает на то, что допустимые значения не могут быть получены. |
| SpekeDrm | [SpekeDrm](#SpekeDrm) | No | Информация о шифровании FairPlay, WideVine и PlayReady. |

## EditMediaFileInfo

Информация о редактировании файла VOD видео

Используется действиями: DescribeTaskDetail, EditMedia, ParseNotification.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| InputInfo | [MediaInputInfo](#MediaInputInfo) | Yes | Информация о входном видео. |
| StartTimeOffset | Float | No | Начальное смещение (в секундах) для обрезки видео. Этот параметр действителен для задач обрезки видео. |
| EndTimeOffset | Float | No | Конечное смещение (в секундах) для обрезки видео. Этот параметр действителен для задач обрезки видео. |
| Id | String | No | ID материала, связанного с элементом. Этот параметр требуется для задач видеокомпозирования. Примечание: ID может содержать до 32 символов, букв, цифр и специальных символов -_. Примечание: это поле может возвращать null, что указывает на то, что допустимые значения не могут быть получены. |

## EditMediaOutputConfig

Конфигурация выходных файлов видеоредактирования

Используется действиями: EditMedia.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Container | String | No | Контейнер. Допустимые значения: `mp4` (по умолчанию), `hls`, `mov`, `flv`, `avi`. Примечание: это поле может возвращать null, что указывает на то, что допустимые значения не могут быть получены. |
| Type | String | No | Режим редактирования. Необязательные значения: normal (по умолчанию): точное редактирование. fast: быстрое редактирование, с более высокой скоростью обработки, но с некоторым снижением точности. Примечание: fast поддерживает только отдельные файлы, выходной формат транскодирования по умолчанию для normal — h264. Примечание: это поле может возвращать null, что указывает на то, что допустимое значение не может быть получено. |

## EditMediaTask

Информация о задаче редактирования видео

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| TaskId | String | ID задачи. |
| Status | String | Статус задачи. Допустимые значения: PROCESSING: обработка; FINISH: завершено. |
| ErrCode | Integer | Код ошибки. 0: успех; другие значения: ошибка. |
| Message | String | Сообщение об ошибке. |
| Input | [EditMediaTaskInput](#EditMediaTaskInput) | Входные данные задачи редактирования видео. |
| Output | [EditMediaTaskOutput](#EditMediaTaskOutput) | Выходные данные задачи редактирования видео. |

## EditMediaTaskInput

Входные данные задачи редактирования видео.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| FileInfoSet | Array of [EditMediaFileInfo](#EditMediaFileInfo) | Информация о входном видеофайле. |

## EditMediaTaskOutput

Выходные данные задачи редактирования видео

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| OutputStorage | [TaskOutputStorage](#TaskOutputStorage) | Целевое хранилище отредактированного файла. |
| Path | String | Путь отредактированного видеофайла. |

## EnhanceConfig

Конфигурация улучшения аудио/видео.

Используется действиями: CreateTranscodeTemplate, CreateWorkflow, DescribeTranscodeTemplates, ModifyTranscodeTemplate, ProcessMedia, ResetWorkflow.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| VideoEnhance | [VideoEnhanceConfig](#VideoEnhanceConfig) | No | Конфигурация улучшения видео. Примечание: это поле может возвращать null, что указывает на то, что допустимые значения не могут быть получены. |
| AudioEnhance | [AudioEnhanceConfig](#AudioEnhanceConfig) | No | Конфигурация улучшения аудио. Примечание: это поле может возвращать null, что указывает на то, что допустимые значения не могут быть получены. |

## EraseArea

Интеллектуальное стирание. конфигурация координат удаляемой области.
Область определяется координатами верхнего левого угла и нижнего правого угла.
Начало координат находится в верхнем левом углу кадра, и точки координат можно указать, используя значения в пикселях или процентах.
**Для автоматической удаляемой области:**
Когда единица составляет %, диапазон координат составляет [0,1].
Когда единица — px, диапазон значения X — [0, ширина видеоизображения]. Диапазон значения Y — [0, высота видеоизображения].
**Для удаления указанной области:**
Укажите диапазон координат [0,1) при использовании единицы %.
Когда единица: px, диапазон значения X [0, ширина видеоизображения], диапазон значения Y [0, высота видеоизображения].

Используется действиями: CreateSmartEraseTemplate, CreateSmartSubtitleTemplate, ModifySmartEraseTemplate, ModifySmartSubtitleTemplate, ProcessMedia.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| LeftTopX | Float | Yes | Координата оси X верхнего левого угла. |
| LeftTopY | Float | Yes | Координата оси Y верхнего левого угла. |

## HdrConfig

Конфигурация HDR.

Используется действиями: CreateTranscodeTemplate, ModifyTranscodeTemplate.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Switch | String | No | Включена ли функция. Допустимые значения: ONOFF Значение по умолчанию: ON. |
| Type | String | No | Тип. Допустимые значения: HDR10HLG Значение по умолчанию: HDR10. Примечание: Метод кодирования видео должен быть h264 или h265. Примечание: Глубина бита видео составляет 10. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимые значения. |

## HeadTailParameter

Параметры открывающих и закрывающих титров

Используется действиями: CreateWorkflow, ProcessMedia, ResetWorkflow.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| HeadSet | Array of [MediaInputInfo](#MediaInputInfo) | No | Открывающие сегменты. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимые значения. |
| TailSet | Array of [MediaInputInfo](#MediaInputInfo) | No | Закрывающие сегменты. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимые значения. |

## HighlightSegmentItem

Информация о сегменте с выделением.

Используется действиями: ParseLiveStreamProcessNotification.

| Name | Type | Description |
| --- | --- | --- |
| Confidence | Float | Оценка уверенности. |
| StartTimeOffset | Float | Смещение времени начала сегмента. |
| EndTimeOffset | Float | Смещение времени окончания сегмента. |
| SegmentTags | Array of String | Тег сегмента. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимые значения. |
| BeginTime | String | Время начала сегмента прямой трансляции в формате даты и времени ISO. |
| EndTime | String | Время окончания сегмента прямой трансляции в формате даты и времени ISO. |
| Title | String | Название выделения. |
| Summary | String | Обзор выделения. |

## ImageAreaBoxInfo

Информация о выбранной прямоугольной области в изображении.

Используется действиями: CreateProcessImageTemplate, ModifyProcessImageTemplate, ProcessImage.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Type | String | No | Тип выбранной прямоугольной области в изображении. Допустимые значения: logo: значок.Text: текст. Значение по умолчанию: logo. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимое значение. |
| AreaCoordSet | Array of Integer | No | Координаты (на уровне пикселей) выбранной прямоугольной области в изображении в формате [x1, y1, x2, y2]. Указывает координаты верхнего левого угла и нижнего правого угла. Примечание: Максимальное значение этого поля составляет 4096. Например, [101, 85, 111, 95]. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимые значения. |
| BoundingBox | Array of Float | No | Координаты выбранной прямоугольной области в изображении в формате [x1, y1, x2, y2]. Указывает координаты верхнего левого угла и нижнего правого угла. Это поле вступает в силу, если AreaCoordSet не указан. Когда указывается пиксель, максимальное значение этого поля составляет 4096. - [0.1, 0.1, 0.3, 0.3]: указывает отношение (значения меньше 1). - [50, 50, 350, 280]: указывает пиксель (значения больше или равны 1). Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимые значения. |
| BoundingBoxUnitType | Integer | No | Единица измерения поля BoundingBox. Если для значения установлено 0, единица выбирается автоматически в соответствии с правилом поля. Если установлено 1, единица измерения — отношение. Если установлено 2, единица измерения — пиксель. |

## ImageDenoiseConfig

Конфигурация очистки изображения от шума.

Используется действиями: CreateProcessImageTemplate, ModifyProcessImageTemplate, ProcessImage.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Switch | String | No | Статус включения конфигурации функции. Допустимые значения: ON: включено.OFF: отключено. Значение по умолчанию: ON. |
| Type | String | No | Тип с допустимыми значениями: weakstrong Значение по умолчанию: weak. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимое значение. |

## ImageEncodeConfig

Параметры формата кодирования изображения

Используется действиями: CreateProcessImageTemplate, ModifyProcessImageTemplate, ProcessImage.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Format | String | No | Формат изображения. Допустимые значения: JPEG, PNG, BMP и WebP. Если не указано, используется исходный формат изображения. Анимации не поддерживаются. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимое значение. |
| Quality | Integer | No | Относительное качество изображения. Допустимый диапазон: 1–100. Значение зависит от качества исходного изображения, по умолчанию используется качество исходного изображения. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимое значение. |

## ImageEnhanceConfig

Параметры расширения изображения

Используется действиями: CreateProcessImageTemplate, ModifyProcessImageTemplate, ProcessImage.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| SuperResolution | [SuperResolutionConfig](#SuperResolutionConfig) | No | Конфигурация повышения разрешения. |
| AdvancedSuperResolutionConfig | [AdvancedSuperResolutionConfig](#AdvancedSuperResolutionConfig) | No | Конфигурация продвинутого повышения разрешения. |
| Denoise | [ImageDenoiseConfig](#ImageDenoiseConfig) | No | Конфигурация очистки от шума. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимое значение. |
| ImageQualityEnhance | [ImageQualityEnhanceConfig](#ImageQualityEnhanceConfig) | No | Конфигурация комплексного расширения. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимое значение. |
| ColorEnhance | [ColorEnhanceConfig](#ColorEnhanceConfig) | No | Конфигурация улучшения цвета. |
| SharpEnhance | [SharpEnhanceConfig](#SharpEnhanceConfig) | No | Конфигурация улучшения деталей. |
| FaceEnhance | [FaceEnhanceConfig](#FaceEnhanceConfig) | No | Конфигурация расширения лица. |
| LowLightEnhance | [LowLightEnhanceConfig](#LowLightEnhanceConfig) | No | Конфигурация улучшения при низком освещении. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимое значение. |

## ImageEraseConfig

Параметр стирания изображения.

Используется действиями: CreateProcessImageTemplate, ModifyProcessImageTemplate, ProcessImage.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| ImageEraseLogo | [ImageEraseLogoConfig](#ImageEraseLogoConfig) | No | Конфигурация стирания значка. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимое значение. |

## ImageEraseLogoConfig

Конфигурация стирания значка.

Используется действиями: CreateProcessImageTemplate, ModifyProcessImageTemplate, ProcessImage.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Switch | String | No | Статус включения конфигурации функции. Допустимые значения: ON: включеноOFF: отключено Значение по умолчанию: ON. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимое значение. |
| ImageAreaBoxes | Array of [ImageAreaBoxInfo](#ImageAreaBoxInfo) | No | Несколько прямоугольных областей, которые необходимо стереть, максимум 16 областей. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимое значение.  Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимые значения. |

## ImageProcessTaskOutput

Информация о результате обработки изображения.

Используется действиями: DescribeImageTaskDetail.

| Name | Type | Description |
| --- | --- | --- |
| Path | String | Путь к выходному файлу. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимое значение. |
| OutputStorage | [TaskOutputStorage](#TaskOutputStorage) | Место хранения выходного файла. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимое значение. |
| Content | String | Результат обработки задачи преобразования изображения в текст. |

## ImageProcessTaskResult

Тип результата задачи обработки изображения.

Используется действиями: DescribeImageTaskDetail.

| Name | Type | Description |
| --- | --- | --- |
| Status | String | Статус задачи, включая PROCESSING, SUCCESS и FAIL. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимое значение. |
| ErrMsg | String | Код ошибки. Пустая строка указывает на то, что задача выполнена успешно, остальные значения указывают на то, что задача не выполнена. Допустимые значения см. в списке [кодов ошибок MPS](https://www.tencentcloud.comom/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81). |
| Message | String | Сообщение об ошибке. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимое значение. |
| Output | [ImageProcessTaskOutput](#ImageProcessTaskOutput) | Выход задачи транскодирования. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимое значение. |
| Progress | Integer | Прогресс транскодирования в диапазоне значений [0–100]. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимое значение. |

## ImageQualityEnhanceConfig

Конфигурация комплексного расширения.

Используется действиями: CreateProcessImageTemplate, CreateTranscodeTemplate, ModifyProcessImageTemplate, ModifyTranscodeTemplate, ProcessImage.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Switch | String | No | Включена ли функция. Допустимые значения: ONOFF Значение по умолчанию: ON. |
| Type | String | No | Интенсивность. Допустимые значения: weaknormalstrong Значение по умолчанию: weak. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимые значения. |

## ImageSpriteTaskInput

Тип входного параметра задачи создания спрайт-листа изображений

Используется действиями: CreateSchedule, CreateWorkflow, DescribeTaskDetail, ModifySchedule, ParseNotification, ProcessMedia, ResetWorkflow.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Definition | Integer | Yes | ID шаблона для создания спрайт-листа изображений. |
| OutputStorage | [TaskOutputStorage](#TaskOutputStorage) | No | Целевой контейнер для созданного спрайт-листа. Если этот параметр оставлен пустым, будет унаследовано значение `OutputStorage` верхней папки. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимые значения. |
| OutputObjectPath | String | No | Выходной путь файла снимка спрайт-листа, который может быть относительным или абсолютным путем. Если необходимо определить выходной путь, путь должен заканчиваться на `.{format}`. Для имен переменных см. [Переменная имени файла](https://intl.cloud.tencent.com/document/product/862/37039?from_cn_redirect=1).Пример относительного пути: Filename_{Variable name}.{format}.Filename.{format}. Пример абсолютного пути: /Custom path/Filename_{Variable name}.{format}. Если оставлено пустым, по умолчанию используется относительный путь: `{inputName}_imageSprite_{definition}_{number}.{format}`. |
| WebVttObjectName | String | No | Выходной путь файла WebVTT после создания спрайт-листа изображений, который может быть только относительным путем. Если этот параметр оставлен пустым, будет использован следующий относительный путь по умолчанию: `{inputName}_imageSprite_{definition}.{format}`. |
| ObjectNumberFormat | [NumberFormat](#NumberFormat) | No | Правило переменной `{number}` в выходном пути спрайт-листа изображений. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимые значения. |

## ImageSpriteTemplate

Детали шаблона для создания спрайт-листа изображений

Используется действиями: DescribeImageSpriteTemplates.

| Name | Type | Description |
| --- | --- | --- |
| Definition | Integer | Уникальный ID шаблона для создания спрайт-листа изображений. |
| Type | String | Тип шаблона. Допустимые значения: Preset: предустановленный шаблон;Custom: пользовательский шаблон. |
| Name | String | Имя шаблона для создания спрайт-листа изображений. |
| Width | Integer | Ширина подизображения спрайт-листа. |
| Height | Integer | Высота подизображения спрайт-листа. |
| ResolutionAdaptive | String | Адаптация разрешения. Допустимые значения: open: включено. В этом случае `Width` представляет длинную сторону видео, а `Height` — короткую;close: отключено. В этом случае `Width` представляет ширину видео, а `Height` — высоту. Значение по умолчанию: open. |
| SampleType | String | Тип выборки. |
| SampleInterval | Integer | Интервал выборки. |
| RowCount | Integer | Количество строк подизображений спрайт-листа. |
| ColumnCount | Integer | Количество столбцов подизображений спрайт-листа. |
| CreateTime | String | Время создания шаблона в [формате даты ISO](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |
| UpdateTime | String | Время последнего изменения шаблона в [формате даты ISO](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |
| FillType | String | Тип заполнения. "Заполнение" относится к способу обработки скриншота, когда его соотношение сторон отличается от соотношения сторон исходного видео. Поддерживаются следующие типы заполнения:  stretch: растяжение. Скриншот будет растянут кадр за кадром, чтобы соответствовать соотношению сторон исходного видео, что может сделать скриншот "короче" или "длиннее";black: заполнение черным. Этот параметр сохраняет соотношение сторон исходного видео для скриншота и заполняет несовпадающую область черными блоками. Значение по умолчанию: black. |
| Comment | String | Описание шаблона. |
| Format | String | Формат изображения. |

## ImageTaskInput

Параметры входных данных задачи обработки изображения

Используется действиями: CreateProcessImageTemplate, DescribeProcessImageTemplates, ModifyProcessImageTemplate, ProcessImage.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| EncodeConfig | [ImageEncodeConfig](#ImageEncodeConfig) | No | Конфигурация кодирования изображения. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимое значение. |
| EnhanceConfig | [ImageEnhanceConfig](#ImageEnhanceConfig) | No | Конфигурация расширения изображения. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимое значение. |
| EraseConfig | [ImageEraseConfig](#ImageEraseConfig) | No | Конфигурация стирания изображения. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимое значение. |

## ImageWatermarkInput

Входной параметр шаблона водяного знака на изображении

Используется действиями: CreateWatermarkTemplate.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| ImageContent | String | Yes | Строка, созданная путем [кодирования Base64](https://tools.ietf.org/html/rfc4648) изображения водяного знака. Поддерживаются изображения JPEG и PNG. |
| Width | String | No | Ширина водяного знака, поддерживающая два формата: % и px. Если строка заканчивается на %, то `Width` водяного знака является процентом от ширины видео. Например, `10%` означает, что `Width` составляет 10% ширины видео.Если строка заканчивается на px, то `Width` водяного знака будет в пикселях. Например, `100px` означает, что `Width` составляет 100 пикселей. Диапазон значений: [8, 4096].  Если ширина и высота не указаны или установлены в 0, значение по умолчанию составляет 10%. |
| Height | String | No | Высота водяного знака. Поддерживаются форматы % и px: если строка заканчивается на %, то `Height` водяного знака будет указанным процентом высоты видео. Например, `10%` означает, что `Height` составляет 10% высоты видео;если строка заканчивается на px, то `Height` водяного знака будет в пикселях. Например, `100px` означает, что `Height` составляет 100 пикселей. Диапазон значений: 0 или [8, 4096]. Значение по умолчанию: 0px, что означает, что `Height` будет пропорционально масштабирован в соответствии с соотношением сторон исходного изображения водяного знака. |
| RepeatType | String | No | Тип повтора анимированного водяного знака. Допустимые значения: once: больше не отображается после завершения воспроизведения водяного знака.repeat_last_frame: остается на последнем кадре после завершения воспроизведения водяного знака.repeat (по умолчанию): повторяется при воспроизведении до конца видео. |

## ImageWatermarkInputForUpdate

Входной параметр шаблона водяного знака на изображении

Используется действиями: ModifyWatermarkTemplate.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| ImageContent | String | No | Строка, созданная путем [кодирования Base64](https://tools.ietf.org/html/rfc4648) изображения водяного знака. Поддерживаются изображения JPEG и PNG. |
| Width | String | No | Ширина водяного знака. Поддерживаются форматы % и px: если строка заканчивается на %, то `Width` водяного знака будет указанным процентом ширины видео. Например, `10%` означает, что `Width` составляет 10% ширины видео;если строка заканчивается на px, то `Width` водяного знака будет в пикселях. Например, `100px` означает, что `Width` составляет 100 пикселей. Диапазон значений: [8, 4096]. |
| Height | String | No | Высота водяного знака. Поддерживаются форматы % и px: если строка заканчивается на %, то `Height` водяного знака будет указанным процентом высоты видео. Например, `10%` означает, что `Height` составляет 10% высоты видео;если строка заканчивается на px, то `Height` водяного знака будет в пикселях. Например, `100px` означает, что `Height` составляет 100 пикселей. Диапазон значений: 0 или [8, 4096]. |
| RepeatType | String | No | Тип повтора анимированного водяного знака. Допустимые значения: once: больше не отображается после завершения воспроизведения водяного знака.repeat_last_frame: остается на последнем кадре после завершения воспроизведения водяного знака.repeat (по умолчанию): повторяется при воспроизведении до конца видео. |

## ImageWatermarkTemplate

Шаблон водяного знака на изображении

Используется действиями: DescribeWatermarkTemplates.

| Name | Type | Description |
| --- | --- | --- |
| ImageUrl | String | Адрес изображения водяного знака. |
| Width | String | Ширина водяного знака. Поддерживаются форматы % и px: если строка заканчивается на %, то `Width` водяного знака будет указанным процентом ширины видео; например, `10%` означает, что `Width` составляет 10% ширины видео;если строка заканчивается на px, то `Width` водяного знака будет в px; например, `100px` означает, что `Width` составляет 100 px. |
| Height | String | Высота водяного знака. Поддерживаются форматы % и px: если строка заканчивается на %, то `Height` водяного знака будет указанным процентом высоты видео. Например, `10%` означает, что `Height` составляет 10% высоты видео;если строка заканчивается на px, то `Height` водяного знака будет в пикселях. Например, `100px` означает, что `Height` составляет 100 пикселей. `0px` означает, что `Height` будет пропорционально масштабирован в соответствии с шириной видео. |
| RepeatType | String | Тип повтора анимированного водяного знака. Допустимые значения: once: больше не отображается после завершения воспроизведения водяного знака.repeat_last_frame: остается на последнем кадре после завершения воспроизведения водяного знака.repeat (по умолчанию): повторяется при воспроизведении до конца видео. |

## LiveActivityResItem

Выход подзадачи схемы прямой трансляции.

Используется действиями: DescribeTaskDetail.

| Name | Type | Description |
| --- | --- | --- |
| LiveRecordTask | [LiveScheduleLiveRecordTaskResult](#LiveScheduleLiveRecordTaskResult) | Выход задачи записи прямой трансляции. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимые значения. |
| LiveQualityControlTask | [ScheduleQualityControlTaskResult](#ScheduleQualityControlTaskResult) | Выход задачи проверки качества медиа. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимые значения. |

## LiveActivityResult

Выход подзадачи схемы прямой трансляции.

Используется действиями: DescribeTaskDetail.

| Name | Type | Description |
| --- | --- | --- |
| ActivityType | String | Тип атомной задачи. LiveRecord: запись прямой трансляцииAiQualityControl: проверка качества медиа |
| LiveActivityResItem | [LiveActivityResItem](#LiveActivityResItem) | Выход задачи. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимые значения. |

## LiveAiAnalysisDescriptionItem

Информация о результате резюме прямой трансляции.

Используется действиями: ParseLiveStreamProcessNotification.

| Name | Type | Description |
| --- | --- | --- |
| Paragraphs | Array of [LiveAiParagraphInfo](#LiveAiParagraphInfo) | Результат сегментации. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимые значения. |

## LiveAiParagraphInfo

Информация о сегменте.

Используется действиями: ParseLiveStreamProcessNotification.

| Name | Type | Description |
| --- | --- | --- |
| Summary | String | Резюме сегмента. |
| Title | String | Название сегмента. |
| Keywords | Array of String | Ключевое слово сегмента. |
| StartTimeOffset | Float | Начальная точка сегмента в секундах. |
| EndTimeOffset | Float | Конечная точка сегмента в секундах. |
| BeginTime | String | Начальная точка сегмента прямой трансляции в формате даты и времени ISO. |
| EndTime | String | Конечная точка сегмента прямой трансляции в формате даты и времени ISO. |

## LiveRecordFile

Информация о файле записи прямой трансляции.

Используется действиями: DescribeTaskDetail, ParseLiveStreamProcessNotification.

| Name | Type | Description |
| --- | --- | --- |
| Url | String | URL файла записи. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимые значения. |
| Size | Integer | Размер файла записи. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимые значения. |
| Duration | Integer | Длительность файла записи. Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимые значения. |
| StartTime | String | Время начала записи в [формате даты ISO](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52). Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимые значения. |
| EndTime | String | Время окончания записи в [формате даты ISO](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52). Примечание: Это поле может быть null, что указывает на то, что не удалось получить допустимые значения. |

## LiveRecordResult

Результат записи прямой трансляции.

Используется действиями: Describe

## LiveStreamAiReviewImagePoliticalResult

Результат обнаружения конфиденциальной информации в видео трансляции.

Используется действиями: ParseLiveStreamProcessNotification.

| Name | Type | Description |
| --- | --- | --- |
| StartPtsTime | Float | Начальное время PTS подозрительного сегмента в секундах. |
| EndPtsTime | Float | Конечное время PTS подозрительного сегмента в секундах. |
| Confidence | Float | Оценка уверенности для обнаруженных подозрительных сегментов. |
| Suggestion | String | Предложение для обнаружения информации о порнографии в подозрительном сегменте. Допустимые значения: passreviewblock |
| Label | String | Метки для обнаруженной конфиденциальной информации. Допустимые значения: politicianviolation_photo (запрещенные значки) |
| Name | String | Имя конфиденциального лица или запрещенного значка. |
| AreaCoordSet | Array of Integer | Пиксельные координаты обнаруженных конфиденциальных лиц или запрещенных значков. Формат: [x1, y1, x2, y2], что указывает координаты верхнего левого и нижнего правого углов. |
| Url | String | URL подозрительного изображения (которое не будет постоянно сохраняться и будет удалено после `PicUrlExpireTime`). |
| PicUrlExpireTime | String | Время истечения URL подозрительного изображения в [формате даты ISO](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |

## LiveStreamAiReviewImagePornResult

Результат обнаружения порнографической информации в изображении при проверке контента трансляции на основе ИИ

Используется действиями: ParseLiveStreamProcessNotification.

| Name | Type | Description |
| --- | --- | --- |
| StartPtsTime | Float | Начальное время PTS подозрительного сегмента в секундах. |
| EndPtsTime | Float | Конечное время PTS подозрительного сегмента в секундах. |
| Confidence | Float | Оценка подозрительного порнографического сегмента. |
| Suggestion | String | Предложение для обнаружения информации о порнографии в подозрительном сегменте. Допустимые значения: passreviewblock |
| Label | String | Тег обнаруженной порнографической информации в видео. Допустимые значения: porn: Порнография.sexy: Сексуальность.vulgar: Вульгарность.intimacy: Интимность. |
| Url | String | URL подозрительного изображения (которое не будет постоянно сохраняться и будет удалено после `PicUrlExpireTime`). |
| PicUrlExpireTime | String | Время истечения URL подозрительного изображения в [формате даты ISO](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |

## LiveStreamAiReviewImageTerrorismResult

Результат обнаружения конфиденциальной информации в видео трансляции.

Используется действиями: ParseLiveStreamProcessNotification.

| Name | Type | Description |
| --- | --- | --- |
| StartPtsTime | Float | Начальное время PTS подозрительного сегмента в секундах. |
| EndPtsTime | Float | Конечное время PTS подозрительного сегмента в секундах. |
| Confidence | Float | Оценка уверенности для обнаруженных подозрительных сегментов. |
| Suggestion | String | Предложение по обработке подозрительных сегментов. Допустимые значения: passreviewblock |
| Label | String | Метки для обнаруженного конфиденциального контента. Допустимые значения: gunscrowdpolicebloodybanners (конфиденциальные флаги)militantexplosionterrorists |
| Url | String | URL подозрительного изображения (которое не будет постоянно сохраняться и будет удалено после `PicUrlExpireTime`). |
| PicUrlExpireTime | String | Время истечения URL подозрительного изображения в [формате даты ISO](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |

## LiveStreamAiReviewResultInfo

Результат проверки трансляции на основе ИИ

Используется действиями: ParseLiveStreamProcessNotification.

| Name | Type | Description |
| --- | --- | --- |
| ResultSet | Array of [LiveStreamAiReviewResultItem](#LiveStreamAiReviewResultItem) | Список результатов проверки контента. |

## LiveStreamAiReviewResultItem

Результат проверки трансляции на основе ИИ

Используется действиями: ParseLiveStreamProcessNotification.

| Name | Type | Description |
| --- | --- | --- |
| Type | String | Тип результата модерации. Допустимые значения: ImagePornImageTerrorismImagePoliticalVoicePorn |
| ImagePornResultSet | Array of [LiveStreamAiReviewImagePornResult](#LiveStreamAiReviewImagePornResult) | Результат обнаружения порнографической информации в изображении, действителен, если `Type` имеет значение `ImagePorn`. |
| ImageTerrorismResultSet | Array of [LiveStreamAiReviewImageTerrorismResult](#LiveStreamAiReviewImageTerrorismResult) | Результат обнаружения конфиденциальной информации в изображениях, действителен, если `Type` имеет значение `ImageTerrorism`. |
| ImagePoliticalResultSet | Array of [LiveStreamAiReviewImagePoliticalResult](#LiveStreamAiReviewImagePoliticalResult) | Результат обнаружения конфиденциальной информации в изображениях, действителен, если `Type` имеет значение `ImagePolitical`. |
| VoicePornResultSet | Array of [LiveStreamAiReviewVoicePornResult](#LiveStreamAiReviewVoicePornResult) | Результат модерации порнографического контента в аудио. Этот параметр действителен, если `Type` имеет значение `VoicePorn`. |

## LiveStreamAiReviewVoicePornResult

Результат обнаружения порнографической информации в речи при проверке контента трансляции на основе ИИ

Используется действиями: ParseLiveStreamProcessNotification.

| Name | Type | Description |
| --- | --- | --- |
| StartPtsTime | Float | Начальное время PTS подозрительного сегмента в секундах. |
| EndPtsTime | Float | Конечное время PTS подозрительного сегмента в секундах. |
| Confidence | Float | Оценка подозрительного порнографического сегмента. |
| Suggestion | String | Предложение для обнаружения информации о порнографии в подозрительном сегменте. Допустимые значения: passreviewblock |
| Label | String | Тег обнаруженной порнографической информации в видео. Допустимые значения: sexual_moan: Сексуальные стоны. |

## LiveStreamAiSmartSubtitleResultInfo

Результат задачи интеллектуального субтитрирования для трансляции.

Используется действиями: ParseLiveStreamProcessNotification.

| Name | Type | Description |
| --- | --- | --- |
| SmartSubtitleResult | Array of [LiveSmartSubtitleResult](#LiveSmartSubtitleResult) | Список результатов задачи интеллектуального субтитрирования трансляции. |

## LiveStreamAsrFullTextRecognitionResult

Полное распознавание трансляции на основе ASR

Используется действиями: ParseLiveStreamProcessNotification.

| Name | Type | Description |
| --- | --- | --- |
| Text | String | Распознанный текст. |
| StartPtsTime | Float | Начальное время PTS распознанного сегмента в секундах. |
| EndPtsTime | Float | Конечное время PTS распознанного сегмента в секундах. |
| Confidence | Float | Уверенность распознанного сегмента. Диапазон значений: 0–100. |
| StartTime | String |  |
| EndTime | String |  |
| SteadyState | Boolean |  |
| UserId | String | ID пользователя в результате распознавания через WebSocket и TRTC.Примечание: Это поле может возвращать null, что указывает на то, что допустимое значение не найдено. |

## LiveStreamAsrWordsRecognitionResult

Результат распознавания ключевых слов в трансляции на основе ASR и ИИ

Используется действиями: ParseLiveStreamProcessNotification.

| Name | Type | Description |
| --- | --- | --- |
| Word | String | Ключевое слово речи. |
| StartPtsTime | Float | Начальное время PTS распознанного сегмента в секундах. |
| EndPtsTime | Float | Конечное время PTS распознанного сегмента в секундах. |
| Confidence | Float | Уверенность распознанного сегмента. Диапазон значений: 0–100. |

## LiveStreamFaceRecognitionResult

Результат распознавания лиц в трансляции на основе ИИ

Используется действиями: ParseLiveStreamProcessNotification.

| Name | Type | Description |
| --- | --- | --- |
| Id | String | Уникальный ID персоны. |
| Name | String | Имя персоны. |
| Type | String | Тип библиотеки персон, указывающий, какой библиотеке персон принадлежит распознанная персона: Default: библиотека персон по умолчаниюUserDefine: пользовательская библиотека |
| StartPtsTime | Float | Начальное время PTS распознанного сегмента в секундах. |
| EndPtsTime | Float | Конечное время PTS распознанного сегмента в секундах. |
| Confidence | Float | Уверенность распознанного сегмента. Диапазон значений: 0–100. |
| AreaCoordSet | Array of Integer | Координаты зоны результата распознавания. Массив содержит четыре элемента: [x1,y1,x2,y2], то есть горизонтальные и вертикальные координаты верхнего левого и нижнего правого углов. |

## LiveStreamObjectRecognitionResult

Результат распознавания объектов в трансляции на основе ИИ.

Используется действиями: ParseLiveStreamProcessNotification.

| Name | Type | Description |
| --- | --- | --- |
| Name | String | Имя распознанного объекта. |
| StartPtsOffset | Float | Начальное время PTS распознанного сегмента в секундах. |
| EndPtsOffset | Float | Конечное время PTS распознанного сегмента в секундах. |
| Confidence | Float | Уверенность распознанного сегмента. Диапазон значений: 0-100. |
| AreaCoordSet | Array of Integer | Координаты зоны результата распознавания. Массив содержит четыре элемента: [x1, y1, x2, y2], представляющие горизонтальные и вертикальные координаты верхнего левого и нижнего правого углов соответственно. |
| Url | String | Ссылка на скриншот. Примечание: Это поле может возвращать null, что указывает на то, что допустимые значения не получены. |

## LiveStreamOcrFullTextRecognitionResult

Полное распознавание трансляции на основе OCR

Используется действиями: ParseLiveStreamProcessNotification.

| Name | Type | Description |
| --- | --- | --- |
| Text | String | Текст речи. |
| StartPtsTime | Float | Начальное время PTS распознанного сегмента в секундах. |
| EndPtsTime | Float | Конечное время PTS распознанного сегмента в секундах. |
| Confidence | Float | Уверенность распознанного сегмента. Диапазон значений: 0–100. |
| AreaCoordSet | Array of Integer | Координаты зоны результата распознавания. Массив содержит четыре элемента: [x1,y1,x2,y2], то есть горизонтальные и вертикальные координаты верхнего левого и нижнего правого углов. |

## LiveStreamOcrWordsRecognitionResult

Результат распознавания ключевых слов в трансляции на основе OCR и ИИ

Используется действиями: ParseLiveStreamProcessNotification.

| Name | Type | Description |
| --- | --- | --- |
| Word | String | Ключевое слово текста. |
| StartPtsTime | Float | Начальное время PTS распознанного сегмента в секундах. |
| EndPtsTime | Float | Конечное время PTS распознанного сегмента в секундах. |
| Confidence | Float | Уверенность распознанного сегмента. Диапазон значений: 0–100. |
| AreaCoords | Array of Integer | Координаты зоны результата распознавания. Массив содержит четыре элемента: [x1,y1,x2,y2], то есть горизонтальные и вертикальные координаты верхнего левого и нижнего правого углов. |

## LiveStreamProcessErrorInfo

Информация об ошибке обработки трансляции

Используется действиями: ParseLiveStreamProcessNotification.

| Name | Type | Description |
| --- | --- | --- |
| ErrCode | Integer | Код ошибки: 0: Нет ошибки;Если этот параметр не равен 0, произошла ошибка. Пожалуйста, см. сообщение об ошибке (`Message`). |
| Message | String | Сообщение об ошибке. |

## LiveStreamProcessTask

Информация о задаче обработки трансляции

Используется действиями: DescribeTaskDetail.

| Name | Type | Description |
| --- | --- | --- |
| TaskId | String | ID задачи обработки медиа. |
| Status | String | Статус потока задач. Допустимые значения: PROCESSING: Обработка;FINISH: Завершено. |
| ErrCode | Integer | Код ошибки. 0: успех; другие значения: ошибка. |
| Message | String | Сообщение об ошибке. |
| Url | String | URL трансляции. |

## LiveStreamRecordResultInfo

Результат записи трансляции.

Используется действиями: ParseLiveStreamProcessNotification.

| Name | Type | Description |
| --- | --- | --- |
| RecordOver | Integer | Завершилась ли запись. 0: Запись не завершена, возвращается один файл. 1: Запись завершена, возвращаются все файлы записи. Примечание: Это поле может возвращать null, что указывает на то, что допустимые значения не получены. |
| FileResults | Array of [LiveRecordFile](#LiveRecordFile) | Список файлов.  Примечание: Это поле может возвращать null, что указывает на то, что допустимые значения не получены. |

## LiveStreamTagRecognitionResult

Используется действиями: ParseLiveStreamProcessNotification.

| Name | Type | Description |
| --- | --- | --- |
| Id | String |  |
| StartPtsTime | Float |  |
| EndPtsTime | Float |  |
| Confidence | Float |  |

## LiveStreamTaskNotifyConfig

Конфигурация уведомления о событии задачи.

Используется действиями: ProcessLiveStream.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| NotifyType | String | No | Тип уведомления: TDMQ-CMQ: очередь сообщений. "URL": Когда указан URL, обратные вызовы HTTP отправляются на адрес, указанный в NotifyUrl. Протокол обратного вызова — HTTP+JSON. Содержимое текста пакета совпадает с выходными параметрами [ParseLiveStreamProcessNotification](https://www.tencentcloud.comom/document/product/862/39229?from_cn_redirect=1).  Примечание: если не указано или оставлено пустым, обратный вызов не будет отправлен. Чтобы отправить обратный вызов, заполните соответствующее значение типа. |
| NotifyUrl | String | No | URL для HTTP обратного вызова, обязателен, если для `NotifyType` установлено значение `URL` |
| CmqModel | String | No | Предоставляются модели Queue и Topic. |
| CmqRegion | String | No | Регион, когда NotifyType установлено на TDMQ-CMQ. Например, sh или bj. |
| QueueName | String | No | Это поле действительно при модели Queue. Указывает имя очереди TDMQ for CMQ для получения уведомлений о событиях. |
| TopicName | String | No | Это поле действительно при модели Topic. Указывает имя темы TDMQ for CMQ для получения уведомлений о событиях. |
| NotifyKey | String | No | Ключ, используемый для создания подписи обратного вызова. Примечание: Это поле может возвращать null, что указывает на то, что допустимые значения не получены. |

## LiveStreamTransTextRecognitionResult

Результат перевода трансляции.

Используется действиями: ParseLiveStreamProcessNotification.

| Name | Type | Description |
| --- | --- | --- |
| Text | String | Расшифровка текста. |
| StartPtsTime | Float | PTS (секунды) начала сегмента. |
| EndPtsTime | Float | PTS (секунды) конца сегмента. |
| Confidence | Float | Оценка уверенности для сегмента. Диапазон значений: 0-100. |
| Trans | String | Перевод. |
| StartTime | String |  |
| EndTime | String |  |
| SteadyState | Boolean |  |
| UserId | String | ID пользователя в результате перевода в реальном времени через WebSocket и TRTC. Примечание: Это поле может возвращать null, что указывает на то, что допустимое значение не найдено. |

## LowLightEnhanceConfig

Конфигурация улучшения при низком освещении.

Используется действиями: CreateProcessImageTemplate, CreateTranscodeTemplate, ModifyProcessImageTemplate, ModifyTranscodeTemplate, ProcessImage.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Switch | String | No | Включена ли функция. Допустимые значения: ONOFF Значение по умолчанию: ON. |
| Type | String | No | Интенсивность. Допустимые значения: normal Значение по умолчанию: normal. Примечание: Это поле может возвращать null, что указывает на то, что допустимые значения не получены. |

## MP4ConfigureInfo

Параметр конфигурации MP4.

Используется действиями: CreateLiveRecordTemplate, DescribeLiveRecordTemplates, ModifyLiveRecordTemplate.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Interval | Integer | No | Длительность записи в секундах. Интервал может варьироваться от 10 минут до 720 минут. По умолчанию установлено значение 60 минут (3600 секунд). |

## MediaAiAnalysisClassificationItem

Результат интеллектуальной категоризации

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| Classification | String | Имя интеллектуально созданной категории. |
| Confidence | Float | Уверенность интеллектуально созданной категории от 0 до 100. |

## MediaAiAnalysisCoverItem

Информация об интеллектуально созданном обложке

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| CoverPath | String | Путь хранения интеллектуально созданной обложки. |
| Confidence | Float | Уверенность интеллектуально созданной обложки от 0 до 100. |

## MediaAiAnalysisDescriptionItem

Информация об интеллектуальном описании.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| Description | String | Интеллектуальное описание. |
| Confidence | Float | Уверенность интеллектуального описания с диапазоном значений от 0 до 100. |
| Title | String | Заголовок интеллектуального описания. |
| Keywords | Array of String | Ключевые слова интеллектуального описания. |
| Paragraphs | Array of [AiParagraphInfo](#AiParagraphInfo) | Результат сегментации. Примечание: Это поле может возвращать null, что указывает на то, что допустимые значения не получены. |
| MindMapUrl | String | Адрес интеллект-карты задачи суммирования. Примечание: Это поле может возвращать null, что указывает на то, что допустимое значение не получено. |
| MindMapPath | String | Путь интеллект-карты задачи суммирования. |
| SubtitlePath | String | Путь файла субтитров видео. |
| OutputStorage | [TaskOutputStorage](#TaskOutputStorage) | Место хранения файла суммирования. |

## MediaAiAnalysisFrameTagItem

Информация о результате интеллектуального отмечивания кадров

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| Tag | String | Имя тега кадра. |
| CategorySet | Array of String |  |
| Confidence | Float | Уверенность интеллектуально созданного тега кадра между 0 и 100. |

## MediaAiAnalysisFrameTagSegmentItem

Список сегментов тега кадра

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| StartTimeOffset | Float | Начальное смещение времени тега кадра. |
| EndTimeOffset | Float | Конечное смещение времени тега кадра. |
| TagSet | Array of [MediaAiAnalysisFrameTagItem](#MediaAiAnalysisFrameTagItem) | Список тегов в периоде времени. |

## MediaAiAnalysisHighlightItem

Информация об интеллектуально созданных сегментах выделения.

Используется действиями: DescribeTaskDetail, ParseLiveStreamProcessNotification, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| HighlightPath | String | URL сегментов выделения. |
| CovImgPath | String | URL миниатюры. |
| Confidence | Float | Оценка уверенности. Диапазон значений: 0-100. |
| Duration | Float | Длительность выделения. |
| SegmentSet | Array of [HighlightSegmentItem](#HighlightSegmentItem) | Список сегментов выделения. |
| HighlightUrl | String | Адрес интеллектуального выделения. Примечание: Это поле может возвращать null, что указывает на то, что допустимые значения не получены. |
| CovImgUrl | String | Адрес обложки интеллектуального выделения. Примечание: Это поле может возвращать null, что указывает на то, что допустимые значения не получены. |

## MediaAiAnalysisTagItem

Информация о результате интеллектуального отмечивания

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| Tag | String | Имя тега. |
| Confidence | Float | Уверенность тега между 0 и 100. |
| SpecialInfo | String | Варьируется в зависимости от разных типов. |

## MediaAnimatedGraphicsItem

Информация о результате задачи создания анимированного изображения

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| Storage | [TaskOutputStorage](#TaskOutputStorage) | Место хранения созданного файла анимированного изображения. |
| Path | String | Путь к созданному файлу анимированного изображения. |
| Definition | Integer | Указывает ID шаблона вращающегося изображения. см. [шаблон вращающегося изображения](https://intl.cloud.tencent.com/document/product/862/77168?from_cn_redirect=1#.E8.BD.AC.E5.8A.A8.E5.9B.BE.E6.A8.A1.E6.9D.BF.5B.5D(ID.3Amove)). |
| Container | String | Формат анимированного изображения, например gif. |
| Height | Integer | Высота анимированного изображения в пикселях. |
| Width | Integer | Ширина анимированного изображения в пикселях. |
| Bitrate | Integer | Битрейт анимированного изображения в бит/сек. |
| Size | Integer | Размер анимированного изображения в байтах. |
| Md5 | String | Значение MD5 анимированного изображения. |
| StartTimeOffset | Float | Начальное смещение времени анимированного изображения в видео в секундах. |
| EndTimeOffset | Float | Конечное смещение времени анимированного изображения в видео в секундах. |

## MediaAudioStreamItem

Информация об аудиопотоке в файле VOD

Используется действиями: DescribeBatchTaskDetail, DescribeMediaMetaData, DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| Bitrate | Integer | Битрейт аудиопотока в бит/сек. Примечание: Это поле может возвращать null, что указывает на то, что допустимые значения не получены. |
| SamplingRate | Integer | Частота дискретизации аудиопотока в Гц. Примечание: Это поле может возвращать null, что указывает на то, что допустимые значения не получены. |
| Codec | String | Кодек аудиопотока, например aac. Примечание: Это поле может возвращать null, что указывает на то, что допустимые значения не получены. |
| Channel | Integer | Количество звуковых каналов, например 2. Примечание: это поле может возвращать `null`, что указывает на то, что допустимое значение не найдено. |

## MediaContentReviewAsrTextSegmentItem

Подозрительный сегмент, выявленный при аудите текста на основе ASR при проверке контента

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| StartTimeOffset | Float | Начальное смещение времени подозрительного сегмента в секундах. |
| EndTimeOffset | Float | Конечное смещение времени подозрительного сегмента в секундах. |
| Confidence | Float | Уверенность подозрительного сегмента. |
| Suggestion | String | Предложение для аудита подозрительного сегмента. Допустимые значения: pass.review.block. |
| KeywordSet | Array of String | Список подозрительных ключевых слов. |

## MediaContentReviewOcrTextSegmentItem

Подозрительный сегмент, выявленный при аудите текста на основе OCR при проверке контента

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| StartTimeOffset | Float | Начальное смещение времени подозрительного сегмента в секундах. |
| EndTimeOffset | Float | Конечное смещение времени подозрительного сегмента в секундах. |
| Confidence | Float | Уверенность подозрительного сегмента. |
| Suggestion | String | Предложение для аудита подозрительного сег

## MediaProcessTaskAnimatedGraphicResult

Тип результата задачи генерации анимированного изображения

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: PROCESSING, SUCCESS, FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи; любое другое значение указывает на ошибку выполнения. Подробнее см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1041/40249). |
| ErrCode | Integer | Код ошибки. 0 указывает на успешное выполнение задачи; в остальных случаях — ошибка. Этот параметр больше не рекомендуется. Используйте новый параметр кода ошибки ErrCodeExt. |
| Message | String | Сообщение об ошибке. |
| Input | [AnimatedGraphicTaskInput](#AnimatedGraphicTaskInput) | Входные данные для задачи генерации анимированного изображения. |
| Output | [MediaAnimatedGraphicsItem](#MediaAnimatedGraphicsItem) | Выходные данные задачи генерации анимированного изображения. Примечание: это поле может возвращать null, указывая на то, что нет доступных значений. |

## MediaProcessTaskImageSpriteResult

Тип результата задачи генерации спрайта изображения

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: PROCESSING, SUCCESS, FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи; любое другое значение указывает на ошибку выполнения. Подробнее см. [Коды ошибок](https://www.tencentcloud.com/document/api/1041/33691). |
| ErrCode | Integer | Код ошибки. 0 указывает на успешное выполнение задачи; в остальных случаях — ошибка. Этот параметр больше не рекомендуется. Используйте новый параметр кода ошибки ErrCodeExt. |
| Message | String | Сообщение об ошибке. |
| Input | [ImageSpriteTaskInput](#ImageSpriteTaskInput) | Входные данные для задачи генерации спрайта изображения. |
| Output | [MediaImageSpriteItem](#MediaImageSpriteItem) | Выходные данные задачи спрайта изображения для видео. Примечание: это поле может возвращать null, указывая на то, что нет доступного значения. |
| BeginProcessTime | String | Время начала выполнения задачи в формате даты и времени ISO. |
| FinishTime | String | Время завершения выполнения задачи в формате даты и времени ISO. |

## MediaProcessTaskInput

Тип задачи обработки медиа.

Используется действиями: CreateWorkflow, DescribeWorkflows, ProcessMedia, ResetWorkflow.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| TranscodeTaskSet | Array of [TranscodeTaskInput](#TranscodeTaskInput) | No | Список задач трансодирования. |
| AnimatedGraphicTaskSet | Array of [AnimatedGraphicTaskInput](#AnimatedGraphicTaskInput) | No | Список задач создания скриншотов анимированного изображения. |
| SnapshotByTimeOffsetTaskSet | Array of [SnapshotByTimeOffsetTaskInput](#SnapshotByTimeOffsetTaskInput) | No | Список задач создания скриншотов в определённые моменты времени. |
| SampleSnapshotTaskSet | Array of [SampleSnapshotTaskInput](#SampleSnapshotTaskInput) | No | Список задач создания выборочных скриншотов. |
| ImageSpriteTaskSet | Array of [ImageSpriteTaskInput](#ImageSpriteTaskInput) | No | Список задач создания спрайтов изображения. |
| AdaptiveDynamicStreamingTaskSet | Array of [AdaptiveDynamicStreamingTaskInput](#AdaptiveDynamicStreamingTaskInput) | No | Список задач адаптивного потокового вещания с переменной скоростью передачи данных. |

## MediaProcessTaskResult

Тип результата запроса задачи

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| Type | String | Тип задачи. Допустимые значения: Transcode: ТрансодированиеAnimatedGraphics: Генерация анимированного изображенияSnapshotByTimeOffset: Скриншот в определённый момент времениSampleSnapshot: Выборочный скриншотImageSprites: Спрайт изображенияCoverBySnapshot: Скриншот для обложкиAdaptiveDynamicStreaming: Адаптивное потоковое вещание с переменной скоростью передачи данных |
| TranscodeTask | [MediaProcessTaskTranscodeResult](#MediaProcessTaskTranscodeResult) | Результат запроса задачи трансодирования, действительный когда тип задачи — `Transcode`. Примечание: это поле может возвращать null, указывая на то, что нет доступных значений. |
| AnimatedGraphicTask | [MediaProcessTaskAnimatedGraphicResult](#MediaProcessTaskAnimatedGraphicResult) | Результат запроса задачи генерации анимированного изображения, действительный когда тип задачи — `AnimatedGraphics`. Примечание: это поле может возвращать null, указывая на то, что нет доступных значений. |
| SnapshotByTimeOffsetTask | [MediaProcessTaskSnapshotByTimeOffsetResult](#MediaProcessTaskSnapshotByTimeOffsetResult) | Результат запроса задачи создания скриншота в определённый момент времени, действительный когда тип задачи — `SnapshotByTimeOffset`. Примечание: это поле может возвращать null, указывая на то, что нет доступных значений. |
| SampleSnapshotTask | [MediaProcessTaskSampleSnapshotResult](#MediaProcessTaskSampleSnapshotResult) | Результат запроса задачи создания выборочного скриншота, действительный когда тип задачи — `SampleSnapshot`. Примечание: это поле может возвращать null, указывая на то, что нет доступных значений. |
| ImageSpriteTask | [MediaProcessTaskImageSpriteResult](#MediaProcessTaskImageSpriteResult) | Результат запроса задачи создания спрайта изображения, действительный когда тип задачи — `ImageSprite`. Примечание: это поле может возвращать null, указывая на то, что нет доступных значений. |
| AdaptiveDynamicStreamingTask | [MediaProcessTaskAdaptiveDynamicStreamingResult](#MediaProcessTaskAdaptiveDynamicStreamingResult) | Результат запроса задачи адаптивного потокового вещания с переменной скоростью передачи данных, действительный если тип задачи — `AdaptiveDynamicStreaming`. Примечание: это поле может возвращать null, указывая на то, что нет доступных значений. |

## MediaProcessTaskSampleSnapshotResult

Тип результата задачи создания выборочного скриншота

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: PROCESSING, SUCCESS, FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи; любое другое значение указывает на ошибку выполнения. Подробнее см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1041/40249). |
| ErrCode | Integer | Код ошибки. 0 указывает на успешное выполнение задачи; в остальных случаях — ошибка. Этот параметр больше не рекомендуется. Используйте новый параметр кода ошибки ErrCodeExt. |
| Message | String | Сообщение об ошибке. Примечание: это поле может возвращать null, указывая на то, что нет доступных значений. |
| Input | [SampleSnapshotTaskInput](#SampleSnapshotTaskInput) | Входные данные для задачи создания выборочного скриншота. |
| Output | [MediaSampleSnapshotItem](#MediaSampleSnapshotItem) | Выходные данные задачи создания выборочного скриншота для видео. Примечание: это поле может возвращать null, указывая на то, что нет доступного значения. |
| BeginProcessTime | String | Время начала выполнения задачи в [формате даты и времени ISO](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52). |
| FinishTime | String | Время завершения выполнения задачи в [формате даты и времени ISO](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52). |

## MediaProcessTaskSnapshotByTimeOffsetResult

Тип результата задачи создания скриншота в определённый момент времени

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: PROCESSING, SUCCESS, FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи; любое другое значение указывает на ошибку выполнения. Подробнее см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1041/40249). |
| ErrCode | Integer | Код ошибки. 0 указывает на успешное выполнение задачи; в остальных случаях — ошибка. Этот параметр больше не рекомендуется. Используйте новый параметр кода ошибки ErrCodeExt. |
| Message | String | Сообщение об ошибке. |
| Input | [SnapshotByTimeOffsetTaskInput](#SnapshotByTimeOffsetTaskInput) | Входные данные для задачи создания скриншота в определённый момент времени. |
| Output | [MediaSnapshotByTimeOffsetItem](#MediaSnapshotByTimeOffsetItem) | Выходные данные задачи создания скриншота в определённый момент времени для видео. Примечание: это поле может возвращать null, указывая на то, что нет доступного значения. |
| BeginProcessTime | String | Время начала выполнения задачи в [формате даты и времени ISO](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52). |
| FinishTime | String | Время завершения выполнения задачи в [формате даты и времени ISO](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52). |

## MediaProcessTaskTranscodeResult

Тип результата задачи трансодирования

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: PROCESSING, SUCCESS, FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи; любое другое значение указывает на ошибку выполнения. Подробнее см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1041/40249). |
| ErrCode | Integer | Код ошибки. 0 указывает на успешное выполнение задачи; в остальных случаях — ошибка. Этот параметр больше не рекомендуется. Используйте новый параметр кода ошибки ErrCodeExt. |
| Message | String | Сообщение об ошибке. |
| Input | [TranscodeTaskInput](#TranscodeTaskInput) | Входные данные для задачи трансодирования. |
| Output | [MediaTranscodeItem](#MediaTranscodeItem) | Выходные данные задачи трансодирования. Примечание: это поле может возвращать null, указывая на то, что нет доступных значений. |
| Progress | Integer | Прогресс трансодирования в диапазоне [0-100]. |

## MediaSampleSnapshotItem

Информация о выборочном скриншоте

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| Definition | Integer | ID спецификации выборочного скриншота. Подробнее см. [Шаблон параметров выборочного скриншота](https://intl.cloud.tencent.com/document/product/266/33480?from_cn_redirect=1#.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF). |
| SampleType | String | Тип выборки. Допустимые значения: Percent: выборка на указанный процентный интервал.Time: выборка на указанный временной интервал. |
| Interval | Integer | Интервал выборки. Если `SampleType` имеет значение `Percent`, это значение означает создание скриншота через указанный процентный интервал.Если `SampleType` имеет значение `Time`, это значение означает создание скриншота через указанный временной интервал (в секундах). Первый скриншот всегда является первым кадром видео. |
| Storage | [TaskOutputStorage](#TaskOutputStorage) | Место хранения созданного файла скриншота. |
| ImagePathSet | Array of String | Список путей к созданным скриншотам. |
| WaterMarkDefinition | Array of Integer | Список ID шаблонов водяного знака, если скриншоты имеют водяной знак. |

## MediaSnapshotByTimeOffsetItem

Информация о скриншотах в определённые моменты времени в файле VOD

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| Definition | Integer | Спецификация шаблона скриншота в определённый момент времени. |
| PicInfoSet | Array of [MediaSnapshotByTimePicInfoItem](#MediaSnapshotByTimePicInfoItem) | Набор информации о скриншотах одной спецификации. Каждый элемент представляет скриншот. |
| Storage | [TaskOutputStorage](#TaskOutputStorage) | Место хранения файла скриншота в определённый момент времени. |

## MediaSnapshotByTimePicInfoItem

Информация о скриншоте в определённый момент времени

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| TimeOffset | Float | Временная метка (в секундах) скриншота. |
| Path | String | Путь к скриншоту. |
| WaterMarkDefinition | Array of Integer | Список ID шаблонов водяного знака, если скриншоты имеют водяной знак. |

## MediaTranscodeItem

Информация о трансодировании

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| OutputStorage | [TaskOutputStorage](#TaskOutputStorage) | Целевой бакет выходного файла. |
| Path | String | Путь к выходному видеофайлу. |
| Definition | Integer | ID спецификации трансодирования. Подробнее см. [Шаблон параметров трансодирования](https://intl.cloud.tencent.com/document/product/266/33478?from_cn_redirect=1#.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF). |
| Bitrate | Integer | Сумма средней скорости передачи видеопотока и среднего коэффициента звука в бит/с. |
| Height | Integer | Максимальное значение высоты видеопотока в пикселях. |
| Width | Integer | Максимальное значение ширины видеопотока в пикселях. |
| Size | Integer | Общий размер медиафайла в байтах (сумма размеров файлов m3u8 и ts, если видео в формате HLS). |
| Duration | Float | Продолжительность видео в секундах. |
| Container | String | Контейнер, например m4a и mp4. |
| Md5 | String | Значение MD5 видео. |
| AudioStreamSet | Array of [MediaAudioStreamItem](#MediaAudioStreamItem) | Информация об аудиопотоке. Примечание: это поле может возвращать null, указывая на то, что нет доступных значений. |
| VideoStreamSet | Array of [MediaVideoStreamItem](#MediaVideoStreamItem) | Информация о видеопотоке. Примечание: это поле может возвращать null, указывая на то, что нет доступных значений. |
| CallBackExtInfo | String | Элементы улучшения, используемые для видеотрансодирования. Описания элементов улучшения: hdr: конфигурация HDRwd_fps: конфигурация интерполяции кадров для более высокой частоты кадровvideo_super_resolution:     конфигурация сверхвысокого разрешенияrepair: конфигурация комплексного улучшенияdenoise: конфигурация шумоподавления видео color_enhance: конфигурация улучшения цвета scratch: конфигурация удаления царапин artifact: конфигурация удаления артефактов (помех)sharp: конфигурация улучшения деталей low_light: конфигурация улучшения при слабом освещении face_enhance: конфигурация улучшения лица Примечание: это поле может возвращать null, указывая на то, что нет доступного значения. |

## MediaVideoStreamItem

Информация о видеопотоке в файле VOD

Используется действиями: DescribeBatchTaskDetail, DescribeMediaMetaData, DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| Bitrate | Integer | Скорость передачи видеопотока в бит/с. Примечание: это поле может возвращать null, указывая на то, что нет доступных значений. |
| Height | Integer | Высота видеопотока в пикселях. Примечание: это поле может возвращать null, указывая на то, что нет доступных значений. |
| Width | Integer | Ширина видеопотока в пикселях. Примечание: это поле может возвращать null, указывая на то, что нет доступных значений. |
| Codec | String | Кодек видеопотока, например h264. Примечание: это поле может возвращать null, указывая на то, что нет доступных значений. |
| Fps | Integer | Частота кадров в Гц. Примечание: это поле может возвращать null, указывая на то, что нет доступных значений. |
| ColorPrimaries | String | Основные цвета. Примечание: это поле может возвращать `null`, указывая на то, что значение не найдено. |
| ColorSpace | String | Цветовое пространство. Примечание: это поле может возвращать `null`, указывая на то, что значение не найдено. |
| ColorTransfer | String | Цветовая передача. Примечание: это поле может возвращать `null`, указывая на то, что значение не найдено. |
| HdrType | String | Тип HDR. Примечание: это поле может возвращать `null`, указывая на то, что значение не найдено. |
| Codecs | String |  |
| FpsNumerator | Integer | Числитель частоты кадров. Примечание: это поле может возвращать null, указывая на то, что нет доступных значений. |
| FpsDenominator | Integer | Знаменатель частоты кадров. Примечание: это поле может возвращать null, указывая на то, что нет доступных значений. |

## MosaicInput

Параметры эффекта пиксельного мозаичного размытия для использования в задаче обработки медиа.

Используется действиями: CreateWorkflow, ProcessMedia, ResetWorkflow.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| CoordinateOrigin | String | No | Позиция начала координат, которая в настоящее время может быть только: TopLeft: начало координат находится в верхнем левом углу видео, и начало размытия находится в верхнем левом углу изображения или текста. Значение по умолчанию: TopLeft. |
| XPos | String | No | Горизонтальное положение начала размытия относительно начала координат видео. Поддерживаются форматы % и px: Если строка заканчивается на %, то `XPos` размытия будет указанным процентом ширины видео; например, `10%` означает, что `XPos` составляет 10% ширины видео;Если строка заканчивается на px, то `XPos` размытия будет указанным пиксельным значением; например, `100px` означает, что `XPos` составляет 100 пикселей. Значение по умолчанию: 0 px. |
| YPos | String | No | Вертикальное положение начала размытия относительно начала координат видео. Поддерживаются форматы % и px: Если строка заканчивается на %, то `YPos` размытия будет указанным процентом высоты видео; например, `10%` означает, что `YPos` составляет 10% высоты видео;Если строка заканчивается на px, то `YPos` размытия будет указанным пиксельным значением; например, `100px` означает, что `YPos` составляет 100 пикселей. Значение по умолчанию: 0 px. |
| Width | String | No | Ширина размытия. Поддерживаются форматы % и px: Если строка заканчивается на %, то `Width` размытия будет указанным процентом ширины видео; например, `10%` означает, что `Width` составляет 10% ширины видео;Если строка заканчивается на px, то `Width` размытия будет в пикселях; например, `100px` означает, что `Width` составляет 100 пикселей. Значение по умолчанию: 10%. |
| Height | String | No | Высота размытия. Поддерживаются форматы % и px: Если строка заканчивается на %, то `Height` размытия будет указанным процентом высоты видео; например, `10%` означает, что `Height` составляет 10% высоты видео;Если строка заканчивается на px, то `Height` размытия будет в пикселях; например, `100px` означает, что `Height` составляет 100 пикселей. Значение по умолчанию: 10%. |
| StartTimeOffset | Float | No | Смещение времени начала размытия в секундах. Если этот параметр не заполнен или введено значение 0, размытие появится на первом кадре видео. Если этот параметр не заполнен или введено значение 0, размытие появится на первом кадре видео;Если это значение больше 0 (например, n), размытие появится на секунде n после первого кадра видео;Если это значение меньше 0 (например, -n), размытие появится на секунде n перед последним кадром видео. |
| EndTimeOffset | Float | No | Смещение времени окончания размытия в секундах. Если этот параметр не заполнен или введено значение 0, размытие будет существовать до последнего кадра видео;Если это значение больше 0 (например, n), размытие будет существовать до секунды n;Если это значение меньше 0 (например, -n), размытие будет существовать до секунды n перед последним кадром видео. |

## NumberFormat

Правило для переменной `{number}` в имени выходного файла.

Используется действиями: CreateWorkflow, ProcessMedia, ResetWorkflow.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| InitialValue | Integer | No | Начальное значение переменной `{number}`. Значение по умолчанию: 0. |
| Increment | Integer | No | Приращение переменной `{number}`. Значение по умолчанию: 1. |
| MinLength | Integer | No | Минимальная длина переменной `{number}`. Если длина переменной ниже минимального требования, будет использован заполнитель. Значение по умолчанию: 1. |
| PlaceHolder | String | No | Заполнитель, используемый, когда длина переменной `{number}` ниже минимального требования. Значение по умолчанию: 0. |

## OcrFullTextConfigureInfo

Параметр управления задачей полного распознавания текста

Используется действиями: CreateAIRecognitionTemplate, DescribeAIRecognitionTemplates.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Switch | String | Yes | Переключатель задачи полного распознавания текста. Допустимые значения: ON: включает задачу интеллектуального полного распознавания текста;OFF: отключает задачу интеллектуального полного распознавания текста. |

## OcrFullTextConfigureInfoForUpdate

Параметр управления задачей полного распознавания текста

Используется действием: ModifyAIRecognitionTemplate.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Switch | String | No | Переключатель задачи полного распознавания текста. Допустимые значения: ON: включает задачу интеллектуального полного распознавания текста;OFF: отключает задачу интеллектуального полного распознавания текста. |

## OcrWordsConfigureInfo

Параметр управления распознаванием текстового ключевого слова.

Используется действиями: CreateAIRecognitionTemplate, DescribeAIRecognitionTemplates.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Switch | String | Yes | Переключатель задачи распознавания текстового ключевого слова. Допустимые значения: ON: включает задачу распознавания текстового ключевого слова;OFF: отключает задачу распознавания текстового ключевого слова. |
| LabelSet | Array of String | No | Фильтр тегов ключевых слов, который указывает тег ключевого слова, который необходимо вернуть. Если этот параметр не заполнен, будут возвращены все результаты. Может быть до 10 тегов, каждый с ограничением длины 16 символов. |

## OcrWordsConfigureInfoForUpdate

Параметр управления распознаванием текстового ключевого слова.

Используется действием: ModifyAIRecognitionTemplate.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Switch | String | No | Переключатель задачи распознавания текстового ключевого слова. Допустимые значения: ON: включает задачу распознавания текстового ключевого слова;OFF: отключает задачу распознавания текстового ключевого слова. |
| LabelSet | Array of String | No | Фильтр тегов ключевых слов, который указывает тег ключевого слова, который необходимо вернуть. Если этот параметр не заполнен, будут возвращены все результаты. Может быть до 10 тегов, каждый с ограничением длины 16 символов. |

## OverrideEraseParameter

Пользовательские параметры для интеллектуального удаления.

Используется действием: ProcessMedia.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| EraseType | String | No | Тип удаления. -subtitle: удаление субтитров. -watermark: удаление водяного знака. -privacy: защита конфиденциальности. |
| EraseSubtitleConfig | [UpdateSmartEraseSubtitle

## PornAsrReviewTemplateInfo

Контрольный параметр задачи обнаружения информации о порнографии в речи

Используется действиями: CreateContentReviewTemplate, DescribeContentReviewTemplates.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Switch | String | Да | Переключатель задачи обнаружения информации о порнографии в речи. Допустимые значения: ON: включает задачу обнаружения информации о порнографии в речи;OFF: отключает задачу обнаружения информации о порнографии в речи. |
| BlockConfidence | Integer | Нет | Пороговый балл нарушения. Если этот балл достигнут или превышен во время интеллектуальной проверки, будет считаться, что произошло предполагаемое нарушение. Если этот параметр не указан, по умолчанию используется 100. Диапазон значений: 0-100. |
| ReviewConfidence | Integer | Нет | Пороговый балл для проверки человеком. Если этот балл достигнут или превышен во время интеллектуальной проверки, будет считаться необходимой проверка человеком. Если этот параметр не указан, по умолчанию используется 75. Диапазон значений: 0-100. |

## PornAsrReviewTemplateInfoForUpdate

Контрольный параметр задачи обнаружения информации о порнографии в речи.

Используется действиями: ModifyContentReviewTemplate.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Switch | String | Нет | Переключатель задачи обнаружения информации о порнографии в речи. Допустимые значения: ON: включает задачу обнаружения информации о порнографии в речи;OFF: отключает задачу обнаружения информации о порнографии в речи. |
| BlockConfidence | Integer | Нет | Пороговый балл нарушения. Если этот балл достигнут или превышен во время интеллектуальной проверки, будет считаться, что произошло предполагаемое нарушение. Диапазон значений: 0-100. |
| ReviewConfidence | Integer | Нет | Пороговый балл для проверки человеком. Если этот балл достигнут или превышен во время интеллектуальной проверки, будет считаться необходимой проверка человеком. Диапазон значений: 0-100. |

## PornConfigureInfo

Контрольный параметр задачи обнаружения информации о порнографии

Используется действиями: CreateContentReviewTemplate, DescribeContentReviewTemplates.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| ImgReviewInfo | [PornImgReviewTemplateInfo](#PornImgReviewTemplateInfo) | Нет | Контрольный параметр обнаружения информации о порнографии в изображении. Примечание: это поле может вернуть null, указывая, что допустимые значения не могут быть получены. |
| AsrReviewInfo | [PornAsrReviewTemplateInfo](#PornAsrReviewTemplateInfo) | Нет | Контрольный параметр обнаружения информации о порнографии в речи. Примечание: это поле может вернуть null, указывая, что допустимые значения не могут быть получены. |
| OcrReviewInfo | [PornOcrReviewTemplateInfo](#PornOcrReviewTemplateInfo) | Нет | Контрольный параметр обнаружения информации о порнографии в тексте. Примечание: это поле может вернуть null, указывая, что допустимые значения не могут быть получены. |

## PornConfigureInfoForUpdate

Контрольный параметр задачи обнаружения информации о порнографии.

Используется действиями: ModifyContentReviewTemplate.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| ImgReviewInfo | [PornImgReviewTemplateInfoForUpdate](#PornImgReviewTemplateInfoForUpdate) | Нет | Контрольный параметр обнаружения информации о порнографии в изображении. |
| AsrReviewInfo | [PornAsrReviewTemplateInfoForUpdate](#PornAsrReviewTemplateInfoForUpdate) | Нет | Контрольный параметр обнаружения информации о порнографии в речи. |
| OcrReviewInfo | [PornOcrReviewTemplateInfoForUpdate](#PornOcrReviewTemplateInfoForUpdate) | Нет | Контрольный параметр обнаружения информации о порнографии в тексте. |

## PornImgReviewTemplateInfo

Контрольный параметр задачи обнаружения информации о порнографии в изображении

Используется действиями: CreateContentReviewTemplate, DescribeContentReviewTemplates.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Switch | String | Да | Переключатель задачи обнаружения информации о порнографии в изображении. Допустимые значения: ON: включает задачу обнаружения информации о порнографии в изображении;OFF: отключает задачу обнаружения информации о порнографии в изображении. |
| LabelSet | Array of String | Нет | Фильтр тегов для обнаружения информации о порнографии в изображении. Если результат проверки содержит выбранный тег, он будет возвращен; если фильтр тегов пуст, будут возвращены все результаты проверки. Допустимые значения: porn: Порнография;vulgar: Вульгарность;intimacy: Интимность;sexy: Сексуальность. |
| BlockConfidence | Integer | Нет | Пороговый балл нарушения. Если этот балл достигнут или превышен во время интеллектуальной проверки, будет считаться, что произошло предполагаемое нарушение. Если этот параметр не указан, по умолчанию используется 90. Диапазон значений: 0-100. |
| ReviewConfidence | Integer | Нет | Пороговый балл для проверки человеком. Если этот балл достигнут или превышен во время интеллектуальной проверки, будет считаться необходимой проверка человеком. Если этот параметр не указан, по умолчанию используется 0. Диапазон значений: 0-100. |

## PornImgReviewTemplateInfoForUpdate

Контрольный параметр задачи обнаружения информации о порнографии в изображении.

Используется действиями: ModifyContentReviewTemplate.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Switch | String | Нет | Переключатель задачи обнаружения информации о порнографии в изображении. Допустимые значения: ON: включает задачу обнаружения информации о порнографии в изображении;OFF: отключает задачу обнаружения информации о порнографии в изображении. |
| LabelSet | Array of String | Нет | Фильтр тегов для обнаружения информации о порнографии в изображении. Если результат проверки содержит выбранный тег, он будет возвращен; если фильтр тегов пуст, будут возвращены все результаты проверки. Допустимые значения: porn: Порнография;vulgar: Вульгарность;intimacy: Интимность;sexy: Сексуальность. |
| BlockConfidence | Integer | Нет | Пороговый балл нарушения. Если этот балл достигнут или превышен во время интеллектуальной проверки, будет считаться, что произошло предполагаемое нарушение. Диапазон значений: 0-100. |
| ReviewConfidence | Integer | Нет | Пороговый балл для проверки человеком. Если этот балл достигнут или превышен во время интеллектуальной проверки, будет считаться необходимой проверка человеком. Диапазон значений: 0-100. |

## PornOcrReviewTemplateInfo

Контрольный параметр задачи обнаружения информации о порнографии в тексте

Используется действиями: CreateContentReviewTemplate, DescribeContentReviewTemplates.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Switch | String | Да | Переключатель задачи обнаружения информации о порнографии в тексте. Допустимые значения: ON: включает задачу обнаружения информации о порнографии в тексте;OFF: отключает задачу обнаружения информации о порнографии в тексте. |
| BlockConfidence | Integer | Нет | Пороговый балл нарушения. Если этот балл достигнут или превышен во время интеллектуальной проверки, будет считаться, что произошло предполагаемое нарушение. Если этот параметр не указан, по умолчанию используется 100. Диапазон значений: 0-100. |
| ReviewConfidence | Integer | Нет | Пороговый балл для проверки человеком. Если этот балл достигнут или превышен во время интеллектуальной проверки, будет считаться необходимой проверка человеком. Если этот параметр не указан, по умолчанию используется 75. Диапазон значений: 0-100. |

## PornOcrReviewTemplateInfoForUpdate

Контрольный параметр задачи обнаружения информации о порнографии в тексте.

Используется действиями: ModifyContentReviewTemplate.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Switch | String | Нет | Переключатель задачи обнаружения информации о порнографии в тексте. Допустимые значения: ON: включает задачу обнаружения информации о порнографии в тексте;OFF: отключает задачу обнаружения информации о порнографии в тексте. |
| BlockConfidence | Integer | Нет | Пороговый балл нарушения. Если этот балл достигнут или превышен во время интеллектуальной проверки, будет считаться, что произошло предполагаемое нарушение. Диапазон значений: 0-100. |
| ReviewConfidence | Integer | Нет | Пороговый балл для проверки человеком. Если этот балл достигнут или превышен во время интеллектуальной проверки, будет считаться необходимой проверка человеком. Диапазон значений: 0-100. |

## ProcessImageTemplate

Шаблон обработки изображения.

Используется действиями: DescribeProcessImageTemplates.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Уникальный идентификатор шаблона обработки изображения. |
| Name | String | Имя шаблона обработки изображения. |
| Comment | String | Информация об описании шаблона обработки изображения. |
| Type | String | Тип шаблона. |
| ProcessImageConfig | [ImageTaskInput](#ImageTaskInput) | Параметр конфигурации шаблона обработки изображения. |
| CreateTime | String | Время создания шаблона. |
| UpdateTime | String | Время последней модификации шаблона. |

## ProhibitedAsrReviewTemplateInfo

Контрольный параметр задачи обнаружения запрещенной информации в речи

Используется действиями: CreateContentReviewTemplate, DescribeContentReviewTemplates.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Switch | String | Да | Переключатель задачи обнаружения запрещенной информации в речи. Допустимые значения: ON: включает задачу обнаружения запрещенной информации в речи;OFF: отключает задачу обнаружения запрещенной информации в речи. |
| BlockConfidence | Integer | Нет | Пороговый балл нарушения. Если этот балл достигнут или превышен во время интеллектуальной проверки, будет считаться, что произошло предполагаемое нарушение. Если этот параметр не указан, по умолчанию используется 100. Диапазон значений: 0–100. |
| ReviewConfidence | Integer | Нет | Пороговый балл для проверки человеком. Если этот балл достигнут или превышен во время интеллектуальной проверки, будет считаться необходимой проверка человеком. Если этот параметр не указан, по умолчанию используется 75. Диапазон значений: 0–100. |

## ProhibitedAsrReviewTemplateInfoForUpdate

Контрольный параметр задачи обнаружения запрещенной информации в речи

Используется действиями: ModifyContentReviewTemplate.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Switch | String | Нет | Переключатель задачи обнаружения запрещенной информации в речи. Допустимые значения: ON: включает задачу обнаружения запрещенной информации в речи;OFF: отключает задачу обнаружения запрещенной информации в речи. |
| BlockConfidence | Integer | Нет | Пороговый балл нарушения. Если этот балл достигнут или превышен во время интеллектуальной проверки, будет считаться, что произошло предполагаемое нарушение. Если этот параметр не указан, по умолчанию используется 100. Диапазон значений: 0–100. |
| ReviewConfidence | Integer | Нет | Пороговый балл для проверки человеком. Если этот балл достигнут или превышен во время интеллектуальной проверки, будет считаться необходимой проверка человеком. Если этот параметр не указан, по умолчанию используется 75. Диапазон значений: 0–100. |

## ProhibitedConfigureInfo

Контрольный параметр задачи обнаружения запрещенной информации

Используется действиями: CreateContentReviewTemplate, DescribeContentReviewTemplates.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| AsrReviewInfo | [ProhibitedAsrReviewTemplateInfo](#ProhibitedAsrReviewTemplateInfo) | Нет | Контрольный параметр обнаружения запрещенной информации в речи. |
| OcrReviewInfo | [ProhibitedOcrReviewTemplateInfo](#ProhibitedOcrReviewTemplateInfo) | Нет | Контрольный параметр обнаружения запрещенной информации в тексте. |

## ProhibitedConfigureInfoForUpdate

Контрольный параметр задачи обнаружения запрещенной информации

Используется действиями: ModifyContentReviewTemplate.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| AsrReviewInfo | [ProhibitedAsrReviewTemplateInfoForUpdate](#ProhibitedAsrReviewTemplateInfoForUpdate) | Нет | Контрольный параметр обнаружения запрещенной информации в речи. |
| OcrReviewInfo | [ProhibitedOcrReviewTemplateInfoForUpdate](#ProhibitedOcrReviewTemplateInfoForUpdate) | Нет | Контрольный параметр обнаружения запрещенной информации в тексте. |

## ProhibitedOcrReviewTemplateInfo

Контрольный параметр задачи обнаружения запрещенной информации в тексте

Используется действиями: CreateContentReviewTemplate, DescribeContentReviewTemplates.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Switch | String | Да | Переключатель задачи обнаружения запрещенной информации в тексте. Допустимые значения: ON: включает задачу обнаружения запрещенной информации в тексте;OFF: отключает задачу обнаружения запрещенной информации в тексте. |
| BlockConfidence | Integer | Нет | Пороговый балл нарушения. Если этот балл достигнут или превышен во время интеллектуальной проверки, будет считаться, что произошло предполагаемое нарушение. Если этот параметр не указан, по умолчанию используется 100. Диапазон значений: 0–100. |
| ReviewConfidence | Integer | Нет | Пороговый балл для проверки человеком. Если этот балл достигнут или превышен во время интеллектуальной проверки, будет считаться необходимой проверка человеком. Если этот параметр не указан, по умолчанию используется 75. Диапазон значений: 0–100. |

## ProhibitedOcrReviewTemplateInfoForUpdate

Контрольный параметр задачи обнаружения запрещенной информации в тексте

Используется действиями: ModifyContentReviewTemplate.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Switch | String | Нет | Переключатель задачи обнаружения запрещенной информации в тексте. Допустимые значения: ON: включает задачу обнаружения запрещенной информации в тексте;OFF: отключает задачу обнаружения запрещенной информации в тексте. |
| BlockConfidence | Integer | Нет | Пороговый балл нарушения. Если этот балл достигнут или превышен во время интеллектуальной проверки, будет считаться, что произошло предполагаемое нарушение. Если этот параметр не указан, по умолчанию используется 100. Диапазон значений: 0–100. |
| ReviewConfidence | Integer | Нет | Пороговый балл для проверки человеком. Если этот балл достигнут или превышен во время интеллектуальной проверки, будет считаться необходимой проверка человеком. Если этот параметр не указан, по умолчанию используется 75. Диапазон значений: 0–100. |

## PureSubtitleTransResult

Результат перевода чистых файлов субтитров.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи (три допустимых значения следующие): - PROCESSING - SUCCESS  - FAIL |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает, что задача успешна, а другие значения указывают на сбой задачи. Допустимые значения см. в списке кодов ошибок Media Processing Service (MPS). |
| ErrCode | Integer | Код ошибки. 0 указывает, что задача успешна, а другие значения указывают на сбой. (Это поле не рекомендуется. Используйте новое поле кода ошибки ErrCodeExt.) |
| Message | String | Сообщение об ошибке |
| Input | [SmartSubtitleTaskResultInput](#SmartSubtitleTaskResultInput) | Информация о входных данных задачи перевода. |
| Output | [PureSubtitleTransResultOutput](#PureSubtitleTransResultOutput) | Результат вывода перевода чистых файлов субтитров. Примечание: это поле может вернуть null, указывая, что допустимые значения не могут быть получены. |
| Progress | Integer | Прогресс задачи. |

## PureSubtitleTransResultOutput

Подробный результат вывода перевода.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| OutputStorage | [TaskOutputStorage](#TaskOutputStorage) | Местоположение хранилища файла субтитров. Примечание: это поле может вернуть null, указывая, что допустимые значения не могут быть получены. |
| SubtitleResults | Array of [SubtitleTransResultItem](#SubtitleTransResultItem) | Результирующий набор многоязычного перевода. |

## QualityControlData

Выход результата проверки качества медиа.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| NoAudio | Boolean | Когда это поле установлено в true, это указывает, что видео не имеет аудиодорожки. |
| NoVideo | Boolean | Когда это поле установлено в true, это указывает, что видео не имеет видеодорожки. |
| QualityEvaluationScore | Integer | Оценка качества видео без ссылки (всего 100 баллов). |
| QualityEvaluationMeanOpinionScore | Float | Оценка качества видео без ссылки (MOS). |
| QualityControlResultSet | Array of [QualityControlResult](#QualityControlResult) | Элементы исключения, выявленные при проверке качества содержимого. |
| ContainerDiagnoseResultSet | Array of [ContainerDiagnoseResultItem](#ContainerDiagnoseResultItem) | Элементы исключения, выявленные при диагностике формата. |

## QualityControlItem

Информация о проверенном сегменте при контроле качества.

Используется действиями: ParseLiveStreamProcessNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Confidence | Integer | Оценка доверия. Диапазон значений: 0-100. Примечание: это поле может вернуть null, указывая, что допустимые значения не могут быть получены. |
| StartTimeOffset | Float | Начальная временная метка (в секундах) сегмента. |
| EndTimeOffset | Float | Конечная временная метка (в секундах) сегмента. |
| AreaCoordSet | Array of Integer | Координаты (пиксели) верхнего левого и нижнего правого углов. Примечание: это поле может вернуть null, указывая, что допустимые значения не могут быть получены. |

## QualityControlItemConfig

Конфигурации элемента проверки качества.

Используется действиями: CreateQualityControlTemplate, DescribeQualityControlTemplates, ModifyQualityControlTemplate.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Type | String | Да | Имя элемента проверки качества. допустимые значения:. LowEvaluation: указывает оценку видео без ссылки MOS.. AudioEvaluation: указывает оценку аудио без ссылки MOS.. Mosaic: обнаружение мозаики.. CrashScreen: указывает обнаружение глюка экрана.. Blur: указывает обнаружение размытия.. Jitter: обнаружение дрожания.. Noise: обнаружение шума.. QRCode: обнаружение qr кода.. BarCode: указывает обнаружение штрих-кода.. AppletCode: указывает обнаружение кода мини-приложения.. BlackWhiteEdge: указывает обнаружение черной и белой кромки.. SolidColorScreen: указывает обнаружение однотонного экрана.. LowLighting: указывает низкое освещение.. HighLighting: переэкспонирование.. NoVoice: указывает обнаружение тишины.. LowVoice: указывает обнаружение баса.. HighVoice: обнаружение взрывного шума.. AudioNoise: указывает обнаружение шума в аудио.. VideoResolutionChanged: указывает изменение разрешения видео.. AudioSampleRateChanged: указывает изменение частоты дискретизации аудио.. AudioChannelsChanged: указывает изменение количества каналов аудио.. ParameterSetsChanged: указывает, что информация о наборе параметров потока изменилась.. DarOrSarInvalid: указывает на аномальное соотношение сторон видео.. TimestampFallback: указывает откат временной метки DTS.. DtsJitter: указывает на чрезмерное дрожание DTS.. PtsJitter: указывает на чрезмерное дрожание PTS.. AACDurationDeviation: указывает на неправильный интервал временной метки кадра aac.. AudioDroppingFrames: указывает на потерю аудиокадров.. VideoDroppingFrames: указывает на потерю видеокадров.. AVTimestampInterleave: неправильное чередование аудио-видео.. PtsLessThanDts: указывает, что pts потока медиа меньше, чем dts.. ReceiveFpsJitter: указывает на чрезмерное дрожание частоты кадров, полученной из сети.. ReceiveFpsTooSmall: указывает, что частота кадров видео, полученная из сети, слишком низкая.. FpsJitter: указывает на чрезмерное дрожание частоты кадров потока, рассчитанной через PTS.. StreamOpenFailed: указывает на неудачу открытия потока.. StreamEnd: указывает на конец потока.. StreamParseFailed: указывает на неудачу анализа потока.. VideoFirstFrameNotIdr: первый кадр не является IDR кадром.. StreamNALUError: указывает на ошибку кода начала nalu.. TsStreamNoAud: указывает, пропускает ли поток H26x MPEG-TS AUD NALU.. AudioStreamLack: нет аудиопотока.. VideoStreamLack: нет видеопотока.. LackAudioRecover: указывает на восстановление отсутствующего аудиопотока.. LackVideoRecover: восстановление отсутствующего видеопотока.. VideoBitrateOutofRange: битрейт видеопотока (кбит/с) выходит за пределы диапазона.. AudioBitrateOutofRange: битрейт аудиопотока (кбит/с) выходит за пределы диапазона.. VideoDecodeFailed: указывает на ошибку декодирования видео.. AudioDecodeFailed: ошибка декодирования аудио.. AudioOutOfPhase: указывает на противоположную фазу в двухканальном аудио.. VideoDuplicatedFrame: указывает на наличие дублирующихся кадров в видеопотоках.. AudioDuplicatedFrame: указывает на наличие дублирующихся кадров в аудиопотоках.. VideoRotation: указывает на поворот видео.. TsMultiPrograms: указывает на наличие нескольких программ в потоках MPEG2-TS.. Mp4InvalidCodecFourcc: указывает, что fourcc кодека в Mp4 не соответствует требованиям Apple HLS.. HLSBadM3u8Format: неверный формат файла m3u8.. HLSInvalidMasterM3u8: неверный основной файл m3u8.. HLSInvalidMediaM3u8: неверный файл m3u8 медиа.. HLSMasterM3u8Recommended: параметры, рекомендуемые стандартами, отсутствуют в основном файле m3u8.. HLSMediaM3u8Recommended: параметры, рекомендуемые стандартами, отсутствуют в файле m3u8 медиа.. HLSMediaM3u8DiscontinuityExist: указывает на наличие EXT-X-DISCONTINUITY в файле m3u8 медиа.. HLSMediaSegmentsStreamNumChange: указывает на изменение количества потоков в сегментах.. HLSMediaSegmentsPTSJitterDeviation: указывает на скачки PTS между сегментами без EXT-X-DISCONTINUITY.. HLSMediaSegmentsDTSJitterDeviation: указывает на скачки DTS между сегментами без EXT-X-DISCONTINUITY.. TimecodeTrackExist: TMCD дорожка в MP4. |
| Switch | String |

## RawTranscodeParameter

Спецификации для пользовательского перекодирования

Используется действиями: CreateWorkflow, ProcessMedia, ResetWorkflow.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Container | String | Да | Контейнер. Допустимые значения: mp4; flv; hls; mp3; flac; ogg; m4a. Из них mp3, flac, ogg и m4a предназначены для аудиофайлов. |
| RemoveVideo | Integer | Нет | Удалять ли видеоданные. Допустимые значения: 0: сохранять; 1: удалять. Значение по умолчанию: 0. |
| RemoveAudio | Integer | Нет | Удалять ли аудиоданные. Допустимые значения: 0: сохранять; 1: удалять. Значение по умолчанию: 0. |
| VideoTemplate | [VideoTemplateInfo](#VideoTemplateInfo) | Нет | Параметр конфигурации видеопотока. Это поле требуется, когда `RemoveVideo` равно 0. |
| AudioTemplate | [AudioTemplateInfo](#AudioTemplateInfo) | Нет | Параметр конфигурации аудиопотока. Это поле требуется, когда `RemoveAudio` равно 0. |
| TEHDConfig | [TEHDConfig](#TEHDConfig) | Нет | Параметр перекодирования TESHD. |
| StdExtInfo | String | Нет | Дополнительный параметр, представляющий собой сериализованную строку JSON. |
| EnhanceConfig | [EnhanceConfig](#EnhanceConfig) | Нет | Конфигурация улучшения аудио/видео. Примечание: это поле может возвращать null, что указывает на отсутствие допустимого значения. |
| SubtitleTemplate | [SubtitleTemplate](#SubtitleTemplate) | Нет | Параметр субтитров. Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |

## RawWatermarkParameter

Спецификации пользовательского водяного знака.

Используется действиями: CreateWorkflow, ProcessMedia, ResetWorkflow.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Type | String | Да | Тип водяного знака. Допустимые значения: image: водяной знак с изображением. |
| CoordinateOrigin | String | Нет | Исходная позиция. Допустимые значения:. TopLeft: указывает, что исходная точка координат находится в верхнем левом углу видеоизображения, а исходная точка водяного знака находится в верхнем левом углу изображения или текста.. TopRight: указывает, что исходная точка координат находится в верхнем правом углу видеоизображения, а исходная точка водяного знака находится в верхнем правом углу изображения или текста.. BottomLeft: указывает, что исходная точка координат находится в нижнем левом углу видеоизображения, а исходная точка водяного знака находится в нижнем левом углу изображения или текста.. BottomRight: указывает, что исходная точка координат находится в нижнем правом углу видеоизображения, а исходная точка водяного знака находится в нижнем правом углу изображения или текста.  Значение по умолчанию: TopLeft. |
| XPos | String | Нет | Горизонтальная позиция исходной точки водяного знака относительно исходной точки координат видео. Поддерживаются форматы % и px: Если строка заканчивается на %, `XPos` водяного знака будет составлять указанный процент от ширины видео; например, `10%` означает, что `XPos` составляет 10% ширины видео; Если строка заканчивается на px, `XPos` водяного знака будет составлять указанный размер в px; например, `100px` означает, что `XPos` составляет 100 px. Значение по умолчанию: 0 px. |
| YPos | String | Нет | Вертикальная позиция исходной точки водяного знака относительно исходной точки координат видео. Поддерживаются форматы % и px: Если строка заканчивается на %, `YPos` водяного знака будет составлять указанный процент от высоты видео; например, `10%` означает, что `YPos` составляет 10% высоты видео; Если строка заканчивается на px, `YPos` водяного знака будет составлять указанный размер в px; например, `100px` означает, что `YPos` составляет 100 px. Значение по умолчанию: 0 px. |
| ImageTemplate | [RawImageWatermarkInput](#RawImageWatermarkInput) | Нет | Шаблон водяного знака с изображением. Это поле требуется, когда `Type` равно `image` и недействительно, когда `Type` равно `text`. |

## RecognizeAudioSentence

Результат распознавания предложения.

Используется действиями: RecognizeAudio.

| Имя | Тип | Описание |
| --- | --- | --- |
| Start | Float | Время начала в аудио, в секундах. |
| End | Float | Время окончания в аудио, в секундах. |
| Text | String | Результат распознавания аудио. |
| WordsInfo | Array of [WordResult](#WordResult) | Результат временных меток слов. |

## RuleConditionItem

Конфигурация условия правила.

Используется действиями: CreateSchedule, ModifySchedule.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Key | String | Нет | Ключ условия элемента проверки качества. |
| Value | String | Нет | Значение, соответствующее условию. |

## Rules

Условия определения задачи.

Используется действиями: CreateSchedule, ModifySchedule.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Id | String | Нет | ID условия определения. Примечание: это поле может возвращать null, что указывает на отсутствие допустимого значения. |
| Conditions | Array of [RuleConditionItem](#RuleConditionItem) | Нет | Конфигурация условия определения. Примечание: это поле может возвращать null, что указывает на отсутствие допустимого значения. |
| Linker | String | Нет | Логический оператор для списка условий. Допустимые значения:   - &&: логическое И  - \|\|: логическое ИЛИ |
| RearDriveIndexs | Array of Integer | Нет | Индексы узлов для выполнения при выполнении условий определения. Примечание: это поле может возвращать null, что указывает на отсутствие допустимого значения. |

## S3InputInfo

Информация о хранилище AWS S3 исходного файла.

Используется действиями: BatchProcessMedia, DescribeMediaMetaData, ExtractBlindWatermark, ProcessImage, ProcessMedia.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| S3Bucket | String | Да | Бакет AWS S3. |
| S3Region | String | Да | Регион бакета AWS S3. |
| S3Object | String | Да | Путь объекта AWS S3. |
| S3SecretId | String | Нет | ID ключа, необходимый для доступа к объекту AWS S3. |
| S3SecretKey | String | Нет | Ключ, необходимый для доступа к объекту AWS S3. |

## S3OutputStorage

Информация о хранилище AWS S3 выходного файла.

Используется действиями: BatchProcessMedia, CreateSchedule, CreateWorkflow, EditMedia, ModifySchedule, ProcessImage, ProcessLiveStream, ProcessMedia, ResetWorkflow.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| S3Bucket | String | Да | Бакет AWS S3. |
| S3Region | String | Да | Регион бакета AWS S3. |
| S3SecretId | String | Нет | ID ключа, необходимый для загрузки файлов в объект AWS S3. |
| S3SecretKey | String | Нет | Ключ, необходимый для загрузки файлов в объект AWS S3. |

## SampleSnapshotTaskInput

Тип входного параметра задачи выборочного снимка экрана.

Используется действиями: CreateSchedule, CreateWorkflow, DescribeTaskDetail, ModifySchedule, ParseNotification, ProcessMedia, ResetWorkflow.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Definition | Integer | Да | ID шаблона выборочного снимка экрана. |
| WatermarkSet | Array of [WatermarkInput](#WatermarkInput) | Нет | Список до 10 водяных знаков с изображением или текстом. Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| OutputStorage | [TaskOutputStorage](#TaskOutputStorage) | Нет | Целевой бакет для выборочного снимка экрана. Если этот параметр не заполнен, будет унаследовано значение `OutputStorage` родительской папки. Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| OutputObjectPath | String | Нет | Путь вывода файла изображения после создания выборочного снимка экрана, который может быть относительным или абсолютным путем. Если необходимо определить путь вывода, путь должен заканчиваться на `.{format}`. Для имен переменных см. [Переменная имени файла](https://intl.cloud.tencent.com/document/product/862/37039?from_cn_redirect=1).Пример относительного пути: Filename_{Variable name}.{format}.Filename.{format}. Пример абсолютного пути: /Custom path/Filename_{Variable name}.{format}. Если не заполнено, по умолчанию используется относительный путь: `{inputName}_sampleSnapshot_{definition}_{number}.{format}`. |
| ObjectNumberFormat | [NumberFormat](#NumberFormat) | Нет | Правило переменной `{number}` в пути вывода выборочного снимка экрана. Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |

## SampleSnapshotTemplate

Сведения о шаблоне выборочного снимка экрана

Используется действиями: DescribeSampleSnapshotTemplates.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Уникальный ID шаблона выборочного снимка экрана. |
| Type | String | Тип шаблона. Допустимые значения: Preset: предустановленный шаблон; Custom: пользовательский шаблон. |
| Name | String | Имя шаблона выборочного снимка экрана. |
| Comment | String | Описание шаблона. |
| Width | Integer | Максимальное значение ширины (или длинной стороны) снимка экрана в px. Диапазон значений: 0 и [128, 4096]. Если оба `Width` и `Height` равны 0, разрешение будет совпадать с разрешением исходного видео; Если `Width` равен 0, но `Height` не равен 0, `Width` будет масштабирован пропорционально; Если `Width` не равен 0, но `Height` равен 0, `Height` будет масштабирован пропорционально; Если оба `Width` и `Height` не равны 0, будет использовано пользовательское разрешение. Значение по умолчанию: 0. |
| Height | Integer | Максимальное значение высоты (или короткой стороны) снимка экрана в px. Диапазон значений: 0 и [128, 4096]. Если оба `Width` и `Height` равны 0, разрешение будет совпадать с разрешением исходного видео; Если `Width` равен 0, но `Height` не равен 0, `Width` будет масштабирован пропорционально; Если `Width` не равен 0, но `Height` равен 0, `Height` будет масштабирован пропорционально; Если оба `Width` и `Height` не равны 0, будет использовано пользовательское разрешение. Значение по умолчанию: 0. |
| ResolutionAdaptive | String | Адаптация разрешения. Допустимые значения: open: включено. В этом случае `Width` представляет длинную сторону видео, а `Height` — короткую сторону; close: отключено. В этом случае `Width` представляет ширину видео, а `Height` — высоту. Значение по умолчанию: open. |
| Format | String | Формат изображения. |
| SampleType | String | Тип выборочного снимка экрана. |
| SampleInterval | Integer | Интервал выборки. |
| CreateTime | String | Время создания шаблона в [формате даты ISO](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |
| UpdateTime | String | Время последнего изменения шаблона в [формате даты ISO](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |
| FillType | String | Тип заполнения. "Fill" (заполнение) относится к способу обработки снимка экрана, когда его соотношение сторон отличается от соотношения сторон исходного видео. Поддерживаются следующие типы заполнения:  stretch: растянуть. Снимок экрана будет растянут кадр за кадром, чтобы совпадать с соотношением сторон исходного видео, что может сделать снимок экрана "короче" или "длиннее"; black: заполнить черным. Эта опция сохраняет соотношение сторон исходного видео для снимка экрана и заполняет несовместимую область черными блоками.; white: заполнить белым. Эта опция сохраняет соотношение сторон исходного видео для снимка экрана и заполняет несовместимую область белыми блоками.; gauss: заполнить размытием Гаусса. Эта опция сохраняет соотношение сторон исходного видео для снимка экрана и заполняет несовместимую область размытием Гаусса. Значение по умолчанию: black. |

## ScheduleAnalysisTaskResult

Результат задачи анализа содержимого схемы.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: PROCESSING, SUCCESS, FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи; любое другое возвращаемое значение указывает на сбой задачи. Подробнее см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1041/40249). |
| ErrCode | Integer | Код ошибки. 0 указывает на успешное выполнение задачи; другие значения указывают на сбой задачи. Этот параметр не рекомендуется. Используйте вместо него `ErrCodeExt`. |
| Message | String | Сообщение об ошибке. |
| Input | [AiAnalysisTaskInput](#AiAnalysisTaskInput) | Ввод задачи анализа содержимого. |
| Output | Array of [AiAnalysisResult](#AiAnalysisResult) | Вывод задачи анализа. |
| BeginProcessTime | String | Время начала выполнения задачи в формате даты и времени ISO. |
| FinishTime | String | Время завершения выполнения задачи в формате даты и времени ISO. |

## ScheduleExecRuleTaskResult

Тип результата задачи проверки качества медиа.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи, может быть PROCESSING, SUCCESS или FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение, другие значения указывают на сбой. Конкретные значения см. в списке кодов ошибок MPS на https://www.tencentcloud.comom/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81. |
| Message | String | Сообщение об ошибке. |
| Input | [ExecRulesTask](#ExecRulesTask) | Ввод задачи условного определения. |
| Output | [ExecRuleTaskData](#ExecRuleTaskData) | Вывод задачи условного определения. Примечание: это поле может возвращать null, что указывает на отсутствие допустимого значения. |

## ScheduleQualityControlTaskResult

Тип результата задачи проверки качества медиа.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: `PROCESSING`, `SUCCESS`, `FAIL`. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи; любое другое значение указывает на сбой задачи. Подробнее см. [Коды ошибок](https://www.tencentcloud.com/document/product/1041/40249). |
| ErrCode | Integer | Код ошибки. `0` указывает на успешное выполнение задачи; другие значения указывают на сбой задачи. Этот параметр не рекомендуется. Используйте вместо него `ErrCodeExt`. |
| Message | String | Сообщение об ошибке. |
| Input | [AiQualityControlTaskInput](#AiQualityControlTaskInput) | Ввод задачи проверки качества медиа. |
| Output | [QualityControlData](#QualityControlData) | Вывод задачи проверки качества медиа. Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| Progress | Integer | Прогресс выполнения задачи. |

## ScheduleRecognitionTaskResult

Результат задачи распознавания содержимого схемы.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: PROCESSING, SUCCESS, FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи; любое другое возвращаемое значение указывает на сбой задачи. Подробнее см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1041/40249). |
| ErrCode | Integer | Код ошибки. 0 указывает на успешное выполнение задачи; другие значения указывают на сбой задачи. Этот параметр не рекомендуется. Используйте вместо него `ErrCodeExt`. |
| Message | String | Сообщение об ошибке. |
| Input | [AiRecognitionTaskInput](#AiRecognitionTaskInput) | Ввод задачи распознавания содержимого. |
| Output | Array of [AiRecognitionResult](#AiRecognitionResult) | Вывод задачи идентификации. |
| BeginProcessTime | String | Время начала выполнения задачи в [формате даты и времени ISO](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52). |
| FinishTime | String | Время завершения выполнения задачи в [формате даты и времени ISO](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52). |

## ScheduleReviewTaskResult

Результат задачи модерации содержимого схемы.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи. Допустимые значения: PROCESSING, SUCCESS, FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи; любое другое возвращаемое значение указывает на сбой задачи. Подробнее см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/1041/40249). |
| ErrCode | Integer | Код ошибки. 0 указывает на успешное выполнение задачи; другие значения указывают на сбой задачи. Этот параметр не рекомендуется. Используйте вместо него `ErrCodeExt`. |
| Message | String | Сообщение об ошибке. |
| Input | [AiContentReviewTaskInput](#AiContentReviewTaskInput) | Ввод задачи модерации содержимого. |
| Output | Array of [AiContentReviewResult](#AiContentReviewResult) | Вывод задачи модерации содержимого. Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |

## ScheduleSmartSubtitleTaskResult

Результат задачи планирования интеллектуальных субтитров.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи, включая PROCESSING, SUCCESS и FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на то, что задача успешна, другие значения указывают на то, что задача не удалась. Конкретные значения см. [Коды ошибок](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81). |
| ErrCode | Integer | Код ошибки. 0 указывает на то, что задача успешна, другие значения указывают на то, что задача не удалась. (Этот параметр не рекомендуется. Используйте вместо него новое поле кода ошибки ErrCodeExt.) |
| Message | String | Сообщение об ошибке. |
| Input | [SmartSubtitlesTaskInput](#SmartSubtitlesTaskInput) | Ввод задачи распознавания. |
| Output | Array of [SmartSubtitlesResult](#SmartSubtitlesResult) | Вывод задачи идентификации. |
| BeginProcessTime | String | Время начала выполнения задачи в [формате даты и времени ISO](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52). |
| FinishTime | String | Время завершения выполнения задачи в [формате даты и времени ISO](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52). |

## ScheduleTask

Информация о схеме.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| TaskId | String | ID схемы. |
| Status | String | Статус схемы. Допустимые значения: PROCESSINGFINISH |
| ErrCode | Integer | Если возвращаемое значение не равно 0, была ошибка источника. Если возвращается 0, обратитесь к кодам ошибок соответствующего типа задачи. |
| Message | String | Если была ошибка источника, этот параметр является сообщением об ошибке. Для других ошибок обратитесь к сообщениям об ошибках соответствующего типа задачи. |
| InputInfo | [MediaInputInfo](#MediaInputInfo) | Информация об обработанном файле. Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| MetaData | [MediaMetaData](#MediaMetaData) | Метаданные исходного видео. Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| ActivityResultSet | Array of [ActivityResult](#ActivityResult) | Вывод схемы. Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |

## SchedulesInfo

Сведения о схеме.

Используется действиями: DescribeSchedules.

| Имя | Тип | Описание |
| --- | --- | --- |
| ScheduleId | Integer | ID схемы. |
| ScheduleName | String | Имя схемы. Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| Type | String | Тип схемы. Допустимые значения:  `Preset` `Custom`  Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| Status | String | Статус схемы. Допустимые значения: `Enabled` `Disabled` Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| Trigger | [WorkflowTrigger](#WorkflowTrigger) | Триггер схемы. Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| Activities | Array of [Activity](#Activity) | Подзадачи схемы. Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| OutputStorage | [TaskOutputStorage](#TaskOutputStorage) | Бакет для сохранения выходного файла. Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| OutputDir | String | Каталог для сохранения выходного файла. Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| TaskNotifyConfig | [TaskNotifyConfig](#TaskNotifyConfig) | Конфигурация уведомления. Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| CreateTime | String | Время создания в [формате даты ISO](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52). Примечание: это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| UpdateTime | String | Время последнего обновления в [формате даты ISO](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52). Примечание: это поле может возвращать null, что указывает

## SmartEraseTaskInput

Задача интеллектуального стирания.

Используется действиями: CreateSchedule, DescribeTaskDetail, ModifySchedule, ParseNotification, ProcessMedia.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Definition | Integer | Нет | ID шаблона интеллектуального стирания. |
| RawParameter | [RawSmartEraseParameter](#RawSmartEraseParameter) | Нет | Пользовательский параметр интеллектуального стирания. Действует, если Definition установлен на 0. Этот параметр используется для высоко настраиваемых сценариев. Рекомендуется в приоритетном порядке использовать Definition для указания параметров интеллектуального стирания. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |
| OverrideParameter | [OverrideEraseParameter](#OverrideEraseParameter) | Нет | Пользовательские параметры для интеллектуального стирания. Если значение Definition не равно 0, этот параметр действителен. Когда в этой структуре указаны определенные параметры стирания, указанные параметры будут использоваться для переопределения параметров в шаблоне интеллектуального стирания. Этот параметр используется в высоко настраиваемых сценариях. Рекомендуется использовать только Definition для указания параметров интеллектуального стирания. |
| OutputStorage | [TaskOutputStorage](#TaskOutputStorage) | Нет | Указывает целевое хранилище для файлов. Если оставить пусто, наследует значение OutputStorage верхнего уровня. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |
| OutputObjectPath | String | Нет | Путь вывода файла, который может быть относительным или абсолютным. Путь вывода должен заканчиваться на `.{format}`. Для переменных имена см. [объяснение переменных имени файла](https://www.tencentcloud.com/document/product/1041/33495?has_map=1). **Пример относительного пути**: Filename_{Variable name}.{format}Filename.{format}  **Пример абсолютного пути**: /Custom path/filename_{variable name}.{format}  **Примечание**: в настоящее время не поддерживается API `BatchProcessMedia`. |

## SmartEraseTaskResult

Результат задачи интеллектуального стирания.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи, включая PROCESSING, SUCCESS и FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи, другие значения указывают на сбой задачи. Конкретные значения см. в разделе [Коды ошибок](https://www.tencentcloud.comom/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81). |
| Message | String | Сообщение об ошибке. |
| Input | [SmartEraseTaskInput](#SmartEraseTaskInput) | Входные данные задачи интеллектуального стирания. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |
| Output | [AiAnalysisTaskDelLogoOutput](#AiAnalysisTaskDelLogoOutput) | Результат задачи интеллектуального стирания. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |
| Progress | Integer | Ход выполнения задачи. |
| BeginProcessTime | String | Время начала выполнения задачи в формате ISO datetime. |
| FinishTime | String | Время завершения выполнения задачи в формате ISO datetime. |

## SmartEraseTemplateItem

Детали шаблона интеллектуального стирания.

Используется действиями: DescribeSmartEraseTemplates.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Уникальный идентификатор шаблона интеллектуального стирания. |
| Name | String | Имя шаблона интеллектуального стирания. |
| Comment | String | Описание информации шаблона интеллектуального стирания. |
| Type | String | Тип шаблона. Допустимые значения: * Preset: системный предустановленный шаблон. * Custom: определяемый пользователем шаблон. |
| EraseType | String | Тип стирания. -subtitle: удаление субтитров. -watermark: удаление водяного знака. -privacy: защита конфиденциальности. |
| EraseSubtitleConfig | [SmartEraseSubtitleConfig](#SmartEraseSubtitleConfig) | Конфигурация удаления субтитров. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| EraseWatermarkConfig | [SmartEraseWatermarkConfig](#SmartEraseWatermarkConfig) | Конфигурация удаления водяного знака. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| ErasePrivacyConfig | [SmartErasePrivacyConfig](#SmartErasePrivacyConfig) | Конфигурация защиты конфиденциальности. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| CreateTime | String | Время создания шаблона в [формате ISO datetime](https://www.tencentcloud.comom/document/product/862/37710?from_cn_redirect=1#52). |
| UpdateTime | String | Время последнего изменения шаблона в [формате ISO datetime](https://www.tencentcloud.comom/document/product/862/37710?from_cn_redirect=1#52). |
| AliasName | String | Псевдоним предустановленного шаблона интеллектуального стирания. |

## SmartEraseWatermarkConfig

Конфигурация водяного знака в шаблоне интеллектуального стирания.

Используется действиями: CreateSmartEraseTemplate, DescribeSmartEraseTemplates, ModifySmartEraseTemplate, ProcessMedia.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| WatermarkEraseMethod | String | Да | Указывает метод удаления водяного знака. **Автоматическое удаление:** автоматически идентифицирует водяные знаки в видео, используя модель a, и создает новое видео после удаления. подходит для динамических водяных знаков. При использовании автоматического удаления, если не указать AutoAreas, весь экран видео будет стирается автоматически. если указано AutoAreas, оно перейдет к стиранию назначенных областей. **Стирание указанной области:** для статических водяных знаков с фиксированными местоположениями рекомендуется прямо указать область стирания. Когда вы выбираете стирание указанной области, импортируйте по крайней мере одну указанную область.  -Автоматическое удаление. -Указывает пользовательское стирание указанной области. |
| WatermarkModel | String | Да | Указывает модель удаления водяного знака. Базовая версия: среднее качество, экономичная, подходит для видео с чистыми фонами или анимацией. Расширенная версия: лучшее качество, подходит для мини-драм и видео в стиле реальности. **Поддерживаемые значения**: - basic - advanced |
| AutoAreas | Array of [EraseArea](#EraseArea) | Нет | Автоматическое стирание пользовательской области. Автоматически обнаруживает и стирает целевое удаление в указанной области с помощью модели AI. Обратите внимание, что этот параметр не будет действовать, когда метод удаления является пользовательским. Для изменения шаблона введите [] для области очистки. Если не указано, информация о регионе шаблона останется неизменной. |
| CustomAreas | Array of [EraseTimeArea](#EraseTimeArea) | Нет | Указывает удаление пользовательской области. Указывает выполнять удаление непосредственно без обнаружения и распознавания в пределах выбранного диапазона времени для указанной области. Примечание: при изменении шаблона передайте [] для очистки области. если информация о регионе шаблона не передана, она остается неизменной. |

## SmartSubtitleTaskAsrFullTextResult

Результат полного распознавания речи.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи, включая PROCESSING, SUCCESS и FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи, другие значения указывают на сбой задачи. Конкретные значения см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81). |
| ErrCode | Integer | Код ошибки. 0 указывает на успешное выполнение задачи, другие значения указывают на сбой. (Это поле не рекомендуется использовать. Используйте новое поле кода ошибки ErrCodeExt.) |
| Message | String | Сообщение об ошибке. |
| Input | [SmartSubtitleTaskResultInput](#SmartSubtitleTaskResultInput) | Входная информация по задаче полного распознавания речи. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |
| Output | [SmartSubtitleTaskAsrFullTextResultOutput](#SmartSubtitleTaskAsrFullTextResultOutput) | Выходная информация по задаче полного распознавания речи. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |
| Progress | Integer | Ход выполнения задачи. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |

## SmartSubtitleTaskAsrFullTextResultOutput

Результат полного распознавания речи.

Используется действиями: DescribeBatchTaskDetail, DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| SegmentSet | Array of [SmartSubtitleTaskAsrFullTextSegmentItem](#SmartSubtitleTaskAsrFullTextSegmentItem) | Список сегментов для полного распознавания речи. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |
| Path | String | Путь файла субтитров. |
| SubtitlePath | String | Путь файла субтитров. |
| OutputStorage | [TaskOutputStorage](#TaskOutputStorage) | Место хранения файла субтитров. |

## SmartSubtitleTaskAsrFullTextSegmentItem

Сегмент, прошедший полное распознавание речи.

Используется действиями: DescribeBatchTaskDetail, DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Confidence | Float | Уверенность распознанного сегмента. Диапазон значений: 0-100. |
| StartTimeOffset | Float | Начальное смещение времени распознанного сегмента в секундах. |
| EndTimeOffset | Float | Конечное смещение времени распознанного сегмента в секундах. |
| Text | String | Распознанный текст. |
| Wordlist | Array of [WordResult](#WordResult) | Информация о временных метках слова.  Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |
| SpeakerId | String | ID говорящего (если включено распознавание говорящего). |

## SmartSubtitleTaskBatchOutput

Выходная информация для задач интеллектуальных субтитров.

Используется действиями: DescribeBatchTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Progress | Integer | Ход выполнения задачи. |
| Status | String | Статус задачи, включая PROCESSING, SUCCESS и FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи, другие значения указывают на сбой задачи. Конкретные значения см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81). |
| Message | String | Сообщение об ошибке. |
| TransTextTask | [SmartSubtitleTaskTransTextResultOutput](#SmartSubtitleTaskTransTextResultOutput) | Выходная информация задачи перевода. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |
| AsrFullTextTask | [SmartSubtitleTaskAsrFullTextResultOutput](#SmartSubtitleTaskAsrFullTextResultOutput) | Выходная информация по задаче полного распознавания речи. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |

## SmartSubtitleTaskFullTextResult

Результат полнотекстового распознавания для задач интеллектуальных субтитров.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи, который может быть PROCESSING, SUCCESS или FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи, другие значения указывают на сбой. Допустимые значения см. в списке [кодов ошибок MPS](https://www.tencentcloud.comom/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81). |
| ErrCode | Integer | Код ошибки. 0 указывает на успешное выполнение задачи, другие значения указывают на сбой. (Это поле не рекомендуется использовать. Используйте новое поле кода ошибки ErrCodeExt.) |
| Message | String | Сообщение об ошибке. |
| Input | [SmartSubtitleTaskResultInput](#SmartSubtitleTaskResultInput) | Входная информация для задач интеллектуальных субтитров. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| Output | [SmartSubtitleTaskTextResultOutput](#SmartSubtitleTaskTextResultOutput) | Выходная информация для задач интеллектуальных субтитров. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| Progress | Integer | Ход выполнения задачи. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимых значений. |

## SmartSubtitleTaskResultInput

Входные данные для перевода интеллектуальных субтитров.

Используется действиями: DescribeBatchTaskDetail, DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | ID шаблона интеллектуальных субтитров. |
| RawParameter | [RawSmartSubtitleParameter](#RawSmartSubtitleParameter) | Пользовательский параметр интеллектуальных субтитров. Действует, когда Definition установлен на 0. Этот параметр используется в высоко настраиваемых сценариях. Рекомендуется в приоритетном порядке использовать Definition для указания параметров интеллектуальных субтитров. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |

## SmartSubtitleTaskTextResultOutput

Результат распознавания интеллектуальных субтитров.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| RecognizeSubtitleResult | Array of [SubtitleResult](#SubtitleResult) | Результат распознавания субтитров. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| TransSubtitleResult | Array of [SubtitleResult](#SubtitleResult) | Результат перевода субтитров. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| OutputStorage | [TaskOutputStorage](#TaskOutputStorage) | Место хранения файла субтитров. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимых значений. |

## SmartSubtitleTaskTransTextResult

Результат перевода.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Status | String | Статус задачи, включая PROCESSING, SUCCESS и FAIL. |
| ErrCodeExt | String | Код ошибки. Пустая строка указывает на успешное выполнение задачи, другие значения указывают на сбой задачи. Конкретные значения см. в разделе [Коды ошибок](https://intl.cloud.tencent.com/document/product/862/50369?from_cn_redirect=1#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81). |
| ErrCode | Integer | Код ошибки. 0 указывает на успешное выполнение задачи, другие значения указывают на сбой. (Это поле не рекомендуется использовать. Используйте новое поле кода ошибки ErrCodeExt.) |
| Message | String | Сообщение об ошибке. |
| Input | [SmartSubtitleTaskResultInput](#SmartSubtitleTaskResultInput) | Входная информация задачи перевода. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |
| Output | [SmartSubtitleTaskTransTextResultOutput](#SmartSubtitleTaskTransTextResultOutput) | Выходная информация задачи перевода. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |
| Progress | Integer | Ход выполнения задачи. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |

## SmartSubtitleTaskTransTextResultOutput

Результат перевода.

Используется действиями: DescribeBatchTaskDetail, DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| SegmentSet | Array of [SmartSubtitleTaskTransTextSegmentItem](#SmartSubtitleTaskTransTextSegmentItem) | Список сегментов для перевода. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |
| SubtitlePath | String | Путь файла субтитров. |
| OutputStorage | [TaskOutputStorage](#TaskOutputStorage) | Место хранения файла субтитров. |
| Path | String | URL файла субтитров. |
| SubtitleResults | Array of [SubtitleTransResultItem](#SubtitleTransResultItem) | Возвращаемый результат перевода при многоязычном переводе. |

## SmartSubtitleTaskTransTextSegmentItem

Переведённый сегмент.

Используется действиями: DescribeBatchTaskDetail, DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Confidence | Float | Уверенность распознанного сегмента. Диапазон значений: 0-100. |
| StartTimeOffset | Float | Начальное смещение времени распознанного сегмента в секундах. |
| EndTimeOffset | Float | Конечное смещение времени распознанного сегмента в секундах. |
| Text | String | Распознанный текст. |
| Trans | String | Переведённый текст. |
| Wordlist | Array of [WordResult](#WordResult) | Информация о временных метках слова.  Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |

## SmartSubtitleTemplateItem

Детали шаблона интеллектуальных субтитров.

Используется действиями: DescribeSmartSubtitleTemplates.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | Integer | Уникальный идентификатор шаблона интеллектуальных субтитров. |
| Name | String | Имя шаблона интеллектуальных субтитров. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |
| Comment | String | Описание шаблона интеллектуальных субтитров. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |
| Type | String | Тип шаблона. Допустимые значения: * Preset: системный предустановленный шаблон * Custom: определяемый пользователем шаблон Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |
| AsrHotWordsConfigure | [AsrHotWordsConfigure](#AsrHotWordsConfigure) | Параметр лексикона горячих слов ASR. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |
| AsrHotWordsLibraryName | String | Имя лексикона горячих слов, связанного с шаблоном. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |
| VideoSrcLanguage | String | Список исходных языков видео с интеллектуальными субтитрами. `zh`: упрощённый китайский. `yue`: кантонский. `zh-PY`: китайский, английский и кантонский. `zh_medical`: китайский (медицинский сценарий). `zh_dialect`: китайский диалект. `prime_zh`: китайский, английский и китайские диалекты. `zh_en`: китайский и английский. `en`: английский. `ja`: японский. `ko`: корейский. `fr`: французский. `es`: испанский. `it`: итальянский. `de`: немецкий. `tr`: турецкий. `ru`: русский. `pt`: португальский (Бразилия). `pt-PT`: португальский (Португалия). `vi`: вьетнамский. `id`: индонезийский. `ms`: малайский. `th`: тайский. `ar`: арабский. `hi`: хинди. `fil`: филиппинский. `auto`: автоматическое распознавание (поддерживается только при чистом переводе субтитров). |
| SubtitleFormat | String | Формат файла интеллектуальных субтитров. - vtt: WebVTT.- srt: SRT.- original: то же, что исходный файл субтитров (для шаблонов перевода субтитров).- Не указано или пусто: файл субтитров не создаётся. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| SubtitleType | Integer | Тип языка интеллектуальных субтитров. 0: исходный язык 1: целевой язык 2: исходный язык + целевой язык Значение может быть только 0, когда TranslateSwitch установлен на OFF. Значение может быть только 1 или 2, когда TranslateSwitch установлен на ON. |
| TranslateSwitch | String | Переключатель перевода субтитров. ON: включить перевод OFF: отключить перевод Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |
| TranslateDstLanguage | String | Целевой язык для перевода субтитров. Это поле действительно, когда значение TranslateSwitch равно ON. `zh`: упрощённый китайский. `zh-TW`: традиционный китайский. `en`: английский. `ja`: японский. `ko`: корейский. `fr`: французский. `es`: испанский. `it`: итальянский. `de`: немецкий. `tr`: турецкий. `ru`: русский. `pt`: португальский (Бразилия). `pt-PT`: португальский (Португалия). `vi`: вьетнамский. `id`: индонезийский. `ms`: малайский. `th`: тайский. `ar`: арабский. `hi`: хинди. `fil`: филиппинский. **Примечание**: используйте `/` для разделения нескольких языков, например `en/ja`, что означает английский и японский. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимых значений. |
| CreateTime | String | Время создания шаблона в [формате ISO datetime](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52). |
| UpdateTime | String | Время последнего изменения шаблона в [формате ISO datetime](https://intl.cloud.tencent.com/document/product/862/37710?from_cn_redirect=1#52). |
| AliasName | String | Псевдоним предустановленного шаблона интеллектуальных субтитров. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимого значения. |
| ProcessType | Integer | Тип обработки субтитров:- 0: распознавание субтитров ASR.- 1: перевод субтитров.- 2: распознавание субтитров OCR. |
| SelectingSubtitleAreasConfig | [SelectingSubtitleAreasConfig](#SelectingSubtitleAreasConfig) | Конфигурации области для поля извлечения OCR субтитров. Примечание. Это поле может возвращать null, что указывает на отсутствие допустимых значений. |

## SmartSubtitlesResult

Результат задачи интеллектуальных субтитров.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| Type | String | Тип задачи. Допустимые значения: - AsrFullTextRecognition: полное распознавание речи. - TransTextRecognition: перевод речи. - PureSubtitleTrans: чистый перевод субтитров. - OcrFullTextRecognition: извлечение субтитров на основ

## SubtitlePosition

Информация о позиции субтитров.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Название | Тип | Описание |
| --- | --- | --- |
| CenterY | Integer | Значение координаты Y при центрировании субтитра. |

## SubtitleResult

Результат задачи интеллектуального распознавания субтитров.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Название | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| Language | String | Нет | Язык файла субтитров. |
| Status | String | Нет | Успешна ли обработка. |
| Path | String | Нет | URL-адрес файла субтитров. |

## SubtitleTemplate

Параметры субтитров.

Используется действиями: CreateWorkflow, ProcessMedia, ResetWorkflow.

| Название | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| Path | String | Нет | URL-адрес субтитров для добавления к видео. Примечание. Это поле может возвращать null, что указывает на то, что допустимые значения получить не удалось. |
| StreamIndex | Integer | Нет | Указывает дорожку субтитров для встраивания субтитров в видео. Параметр Streamindex принимает значения, начиная с 0, где 0 обозначает использование первой дорожки субтитров в исходном видео. Если указан Path, используется Path приоритетно. Должен быть указан либо Path, либо Streamindex.  -Примечание. StreamIndex должен соответствовать индексу дорожки субтитров в исходном файле. Например, если дорожка субтитров в исходном файле — stream#0:3, StreamIndex должно быть 3. В противном случае обработка задачи завершится с ошибкой.   Примечание. Это поле может возвращать null, что указывает на то, что допустимое значение получить не удалось. |
| SubtitleFileInput | [MediaInputInfo](#MediaInputInfo) | Нет | Входная информация о файле субтитров для встраивания в видео. В настоящее время поддерживаются только файлы субтитров, хранящиеся в COS. Примечание. Это поле может возвращать null, что указывает на то, что допустимые значения получить не удалось. |
| FontFileInput | [MediaInputInfo](#MediaInputInfo) | Нет | Входная информация о файле шрифта встраиваемого субтитра. Поддерживаются URL и COS. Если указаны оба, используется информация URL. Если указан FontFileInput, FontFileInput имеет приоритет над FontType. |
| FontType | String | Нет | Тип шрифта. Допустимые значения: hei.ttf: SimHei.song.ttf: SimSun.kai.ttf (рекомендуется) или simkai.ttf: SimKai.msyh.ttf: Microsoft YaHei.msyhbd.ttf: Microsoft YaHei Bold.hkjgt.ttf: DynaFont King Gothic.dhttx.ttf: DianHei Extra Light.xqgdzt.ttf: XiQue GuZiDian.qpcyt.ttf: QiaoPin ChaoYuan.arial.ttf: Только английский.dinalternate.ttf: DIN Alternate Bold.helveticalt.ttf: Helvetica.helveticains.ttf: Helvetica Inserat.trajanpro.ttf: TrajanPro-Bold.korean.ttf: Корейский.japanese.ttf: Японский.thai.ttf: Тайский. Значение по умолчанию: hei.ttf.  Примечание: |
| FontSize | String | Нет | Размер шрифта. Если не указано, применяется размер шрифта из файла субтитров. Поддерживаются форматы в пикселях и процентах:  - Пиксели: Npx. Диапазон значений N: (0,4096]. - Проценты: N%. Диапазон значений N: (0,100]. Например, 10% означает, что размер шрифта субтитров составляет 10% от высоты исходного видео.  Размер по умолчанию составляет 5% от высоты исходного видео, если этот параметр не указан или размер шрифта не настроен в файле субтитров.  Примечание. Это поле может возвращать null, что указывает на то, что допустимые значения получить не удалось. |
| FontColor | String | Нет | Цвет шрифта. Формат: 0xRRGGBB. Значение по умолчанию: 0xFFFFFF (белый). Примечание. Это поле может возвращать null, что указывает на то, что допустимое значение получить не удалось. |
| FontAlpha | Float | Нет | Прозрачность текста. Диапазон значений: 0-1. `0`: Полностью прозрачно.`1`: Полностью непрозрачно. Значение по умолчанию: 1. Примечание. Это поле может возвращать null, что указывает на то, что допустимые значения получить не удалось. |
| YPos | String | Нет | Позиция субтитров по оси Y. Если этот параметр указан, встроенные координаты в файле субтитров будут проигнорированы. Поддерживаются форматы пикселей и процентов.   - Пиксели: Npx. Диапазон значений N: [0,4096].  - Проценты: N%. Диапазон значений N: [0,100]. Например, 10% указывает, что позиция субтитров по оси Y составляет 10% от высоты видео.  По умолчанию позиция составляет 4% от высоты исходного видео. Примечание. Начало координатных осей находится внизу центральной оси исходного видео, а опорная позиция субтитров находится внизу центральной оси субтитров, как показано на рисунке ниже. ![image](https://ie-mps-1258344699.cos.ap-nanjing.tencentcos.cn/common/cloud/mps-demo/102_ai_subtitle/subtitle_style.png)  Примечание. Это поле может возвращать null, что указывает на то, что допустимое значение получить не удалось. |
| BoardY | String | Нет | Позиция фона субтитров по оси Y. Поддерживаются форматы пикселей и процентов.   - Пиксели: Npx. Диапазон значений N: [0,4096].  - Проценты: N%. Диапазон значений N: [0,100]. Например, 10% указывает, что позиция фона субтитров по оси Y составляет 10% от высоты видео.  Если этот параметр не указан, фон субтитров отключен. Примечание. Начало координатных осей находится внизу центральной оси исходного видео, а опорная позиция фона субтитров находится внизу центральной оси исходного видео, как показано на рисунке ниже. ![image](https://ie-mps-1258344699.cos.ap-nanjing.tencentcos.cn/common/cloud/mps-demo/102_ai_subtitle/subtitle_style.png)  Примечание. Это поле может возвращать null, что указывает на то, что допустимое значение получить не удалось. |
| BoardWidth | Integer | Нет | Ширина фона. Значение должно быть положительным целым числом. - Диапазон значений для пикселей: [0,4096]. - Диапазон значений для процентов: [0, 100]. Если фон включен и этот параметр не указан, ширина по умолчанию составляет 90% от ширины исходного видео.  Примечание. Это поле может возвращать null, что указывает на то, что допустимые значения получить не удалось. |
| BoardHeight | Integer | Нет | Высота фона. Значение должно быть положительным целым числом. - Диапазон значений для пикселей: [0,4096]. - Диапазон значений для процентов: [0, 100]. Если фон включен и этот параметр не указан, высота по умолчанию составляет 15% от высоты исходного видео.  Примечание. Это поле может возвращать null, что указывает на то, что допустимые значения получить не удалось. |
| BoardColor | String | Нет | Цвет фона. Формат: 0xRRGGBB. Значение по умолчанию: 0x000000 (черный). Примечание. Это поле может возвращать null, что указывает на то, что допустимое значение получить не удалось. |
| BoardAlpha | Float | Нет | Прозрачность фона субтитров. Диапазон значений: [0, 1]. 0: полностью прозрачно.1: полностью непрозрачно. Значение по умолчанию: 0.8. Примечание. Это поле может возвращать null, что указывает на то, что допустимые значения получить не удалось. |
| OutlineWidth | Float | Нет | Ширина штриха. Значение должно быть числом с плавающей точкой. - Диапазон значений для пикселей: [0, 1000]. - Диапазон значений для процентов: [0, 100]. Если это не указано, ширина по умолчанию составляет 0.3% от высоты исходного видео. |
| OutlineColor | String | Нет | Цвет штриха. Значение должно быть 6-значным шестнадцатеричным значением RGB. Если это не указано, цвет по умолчанию — черный. |
| OutlineAlpha | Float | Нет | Прозрачность штриха. Значение должно быть положительным числом с плавающей точкой в диапазоне (0, 1]. Если это не указано, значение по умолчанию — 1, что означает полностью непрозрачно. |
| ShadowWidth | Float | Нет | Ширина тени. Значение должно быть числом с плавающей точкой. - Диапазон значений для пикселей: [0, 1000]. - Диапазон значений для процентов: [0, 100]. Если это не указано, тень не применяется по умолчанию. |
| ShadowColor | String | Нет | Цвет тени. Значение должно быть 6-значным шестнадцатеричным значением RGB. Если это не указано, цвет по умолчанию — черный (при настроенной тени). |
| ShadowAlpha | Float | Нет | Прозрачность тени. Значение должно быть положительным числом с плавающей точкой в диапазоне (0, 1]. Если это не указано, значение по умолчанию — 1, что означает полностью непрозрачно (при настроенной тени). |
| LineSpacing | Integer | Нет | Интерлиньяж. Значение должно быть положительным целым числом. - Диапазон значений для пикселей: [0, 1000]. - Диапазон значений для процентов: [0, 100]. Если это не указано, значение по умолчанию — 0. |
| Alignment | String | Нет | Режим выравнивания. Допустимые значения: top: Верхняя позиция субтитров зафиксирована, нижняя позиция изменяется в зависимости от количества строк. bottom: Нижняя позиция субтитров зафиксирована, верхняя позиция изменяется в зависимости от количества строк. Если это не указано, по умолчанию используется выравнивание по нижнему краю. |
| BoardWidthUnit | Integer | Нет | Значение по умолчанию — 0. Если это установлено на 1, значение BoardWidth — это процент от ширины видео. |
| BoardHeightUnit | Integer | Нет | Значение по умолчанию — 0. Если это установлено на 1, значение BoardHeight — это процент от высоты видео. |
| OutlineWidthUnit | Integer | Нет | Значение по умолчанию — 0. Если это установлено на 1, значение OutlineWidth — это процент от высоты видео. |
| ShadowWidthUnit | Integer | Нет | Значение по умолчанию — 0. Если это установлено на 1, значение ShadowWidth — это процент от высоты видео. |
| LineSpacingUnit | Integer | Нет | Значение по умолчанию — 0. Если это установлено на 1, значение LineSpacing — это процент от высоты видео. |

## SubtitleTransResultItem

Результат вывода перевода субтитров.

Используется действиями: DescribeBatchTaskDetail, DescribeTaskDetail, ParseNotification.

| Название | Тип | Описание |
| --- | --- | --- |
| Status | String | Маркер перевода. - Success - Error |
| TransSrc | String | Исходный язык (например, "en"). |
| TransDst | String | Целевой язык (например, "zh"). |
| Path | String | URL-адрес файла субтитров. |

## SuperResolutionConfig

Конфигурация повышения разрешения.

Используется действиями: CreateProcessImageTemplate, CreateTranscodeTemplate, ModifyProcessImageTemplate, ModifyTranscodeTemplate, ProcessImage.

| Название | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| Switch | String | Нет | Включена ли функция. Допустимые значения: ONOFF Значение по умолчанию: ON. |
| Type | String | Нет | Интенсивность. Допустимые значения: lq: Для видео низкого разрешения с явным шумом hq: Для видео высокого разрешения Значение по умолчанию: lq. Примечание. Это поле может возвращать null, что указывает на то, что допустимые значения получить не удалось. |
| Size | Integer | Нет | Соотношение целевого разрешения к исходному разрешению. Допустимые значения: 2 Значение по умолчанию: 2. Примечание. Это поле может возвращать null, что указывает на то, что допустимые значения получить не удалось. |

## SvgWatermarkInput

Входной параметр шаблона водяного знака SVG

Используется действиями: CreateWatermarkTemplate, DescribeWatermarkTemplates.

| Название | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| Width | String | Нет | Ширина водяного знака, поддерживает шесть форматов: px, %, W%, H%, S%, и L%: Если строка заканчивается на px, `Width` водяного знака будет в пикселях; например, `100px` означает, что `Width` составляет 100 пх; если введено `0px`  и `Height` не равно `0px`, ширина водяного знака будет пропорционально масштабироваться на основе исходного изображения SVG; если для обоих `Width` и `Height` введено `0px`, ширина водяного знака будет равна ширине исходного изображения SVG;Если строка заканчивается на `W%`, `Width` водяного знака будет указанным процентом от ширины видео; например, `10W%` означает, что `Width` составляет 10% от ширины видео;Если строка заканчивается на `H%`, `Width` водяного знака будет указанным процентом от высоты видео; например, `10H%` означает, что `Width` составляет 10% от высоты видео;Если строка заканчивается на `S%`, `Width` водяного знака будет указанным процентом от короткой стороны видео; например, `10S%` означает, что `Width` составляет 10% от короткой стороны видео;Если строка заканчивается на `L%`, `Width` водяного знака будет указанным процентом от длинной стороны видео; например, `10L%` означает, что `Width` составляет 10% от длинной стороны видео;Если строка заканчивается на %, смысл совпадает с `W%`. Значение по умолчанию: 10W%. |
| Height | String | Нет | Высота водяного знака, поддерживает шесть форматов: px, %, W%, H%, S%, и L%: Если строка заканчивается на px, `Height` водяного знака будет в пикселях; например, `100px` означает, что `Height` составляет 100 пх; если введено `0px`  и `Width` не равно `0px`, высота водяного знака будет пропорционально масштабироваться на основе исходного изображения SVG; если для обоих `Width` и `Height` введено `0px`, высота водяного знака будет равна высоте исходного изображения SVG;Если строка заканчивается на `W%`, `Height` водяного знака будет указанным процентом от ширины видео; например, `10W%` означает, что `Height` составляет 10% от ширины видео;Если строка заканчивается на `H%`, `Height` водяного знака будет указанным процентом от высоты видео; например, `10H%` означает, что `Height` составляет 10% от высоты видео;Если строка заканчивается на `S%`, `Height` водяного знака будет указанным процентом от короткой стороны видео; например, `10S%` означает, что `Height` составляет 10% от короткой стороны видео;Если строка заканчивается на `L%`, `Height` водяного знака будет указанным процентом от длинной стороны видео; например, `10L%` означает, что `Height` составляет 10% от длинной стороны видео;Если строка заканчивается на %, смысл совпадает с `H%`. Значение по умолчанию: 0 px. |

## SvgWatermarkInputForUpdate

Входной параметр шаблона водяного знака SVG

Используется действиями: ModifyWatermarkTemplate.

| Название | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| Width | String | Нет | Ширина водяного знака, поддерживает шесть форматов: px, %, W%, H%, S%, и L%: Если строка заканчивается на px, `Width` водяного знака будет в пикселях; например, `100px` означает, что `Width` составляет 100 пх; если введено `0px`  и `Height` не равно `0px`, ширина водяного знака будет пропорционально масштабироваться на основе исходного изображения SVG; если для обоих `Width` и `Height` введено `0px`, ширина водяного знака будет равна ширине исходного изображения SVG;Если строка заканчивается на `W%`, `Width` водяного знака будет указанным процентом от ширины видео; например, `10W%` означает, что `Width` составляет 10% от ширины видео;Если строка заканчивается на `H%`, `Width` водяного знака будет указанным процентом от высоты видео; например, `10H%` означает, что `Width` составляет 10% от высоты видео;Если строка заканчивается на `S%`, `Width` водяного знака будет указанным процентом от короткой стороны видео; например, `10S%` означает, что `Width` составляет 10% от короткой стороны видео;Если строка заканчивается на `L%`, `Width` водяного знака будет указанным процентом от длинной стороны видео; например, `10L%` означает, что `Width` составляет 10% от длинной стороны видео;Если строка заканчивается на %, смысл совпадает с `W%`. Значение по умолчанию: 10W%. |
| Height | String | Нет | Высота водяного знака, поддерживает шесть форматов: px, %, W%, H%, S%, и L%: Если строка заканчивается на px, `Height` водяного знака будет в пикселях; например, `100px` означает, что `Height` составляет 100 пх; если введено `0px`  и `Width` не равно `0px`, высота водяного знака будет пропорционально масштабироваться на основе исходного изображения SVG; если для обоих `Width` и `Height` введено `0px`, размер водяного знака будет равен размеру исходного изображения SVG;Если строка заканчивается на `W%`, `Height` водяного знака будет указанным процентом от ширины видео; например, `10W%` означает, что `Height` составляет 10% от ширины видео;Если строка заканчивается на `H%`, `Height` водяного знака будет указанным процентом от высоты видео; например, `10H%` означает, что `Height` составляет 10% от высоты видео;Если строка заканчивается на `S%`, `Height` водяного знака будет указанным процентом от короткой стороны видео; например, `10S%` означает, что `Height` составляет 10% от короткой стороны видео;Если строка заканчивается на `L%`, `Height` водяного знака будет указанным процентом от длинной стороны видео; например, `10L%` означает, что `Height` составляет 10% от длинной стороны видео;Если строка заканчивается на %, смысл совпадает с `W%`. Значение по умолчанию: 0px. |

## TEHDConfig

Конфигурация параметров TESHD.

Используется действиями: CreateTranscodeTemplate, CreateWorkflow, DescribeTranscodeTemplates, ProcessMedia, ResetWorkflow.

| Название | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| Type | String | Да | Тип TESHD. Допустимые значения: TEHD-100: TESHD-100. Если этот параметр оставлен пустым, TESHD не будет включен. |
| MaxVideoBitrate | Integer | Нет | Максимальный битрейт, действительный при `Type` равном `TESHD`. Если этот параметр оставлен пустым или введено 0, верхний предел битрейта не будет установлен. |

## TEHDConfigForUpdate

Конфигурация параметров TESHD.

Используется действиями: CreateWorkflow, ModifyTranscodeTemplate, ProcessMedia, ResetWorkflow.

| Название | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| Type | String | Нет | Тип TSC. Допустимые значения: `TEHD-100`: TSC-100 (видеокодирование TSC). `TEHD-200`: TSC-200 (аудиокодирование TSC).  Если этот параметр оставлен пустым, изменения не будут внесены. Примечание. Это поле может возвращать null, что указывает на то, что допустимые значения получить не удалось. |
| MaxVideoBitrate | Integer | Нет | Максимальный видеобитрейт. Если этот параметр не указан, изменения не будут внесены. Примечание. Это поле может возвращать null, что указывает на то, что допустимые значения получить не удалось. |

## TagConfigureInfo

Параметр управления задачей интеллектуального тегирования

Используется действиями: CreateAIAnalysisTemplate, DescribeAIAnalysisTemplates.

| Название | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| Switch | String | Да | Переключатель задачи интеллектуального тегирования. Допустимые значения: ON: включить задачу интеллектуального тегирования;OFF: отключить задачу интеллектуального тегирования. |

## TagConfigureInfoForUpdate

Параметр управления задачей интеллектуального тегирования

Используется действиями: ModifyAIAnalysisTemplate.

| Название | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| Switch | String | Нет | Переключатель задачи интеллектуального тегирования. Допустимые значения: ON: включить задачу интеллектуального тегирования;OFF: отключить задачу интеллектуального тегирования. |

## TaskNotifyConfig

Конфигурация уведомления о событиях задачи.

Используется действиями: BatchProcessMedia, CreateSchedule, CreateWorkflow, DescribeBatchTaskDetail, DescribeSchedules, DescribeTaskDetail, DescribeWorkflows, EditMedia, ExtractBlindWatermark, ModifySchedule, ProcessMedia, ResetWorkflow.

| Название | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| NotifyType | String | Нет | Тип уведомления. доступные значения:. CMQ: автономный. переключиться на TDMQ-CMQ.. TDMQ-CMQ: очередь сообщений. URL: когда указан URL-адрес, HTTP-обратный вызов отправляется на адрес, указанный в NotifyUrl. протокол обратного вызова — HTTP+json. содержимое тела пакета совпадает с выходными параметрами API parseeventnotification.. SCF: не рекомендуется. требуется дополнительная конфигурация в консоли.. AWS-SQS: очередь AWS, подходит только для задач AWS и требует того же региона.. примечание: если оставить пустым, по умолчанию используется TDMQ-CMQ. для использования другого типа необходимо заполнить соответствующее значение типа. при использовании очереди сообщений TDMQ-CMQ чрезмерно большой ответ задачи может привести к сбою очереди.. |
| NotifyMode | String | Нет | Метод уведомления рабочего процесса. Допустимые значения: Finish, Change. Если этот параметр оставлен пустым, будет использован `Finish`. |
| NotifyUrl | String | Нет | URL-адрес HTTP-обратного вызова, требуется если `NotifyType` установлен на `URL` |
| CmqModel | String | Нет | Модель CMQ или TDMQ-CMQ. Допустимые значения: Queue, Topic. |
| CmqRegion | String | Нет | Регион CMQ или TDMQ-CMQ, например `sh` (Шанхай) или `bj` (Пекин). |
| TopicName | String | Нет | Тема CMQ или TDMQ-CMQ для получения уведомлений. Этот параметр действителен при `CmqModel` равном `Topic`. |
| QueueName | String | Нет | Очередь CMQ или TDMQ-CMQ для получения уведомлений. Этот параметр действителен при `CmqModel` равном `Queue`. |
| AwsSQS | [AwsSQS](#AwsSQS) | Нет | Очередь AWS SQS. Этот параметр требуется, если `NotifyType` равен `AWS-SQS`.  Примечание. Это поле может возвращать null, что указывает на то, что допустимые значения получить не удалось. |
| NotifyKey | String | Нет | Ключ, используемый для создания подписи обратного вызова. |

## TaskOutputStorage

Информация об объекте вывода обработки медиа.

Используется действиями: BatchProcessMedia, CreateSchedule, CreateWorkflow, DescribeBatchTaskDetail, DescribeImageTaskDetail, DescribeSchedules, DescribeTaskDetail, DescribeWorkflows, EditMedia, ModifySchedule, ParseNotification, ProcessImage, ProcessLiveStream, ProcessMedia, ResetWorkflow.

| Название | Тип | Требуется | Описание |
| --- | --- | --- | --- |
| Type | String | Да | Указывает тип хранилища объектов вывода сервиса обработки медиа.

## TerrorismOcrReviewTemplateInfo

Параметры для выявления конфиденциальной информации на основе распознавания текста в изображениях (OCR).

Используется операциями: CreateContentReviewTemplate, DescribeContentReviewTemplates.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Switch | String | Да | Включить выявление конфиденциальной информации на основе OCR. Допустимые значения: ONOFF |
| BlockConfidence | Integer | Нет | Пороговая оценка нарушения. Если эта оценка достигнута или превышена при интеллектуальной проверке, это будет считаться предполагаемым нарушением. Если этот параметр не указан, по умолчанию используется значение 100. Диапазон значений: 0–100. |
| ReviewConfidence | Integer | Нет | Пороговая оценка для ручной проверки. Если эта оценка достигнута или превышена при интеллектуальной проверке, будет признана необходимость ручной проверки. Если этот параметр не указан, по умолчанию используется значение 75. Диапазон значений: 0–100. |

## TerrorismOcrReviewTemplateInfoForUpdate

Параметры для выявления конфиденциальной информации на основе распознавания текста в изображениях (OCR).

Используется операциями: ModifyContentReviewTemplate.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Switch | String | Нет | Включить выявление конфиденциальной информации на основе OCR. Допустимые значения: ONOFF |
| BlockConfidence | Integer | Нет | Пороговая оценка нарушения. Если эта оценка достигнута или превышена при интеллектуальной проверке, это будет считаться предполагаемым нарушением. Если этот параметр не указан, по умолчанию используется значение 100. Диапазон значений: 0–100. |
| ReviewConfidence | Integer | Нет | Пороговая оценка для ручной проверки. Если эта оценка достигнута или превышена при интеллектуальной проверке, будет признана необходимость ручной проверки. Если этот параметр не указан, по умолчанию используется значение 75. Диапазон значений: 0–100. |

## TextWatermarkTemplateInput

Шаблон текстовых водяных знаков

Используется операциями: CreateWatermarkTemplate, DescribeWatermarkTemplates.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| FontType | String | Да | Тип шрифта. В настоящее время поддерживаются два типа: simkai.ttf: поддерживаются как китайский, так и английский языки; arial.ttf: поддерживается только английский язык. |
| FontSize | String | Да | Размер шрифта в формате Npx. N — числовое значение с диапазоном [0, 1] или [8, 4096]. |
| FontColor | String | Да | Цвет шрифта в формате 0xRRGGBB. Значение по умолчанию: 0xFFFFFF (белый). |
| FontAlpha | Float | Да | Прозрачность текста. Диапазон значений: (0, 1] 0: полностью прозрачный; 1: полностью непрозрачный. Значение по умолчанию: 1. |
| TextContent | String | Нет | Текстовое содержимое, максимум 100 символов. Примечание: это поле может возвращать null, указывая на то, что достоверные значения не получены. |

## TextWatermarkTemplateInputForUpdate

Шаблон текстовых водяных знаков

Используется операциями: ModifyWatermarkTemplate.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| FontType | String | Нет | Тип шрифта. В настоящее время поддерживаются два типа: simkai.ttf: поддерживаются как китайский, так и английский языки; arial.ttf: поддерживается только английский язык. |
| FontSize | String | Нет | Размер шрифта в формате Npx. N — числовое значение с диапазоном [0, 1] или [8, 4096]. |
| FontColor | String | Нет | Цвет шрифта в формате 0xRRGGBB. Значение по умолчанию: 0xFFFFFF (белый). |
| FontAlpha | Float | Нет | Прозрачность текста. Диапазон значений: (0, 1] 0: полностью прозрачный; 1: полностью непрозрачный. |
| TextContent | String | Нет | Текстовое содержимое, максимум 100 символов. |

## TimeSpotCheck

Политика выявления для проверки качества медиа.

Используется операциями: CreateQualityControlTemplate, ModifyQualityControlTemplate.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| CheckDuration | Integer | Нет | Длительность каждого цикла выявления в секундах. Диапазон значений:   - Минимальное значение: 10.  - Максимальное значение: 86400. |
| CheckInterval | Integer | Нет | Интервал выявления в секундах. Обозначает длительность после завершения проверки и перед следующей проверкой. Диапазон значений:  - Минимальное значение: 10.  - Максимальное значение: 3600. |
| SkipDuration | Integer | Нет | Пропускаемая длительность открытия в секундах. Диапазон значений:  - Минимальное значение: 1.  - Максимальное значение: 1800. |
| CirclesNumber | Integer | Нет | Количество циклов. Диапазон значений:  - Минимальное значение: 0.  - Максимальное значение: 1000.  Если значение равно 0 или не указано, это означает, что циклы выполняются до конца видео. |

## TrackInfo

Информация об аудиодорожке.

Используется операциями: CreateTranscodeTemplate.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| TrackNum | String | Нет | Порядковый номер аудиодорожки и звукового канала. Когда значение SelectType равен track, это значение представляет собой целое число, например: 1. Когда значение SelectType равен track_channel, это значение представляет собой десятичное число, например: 1.0. Значение по умолчанию: 1.0. Целая часть обозначает порядковый номер аудиодорожки, десятичная часть обозначает звуковой канал. Порядковый номер аудиодорожки — это значение индекса потока аудиодорожки, которое может быть 0 или положительным целым числом. Десятичная часть поддерживает до 2 десятичных знаков и поддерживает только значения 0–63. Однако когда Codec имеет значение aac/eac3/ac3, для десятичной части поддерживаются только значения 0–15. Например: для аудиодорожки со значением индекса потока 1, 1.0 обозначает первый звуковой канал этой аудиодорожки, 1.1 обозначает второй звуковой канал этой аудиодорожки.  Примечание: это поле может возвращать null, указывая на то, что достоверные значения не получены. |
| ChannelVolume | Array of Float | Нет | Громкость звукового канала. Когда значение AudioChannel равен 1, длина этого массива составляет 1. Например: [6]. Когда значение AudioChannel равен 2, длина этого массива составляет 2. Например: [0,6]. Когда значение AudioChannel равен 6, длина этого массива больше 2 и меньше 16. Например: [-60,0,0,6].  Укажите массив значений для этого параметра. Диапазон значений находится между -60 и 6, где -60 обозначает отключение звука, 0 сохраняет исходную громкость, 6 удваивает исходную громкость. Значение по умолчанию — -60. Примечание: это поле поддерживает до 3 десятичных знаков.  Примечание: это поле может возвращать null, указывая на то, что достоверные значения не получены. |

## TranscodeTaskInput

Тип входного параметра задачи перекодирования

Используется операциями: CreateSchedule, CreateWorkflow, DescribeTaskDetail, ModifySchedule, ParseNotification, ProcessMedia, ResetWorkflow.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Definition | Integer | Да | ID шаблона видеоперекодирования. |
| RawParameter | [RawTranscodeParameter](#RawTranscodeParameter) | Нет | Пользовательский параметр видеоперекодирования. Действителен, когда Definition установлен на 0. Этот параметр используется в сценариях высокой кастомизации. Рекомендуется сначала использовать Definition для указания параметров перекодирования. |
| OverrideParameter | [OverrideTranscodeParameter](#OverrideTranscodeParameter) | Нет | Пользовательский параметр видеоперекодирования, действителен, когда `Definition` не равен 0. Если введены какие-либо параметры из этой структуры, они будут использованы для переопределения соответствующих параметров в шаблонах. Этот параметр используется в высокоспециализированных сценариях. Рекомендуется использовать только `Definition` для указания параметра перекодирования. Примечание: это поле может возвращать `null`, указывая на то, что достоверные значения не найдены. |
| WatermarkSet | Array of [WatermarkInput](#WatermarkInput) | Нет | Список водяных знаков. Поддерживаются несколько изображений или текстовых водяных знаков, максимум 10. |
| BlindWatermark | [BlindWatermarkInput](#BlindWatermarkInput) | Нет | Параметр цифрового водяного знака. Примечание: это поле может возвращать null, указывая на то, что достоверные значения не получены. |
| MosaicSet | Array of [MosaicInput](#MosaicInput) | Нет | Список размытий. Может быть поддержано до 10 единиц. |
| StartTimeOffset | Float | Нет | Смещение времени начала перекодированного видео в секундах. Если этот параметр не указан или установлен на 0, перекодированное видео начнется одновременно с исходным видео. Если этот параметр установлен на положительное число (например, n), перекодированное видео начнется на n-й секунде исходного видео. Если этот параметр установлен на отрицательное число (например, -n), перекодированное видео начнется за n секунд до конца исходного видео. |
| EndTimeOffset | Float | Нет | Смещение времени окончания перекодированного видео в секундах. Если этот параметр не указан или установлен на 0, перекодированное видео закончится одновременно с исходным видео. Если этот параметр установлен на положительное число (например, n), перекодированное видео закончится на n-й секунде исходного видео. Если этот параметр установлен на отрицательное число (например, -n), перекодированное видео закончится за n секунд до конца исходного видео. |
| OutputStorage | [TaskOutputStorage](#TaskOutputStorage) | Нет | Целевое хранилище (bucket) для выходного файла. Если этот параметр не указан, будет унаследовано значение `OutputStorage` родительской папки. Примечание: это поле может возвращать null, указывая на то, что достоверные значения не получены. |
| OutputObjectPath | String | Нет | Путь вывода основного файла после перекодирования, который может быть относительным или абсолютным путем. Если необходимо определить путь вывода, путь должен заканчиваться на `.{format}`. Для имен переменных см. [Переменная имени файла](https://intl.cloud.tencent.com/document/product/862/37039?from_cn_redirect=1). Пример относительного пути: Filename_{Variable name}.{format}.Filename.{format}. Пример абсолютного пути: /Custom path/Filename_{Variable name}.{format}. Если оставлено пустым, по умолчанию используется относительный путь: `{inputName}_transcode_{definition}.{format}`. |
| SegmentObjectName | String | Нет | Путь к выходному файлу (путь к ts при перекодировании в HLS), может быть только относительным путем. Если этот параметр не указан, будет использован следующий относительный путь по умолчанию: `{inputName}_transcode_{definition}_{number}.{format}`. |
| ObjectNumberFormat | [NumberFormat](#NumberFormat) | Нет | Правило переменной `{number}` в выходном пути после перекодирования. Примечание: это поле может возвращать null, указывая на то, что достоверные значения не получены. |
| HeadTailParameter | [HeadTailParameter](#HeadTailParameter) | Нет | Параметры вступительных и завершающих титров. Примечание: это поле может возвращать `null`, указывая на то, что достоверные значения не найдены. |

## TranscodeTemplate

Детали шаблона перекодирования

Используется операциями: DescribeTranscodeTemplates.

| Имя | Тип | Описание |
| --- | --- | --- |
| Definition | String | Уникальный ID шаблона перекодирования. |
| Container | String | Формат контейнера. Допустимые значения: mp4, flv, hls, mp3, flac, ogg. |
| Name | String | Имя шаблона перекодирования. Примечание: это поле может возвращать null, указывая на то, что достоверные значения не получены. |
| Comment | String | Описание шаблона. Примечание: это поле может возвращать null, указывая на то, что достоверные значения не получены. |
| Type | String | Тип шаблона. Допустимые значения: Preset: встроенный шаблон; Custom: пользовательский шаблон. |
| RemoveVideo | Integer | Удалять ли видеоданные. Допустимые значения: 0: сохранить; 1: удалить. |
| RemoveAudio | Integer | Удалять ли аудиоданные. Допустимые значения: 0: сохранить; 1: удалить. |
| VideoTemplate | [VideoTemplateInfo](#VideoTemplateInfo) | Параметр конфигурации видеопотока. Это поле действительно только, когда `RemoveVideo` равен 0. Примечание: это поле может возвращать null, указывая на то, что достоверные значения не получены. |
| AudioTemplate | [AudioTemplateInfo](#AudioTemplateInfo) | Параметр конфигурации аудиопотока. Это поле действительно только, когда `RemoveAudio` равен 0. Примечание: это поле может возвращать null, указывая на то, что достоверные значения не получены. |
| TEHDConfig | [TEHDConfig](#TEHDConfig) | Параметр перекодирования TESHD. Чтобы его включить, обратитесь к представителю отдела продаж Tencent Cloud. Примечание: это поле может возвращать null, указывая на то, что достоверные значения не получены. |
| ContainerType | String | Фильтр формата контейнера. Допустимые значения: Video: формат видеоконтейнера, который может содержать как видеопоток, так и аудиопоток; PureAudio: формат аудиоконтейнера, который может содержать только аудиопоток. |
| CreateTime | String | Время создания шаблона в [формате ISO даты](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |
| UpdateTime | String | Время последнего изменения шаблона в [формате ISO даты](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |
| EnhanceConfig | [EnhanceConfig](#EnhanceConfig) | Конфигурация улучшения аудио/видео. Примечание: это поле может возвращать null, указывая на то, что достоверные значения не получены. |
| AliasName | String | Псевдоним шаблона перекодирования. Примечание: это поле может возвращать null, указывая на то, что достоверные значения не получены. |

## TranslateConfigureInfo

Параметр управления полной задачей распознавания речи.

Используется операциями: DescribeAIRecognitionTemplates.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| Switch | String | Да | Переключатель полной задачи распознавания речи. Допустимые значения: ON: включить задачу интеллектуального полного распознавания речи; OFF: отключить задачу интеллектуального полного распознавания речи. |
| SourceLanguage | String | Нет |  |
| DestinationLanguage | String | Нет |  |
| SubtitleFormat | String | Нет | Формат создаваемого файла субтитров. Оставление пустым означает, что файл субтитров создаваться не будет. Допустимое значение: vtt: создать файл субтитров WebVTT.  Примечание: это поле может возвращать null, указывая на то, что достоверные значения не получены. |

## UpdateSmartErasePrivacyConfig

Конфигурация защиты конфиденциальности для шаблона интеллектуального удаления.

Используется операциями: ProcessMedia.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| PrivacyModel | String | Нет | Метод удаления защиты конфиденциальности. - blur - размытие - mosaic - мозаика |
| PrivacyTargets | Array of String | Нет | Целевой объект защиты конфиденциальности. (При использовании API Explorer не требуется указывать массив. Добавьте соответствующие элементы и введите соответствующие значения.) - face: человеческое лицо. - plate: номерной знак. |

## UpdateSmartEraseSubtitleConfig

Конфигурация удаления субтитров для шаблона интеллектуального удаления.

Используется операциями: ProcessMedia.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| SubtitleEraseMethod | String | Нет | Метод удаления субтитров. **Автоматическое удаление:** видеосубтитры автоматически распознаются с использованием модели ИИ и удаляются без следов для создания нового видео. Однако из-за помех в изображении и особых стилей субтитров могут возникнуть пропущенные или неправильные удаления. В этом случае можно указать область удаления. При использовании автоматического удаления, если AutoAreas не указана, область по умолчанию (нижняя средняя часть изображения) будет автоматически удалена. Если указана AutoAreas, указанная область будет автоматически удалена. **Удаление указанной области:** если позиция субтитров относительно фиксирована, рекомендуется указать область удаления непосредственно, чтобы свести к минимуму пропущенные удаления. Когда вы выбираете удаление указанной области, укажите по крайней мере одну область для CustomAreas. - auto: автоматическое удаление. - custom: удаление указанной области. |
| SubtitleModel | String | Нет | Модель удаления субтитров. **Стандартное издание (рекомендуется):** для стандартных стилей субтитров рекомендуется выбрать это издание, чтобы обеспечить лучшие результаты без следов в деталях. **Издание области:** если субтитры имеют особые стили, такие как каллиграфия, тень или эффекты движения, рекомендуется выбрать это издание, чтобы обеспечить большую область удаления. Однако результат удаления в деталях не так хорош, как в стандартном издании. - standard: стандартное издание. - area: издание области. |
| OcrSwitch | String | Нет | Включить ли извлечение субтитров через OCR. Значение по умолчанию — OFF. Извлечение субтитров через OCR поддерживается тогда и только тогда, когда SubtitleEraseMethod установлен на auto. Когда извлечение субтитров через OCR включено, оно определяет текстовую область, которая появляется наиболее постоянно и стабильно в области автоматического удаления, как область субтитров. Текст в области субтитров извлекается и удаляется. - ON: включено. -OFF: отключено. |
| SubtitleLang | String | Нет | Язык субтитров, используемый для направления распознавания OCR. Значение по умолчанию — zh_en. Этот параметр действителен только, когда OcrSwitch установлен на ON. - zh_en: китайский и английский. - multi: другие. Ниже приведены другие языки, поддерживаемые для распознавания: китайский, английский, японский, корейский, испанский, французский, немецкий, португальский, вьетнамский, малайский, русский, итальянский, нидерландский, шведский, финский, датский, норвежский, венгерский, тайский, хинди, арабский, индийский бенгальский, индийский гуджарати, индийский каннада, индийский малаялам, индийский тамильский, индийский телугу, словенский, польский, каталанский, боснийский, чешский, эстонский, хорватский, панджаби, маратхи, азербайджанский, индонезийский, люксембургский, литовский, латышский, мальтийский, словацкий, турецкий, казахский, греческий, ирландский, беларусский, кхмерский, тагальский, пушту, персидский и таджицкий. |
| SubtitleFormat | String | Нет | Формат файла субтитров. Значение по умолчанию — vtt. Этот параметр действителен только, когда OcrSwitch установлен на ON. - srt: формат SRT. - vtt: формат WebVTT. |
| TransSwitch | String | Нет | Включить ли перевод субтитров. Значение по умолчанию — OFF. Этот параметр действителен только, когда OcrSwitch установлен на ON. - ON: включено. - OFF: отключено. |
| TransDstLang | String | Нет | Целевой язык для перевода субтитров. Значение по умолчанию — en. Этот параметр действителен только, когда TransSwitch установлен на ON. В настоящее время поддерживаются следующие языки: zh: упрощенный китайский. en: английский. ja: японский. ko: корейский. fr: французский. es: испанский. it: итальянский. de: немецкий. tr: турецкий. ru: русский. pt: португальский. vi: вьетнамский. id: индонезийский. ms: малайский. th: тайский. ar: арабский. hi: хинди. |
| AutoAreas | Array of [EraseArea](#EraseArea) | Нет | Пользовательская область для автоматического удаления. Для указанной области модели ИИ используются для автоматического обнаружения и удаления целевых объектов. Примечание: когда метод удаления установлен на custom, этот параметр недействителен. При изменении шаблона введите [] для области удаления; если этот параметр не указан, информация о области шаблона останется неизменной. |
| CustomAreas | Array of [EraseTimeArea](#EraseTimeArea) | Нет | Пользовательская область для удаления указанной области. Для указанной области удалите целевые объекты непосредственно без обнаружения и распознавания в течение выбранного периода времени. Примечание: при изменении шаблона введите [] для области удаления; если этот параметр не указан, информация о области шаблона останется неизменной. |

## UpdateSmartEraseWatermarkConfig

Конфигурация удаления водяного знака для шаблона интеллектуального удаления.

Используется операциями: ProcessMedia.

| Имя | Тип | Обязательно | Описание |
| --- | --- | --- | --- |
| WatermarkEraseMethod | String | Нет | Метод удаления водяного знака. **Автоматическое удаление:** видеоводяные знаки автоматически распознаются с использованием модели ИИ и удаляются для создания нового видео. Применяется к динамическим водяным знакам. При использовании автоматического удаления, если AutoAreas не указана, область полного видеоизображения будет автоматически удалена. Если указана AutoAreas, указанная область будет автоматически удалена.  **Удаление указанной области:** для статических водяных знаков в фиксированных позициях рекомендуется указать область удаления непосредственно. Когда вы выбираете удаление указанной области, укажите по крайней мере одну область. - auto: автоматическое удаление. - custom: удаление указанной области. |
| WatermarkModel | String | Нет | Модель удаления водяного знака. Базовое издание: обеспечивает средние результаты и высокую рентабельность. Применяется к анимационным видео или видео с чистым фоном. Расширенное издание: обеспечивает лучшие результаты. Применяется к реалистичным видео, таким как короткие драмы. - basic: базовое издание. - advanced: расширенное издание. |
| AutoAreas | Array of [EraseArea](#EraseArea) | Нет | Пользовательская область для автоматического удаления. Для указанной области модели ИИ используются для автоматического обнаружения и удаления целевых объектов. Примечание: когда метод удаления установлен на custom, этот параметр недействителен. Введите [] для области удаления; если этот параметр не указан, информация о области шаблона останется неизменной. |
| CustomAreas | Array of [EraseTimeArea](#EraseTimeArea) | Нет | Пользовательская область для удаления указанной области. Для указанной области удалите целевые объекты непосредственно без обнаружения и распознавания в течение выбранного периода времени. Примечание: введите [] для области удаления; если этот параметр не указан, информация о области шаблона останется неизменной. |

## UrlInputInfo

URL объекта для обработки.

Используется операциями: BatchProcessMedia, DescribeMediaMetaData, ExtractBlindWatermark, ProcessImage, ProcessMedia

## VODOutputStorage

Информация об объекте выходных данных VOD Pro для MPS.

Используется действиями: BatchProcessMedia, CreateSchedule, CreateWorkflow, EditMedia, ModifySchedule, ProcessImage, ProcessLiveStream, ProcessMedia, ResetWorkflow.

| Имя | Тип | Обязательный | Описание |
| --- | --- | --- | --- |
| Bucket | String | Нет | Указывает целевой ID Bucket для выходного файла, созданного MPS. |
| Region | String | Нет | Указывает регион целевого Bucket для выходных данных. |
| SubAppId | Integer | Нет | ID приложения VOD Pro. |

## VideoComprehensionResultItem

Результат анализа видеоэпизода.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Имя | Тип | Описание |
| --- | --- | --- |
| StartTime | Float | Время начала сегмента (единица: секунды). |
| EndTime | Float | Время окончания сегмента (единица: с). |
| Title | String | Название видеоклипа. |
| Description | String | Описание информации о кадре раскадровки. |
| Keywords | Array of String | Ключевые слова сцены. |

## VideoDenoiseConfig

Конфигурация удаления шума изображения.

Используется действиями: CreateTranscodeTemplate, ModifyTranscodeTemplate.

| Имя | Тип | Обязательный | Описание |
| --- | --- | --- | --- |
| Switch | String | Нет | Включить функцию или нет. Допустимые значения: ON, OFF. Значение по умолчанию: ON. |
| Type | String | Нет | Интенсивность. Допустимые значения: weak, strong. Значение по умолчанию: weak. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |

## VideoEnhanceConfig

Конфигурация улучшения видео.

Используется действиями: CreateTranscodeTemplate, ModifyTranscodeTemplate.

| Имя | Тип | Обязательный | Описание |
| --- | --- | --- | --- |
| FrameRate | [FrameRateConfig](#FrameRateConfig) | Нет | Конфигурация частоты кадров (старая) для интерполяции кадров. Новым пользователям рекомендуется использовать FrameRateWithDen для конфигурации частоты кадров интерполяции, которая поддерживает дроби и дает лучшие результаты. Обратите внимание, что FrameRate и FrameRateWithDen являются взаимоисключающими; одновременная конфигурация обоих может привести к сбоям задач. Конфигурация не вступает в силу, если исходная частота кадров больше или равна целевой частоте кадров. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| SuperResolution | [SuperResolutionConfig](#SuperResolutionConfig) | Нет | Конфигурация сверхвысокого разрешения. Видео не обрабатывается, если исходное разрешение выше целевого разрешения. Обратите внимание, что оно не может быть включено одновременно с улучшением больших моделей. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| Hdr | [HdrConfig](#HdrConfig) | Нет | Конфигурация HDR. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| Denoise | [VideoDenoiseConfig](#VideoDenoiseConfig) | Нет | Конфигурация снижения шума видео. Обратите внимание, что оно не может быть включено одновременно с улучшением LLM. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| ImageQualityEnhance | [ImageQualityEnhanceConfig](#ImageQualityEnhanceConfig) | Нет | Конфигурация комплексного улучшения. Обратите внимание, что можно настроить только один из трех пунктов: улучшение LLM, комплексное улучшение и удаление артефактов. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| ColorEnhance | [ColorEnhanceConfig](#ColorEnhanceConfig) | Нет | Конфигурация улучшения цвета. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| LowLightEnhance | [LowLightEnhanceConfig](#LowLightEnhanceConfig) | Нет | Конфигурация улучшения при слабом освещении. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| ScratchRepair | [ScratchRepairConfig](#ScratchRepairConfig) | Нет | Конфигурация удаления полос. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| ArtifactRepair | [ArtifactRepairConfig](#ArtifactRepairConfig) | Нет | Конфигурация удаления артефактов. Обратите внимание, что можно настроить только один из трех пунктов: улучшение LLM, комплексное улучшение и удаление артефактов. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| EnhanceSceneType | String | Нет | Конфигурация сценария улучшения. Допустимые значения: common: параметры базового улучшения, подходящие для различных типов видео, улучшающие общее качество изображения.AIGC: улучшение разрешения в целом. Использует технологию ИИ для повышения общего разрешения видео и четкости изображения.short_play: улучшение деталей лиц и субтитров, акцент на выражениях лиц персонажей и четкости субтитров для улучшения впечатления от просмотра.short_video: оптимизация сложных и разнообразных проблем качества изображения, адаптированное повышение качества для сложных сценариев, таких как короткие видео, для решения различных визуальных проблем.game: исправление размытия при движении и улучшение деталей, акцент на повышении четкости деталей игры и восстановлении размытых областей при движениях для более ясного и насыщенного содержимого изображения при игре.HD_movie_series: обеспечить плавное воспроизведение для видео UHD. Генерируются стандартные видео 4K HDR с частотой 60 FPS для удовлетворения потребностей вещания/OTT в видеоконтенте UHD. Поддерживаются форматы для сценариев вещания.LQ_material: восстановление видеоматериалов низкого разрешения/старых видео. Повышает общее разрешение и решает проблемы старых видео, такие как низкое разрешение, размытие, искажения, царапины и цветовая температура из-за их возраста.lecture: живые шоу, электронная коммерция, конференции и лекции. Улучшает эффект отображения лица и выполняет специальную оптимизацию, включая улучшение области лица, снижение шума и удаление артефактов, для сценариев, связанных с устным объяснением, таких как живые шоу, электронная коммерция, конференции и лекции.Ввод пустой строки указывает, что сценарий улучшения не используется. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| DiffusionEnhance | [DiffusionEnhanceConfig](#DiffusionEnhanceConfig) | Нет | Конфигурация улучшения больших моделей. Обратите внимание, что можно настроить только один из трех пунктов: улучшение LLM, комплексное улучшение и удаление артефактов. Не может быть включено одновременно с сверхвысоким разрешением и снижением шума. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| FrameRateWithDen | [FrameRateWithDenConfig](#FrameRateWithDenConfig) | Нет | Новая конфигурация частоты кадров для интерполяции кадров, которая поддерживает дроби. Обратите внимание, что она является взаимоисключающей с FrameRate. Конфигурация не вступает в силу, если исходная частота кадров больше или равна целевой частоте кадров. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |

## VideoTemplateInfo

Параметр конфигурации видеопотока

Используется действиями: CreateAdaptiveDynamicStreamingTemplate, CreateTranscodeTemplate, CreateWorkflow, DescribeTranscodeTemplates, ModifyAdaptiveDynamicStreamingTemplate, ProcessMedia, ResetWorkflow.

| Имя | Тип | Обязательный | Описание |
| --- | --- | --- | --- |
| Codec | String | Да | Формат кодирования видеопотоков. Допустимые значения: h264: кодирование H.264.h265: кодирование H.265.h266: кодирование H.266.av1: кодирование AOMedia Video 1.vp8: кодирование VP8.vp9: кодирование VP9.mpeg2: кодирование MPEG2.dnxhd: кодирование DNxHD.mv-hevc: кодирование MV-HEVC. Примечание: Кодек av1 в настоящее время поддерживает только mp4, webm и mkv. Примечание: Кодек H.266 в настоящее время поддерживает только mp4, hls, ts и mov. Примечание: Кодеки VP8 и VP9 в настоящее время поддерживают только webm и mkv. Примечание: Кодеки MPEG2 и dnxhd в настоящее время поддерживают только mxf. Примечание: Кодек MV-HEVC в настоящее время поддерживает только mp4, hls и mov. Среди них формат HLS поддерживает только MP4-сегментированный формат и требует, чтобы исходный источник был панорамным видео (с несколькими представлениями). |
| Fps | Integer | Да | Частота кадров видео. Диапазон значений: Когда FpsDenominator пуст, диапазон составляет [0, 120] в Гц. Когда FpsDenominator не пуст, диапазон Fps/FpsDenominator составляет [0, 120]. Если значение равно 0, частота кадров будет совпадать с частотой кадров исходного видео. |
| Bitrate | Integer | Да | Битрейт видеопотока в кбит/с. Диапазон значений: 0 и [128, 100000].Если значение равно 0, битрейт видео будет совпадать с битрейтом исходного видео. |
| ResolutionAdaptive | String | Нет | Адаптация разрешения. Допустимые значения: open: включено. Когда адаптация разрешения включена, `Width` указывает длинную сторону видео, а `Height` указывает короткую сторону.close: отключено. Когда адаптация разрешения отключена, `Width` указывает ширину видео, а `Height` указывает высоту. Значение по умолчанию: open. Примечание: Когда адаптация разрешения включена, `Width` не может быть меньше `Height`. |
| Width | Integer | Нет | Максимальное значение ширины (или длинной стороны) видеопотока в пикселях. Диапазон значений: 0 и [128, 4096]. Если оба значения Width и Height равны 0, разрешение совпадает с исходным.Если Width равно 0, но Height не равно 0, ширина будет масштабирована пропорционально.Если Width не равно 0, но Height равно 0, высота будет масштабирована пропорционально.Если оба значения Width и Height не равны 0, разрешение соответствует спецификации пользователя. Значение по умолчанию: 0. Примечание: Если Codec установлен на MV-HEVC, максимальное значение может быть 7680. |
| Height | Integer | Нет | Максимальное значение высоты (или короткой стороны) видеопотока в пикселях. Диапазон значений: 0 и [128, 4096]. Если оба значения Width и Height равны 0, разрешение совпадает с исходным.Если Width равно 0, но Height не равно 0, ширина будет масштабирована пропорционально.Если Width не равно 0, но Height равно 0, высота будет масштабирована пропорционально.Если оба значения Width и Height не равны 0, разрешение соответствует спецификации пользователя. Значение по умолчанию: 0. Примечание: Если Codec установлен на MV-HEVC, максимальное значение может быть 7680. |
| Gop | Integer | Нет | Интервал между I-кадрами (ключевыми кадрами), который можно настроить в кадрах или секундах. Диапазон значений GOP: 0 и [1, 100000]. Если этот параметр равен 0 или не заполнен, система автоматически установит длину GOP. |
| GopUnit | String | Нет | Единица значения GOP. Необязательные значения: frame: указывает кадр second: указывает секунду Значение по умолчанию: frame Примечание: Это поле может возвращать null, указывая, что допустимое значение недоступно. |
| FillType | String | Нет | Метод заполнения. Когда параметры ширины и высоты конфигурации видеопотока несовместимы с соотношением сторон исходного видео, метод обработки транскодирования — это "заполнение". Необязательный метод заполнения: stretch: Растянуть. Снимок экрана будет растянут кадр за кадром, чтобы соответствовать соотношению сторон исходного видео, что может сделать снимок экрана "короче" или "длиннее";black: Заполнить черным. Этот параметр сохраняет соотношение сторон исходного видео для снимка экрана и заполняет несоответствующую область черными блоками.white: Заполнить белым. Этот параметр сохраняет соотношение сторон исходного видео для снимка экрана и заполняет несоответствующую область белыми блоками.gauss: применяет размытие по Гауссу к некрытой области без изменения соотношения сторон изображения. smarttailor: Видеоизображения интеллектуально выбираются, чтобы обеспечить пропорциональное обрезание изображения. Значение по умолчанию: black. |
| Vcrf | Integer | Нет | Указывает коэффициент управления с постоянным битрейтом для видео. Диапазон значений: [0, 51]. Если этот параметр не заполнен, он устанавливается как "Автоматический". Рекомендуется не указывать этот параметр, если это не требуется. Если параметр Mode установлен на VBR и значение Vcrf также сконфигурировано, MPS будет обрабатывать видео в режиме VBR, учитывая оба параметра Vcrf и Bitrate для баланса качества видео, битрейта, эффективности транскодирования и размера файла. Если параметр Mode установлен на CRF, параметр Bitrate будет недействителен, и кодирование будет основано на значении Vcrf. Если параметр Mode установлен на ABR или CBR, значение Vcrf не требуется конфигурирования. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| HlsTime | Integer | Нет | Средняя длительность сегмента. Диапазон значений: (0-10], единица: секунда. Если оставить пусто, будет использоваться автоматический выбор, который автоматически выбирает соответствующую длительность сегмента на основе параметров видео, таких как GOP. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| SegmentType | Integer | Нет | Тип сегмента HLS. Допустимые значения: 0: сегмент HLS+TS2: диапазон байтов HLS+TS7: сегмент HLS+MP45: диапазон байтов HLS+MP4 Значение по умолчанию: 0 Примечание: Это поле используется для параметров обычного/TSC транскодирования и не применяется к адаптивному потоковому вещанию с переменным битрейтом. Чтобы настроить тип сегмента для адаптивного потокового вещания с переменным битрейтом, используйте внешнее поле. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| FpsDenominator | Integer | Нет | Знаменатель частоты кадров. Примечание: Значение должно быть больше 0. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| Stereo3dType | String | Нет | Режим сращивания 3D видео, применимо только к mv-hevc и эффективно для 3D видео. допустимые значения: side_by_side: исходное содержимое видео расположено в левостороннем макете.top_bottom: вертикальное расположение исходного содержимого видео. Отправка количества и стоимости на основе размера сегментированного разрешения. Значение по умолчанию: side_by_side. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| VideoProfile | String | Нет | Профиль, подходящий для различных сценариев. baseline: Поддерживает только I/P-кадры и неперемешанные сценарии, подходящие для сценариев, таких как видеозвонки и мобильные видео. main: Предлагает I-кадры, P-кадры и B-кадры, поддерживает как перемешанные, так и неперемешанные режимы. Главным образом используется в основных продуктах потребления аудио и видео, таких как видеопроигрыватели и устройства трансляции потокового видео. high: наивысший уровень кодирования с предсказанием 8x8, добавленным в основной профиль, и поддержкой пользовательского квантования. Широко используется в сценариях, таких как хранилище Blu-ray и HDTV. default: автоматическое заполнение в соответствии с исходным видео. Эта конфигурация появляется только, когда стандарт кодирования установлен на H264. Поддерживаются baseline/main/high. Значение по умолчанию: default Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| VideoLevel | String | Нет | Уровень кодировщика. Значение по умолчанию: auto ("") Если стандарт кодирования установлен на H264, поддерживаются следующие параметры: "", 1, 1.1, 1.2, 1.3, 2, 2.1, 2.2, 3, 3.1, 3.2, 4, 4.1, 4.2, 5 и 5.1. Если стандарт кодирования установлен на H265, поддерживаются следующие параметры: "", 1, 2, 2.1, 3, 3.1, 4, 4.1, 5, 5.1, 5.2, 6, 6.1, 6.2 и 8.5. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| Bframes | Integer | Нет | Количество B-кадров между опорными кадрами. Значение по умолчанию — автоматическое, поддерживается диапазон 0–16. Примечание: Если оставить пусто, будет использоваться автоматический параметр. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| Mode | String | Нет | Режим управления битрейтом. Необязательные значения: VBR: переменный битрейт. Выходной битрейт регулируется на основе сложности видеоизображения, обеспечивая более высокое качество изображения. Этот режим подходит для сценариев хранилища, а также приложений с высокими требованиями к качеству изображения. ABR: средний битрейт. Средний битрейт выходного видео в максимальной степени остается стабильным, но допускаются кратковременные колебания битрейта. Этот режим подходит для сценариев, когда необходимо минимизировать общий битрейт при сохранении определенного качества. CBR: постоянный битрейт. Выходной битрейт остается постоянным в процессе кодирования видео, независимо от изменений сложности изображения. Этот режим подходит для сценариев со строгими требованиями к пропускной способности сети, таких как потоковое вещание. VCRF: коэффициент постоянного качества. Качество видео контролируется установкой коэффициента качества, достигая кодирования видео с постоянным качеством. Битрейт автоматически регулируется на основе сложности содержимого. Этот режим подходит для сценариев, когда желательно сохранить определенное качество. По умолчанию выбран VBR. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| Sar | String | Нет | Соотношение сторон отображения. Необязательные значения: [1:1, 2:1, default] Значение по умолчанию: default Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| NoScenecut | Integer | Нет | Адаптивное решение I-кадра. Когда это включено, Media Processing Service будет автоматически определять точки перехода между различными сценариями в видео (обычно это визуально отличные кадры, такие как переключение между одним кадром и другим) и адаптивно вставлять ключевые кадры (I-кадры) в эти точки для улучшения случайной доступности и эффективности кодирования видео. Необязательные значения: 0: отключить адаптивное решение I-кадра 1: включить адаптивное решение I-кадра Значение по умолчанию: 0 Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| BitDepth | Integer | Нет | Бит: поддерживаются 8/10. Значение по умолчанию: 8 Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| RawPts | Integer | Нет | Сохранение исходной временной метки. Необязательные значения: 0: Отключено 1: Включено Значение по умолчанию: Отключено Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| Compress | Integer | Нет | Пропорциональное сжатие битрейта. Когда это включено, битрейт выходного видео будет отрегулирован в соответствии с пропорцией. После введения коэффициента сжатия система автоматически вычислит целевой выходной битрейт на основе исходного битрейта видео. Диапазон коэффициента сжатия: 0-100 Если это значение не заполнено, это означает, что оно не включено по умолчанию. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| SegmentSpecificInfo | [SegmentSpecificInfo](#SegmentSpecificInfo) | Нет | Длительность сегмента при запуске. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| ScenarioBased | Integer | Нет | Включает ли шаблон параметры на основе сценариев. 0: отключить. 1: включить Значение по умолчанию: 0 Примечание: Значения полей SceneType и CompressType вступают в силу только когда значение этого поля равно 1. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| SceneType | String | Нет | Сценарий видео. Допустимые значения: - normal: Общий сценарий транскодирования. Сценарий общего транскодирования и сжатия. - pgc: PGC HD телепередачи и фильмы. При сжатии основное внимание уделяется опыту просмотра телепередач и фильмов, а кодирование ROI выполняется в соответствии с их характеристиками, при этом сохраняется высокое качество видео и аудио. - materials_video: HD материалы. Сценарий, связанный с материальными ресурсами, где требования к качеству изображения чрезвычайно высоки и много прозрачных изображений с почти нулевой потерей визуальной информации при сжатии. - ugc: Содержимое UGC. Подходит для широкого спектра сценариев UGC/коротких видео с оптимизированным битрейтом кодирования для характеристик коротких видео, улучшенным качеством изображения и улучшенными метриками QOS/QOE бизнеса. - e-commerce_video. Модное шоу/электронная коммерция: При сжатии акцент делается на четкость деталей и улучшение ROI, с особым вниманием к сохранению качества изображения области лица. - educational_video. Образование. При сжатии акцент делается на четкость и читаемость текста и изображений, чтобы помочь студентам лучше понять содержание, обеспечивая ясное передачу учебного содержимого. Значение по умолчанию: normal. Примечание: Чтобы использовать это значение, значение ScenarioBased должно быть 1; в противном случае это значение не вступит в силу. Примечание: Это поле может возвращать null, указывая, что допустимые значения недоступны. |
| CompressType | String | Нет | Политика транскодирования. Допустимые значения: - ultra_compress: Экстремальное сжатие. По сравнению со стандартным сжатием, эта политика может максимизировать

## VolumeBalanceConfig

Конфигурация выравнивания громкости.

Используется действиями: CreateTranscodeTemplate, ModifyTranscodeTemplate.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Switch | String | No | Включить или отключить функцию. Допустимые значения: `ON``OFF`  Значение по умолчанию: `ON`. |
| Type | String | No | Тип. Допустимые значения: `loudNorm`: Нормализация громкости.`gainControl`: Выравнивание уровня громкости. Значение по умолчанию: `loudNorm`. Примечание. Это поле может быть пустым, что означает отсутствие допустимых значений. |

## WatermarkInput

Параметры водяного знака для использования в задаче обработки медиа.

Используется действиями: CreateWorkflow, ProcessMedia, ResetWorkflow.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Definition | Integer | Yes | ID шаблона водяного знака. |
| RawParameter | [RawWatermarkParameter](#RawWatermarkParameter) | No | Пользовательский параметр водяного знака, допустимый если `Definition` равен 0. Этот параметр используется в высокоспециализированных сценариях. Рекомендуется в первую очередь использовать `Definition` для указания параметра водяного знака. Пользовательский параметр водяного знака недоступен для скриншотов. |
| TextContent | String | No | Текстовое содержимое длиной до 100 символов. Это поле требуется только если тип водяного знака — текст. Текстовый водяной знак недоступен для скриншотов. |
| SvgContent | String | No | Содержимое SVG длиной до 2 000 000 символов. Это поле требуется только если тип водяного знака — `SVG`. Водяной знак SVG недоступен для скриншотов. |
| StartTimeOffset | Float | No | Смещение времени начала водяного знака в секундах. Если не установлено или установлено значение 0, водяной знак начинает отображаться при начале видео. Если не установлено или установлено значение 0, водяной знак начинает отображаться при начале видео. Если значение больше 0 (например, n), водяной знак будет отображаться на n-й секунде видео. Если значение меньше 0 (например, -n), водяной знак будет отображаться за n секунд до конца видео.  Примечание. Используется только для видеосценариев. Скриншоты не поддерживаются. |
| EndTimeOffset | Float | No | Смещение времени окончания водяного знака в секундах. Если не установлено или установлено значение 0, водяной знак будет отображаться до конца видео. Если значение больше 0 (например, n), водяной знак исчезнет на n-й секунде. Если значение меньше 0 (например, -n), водяной знак исчезнет за n секунд до конца видео.  Примечание. Используется только для видеосценариев. Скриншоты не поддерживаются. |

## WatermarkTemplate

Детали шаблона водяного знака

Используется действиями: DescribeWatermarkTemplates.

| Name | Type | Description |
| --- | --- | --- |
| Definition | Integer | Уникальный ID шаблона водяного знака. |
| Type | String | Тип водяного знака. Допустимые значения: image: Графический водяной знак;text: Текстовый водяной знак. |
| Name | String | Название шаблона водяного знака. |
| Comment | String | Описание шаблона. |
| XPos | String | Горизонтальная позиция начальной точки изображения водяного знака относительно начальной точки видео. Если строка заканчивается на %, левый край водяного знака будет находиться на позиции указанного процента от ширины видео; например, `10%` означает, что левый край находится на 10% ширины видео. Если строка заканчивается на px, левый край водяного знака будет находиться на позиции указанного пикселя от ширины видео; например, `100px` означает, что левый край находится на позиции 100 пикселей. |
| YPos | String | Вертикальная позиция начальной точки изображения водяного знака относительно начальной точки видео. Если строка заканчивается на %, верхний край водяного знака будет находиться на позиции указанного процента от высоты видео; например, `10%` означает, что верхний край находится на 10% высоты видео. Если строка заканчивается на px, верхний край водяного знака будет находиться на позиции указанного пикселя от высоты видео; например, `100px` означает, что верхний край находится на позиции 100 пикселей. |
| ImageTemplate | [ImageWatermarkTemplate](#ImageWatermarkTemplate) | Шаблон графического водяного знака. Это поле действительно только если `Type` равен `image`. Примечание. Это поле может быть пустым, что означает отсутствие допустимых значений. |
| TextTemplate | [TextWatermarkTemplateInput](#TextWatermarkTemplateInput) | Шаблон текстового водяного знака. Это поле действительно только если `Type` равен `text`. Примечание. Это поле может быть пустым, что означает отсутствие допустимых значений. |
| SvgTemplate | [SvgWatermarkInput](#SvgWatermarkInput) | Шаблон водяного знака SVG. Это поле действительно если `Type` равен `svg`. Примечание. Это поле может быть пустым, что означает отсутствие допустимых значений. |
| CreateTime | String | Время создания шаблона в [формате ISO](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |
| UpdateTime | String | Время последнего изменения шаблона в [формате ISO](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |
| CoordinateOrigin | String | Позиция начальной точки. Допустимые значения: TopLeft: Координатная система начинается в левом верхнем углу видеоизображения, а начальная точка водяного знака находится в левом верхнем углу изображения или текста. TopRight: Координатная система начинается в правом верхнем углу видеоизображения, а начальная точка водяного знака находится в правом верхнем углу изображения или текста. BottomLeft: Координатная система начинается в левом нижнем углу видеоизображения, а начальная точка водяного знака находится в левом нижнем углу изображения или текста. BottomRight: Координатная система начинается в правом нижнем углу видеоизображения, а начальная точка водяного знака находится в правом нижнем углу изображения или текста. |

## WordResult

Информация о слове.

Используется действиями: DescribeBatchTaskDetail, DescribeTaskDetail, ParseNotification, RecognizeAudio.

| Name | Type | Description |
| --- | --- | --- |
| Word | String | Текст слова. |
| Start | Float | Временная метка начала слова в секундах. |
| End | Float | Временная метка окончания слова в секундах. |
| Trans | String | Текст после перевода. |

## WorkflowInfo

Детали информации о рабочем процессе.

Используется действиями: DescribeWorkflows.

| Name | Type | Description |
| --- | --- | --- |
| WorkflowId | Integer | ID рабочего процесса. |
| WorkflowName | String | Имя рабочего процесса. |
| Status | String | Статус рабочего процесса. Допустимые значения: Enabled: Включен, Disabled: Отключен. |
| Trigger | [WorkflowTrigger](#WorkflowTrigger) | Входное правило, связанное с рабочим процессом. Если загруженное видео соответствует правилу объекта, рабочий процесс будет запущен. |
| OutputStorage | [TaskOutputStorage](#TaskOutputStorage) | Место для сохранения файла с результатом обработки медиа. Примечание. Это поле может быть пустым, что означает отсутствие допустимого значения. |
| MediaProcessTask | [MediaProcessTaskInput](#MediaProcessTaskInput) | Параметры обработки медиа для использования. Примечание. Это поле может быть пустым, что означает отсутствие допустимого значения. |
| AiContentReviewTask | [AiContentReviewTaskInput](#AiContentReviewTaskInput) | Параметр типа задачи аудита содержимого видео. Примечание. Это поле может быть пустым, что означает отсутствие допустимых значений. |
| AiAnalysisTask | [AiAnalysisTaskInput](#AiAnalysisTaskInput) | Параметр задачи анализа содержимого видео. |
| AiRecognitionTask | [AiRecognitionTaskInput](#AiRecognitionTaskInput) | Параметр типа задачи распознавания содержимого видео. Примечание. Это поле может быть пустым, что означает отсутствие допустимых значений. |
| TaskNotifyConfig | [TaskNotifyConfig](#TaskNotifyConfig) | Информация уведомления о событии задачи. Если этот параметр остается пустым, уведомления о событиях не будут получены. Примечание. Это поле может быть пустым, что означает отсутствие допустимых значений. |
| TaskPriority | Integer | Приоритет потока задач. Чем выше значение, тем выше приоритет. Диапазон значений: [-10, 10]. Если этот параметр остается пустым, будет использовано значение 0. |
| OutputDir | String | Каталог для сохранения файла с результатом обработки медиа, например `/movie/201907/`. |
| CreateTime | String | Время создания рабочего процесса в [формате ISO](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |
| UpdateTime | String | Время последнего изменения рабочего процесса в [формате ISO](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F). |

## WorkflowTask

Информация о задаче обработки медиа.

Используется действиями: DescribeTaskDetail, ParseNotification.

| Name | Type | Description |
| --- | --- | --- |
| TaskId | String | ID задачи обработки медиа. |
| Status | String | Статус потока задач. Допустимые значения: PROCESSING: Обработка;FINISH: Завершено. |
| ErrCode | Integer | Если возвращаемое значение не равно 0, произошла ошибка источника. Если возвращено 0, обратитесь к кодам ошибок соответствующего типа задачи. |
| Message | String | Кроме ошибок источника, сообщения об ошибках различаются в зависимости от типа задачи. |
| InputInfo | [MediaInputInfo](#MediaInputInfo) | Информация о обработанном файле. Примечание. Это поле может быть пустым, что означает отсутствие допустимого значения. |
| MetaData | [MediaMetaData](#MediaMetaData) | Метаданные исходного видео. Примечание. Это поле может быть пустым, что означает отсутствие допустимых значений. |
| MediaProcessResultSet | Array of [MediaProcessTaskResult](#MediaProcessTaskResult) | Статус выполнения и результат задачи обработки медиа. |
| AiContentReviewResultSet | Array of [AiContentReviewResult](#AiContentReviewResult) | Статус выполнения и результат задачи аудита содержимого видео. |
| AiAnalysisResultSet | Array of [AiAnalysisResult](#AiAnalysisResult) | Статус выполнения и результат задачи анализа содержимого видео. |
| AiRecognitionResultSet | Array of [AiRecognitionResult](#AiRecognitionResult) | Статус выполнения и результат задачи распознавания содержимого видео. |
| AiQualityControlTaskResult | [ScheduleQualityControlTaskResult](#ScheduleQualityControlTaskResult) | Статус выполнения и результаты задачи проверки качества медиа. Примечание. Это поле может быть пустым, что означает отсутствие допустимых значений. |
| SmartSubtitlesTaskResult | Array of [SmartSubtitlesResult](#SmartSubtitlesResult) | Результат выполнения задачи интеллектуального создания субтитров. Примечание. Это поле может быть пустым, что означает отсутствие допустимого значения. |
| SmartEraseTaskResult | [SmartEraseTaskResult](#SmartEraseTaskResult) | Результат выполнения задачи интеллектуального удаления. Примечание. Это поле может быть пустым, что означает отсутствие допустимого значения. |

## WorkflowTrigger

Входное правило. Если загруженное видео соответствует правилу, рабочий процесс будет запущен.

Используется действиями: CreateSchedule, CreateWorkflow, DescribeSchedules, DescribeWorkflows, ModifySchedule, ResetWorkflow.

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Type | String | Yes | Тип триггера. Допустимые значения: `CosFileUpload`: Триггер Tencent Cloud COS.`AwsS3FileUpload`: Триггер AWS S3. В настоящее время этот тип поддерживается только для задач транскодирования и схем (не поддерживается для рабочих процессов). |
| CosFileUploadTrigger | [CosFileUploadTrigger](#CosFileUploadTrigger) | No | Этот параметр требуется и действителен когда `Type` равен `CosFileUpload`, указывая правило триггера COS. Примечание. Это поле может быть пустым, что означает отсутствие допустимых значений. |
| AwsS3FileUploadTrigger | [AwsS3FileUploadTrigger](#AwsS3FileUploadTrigger) | No | Триггер AWS S3. Этот параметр действителен и требуется если `Type` равен `AwsS3FileUpload`.  Примечание. В настоящее время ключ для bucket AWS S3, очередь триггера SQS и очередь обратного вызова SQS должны быть одинаковыми. Примечание. Это поле может быть пустым, что означает отсутствие допустимых значений. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33690](https://www.tencentcloud.com/document/product/1041/33690)*

---
*Источник (EN): [data-types.md](./data-types.md)*

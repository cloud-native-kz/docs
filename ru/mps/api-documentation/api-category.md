# Категория API

## API-интерфейсы для инициирования задач обработки

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [BatchProcessMedia](https://www.tencentcloud.com/document/api/1041/70403) | Вводит несколько URL-адресов видео и инициирует несколько задач | 20 |
| [ProcessMedia](https://www.tencentcloud.com/document/api/1041/33640) | Запускает задачу обработки медиа | 100 |
| [ProcessLiveStream](https://www.tencentcloud.com/document/api/1041/33641) | Инициирует задачу обработки потока в прямом эфире | 100 |
| [ProcessImage](https://www.tencentcloud.com/document/api/1041/66929) | Инициирует обработку изображения | 20 |
| [EditMedia](https://www.tencentcloud.com/document/api/1041/37460) | Редактирует видео | 20 |
| [DescribeMediaMetaData](https://www.tencentcloud.com/document/api/1041/37461) | Получает метаданные медиа | 20 |
| [ExtractBlindWatermark](https://www.tencentcloud.com/document/api/1041/74705) | Извлекает цифровой водяной знак видео | 20 |
| [RecognizeAudio](https://www.tencentcloud.com/document/api/1041/77359) | Распознает аудио | 5 |
| [SyncDubbing](https://www.tencentcloud.com/document/api/1041/77775) | Синхронно генерирует дубляж | 20 |

## API-интерфейсы управления задачами

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [DescribeBatchTaskDetail](https://www.tencentcloud.com/document/api/1041/70402) | Запрашивает подробные сведения о задаче с несколькими входными данными | 20 |
| [DescribeTaskDetail](https://www.tencentcloud.com/document/api/1041/33644) | Запрашивает сведения о задаче | 100 |
| [DescribeTasks](https://www.tencentcloud.com/document/api/1041/33643) | Получает список задач | 100 |
| [ManageTask](https://www.tencentcloud.com/document/api/1041/37462) | Управляет задачей | 20 |
| [DescribeImageTaskDetail](https://www.tencentcloud.com/document/api/1041/70401) | Запрашивает подробные сведения о задаче обработки изображения | 100 |

## API-интерфейсы шаблонов транскодирования и улучшения

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [CreateTranscodeTemplate](https://www.tencentcloud.com/document/api/1041/33671) | Создает шаблон транскодирования | 100 |
| [CreateAdaptiveDynamicStreamingTemplate](https://www.tencentcloud.com/document/api/1041/37469) | Создает шаблоны адаптивной потоковой передачи | 20 |
| [DeleteTranscodeTemplate](https://www.tencentcloud.com/document/api/1041/33663) | Удаляет шаблон транскодирования | 100 |
| [DeleteAdaptiveDynamicStreamingTemplate](https://www.tencentcloud.com/document/api/1041/37467) | Удаляет шаблон адаптивной потоковой передачи | 20 |
| [DescribeTranscodeTemplates](https://www.tencentcloud.com/document/api/1041/33655) | Получает список шаблонов транскодирования | 100 |
| [DescribeAdaptiveDynamicStreamingTemplates](https://www.tencentcloud.com/document/api/1041/37465) | Получает список шаблонов адаптивной потоковой передачи | 20 |
| [ModifyTranscodeTemplate](https://www.tencentcloud.com/document/api/1041/33647) | Изменяет шаблон транскодирования | 100 |
| [ModifyAdaptiveDynamicStreamingTemplate](https://www.tencentcloud.com/document/api/1041/37463) | Изменяет шаблон адаптивной потоковой передачи | 20 |

## API-интерфейсы шаблонов водяных знаков

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [CreateBlindWatermarkTemplate](https://www.tencentcloud.com/document/api/1041/74704) | Создает шаблон цифрового водяного знака | 20 |
| [CreateWatermarkTemplate](https://www.tencentcloud.com/document/api/1041/33670) | Создает шаблон нанесения водяного знака | 100 |
| [DeleteBlindWatermarkTemplate](https://www.tencentcloud.com/document/api/1041/74703) | Удаляет шаблон цифрового водяного знака | 20 |
| [DeleteWatermarkTemplate](https://www.tencentcloud.com/document/api/1041/33662) | Удаляет шаблон нанесения водяного знака | 100 |
| [DescribeBlindWatermarkTemplates](https://www.tencentcloud.com/document/api/1041/74702) | Получает список шаблонов цифровых водяных знаков | 20 |
| [DescribeWatermarkTemplates](https://www.tencentcloud.com/document/api/1041/33654) | Получает список шаблонов нанесения водяных знаков | 100 |
| [ModifyBlindWatermarkTemplate](https://www.tencentcloud.com/document/api/1041/74701) | Изменяет шаблон цифрового водяного знака | 20 |
| [ModifyWatermarkTemplate](https://www.tencentcloud.com/document/api/1041/33646) | Изменяет шаблон нанесения водяного знака | 100 |

## API-интерфейсы шаблонов снимков экрана

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [CreateAnimatedGraphicsTemplate](https://www.tencentcloud.com/document/api/1041/33676) | Создает шаблон генерирования анимированных изображений | 100 |
| [CreateSnapshotByTimeOffsetTemplate](https://www.tencentcloud.com/document/api/1041/33672) | Создает шаблон захвата скриншота по временной точке | 100 |
| [CreateSampleSnapshotTemplate](https://www.tencentcloud.com/document/api/1041/33673) | Создает шаблон выборочного захвата скриншота | 100 |
| [CreateImageSpriteTemplate](https://www.tencentcloud.com/document/api/1041/33674) | Создает шаблон генерирования спрайта изображения | 100 |
| [DeleteAnimatedGraphicsTemplate](https://www.tencentcloud.com/document/api/1041/33668) | Удаляет шаблон генерирования анимированных изображений | 100 |
| [DeleteSnapshotByTimeOffsetTemplate](https://www.tencentcloud.com/document/api/1041/33664) | Удаляет шаблон захвата скриншота по временной точке | 100 |
| [DeleteSampleSnapshotTemplate](https://www.tencentcloud.com/document/api/1041/33665) | Удаляет шаблон выборочного захвата скриншота | 100 |
| [DeleteImageSpriteTemplate](https://www.tencentcloud.com/document/api/1041/33666) | Удаляет шаблон генерирования спрайта изображения | 100 |
| [DescribeAnimatedGraphicsTemplates](https://www.tencentcloud.com/document/api/1041/33660) | Получает список шаблонов генерирования анимированных изображений | 100 |
| [DescribeSnapshotByTimeOffsetTemplates](https://www.tencentcloud.com/document/api/1041/33656) | Получает список шаблонов захвата скриншота по временной точке | 100 |
| [DescribeSampleSnapshotTemplates](https://www.tencentcloud.com/document/api/1041/33657) | Получает список шаблонов выборочного захвата скриншота | 100 |
| [DescribeImageSpriteTemplates](https://www.tencentcloud.com/document/api/1041/33658) | Получает список шаблонов генерирования спрайта изображения | 100 |
| [ModifyAnimatedGraphicsTemplate](https://www.tencentcloud.com/document/api/1041/33652) | Изменяет шаблон генерирования анимированных изображений | 100 |
| [ModifySnapshotByTimeOffsetTemplate](https://www.tencentcloud.com/document/api/1041/33648) | Изменяет шаблон захвата скриншота по временной точке | 100 |
| [ModifySampleSnapshotTemplate](https://www.tencentcloud.com/document/api/1041/33649) | Изменяет шаблон выборочного захвата скриншота | 100 |
| [ModifyImageSpriteTemplate](https://www.tencentcloud.com/document/api/1041/33650) | Изменяет шаблон генерирования спрайта изображения | 100 |

## API-интерфейсы шаблонов AI для медиа

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [CreateSmartEraseTemplate](https://www.tencentcloud.com/document/api/1041/73667) | Создает шаблон интеллектуального удаления | 20 |
| [CreateSmartSubtitleTemplate](https://www.tencentcloud.com/document/api/1041/68919) | Создает шаблон интеллектуальных субтитров | 20 |
| [CreateContentReviewTemplate](https://www.tencentcloud.com/document/api/1041/33675) | Создает шаблон модерации контента | 10 |
| [CreateAIAnalysisTemplate](https://www.tencentcloud.com/document/api/1041/37470) | Создает шаблон анализа контента | 10 |
| [CreateAIRecognitionTemplate](https://www.tencentcloud.com/document/api/1041/33677) | Создает шаблон распознавания контента | 10 |
| [DeleteSmartEraseTemplate](https://www.tencentcloud.com/document/api/1041/73666) | Удаляет шаблон интеллектуального удаления | 20 |
| [DeleteSmartSubtitleTemplate](https://www.tencentcloud.com/document/api/1041/68918) | Удаляет шаблон интеллектуальных субтитров | 20 |
| [DeleteContentReviewTemplate](https://www.tencentcloud.com/document/api/1041/33667) | Удаляет шаблон модерации контента | 10 |
| [DeleteAIAnalysisTemplate](https://www.tencentcloud.com/document/api/1041/37468) | Удаляет шаблон анализа контента | 10 |
| [DeleteAIRecognitionTemplate](https://www.tencentcloud.com/document/api/1041/33669) | Удаляет шаблон распознавания контента | 10 |
| [DescribeSmartEraseTemplates](https://www.tencentcloud.com/document/api/1041/73665) | Получает список шаблонов интеллектуального удаления | 20 |
| [DescribeSmartSubtitleTemplates](https://www.tencentcloud.com/document/api/1041/68917) | Получает список шаблонов интеллектуальных субтитров | 20 |
| [DescribeContentReviewTemplates](https://www.tencentcloud.com/document/api/1041/33659) | Запрашивает шаблоны модерации контента | 10 |
| [DescribeAIAnalysisTemplates](https://www.tencentcloud.com/document/api/1041/37466) | Получает список шаблонов анализа контента | 10 |
| [DescribeAIRecognitionTemplates](https://www.tencentcloud.com/document/api/1041/33661) | Получает список шаблонов распознавания контента | 10 |
| [ModifySmartEraseTemplate](https://www.tencentcloud.com/document/api/1041/73664) | Изменяет шаблон интеллектуального удаления | 20 |
| [ModifySmartSubtitleTemplate](https://www.tencentcloud.com/document/api/1041/68916) | Изменяет шаблон интеллектуальных субтитров | 20 |
| [ModifyContentReviewTemplate](https://www.tencentcloud.com/document/api/1041/33651) | Изменяет шаблон модерации контента | 10 |
| [ModifyAIAnalysisTemplate](https://www.tencentcloud.com/document/api/1041/37464) | Изменяет шаблон анализа контента | 10 |
| [ModifyAIRecognitionTemplate](https://www.tencentcloud.com/document/api/1041/33653) | Изменяет шаблон распознавания контента | 10 |

## API-интерфейсы AI для медиа — управление словарём горячих слов

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [CreateAsrHotwords](https://www.tencentcloud.com/document/api/1041/68915) | Создает словарь горячих слов интеллектуальных субтитров | 20 |
| [DeleteAsrHotwords](https://www.tencentcloud.com/document/api/1041/68914) | Удаляет словарь горячих слов интеллектуальных субтитров | 20 |
| [DescribeAsrHotwords](https://www.tencentcloud.com/document/api/1041/68913) | Запрашивает сведения о словаре горячих слов интеллектуальных субтитров | 20 |
| [DescribeAsrHotwordsList](https://www.tencentcloud.com/document/api/1041/68912) | Запрашивает список словарей горячих слов интеллектуальных субтитров | 20 |
| [ModifyAsrHotwords](https://www.tencentcloud.com/document/api/1041/68911) | Изменяет словарь горячих слов интеллектуальных субтитров | 20 |

## API-интерфейсы AI для медиа — управление примерами

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [CreatePersonSample](https://www.tencentcloud.com/document/api/1041/33689) | Создает примеры изображений | 100 |
| [CreateWordSamples](https://www.tencentcloud.com/document/api/1041/33688) | Создает примеры ключевых слов | 100 |
| [DeletePersonSample](https://www.tencentcloud.com/document/api/1041/33687) | Удаляет примеры изображений | 100 |
| [DeleteWordSamples](https://www.tencentcloud.com/document/api/1041/33686) | Удаляет примеры ключевых слов | 100 |
| [DescribePersonSamples](https://www.tencentcloud.com/document/api/1041/33685) | Получает список примеров изображений | 100 |
| [DescribeWordSamples](https://www.tencentcloud.com/document/api/1041/33684) | Получает список примеров ключевых слов | 100 |
| [ModifyPersonSample](https://www.tencentcloud.com/document/api/1041/33683) | Изменяет примеры изображений | 100 |
| [ModifyWordSample](https://www.tencentcloud.com/document/api/1041/33682) | Изменяет пример ключевого слова | 100 |

## API-интерфейсы шаблонов проверки качества медиа

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [CreateQualityControlTemplate](https://www.tencentcloud.com/document/api/1041/64713) | Создает шаблон проверки качества медиа | 20 |
| [DeleteQualityControlTemplate](https://www.tencentcloud.com/document/api/1041/64712) | Удаляет шаблон проверки качества медиа | 20 |
| [DescribeQualityControlTemplates](https://www.tencentcloud.com/document/api/1041/64711) | Получает список шаблонов проверки качества медиа | 20 |
| [ModifyQualityControlTemplate](https://www.tencentcloud.com/document/api/1041/64710) | Изменяет шаблон проверки качества медиа | 20 |

## API-интерфейсы шаблонов записи потока в прямом эфире

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [CreateLiveRecordTemplate](https://www.tencentcloud.com/document/api/1041/67515) | Создает шаблон записи потока в прямом эфире | 20 |
| [DeleteLiveRecordTemplate](https://www.tencentcloud.com/document/api/1041/67514) | Удаляет шаблон записи потока в прямом эфире | 20 |
| [DescribeLiveRecordTemplates](https://www.tencentcloud.com/document/api/1041/67513) | Получает шаблон записи потока в прямом эфире | 20 |
| [ModifyLiveRecordTemplate](https://www.tencentcloud.com/document/api/1041/67512) | Изменяет шаблон записи потока в прямом эфире | 20 |

## API-интерфейсы управления оркестрацией

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [CreateSchedule](https://www.tencentcloud.com/document/api/1041/54035) | Создает схему | 20 |
| [CreateWorkflow](https://www.tencentcloud.com/document/api/1041/33638) | Создает рабочий процесс | 200 |
| [DeleteSchedule](https://www.tencentcloud.com/document/api/1041/54034) | Удаляет схему | 20 |
| [DeleteWorkflow](https://www.tencentcloud.com/document/api/1041/33637) | Удаляет рабочий процесс | 20 |
| [DescribeSchedules](https://www.tencentcloud.com/document/api/1041/54033) | Запрашивает схему | 20 |
| [DescribeWorkflows](https://www.tencentcloud.com/document/api/1041/33636) | Получает список рабочих процессов | 20 |
| [ModifySchedule](https://www.tencentcloud.com/document/api/1041/54030) | Изменяет схему | 20 |
| [ResetWorkflow](https://www.tencentcloud.com/document/api/1041/33633) | Сбрасывает рабочий процесс | 20 |
| [EnableSchedule](https://www.tencentcloud.com/document/api/1041/54031) | Включает схему | 20 |
| [EnableWorkflow](https://www.tencentcloud.com/document/api/1041/33634) | Включает рабочий процесс | 20 |
| [DisableSchedule](https://www.tencentcloud.com/document/api/1041/54032) | Отключает схему | 20 |
| [DisableWorkflow](https://www.tencentcloud.com/document/api/1041/33635) | Отключает рабочий процесс | 20 |

## API-интерфейсы статистики данных

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [DescribeUsageData](https://www.tencentcloud.com/document/api/1041/75556) | Запрашивает информацию об использовании | 100 |

## API-интерфейсы управления группой безопасности StreamLink

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [DescribeStreamLinkSecurityGroup](https://www.tencentcloud.com/document/api/1041/67844) | Запрашивает группу безопасности | 20 |

## Другие API-интерфейсы

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [ParseLiveStreamProcessNotification](https://www.tencentcloud.com/document/api/1041/33680) | Анализирует результат обработки потока в прямом эфире | 20 |
| [ParseNotification](https://www.tencentcloud.com/document/api/1041/33679) | Анализирует уведомление о событии | 20 |
| [ExecuteFunction](https://www.tencentcloud.com/document/api/1041/38515) | Запускает пользовательский API | 20 |
| [TextTranslation](https://www.tencentcloud.com/document/api/1041/75936) | Переводит текст | 5 |

## API-интерфейсы генерирования AI

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [CreateAigcImageTask](https://www.tencentcloud.com/document/api/1041/76488) | Создает задачу генерирования изображения AIGC | 20 |
| [CreateAigcVideoTask](https://www.tencentcloud.com/document/api/1041/76487) | Создает задачу генерирования видео AIGC | 10 |
| [DescribeAigcImageTask](https://www.tencentcloud.com/document/api/1041/76486) | Запрашивает задачу генерирования изображения AIGC | 20 |
| [DescribeAigcVideoTask](https://www.tencentcloud.com/document/api/1041/76485) | Запрашивает задачу генерирования видео AIGC | 50 |

## API-интерфейсы шаблонов обработки изображения

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [CreateProcessImageTemplate](https://www.tencentcloud.com/document/api/1041/74710) | Создает шаблон обработки изображения | 20 |
| [DeleteProcessImageTemplate](https://www.tencentcloud.com/document/api/1041/74709) | Удаляет шаблон обработки изображения | 20 |
| [DescribeProcessImageTemplates](https://www.tencentcloud.com/document/api/1041/74708) | Запрашивает список шаблонов обработки изображения | 20 |
| [ModifyProcessImageTemplate](https://www.tencentcloud.com/document/api/1041/74707) | Изменяет шаблон обработки изображения | 20 |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33625](https://www.tencentcloud.com/document/product/1041/33625)*

---
*Источник (EN): [api-category.md](./api-category.md)*

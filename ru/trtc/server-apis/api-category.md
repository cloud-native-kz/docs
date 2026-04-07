# Категория API

## API управления комнатами

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [RemoveUser](https://www.tencentcloud.com/document/api/647/34268) | Удаляет пользователя | 20 |
| [SetUserBlocked](https://www.tencentcloud.com/document/api/647/51289) | Отключает/включает аудио и видео пользователя | 20 |
| [SetUserBlockedByStrRoomId](https://www.tencentcloud.com/document/api/647/51288) | Отключает/включает аудио и видео пользователя (ID комнаты строкового типа) | 20 |
| [DismissRoom](https://www.tencentcloud.com/document/api/647/34269) | Закрывает комнату | 20 |
| [RemoveUserByStrRoomId](https://www.tencentcloud.com/document/api/647/39630) | Удаляет пользователя из комнаты (по ID комнаты строкового типа) | 20 |
| [DismissRoomByStrRoomId](https://www.tencentcloud.com/document/api/647/39631) | Закрывает комнату (по ID комнаты строкового типа) | 20 |

## API мониторинга качества вызовов

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [DescribeRoomInfo](https://www.tencentcloud.com/document/api/647/36754) | Запрашивает список комнат | 20 |
| [DescribeUnusualEvent](https://www.tencentcloud.com/document/api/647/37763) | Запрашивает аномальный опыт пользователей | 20 |
| [DescribeUserEvent](https://www.tencentcloud.com/document/api/647/37762) | Запрашивает события во время вызова | 20 |
| [DescribeCallDetailInfo](https://www.tencentcloud.com/document/api/647/55013) | Запрашивает список пользователей и метрики вызовов | 20 |
| [DescribeUserInfo](https://www.tencentcloud.com/document/api/647/39096) | Запрашивает список пользователей | 20 |
| [DescribeScaleInfo](https://www.tencentcloud.com/document/api/647/36758) | Запрашивает количество комнат и пользователей | 20 |

## API микширования потоков и ретрансляции

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [UpdatePublishCdnStream](https://www.tencentcloud.com/document/api/647/48245) | Изменяет параметры ретрансляции | 20 |
| [StartPublishCdnStream](https://www.tencentcloud.com/document/api/647/48247) | Запускает задачу ретрансляции | 20 |
| [StopPublishCdnStream](https://www.tencentcloud.com/document/api/647/48246) | Останавливает задачу ретрансляции | 20 |

## API облачной записи

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [DeleteCloudRecording](https://www.tencentcloud.com/document/api/647/46959) | Останавливает задачу облачной записи | 20 |
| [DescribeCloudRecording](https://www.tencentcloud.com/document/api/647/46958) | Запрашивает статус задачи записи | 20 |
| [CreateCloudRecording](https://www.tencentcloud.com/document/api/647/46960) | Запускает задачу облачной записи | 20 |
| [ModifyCloudRecording](https://www.tencentcloud.com/document/api/647/46957) | Изменяет задачу записи | 20 |

## API статистики использования

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [DescribeTrtcUsage](https://www.tencentcloud.com/document/api/647/54137) | Запрашивает продолжительность аудио/видео TRTC | 5 |
| [DescribeRecordingUsage](https://www.tencentcloud.com/document/api/647/54139) | Запрашивает использование записи TRTC | 5 |
| [DescribeMixTranscodingUsage](https://www.tencentcloud.com/document/api/647/54140) | Запрашивает использование On-Cloud MixTranscoding TRTC | 5 |
| [DescribeRelayUsage](https://www.tencentcloud.com/document/api/647/54138) | Запрашивает использование ретрансляции TRTC на CDN | 5 |
| [DescribeTrtcRoomUsage](https://www.tencentcloud.com/document/api/647/54327) | Запрашивает данные использования, сгруппированные по комнатам | - |

## API мониторинга данных

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [DescribeTRTCRealTimeScaleData](https://www.tencentcloud.com/document/api/647/58628) | Запрашивает панель мониторинга TRTC - масштаб мониторинга в реальном времени | 20 |
| [DescribeTRTCRealTimeQualityData](https://www.tencentcloud.com/document/api/647/58629) | Запрашивает панель мониторинга TRTC - качество мониторинга в реальном времени | 20 |
| [DescribeTRTCMarketScaleData](https://www.tencentcloud.com/document/api/647/58630) | Запрашивает панель мониторинга TRTC - метрики масштаба информационной панели | 20 |
| [DescribeTRTCMarketQualityData](https://www.tencentcloud.com/document/api/647/58631) | Запрашивает панель мониторинга TRTC - метрики качества информационной панели | 20 |

## API веб-записи

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [StartWebRecord](https://www.tencentcloud.com/document/api/647/72066) | Запускает задачу записи веб-страницы | 20 |
| [DescribeWebRecord](https://www.tencentcloud.com/document/api/647/72067) | Запрашивает статус задачи записи веб-страницы | 20 |
| [StopWebRecord](https://www.tencentcloud.com/document/api/647/72065) | Останавливает задачу записи веб-страницы | 20 |

## Интерфейс ретрансляции потока извлечения

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [StopStreamIngest](https://www.tencentcloud.com/document/api/647/57834) | Останавливает ретрансляцию потока извлечения | 20 |
| [DescribeStreamIngest](https://www.tencentcloud.com/document/api/647/57836) | Запрашивает задачу ретрансляции | 20 |
| [StartStreamIngest](https://www.tencentcloud.com/document/api/647/57835) | Запускает ретрансляцию потока извлечения | 20 |
| [UpdateStreamIngest](https://www.tencentcloud.com/document/api/647/63238) | Обновляет задачу ретрансляции | 20 |

## API сервисов ИИ

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [StartAIConversation](https://www.tencentcloud.com/document/api/647/64963) | Запускает задачу ИИ-беседы | 20 |
| [DescribeAIConversation](https://www.tencentcloud.com/document/api/647/64964) | Описывает ИИ-беседу | 20 |
| [StopAIConversation](https://www.tencentcloud.com/document/api/647/65296) | Останавливает задачу ИИ-беседы | 20 |
| [DescribeAITranscription](https://www.tencentcloud.com/document/api/647/64968) | Описывает транскрипцию ИИ | 20 |
| [StopAITranscription](https://www.tencentcloud.com/document/api/647/64966) | Останавливает задачу транскрипции ИИ | 20 |
| [ControlAIConversation](https://www.tencentcloud.com/document/api/647/64965) | Управляет ИИ-диалогом | 50 |
| [StartAITranscription](https://www.tencentcloud.com/document/api/647/64967) | Запускает задачу транскрипции ИИ | 50 |
| [UpdateAIConversation](https://www.tencentcloud.com/document/api/647/64962) | Обновляет задачу ИИ-беседы | 20 |

## API облачной нарезки

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [CreateCloudSliceTask](https://www.tencentcloud.com/document/api/647/72331) | Создает задачу облачной нарезки | 20 |
| [DeleteCloudSliceTask](https://www.tencentcloud.com/document/api/647/72330) | Останавливает задачу облачной нарезки | 20 |
| [DescribeCloudSliceTask](https://www.tencentcloud.com/document/api/647/72329) | Запрашивает информацию о задачах облачной нарезки | 20 |
| [ModifyCloudSliceTask](https://www.tencentcloud.com/document/api/647/72328) | Изменяет задачу облачной нарезки | 20 |

## API облачной модерации

| Имя API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [DeleteCloudModeration](https://www.tencentcloud.com/document/api/647/72647) | Останавливает облачную модерацию | 20 |
| [DescribeCloudModeration](https://www.tencentcloud.com/document/api/647/72646) | Запрашивает информацию облачной модерации | 20 |
| [ModifyCloudModeration](https://www.tencentcloud.com/document/api/647/72645) | Изменяет задачи облачной модерации | 20 |
| [CreateCloudModeration](https://www.tencentcloud.com/document/api/647/72648) | Создает задачи облачной модерации | 20 |


---
*Источник: [https://trtc.io/document/34260](https://trtc.io/document/34260)*

---
*Источник (EN): [api-category.md](./api-category.md)*

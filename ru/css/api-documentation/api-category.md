# Категория API

## API Live Pad

| Название API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [CreateLivePadTemplate](https://www.tencentcloud.com/document/api/267/71831) | создание шаблона live pad | 20 |
| [CreateLivePadRule](https://www.tencentcloud.com/document/api/267/71832) | создание правила live pad | 20 |
| [StartLivePadStream](https://www.tencentcloud.com/document/api/267/70664) | StartLivePadStream | 20 |
| [StopLivePadStream](https://www.tencentcloud.com/document/api/267/71611) | StopLivePadStream | 20 |

## API трансляции LVB

| Название API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [DeleteLiveTranscodeRule](https://www.tencentcloud.com/document/api/267/30789) | Удаляет правило трансляции | 200 |
| [DeleteLiveTranscodeTemplate](https://www.tencentcloud.com/document/api/267/30788) | Удаляет шаблон трансляции | 200 |
| [DescribeLiveTranscodeRules](https://www.tencentcloud.com/document/api/267/30787) | Получает список правил трансляции | 500 |
| [DescribeLiveTranscodeTemplate](https://www.tencentcloud.com/document/api/267/30786) | Получает один шаблон трансляции | 500 |
| [DescribeLiveTranscodeTemplates](https://www.tencentcloud.com/document/api/267/30785) | Получает список шаблонов трансляции | 500 |
| [CreateLiveTranscodeTemplate](https://www.tencentcloud.com/document/api/267/30790) | Создание шаблона трансляции | 200 |
| [ModifyLiveTranscodeTemplate](https://www.tencentcloud.com/document/api/267/30784) | Изменяет конфигурацию шаблона трансляции | 200 |
| [CreateLiveTranscodeRule](https://www.tencentcloud.com/document/api/267/30791) | Создает правило трансляции | 200 |

## API управления отложенным воспроизведением

| Название API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [DescribeLiveDelayInfoList](https://www.tencentcloud.com/document/api/267/33532) | Получает список отложенных воспроизведений. | 500 |
| [ResumeDelayLiveStream](https://www.tencentcloud.com/document/api/267/30849) | Отменяет задержку прямой трансляции | 200 |
| [AddDelayLiveStream](https://www.tencentcloud.com/document/api/267/30850) | Устанавливает задержку прямой трансляции | 200 |

## API управления доменами

| Название API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [AddLiveDomain](https://www.tencentcloud.com/document/api/267/35189) | Добавляет доменное имя | 100 |
| [AuthenticateDomainOwner](https://www.tencentcloud.com/document/api/267/50612) | Проверяет права собственности на домен | 20 |
| [DeleteLiveDomain](https://www.tencentcloud.com/document/api/267/35188) | Удаляет доменное имя | 100 |
| [DescribeLiveDomain](https://www.tencentcloud.com/document/api/267/35187) | Запрашивает информацию о доменном имени | 500 |
| [DescribeLiveDomains](https://www.tencentcloud.com/document/api/267/35186) | Запрашивает список доменных имен | 200 |
| [EnableLiveDomain](https://www.tencentcloud.com/document/api/267/35185) | Включает доменное имя | 100 |
| [ForbidLiveDomain](https://www.tencentcloud.com/document/api/267/35184) | Отключает доменное имя | 100 |
| [ModifyLivePlayDomain](https://www.tencentcloud.com/document/api/267/35183) | Изменяет доменное имя воспроизведения | 200 |

## API управления водяными знаками

| Название API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [AddLiveWatermark](https://www.tencentcloud.com/document/api/267/30826) | Добавляет водяной знак | 100 |
| [CreateLiveWatermarkRule](https://www.tencentcloud.com/document/api/267/30825) | Создает правило добавления водяного знака | 200 |
| [DeleteLiveWatermark](https://www.tencentcloud.com/document/api/267/30824) | Удаляет водяной знак | 100 |
| [DeleteLiveWatermarkRule](https://www.tencentcloud.com/document/api/267/30823) | Удаляет правило добавления водяного знака | 200 |
| [DescribeLiveWatermark](https://www.tencentcloud.com/document/api/267/30822) | Получает информацию об одном водяном знаке | 500 |
| [DescribeLiveWatermarkRules](https://www.tencentcloud.com/document/api/267/30821) | Получает список правил добавления водяного знака | 500 |
| [DescribeLiveWatermarks](https://www.tencentcloud.com/document/api/267/30820) | Запрашивает список водяных знаков | 500 |
| [UpdateLiveWatermark](https://www.tencentcloud.com/document/api/267/30818) | Обновляет водяной знак | 100 |

## API управления сертификатами

| Название API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [DescribeLiveCert](https://www.tencentcloud.com/document/api/267/30779) | Получает информацию о сертификате | 500 |
| [DescribeLiveCerts](https://www.tencentcloud.com/document/api/267/30778) | Получает список информации о сертификатах | 500 |
| [DescribeLiveDomainCert](https://www.tencentcloud.com/document/api/267/30777) | Получает информацию о сертификате доменного имени | 500 |
| [DescribeLiveDomainCertBindings](https://www.tencentcloud.com/document/api/267/49645) | Запрашивает домены, связанные с сертификатами | 20 |
| [ModifyLiveDomainCertBindings](https://www.tencentcloud.com/document/api/267/49644) | Привязывает сертификат к нескольким доменам воспроизведения | 20 |
| [UnBindLiveDomainCert](https://www.tencentcloud.com/document/api/267/30774) | Отвязывает сертификат доменного имени | 200 |

## API микширования потоков прямой трансляции

| Название API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [CancelCommonMixStream](https://www.tencentcloud.com/document/api/267/35998) | Отменяет общее микширование потоков | 100 |
| [CreateCommonMixStream](https://www.tencentcloud.com/document/api/267/35997) | Создает общее микширование потоков | 200 |

## API извлечения потоков

| Название API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [DeleteLivePullStreamTask](https://www.tencentcloud.com/document/api/267/48356) | Удаляет задачу извлечения потока | 50 |
| [DescribeLivePullStreamTasks](https://www.tencentcloud.com/document/api/267/48355) | Запрашивает задачи извлечения потоков | 30 |
| [RestartLivePullStreamTask](https://www.tencentcloud.com/document/api/267/56967) | RestartLivePullStreamTask | 20 |
| [CreateLivePullStreamTask](https://www.tencentcloud.com/document/api/267/48357) | Создает задачу извлечения потока | 50 |
| [ModifyLivePullStreamTask](https://www.tencentcloud.com/document/api/267/48354) | Изменяет задачу извлечения потока | 20 |

## API управления записью

| Название API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [CreateLiveRecord](https://www.tencentcloud.com/document/api/267/30847) | Создает задачу записи (устарело; используйте новый API) | 500 |
| [CreateLiveRecordRule](https://www.tencentcloud.com/document/api/267/30846) | Создает правило записи | 200 |
| [CreateLiveRecordTemplate](https://www.tencentcloud.com/document/api/267/30845) | Создает шаблон записи | 200 |
| [CreateRecordTask](https://www.tencentcloud.com/document/api/267/37309) | Создает задачу записи (новый) | 20 |
| [DeleteLiveRecord](https://www.tencentcloud.com/document/api/267/30844) | Удаляет задачу записи (устарело; используйте новый API) | 200 |
| [DeleteLiveRecordRule](https://www.tencentcloud.com/document/api/267/30843) | Удаляет правило записи | 200 |
| [DeleteLiveRecordTemplate](https://www.tencentcloud.com/document/api/267/30842) | Удаляет шаблон записи. | 200 |
| [DeleteRecordTask](https://www.tencentcloud.com/document/api/267/37308) | Удаляет задачу записи (новый) | 20 |
| [DescribeLiveRecordRules](https://www.tencentcloud.com/document/api/267/30841) | Получает список правил записи | 500 |
| [DescribeLiveRecordTemplate](https://www.tencentcloud.com/document/api/267/30840) | Получает один шаблон записи | 500 |
| [DescribeLiveRecordTemplates](https://www.tencentcloud.com/document/api/267/30839) | Получает список шаблонов записи | 500 |
| [DescribeRecordTask](https://www.tencentcloud.com/document/api/267/56133) | CreateRecordTask (новый) | 20 |
| [ModifyLiveRecordTemplate](https://www.tencentcloud.com/document/api/267/30838) | Изменяет шаблон записи | 200 |
| [StopLiveRecord](https://www.tencentcloud.com/document/api/267/30837) | Завершает задачу записи (устарело; используйте новый API) | 200 |
| [StopRecordTask](https://www.tencentcloud.com/document/api/267/37307) | Завершает задачу записи (API) | 20 |

## API сдвига во времени

| Название API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [CreateLiveTimeShiftRule](https://www.tencentcloud.com/document/api/267/53726) | Создает правило сдвига во времени | 20 |
| [CreateLiveTimeShiftTemplate](https://www.tencentcloud.com/document/api/267/53725) | Создает шаблон сдвига во времени | 20 |
| [DeleteLiveTimeShiftRule](https://www.tencentcloud.com/document/api/267/53724) | Удаляет правило сдвига во времени | 20 |
| [DeleteLiveTimeShiftTemplate](https://www.tencentcloud.com/document/api/267/53723) | Удаляет шаблон сдвига во времени | 20 |
| [DescribeLiveTimeShiftRules](https://www.tencentcloud.com/document/api/267/53722) | Запрашивает правила сдвига во времени | 20 |
| [DescribeLiveTimeShiftTemplates](https://www.tencentcloud.com/document/api/267/53721) | Запрашивает шаблоны сдвига во времени | 20 |
| [DescribeTimeShiftRecordDetail](https://www.tencentcloud.com/document/api/267/53720) | Запрашивает детали сдвига во времени | 20 |
| [DescribeTimeShiftStreamList](https://www.tencentcloud.com/document/api/267/53719) | Запрашивает потоки со сдвигом во времени | 20 |
| [ModifyLiveTimeShiftTemplate](https://www.tencentcloud.com/document/api/267/53718) | Изменяет шаблон резервного потока | 20 |

## API обратного вызова LVB

| Название API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [CreateLiveCallbackRule](https://www.tencentcloud.com/document/api/267/30816) | Создает правило обратного вызова | 200 |
| [CreateLiveCallbackTemplate](https://www.tencentcloud.com/document/api/267/30815) | Создает шаблон обратного вызова | 200 |
| [DeleteLiveCallbackRule](https://www.tencentcloud.com/document/api/267/30814) | Удаляет правило обратного вызова | 200 |
| [DeleteLiveCallbackTemplate](https://www.tencentcloud.com/document/api/267/30813) | Удаляет шаблон обратного вызова | 200 |
| [DescribeLiveCallbackRules](https://www.tencentcloud.com/document/api/267/30812) | Получает список правил обратного вызова | 500 |
| [DescribeLiveCallbackTemplate](https://www.tencentcloud.com/document/api/267/30811) | Получает шаблон обратного вызова | 500 |
| [DescribeLiveCallbackTemplates](https://www.tencentcloud.com/document/api/267/30810) | Получает список шаблонов обратного вызова | 500 |
| [ModifyLiveCallbackTemplate](https://www.tencentcloud.com/document/api/267/30809) | Изменяет шаблон обратного вызова | 200 |

## API захвата скриншотов и обнаружения порнографии

| Название API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [CreateLiveSnapshotRule](https://www.tencentcloud.com/document/api/267/30835) | Создает правило захвата скриншотов | 200 |
| [CreateLiveSnapshotTemplate](https://www.tencentcloud.com/document/api/267/30834) | Создает шаблон захвата скриншотов | 200 |
| [CreateScreenshotTask](https://www.tencentcloud.com/document/api/267/54799) | Создает задачу захвата скриншотов | 20 |
| [DeleteLiveSnapshotRule](https://www.tencentcloud.com/document/api/267/30833) | Удаляет правило захвата скриншотов | 200 |
| [DeleteLiveSnapshotTemplate](https://www.tencentcloud.com/document/api/267/30832) | Удаляет шаблон захвата скриншотов | 200 |
| [DescribeLiveSnapshotRules](https://www.tencentcloud.com/document/api/267/30831) | Получает список правил захвата скриншотов | 500 |
| [DescribeLiveSnapshotTemplate](https://www.tencentcloud.com/document/api/267/30830) | Получает один шаблон захвата скриншотов | 500 |
| [DescribeLiveSnapshotTemplates](https://www.tencentcloud.com/document/api/267/30829) | Получает список шаблонов захвата скриншотов | 500 |
| [ModifyLiveSnapshotTemplate](https://www.tencentcloud.com/document/api/267/30828) | Изменяет конфигурацию шаблона захвата скриншотов | 200 |

## API управления аутентификацией

| Название API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [DescribeLiveDomainReferer](https://www.tencentcloud.com/document/api/267/40611) | Запрашивает конфигурацию списка разрешений/блокировок referer для доменного имени прямой трансляции | 20 |
| [DescribeLivePlayAuthKey](https://www.tencentcloud.com/document/api/267/30772) | Запрашивает ключ аутентификации воспроизведения | 500 |
| [DescribeLivePushAuthKey](https://www.tencentcloud.com/document/api/267/30771) | Запрашивает ключ аутентификации отправки | 500 |
| [ModifyLiveDomainReferer](https://www.tencentcloud.com/document/api/267/40610) | Настраивает список разрешений/блокировок referer для доменного имени прямой трансляции | 20 |
| [ModifyLivePlayAuthKey](https://www.tencentcloud.com/document/api/267/30770) | Изменяет ключ аутентификации воспроизведения | 100 |
| [ModifyLivePushAuthKey](https://www.tencentcloud.com/document/api/267/30769) | Изменяет ключ аутентификации отправки | 200 |

## API запросов данных мониторинга

| Название API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [DescribeAllStreamPlayInfoList](https://www.tencentcloud.com/document/api/267/37306) | Получает данные воспроизведения всех потоков в указанный момент времени | 20 |
| [DescribeGroupProIspPlayInfoList](https://www.tencentcloud.com/document/api/267/36097) | Запрашивает данные нисходящего воспроизведения по округам и поставщикам услуг интернета | 200 |
| [DescribeHttpStatusInfoList](https://www.tencentcloud.com/document/api/267/37305) | Запрашивает детали каждого кода состояния HTTP при воспроизведении | 200 |
| [DescribeLiveStreamPushInfoList](https://www.tencentcloud.com/document/api/267/37303) | Получает данные отправки потоков прямой трансляции | 500 |
| [DescribePlayErrorCodeDetailInfoList](https://www.tencentcloud.com/document/api/267/37301) | Запрашивает данные в реальном времени каждого кода ошибки HTTP при воспроизведении | 100 |
| [DescribePlayErrorCodeSumInfoList](https://www.tencentcloud.com/document/api/267/37300) | Запрашивает агрегированные данные кодов ошибок HTTP при воспроизведении | 200 |
| [DescribeProvinceIspPlayInfoList](https://www.tencentcloud.com/document/api/267/37299) | Запрашивает информацию о воспроизведении по поставщикам услуг интернета и округам | 200 |
| [DescribeStreamDayPlayInfoList](https://www.tencentcloud.com/document/api/267/36095) | Запрашивает данные трафика всех потоков | 500 |
| [DescribeStreamPlayInfoList](https://www.tencentcloud.com/document/api/267/37297) | Запрашивает список информации о воспроизведении потока | 500 |
| [DescribeStreamPushInfoList](https://www.tencentcloud.com/document/api/267/36094) | Получает данные отправки потока | 40 |
| [DescribeTopClientIpSumInfoList](https://www.tencentcloud.com/document/api/267/37296) | Запрашивает информацию о топе n IP адресов клиентов за определенный период времени | 100 |
| [DescribeVisitTopSumInfoList](https://www.tencentcloud.com/document/api/267/37295) | Запрашивает информацию о топе n доменных имен или ID потоков за определенный период времени | 100 |
| [DescribeLiveTranscodeDetailInfo](https://www.tencentcloud.com/document/api/267/37302) | Запрашивает статистику трансляции LVB | 200 |

## API запросов данных биллинга

| Название API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [DescribeDeliverBandwidthList](https://www.tencentcloud.com/document/api/267/37836) | Запрашивает оплачиваемую пропускную способность прямой трансляции ретрансляции | 20 |
| [DescribeLiveTimeShiftBillInfoList](https://www.tencentcloud.com/document/api/267/47919) | Запрашивает данные биллинга сдвига во времени | 20 |
| [DescribeLiveTranscodeTotalInfo](https://www.tencentcloud.com/document/api/267/44907) | Запрашивает общее использование услуги трансляции | 200 |
| [DescribeScreenShotSheetNumList](https://www.tencentcloud.com/document/api/267/37298) | Запрашивает количество снимков экрана | 100 |
| [DescribeTranscodeTaskNum](https://www.tencentcloud.com/document/api/267/50613) | Запрашивает количество задач трансляции | 20 |
| [DescribeUploadStreamNums](https://www.tencentcloud.com/document/api/267/39500) | Запрашивает количество восходящих каналов LVB. | 20 |
| [DescribeConcurrentRecordStreamNum](https://www.tencentcloud.com/document/api/267/36188) | Запрашивает количество одновременных каналов записи | 200 |
| [DescribeBillBandwidthAndFluxList](https://www.tencentcloud.com/document/api/267/36098) | Запрашивает данные оплачиваемой пропускной способности и трафика | 100 |

## API управления потоками прямой трансляции

| Название API | Функция | Ограничение частоты (максимум запросов в секунду) |
| --- | --- | --- |
| [DescribeLiveForbidStreamList](https://www.tencentcloud.com/document/api/267/30801) | Получает список запрещенных потоков. | 100 |
| [DescribeLiveStreamEventList](https://www.tencentcloud.com/document/api/267/30800) | Запрашивает события потоков. | 300 |
| [DescribeLiveStreamOnlineList](https://www.tencentcloud.com/document/api/267/30798) | Запрашивает потоки прямой трансляции. | 100 |
| [DescribeLiveStreamPublishedList](https://www.tencentcloud.com/document/api/267/30797) | Запрашивает список отправленных потоков. | 300 |
| [DropLiveStream](https://www.tencentcloud.com/document/api/267/30795) | Приостанавливает поток прямой трансляции | 100 |
| [ResumeLiveStream](https://www.tencentcloud.com/document/api/267/30793) | Возобновляет поток прямой трансляции. | 100 |
| [DescribeLiveStreamState](https://www.tencentcloud.com/document/api/267/30796) | Запрашивает статус потока. | 300 |
| [ForbidLiveStream](https://www.tencentcloud.com/document/api/267/30794) | Запрещает поток прямой трансляции. | 200 |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30760](https://www.tencentcloud.com/document/product/267/30760)*

---
*Источник (EN): [api-category.md](./api-category.md)*

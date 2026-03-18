# RoomKit API

## Введение

TUIRoomKit API — это компонент для многопользовательских встреч с **встроенным пользовательским интерфейсом**. Используя TUIRoomKit API, вы можете быстро реализовать сценарий, похожий на встречу, через простой интерфейс. Подробные инструкции по интеграции см. в разделе: [Интеграция](https://www.tencentcloud.com/document/product/647/57508#).

В этом документе подробно описаны классы и связанные интерфейсы, которые вы можете использовать в Flutter TUIRoomKit. Ознакомившись с этим документом, вы получите более полное понимание того, как использовать Flutter TUIRoomKit.

## ConferenceMainPage

Главная страница конференции

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4a022c4d0e9911ef8c545254000781d8.png)

| Параметр | Тип | Описание |
| --- | --- | --- |
| conferenceId | String | ID конференции, необходимый для создания или присоединения к конференции |
| isCreateConference | bool | Является ли это созданием конференции (true для создания, false для присоединения) |
| conferenceParams | [ConferenceParams](https://www.tencentcloud.com/document/product/647/60356#ConferenceParams) | Параметры, связанные с созданием или присоединением к конференции |
| conferenceObserver | [ConferenceObserver](https://www.tencentcloud.com/document/product/647/60356#ConferenceObserver) | Слушатель обратного вызова изменения статуса конференции |

> **Примечание：** Когда вы используете [ConferenceSession](https://www.tencentcloud.com/document/product/647/60356#f09c9c3b-4eeb-4fee-879c-51eef62ab13d) для создания или присоединения к конференции, вам не нужно передавать какие-либо параметры отсюда.

## ConferenceSession

Если вы хотите перейти на страницу конференции после успешного создания/присоединения к конференции, вы можете использовать класс `ConferenceSession` для выполнения связанных операций.

| Параметр | Тип | Описание |
| --- | --- | --- |
| isMuteMicrophone | bool | Отключить ли микрофон (по умолчанию false) |
| isOpenCamera | bool | Включить ли камеру (по умолчанию false) |
| isSoundOnSpeaker | bool | Использовать ли громкоговорители (по умолчанию true) |
| name | String | Имя конференции (по умолчанию используется ID вашей конференции, недействительно при присоединении к конференции) |
| enableMicrophoneForAllUser | bool | Включить ли разрешение микрофона для всех участников (по умолчанию true, недействительно при присоединении к конференции) |
| enableCameraForAllUser | bool | Включить ли разрешение камеры для всех участников (по умолчанию true, недействительно при присоединении к конференции) |
| enableMessageForAllUser | bool | Включить ли разрешение на речь для всех участников (по умолчанию true, недействительно при присоединении к конференции) |
| enableSeatControl | bool | Включить ли режим выступления на сцене (по умолчанию false, недействительно при присоединении к конференции) |
| onActionSuccess | VoidCallback | Обратный вызов при успешном создании/присоединении к конференции. В этом обратном вызове вы можете перейти на страницу встречи. |
| onActionError | Function ([ConferenceError](https://www.tencentcloud.com/document/product/647/60356#ConferenceError),  String) | Обратный вызов при неудачном создании/присоединении к конференции. |

### newInstance

Создает новый объект ConferenceSession.

```
factory ConferenceSession.newInstance(String id)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| id | String | ID конференции, необходимый для создания или присоединения к конференции |

### quickStart

Быстрое создание интерфейсов конференции.

```
Future<void> quickStart()
```

### join

Интерфейс присоединения к конференции.

```
Future<void> join()
```

> **Примечание：** Перед вызовом интерфейса быстрого создания конференции или присоединения к конференции необходимо завершить все параметры ConferenceSession, которые вам нужно установить. Подробные сведения см. в разделе [Управление до конференции](https://www.tencentcloud.com/document/product/647/59974#67fc07af-5df6-445f-a705-bd49643e0047). При прямой навигации на [ConferenceMainPage](https://www.tencentcloud.com/document/product/647/60356#ConferenceMainPage) и передаче соответствующих параметров для создания/присоединения к конференции нет необходимости использовать `ConferenceSession`.

## ConferenceParams

| Параметр | Тип | Описание |
| --- | --- | --- |
| isMuteMicrophone | bool | Отключить ли микрофон (по умолчанию false) |
| isOpenCamera | bool | Включить ли камеру (по умолчанию false) |
| isSoundOnSpeaker | bool | Использовать ли громкоговорители (по умолчанию true) |
| name | String | Имя конференции (по умолчанию используется ID вашей конференции, недействительно при присоединении к конференции) |
| enableMicrophoneForAllUser | bool | Включить ли разрешение микрофона для всех участников (по умолчанию true, недействительно при присоединении к конференции) |
| enableCameraForAllUser | bool | Включить ли разрешение камеры для всех участников (по умолчанию true, недействительно при присоединении к конференции) |
| enableMessageForAllUser | bool | Включить ли разрешение на речь для всех участников (по умолчанию true, недействительно при присоединении к конференции) |
| enableSeatControl | bool | Включить ли режим выступления на сцене (по умолчанию false, недействительно при присоединении к конференции) |
| onActionSuccess | VoidCallback | Обратный вызов при успешном создании/присоединении к конференции. В этом обратном вызове вы можете перейти на страницу встречи. |
| onActionError | Function ([ConferenceError](https://www.tencentcloud.com/document/product/647/60356#ConferenceError),  String) | Обратный вызов при неудачном создании/присоединении к конференции. |

## ConferenceObserver

### onConferenceStarted

Событие начала конференции.

```
Function(String conferenceId, ConferenceError error) onConferenceStarted
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| conferenceId | String | ID конференции |
| error | [ConferenceError](https://www.tencentcloud.com/document/product/647/60356#ConferenceError) | Код ошибки |

### onConferenceJoined

Событие присоединения к конференции.

```
Function(String conferenceId, ConferenceError error) onConferenceJoined
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| conferenceId | String | ID конференции |
| error | [ConferenceError](https://www.tencentcloud.com/document/product/647/60356#ConferenceError) | Код ошибки |

### onConferenceFinished

Событие окончания встречи. Этот обратный вызов будет запущен при активном завершении встречи или закрытии встречи.

```
Function(String conferenceId) onConferenceFinished
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| conferenceId | String | ID конференции |

### onConferenceExited

Событие выхода из встречи. Этот обратный вызов будет запущен при активном выходе из встречи или исключении из встречи.

```
Function(String conferenceId) onConferenceFinished
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| conferenceId | String | ID конференции |

## ConferenceError

Код ошибки

| Перечисление | Значение | Описание |
| --- | --- | --- |
| success | 0 | Операция успешна |
| errFailed | -1 | Временная неклассифицированная общая ошибка |
| errConferenceIdNotExist | -2100 | Комната не существует при входе, может быть закрыта |
| errConferenceIdInvalid | -2105 | Недопустимый пользовательский ID комнаты, должен содержать печатаемые символы ASCII (0x20-0x7e), длина до 48 байт |
| errConferenceIdOccupied | -2106 | ID комнаты уже используется, выберите другой ID комнаты |
| errConferenceNameInvalid | -2107 | Недопустимое имя комнаты, максимум 30 байт, кодировка UTF-8 при наличии китайских символов |


---
*Источник: [https://trtc.io/document/60356](https://trtc.io/document/60356)*

---
*Источник (EN): [roomkit-api.md](./roomkit-api.md)*

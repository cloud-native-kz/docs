# TUILiveListManager

Copyright (c) 2024 Tencent. All rights reserved.

Module:   TUILiveListManager @ TUIKitEngine

Function: Интерфейс для потоковой трансляции

**TUILiveListManager**

## TUILiveListManager

| Список функций | Описание |
| --- | --- |
| [onLiveInfoChanged](https://www.tencentcloud.com/document/product/647/67260#onLiveInfoChanged) | Обратный вызов при изменении информации о потоковой трансляции |
| [addObserver](https://www.tencentcloud.com/document/product/647/67260#setObserver) | Добавить обратный вызов события |
| [removeObserver](https://www.tencentcloud.com/document/product/647/67260#efc0a6c0-9ac3-4012-810e-c6d4ad12fa71) | Удалить обратный вызов события |
| [setLiveInfo](https://www.tencentcloud.com/document/product/647/67260#setLiveInfo) | Изменить информацию о потоковой трансляции |
| [getLiveInfo](https://www.tencentcloud.com/document/product/647/67260#getLiveInfo) | Получить информацию о потоковой трансляции |
| [fetchLiveList](https://www.tencentcloud.com/document/product/647/67260#fetchLiveList) | Получить список потоковых трансляций |

## Тип структуры

| Список функций | Описание |
| --- | --- |
| [TUILiveInfo](https://www.tencentcloud.com/document/product/647/67260#TUILiveInfo) | Информация о потоковой трансляции |

## Типы перечисления

| Типы перечисления | Описание |
| --- | --- |
| [TUILiveModifyFlag](https://www.tencentcloud.com/document/product/647/67260#TUILiveModifyFlag) | Флаги изменения для комнаты потоковой трансляции |

## onLiveInfoChanged

**onLiveInfoChanged**

| OnLiveInfoChanged onLiveInfoChanged | ([TUILiveInfo](https://www.tencentcloud.com/document/product/647/67260#TUILiveInfo) TUILiveInfo |
| --- | --- |
|  | [TUILiveModifyFlag](https://www.tencentcloud.com/document/product/647/67260#TUILiveModifyFlag) modifyFlag) |

#### Обратный вызов при изменении информации о потоковой трансляции

| Параметры | Описание |
| --- | --- |
| TUILiveInfo | Информация о комнате потоковой трансляции |
| modifyFlagList | Список флагов изменённых значений |

## addObserver

**setObserver**

| void setObserver | (TUILiveListObserver observer) |
| --- | --- |

#### Добавить обратный вызов события

Вы можете получать уведомления о событиях комнаты потоковой трансляции через TUILiveListManagerObserver

| Параметры | Описание |
| --- | --- |
| observer | Экземпляр для мониторинга |

## removeObserver

**removeObserver**

| void setObserver | (TUILiveListObserver observer) |
| --- | --- |

#### Удалить обратный вызов события

Вы можете получать уведомления о событиях комнаты потоковой трансляции через TUILiveListManagerObserver

| Параметры | Описание |
| --- | --- |
| observer | Экземпляр для мониторинга |

## setLiveInfo

**setLiveInfo**

| Future<TUIActionCallback> setLiveInfo | ([TUILiveInfo](https://www.tencentcloud.com/document/product/647/67260#TUILiveInfo) TUILiveInfo |
| --- | --- |
|  | [TUILiveModifyFlag](https://www.tencentcloud.com/document/product/647/67260#TUILiveModifyFlag) modifyFlag) |

#### Изменить информацию о потоковой трансляции

| Параметры | Описание |
| --- | --- |
| roomId | ID комнаты |
| coverUrl | URL фотографии профиля |
| categoryList | Теги категории комнаты потоковой трансляции |
| isPublicVisible | Является ли публичной |
| activityStatus | Статус активности комнаты потоковой трансляции: пользовательский тег определения |

## getLiveInfo

**getLiveInfo**

| Future<TUIValueCallBack<TUILiveInfo>> getLiveInfo | (String roomId) |
| --- | --- |

#### Получить информацию о потоковой трансляции

| Параметры | Описание |
| --- | --- |
| callback | Обратный вызов вызова API, используется для уведомления об успехе или сбое вызова API |
| roomId | ID комнаты |

## fetchLiveList

**fetchLiveList**

| Future<TUIValueCallBack<TUILiveListResult>> fetchLiveList | (String cursor |
| --- | --- |
|  | int count) |

#### Получить список потоковых трансляций

| Параметры | Описание |
| --- | --- |
| count | Количество получаемых элементов за раз |
| cursor | Индекс списка |

## TUILiveModifyFlag

**TUILiveModifyFlag**

#### Флаги изменения для комнаты потоковой трансляции

| Перечисление | Значение | Описание |
| --- | --- | --- |
| ACTIVITY_STATUS | 0x0100 | ActivityStatus: статус активности комнаты потоковой трансляции, поддерживает пользовательские настройки |
| COVER_URL | 0x0200 | CoverUrl: обложка комнаты потоковой трансляции |
| CATEGORY | 0x0400 | Category: категория комнаты потоковой трансляции |
| PUBLISH | 0x0800 | Publish: публичный тег комнаты потоковой трансляции |

## TUILiveInfo

**TUILiveInfo**

#### Информация о потоковой трансляции

| Типы перечисления | Описание |
| --- | --- |
| activityStatus | Статус активности комнаты потоковой трансляции: пользовательский тег определения |
| categoryList | Теги категории комнаты потоковой трансляции |
| coverUrl | Обложка комнаты потоковой трансляции |
| isPublicVisible | Является ли комната потоковой трансляции публичной |
| roomInfo | Информация о комнате (только для чтения) |
| viewCount | Общее количество просмотров |


---
*Источник: [https://trtc.io/document/67260](https://trtc.io/document/67260)*

---
*Источник (EN): [tuilivelistmanager.md](./tuilivelistmanager.md)*

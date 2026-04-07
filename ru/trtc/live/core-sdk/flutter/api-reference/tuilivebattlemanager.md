# TUILiveBattleManager

Copyright (c) 2024 Tencent. All rights reserved.

Модуль:   TUILiveBattleManager @ TUIKitEngine

API-интерфейсы, связанные с прямой трансляцией Battle

**TUILiveBattleManager**

## TUILiveBattleObserver

| Список функций | Описание |
| --- | --- |
| [onBattleStarted](https://www.tencentcloud.com/document/product/647/69266#7a0cc7db9328b7ed901d596edba5c6ec) | Уведомление о начале Battle |
| [onBattleEnded](https://www.tencentcloud.com/document/product/647/69266#2e3d364b388a92476d657e2d28ddcf8b) | Уведомление об окончании Battle |
| [onUserJoinBattle](https://www.tencentcloud.com/document/product/647/69266#a7837241acd6fa7baf2b4fd14e437847) | Уведомление о присоединении пользователя к Battle |
| [onUserExitBattle](https://www.tencentcloud.com/document/product/647/69266#8d6695e3a5bd6703073a5decc2ef0a86) | Уведомление о выходе пользователя из Battle |
| [onBattleScoreChanged](https://www.tencentcloud.com/document/product/647/69266#b644272d9d1d0d3ce2726c6991ad2f97) | Уведомление об обновлении оценки Battle пользователя |
| [onBattleRequestReceived](https://www.tencentcloud.com/document/product/647/69266#bce652dfde53919487fd7b88e0ba002a) | Вызываемый получает уведомление о приглашении на Battle |
| [onBattleRequestCancelled](https://www.tencentcloud.com/document/product/647/69266#69b7c2f7116d6eb875949bb948a10bc3) | Вызываемый получает уведомление об отмене Battle |
| [onBattleRequestTimeout](https://www.tencentcloud.com/document/product/647/69266#67668637eacf189329cbece2638a56e5) | Уведомление об истечении времени обработки Battle |
| [onBattleRequestAccept](https://www.tencentcloud.com/document/product/647/69266#c36eb33aea066c55ca692bff5b1baabe) | Вызывающий получает уведомление о согласии вызываемого |
| [onBattleRequestReject](https://www.tencentcloud.com/document/product/647/69266#097d2c0b5a506d72c28b8060e5b75762) | Вызывающий получает уведомление об отказе вызываемого |

## TUILiveBattleManager

| Список функций | Описание |
| --- | --- |
| [addObserver](https://www.tencentcloud.com/document/product/647/69266#bb2be01f092eca743c1bda28810cf314) | Добавить обратный вызов события |
| [removeObserver](https://www.tencentcloud.com/document/product/647/69266#5dcc0f73f5a5d0587fe1706b50025cc8) | Удалить обратный вызов события |
| [requestBattle](https://www.tencentcloud.com/document/product/647/69266#cb5a6c657ac328bc81310dbbde6f11ba) | Инициировать запрос Battle |
| [cancelBattleRequest](https://www.tencentcloud.com/document/product/647/69266#7cce082bea8a3aa9478b69abc6a7cdd1) | Отменить запрос Battle |
| [acceptBattle](https://www.tencentcloud.com/document/product/647/69266#2ade6de883b4c32df3b8125803c758e4) | Принять запрос Battle |
| [rejectBattle](https://www.tencentcloud.com/document/product/647/69266#0476a8497fca375ae3e2540e2a810c73) | Отклонить запрос Battle |
| [exitBattle](https://www.tencentcloud.com/document/product/647/69266#f86e8b8f25f9e4b7ed523588e149e315) | Выход из Battle |

## Типы структурных данных

| Список функций | Описание |
| --- | --- |
| [TUIBattleUser](https://www.tencentcloud.com/document/product/647/69266#e079d942f7b568a2a1d6eaef6a3a31b5) | Информация пользователя Battle |
| [TUIBattleConfig](https://www.tencentcloud.com/document/product/647/69266#6ca8b8898efedde803c17d8513bbcae7) | Конфигурация Battle |
| [TUIBattleInfo](https://www.tencentcloud.com/document/product/647/69266#6b40e91c64a0a1ddbc355f14e0882d07) | Информация Battle |
| [TUIBattleRequestResult](https://www.tencentcloud.com/document/product/647/69266#490d4a56-5cea-4b36-918e-7fac96672c75) | Результат запроса Battle |

## Типы перечисления

| Типы перечисления | Описание |
| --- | --- |
| [TUIBattleCode](https://www.tencentcloud.com/document/product/647/69266#7fb9c27105c7f9ca9ccb3d560ac3017d) | Статус приглашения Battle |
| [TUIBattleStoppedReason](https://www.tencentcloud.com/document/product/647/69266#e162b34537d4a7e02e70c1a11d9c0e41) | Причины завершения Battle |

## onBattleStarted

**Уведомление о начале Battle**

```
OnBattleStarted onBattleStarted = (TUIBattleInfo battleInfo) {};
```

| Параметр | Описание |
| --- | --- |
| battleInfo | Информация Battle. |

## onBattleEnded

**Уведомление об окончании Battle**

```
OnBattleEnded onBattleEnded = (TUIBattleInfo battleInfo, TUIBattleStoppedReason reason) {};
```

| Параметр | Описание |
| --- | --- |
| battleInfo | Информация Battle. |
| reason | Причины завершения Battle. |

## onUserJoinBattle

**Уведомление о присоединении пользователя к Battle**

```
OnUserJoinBattle onUserJoinBattle = (String battleId, TUIBattleUser battleUser) {};
```

| Параметр | Описание |
| --- | --- |
| battleId | ID Battle. |
| battleUser | Информация пользователя Battle. |

## onUserExitBattle

**Уведомление о выходе пользователя из Battle**

```
OnUserExitBattle onUserExitBattle = (String battleId, TUIBattleUser battleUser) {};
```

| Параметр | Описание |
| --- | --- |
| battleId | ID Battle. |
| battleUser | Информация пользователя Battle. |

## onBattleScoreChanged

**Уведомление об обновлении оценки Battle пользователя**

```
OnBattleScoreChanged onBattleScoreChanged = (String battleId, List<TUIBattleUser> battleUserList) {};
```

| Параметр | Описание |
| --- | --- |
| battleId | ID Battle. |
| battleUserList | Информация пользователя Battle. |

## onBattleRequestReceived

**Вызываемый получает уведомление о приглашении на Battle**

```
OnBattleRequestReceived onBattleRequestReceived =     (TUIBattleInfo battleInfo,      TUIBattleUser inviter,      TUIBattleUser invitee) {};
```

| Параметр | Описание |
| --- | --- |
| battleInfo | Информация Battle. |
| inviter | Информация пользователя, инициирующего приглашение. |
| invitee | Информация пользователя, получающего приглашение. |

## onBattleRequestCancelled

**Вызываемый получает уведомление об отмене Battle**

```
OnBattleRequestCancelled onBattleRequestCancelled =     (TUIBattleInfo battleInfo,      TUIBattleUser inviter,      TUIBattleUser invitee) {};
```

| Параметр | Описание |
| --- | --- |
| battleInfo | Информация Battle. |
| inviter | Информация пользователя, инициирующего приглашение. |
| invitee | Информация пользователя, получающего приглашение. |

## onBattleRequestTimeout

**Уведомление об истечении времени обработки Battle**

```
OnBattleRequestTimeout onBattleRequestTimeout =     (TUIBattleInfo battleInfo,      TUIBattleUser inviter,      TUIBattleUser invitee) {};
```

| Параметр | Описание |
| --- | --- |
| battleInfo | Информация Battle. |
| inviter | Информация пользователя, инициирующего приглашение. |
| invitee | Информация пользователя, получающего приглашение. |

## onBattleRequestAccept

**Вызывающий получает уведомление о согласии вызываемого**

```
OnBattleRequestAccept onBattleRequestAccept =     (TUIBattleInfo battleInfo,      TUIBattleUser inviter,      TUIBattleUser invitee) {};
```

| Параметр | Описание |
| --- | --- |
| battleInfo | Информация Battle. |
| inviter | Информация пользователя, инициирующего приглашение. |
| invitee | Информация пользователя, получающего приглашение. |

## onBattleRequestReject

**Вызывающий получает уведомление об отказе вызываемого**

```
OnBattleRequestReject onBattleRequestAccept =     (TUIBattleInfo battleInfo,      TUIBattleUser inviter,      TUIBattleUser invitee) {};
```

| Параметр | Описание |
| --- | --- |
| battleInfo | Информация Battle. |
| inviter | Информация пользователя, инициирующего приглашение. |
| invitee | Информация пользователя, получающего приглашение. |

## addObserver

**Добавить обратный вызов события**

```
 void addObserver(TUILiveBattleObserver observer);
```

| Параметр | Описание |
| --- | --- |
| observer | Прослушиваемые экземпляры. |

## removeObserver

**Удалить обратный вызов события**

```
void removeObserver(TUILiveBattleObserver observer);
```

| Параметр | Описание |
| --- | --- |
| observer | Прослушиваемые экземпляры. |

## requestBattle:userIdList

**Инициировать запрос Battle**

```
Future<TUIValueCallBack<TUIBattleRequestResult>> requestBattle    (TUIBattleConfig config,      List<String> userIdList,      int timeout);
```

| Параметр | Описание |
| --- | --- |
| config | Информация о конфигурации Battle. |
| userIdList | Список ID приглашаемых пользователей. |
| timeout | Время истечения |

## cancelBattleRequest

**Отменить запрос Battle**

```
Future<TUIActionCallback> cancelBattleRequest(String battleId, List<String> userIdList);
```

| Параметр | Описание |
| --- | --- |
| battleId | ID Battle. |
| userIdList | Список ID пользователей, отмену которых нужно отменить. |

## acceptBattle

**Принять запрос Battle**

```
Future<TUIActionCallback> acceptBattle(String battleId);
```

| Параметр | Описание |
| --- | --- |
| battleId | ID Battle. |

## rejectBattle

**Отклонить запрос Battle**

```
Future<TUIActionCallback> rejectBattle(String battleId);
```

| Параметр | Описание |
| --- | --- |
| battleId | ID Battle. |

## exitBattle

**Выход из Battle**

```
Future<TUIActionCallback> exitBattle(String battleId);
```

| Параметр | Описание |
| --- | --- |
| battleId | ID Battle. |

## TUIBattleUser

**Информация пользователя Battle**

| Типы перечисления | Описание |
| --- | --- |
| roomId | ID комнаты Battle. |
| userId | ID пользователя Battle. |
| userName | Никнейм пользователя Battle. |
| avatarUrl | Адрес аватара пользователя Battle. |
| score | Оценка Battle. |

## TUIBattleConfig

**Конфигурация Battle**

| Типы перечисления | Описание |
| --- | --- |
| duration | Максимальная продолжительность Battle (единица: секунды). |
| needResponse | Должен ли приглашённый пользователь ответить согласием или отказом. |
| extensionInfo | Расширенная информация Battle. |

## TUIBattleInfo

**Информация Battle**

| Типы перечисления | Описание |
| --- | --- |
| battleId | ID Battle. |
| config | Конфигурация Battle. |
| inviter | Инициатор Battle. |
| inviteeList | Пригласить членов Battle. |
| startTime | Временная метка начала Battle (единица: секунды). |
| endTime | Временная метка окончания Battle (единица: секунды). |

## TUIBattleRequestResult

| Типы перечисления | Описание |
| --- | --- |
| battleInfo | Информация Battle. |
| requestMap | Результат запроса Battle |

## TUIBattleCode

**Статус приглашения Battle**

| Пример ошибки | Значение | Описание |
| --- | --- | --- |
| unknown | -1 | Статус по умолчанию. |
| success | 0 | Запрос Battle отправлен успешно. |
| roomNotExists | 1 | Приглашённая комната не существует. |
| battling | 2 | Приглашённая комната уже находится в Battle. |
| battlingOtherRoom | 3 | Приглашённая комната уже находится в Battle с другой комнатой. |
| roomExit | 4 | Комната вышла. |
| retry | 5 | Внутренняя ошибка, рекомендуется повторить попытку. |

## TUIBattleStoppedReason

**Причины завершения Battle**

| Пример ошибки | Значение | Описание |
| --- | --- | --- |
| timeOver | 0 | Battle достигло максимальной продолжительности и завершилось по истечении времени. |
| otherExit | 1 | Все остальные пользователи в Battle вышли. |


---
*Источник: [https://trtc.io/document/69266](https://trtc.io/document/69266)*

---
*Источник (EN): [tuilivebattlemanager.md](./tuilivebattlemanager.md)*

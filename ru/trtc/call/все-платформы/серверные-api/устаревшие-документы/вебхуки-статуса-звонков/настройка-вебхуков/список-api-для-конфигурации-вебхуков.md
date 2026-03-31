# Список API для конфигурации вебхуков

## Конфигурация информации обратного вызова

| Обзор функции | API |
| --- | --- |
| Создать обратный вызов | [v1/callback/set](https://www.tencentcloud.com/document/product/647/60111#) |
| Запросить обратный вызов | [v1/callback/get](https://www.tencentcloud.com/document/product/647/60112#) |
| Обновить обратный вызов | [v1/callback/update](https://www.tencentcloud.com/document/product/647/60113#) |
| Удалить обратный вызов | [v1/callback/delete](https://www.tencentcloud.com/document/product/647/60114#) |

## Список команд обратного вызова

| Обратный вызов статуса вызова | Обратный вызов события вызова |
| --- | --- |
| `cancel` Отмена: инициатор отменяет вызов до его принятия`reject` Отклонено: адресат отклоняет вызов`not_answer` Пропущенный вызов: адресат не отвечает в течение периода ожидания`normal_end` Завершено: вызов установлен и завершен нормально`call_busy` Занято: вызов попал на занятую линию`interrupt` Прерывание: вызов прерван из-за сетевых или других причин | `caller_start_call` Инициатор начинает вызов`caller_call_accepted` Инициатор принимает вызов`caller_call_missed` Инициатор пропускает вызов`caller_call_rejected` Инициатор отклоняет вызов`caller_call_busy` Линия инициатора занята`caller_cancel_call` Инициатор отменяет вызов`caller_call_failed` Инициатор не может начать вызов`caller_call_end` Инициатор нормально завершает вызов`caller_call_interrupted` Вызов инициатора прерван`callee_receive_call` Адресат получает вызов`callee_accept_call` Адресат принимает вызов`callee_not_answer_call` Адресат не отвечает`callee_reject_call` Адресат отклоняет вызов`callee_ignore_call` Адресат игнорирует вызов`callee_call_canceled` Адресат отменяет вызов`callee_call_end` Адресат нормально завершает вызов`callee_call_interrupted` Вызов адресата прерван`invite_user` Приглашение пользователя во время вызова`join_in_group_call` Присоединиться к вызову во время разговора |


---
*Источник: [https://trtc.io/document/60135](https://trtc.io/document/60135)*

---
*Источник (EN): [api-list-for-webhooks-configuration.md](список-api-для-конфигурации-вебхуков.md)*

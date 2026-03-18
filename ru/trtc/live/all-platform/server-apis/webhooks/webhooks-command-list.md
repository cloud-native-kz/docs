# Список команд Webhooks

## Связанные с комнатой

| Тип Webhook | Команда Webhook |
| --- | --- |
| После создания комнаты | [Live.CallbackAfterCreateRoom](https://www.tencentcloud.com/document/product/647/64422) |
| После удаления комнаты | [Live.CallbackAfterDestroyRoom](https://www.tencentcloud.com/document/product/647/64423) |
| После обновления комнаты | [Live.CallbackAfterUpdateRoomInfo](https://www.tencentcloud.com/document/product/647/67938) |
| После установки метаданных | [Live.CallbackAfterSetMetadata](https://www.tencentcloud.com/document/product/647/68222) |
| После удаления метаданных | [Live.CallbackAfterDelMetadata](https://www.tencentcloud.com/document/product/647/68223) |
| Оповещение при достижении 70% при создании комнаты | [Live.CallbackAfterCreateRoomReachingThreshold](https://www.tencentcloud.com/document/product/647/70485) |

## Связанные с пользователем

| Тип Webhook | Команда Webhook |
| --- | --- |
| Webhook для изменения статуса участника комнаты | [Live.CallbackAfterMemberStateChanged](https://www.tencentcloud.com/document/product/647/64424) |
| Webhook для изменения владельца комнаты | [Live.CallbackAfterChangeOwner](https://www.tencentcloud.com/document/product/647/72553) |
| Webhook для изменения администратора комнаты | [Live.CallbackAfterModifyAdmin](https://www.tencentcloud.com/document/product/647/72554) |

## Связанные с микрофоном

| Тип Webhook | Команда Webhook |
| --- | --- |
| Webhook после изменения списка мест на микрофоне | [Mic.CallbackAfterSeatInfoChanged](https://www.tencentcloud.com/document/product/647/64425) |

## Связанные с боем

| Тип Webhook | Команда Webhook |
| --- | --- |
| Webhook после создания боя | [Live.CallbackAfterCreateBattle](https://www.tencentcloud.com/document/product/647/68259) |
| Webhook после начала боя | [Live.CallbackAfterStartBattle](https://www.tencentcloud.com/document/product/647/68260) |
| Webhook после окончания боя | [Live.CallbackAfterEndBattle](https://www.tencentcloud.com/document/product/647/68261) |

## Связанные с подарками

| Тип Webhook | Команда Webhook |
| --- | --- |
| Webhook перед отправкой подарка | [Live.CallbackBeforeSendGift](https://www.tencentcloud.com/document/product/647/72210) |
| Конфигурация неблокирующего режима перед отправкой подарка | [Live.CallbackBeforeCallBackNotBlock](https://www.tencentcloud.com/document/product/647/72210) |

## Связанные с сообщениями

| Тип Webhook | Команда Webhook |
| --- | --- |
| После отправки группового сообщения | [Group.CallbackAfterSendMsg](https://www.tencentcloud.com/document/product/647/74348) |
| Перед отправкой группового сообщения | [Group.CallbackBeforeSendMsg](https://www.tencentcloud.com/document/product/647/74347) |

## Подписки и подписчики

| Тип Webhook | Команда Webhook |
| --- | --- |
| После подписки на пользователя | [Follow.CallbackAfterFollowAdd](https://www.tencentcloud.com/document/product/647/74356) |
| После отписки от пользователя | [Follow.CallbackAfterFollowDelete](https://www.tencentcloud.com/document/product/647/74357) |


---
*Источник: [https://trtc.io/document/64413](https://trtc.io/document/64413)*

---
*Источник (EN): [webhooks-command-list.md](./webhooks-command-list.md)*

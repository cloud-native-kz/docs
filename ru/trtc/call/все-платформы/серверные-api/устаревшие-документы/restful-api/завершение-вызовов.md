# Завершение вызовов

Этот документ описывает способ завершения вызовов на сервере во время аудио- и видеозвонков для лучшего управления продолжительностью вызова и улучшения качества обслуживания в различных сценариях, таких как медицинские консультации и социальные взаимодействия один-на-один.

## Описание API

Домен запроса API: **trtc.tencentcloudapi.com**.

Описание API: удалить всех пользователей из аудио- и видеокомнаты для завершения вызова.

Ограничение частоты запросов API по умолчанию: **20 раз/сек**.

## Пример запроса

```
https://trtc.tencentcloudapi.com/?Action=DismissRoom&SdkAppId=1400000001&RoomId=1234&<Common request parameters>
```

В следующей таблице описаны только измененные параметры при вызове этого API. Дополнительную информацию см. в разделе: [TRTC API Request](https://trtc.io/document/34262?product=serverapis).

| Параметр | Обязательный | Тип | Описание |
| --- | --- | --- | --- |
| trtc.tencentcloudapi.com | Да | String | API запроса |
| Action | Да | String | [Общие параметры](https://trtc.io/document/34263?product=serverapis). Для этого API значение: `DismissRoom`. |
| Version | Да | String | [Общие параметры](https://trtc.io/document/34263?product=serverapis), значение для этого API: 2019-07-22. |
| Region | Да | String | [Общие параметры](https://trtc.io/document/34263?product=serverapis). См. поддерживаемый [список регионов](https://trtc.io/document/34262?product=serverapis#1.-service-address). Этот API поддерживает только: ap-beijing, ap-guangzhou, ap-mumbai. |
| SdkAppId | Да | Integer | SDKAppId для вызова. Пример значения: 1400188366 |
| RoomId | Да | Integer | Номер аудио- и видеокомнаты. |
| Common request parameters | Да | / | Дополнительные сведения см. в разделе: [Общие параметры](https://trtc.io/document/34263?product=serverapis) |

> **Примечание:** Для удаления комнаты со строковым номером комнаты установите Action на: DismissRoomByStrRoomId, где RoomId имеет тип: String.

## Пример ответа

```
{    "Response": {        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"        }}
```

| Имя параметра | Тип | Описание |
| --- | --- | --- |
| RequestId | String | Уникальный ID запроса, сгенерированный на сервере, возвращается с каждым запросом (если запрос по другим причинам не достигает сервера, RequestId не будет получен). При устранении неполадок укажите RequestId запроса. |

### Отладка API

API Explorer: [API Explorer](https://console.tencentcloud.com/api/explorer?SignVersion=api3v3).

API Explorer упрощает выполнение онлайн-вызовов API, проверку подписей, создание кода SDK, поиск API и т. д. Его также можно использовать для запроса содержимого каждого запроса и его ответа.

## Коды ошибок

Коды ошибок, указанные ниже, относятся только к бизнес-логике API. Дополнительные коды ошибок см. в разделе [Общие коды ошибок](https://trtc.io/document/34270?product=serverapis#common-error-codes).

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.RoomNotExist | Комната не существует. |
| InternalError | Внутренняя ошибка. |
| InternalError.GetRoomCacheIpError | Ошибка при запросе информации о комнате. |
| InvalidParameter.RoomId | Ошибка параметра RoomId. |
| InvalidParameter.SdkAppId | Ошибка параметра SdkAppId. |
| InvalidParameterValue.RoomId | Неверное значение RoomId. |
| MissingParameter.RoomId | Отсутствует параметр RoomId. |
| MissingParameter.SdkAppId | Отсутствует параметр SdkAppId. |
| UnauthorizedOperation.SdkAppId | Нет прав на операцию с SdkAppId. |


---
*Источник: [https://trtc.io/document/64160](https://trtc.io/document/64160)*

---
*Источник (EN): [end-calls.md](./end-calls.md)*

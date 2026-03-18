# Коды ошибок

## Описание функции

Если в ответе присутствует поле Error, это означает, что вызов API не выполнен. Например:

```
 {
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "The provided credentials could not be validated. Please check your signature is correct."
        },
        "RequestId": "ed93f3cb-f35e-473f-b9f3-0d451b8b79c6"
    }
}
```

Код в Error указывает на код ошибки, а Message содержит подробную информацию об ошибке.

## Список кодов ошибок

### Общие коды ошибок

| Код ошибки | Описание |
| --- | --- |
| ActionOffline | Этот API больше не используется. |
| AuthFailure.InvalidAuthorization | `Authorization` в заголовке запроса недействителен. |
| AuthFailure.InvalidSecretId | Неверный ключ (не тип ключа TencentCloud API). |
| AuthFailure.MFAFailure | Ошибка MFA. |
| AuthFailure.SecretIdNotFound | Ключ не существует. Проверьте, был ли ключ удален или отключен в консоли, и если нет, проверьте, правильно ли введен ключ. Обратите внимание, что перед ключом и после него не должно быть пробелов. |
| AuthFailure.SignatureExpire | Подпись истекла. Разница между временем метки и временем сервера не должна превышать пять минут. Убедитесь, что текущее местное время соответствует стандартному времени. |
| AuthFailure.SignatureFailure | Неверная подпись. Ошибка при расчете подписи. Убедитесь, что вы выполнили процесс расчета подписи, описанный в документации API подписей. |
| AuthFailure.TokenFailure | Ошибка токена. |
| AuthFailure.UnauthorizedOperation | Запрос не авторизован. Для получения дополнительной информации см. документацию [CAM](https://intl.cloud.tencent.com/document/product/598). |
| DryRunOperation | Операция DryRun. Это означает, что запрос был бы успешным, но использовался параметр DryRun. |
| FailedOperation | Операция не выполнена. |
| InternalError | Внутренняя ошибка. |
| InvalidAction | API не существует. |
| InvalidParameter | Неправильный параметр. |
| InvalidParameterValue | Неверное значение параметра. |
| InvalidRequest | Неправильный формат многокомпонентного тела запроса. |
| IpInBlacklist | Ваш IP находится в черном списке UIN. |
| IpNotInWhitelist | Ваш IP не находится в белом списке UIN. |
| LimitExceeded | Превышено ограничение квоты. |
| MissingParameter | Отсутствует параметр. |
| NoSuchProduct | Продукт не существует. |
| NoSuchVersion | Версия API не существует. |
| RequestLimitExceeded | Количество запросов превышает предел частоты. |
| RequestLimitExceeded.GlobalRegionUinLimitExceeded | UIN превышает предел частоты. |
| RequestLimitExceeded.IPLimitExceeded | Количество запросов по IP превышает предел частоты. |
| RequestLimitExceeded.UinLimitExceeded | Количество запросов по UIN превышает предел частоты. |
| RequestSizeLimitExceeded | Размер запроса превышает верхний предел. |
| ResourceInUse | Ресурс используется. |
| ResourceInsufficient | Недостаточно ресурсов. |
| ResourceNotFound | Ресурс не найден. |
| ResourceUnavailable | Ресурс недоступен. |
| ResponseSizeLimitExceeded | Размер ответа превышает верхний предел. |
| ServiceUnavailable | Сервис сейчас недоступен. |
| UnauthorizedOperation | Неавторизованная операция. |
| UnknownParameter | Неизвестный параметр. |
| UnsupportedOperation | Неподдерживаемая операция. |
| UnsupportedProtocol | Ошибка протокола HTTP(S) запроса; поддерживаются только запросы GET и POST. |
| UnsupportedRegion | API не поддерживает запрашиваемый регион. |

### Коды ошибок сервиса

| Код ошибки | Описание |
| --- | --- |
| AuthFailure | Ошибка подписи/аутентификации CAM. |
| AuthFailure.UnRealNameAuthenticated | Проверка личности не завершена, поэтому эта операция не разрешена. |
| AuthFailure.UnsupportedOperation | Неподдерживаемая операция. |
| FailedOperation.CRUnsupportMethod | Неподдерживаемый метод облачной записи. |
| FailedOperation.CSUnsupportMethod | Метод облачного нарезания не поддерживается. |
| FailedOperation.NotAbility | Необходимо разблокировать требуемую возможность |
| FailedOperation.NotAllowed | Эта операция не разрешена, пожалуйста, отправьте тикет для связи с нами |
| FailedOperation.NotRtmpFunction | RTMP не включен. |
| FailedOperation.QueryTaskInfoFailed | Ошибка при запросе задачи |
| FailedOperation.RestrictedConcurrency | Достигнуто максимальное количество одновременных задач облачной записи. Свяжитесь с нами, чтобы повысить ограничение. |
| FailedOperation.RoomNotExist | Комната не существует. |
| FailedOperation.SdkAppIdNotExist | Идентификатор приложения не существует. |
| FailedOperation.SdkAppIdNotUnderAppId | Нет ресурса для этого SdkAppId в этом AppId |
| FailedOperation.TaskExist | Задача уже существует |
| FailedOperation.TaskFinished | Задача завершена при вызове интерфейса. |
| FailedOperation.TaskNotExist | Задача не существует или остановлена. |
| FailedOperation.UserNotExist | Пользователь не находится в комнате. |
| InternalError.CRInternalError | Внутренняя ошибка облачной записи. |
| InternalError.CSInternalError | Внутренняя ошибка сервиса облачного нарезания. |
| InternalError.DBError | При запросе базы данных произошла ошибка. |
| InternalError.EsQueryError | При выполнении запроса ES произошла ошибка. |
| InternalError.GetRoomCacheIpError | Ошибка при запросе информации о комнате. |
| InternalError.GetRoomFromCacheError | Ошибка при получении информации о комнате. |
| InternalError.HttpParaseFalied | Ошибка при разборе HTTP запроса. |
| InternalError.HttpParseFailed | Ошибка при разборе HTTP запроса. |
| InternalError.InterfaceErr | Ошибка API. |
| InternalError.InternalError | Внутренняя ошибка, пожалуйста, повторите попытку. |
| InternalError.MethodErr | Неподдерживаемый метод. |
| InternalError.UserNotExist | Пользователь не находится в комнате. |
| InvalidParameter.BodyParamsError | Ошибка при разборе параметров тела запроса. |
| InvalidParameter.EncodeParams | Неверный `EncodeParams`. |
| InvalidParameter.EndTs | Неверный `EndTs`. |
| InvalidParameter.OutOfRange | Значение параметра выходит за допустимый диапазон. |
| InvalidParameter.PageNumber | Неверный `PageNumber`. |
| InvalidParameter.PageSize | Неверный `PageSize`. |
| InvalidParameter.PageSizeOversize | Значение `PageSize` превышает 100. |
| InvalidParameter.QueryScaleOversize | Период запроса превышает ограничение. |
| InvalidParameter.RoomId | `RoomId` неправильный. |
| InvalidParameter.SdkAppId | `SdkAppId` неправильный. |
| InvalidParameter.SdkAppid | Неработающий `SdkAppid`. |
| InvalidParameter.StartTimeExpire | Время начала запроса превысило ограничение. |
| InvalidParameter.StartTimeOversize | Время начала запроса превышает диапазон, разрешенный текущей версией панели мониторинга. Дополнительные сведения см. на https://intl.cloud.tencent.com/document/product/647/81331?from_cn_redirect=1 |
| InvalidParameter.StartTs | Неверный `StartTs`. |
| InvalidParameter.StartTsOversize | Время начала запроса превысило ограничение. |
| InvalidParameter.StrRoomId | Ошибка параметра StrRoomId. |
| InvalidParameter.StreamUrl | Неверный формат StreamUrl |
| InvalidParameter.TaskId | Ошибка параметра TaskId. |
| InvalidParameter.UrlParamsError | Ошибка при разборе параметров URL. |
| InvalidParameter.UserId | Неверный `UserId`. |
| InvalidParameter.UserIds | `UserIds` неправильный. |
| InvalidParameter.UserIdsMorethanSix | Количество пользователей превышает 6. |
| InvalidParameter.UserSig | UserSig истек или неверен |
| InvalidParameter.UserSigNotAdmin | UserSig не является администратором суперпользователя. |
| InvalidParameterValue.RoomId | Неверный RoomId. |
| MissingParameter.AccessKey | Отсутствует параметр `AccessKey`. |
| MissingParameter.AppId | Отсутствует `AppId`. |
| MissingParameter.Bucket | Отсутствует параметр `Bucket`. |
| MissingParameter.CloudStorage | Отсутствует параметр `CloudStorage`. |
| MissingParameter.CommId | Отсутствует `CommId`. |
| MissingParameter.CommIdOrSdkAppId | Отсутствует `SdkAppId` или `CommID`. |
| MissingParameter.EndTs | Отсутствует `endTS_s`. |
| MissingParameter.RecordMode | Отсутствует параметр `RecordMode`. |
| MissingParameter.RecordParams | Отсутствует параметр `RecordParams`. |
| MissingParameter.Region | Отсутствует параметр `Region`. |
| MissingParameter.RoomId | Отсутствует `RoomId`. |
| MissingParameter.RoomNum | Отсутствует `RoomNum`. |
| MissingParameter.SdkAppId | Отсутствует `SdkAppId`. |
| MissingParameter.SecretKey | Отсутствует параметр `SecretKey`. |
| MissingParameter.SliceParams | Требуется параметр SliceParams. |
| MissingParameter.SliceStorageParams | Требуется параметр SliceStorageParams. |
| MissingParameter.SliceType | Требуется параметр SliceType. |
| MissingParameter.StartTs | Отсутствует `startTS_s`. |
| MissingParameter.StorageParams | Отсутствует параметр `StorageParams`. |
| MissingParameter.StreamType | Отсутствует параметр `StreamType`. |
| MissingParameter.TaskId | Отсутствует параметр `TaskId`. |
| MissingParameter.UserId | Отсутствует параметр `UserId`. |
| MissingParameter.UserIds | Отсутствует `UserIds`. |
| MissingParameter.UserSig | Отсутствует параметр `UserSig`. |
| MissingParameter.Vendor | Отсутствует параметр `Vendor`. |
| ResourceInsufficient.RequestRejection | Недостаточно ресурсов. |
| UnauthorizedOperation.SdkAppId | Нет разрешения на манипулирование `SdkAppId`. |

---
*Источник: [https://trtc.io/document/34270](https://trtc.io/document/34270)*

---
*Источник (EN): [error-codes.md](./error-codes.md)*

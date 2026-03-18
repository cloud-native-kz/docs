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

Code в Error указывает код ошибки, а Message содержит подробную информацию об ошибке.

## Список кодов ошибок

### Общие коды ошибок

| Код ошибки | Описание |
| --- | --- |
| ActionOffline | Этот API был объявлен устаревшим. |
| AuthFailure.InvalidAuthorization | `Authorization` в заголовке запроса является недействительным. |
| AuthFailure.InvalidSecretId | Недействительный ключ (не является типом ключа API TencentCloud). |
| AuthFailure.MFAFailure | Ошибка многофакторной аутентификации. |
| AuthFailure.SecretIdNotFound | Ключ не существует. Проверьте, был ли ключ удален или отключен в консоли, и если нет, проверьте, правильно ли введен ключ. Обратите внимание, что перед ключом и после него не должно быть пробелов. |
| AuthFailure.SignatureExpire | Подпись истекла. Разница между временной меткой и временем сервера не должна превышать пять минут. Пожалуйста, убедитесь, что текущее локальное время совпадает со стандартным временем. |
| AuthFailure.SignatureFailure | Недействительная подпись. Ошибка расчета подписи. Пожалуйста, убедитесь, что вы следуете процессу расчета подписи, описанному в документации API Signature. |
| AuthFailure.TokenFailure | Ошибка токена. |
| AuthFailure.UnauthorizedOperation | Запрос не авторизован. Дополнительную информацию см. в документации [CAM](https://intl.cloud.tencent.com/document/product/598). |
| DryRunOperation | Операция DryRun. Это означает, что запрос был бы успешным, но был использован параметр DryRun. |
| FailedOperation | Ошибка операции. |
| InternalError | Внутренняя ошибка. |
| InvalidAction | API не существует. |
| InvalidParameter | Неверный параметр. |
| InvalidParameterValue | Недействительное значение параметра. |
| InvalidRequest | Формат многочастного тела запроса неправильный. |
| IpInBlacklist | Ваш IP находится в чёрном списке IP uin. |
| IpNotInWhitelist | Ваш IP не находится в белом списке IP uin. |
| LimitExceeded | Превышено ограничение квоты. |
| MissingParameter | Отсутствует параметр. |
| NoSuchProduct | Продукт не существует. |
| NoSuchVersion | Версия API не существует. |
| RequestLimitExceeded | Число запросов превышает лимит частоты. |
| RequestLimitExceeded.GlobalRegionUinLimitExceeded | Uin превышает лимит частоты. |
| RequestLimitExceeded.IPLimitExceeded | Число запросов IP превышает лимит частоты. |
| RequestLimitExceeded.UinLimitExceeded | Число запросов uin превышает лимит частоты. |
| RequestSizeLimitExceeded | Размер запроса превышает верхний лимит. |
| ResourceInUse | Ресурс используется. |
| ResourceInsufficient | Недостаточно ресурсов. |
| ResourceNotFound | Ресурс не существует. |
| ResourceUnavailable | Ресурс недоступен. |
| ResponseSizeLimitExceeded | Размер ответа превышает верхний лимит. |
| ServiceUnavailable | Сервис в настоящее время недоступен. |
| UnauthorizedOperation | Неавторизованная операция. |
| UnknownParameter | Неизвестный параметр. |
| UnsupportedOperation | Неподдерживаемая операция. |
| UnsupportedProtocol | Ошибка протокола HTTP(S) запроса; поддерживаются только запросы GET и POST. |
| UnsupportedRegion | API не поддерживает запрошенный регион. |

### Коды ошибок сервиса

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.AiTranscodeOptionFail | Ошибка при работе с API AI. |
| FailedOperation.AlterTaskState | Ошибка при изменении статуса задачи. |
| FailedOperation.AuthError | У вас нет прав для выполнения этой операции. |
| FailedOperation.CallOtherSvrError | Ошибка при вызове сторонней службы. |
| FailedOperation.CallOtherSvrFailed | Ошибка при вызове внутренней службы. |
| FailedOperation.CancelSessionNotExist | Отмененная сессия микширования потока не существует. |
| FailedOperation.CannotBeDeletedIssued | Ошибка удаления сертификата, так как он был выдан. |
| FailedOperation.CannotBeDeletedWithinHour | Бесплатные сертификаты не могут быть удалены в течение одного часа после подачи заявки. |
| FailedOperation.CertificateExists | Сертификат уже существует. |
| FailedOperation.CertificateInvalid | Сертификат является недействительным. |
| FailedOperation.CertificateMismatch | Сертификат и приватный ключ не совпадают. |
| FailedOperation.CertificateNotFound | Сертификат не существует. |
| FailedOperation.ConfInUsed | Шаблон используется. |
| FailedOperation.ConfigCDNFailed | Ошибка конфигурации CDN. |
| FailedOperation.CosBucketNotExist | Бакет COS не существует. |
| FailedOperation.CosBucketNotPermission | У вас нет разрешения на доступ к бакету COS. |
| FailedOperation.CosRoleNotExists | Роль COS не существует. Пожалуйста, перейдите на страницу "Feature Configuration > Live Screencapture & Porn Detection" в консоли CSS для предоставления разрешения. |
| FailedOperation.DeleteDomainInLockedTime | Доменное имя не может быть удалено, потому что в последние 2 дня оно генерировало трафик и находится в заблокированном состоянии. |
| FailedOperation.DomainAdded | Доменное имя уже было добавлено. |
| FailedOperation.DomainGslbFail | Ошибка конфигурации правила доменного имени. |
| FailedOperation.DomainNeedRealName | Доменное имя не проверено. |
| FailedOperation.DomainNeedVerifyOwner | Право собственности на доменное имя не проверено. |
| FailedOperation.ExceedsFreeLimit | Число бесплатных сертификатов превышает лимит. |
| FailedOperation.GetPictureUrlError | Невозможно получить URL водяного знака. |
| FailedOperation.GetStreamResolutionError | Ошибка при получении длины и ширины входного потока. |
| FailedOperation.HasNotLivingStream | Нет потока в реальном времени. |
| FailedOperation.HostOutLimit | Число доменных имен превышает верхний лимит (100). |
| FailedOperation.InvalidCertificateStatusCode | Недействительный статус сертификата. |
| FailedOperation.InvalidParam | Неверный параметр. |
| FailedOperation.InvokeVideoApiFail | Произошло исключение при работе с API VOD. |
| FailedOperation.JiFeiNoEnoughFund | Платежная платформа вернула ошибку недостаточного баланса. |
| FailedOperation.NetworkError | Система CA занята. Повторите попытку позже. |
| FailedOperation.NoProjectPermission | У вас нет разрешения на работу с этим проектом. |
| FailedOperation.NoRealNameAuth | Вы не завершили проверку личности. |
| FailedOperation.NotFound | Записи не найдены. |
| FailedOperation.ParentDomainAdded | Родительское доменное имя уже было добавлено. |
| FailedOperation.ProcessMixError | Ошибка при запуске микширования потока. |
| FailedOperation.QueryUploadInfoFailed | Ошибка при запросе информации о загрузке. |
| FailedOperation.RuleAlreadyExist | Правило уже существует. |
| FailedOperation.SdkNoPackage | У пользователя нет действительного пакета трафика. |
| FailedOperation.StreamNotExist | Поток не существует. |
| FailedOperation.SubDomainAdded | Поддоменное имя уже было добавлено. |
| FailedOperation.TagUnbindError | Ошибка отвязки тега. Попробуйте отвязать его вручную. |
| InternalError.ArgsNotMatch | Для API добавления шаблона транскодирования. |
| InternalError.CallOtherSvrError | Ошибка при вызове внутренней службы. |
| InternalError.ChineseCharacterDetected | Китайские доменные имена в настоящее время не поддерживаются. Пожалуйста, проверьте формат доменного имени. |
| InternalError.ConfInUsed | Шаблон используется. |
| InternalError.ConfNotFound | Шаблон не существует. |
| InternalError.ConfOutLimit | Число шаблонов превышает лимит. |
| InternalError.ConfigNotExist | Конфигурация не существует. |
| InternalError.ConnectDbError | Ошибка подключения к базе данных. |
| InternalError.CrtDateInUsing | Сертификат используется. |
| InternalError.CrtDateNotFound | Сертификат не существует. |
| InternalError.CrtDateNotLegal | Сертификат является недействительным. |
| InternalError.CrtDateOverdue | Сертификат истек. |
| InternalError.CrtDomainNotFound | Нет связанного доменного имени. |
| InternalError.CrtKeyNotMatch | Ключ сертификата не совпадает. |
| InternalError.DBError | Ошибка выполнения БД. |
| InternalError.DomainAlreadyExist | Доменное имя уже подключено в другом месте. Пожалуйста, проверьте, правильно ли введено доменное имя, и если да, вы можете добавить его снова после успешной проверки прав собственности. |
| InternalError.DomainFormatError | Формат доменного имени неправильный. Пожалуйста, введите правильное доменное имя. |
| InternalError.DomainGslbFail | Ошибка при добавлении правила GSLB. |
| InternalError.DomainIsFamous | Доменное имя уже подключено в другом месте. Пожалуйста, проверьте, правильно ли введено доменное имя, и если да, вы можете добавить его снова после успешной проверки прав собственности. |
| InternalError.DomainIsLimited | Ваше доменное имя недоступно. Пожалуйста, введите правильное доменное имя. |
| InternalError.DomainNoRecord | Доменное имя не имеет регистрации ICP. |
| InternalError.DomainNotExist | Доменное имя не существует. |
| InternalError.DomainTooLong | Длина доменного имени превышает лимит. |
| InternalError.GetBizidError | Ошибка при получении учетной записи пользователя. |
| InternalError.GetConfigError | Ошибка при получении конфигурации. |
| InternalError.GetStreamInfoError | Ошибка при получении информации о потоке. |
| InternalError.GetUpstreamInfoError | Ошибка при получении информации об источнике потока в реальном времени. |
| InternalError.GetWatermarkError | Произошла ошибка при получении водяного знака. |
| InternalError.HasNotLivingStream | Нет потока в реальном времени. |
| InternalError.InvalidInput | Проверка параметра не выполнена. |
| InternalError.InvalidRequest | Неверный запрос. |
| InternalError.InvalidUser | Ошибка информации об учетной записи. |
| InternalError.JiFeiOtherError | Платежная платформа вернула другие ошибки. |
| InternalError.NetworkError | Внутренняя ошибка сети. |
| InternalError.NotFound | Запись не существует. |
| InternalError.NotPermmitOperat | Нет разрешения на работу. |
| InternalError.PlayDomainNoRecord | Доменное имя воспроизведения не существует. |
| InternalError.ProcessorAlreadyExist | Имя шаблона транскодирования уже существует. |
| InternalError.PushDomainNoRecord | Доменное имя отправки не существует. |
| InternalError.QueryProIspPlayInfoError | Ошибка при запросе информации о воспроизведении по ISP и округам. |
| InternalError.QueryUploadInfoFailed | Ошибка при запросе информации о загрузке. |
| InternalError.RuleAlreadyExist | Правило уже было настроено. |
| InternalError.RuleInUsing | Правило используется. |
| InternalError.RuleNotFound | Правило не существует. |
| InternalError.RuleOutLimit | Правило превышает лимит. |
| InternalError.StreamStatusError | Исключительный статус потока. |
| InternalError.SystemError | Внутренняя ошибка системы. |
| InternalError.UpdateDataError | Ошибка при обновлении данных. |
| InternalError.WatermarkAddError | Ошибка при добавлении водяного знака. |
| InternalError.WatermarkEditError | Внутренняя ошибка при изменении водяного знака. |
| InternalError.WatermarkNotExist | Водяной знак не существует. |
| InvalidParameter.ArgsNotMatch | Неверное имя шаблона. |
| InvalidParameter.COSCustomFileNameError | Неверное пользовательское имя файла COS. |
| InvalidParameter.CancelSessionNotExist | Отмененная сессия не существует. |
| InvalidParameter.CloudCrtIdError | Неверный ID сертификата, размещенного в Tencent Cloud. |
| InvalidParameter.CloudDomainIsStop | Подарочное доменное имя Tencent Cloud истекло. |
| InvalidParameter.ConfInUsed | Шаблон используется. |
| InvalidParameter.ConfNotFound | Конфигурация не найдена. |
| InvalidParameter.CrtDateInUsing | Сертификат используется. |
| InvalidParameter.CrtDateNotFound | Сертификат не существует. |
| InvalidParameter.CrtDateNotLegal | Сертификат является недействительным. |
| InvalidParameter.CrtDateOverdue | Сертификат истек. |
| InvalidParameter.CrtDomainNotFound | Невозможно найти доменное имя. |
| InvalidParameter.CrtKeyNotMatch | Ключ сертификата не совпадает. |
| InvalidParameter.CrtOrKeyNotExist | Содержимое сертификата или приватный ключ не были предоставлены. |
| InvalidParameter.DomainAlreadyExist | Доменное имя уже существует. |
| InvalidParameter.DomainFormatError | Формат доменного имени неправильный. Пожалуйста, введите правильное доменное имя. |
| InvalidParameter.DomainHitBlackList | Это доменное имя находится в чёрном списке. |
| InvalidParameter.DomainIsFamous | Используется доменное имя из чёрного списка. |
| InvalidParameter.DomainIsLimited | Доменное имя ограничено. Пожалуйста, отправьте тикет для подачи заявки на удаление ограничений. |
| InvalidParameter.DomainTooLong | Доменное имя превышает лимит длины. |
| InvalidParameter.GopMustEqualAndExists | GOP шаблона адаптивной скорости передачи является обязательным и должен быть одинаковым для каждого потока. |
| InvalidParameter.InputNumLimitExceeded | Число входов превышает лимит. |
| InvalidParameter.InvalidBackgroudResolution | Неверная длина и ширина фона. |
| InvalidParameter.InvalidBackupToUrl | Неверный BackupToUrl. |
| InvalidParameter.InvalidBitrate | Неверная скорость передачи вывода. |
| InvalidParameter.InvalidCallbackUrl | Неверный URL обратного вызова. |
| InvalidParameter.InvalidCropParam | Обрезанная область выходит за границы исходного изображения. |
| InvalidParameter.InvalidLayerParam | Неверный параметр слоя. |
| InvalidParameter.InvalidMixInputParam | Неверные входные параметры для микширования потока. |
| InvalidParameter.InvalidOutputParam | Неверные параметры выходного потока. |
| InvalidParameter.InvalidOutputStreamID | ID выходного потока уже используется. |
| InvalidParameter.InvalidOutputType | Неверный тип вывода. Пожалуйста, проверьте, совпадают ли `OutputPram-StreamId` и `OutputType`. |
| InvalidParameter.InvalidPictureID | ID водяного знака не был установлен. |
| InvalidParameter.InvalidRoundRectRadius | Неверный радиус скругления угла скругленного прямоугольника. |
| InvalidParameter.InvalidSourceUrl | Неверный исходный URL. |
| InvalidParameter.InvalidTaskTime | Период времени задачи превышает лимит. |
| InvalidParameter.InvalidToUrl | Неверный URL назначения. |
| InvalidParameter.InvalidVodFileName | Неверный `VodFileName`. |
| InvalidParameter.InvalidWatermark | Неверный параметр водяного знака. |
| InvalidParameter.MpHostDelete | Не допускается добавление доменного имени мини-программы, удаленного в том же месяце. |
| InvalidParameter.MpPluginNoUse | Плагин WeChat Mini Program не авторизован. |
| InvalidParameter.OtherError | Другие ошибки. |
| InvalidParameter.ProcessorAlreadyExist | Шаблон транскодирования уже существует. |
| InvalidParameter.RuleNotFound | Правило не найдено. |
| InvalidParameter.SessionOutputStreamChanged | Выходной поток одной сессии изменился. |
| InvalidParameter.TaskNotExist | Задача не существует. |
| InvalidParameter.TaskNumMoreThanLimit | Число задач достигло лимита. |
| InvalidParameter.TemplateNotMatchInputNum | Шаблон не совпадает с числом входных потоков. |
| InvalidParameter.ToUrlNoPermission | Нет разрешения на доступ к внешнему URL. |
| InvalidParameter.UrlNotSafe | Ошибка при разрешении доменного имени. |
| LimitExceeded.MaximumRunningTask | Текущее число одновременных задач превышает лимит. |
| LimitExceeded.MaximumTask | Число созданных задач в день превышает лимит. |
| LimitExceeded.RateLimitExceeded | Достигнут лимит частоты вызовов API. |
| ResourceNotFound.ChannelNotExist | Канал не существует. |
| ResourceNotFound.CrtDateNotFound | Сертификат не существует. |
| ResourceNotFound.CrtDomainNotFound | Сертификат не найден. |
| ResourceNotFound.DomainNoRecord | Доменное имя не имеет регистрации ICP. |
| ResourceNotFound.DomainNotExist | Доменное имя не существует или не совпадает. |
| ResourceNotFound.EmptyData | Данные пусты. |
| ResourceNotFound.ForbidService | Вы заблокированы. |
| ResourceNotFound.FreezeService | Сервис приостановлен. |
| ResourceNotFound.InvalidUser | Этот API не поддерживается для пользователя. |
| ResourceNotFound.PlayDomainNoRecord | Доменное имя воспроизведения не существует. |
| ResourceNotFound.PushDomainNoRecord | Доменное имя отправки не существует. |
| ResourceNotFound.StopService | Сервис был приостановлен из-за задолженности по счету. Пожалуйста, пополните счет до положительного баланса, чтобы сначала активировать сервис. |
| ResourceNotFound.TaskId | `TaskId` не существует. |
| ResourceNotFound.UserDisableService | Вы отключили сервис. |
| ResourceNotFound.UserNotExist | Сервис CSS не был активирован. |
| ResourceNotFound.UserNotFount | Пользователь не существует. |
| ResourceNotFound.WatermarkNotExist | Водяной знак не существует. |
| ResourceUnavailable.InvalidVodStatus | Сервис VOD не был активирован. |
| ResourceUnavailable.StreamNotExist | Поток не существует. |
| UnsupportedOperation.NotLVBCodeMode | Не режим LVB кода/новая консоль |


---
*Источник: [https://www.tencentcloud.com/document/product/267/30851](https://www.tencentcloud.com/document/product/267/30851)*

---
*Источник (EN): [error-codes.md](./error-codes.md)*

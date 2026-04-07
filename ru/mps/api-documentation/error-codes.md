# Коды ошибок

## Описание функции

Если в ответе присутствует поле Error, это означает, что вызов API не удался. Например:

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

Code в Error указывает на код ошибки, а Message содержит подробную информацию об ошибке.

## Список кодов ошибок

### Распространённые коды ошибок

| Код ошибки | Описание |
| --- | --- |
| ActionOffline | Этот API был объявлен устаревшим. |
| AuthFailure.InvalidAuthorization | `Authorization` в заголовке запроса недействителен. |
| AuthFailure.InvalidSecretId | Недействительный ключ (не является типом ключа TencentCloud API). |
| AuthFailure.MFAFailure | Ошибка MFA. |
| AuthFailure.SecretIdNotFound | Ключ не существует. Проверьте, не был ли ключ удалён или отключен в консоли, а если нет, убедитесь, что ключ введён правильно. Обратите внимание, что перед ключом и после него не должно быть пробелов. |
| AuthFailure.SignatureExpire | Подпись истекла. Временная метка и время сервера не должны отличаться более чем на пять минут. Убедитесь, что ваше текущее локальное время совпадает со стандартным временем. |
| AuthFailure.SignatureFailure | Недействительная подпись. Ошибка при расчёте подписи. Убедитесь, что вы следовали процессу расчёта подписи, описанному в документации по API подписи. |
| AuthFailure.TokenFailure | Ошибка токена. |
| AuthFailure.UnauthorizedOperation | Запрос не авторизован. Дополнительную информацию см. в документации [CAM](https://intl.cloud.tencent.com/document/product/598). |
| DryRunOperation | Операция DryRun. Это означает, что запрос был бы успешным, но был использован параметр DryRun. |
| FailedOperation | Операция не удалась. |
| InternalError | Внутренняя ошибка. |
| InvalidAction | API не существует. |
| InvalidParameter | Некорректный параметр. |
| InvalidParameterValue | Недействительное значение параметра. |
| InvalidRequest | Формат многочастного тела запроса некорректен. |
| IpInBlacklist | Ваш IP находится в чёрном списке IP uin. |
| IpNotInWhitelist | Ваш IP не находится в белом списке IP uin. |
| LimitExceeded | Превышено ограничение квоты. |
| MissingParameter | Отсутствует параметр. |
| NoSuchProduct | Продукт не существует. |
| NoSuchVersion | Версия API не существует. |
| RequestLimitExceeded | Количество запросов превышает предел частоты. |
| RequestLimitExceeded.GlobalRegionUinLimitExceeded | Uin превышает предел частоты. |
| RequestLimitExceeded.IPLimitExceeded | Количество запросов IP превышает предел частоты. |
| RequestLimitExceeded.UinLimitExceeded | Количество запросов uin превышает предел частоты. |
| RequestSizeLimitExceeded | Размер запроса превышает верхний предел. |
| ResourceInUse | Ресурс используется. |
| ResourceInsufficient | Недостаточно ресурсов. |
| ResourceNotFound | Ресурс не существует. |
| ResourceUnavailable | Ресурс недоступен. |
| ResponseSizeLimitExceeded | Размер ответа превышает верхний предел. |
| ServiceUnavailable | Сервис сейчас недоступен. |
| UnauthorizedOperation | Неавторизованная операция. |
| UnknownParameter | Неизвестный параметр. |
| UnsupportedOperation | Неподдерживаемая операция. |
| UnsupportedProtocol | Ошибка протокола HTTP(S); поддерживаются только запросы GET и POST. |
| UnsupportedRegion | API не поддерживает запрашиваемый регион. |

### Коды ошибок сервиса

| Код ошибки | Описание |
| --- | --- |
| FailedOperation.BucketNotifyAlreadyExist | Операция не удалась: уведомление уже установлено для бакета. |
| FailedOperation.CosStatusInavlid | Операция не удалась: сервис COS приостановлен. |
| FailedOperation.GenerateResource | Ошибка при создании ресурса. |
| FailedOperation.GetSourceNotify | Операция не удалась: ошибка получения исходного уведомления. |
| FailedOperation.InvalidMpsUser | Операция не удалась: неавторизованный пользователь MPS. |
| FailedOperation.InvalidUser | Операция не удалась: недействительный пользователь. |
| FailedOperation.NetWorkError | Операция не удалась из-за ошибки сети. |
| FailedOperation.SetSourceNotify | Операция не удалась: ошибка установки исходного уведомления. |
| InternalError.AccessDBError | Ошибка данных. |
| InternalError.GenDefinition | Внутренняя ошибка: ошибка при создании ID шаблона. |
| InternalError.RecognitionError | Ошибка распознавания. |
| InternalError.UploadWatermarkError | Внутренняя ошибка: ошибка при загрузке изображения водяного знака. |
| InvalidParameter.Id | InvalidParameter.Id |
| InvalidParameter.NotFound | InvalidParameter.NotFound |
| InvalidParameterValue.AsrHotWordsConfigure | Значение параметра конфигурации словаря горячих слов неправильно. |
| InvalidParameterValue.AsrHotWordsLibraryId | Значение параметра ID словаря горячих слов неправильно. |
| InvalidParameterValue.AsrHotWordsSwitch | Значение параметра переключателя словаря горячих слов неправильно. |
| InvalidParameterValue.AudioBitrate | Ошибка параметра: битрейт аудиопотока. |
| InvalidParameterValue.AudioChannel | Неправильное значение параметра: AudioChannel. |
| InvalidParameterValue.AudioCodec | Ошибка параметра: кодек аудиопотока. |
| InvalidParameterValue.AudioData | Недействительные аудиоданные. |
| InvalidParameterValue.AudioDataTooLong | Аудиоданные слишком длинные. |
| InvalidParameterValue.AudioFormat | Неподдерживаемый формат аудиоданных. |
| InvalidParameterValue.AudioSampleRate | Ошибка параметра: частота дискретизации аудиопотока. |
| InvalidParameterValue.AutoAreas | Конфигурация для автоматического стирания области шаблона стирания неправильна. |
| InvalidParameterValue.Bitrate | Недействительный битрейт аудио/видео. |
| InvalidParameterValue.BlockConfidence | Неправильное значение параметра: значение параметра `BlockConfidence` недействительно. |
| InvalidParameterValue.ClassifcationConfigure | Неправильное значение параметра: параметр поля управления для интеллектуальной категоризации неправильно. |
| InvalidParameterValue.Codec | Недействительный кодек аудио/видео. |
| InvalidParameterValue.ColumnCount | Неправильное значение параметра: ColumnCount. |
| InvalidParameterValue.Comment | Ошибка параметра: описание шаблона. |
| InvalidParameterValue.Container | Ошибка параметра: формат контейнера. |
| InvalidParameterValue.ContainerType | Неправильное значение параметра: ContainerType. |
| InvalidParameterValue.CoordinateOrigin | Неправильное значение параметра: CoordinateOrigin. |
| InvalidParameterValue.CoverConfigure | Неправильное значение параметра: параметр поля управления для интеллектуального создания обложки неправильно. |
| InvalidParameterValue.CustomAreas | Указанная область шаблона стирания неправильна. |
| InvalidParameterValue.DefaultLibraryLabelSet | Неправильное значение параметра: тег фильтра библиотеки лиц по умолчанию недействителен. |
| InvalidParameterValue.Definition | Ошибка параметра: Definition. |
| InvalidParameterValue.Definitions | Ошибка параметра: Definitions. |
| InvalidParameterValue.DeleteDefaultTemplate | Неправильное значение параметра: шаблон по умолчанию не может быть удалён. |
| InvalidParameterValue.DestinationLanguage | Ошибка параметра DestinationLanguage. |
| InvalidParameterValue.DisableHigherVideoBitrate | Недействительное значение переключателя для запрета транскодирования с низкого битрейта на высокий. |
| InvalidParameterValue.DisableHigherVideoResolution | Недействительное значение переключателя для запрета транскодирования с низкого разрешения на высокое. |
| InvalidParameterValue.DuplicatedTextContent | Дублированный текст водяного знака. |
| InvalidParameterValue.EmptyDetectItem | Включённые элементы обнаружения шаблона пусты. |
| InvalidParameterValue.ErasePrivacyConfig | Конфигурация защиты конфиденциальности шаблона стирания неправильна. |
| InvalidParameterValue.EraseSubtitleConfig | Конфигурация стирания субтитров шаблона стирания неправильна. |
| InvalidParameterValue.EraseType | Тип стирания шаблона стирания неправильно. |
| InvalidParameterValue.EraseWatermarkConfig | Конфигурация стирания водяного знака шаблона стирания неправильна. |
| InvalidParameterValue.FaceDuplicate | Неправильное значение параметра: дублированное лицо. |
| InvalidParameterValue.FaceLibrary | Неправильное значение параметра: недействительный параметр библиотеки лиц. |
| InvalidParameterValue.FaceScore | Неправильное значение параметра: значение параметра оценки лица недействительно. |
| InvalidParameterValue.FillType | Недействительный параметр: некорректный тип заполнения. |
| InvalidParameterValue.Format | Неправильное значение параметра: Format. |
| InvalidParameterValue.FormatWebpLackWidthAndHeight | Неправильное значение параметра: `Format` имеет значение `webp`, но оба `Width` и `Height` пусты. |
| InvalidParameterValue.FormatWebpWidthAndHeightBothZero | Неправильное значение параметра: когда `Format` имеет значение `webp`, `Width` и `Height` не могут быть оба 0. |
| InvalidParameterValue.Fps | Ошибка параметра: частота кадров видео. |
| InvalidParameterValue.FrameTagConfigure | Неправильное значение параметра: параметр поля управления для интеллектуального тегирования конкретных кадров неправильно. |
| InvalidParameterValue.FunctionArg | Неправильное значение параметра: FunctionArg. |
| InvalidParameterValue.FunctionName | Неправильное значение параметра: FunctionName. |
| InvalidParameterValue.Gop | Недействительное значение GOP. |
| InvalidParameterValue.Height | Ошибка параметра: высота. |
| InvalidParameterValue.HotWordsNotExist | Ошибка параметра. Словарь горячих слов не существует. |
| InvalidParameterValue.HotwordsFormatError | Ошибка формата словаря горячих слов. см. документ инструкции конфигурации горячих слов (https://intl.cloud.tencent.com/document/product/862/116244?from_cn_redirect=1#afc37e17-2786-4289-9bc3-8e24435d3f45). |
| InvalidParameterValue.ImageContent | Недействительный ImageContent |
| InvalidParameterValue.ImageTemplate | Ошибка параметра: шаблон водяного знака изображения. |
| InvalidParameterValue.InputInfo | Неправильные входные параметры. |
| InvalidParameterValue.InvalidContent | Значение проанализированного `Content` недействительно. |
| InvalidParameterValue.InvalidOperationType | Недействительный тип операции. |
| InvalidParameterValue.LabelSet | Неправильное значение параметра: недействительное значение `LabelSet`. |
| InvalidParameterValue.Limit | Ошибка параметра: Limit. |
| InvalidParameterValue.ModifyDefaultTemplate | Неправильное значение параметра: шаблон по умолчанию не может быть изменён. |
| InvalidParameterValue.Name | Неправильное значение параметра: `Name` превышает ограничение длины. |
| InvalidParameterValue.NotProcessingTask | Задачи, не находящиеся в статусе обработки, не поддерживаются. |
| InvalidParameterValue.ObjectLibrary | Неправильное значение параметра: параметр библиотеки объектов недействителен. |
| InvalidParameterValue.OcrSwitch | Неправильное значение параметра: значение параметра OcrSwitch недействительно. |
| InvalidParameterValue.PicFormatError | Неправильное значение параметра: некорректный формат изображения лица. |
| InvalidParameterValue.PrivacyModel | Модель защиты конфиденциальности шаблона стирания неправильна. |
| InvalidParameterValue.PrivacyTargets | Цель защиты конфиденциальности шаблона стирания неправильна. |
| InvalidParameterValue.Quality | Неправильное значение параметра: Quality. |
| InvalidParameterValue.RemoveAudio | Неправильное значение параметра: RemoveAudio. |
| InvalidParameterValue.RemoveVideo | Неправильное значение параметра: RemoveVideo. |
| InvalidParameterValue.RepeatType | Ошибка параметра: недействительный `RepeatType`. |
| InvalidParameterValue.Resolution | Ошибка параметра: Некорректное разрешение. |
| InvalidParameterValue.ResolutionAdaptive | Недействительный ResolutionAdaptive |
| InvalidParameterValue.ReviewConfidence | Неправильное значение параметра: Значение параметра `ReviewConfidence` недействительно. |
| InvalidParameterValue.RowCount | Неправильное значение параметра: RowCount. |
| InvalidParameterValue.SampleInterval | Неправильное значение параметра: SampleInterval. |
| InvalidParameterValue.SampleRate | Недействительная частота дискретизации аудио. |
| InvalidParameterValue.SampleType | Неправильное значение параметра: SampleType. |
| InvalidParameterValue.Service | Возникает ошибка значения параметра сервиса. |
| InvalidParameterValue.SessionContextTooLong | `SessionContext` слишком длинный. |
| InvalidParameterValue.SessionId | ID дедупликации уже существует. Запрос удалён из-за дублирования. |
| InvalidParameterValue.SessionIdTooLong | `SessionId` слишком длинный. |
| InvalidParameterValue.SoundSystem | Недействительный параметр: некорректная система аудиоканалов. |
| InvalidParameterValue.SourceLanguage | Ошибка параметра SourceLanguage. |
| InvalidParameterValue.SourceText | Возникает ошибка параметра SourceText. |
| InvalidParameterValue.SrcFile | Ошибка исходного файла. |
| InvalidParameterValue.SubtitleEraseMethod | Метод стирания субтитров шаблона стирания неправильно. |
| InvalidParameterValue.SubtitleFormat | Неправильное значение параметра: Значение параметра `SubtitleFormat` недействительно. |
| InvalidParameterValue.SubtitleLang | Язык для стирания субтитров шаблона стирания неправильно. |
| InvalidParameterValue.SubtitleModel | Модель стирания субтитров шаблона стирания неправильна. |
| InvalidParameterValue.SubtitleType | Значение типа языка субтитра неправильно. |
| InvalidParameterValue.SvgTemplate | Неправильное значение параметра: SVG пусто. |
| InvalidParameterValue.SvgTemplateHeight | Неправильное значение параметра: высота SVG. |
| InvalidParameterValue.SvgTemplateWidth | Неправильное значение параметра: ширина SVG. |
| InvalidParameterValue.Switch | Неправильное значение параметра: недействительное значение `Switch`. |
| InvalidParameterValue.TEHDType | Неправильное значение параметра: недействительный `TEHD Type`. |
| InvalidParameterValue.TagConfigure | Неправильное значение параметра: параметр поля управления для интеллектуального тегирования неправильно. |
| InvalidParameterValue.TaskId | ID задачи не существует. |
| InvalidParameterValue.TextAlpha | Ошибка параметра: прозрачность текста. |
| InvalidParameterValue.TextContent | Возникает ошибка значения параметра TextContent. |
| InvalidParameterValue.TextTemplate | Ошибка параметра: текстовый шаблон. |
| InvalidParameterValue.TransDstLang | Конфигурация для целевого языка перевода неправильна в шаблоне стирания субтитров интеллектуального стирания. |
| InvalidParameterValue.TransSwitch | Неправильное значение параметра: значение параметра TransSwitch недействительно. |
| InvalidParameterValue.TranslateDstLanguage | Значение параметра целевого языка неправильно. |
| InvalidParameterValue.TranslateSwitch | Значение параметра переключателя перевода неправильно. |
| InvalidParameterValue.Type | Ошибка параметра: некорректное значение `Type`. |
| InvalidParameterValue.UnknownCategory | Неизвестная категория обнаружения. |
| InvalidParameterValue.UserDefineLibraryLabelSet | Неправильное значение параметра: тег фильтра пользовательской библиотеки лиц недействителен. |
| InvalidParameterValue.VideoBitrate | Ошибка параметра: битрейт видеопотока. |
| InvalidParameterValue.VideoCodec | Ошибка параметра: кодек видеопотока. |
| InvalidParameterValue.VideoSrcLanguage | Значение параметра языка источника видео неправильно. |
| InvalidParameterValue.WatermarkEraseMethod | Метод стирания водяного знака шаблона стирания неправильно. |
| InvalidParameterValue.WatermarkModel | Модель стирания водяного знака шаблона стирания неправильна. |
| InvalidParameterValue.Width | Ошибка параметра: Wwdth. |
| InvalidParameterValue.XPos | Горизонтальное положение начала водяного знака относительно начала координат видео. Поддерживаются форматы % и px. |
| InvalidParameterValue.YPos | Вертикальное положение начала водяного знака относительно начала координат видео. Поддерживаются форматы % и px. |
| LimitExceeded.TooMuchHotWords | Количество созданных словарей горячих слов достигло установленного по умолчанию верхнего предела. |
| LimitExceeded.TooMuchLargeHotWords | Количество созданных больших словарей горячих слов достигло верхнего предела. |
| LimitExceeded.TooMuchTemplate | Достигнут предел: количество шаблонов превышает лимит. |
| ResourceNotFound.CosBucketNameInvalid | Ресурс не существует: недействительное имя бакета COS. |
| ResourceNotFound.CosBucketNotExist | Ресурс не существует: бакет COS не существует. |
| ResourceNotFound.Person | Ресурс не существует: персона. |
| ResourceNotFound.TemplateNotExist | Ресурс не существует: шаблон не существует. |
| ResourceNotFound.UserUnregister | Пользователь не зарегистрирован. |
| ResourceNotFound.Word | Ресурс не существует: Ключевое слово. |
| UnsupportedOperation.TextTooLong | Текст для одного запроса превышает ограничение длины. |


---
*Источник: [https://www.tencentcloud.com/document/product/1041/33691](https://www.tencentcloud.com/document/product/1041/33691)*

---
*Источник (EN): [error-codes.md](./error-codes.md)*

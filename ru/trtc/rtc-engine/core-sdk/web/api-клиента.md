# API клиента

## Сведения об API

### TRTC

1. [TRTC](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html) — это основная точка входа для SDK TRTC, предоставляющая API-интерфейсы, такие как создание экземпляра trtc ([TRTC.create](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#.create)), [TRTC.getCameraList](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#.getCameraList), [TRTC.getMicrophoneList](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#.getMicrophoneList),  [TRTC.isSupported](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#.isSupported).
2. Экземпляр [trtc](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html) предоставляет основные возможности для телефонных звонков с передачей аудио и видео в реальном времени.
  - Вход в комнату [trtc.enterRoom](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#enterRoom)
  - Выход из комнаты [trtc.exitRoom](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#exitRoom)
  - Включение камеры [trtc.startLocalVideo](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startLocalVideo)
  - Включение микрофона [trtc.startLocalAudio](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startLocalAudio)
  - Отключение камеры [trtc.stopLocalVideo](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#stopLocalVideo)
  - Отключение микрофона [trtc.stopLocalAudio](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#stopLocalAudio)
  - Воспроизведение удалённого видео [trtc.startRemoteVideo](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startRemoteVideo)
  - Остановка воспроизведения удалённого видео [trtc.stopRemoteVideo](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#stopRemoteVideo)
  - Отключение/включение звука удалённого пользователя [trtc.muteRemoteAudio](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#muteRemoteAudio)

### Статические методы TRTC

| Имя | Описание |
| --- | --- |
| [create](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#.create) | Создание объекта TRTC для реализации таких функций, как вход в комнату, предпросмотр, передача и получение потоков. |
| [setLogLevel](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#.setLogLevel) | Установка уровня вывода журнала. Рекомендуется устанавливать уровень DEBUG во время разработки и тестирования, включающий подробную информацию. Уровень вывода по умолчанию — INFO, включающий информацию журнала основных функций SDK. |
| [isSupported](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#.isSupported) | Проверка поддержки TRTC Web SDK текущим браузером |
| [getCameraList](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#.getCameraList) | Возврат списка устройств камеры. Примечание |
| [getMicrophoneList](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#.getMicrophoneList) | Возврат списка устройств микрофона. Примечание |
| [getSpeakerList](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#.getSpeakerList) | Возврат списка устройств динамика. В целях безопасности поля label и deviceId могут быть пустыми до авторизации пользователем доступа к камере или микрофону. Поэтому рекомендуется вызвать этот интерфейс для получения сведений об устройстве после авторизации пользователем доступа. |
| [setCurrentSpeaker](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#.setCurrentSpeaker) | Установка текущего динамика для воспроизведения аудио |

### Методы TRTC

| Имя | Описание |
| --- | --- |
| [enterRoom](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#enterRoom) | Вход в видеозвонок в комнату. |
| [exitRoom](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#exitRoom) | Выход из текущей комнаты аудио и видеозвонков. |
| [switchRole](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#switchRole) | Переключение роли пользователя, действует только в режиме интерактивного потокового вещания TRTC.TYPE.SCENE_LIVE. |
| [destroy](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#destroy) | Уничтожение экземпляра TRTC |
| [startLocalAudio](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startLocalAudio) | Начало сбора аудио с локального микрофона и его публикация в текущую комнату. |
| [updateLocalAudio](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#updateLocalAudio) | Обновление конфигурации локального микрофона. |
| [stopLocalAudio](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#stopLocalAudio) | Остановка сбора и публикации локального микрофона. |
| [startLocalVideo](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startLocalVideo) | Начало сбора видео с локальной камеры, воспроизведение видео камеры на указанном теге HTMLElement и публикация видео камеры в текущую комнату. |
| [updateLocalVideo](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#updateLocalVideo) | Обновление конфигурации локальной камеры. |
| [stopLocalVideo](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#stopLocalVideo) | Остановка захвата, предпросмотра и публикации локальной камеры. |
| [startScreenShare](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startScreenShare) | Начало общего доступа к экрану. |
| [updateScreenShare](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#updateScreenShare) | Обновление конфигурации общего доступа к экрану |
| [stopScreenShare](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#stopScreenShare) | Остановка общего доступа к экрану. |
| [startRemoteVideo](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startRemoteVideo) | Воспроизведение удалённого видео |
| [updateRemoteVideo](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#updateRemoteVideo) | Обновление конфигурации воспроизведения удалённого видео |
| [stopRemoteVideo](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#stopRemoteVideo) | Остановка воспроизведения удалённого видео. |
| [muteRemoteAudio](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#muteRemoteAudio) | Отключение звука удалённого пользователя и остановка получения аудиоданных этого пользователя. Действует только для текущего пользователя; другие пользователи в комнате по-прежнему могут слышать голос пользователя с отключённым звуком. |
| [setRemoteAudioVolume](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#setRemoteAudioVolume) | Управление громкостью воспроизведения удалённого аудио. |
| [enableAudioVolumeEvaluation](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#enableAudioVolumeEvaluation) | Включение или отключение обратного вызова громкости. |
| [on](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#on) | Прослушивание [событий TRTC](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-EVENT.html) |
| [off](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#off) | Удаление прослушивателя события |
| [getVideoSnapshot](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#getVideoSnapshot) | Получение снимка видео |
| [getVideoTrack](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#getVideoTrack) | Получение видеодорожки |
| [getAudioTrack](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#getAudioTrack) | Получение аудиодорожки |
| [sendSEIMessage](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#sendSEIMessage) | Отправка сообщения SEI |
| [sendCustomMessage](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#sendCustomMessage) | Отправка пользовательского сообщения |
| [startPlugin](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#startPlugin) | Запуск плагина |
| [updatePlugin](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#updatePlugin) | Обновление плагина |
| [stopPlugin](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/TRTC.html#stopPlugin) | Остановка плагина |

> **Примечание.** Часто задаваемые вопросы см. в разделе [Web](https://www.tencentcloud.com/document/product/647/37340).

## Коды ошибок

SDK TRTC определяет 8 типов кодов ошибок. TRTC выдаёт ошибки в API-интерфейсах и событии [TRTC.EVENT.ERROR](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-EVENT.html#.ERROR), и вы можете получить объект [RtcError](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/RtcError.html) для обработки ошибки.

| Ключ | Код | Описание |
| --- | --- | --- |
| [INVALID_PARAMETER](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-ERROR_CODE.html#.INVALID_PARAMETER) | 5000 | Параметры, переданные при вызове интерфейса, не соответствуют требованиям API.  **Рекомендации по обработке:** проверьте, соответствуют ли переданные параметры спецификациям API, например правильны ли тип параметра. |
| [INVALID_OPERATION](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-ERROR_CODE.html#.INVALID_OPERATION) | 5100 | При вызове интерфейса не выполнены предварительные требования API.  **Рекомендации по обработке:** проверьте, соответствует ли логика вызова предварительным требованиям API в соответствии с документацией соответствующего API.  Например: переключение ролей перед успешным входом в комнату. Удалённый пользователь и воспроизводимый поток не существуют. |
| [ENV_NOT_SUPPORTED](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-ERROR_CODE.html#.ENV_NOT_SUPPORTED) | 5200 | Текущая среда не поддерживает эту функцию, что означает, что текущий браузер не поддерживает вызов соответствующего API.  **Рекомендации по обработке:** обычно TRTC.isSupported можно использовать для определения, какие возможности поддерживает текущий браузер. Если браузер не поддерживает эту функцию, необходимо направить пользователя на использование браузера, который поддерживает эту функцию. Справочное средство: [Определение возможностей](https://www.tencentcloud.com/document/product/647/59656) |
| [DEVICE_ERROR](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-ERROR_CODE.html#.DEVICE_ERROR) | 5300 | Ошибка при захвате устройств мультимедиа.  Следующие интерфейсы будут выдавать этот код ошибки при возникновении исключения: startLocalVideo, updateLocalVideo, startLocalAudio, updateLocalAudio, startScreenShare, updateScreenShare. **Рекомендации по обработке:** направьте пользователя на проверку наличия камеры и микрофона на устройстве, авторизации браузера в системе и авторизации страницы браузером. Рекомендуется добавить процесс обнаружения устройства перед входом в комнату, чтобы подтвердить наличие микрофона и камеры и возможность их нормального захвата перед переходом к следующей операции вызова. Обычно это исключение можно избежать после проверки устройства.  Справочное средство по реализации: [Определение возможностей](https://www.tencentcloud.com/document/product/647/59656). Если требуется различать более подробные категории исключений, можно обработать согласно [extraCode](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-ERROR_CODE.html#.DEVICE_ERROR) |
| [SERVER_ERROR](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-ERROR_CODE.html#.SERVER_ERROR) | 5400 | Получена ошибка сервера. Причины: истёкший userSig, задолженность по счёту Tencent Cloud, служба TRTC не включена и т. д.  **Рекомендации по обработке:** см. раздел [extraCode](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-ERROR_CODE.html#.SERVER_ERROR). |
| [OPERATION_FAILED](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-ERROR_CODE.html#.OPERATION_FAILED) | 5500 | Исключение, которое SDK не может устранить после нескольких повторных попыток при выполнении требований вызова API, обычно вызванное проблемами с браузером или сетью.  Следующие интерфейсы будут выдавать этот код ошибки при возникновении исключения: enterRoom, startLocalVideo, startLocalAudio, startScreenShare, startRemoteVideo, switchRole.  **Рекомендации по обработке:** проверьте соответствие доменного имени и порта, требуемых для взаимодействия, требованиям вашей сетевой среды, см. раздел [Обработка ограничений брандмауэра](https://www.tencentcloud.com/document/product/647/59667). Другие проблемы должны быть решены инженерами. [Отправить проблему на GitHub](https://github.com/LiteAVSDK/TRTC_Web/issues). |
| [OPERATION_ABORT](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-ERROR_CODE.html#.OPERATION_ABORT) | 5998 | Код ошибки, выдаваемый при отмене выполнения API.  Когда API вызывается или многократно вызывается без соответствия [жизненному циклу API](https://trtc.io/document/41664#33599d2d-ad9e-42e1-81af-907ab6acb5bb), API отменит выполнение, чтобы избежать бессмысленных операций.  Например: непрерывный вызов enterRoom, startLocalVideo и вызов exitRoom без входа в комнату.  Следующие интерфейсы будут выдавать этот код ошибки при возникновении исключения: enterRoom, startLocalVideo, startLocalAudio, startScreenShare, startRemoteVideo, switchRole.  **Рекомендации по обработке:** перехватите и определите этот код ошибки, затем избегите ненужных вызовов в логике бизнеса, или вы можете ничего не делать, поскольку SDK выполнил обработку без побочных эффектов, вам нужно только определить и игнорировать этот код ошибки при его перехвате. |
| [UNKNOWN_ERROR](https://web.sdk.qcloud.com/trtc/webrtc/v5/doc/en/module-ERROR_CODE.html#.OPERATION_ABORT) | 5999 | Неизвестная ошибка. Рекомендации по обработке: [отправить проблему на GitHub](https://github.com/LiteAVSDK/TRTC_Web). |

## Свяжитесь с нами

- [Отправить проблему на GitHub](https://github.com/LiteAVSDK/TRTC_Web).
- Свяжитесь с нами в [Telegram](https://t.me/+EPk6TMZEZMM5OGY1).


---
*Источник: [https://trtc.io/document/41664](https://trtc.io/document/41664)*

---
*Источник (EN): [client-apis.md](api-клиента.md)*

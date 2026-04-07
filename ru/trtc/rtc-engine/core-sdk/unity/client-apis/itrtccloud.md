# ITRTCCloud

Авторское право (c) 2021 Tencent. Все права защищены.

Модуль:   TRTCCloud @ TXLiteAVSDK

Функция: API основных возможностей TRTC

Версия: 12.6

**ITRTCCloud**

## ITRTCCloud

| FuncList | DESC |
| --- | --- |
| [getTRTCShareInstance](https://www.tencentcloud.com/document/product/647/72270#65f8f22625bce741ae1b4f38d62979f5) | Создать экземпляр TRTCCloud (режим singleton). |
| [destroyTRTCShareInstance](https://www.tencentcloud.com/document/product/647/72270#a077f03f488af3cc8fefc5978d7f4dd0) | Завершить экземпляр TRTCCloud (режим singleton). |
| [addCallback](https://www.tencentcloud.com/document/product/647/72270#e8ad8b727e6136af5ead580623dd58bf) | Добавить обратный вызов события TRTC. |
| [removeCallback](https://www.tencentcloud.com/document/product/647/72270#a3d2ae539728e319163b9a3364ea2d65) | Удалить обратный вызов события TRTC. |
| [enterRoom](https://www.tencentcloud.com/document/product/647/72270#159a2893d28f7e533ed7dd67e63a9a7b) | Войти в комнату. |
| [exitRoom](https://www.tencentcloud.com/document/product/647/72270#8e2de8da4b60ce0e19d385897ed77888) | Выйти из комнаты. |
| [switchRole](https://www.tencentcloud.com/document/product/647/72270#a2f85cd8f74124a8d0ec0c8b34d94b01) | Переключить роль. |
| [switchRoom](https://www.tencentcloud.com/document/product/647/72270#9f8d51bf4f02a354b060068482db62e8) | Переключить комнату. |
| [connectOtherRoom](https://www.tencentcloud.com/document/product/647/72270#f02d65d741e1ab3431427b94d472d6ac) | Запросить кроссрумовый вызов. |
| [disconnectOtherRoom](https://www.tencentcloud.com/document/product/647/72270#b061973682a21bfc056496655ba7e7e8) | Выход из кроссрумового вызова. |
| [setDefaultStreamRecvMode](https://www.tencentcloud.com/document/product/647/72270#f796890d9df3075ba7ce0cfa3b8a77a3) | Установить режим подписки (должен быть установлен до входа в комнату, чтобы вступить в силу). |
| [createSubCloud](https://www.tencentcloud.com/document/product/647/72270#2a6ba6f8c37d0a3453cef09671f8cee2) | Создать подэкземпляр комнаты (для параллельного прослушивания/просмотра нескольких комнат). |
| [destroySubCloud](https://www.tencentcloud.com/document/product/647/72270#5a2d2f205d2590e44e36ec532a3e9260) | Завершить подэкземпляр комнаты. |
| [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#1a29a736a9eba0c853f1962fb8d682a4) | Опубликовать поток. |
| [updatePublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#dad88b0322dc59b7e5dbf084b963782e) | Изменить параметры публикации. |
| [stopPublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#5d9c082fb84a8784246a729663df1ac4) | Остановить публикацию. |
| [startLocalPreview](https://www.tencentcloud.com/document/product/647/72270#38628a2c12121285b0ab3c24eba211dc) | Включить предпросмотр локальной камеры (мобильное). |
| [stopLocalPreview](https://www.tencentcloud.com/document/product/647/72270#e379630cda7e794574b00d549b64a815) | Остановить предпросмотр камеры. |
| [muteLocalVideo](https://www.tencentcloud.com/document/product/647/72270#b56b309b0223256eac598cb305d37270) | Приостановить/возобновить публикацию локального видеопотока. |
| [startRemoteView](https://www.tencentcloud.com/document/product/647/72270#1d041c439b9c088d4351eaf5aa832ca7) | Подписаться на видеопоток удаленного пользователя и привязать элемент управления отрисовкой видео. |
| [stopRemoteView](https://www.tencentcloud.com/document/product/647/72270#67277df08ab18e0c02a7d65f7b9a65c4) | Прекратить подписку на видеопоток удаленного пользователя и освободить элемент управления отрисовкой. |
| [stopAllRemoteView](https://www.tencentcloud.com/document/product/647/72270#5d9b1929a45db4a7a01d715628e3bbe0) | Прекратить подписку на видеопотоки всех удаленных пользователей и освободить все ресурсы отрисовки. |
| [muteRemoteVideoStream](https://www.tencentcloud.com/document/product/647/72270#e47216c48085fc929661d33cfece2181) | Приостановить/возобновить подписку на видеопоток удаленного пользователя. |
| [muteAllRemoteVideoStreams](https://www.tencentcloud.com/document/product/647/72270#d8b35494f4f1d45de0f70ca1f3cbdc15) | Приостановить/возобновить подписку на видеопотоки всех удаленных пользователей. |
| [setVideoEncoderParam](https://www.tencentcloud.com/document/product/647/72270#944184af05e4175e9458e5b0d563fb68) | Установить параметры кодирования видеокодера. |
| [setNetworkQosParam](https://www.tencentcloud.com/document/product/647/72270#a082314a7ac982791d01615b9bd4b9ff) | Установить параметры контроля качества сети. |
| [setLocalRenderParams](https://www.tencentcloud.com/document/product/647/72270#89eb94d30d078da58b4e29ab88d0b8a0) | Установить параметры отрисовки локального видеоизображения. |
| [setRemoteRenderParams](https://www.tencentcloud.com/document/product/647/72270#80129ddbe95cb5820c30be890d25f299) | Установить режим отрисовки удаленного видеоизображения. |
| [enableSmallVideoStream](https://www.tencentcloud.com/document/product/647/72270#0eaec8c2511ebc3aa5b402690bd6f007) | Включить режим двухканального кодирования с большим и малым изображениями. |
| [setRemoteVideoStreamType](https://www.tencentcloud.com/document/product/647/72270#e68258e11f2b24f72390c6e12a1356f8) | Переключить большое/малое изображение указанного удаленного пользователя. |
| [setGravitySensorAdaptiveMode](https://www.tencentcloud.com/document/product/647/72270#bbb20de90ec72745278e02ec92b2e7c6) | Установить режим адаптации гравитационного датчика (версия 11.7 и выше). |
| [startLocalAudio](https://www.tencentcloud.com/document/product/647/72270#126e2ce82ad449e5aafe277315896806) | Включить локальный захват и публикацию аудио. |
| [stopLocalAudio](https://www.tencentcloud.com/document/product/647/72270#8fafafeb80fe86f9fc0d893c9c35bd4e) | Остановить локальный захват и публикацию аудио. |
| [muteLocalAudio](https://www.tencentcloud.com/document/product/647/72270#00a0d2a0d3979a7edaf3b013f1bedc6a) | Приостановить/возобновить публикацию локального аудиопотока. |
| [muteRemoteAudio](https://www.tencentcloud.com/document/product/647/72270#b9f7792974d2df2e3922f2ed1e06ea39) | Приостановить/возобновить воспроизведение удаленного аудиопотока. |
| [muteAllRemoteAudio](https://www.tencentcloud.com/document/product/647/72270#c6a3fa5a81dd319bd3e3cdc06176e3d0) | Приостановить/возобновить воспроизведение аудиопотоков всех удаленных пользователей. |
| [setRemoteAudioVolume](https://www.tencentcloud.com/document/product/647/72270#a4705489d5d338ee436694837813976c) | Установить громкость воспроизведения аудио удаленного пользователя. |
| [setAudioCaptureVolume](https://www.tencentcloud.com/document/product/647/72270#8326d139f429c00b542151923d12d579) | Установить громкость захвата локального аудио. |
| [getAudioCaptureVolume](https://www.tencentcloud.com/document/product/647/72270#2d920084bbca50226a4e23db7178838c) | Получить громкость захвата локального аудио. |
| [setAudioPlayoutVolume](https://www.tencentcloud.com/document/product/647/72270#43a82fe566327b25f73fcf509ec3fbcc) | Установить громкость воспроизведения удаленного аудио. |
| [getAudioPlayoutVolume](https://www.tencentcloud.com/document/product/647/72270#3563829d921079d4da7207263302f8d4) | Получить громкость воспроизведения удаленного аудио. |
| [enableAudioVolumeEvaluation](https://www.tencentcloud.com/document/product/647/72270#e47cf2e48182962b7afde88a8f31fbbd) | Включить напоминание об уровне громкости. |
| [startLocalRecording](https://www.tencentcloud.com/document/product/647/72270#c0358d2dce89b4c19aa824350e2db40d) | Начать локальную запись мультимедиа. |
| [stopLocalRecording](https://www.tencentcloud.com/document/product/647/72270#a1236129ca8f62c01939c1882f184a88) | Остановить локальную запись мультимедиа. |
| [getDeviceManager](https://www.tencentcloud.com/document/product/647/72270#3237892a1dc5ad0a46fa7ab04f5e6712) | Получить класс управления устройствами (TXDeviceManager). |
| [setBeautyStyle](https://www.tencentcloud.com/document/product/647/72270#d78703f46f5b1a03720a3f23b9a6fc80) | Установить специальные эффекты, такие как фильтры красоты, осветления и розового цвета кожи. |
| [setWaterMark](https://www.tencentcloud.com/document/product/647/72270#9c85552e121871f7f2406189851aff0f) | Добавить водяной знак. |
| [getAudioEffectManager](https://www.tencentcloud.com/document/product/647/72270#dfd6d9d478ad8ca096bbe41997ab18c3) | Получить класс управления звуковыми эффектами (TXAudioEffectManager). |
| [startSystemAudioLoopback](https://www.tencentcloud.com/document/product/647/72270#9c7f414129474867563f4cb57398db05) | Включить захват системного аудио (iOS не поддерживается). |
| [stopSystemAudioLoopback](https://www.tencentcloud.com/document/product/647/72270#a542a2b1c0a06558e5ee453811395fca) | Остановить захват системного аудио (iOS не поддерживается). |
| [startScreenCapture](https://www.tencentcloud.com/document/product/647/72270#62ca4f19707f9c5046ee470b2034ec5d) | Начать общий доступ к экрану. |
| [stopScreenCapture](https://www.tencentcloud.com/document/product/647/72270#2a667ba75e08183bd5f764374a6de7ba) | Остановить общий доступ к экрану. |
| [pauseScreenCapture](https://www.tencentcloud.com/document/product/647/72270#d7f9ad7b108c98e919f5f1cca757e72d) | Приостановить общий доступ к экрану. |
| [resumeScreenCapture](https://www.tencentcloud.com/document/product/647/72270#1924263011bb92fba1642ad3e139629f) | Возобновить общий доступ к экрану. |
| [selectScreenCaptureTarget](https://www.tencentcloud.com/document/product/647/72270#ee8657c153c0c55123ca2524fc87b833) | Выбрать экран или окно для совместного доступа (только для настольных систем). |
| [setSubStreamEncoderParam](https://www.tencentcloud.com/document/product/647/72270#b809f30d749d36cfbd2d02d3975af747) | Установить параметры видеокодирования общего доступа к экрану (подпоток) (для настольных и мобильных систем). |
| [enableCustomVideoCapture](https://www.tencentcloud.com/document/product/647/72270#ab16ab952e0fab1102142bf0fd9dc13b) | Включить/отключить пользовательский режим захвата видео. |
| [sendCustomVideoData](https://www.tencentcloud.com/document/product/647/72270#8c8378c65a0b11187d6812523706a9f0) | Передать захватные видеокадры в SDK. |
| [enableCustomAudioCapture](https://www.tencentcloud.com/document/product/647/72270#f6957b147b00bf21188cefb40d9d12b0) | Включить пользовательский режим захвата аудио. |
| [sendCustomAudioData](https://www.tencentcloud.com/document/product/647/72270#346038d926da53656a6b0744a635a525) | Передать захватные аудиоданные в SDK. |
| [enableMixExternalAudioFrame](https://www.tencentcloud.com/document/product/647/72270#52ab34f49ed6033aa3856504c33c10ff) | Включить/отключить пользовательскую аудиодорожку. |
| [enableLocalVideoCustomProcess](https://www.tencentcloud.com/document/product/647/72270#ca8ffe633d84e1d03ac4513efd9730c9) | .1 Включить фильтры красоты третьих сторон в видео. |
| [setLocalVideoCustomProcessCallback](https://www.tencentcloud.com/document/product/647/72270#3ff1164f5fe9646f413a1f9ff5e8a83d) | .2 Установить обратный вызов видеоданных для фильтров красоты третьих сторон. |
| [setLocalVideoRenderCallback](https://www.tencentcloud.com/document/product/647/72270#90446bafe45e8f227390ec15613cbcf7) | Установить обратный вызов пользовательской отрисовки для локального видео. |
| [setRemoteVideoRenderCallback](https://www.tencentcloud.com/document/product/647/72270#1f8dfcdde1c0f2cd099fc0ac1464fb37) | Установить обратный вызов пользовательской отрисовки для удаленного видео. |
| [setAudioFrameCallback](https://www.tencentcloud.com/document/product/647/72270#f3d09f001ca9928b417b4d2a48ce692e) | Установить пользовательский обратный вызов аудиоданных. |
| [setCapturedAudioFrameCallbackFormat](https://www.tencentcloud.com/document/product/647/72270#fbe5029c6cbbd6c4354e4a66807ff9b7) | Установить формат обратного вызова аудиокадров, захватанных локальным микрофоном. |
| [setLocalProcessedAudioFrameCallbackFormat](https://www.tencentcloud.com/document/product/647/72270#06a441d79f72dc5269aa80e3fe766873) | Установить формат обратного вызова предварительно обработанных локальных аудиокадров. |
| [setMixedPlayAudioFrameCallbackFormat](https://www.tencentcloud.com/document/product/647/72270#59c33318c04f505402792cf49535085c) | Установить формат обратного вызова аудиокадров для воспроизведения системой. |
| [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/72270#20d4d41de96d8e2e6d2cf6499ea55171) | Использовать канал UDP для отправки пользовательского сообщения всем пользователям в комнате. |
| [sendSEIMsg](https://www.tencentcloud.com/document/product/647/72270#2d918c3d0ef54d41bd5f5adcb62f63d6) | Использовать канал SEI для отправки пользовательского сообщения всем пользователям в комнате. |
| [startSpeedTest](https://www.tencentcloud.com/document/product/647/72270#ecb445c9cc990d87be9fd5b11877af87) | Начать тест скорости сети (используется перед входом в комнату). |
| [stopSpeedTest](https://www.tencentcloud.com/document/product/647/72270#300e5f71dde3917dc5e057f9e1f6e014) | Остановить тест скорости сети. |
| [getScriptVersion](https://www.tencentcloud.com/document/product/647/72270#b71b2488d8664664486147fb47c570f4) | Получить информацию о версии скрипта SDK. |
| [getSDKVersion](https://www.tencentcloud.com/document/product/647/72270#f01e9209a78e98ddd4562d429e473256) | Получить информацию о версии SDK. |
| [setLogLevel](https://www.tencentcloud.com/document/product/647/72270#06eaac4ef81347a5804f5188214eb8e9) | Установить уровень вывода журнала. |
| [setConsoleEnabled](https://www.tencentcloud.com/document/product/647/72270#9d772868a17e895634e911b5c1d64b1f) | Включить/отключить вывод журнала на консоль. |
| [setLogCompressEnabled](https://www.tencentcloud.com/document/product/647/72270#a2b056173cd36a1e3ce30bcbde1ad3a1) | Включить/отключить сжатие локального журнала. |
| [setLogDirPath](https://www.tencentcloud.com/document/product/647/72270#171009adcb84ac7436010b7d84b95b6b) | Установить путь хранения локального журнала. |
| [setLogCallback](https://www.tencentcloud.com/document/product/647/72270#3581586698172fd227b6f6f1db929a7b) | Установить обратный вызов журнала. |
| [callExperimentalAPI](https://www.tencentcloud.com/document/product/647/72270#d39524378aab365ff67e393e3844230c) | Вызвать экспериментальные API. |

## getTRTCShareInstance

**getTRTCShareInstance**

#### Создать экземпляр TRTCCloud (режим singleton).

> **Примечание**1. Если вы используете ` delete ITRTCCloud* `, произойдет ошибка компиляции. Пожалуйста, используйте [destroyTRTCShareInstance](https://www.tencentcloud.com/document/product/647/72270#a077f03f488af3cc8fefc5978d7f4dd0) для освобождения указателя объекта.

## destroyTRTCShareInstance

**destroyTRTCShareInstance**

#### Завершить экземпляр TRTCCloud (режим singleton).

## addCallback

**addCallback**

| void addCallback | ([ITRTCCloudCallback](https://www.tencentcloud.com/document/product/647/72271#338fdd109b5c9711d47c618b7d14b431) callback) |
| --- | --- |

#### Добавить обратный вызов события TRTC.

Вы можете использовать [ITRTCCloudCallback](https://www.tencentcloud.com/document/product/647/72271#338fdd109b5c9711d47c618b7d14b431) для получения различных уведомлений о событиях от SDK, таких как коды ошибок, коды предупреждений и параметры статуса аудио/видео.

## removeCallback

**removeCallback**

| void removeCallback | ([ITRTCCloudCallback](https://www.tencentcloud.com/document/product/647/72271#338fdd109b5c9711d47c618b7d14b431) callback) |
| --- | --- |

#### Удалить обратный вызов события TRTC.

## enterRoom

**enterRoom**

| void enterRoom | (ref [TRTCParams](https://www.tencentcloud.com/document/product/647/72275#a1de1e93c6cfc6be81dd4152b9e4c190) param |
| --- | --- |
|  | [TRTCAppScene](https://www.tencentcloud.com/document/product/647/72275#50498dba914e98bc767b83dc0c72a0a1) scene) |

#### Войти в комнату.

Все пользователи TRTC должны войти в комнату перед тем, как они смогут "публиковать" или "подписываться на" аудио/видеопотоки. "Публикация" означает отправку собственных потоков в облако, а "подписка" означает получение потоков других пользователей в комнате из облака.

При вызове этого API необходимо указать сценарий приложения ([TRTCAppScene](https://www.tencentcloud.com/document/product/647/72275#50498dba914e98bc767b83dc0c72a0a1)), чтобы получить лучший опыт передачи аудио/видео. Мы предоставляем четыре следующих сценария на ваш выбор:

- [TRTCAppSceneVideoCall](https://www.tencentcloud.com/document/product/647/72275#50498dba914e98bc767b83dc0c72a0a1):

Сценарий видеовызова. Случаи использования: [видеовызов один-на-один], [видеоконференция с участием до 300 пользователей], [онлайн-консультация врача], [небольшой класс], [видеоинтервью] и т.д.

В этом сценарии каждая комната поддерживает до 300 одновременно онлайн пользователей, и до 50 из них могут говорить одновременно.

- [TRTCAppSceneAudioCall](https://www.tencentcloud.com/document/product/647/72275#50498dba914e98bc767b83dc0c72a0a1):

Сценарий аудиовызова. Случаи использования: [аудиовызов один-на-один], [аудиоконференция с участием до 300 пользователей], [аудиочат], [онлайн "Мафия"] и т.д.

В этом сценарии каждая комната поддерживает до 300 одновременно онлайн пользователей, и до 50 из них могут говорить одновременно.

- [TRTCAppSceneLIVE](https://www.tencentcloud.com/document/product/647/72275#50498dba914e98bc767b83dc0c72a0a1):

Сценарий прямой трансляции. Случаи использования: [потоковое видео с низкой задержкой], [интерактивный класс для участия до 100 000 пользователей], [конкурс видеотрансляции], [видео-знакомства], [удаленное обучение], [крупномасштабная конференция] и т.д.

В этом сценарии каждая комната поддерживает до 100 000 одновременно онлайн пользователей, но вы должны указать роли пользователей: якорь ([TRTCRoleAnchor](https://www.tencentcloud.com/document/product/647/72275#874dbd6062bbf1384648ca9f9054aa5b)) или аудитория ([TRTCRoleAudience](https://www.tencentcloud.com/document/product/647/72275#874dbd6062bbf1384648ca9f9054aa5b)).

- [TRTCAppSceneVoiceChatRoom](https://www.tencentcloud.com/document/product/647/72275#50498dba914e98bc767b83dc0c72a0a1):

Сценарий комнаты аудиочата. Случаи использования: [Clubhouse], [онлайн-караоке], [музыкальная комната прямой трансляции], [FM-радио] и т.д.

В этом сценарии каждая комната поддерживает до 100 000 одновременно онлайн пользователей, но вы должны указать роли пользователей: якорь ([TRTCRoleAnchor](https://www.tencentcloud.com/document/product/647/72275#874dbd6062bbf1384648ca9f9054aa5b)) или аудитория ([TRTCRoleAudience](https://www.tencentcloud.com/document/product/647/72275#874dbd6062bbf1384648ca9f9054aa5b)).

После вызова этого API вы получите обратный вызов ` onEnterRoom(result) ` от [ITRTCCloudCallback](https://www.tencentcloud.com/document/product/647/72271#338fdd109b5c9711d47c618b7d14b431):

- Если вход в комнату был успешным, параметр ` result ` будет положительным числом (` result ` > 0), указывающим время в миллисекундах (мс) между вызовом функции и входом в комнату.
- Если вход в комнату не удался, параметр ` result ` будет отрицательным числом (` result ` < 0), указывающим TXLiteAVError для ошибки входа в комнату.

| Param | DESC |
| --- | --- |
| param | Параметр входа в комнату, используется для указания удостоверения пользователя, роли, учетных данных аутентификации и другой информации. Для получения дополнительной информации см. [TRTCParams](https://www.tencentcloud.com/document/product/647/72275#a1de1e93c6cfc6be81dd4152b9e4c190). |
| scene | Сценарий приложения, используется для указания случая использования. Один и тот же [TRTCAppScene](https://www.tencentcloud.com/document/product/647/72275#50498dba914e98bc767b83dc0c72a0a1) должен быть настроен для всех пользователей в одной комнате. |

> **Примечание**Если ` scene ` установлен как [TRTCAppSceneLIVE](https://www.tencentcloud.com/document/product/647/72275#50498dba914e98bc767b83dc0c72a0a1) или [TRTCAppSceneVoiceChatRoom](https://www.tencentcloud.com/document/product/647/72275#50498dba914e98bc767b83dc0c72a0a1

## destroySubCloud

**destroySubCloud**

| void destroySubCloud | ([ITRTCCloud](https://www.tencentcloud.com/document/product/647/72270#c147edc3349cedea03776fa64458db5c) subCloud) |
| --- | --- |

#### Завершить подэкземпляр комнаты.

| Параметр | Описание |
| --- | --- |
| subCloud | Подэкземпляр комнаты |

## startPublishMediaStream

**startPublishMediaStream**

| void startPublishMediaStream | (ref [TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/72275#e106259cbc7f1cff297f52931b7e7c49) target |
| --- | --- |
|  | ref [TRTCStreamEncoderParam](https://www.tencentcloud.com/document/product/647/72275#22718fe81d94d21ec895cbc11820c726) param |
|  | ref [TRTCStreamMixingConfig](https://www.tencentcloud.com/document/product/647/72275#7ddba434412d83f9aa8f34b1bb36b166) config) |

#### Опубликовать поток.

После вызова этого API сервер TRTC будет передавать поток локального пользователя на CDN (с перекодированием или без), либо перекодировать и опубликовать поток в комнату TRTC.

Вы можете использовать параметр [TRTCPublishMode](https://www.tencentcloud.com/document/product/647/72275#064db271e894d12e1e3ad63bbb1677fb) в [TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/72275#e106259cbc7f1cff297f52931b7e7c49) для указания режима публикации.

| Параметр | Описание |
| --- | --- |
| config | Настройки транскодирования на облаке. Этот параметр не используется в режиме передачи на CDN. Требуется, если вы перекодируете и публикуете поток на CDN или в комнату TRTC. Подробнее см. [TRTCStreamMixingConfig](https://www.tencentcloud.com/document/product/647/72275#7ddba434412d83f9aa8f34b1bb36b166). |
| params | Параметры кодирования. Этот параметр требуется, если вы перекодируете и публикуете поток на CDN или в комнату TRTC. Если вы передаёте на CDN без перекодирования, для повышения стабильности передачи и совместимости воспроизведения рекомендуется также установить этот параметр. Подробнее см. [TRTCStreamEncoderParam](https://www.tencentcloud.com/document/product/647/72275#22718fe81d94d21ec895cbc11820c726). |
| target | Назначение публикации. Вы можете передавать поток на CDN (с перекодированием или без) или перекодировать и публикуете поток в комнату TRTC. Подробнее см. [TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/72275#e106259cbc7f1cff297f52931b7e7c49). |

> **Примечание** 1. SDK отправит вам идентификатор задачи через обратный вызов [onStartPublishMediaStream](https://www.tencentcloud.com/document/product/647/72271#8c314542e34620ecf64a2310577b34ba). 2. Вы можете запустить задачу публикации только один раз и не можете инициировать две задачи, которые используют одинаковый режим публикации и URL-адрес публикации CDN. Сохраните возвращённый идентификатор задачи, который вам нужно передать в [updatePublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#dad88b0322dc59b7e5dbf084b963782e) для изменения параметров публикации или в [stopPublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#5d9c082fb84a8784246a729663df1ac4) для остановки задачи. 3. Вы можете указать до 10 URL-адресов CDN в ` target `. Взимание платы за транскодирование будет произведено только один раз, даже если вы передаёте на несколько CDN. 4. Чтобы избежать ошибок, не указывайте одинаковые URL-адреса для различных задач публикации, выполняемых одновременно. Рекомендуется добавлять "sdkappid_roomid_userid_main" к URL-адресам для их различения и избежания конфликтов приложений.

## updatePublishMediaStream

**updatePublishMediaStream**

| void updatePublishMediaStream | (string taskId |
| --- | --- |
|  | ref [TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/72275#e106259cbc7f1cff297f52931b7e7c49) target |
|  | ref [TRTCStreamEncoderParam](https://www.tencentcloud.com/document/product/647/72275#22718fe81d94d21ec895cbc11820c726) param |
|  | ref [TRTCStreamMixingConfig](https://www.tencentcloud.com/document/product/647/72275#7ddba434412d83f9aa8f34b1bb36b166) config) |

#### Изменить параметры публикации.

Вы можете использовать этот API для изменения параметров задачи публикации, инициированной методом [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#1a29a736a9eba0c853f1962fb8d682a4).

| Параметр | Описание |
| --- | --- |
| config | Настройки транскодирования на облаке. Этот параметр не используется в режиме передачи на CDN. Требуется, если вы перекодируете и публикуете поток на CDN или в комнату TRTC. Подробнее см. [TRTCStreamMixingConfig](https://www.tencentcloud.com/document/product/647/72275#7ddba434412d83f9aa8f34b1bb36b166). |
| params | Параметры кодирования. Этот параметр требуется, если вы перекодируете и публикуете поток на CDN или в комнату TRTC. Если вы передаёте на CDN без перекодирования, для повышения стабильности передачи и совместимости воспроизведения рекомендуется установить этот параметр. Подробнее см. [TRTCStreamEncoderParam](https://www.tencentcloud.com/document/product/647/72275#22718fe81d94d21ec895cbc11820c726). |
| target | Назначение публикации. Вы можете передавать поток на CDN (с перекодированием или без) или перекодировать и публикуете поток в комнату TRTC. Подробнее см. [TRTCPublishTarget](https://www.tencentcloud.com/document/product/647/72275#e106259cbc7f1cff297f52931b7e7c49). |
| taskId | Идентификатор задачи, возвращённый вам через обратный вызов [onStartPublishMediaStream](https://www.tencentcloud.com/document/product/647/72271#8c314542e34620ecf64a2310577b34ba). |

> **Примечание** 1. Вы можете использовать этот API для добавления или удаления URL-адресов CDN для публикации (вы можете одновременно публиковать на до 10 CDN). Чтобы избежать ошибок, не указывайте одинаковые URL-адреса для различных задач, выполняемых одновременно. 2. Вы можете использовать этот API для переключения задачи передачи на транскодирование или наоборот. Например, при кросс-комнатной коммуникации вы можете сначала вызвать [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#1a29a736a9eba0c853f1962fb8d682a4) для передачи на CDN. Когда ведущий запрашивает кросс-комнатную коммуникацию, вызовите этот API, передав идентификатор задачи для переключения задачи передачи на задачу транскодирования. Это может обеспечить непрерывность прямой трансляции и воспроизведения на CDN (вам нужно сохранять согласованность параметров кодирования). 3. Вы не можете переключать вывод между "только аудио", "только видео" и "аудио и видео" для одной задачи.

## stopPublishMediaStream

**stopPublishMediaStream**

| void stopPublishMediaStream | (string taskId) |
| --- | --- |

#### Остановить публикацию.

Вы можете использовать этот API для остановки задачи, инициированной методом [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#1a29a736a9eba0c853f1962fb8d682a4).

| Параметр | Описание |
| --- | --- |
| taskId | Идентификатор задачи, возвращённый вам через обратный вызов [onStartPublishMediaStream](https://www.tencentcloud.com/document/product/647/72271#8c314542e34620ecf64a2310577b34ba). |

> **Примечание** 1. Если идентификатор задачи не сохранён на вашем сервере, вы можете вызвать [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#1a29a736a9eba0c853f1962fb8d682a4) снова, когда ведущий повторно входит в комнату после аномального выхода. Публикация будет неудачной, но бэкенд TRTC вернёт вам идентификатор задачи. 2. Если ` taskId ` остаётся пустым, бэкенд TRTC завершит все задачи, которые вы запустили через [startPublishMediaStream](https://www.tencentcloud.com/document/product/647/72270#1a29a736a9eba0c853f1962fb8d682a4). Вы можете оставить его пустым, если вы запустили только одну задачу или хотите остановить все задачи публикации, запущенные вами.

## startLocalPreview

**startLocalPreview**

| void startLocalPreview | (bool frontCamera |
| --- | --- |
|  | GameObject view) |

#### Включить предпросмотр изображения локальной камеры (мобильная версия).

Если этот API вызывается перед [enterRoom](https://www.tencentcloud.com/document/product/647/72270#159a2893d28f7e533ed7dd67e63a9a7b), SDK только включит камеру и будет ждать, пока будет вызван [enterRoom](https://www.tencentcloud.com/document/product/647/72270#159a2893d28f7e533ed7dd67e63a9a7b), прежде чем начать передачу.

Если он вызывается после [enterRoom](https://www.tencentcloud.com/document/product/647/72270#159a2893d28f7e533ed7dd67e63a9a7b), SDK включит камеру и автоматически начнёт передачу видеопотока.

Когда начнёт отрисовываться первый видеокадр камеры, вы получите обратный вызов ` onCameraDidReady ` в [ITRTCCloudCallback](https://www.tencentcloud.com/document/product/647/72271#338fdd109b5c9711d47c618b7d14b431).

| Параметр | Описание |
| --- | --- |
| frontCamera | true: передняя камера; false: задняя камера |
| view | Элемент управления, который несёт видеоизображение |

> **Примечание** Если вы хотите предпросмотреть изображение камеры и настроить параметры фильтра красоты через ` BeautyManager ` перед прямой трансляцией, вы можете: Способ 1. Вызовите ` startLocalPreview ` перед вызовом [enterRoom](https://www.tencentcloud.com/document/product/647/72270#159a2893d28f7e533ed7dd67e63a9a7b). Способ 2. Вызовите ` startLocalPreview ` и ` muteLocalVideo(true) ` после вызова [enterRoom](https://www.tencentcloud.com/document/product/647/72270#159a2893d28f7e533ed7dd67e63a9a7b).

## stopLocalPreview

**stopLocalPreview**

#### Остановить предпросмотр камеры.

## muteLocalVideo

**muteLocalVideo**

| void muteLocalVideo | ([TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868) streamType |
| --- | --- |
|  | bool mute) |

#### Приостановить/Возобновить публикацию локального видеопотока.

Этот API может приостановить (или возобновить) публикацию локального видеоизображения. После паузы другие пользователи в той же комнате не смогут видеть локальное изображение.

Этот API эквивалентен двум API ` startLocalPreview/stopLocalPreview ` при указании TRTCVideoStreamTypeBig, но имеет более высокую производительность и скорость отклика.

API ` startLocalPreview/stopLocalPreview ` требуют включения/отключения камеры, которые являются операциями, связанными с аппаратными устройствами, поэтому они очень затратны по времени.

В отличие от этого, ` muteLocalVideo ` требуется только приостановить или разрешить поток данных на уровне программного обеспечения, поэтому это более эффективно и больше подходит для сценариев, которые требуют частого включения/отключения.

После приостановки публикации локального видео другие члены в той же комнате получат уведомление обратного вызова ` onUserVideoAvailable(userId, false) `.

После возобновления публикации локального видео другие члены в той же комнате получат уведомление обратного вызова ` onUserVideoAvailable(userId, true) `.

| Параметр | Описание |
| --- | --- |
| mute | true: приостановить; false: возобновить |
| streamType | Укажите, для какого видеопотока нужно приостановить (или возобновить). Поддерживаются только [TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868) и [TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868) |

## startRemoteView

**startRemoteView**

| void startRemoteView | (string userId |
| --- | --- |
|  | [TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868) streamType |
|  | GameObject view) |

#### Подписаться на видеопоток удалённого пользователя и привязать элемент управления отрисовкой видео.

Вызов этого API позволяет SDK извлечь видеопоток указанного ` userId ` и отрисовать его в элемент управления отрисовкой, указанный параметром ` view `. Вы можете установить режим отображения видеоизображения через [setRemoteRenderParams](https://www.tencentcloud.com/document/product/647/72270#80129ddbe95cb5820c30be890d25f299).

- Если вы уже знаете ` userId ` пользователя, который имеет видеопоток в комнате, вы можете напрямую вызвать ` startRemoteView ` для подписки на видеоизображение пользователя.
- Если вы не знаете, какие пользователи в комнате публикуют видеопотоки, вы можете ждать уведомления от [onUserVideoAvailable](https://www.tencentcloud.com/document/product/647/72271#59380ac1827201d40a1795e59f2f894a) после [enterRoom](https://www.tencentcloud.com/document/product/647/72270#159a2893d28f7e533ed7dd67e63a9a7b).

Вызов этого API только начинает извлечение видеопотока, и изображение необходимо загрузить и буферизировать в это время. После завершения буферизации вы получите уведомление от [onFirstVideoFrame](https://www.tencentcloud.com/document/product/647/72271#7506c0166d59556803da3620d8bed4fb).

| Параметр | Описание |
| --- | --- |
| streamType | Тип видеопотока указанного ` userId ` для просмотра: HD большое изображение: [TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868) Плавное маленькое изображение: [TRTCVideoStreamTypeSmall](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868) (удалённый пользователь должен включить двухканальное кодирование через [enableSmallVideoStream](https://www.tencentcloud.com/document/product/647/72270#0eaec8c2511ebc3aa5b402690bd6f007) для вступления этого параметра в силу) Изображение подпотока (обычно используется для совместного использования экрана): [TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868) |
| userId | ID указанного удалённого пользователя |
| view | Элемент управления отрисовкой, который несёт видеоизображение |

> **Примечание** Требуется обратить внимание на следующее: 1. SDK поддерживает просмотр большого изображения и изображения подпотока или маленького и изображения подпотока одного ` userId ` одновременно, но не поддерживает просмотр большого и маленького изображения одновременно. 2. Только когда указанный ` userId ` включит двухканальное кодирование через [enableSmallVideoStream](https://www.tencentcloud.com/document/product/647/72270#0eaec8c2511ebc3aa5b402690bd6f007), можно просмотреть маленькое изображение пользователя. 3. Если маленькое изображение указанного ` userId ` не существует, SDK по умолчанию переключится на большое изображение пользователя.

## stopRemoteView

**stopRemoteView**

| void stopRemoteView | (string userId |
| --- | --- |
|  | [TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868) streamType) |

#### Отписаться от видеопотока удалённого пользователя и освободить элемент управления отрисовкой.

Вызов этого API приведёт к тому, что SDK перестанет получать видеопоток пользователя и освободит ресурсы декодирования и отрисовки для потока.

| Параметр | Описание |
| --- | --- |
| streamType | Тип видеопотока указанного ` userId ` для просмотра: HD большое изображение: [TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868) Плавное маленькое изображение: [TRTCVideoStreamTypeSmall](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868) Изображение подпотока (обычно используется для совместного использования экрана): [TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868) |
| userId | ID указанного удалённого пользователя |

## stopAllRemoteView

**stopAllRemoteView**

#### Отписаться от видеопотоков всех удалённых пользователей и освободить все ресурсы отрисовки.

Вызов этого API приведёт к тому, что SDK перестанет получать все удалённые видеопотоки и освободит все ресурсы декодирования и отрисовки.

> **Примечание** Если отображается изображение подпотока (совместное использование экрана), оно также будет остановлено.

## muteRemoteVideoStream

**muteRemoteVideoStream**

| void muteRemoteVideoStream | (string userId |
| --- | --- |
|  | [TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868) streamType |
|  | bool mute) |

#### Приостановить/Возобновить подписку на видеопоток удалённого пользователя.

Этот API только приостанавливает/возобновляет получение видеопотока указанного пользователя, но не освобождает ресурсы отображения; поэтому видеоизображение будет заморожено на последнем кадре перед вызовом.

| Параметр | Описание |
| --- | --- |
| mute | Приостановить ли получение |
| streamType | Укажите, для какого видеопотока нужно приостановить (или возобновить): HD большое изображение: [TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868) Плавное маленькое изображение: [TRTCVideoStreamTypeSmall](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868) Изображение подпотока (обычно используется для совместного использования экрана): [TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868) |
| userId | ID указанного удалённого пользователя |

> **Примечание** Этот API можно вызывать перед входом в комнату ([enterRoom](https://www.tencentcloud.com/document/product/647/72270#159a2893d28f7e533ed7dd67e63a9a7b)), и состояние паузы будет сброшено после выхода из комнаты ([exitRoom](https://www.tencentcloud.com/document/product/647/72270#8e2de8da4b60ce0e19d385897ed77888)). После вызова этого API для приостановки получения видеопотока от конкретного пользователя просто вызов API [startRemoteView](https://www.tencentcloud.com/document/product/647/72270#1d041c439b9c088d4351eaf5aa832ca7) не сможет воспроизвести видео этого пользователя. Вам нужно вызвать [muteRemoteVideoStream](https://www.tencentcloud.com/document/product/647/72270#e47216c48085fc929661d33cfece2181)(false) или [muteAllRemoteVideoStreams](https://www.tencentcloud.com/document/product/647/72270#d8b35494f4f1d45de0f70ca1f3cbdc15)(false) для возобновления.

## muteAllRemoteVideoStreams

**muteAllRemoteVideoStreams**

| void muteAllRemoteVideoStreams | (bool mute) |
| --- | --- |

#### Приостановить/Возобновить подписку на видеопотоки всех удалённых пользователей.

Этот API только приостанавливает/возобновляет получение видеопотоков всех пользователей, но не освобождает ресурсы отображения; поэтому видеоизображение будет заморожено на последнем кадре перед вызовом.

| Параметр | Описание |
| --- | --- |
| mute | Приостановить ли получение |

> **Примечание** Этот API можно вызывать перед входом в комнату ([enterRoom](https://www.tencentcloud.com/document/product/647/72270#159a2893d28f7e533ed7dd67e63a9a7b)), и состояние паузы будет сброшено после выхода из комнаты ([exitRoom](https://www.tencentcloud.com/document/product/647/72270#8e2de8da4b60ce0e19d385897ed77888)). После вызова этого интерфейса для приостановки получения видеопотоков от всех пользователей просто вызов интерфейса [startRemoteView](https://www.tencentcloud.com/document/product/647/72270#1d041c439b9c088d4351eaf5aa832ca7) не сможет воспроизвести видео конкретного пользователя. Вам нужно вызвать [muteRemoteVideoStream](https://www.tencentcloud.com/document/product/647/72270#e47216c48085fc929661d33cfece2181)(false) или [muteAllRemoteVideoStreams](https://www.tencentcloud.com/document/product/647/72270#d8b35494f4f1d45de0f70ca1f3cbdc15)(false) для возобновления.

## setVideoEncoderParam

**setVideoEncoderParam**

| void setVideoEncoderParam | (ref [TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/72275#b5beabfeefb812ccf1060aea67185c4e) param) |
| --- | --- |

#### Установить параметры кодирования видеокодека.

Эта настройка может определить качество изображения, просматриваемого удалённых пользователем, что также является качеством изображения файлов облачной записи.

| Параметр | Описание |
| --- | --- |
| param | Используется для установки соответствующих параметров видеокодека. Для получения дополнительной информации см. [TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/72275#b5beabfeefb812ccf1060aea67185c4e). |

> **Примечание** Начиная с версии v11.5, разрешение выходного кодирования будет выровнено в соответствии с шириной 8 и высотой 2 байта и будет скорректировано в сторону уменьшения, например: входное разрешение 540x960, фактическое выходное разрешение кодирования 536x960.

## setNetworkQosParam

**setNetworkQosParam**

| void setNetworkQosParam | (ref [TRTCNetworkQosParam](https://www.tencentcloud.com/document/product/647/72275#15fa30eb2d0220259cea127fdb0f886f) param) |
| --- | --- |

#### Установить параметры контроля качества сети.

Эта настройка определяет политику контроля качества в условиях плохой сети, например "предпочтение качества изображения" или "предпочтение плавности".

| Параметр | Описание |
| --- | --- |
| param | Используется для установки соответствующих параметров контроля качества сети. Подробнее см. [TRTCNetworkQosParam](https://www.tencentcloud.com/document/product/647/72275#15fa30eb2d0220259cea127fdb0f886f). |

## setLocalRenderParams

**setLocalRenderParams**

| void setLocalRenderParams | ([TRTCRenderParams](https://www.tencentcloud.com/document/product/647/72275#660db44737d95899da095d02d163

## setRemoteAudioVolume

**setRemoteAudioVolume**

| void setRemoteAudioVolume | (string userId |
| --- | --- |
|  | int volume) |

#### Установить громкость воспроизведения звука удалённого пользователя.

Вы можете отключить звук удалённого пользователя через ` setRemoteAudioVolume(userId, 0) `.

| Param | DESC |
| --- | --- |
| userId | ID указанного удалённого пользователя |
| volume | Громкость. 100 — исходная громкость. Диапазон значений: [0,150]. Значение по умолчанию: 100 |

> **Примечание** Если громкость 100 недостаточна, вы можете установить громкость до 150, но это может вызвать побочные эффекты.

## setAudioCaptureVolume

**setAudioCaptureVolume**

| void setAudioCaptureVolume | (int volume) |
| --- | --- |

#### Установить громкость захвата локального звука.

| Param | DESC |
| --- | --- |
| volume | Громкость. 100 — исходная громкость. Диапазон значений: [0,150]. Значение по умолчанию: 100 |

> **Примечание** Если громкость 100 недостаточна, вы можете установить громкость до 150, но это может вызвать побочные эффекты.

## getAudioCaptureVolume

**getAudioCaptureVolume**

#### Получить громкость захвата локального звука.

#### Return Desc:

громкость захвата

## setAudioPlayoutVolume

**setAudioPlayoutVolume**

| void setAudioPlayoutVolume | (int volume) |
| --- | --- |

#### Установить громкость воспроизведения удалённого звука.

Этот API управляет громкостью звука, который в конечном итоге передаётся SDK системе для воспроизведения. Он влияет на громкость записанного локального звука, но не влияет на громкость мониторинга в наушниках.

| Param | DESC |
| --- | --- |
| volume | Громкость. 100 — исходная громкость. Диапазон значений: [0,150]. Значение по умолчанию: 100 |

> **Примечание** Если громкость 100 недостаточна, вы можете установить громкость до 150, но это может вызвать побочные эффекты.

## getAudioPlayoutVolume

**getAudioPlayoutVolume**

#### Получить громкость воспроизведения удалённого звука.

## enableAudioVolumeEvaluation

**enableAudioVolumeEvaluation**

| void enableAudioVolumeEvaluation | (bool enable |
| --- | --- |
|  | [TRTCAudioVolumeEvaluateParams](https://www.tencentcloud.com/document/product/647/72275#a009476d3d69bd49ff693344302409bf) evaluateParams) |

#### Включить напоминание о громкости.

После включения этой функции SDK будет возвращать информацию об оценке громкости звука локального пользователя, который отправляет поток, и удалённых пользователей в обратном вызове [onUserVoiceVolume](https://www.tencentcloud.com/document/product/647/72271#12c009f500ddcfac4dc9bbf142bf68cb) интерфейса [ITRTCCloudCallback](https://www.tencentcloud.com/document/product/647/72271#338fdd109b5c9711d47c618b7d14b431).

| Param | DESC |
| --- | --- |
| enable | Включить ли напоминание о громкости. По умолчанию отключено. |
| params | Параметры оценки громкости и другие связанные параметры, см. [TRTCAudioVolumeEvaluateParams](https://www.tencentcloud.com/document/product/647/72275#a009476d3d69bd49ff693344302409bf) |

> **Примечание** Для включения этой функции вызовите этот API перед вызовом [startLocalAudio](https://www.tencentcloud.com/document/product/647/72270#126e2ce82ad449e5aafe277315896806).

## startLocalRecording

**startLocalRecording**

| void startLocalRecording | (ref [TRTCLocalRecordingParams](https://www.tencentcloud.com/document/product/647/72275#4d8f80d5bf4ece224c7125eec1490b3d) localRecordingParams) |
| --- | --- |

#### Начать локальную запись медиа.

Этот API записывает аудио/видео содержимое во время прямой трансляции в локальный файл, и комиссия за локальную запись не взимается.

| Param | DESC |
| --- | --- |
| params | Параметр записи. Для получения дополнительной информации см. [TRTCLocalRecordingParams](https://www.tencentcloud.com/document/product/647/72275#4d8f80d5bf4ece224c7125eec1490b3d) |

## stopLocalRecording

**stopLocalRecording**

#### Остановить локальную запись медиа.

Если задача записи не была остановлена с помощью этого API перед выходом из комнаты, она будет автоматически остановлена после выхода из комнаты.

## getDeviceManager

**getDeviceManager**

#### Получить класс управления устройствами (TXDeviceManager).

Благодаря управлению устройствами вы можете установить функции аппаратных устройств, связанных с звуком и видео, таких как камеры, микрофоны и динамики.

#### Return Desc:

класс управления устройствами TXDeviceManager.

## setBeautyStyle

**setBeautyStyle**

| void setBeautyStyle | ([TRTCBeautyStyle](https://www.tencentcloud.com/document/product/647/72275#6b80cffd21c1ebc2f793a0dcc11abda6) style |
| --- | --- |
|  | uint beauty |
|  | uint white |
|  | uint ruddiness) |

#### Установить специальные эффекты, такие как улучшение красоты, осветление и фильтры здорового цвета кожи.

SDK интегрирует два алгоритма сглаживания кожи разных стилей:

- стиль "Smooth" (Гладкий), который использует более радикальный алгоритм для более очевидного эффекта и подходит для прямых трансляций.
- стиль "Natural" (Натуральный), который сохраняет больше деталей лица для более натурального эффекта и подходит для большинства случаев прямых трансляций.

| Param | DESC |
| --- | --- |
| beautyLevel | Интенсивность фильтра красоты. Диапазон значений: 0–9; 0 означает, что фильтр отключен, чем больше значение, тем более очевидный эффект. |
| ruddinessLevel | Интенсивность фильтра здорового цвета кожи. Диапазон значений: 0–9; 0 означает, что фильтр отключен, чем больше значение, тем более очевидный эффект. |
| style | Алгоритм сглаживания кожи ("smooth" или "natural") |
| whitenessLevel | Интенсивность фильтра осветления. Диапазон значений: 0–9; 0 означает, что фильтр отключен, чем больше значение, тем более очевидный эффект. |

## setWaterMark

**setWaterMark**

| void setWaterMark | ([TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868) streamType |
| --- | --- |
|  | string srcData |
|  | [TRTCWaterMarkSrcType](https://www.tencentcloud.com/document/product/647/72275#49ce20e9ead413a1fe53e7a7854a9ef9) srcType |
|  | uint nWidth |
|  | uint nHeight |
|  | float xOffset |
|  | float yOffset |
|  | float fWidthRatio |
|  | bool isVisibleOnLocalPreview = false) |

#### Добавить водяной знак.

Положение водяного знака определяется параметрами ` xOffset `, ` yOffset ` и ` fWidthRatio `.

- ` xOffset `: координата X водяного знака, которая представляет собой число с плавающей запятой от 0 до 1.
- ` yOffset `: координата Y водяного знака, которая представляет собой число с плавающей запятой от 0 до 1.
- ` fWidthRatio `: соотношение размеров водяного знака, которое представляет собой число с плавающей запятой от 0 до 1.

| Param | DESC |
| --- | --- |
| fWidthRatio | Соотношение ширины водяного знака к ширине изображения (водяной знак будет масштабирован в соответствии с этим параметром) |
| isVisibleOnLocalPreview | true: локальный предпросмотр показывает водяной знак; false: локальный предпросмотр скрывает водяной знак. Работает только на win/mac. |
| nHeight | Высота водяного знака в пикселях (этот параметр будет проигнорирован, если исходные данные — это путь к файлу) |
| nWidth | Ширина водяного знака в пикселях (этот параметр будет проигнорирован, если исходные данные — это путь к файлу) |
| srcData | Исходные данные изображения водяного знака (если передано ` nullptr `, водяной знак будет удален) |
| srcType | Тип исходных данных изображения водяного знака. Для получения дополнительной информации см. [TRTCWaterMarkSrcType](https://www.tencentcloud.com/document/product/647/72275#49ce20e9ead413a1fe53e7a7854a9ef9) |
| streamType | Тип потока, к которому применяется водяной знак ([TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868) или @@link TRTCVideoStreamTypeSub}) |
| xOffset | Смещение в верхнем левом углу по оси X водяного знака |
| yOffset | Смещение в верхнем левом углу по оси Y водяного знака |

> **Примечание** Этот API поддерживает только добавление водяного знака изображения к основному потоку

## getAudioEffectManager

**getAudioEffectManager**

#### Получить класс управления звуковыми эффектами (TXAudioEffectManager).

` TXAudioEffectManager ` — это API управления звуковыми эффектами, с помощью которого вы можете реализовать следующие функции:

- Фоновая музыка: воспроизведение как онлайн-музыки, так и локальной музыки с различными функциями, такими как регулировка скорости, регулировка высоты тона, исходный голос, сопровождение и цикл.
- Мониторинг в наушниках: звук, захватываемый микрофоном, воспроизводится в наушниках в реальном времени, что обычно используется при прямых трансляциях музыки.
- Эффект реверберации: караоке в комнате, небольшая комната, большой зал, глубокий, резонансный и другие эффекты.
- Эффект изменения голоса: молодая девушка, мужчина среднего возраста, тяжёлый метал и другие эффекты.
- Короткий звуковой эффект: поддерживаются короткие файлы звуковых эффектов, такие как аплодисменты и смех (для файлов менее 10 секунд в длину установите параметр ` isShortFile ` в ` true `).

#### Return Desc:

класс управления звуковыми эффектами TXAudioEffectManager.

## startSystemAudioLoopback

**startSystemAudioLoopback**

| void startSystemAudioLoopback | (string deviceName) |
| --- | --- |

#### Включить захват системного звука (не поддерживается в iOS).

Этот API захватывает аудиоданные со звуковой карты компьютера якоря и смешивает их с текущим аудиопотоком SDK. Это гарантирует, что другие пользователи в комнате слышат звук, воспроизводимый компьютером якоря.

В сценариях онлайн-образования преподаватель может использовать этот API, чтобы SDK захватил звук учебных видео и транслировал его студентам в комнате.

В сценариях трансляции живой музыки якорь может использовать этот API, чтобы SDK захватил музыку, воспроизводимую его плеером, для добавления фоновой музыки в комнату.

| Param | DESC |
| --- | --- |
| deviceName | Если этот параметр пуст, захватывается звук всей системы. |

> **Примечание** На платформе Windows вы можете указать параметр ` deviceName ` абсолютным путём к исполняемому файлу (например, ` QQMuisc.exe `) определённого приложения. В этом случае SDK будет захватывать только звук этого приложения (поддерживается 32-битная версия SDK, 64-битная версия SDK требует Windows версии 10.0.19042 или выше). Вы также можете указать ` deviceName ` как имя определённого устройства динамика для захвата конкретного звука динамика (вы можете использовать интерфейс getDevicesList в TXDeviceManager для получения устройств динамика типа [TXMediaDeviceTypeSpeaker](https://www.tencentcloud.com/document/product/647/72274#f023a4d94be317eb399df83a25af6b2b)). На платформе Windows вы также можете указать ` deviceName ` как идентификатор процесса определённого процесса (в формате "process_xxx", где xxx — это идентификатор процесса), и затем SDK будет захватывать звук этого процесса (требует Windows версии 10.0.19042 или выше). Кроме того, на платформе Windows вы можете указать ` deviceName ` как идентификатор процесса определённого процесса, который должен быть исключён (в формате "exclude_process_xxx", где xxx — это идентификатор процесса), и затем SDK будет захватывать все звуки, кроме этого процесса (требует Windows версии 10.0.19042 или выше). О названии устройства динамика см. TXDeviceManager

## stopSystemAudioLoopback

**stopSystemAudioLoopback**

#### Остановить захват системного звука (не поддерживается в iOS).

## startScreenCapture

**startScreenCapture**

| void startScreenCapture | (GameObject view |
| --- | --- |
|  | [TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868) type |
|  | ref [TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/72275#b5beabfeefb812ccf1060aea67185c4e) param) |

#### Начать общий доступ к экрану.

Этот API может захватить содержимое всего экрана или определённого приложения и поделиться им с другими пользователями в той же комнате.

| Param | DESC |
| --- | --- |
| encParam | Параметры кодирования изображения, используемые для общего доступа к экрану, которые можно оставить пустыми, что указывает, что SDK будет выбирать оптимальные параметры кодирования (такие как разрешение и битрейт). |
| streamType | Канал, используемый для общего доступа к экрану, который может быть основным потоком ([TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868)) или подпотоком ([TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868)). |
| view | Родительский элемент управления элемента управления рендерингом, который можно установить в значение null, что указывает не отображать предпросмотр общего экрана. |

> **Примечание** 1. Пользователь может одновременно опубликовать максимум один основной поток ([TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868)) и один подпоток ([TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868)). 2. По умолчанию общий доступ к экрану использует изображение подпотока. Если вы хотите использовать основной поток для общего доступа к экрану, вам необходимо предварительно остановить захват камеры (через [stopLocalPreview](https://www.tencentcloud.com/document/product/647/72270#e379630cda7e794574b00d549b64a815)) чтобы избежать конфликтов. 3. Только один пользователь может использовать подпоток для общего доступа к экрану в одной комнате; то есть в одной комнате в любой момент времени допускается включение подпотока только одним пользователем. 4. Когда в комнате уже находится пользователь, использующий подпоток для общего доступа к экрану, вызов этого API вернёт обратный вызов ` onError(ERR_SERVER_CENTER_ANOTHER_USER_PUSH_SUB_VIDEO) ` из [ITRTCCloudCallback](https://www.tencentcloud.com/document/product/647/72271#338fdd109b5c9711d47c618b7d14b431).

## stopScreenCapture

**stopScreenCapture**

#### Остановить общий доступ к экрану.

## pauseScreenCapture

**pauseScreenCapture**

#### Приостановить общий доступ к экрану.

> **Примечание** Начиная с версии v11.5, приостановленный захват экрана будет использовать последний кадр для вывода с частотой кадров 1fps.

## resumeScreenCapture

**resumeScreenCapture**

#### Возобновить общий доступ к экрану.

## selectScreenCaptureTarget

**selectScreenCaptureTarget**

| void selectScreenCaptureTarget | (TRTCScreenCaptureSourceInfo source |
| --- | --- |
|  | Rect captureRect |
|  | TRTCScreenCaptureProperty property) |

#### Выбрать экран или окно для общего доступа (только для настольных систем).

После получения доступных для общего доступа экранов и окон через getScreenCaptureSources, вы можете вызвать этот API для выбора целевого экрана или окна, которым вы хотите поделиться.

Во время общего доступа к экрану вы также можете в любой момент вызвать этот API для переключения целевого объекта общего доступа.

Поддерживаются следующие четыре режима общего доступа:

- Общий доступ к полному экрану: для ` source `, у которого ` type ` — [TRTCScreenCaptureSourceTypeScreen](https://www.tencentcloud.com/document/product/647/72275#18d36b5519a892bf4b8b3f52a8b0a210) в ` sourceInfoList `, установите ` captureRect ` в ` { 0, 0, 0, 0 } `.
- Общий доступ к указанной области: для ` source `, у которого ` type ` — [TRTCScreenCaptureSourceTypeScreen](https://www.tencentcloud.com/document/product/647/72275#18d36b5519a892bf4b8b3f52a8b0a210) в ` sourceInfoList `, установите ` captureRect ` в ненулевое значение, например ` { 100, 100, 300, 300 } `.
- Общий доступ к полному окну: для ` source `, у которого ` type ` — [TRTCScreenCaptureSourceTypeWindow](https://www.tencentcloud.com/document/product/647/72275#18d36b5519a892bf4b8b3f52a8b0a210) в ` sourceInfoList `, установите ` captureRect ` в ` { 0, 0, 0, 0 } `.
- Общий доступ к указанной области окна: для ` source `, у которого ` type ` — [TRTCScreenCaptureSourceTypeWindow](https://www.tencentcloud.com/document/product/647/72275#18d36b5519a892bf4b8b3f52a8b0a210) в ` sourceInfoList `, установите ` captureRect ` в ненулевое значение, например ` { 100, 100, 300, 300 } `.

| Param | DESC |
| --- | --- |
| captureRect | Укажите область, которая будет захвачена |
| property | Укажите атрибуты целевого объекта общего доступа к экрану, такие как захват курсора и выделение захватываемого окна. Для получения дополнительной информации см. определение ` TRTCScreenCaptureProperty ` |
| source | Укажите источник общего доступа. Для получения дополнительной информации см. [TRTCScreenCaptureSourceInfo](https://www.tencentcloud.com/document/product/647/72275#16efc1045b787ecedb85e181e0c2ce29). |

> **Примечание** Установка параметров цвета и ширины границы выделения не действует на macOS.

## setSubStreamEncoderParam

**setSubStreamEncoderParam**

| void setSubStreamEncoderParam | (ref [TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/72275#b5beabfeefb812ccf1060aea67185c4e) param) |
| --- | --- |

#### Установить параметры кодирования видео для общего доступа к экрану (то есть подпотока) (для настольных и мобильных систем).

Этот API может установить качество изображения при общем доступе к экрану (то есть подпотока), просматриваемое удалёнными пользователями, и это также качество изображения при общем доступе к экрану в файлах записи на облаке.

Обратите внимание на различия между следующими двумя API:

- [setVideoEncoderParam](https://www.tencentcloud.com/document/product/647/72270#944184af05e4175e9458e5b0d563fb68) используется для установки параметров кодирования видео основного потока изображения ([TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868), обычно для камеры).
- [setSubStreamEncoderParam](https://www.tencentcloud.com/document/product/647/72270#b809f30d749d36cfbd2d02d3975af747) используется для установки параметров кодирования видео подпотока изображения ([TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868), обычно для общего доступа к экрану).

| Param | DESC |
| --- | --- |
| param | Параметры кодирования подпотока. Для получения дополнительной информации см. [TRTCVideoEncParam](https://www.tencentcloud.com/document/product/647/72275#b5beabfeefb812ccf1060aea67185c4e). |

## enableCustomVideoCapture

**enableCustomVideoCapture**

| void enableCustomVideoCapture | ([TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868) streamType |
| --- | --- |
|  | bool enable) |

#### Включить/отключить режим пользовательского захвата видео.

После включения этого режима SDK не будет запускать исходный процесс захвата видео (то есть остановит захват данных камеры и операции применения фильтра красоты) и сохранит только возможности кодирования и отправки видео.

Вам нужно использовать [sendCustomVideoData](https://www.tencentcloud.com/document/product/647/72270#8c8378c65a0b11187d6812523706a9f0) для непрерывного введения захваченного видеоизображения в SDK.

| Param | DESC |
| --- | --- |
| enable | Включить ли. Значение по умолчанию: false |
| streamType | Указать тип видеопотока ([TRTCVideoStreamTypeBig](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868): высокопольное большое изображение; [TRTCVideoStreamTypeSub](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868): подпоток изображения). |

## sendCustomVideoData

**sendCustomVideoData**

| void sendCustomVideoData | ([TRTCVideoStreamType](https://www.tencentcloud.com/document/product/647/72275#50d8d09e9837560e2946e7b187296868) streamType |
| --- | --- |
|  | [TRTCVideoFrame](https://www.tencentcloud.com/document/product/647/72275#9233a1b1573333abc70e53b51bd89740) frame) |

#### Передать захваченные видеокадры в SDK.

Вы можете использовать этот API для передачи захваченных видеокадров в SDK, и SDK будет кодировать и передавать их через собственный сетевой модуль.

Мы рекомендуем вам ввести следующую информацию для параметра [TRTCVideoFrame](https://www.tencentcloud.com/document/product/647/72275#9233a1b1573333abc70e53b51bd89740) (другие поля можно оставить пустыми):

- pixelFormat: в Windows и Android поддерживается только [TRTCVideoPixelFormat_I420](https://www.tencentcloud.com/document/product/647/72275#0fd3b6da1fb10e3d92eb55b00ba55dc3); в iOS и macOS поддерживаются [TRTCVideoPixelFormat_I420](https://www.tencentcloud.com/document/product/647/72275#0fd3b6da1fb10e3d92eb55b00ba55dc3) и [TRTCVideoPixelFormat_BGRA32](https://www.tencentcloud.com/document/product/647/72275#0fd3b6da1fb10e3d92eb55b00ba55dc3).
- bufferType: рекомендуется [TRTCVideoBufferType_Buffer](https://www.tencentcloud.com/document/product/647/72275#133a51a3a497d78c2b4d5de72ec7aaeb).
- data: буфер, используемый для переноса данных видеокадра.
- length: длина данных видеокадра. Если ` pixelFormat ` установлено на I420, ` length ` можно рассчитать по следующей формуле: ` length = width * height * 3 / 2 `.
- width: ширина видеоизображения, например 640 пикс.
- height: высота видеоизображения, например 480 пикс.
- timestamp (ms): установите его в момент времени, когда были захвачены видеокадры, который вы можете получить, вызвав generateCustomPTS после получения видеокадра.

Для получения дополнительной информации см. [Пользовательский захват и рендеринг](https://www.tencentcloud.com/document/product

## setAudioFrameCallback

**setAudioFrameCallback**

| int setAudioFrameCallback | ([ITRTCAudioFrameCallback](https://www.tencentcloud.com/document/product/647/72271#c83add42f0e7122e1149d522041a5af4) callback) |
| --- | --- |

#### Установить пользовательский обратный вызов для данных аудио.

После установки этого обратного вызова SDK будет внутренне вызывать данные аудио (в формате PCM), включая:

- onCapturedAudioFrame: обратный вызов аудиоданных, захватываемых локальным микрофоном
- [onLocalProcessedAudioFrame](https://www.tencentcloud.com/document/product/647/72271#7013577cbc775c66b7d94a1299b86a64): обратный вызов аудиоданных, захватываемых локальным микрофоном и предварительно обработанных модулем аудио
- [onPlayAudioFrame](https://www.tencentcloud.com/document/product/647/72271#e5b854ddfd36ca3dec95c5ec30a381e2): аудиоданные от каждого удаленного пользователя до смешивания аудио
- [onMixedPlayAudioFrame](https://www.tencentcloud.com/document/product/647/72271#9e10a31ea56497b681f9c8fa7b36c52b): обратный вызов аудиоданных, которые будут воспроизводиться системой после смешивания аудиопотоков

> **Примечание**: Установка обратного вызова в значение null указывает на остановку пользовательского обратного вызова аудио, а установка его в ненулевое значение указывает на запуск пользовательского обратного вызова аудио.

## setCapturedAudioFrameCallbackFormat

**setCapturedAudioFrameCallbackFormat**

| int setCapturedAudioFrameCallbackFormat | ([TRTCAudioFrameCallbackFormat](https://www.tencentcloud.com/document/product/647/72275#352b0878415e79fcd48d9027fab3f683) format) |
| --- | --- |

#### Установить формат обратного вызова аудиокадров, захватываемых локальным микрофоном.

Этот API используется для установки формата `AudioFrame`, вызываемого функцией onCapturedAudioFrame:

- sampleRate: частота дискретизации. Допустимые значения: 16000, 32000, 44100, 48000
- channel: количество каналов (при использовании стерео данные чередуются). Допустимые значения: 1: моноканал; 2: двухканальный
- samplesPerCall: количество точек выборки, которое определяет длину кадра данных обратного вызова. Длина кадра должна быть целым кратным 10 мс.

Если вы хотите рассчитать длину кадра обратного вызова в миллисекундах, формула преобразования количества миллисекунд в количество точек выборки выглядит следующим образом: количество точек выборки = количество миллисекунд * частота дискретизации / 1000

Например, если вы хотите вызвать данные длины кадра 20 мс с частотой дискретизации 48000, количество точек выборки должно быть введено как `960 = 20 * 48000 / 1000`.

Обратите внимание, что длина кадра окончательного обратного вызова выражается в байтах, а формула преобразования количества точек выборки в количество байтов выглядит следующим образом: `количество байтов = количество точек выборки * количество каналов * 2 (битовая глубина)`

Например, если параметры составляют частоту дискретизации 48000, двухканальный, длину кадра 20 мс и 960 точек выборки, то количество байтов составляет `3840 = 960 * 2 * 2`

| Параметр | Описание |
| --- | --- |
| format | Формат обратного вызова аудиоданных |

#### Описание возвращаемого значения:

0: успешно; значения меньше 0: ошибка (для получения дополнительной информации см. TXLiteAVError)

## setLocalProcessedAudioFrameCallbackFormat

**setLocalProcessedAudioFrameCallbackFormat**

| int setLocalProcessedAudioFrameCallbackFormat | ([TRTCAudioFrameCallbackFormat](https://www.tencentcloud.com/document/product/647/72275#352b0878415e79fcd48d9027fab3f683) format) |
| --- | --- |

#### Установить формат обратного вызова предварительно обработанных локальных аудиокадров.

Этот API используется для установки формата `AudioFrame`, вызываемого функцией [onLocalProcessedAudioFrame](https://www.tencentcloud.com/document/product/647/72271#7013577cbc775c66b7d94a1299b86a64):

- sampleRate: частота дискретизации. Допустимые значения: 16000, 32000, 44100, 48000
- channel: количество каналов (при использовании стерео данные чередуются). Допустимые значения: 1: моноканал; 2: двухканальный
- samplesPerCall: количество точек выборки, которое определяет длину кадра данных обратного вызова. Длина кадра должна быть целым кратным 10 мс.

Если вы хотите рассчитать длину кадра обратного вызова в миллисекундах, формула преобразования количества миллисекунд в количество точек выборки выглядит следующим образом: `количество точек выборки = количество миллисекунд * частота дискретизации / 1000`.

Например, если вы хотите вызвать данные длины кадра 20 мс с частотой дискретизации 48000, количество точек выборки должно быть введено как `960 = 20 * 48000 / 1000`.

Обратите внимание, что длина кадра окончательного обратного вызова выражается в байтах, а формула преобразования количества точек выборки в количество байтов выглядит следующим образом: `количество байтов = количество точек выборки * количество каналов * 2 (битовая глубина)`.

Например, если параметры составляют частоту дискретизации 48000, двухканальный, длину кадра 20 мс и 960 точек выборки, то количество байтов составляет `3840 = 960 * 2 * 2`.

| Параметр | Описание |
| --- | --- |
| format | Формат обратного вызова аудиоданных |

#### Описание возвращаемого значения:

0: успешно; значения меньше 0: ошибка (для получения дополнительной информации см. TXLiteAVError)

## setMixedPlayAudioFrameCallbackFormat

**setMixedPlayAudioFrameCallbackFormat**

| int setMixedPlayAudioFrameCallbackFormat | ([TRTCAudioFrameCallbackFormat](https://www.tencentcloud.com/document/product/647/72275#352b0878415e79fcd48d9027fab3f683) format) |
| --- | --- |

#### Установить формат обратного вызова аудиокадров, которые будут воспроизводиться системой.

Этот API используется для установки формата `AudioFrame`, вызываемого функцией [onMixedPlayAudioFrame](https://www.tencentcloud.com/document/product/647/72271#9e10a31ea56497b681f9c8fa7b36c52b):

- sampleRate: частота дискретизации. Допустимые значения: 16000, 32000, 44100, 48000
- channel: количество каналов (при использовании стерео данные чередуются). Допустимые значения: 1: моноканал; 2: двухканальный
- samplesPerCall: количество точек выборки, которое определяет длину кадра данных обратного вызова. Длина кадра должна быть целым кратным 10 мс.

Если вы хотите рассчитать длину кадра обратного вызова в миллисекундах, формула преобразования количества миллисекунд в количество точек выборки выглядит следующим образом: `количество точек выборки = количество миллисекунд * частота дискретизации / 1000`.

Например, если вы хотите вызвать данные длины кадра 20 мс с частотой дискретизации 48000, количество точек выборки должно быть введено как `960 = 20 * 48000 / 1000`.

Обратите внимание, что длина кадра окончательного обратного вызова выражается в байтах, а формула преобразования количества точек выборки в количество байтов выглядит следующим образом: `количество байтов = количество точек выборки * количество каналов * 2 (битовая глубина)`.

Например, если параметры составляют частоту дискретизации 48000, двухканальный, длину кадра 20 мс и 960 точек выборки, то количество байтов составляет `3840 = 960 * 2 * 2`.

| Параметр | Описание |
| --- | --- |
| format | Формат обратного вызова аудиоданных |

#### Описание возвращаемого значения:

0: успешно; значения меньше 0: ошибка (для получения дополнительной информации см. TXLiteAVError)

## sendCustomCmdMsg

**sendCustomCmdMsg**

| bool sendCustomCmdMsg | (int cmdId |
| --- | --- |
|  | byte[] data |
|  | int dataSize |
|  | bool reliable |
|  | bool ordered) |

#### Использовать UDP канал для отправки пользовательского сообщения всем пользователям в комнате.

Этот API позволяет вам использовать UDP канал TRTC для трансляции пользовательских данных другим пользователям в текущей комнате для передачи сигналов.

Другие пользователи в комнате могут получить сообщение через обратный вызов `onRecvCustomCmdMsg` в [ITRTCCloudCallback](https://www.tencentcloud.com/document/product/647/72271#338fdd109b5c9711d47c618b7d14b431).

| Параметр | Описание |
| --- | --- |
| cmdID | ID сообщения. Диапазон значений: [1, 10] |
| data | Сообщение для отправки. Максимальная длина одного сообщения составляет 1 КБ. |
| ordered | Включена ли упорядоченная отправка, то есть должны ли пакеты данных приниматься в том же порядке, в котором они отправляются; если да, это вызовет определенную задержку. |
| reliable | Включена ли надежная отправка. Надежная отправка может обеспечить более высокую вероятность успеха, но с более длительной задержкой приема, чем ненадежная отправка. |

> **Примечание**: 1. Максимум 30 сообщений можно отправить в секунду всем пользователям в комнате (это не поддерживается для веб и мини-программ в настоящее время; это ограничение является общим с [sendSEIMsg](https://www.tencentcloud.com/document/product/647/72270#2d918c3d0ef54d41bd5f5adcb62f63d6)). 2. Пакет может содержать до 1 КБ данных; если этот порог превышен, пакет с большой вероятностью будет отброшен промежуточным маршрутизатором или сервером (это ограничение является общим с [sendSEIMsg](https://www.tencentcloud.com/document/product/647/72270#2d918c3d0ef54d41bd5f5adcb62f63d6)). 3. Клиент может отправлять максимум 16 КБ данных в общей сложности за секунду. 4. `reliable` и `ordered` должны быть установлены на одинаковые значения (`true` или `false`) и в настоящее время не могут быть установлены на разные значения. 5. Настоятельно рекомендуем использовать различные значения `cmdID` для сообщений разных типов. Это может уменьшить задержку сообщений при требовании упорядоченной отправки. 6. В настоящее время поддерживается только роль якоря.

#### Описание возвращаемого значения:

true: сообщение отправлено успешно; false: ошибка при отправке сообщения.

## sendSEIMsg

**sendSEIMsg**

| bool sendSEIMsg | (byte[] data |
| --- | --- |
|  | int dataSize |
|  | int repeatCount) |

#### Использовать SEI канал для отправки пользовательского сообщения всем пользователям в комнате.

Этот API позволяет вам использовать SEI канал TRTC для трансляции пользовательских данных другим пользователям в текущей комнате для передачи сигналов.

Заголовок видеокадра содержит блок данных заголовка, называемый SEI. Этот API работает путем встраивания пользовательских данных сигналов, которые вы хотите отправить, в блок SEI и отправки его вместе с видеокадром.

Таким образом, SEI канал имеет лучшую совместимость, чем [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/72270#20d4d41de96d8e2e6d2cf6499ea55171), так как данные сигналов могут быть переданы в CSS CDN вместе с видеокадром.

Однако, поскольку блок данных заголовка видеокадра не может быть слишком большим, рекомендуем ограничить размер данных сигналов всего несколькими байтами при использовании этого API.

Наиболее распространенное применение - встраивание пользовательской временной метки в видеокадры через этот API, чтобы достичь идеального совмещения между сообщением и видеоизображением (например, между учебным материалом и видеосигналом в сценарии образования).

Другие пользователи в комнате могут получить сообщение через обратный вызов `onRecvSEIMsg` в [ITRTCCloudCallback](https://www.tencentcloud.com/document/product/647/72271#338fdd109b5c9711d47c618b7d14b431).

| Параметр | Описание |
| --- | --- |
| data | Данные для отправки, которые могут быть до 1 КБ (1000 байтов) |
| repeatCount | Количество отправок данных |

> **Примечание**: Этот API имеет следующие ограничения: 1. Данные не будут отправлены мгновенно после вызова этого API; вместо этого они будут вставлены в следующий видеокадр после вызова API. 2. Максимум 30 сообщений можно отправить в секунду всем пользователям в комнате (это ограничение является общим с [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/72270#20d4d41de96d8e2e6d2cf6499ea55171)). 3. Каждый пакет может быть до 1 КБ (это ограничение является общим с [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/72270#20d4d41de96d8e2e6d2cf6499ea55171)). Если отправляется большой объем данных, видеобитрейт увеличится, что может снизить качество видео или даже вызвать зависание. 4. Каждый клиент может отправлять максимум 16 КБ данных в общей сложности за секунду (это ограничение является общим с [sendCustomCmdMsg](https://www.tencentcloud.com/document/product/647/72270#20d4d41de96d8e2e6d2cf6499ea55171)). 5. Если требуется несколько отправок (то есть `repeatCount` > 1), данные будут вставлены в последующие `repeatCount` видеокадров подряд для отправки, что увеличит видеобитрейт. 6. Если `repeatCount` больше 1, данные будут отправлены несколько раз, и одно и то же сообщение может быть получено несколько раз в обратном вызове [onRecvSEIMsg](https://www.tencentcloud.com/document/product/647/72271#10bd0c1f0010a55c27922dadd2723042); поэтому требуется дедупликация.

#### Описание возвращаемого значения:

true: сообщение разрешено и будет отправлено с последующими видеокадрами; false: сообщение не разрешено для отправки

## startSpeedTest

**startSpeedTest**

| void startSpeedTest | ([TRTCSpeedTestParams](https://www.tencentcloud.com/document/product/647/72275#dd22aad94fc4b4773ca7323c7d34a1a7) testParams) |
| --- | --- |

#### Начать тест скорости сети (используется перед входом в комнату).

| Параметр | Описание |
| --- | --- |
| params | опции теста скорости |

> **Примечание**: 1. Процесс измерения скорости будет требовать небольшую сумму за базовые услуги, см. [Руководство по покупке > Базовые услуги](https://intl.cloud.tencent.com/document/product/647/34610?lang=en&pg=#basic-services). 2. Пожалуйста, проводите тест скорости сети перед входом в комнату, потому что если тест проводится после входа в комнату, он повлияет на нормальную передачу аудио/видео, и его результат будет неточным из-за помех в комнате. 3. Одновременно может выполняться только одна задача теста скорости сети.

#### Описание возвращаемого значения:

результат вызова интерфейса, <0: сбой

## stopSpeedTest

**stopSpeedTest**

#### Остановить тест скорости сети.

## getScriptVersion

**getScriptVersion**

#### Получить информацию о версии ScriptVersion SDK.

## getSDKVersion

**getSDKVersion**

#### Получить информацию о версии SDK.

## setLogLevel

**setLogLevel**

| void setLogLevel | ([TRTCLogLevel](https://www.tencentcloud.com/document/product/647/72275#3b7ff44175cba4dd48e97aa8ac7b0b98) level) |
| --- | --- |

#### Установить уровень вывода журнала.

| Параметр | Описание |
| --- | --- |
| level | Для получения дополнительной информации см. [TRTCLogLevel](https://www.tencentcloud.com/document/product/647/72275#3b7ff44175cba4dd48e97aa8ac7b0b98). Значение по умолчанию: [TRTCLogLevelNone](https://www.tencentcloud.com/document/product/647/72275#3b7ff44175cba4dd48e97aa8ac7b0b98) |

## setConsoleEnabled

**setConsoleEnabled**

| void setConsoleEnabled | (bool enabled) |
| --- | --- |

#### Включить/отключить вывод журнала в консоль.

| Параметр | Описание |
| --- | --- |
| enabled | Укажите, включить ли это, что отключено по умолчанию |

## setLogCompressEnabled

**setLogCompressEnabled**

| void setLogCompressEnabled | (bool enabled) |
| --- | --- |

#### Включить/отключить сжатие локального журнала.

Если сжатие включено, размер журнала значительно сократится, но журналы можно прочитать только после распаковки с помощью скрипта Python, предоставленного Tencent Cloud.

Если сжатие отключено, журналы будут сохранены в виде открытого текста и могут быть прочитаны непосредственно в Notepad, но займут больше места для хранения.

| Параметр | Описание |
| --- | --- |
| enabled | Укажите, включить ли это, что включено по умолчанию |

## setLogDirPath

**setLogDirPath**

| void setLogDirPath | (string path) |
| --- | --- |

#### Установить путь локального хранилища журналов.

Вы можете использовать этот API для изменения пути хранения по умолчанию локальных журналов SDK, который выглядит следующим образом:

- Windows: C:/Users/[username]/AppData/Roaming/liteav/log, то есть в `%appdata%/liteav/log`.
- iOS или macOS: в `sandbox Documents/log`.
- Android: в `/app directory/files/log/liteav/`.

| Параметр | Описание |
| --- | --- |
| path | Путь хранилища журналов |

> **Примечание**: Обязательно вызовите этот API перед всеми другими API и убедитесь, что указанный вами каталог существует и ваше приложение имеет права на чтение/запись для этого каталога.

## setLogCallback

**setLogCallback**

| void setLogCallback | ([ITRTCLogCallback](https://www.tencentcloud.com/document/product/647/72271#486f92ae649081ecfa3769fb441f77da) callback) |
| --- | --- |

#### Установить обратный вызов журнала.

## callExperimentalAPI

**callExperimentalAPI**

| void callExperimentalAPI | (string jsonStr) |
| --- | --- |

#### Вызвать экспериментальные API.


---
*Источник: [https://trtc.io/document/72270](https://trtc.io/document/72270)*

---
*Источник (EN): [itrtccloud.md](./itrtccloud.md)*

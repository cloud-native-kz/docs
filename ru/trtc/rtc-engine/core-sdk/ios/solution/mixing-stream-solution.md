# Решение для микширования потока

## Специфическая реализация кода

### 1. Создание основного и вспомогательного экземпляров

```
// Create TRTCCloud main instance (vocal instance)TRTCCloud *trtcCloud = [TRTCCloud sharedInstance];// Create TRTCCloud sub-instance (accompaniment instance)TRTCCloud *subCloud = [trtcCloud createSubCloud];
```

> **Примечание:** В схеме хорового пения в реальном времени ведущему исполнителю необходимо отдельно создать основной экземпляр (вокальный экземпляр) и вспомогательный экземпляр (экземпляр аккомпанемента) для загрузки вокала и фоновой музыки.

### 2. Вокальный экземпляр входит в комнату и отправляет поток

```
TRTCParams *params = [[TRTCParams alloc] init];params.sdkAppId = sdkAppId;params.userId = userId;params.userSig = userSign;params.role = TRTCRoleAnchor;params.roomId = roomIdIntValue;[trtcCloud enterRoom:params appScene:TRTCAppSceneLIVE];// Turn on audio uplink and set audio quality[trtcCloud startLocalAudio:TRTCAudioQualityMusic];// Set media type[trtcCloud setSystemVolumeType:TRTCSystemVolumeTypeMedia];// Mute remote accompaniment music[trtcCloud muteRemoteAudio:remoteAudioId mute:YES];
```

> **Примечание:** В чистых сценариях RTC-аудио рекомендуется использовать VOICE_CHATROOM для входа в комнату. Если требуется видео или перенаправление CDN, для входа в комнату необходимо использовать сценарий LIVE, поскольку VOICE_CHATROOM добавляет параметры чистого аудио при перенаправлении, что приводит к невозможности передачи SEI-сообщений. Ведущему исполнителю/хору необходимо использовать muteRemoteAudio(true) для отписки от аудиопотока, загруженного экземпляром аккомпанемента, иначе локальная и удалённая фоновая музыка будут воспроизводиться повторно.

### 3. Экземпляр аккомпанемента: присоединение к комнате и отправка потока.

```
TRTCParams *bgmParams = [[TRTCParams alloc] init];bgmParams.sdkAppId = sdkAppId;bgmParams.userId = [NSString stringWithFormat:@"%@%@",userId,@"_bgm"];bgmParams.userSig = bgmUserSign;bgmParams.role = TRTCRoleAnchor;bgmParams.roomId = roomIdIntValue;[subCloud enterRoom:bgmParams appScene:TRTCAppSceneLIVE];// Set media type[subCloud setSystemVolumeType:TRTCSystemVolumeTypeMedia];// Enable preloadingNSDictionary *jsonDict = @{                              @"api": @"preloadMusic",                              @"params": @{                                            @"musicId": @(self.currentPlayMusicID),                                            @"path": path,                                            @"startTimeMS": @(startMs),                                           }                             };NSData *jsonData = [NSJSONSerialization dataWithJSONObject:jsonDict options:0 error:NULL];NSString *jsonString = [[NSString alloc] initWithData:jsonData encoding:NSUTF8StringEncoding];[subCloud callExperimentalAPI:jsonString];// Play accompaniment music and push the stream (play at the agreed time)TXAudioMusicParam *musicParam = [[TXAudioMusicParam alloc] init];musicParam.ID = musicID;musicParam.path = url;musicParam.loopCount = 0;musicParam.publish = YES;// Send accompaniment music to the remote endparam.publish = YES;[[subCloud getAudioEffectManager] startPlayMusic:musicParam onStart:startBlock onProgress:progressBlock onComplete:completedBlock]
```

> **Примечание:** Обратите внимание на различие между userId основного экземпляра и вспомогательного экземпляра, убедитесь, что они не дублируются и легко идентифицируются; параметры фоновой музыки musicParam экземпляра аккомпанемента: publish = YES (в то время как музыка воспроизводится локально, удалённые пользователи также могут слышать музыку), publish = NO (значение по умолчанию, музыка может быть услышана только локально, удалённые пользователи не могут её слышать).

### 4. Инициирование микширования потока с транскодированием и отправка обратно.

```
// Create a TRTCPublishTarget objectTRTCPublishTarget *publishTarget = [[TRTCPublishTarget alloc] init];// Push back to the room after mixing, if publishing to CDN, fill in TRTCPublishMixStreamToCdnpublishTarget.mode = TRTCPublishMixStreamToRoom;// The userid of the mixing robot, which cannot be duplicated with other users' userid in the roompublishTarget.mixStreamIdentity = [NSString stringWithFormat:@"%@%@",userId,@"_mix"]; // Set the encoding parameters of the transcoded audio streamTRTCStreamEncoderParam *streamEncoderParam = [[TRTCStreamEncoderParam alloc] init];streamEncoderParam.videoEncodedFPS = 15;streamEncoderParam.videoEncodedGOP = 3;streamEncoderParam.videoEncodedKbps = 30;streamEncoderParam.audioEncodedSampleRate = 48000;streamEncoderParam.audioEncodedChannelNum = 2;streamEncoderParam.audioEncodedKbps = 64;streamEncoderParam.audioEncodedCodecType = 2;// Set audio mixing parametersTRTCStreamMixingConfig *streamMixingConfig = [[TRTCStreamMixingConfig alloc] init];// Support filling in empty values, which will automatically mix the audio of all hosts and outputstreamMixingConfig.audioMixUserList = @[];// Initiate mixed stream transcoding and pushing request[trtcCloud startPublishMediaStream:publishTarget encoderParam:streamEncoderParam mixingConfig:streamMixingConfig];
```

> **Примечание:** Рекомендуется в первую очередь ведущему исполнителю инициировать микширование потока с транскодированием и отправить через робота микширования на серверную часть, смешав фоновую музыку и все вокальные потоки и отправить их обратно в комнату TRTC или отправить на живой CDN. В режиме автоматической подписки хосты, участвующие в микшировании потока с транскодированием, по умолчанию будут загружать отдельные потоки друг друга и не получат смешанный поток, отправленный обратно в комнату; аудитория автоматически загружает смешанный поток, отправленный обратно в комнату, и больше не получает отдельные потоки. Метод микширования потока с транскодированием и отправкой startPublishMediaStream, используемый здесь, принимает совершенно новую архитектуру серверной части. Приложение старой версии должно предоставить SdkAppId для подачи заявления на обновление перед использованием.

---
*Источник: [https://trtc.io/document/57035](https://trtc.io/document/57035)*

---
*Источник (EN): [mixing-stream-solution.md](./mixing-stream-solution.md)*

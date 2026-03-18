# Решение для смешивания потоков

## Реализация конкретного кода

### 1. Создание основного и дополнительного экземпляров

```
// Create TRTCCloud main instance (vocal instance)TRTCCloud mTRTCCloud = TRTCCloud.sharedInstance(getApplicationContext());// Create TRTCCloud sub-instance (accompaniment instance)TRTCCloud subCloud = mTRTCCloud.createSubCloud();
```

> **Примечание:** В схеме хорового пения в реальном времени ведущий певец должен создать основной экземпляр — экземпляр вокала и дополнительный экземпляр — экземпляр сопровождения отдельно для загрузки вокала и музыки сопровождения.

### 2. Экземпляр вокала входит в комнату и отправляет поток

```
TRTCCloudDef.TRTCParams params = new TRTCCloudDef.TRTCParams();params.sdkAppId = sdkAppId;params.userId = mUserId;params.userSig = userSig;params.role = TRTCCloudDef.TRTCRoleAnchor;params.roomId = mRoomId;mTRTCCloud.enterRoom(params, TRTCCloudDef.TRTC_APP_SCENE_LIVE);// Turn on audio uplink and set audio qualitymTRTCCloud.startLocalAudio(TRTCCloudDef.TRTC_AUDIO_QUALITY_MUSIC);// Set media typemTRTCCloud.setSystemVolumeType(TRTCCloudDef.TRTCSystemVolumeTypeMedia);// Mute remote accompaniment musicmTRTCCloud.muteRemoteAudio(mUserId + "_bgm", true);
```

> **Примечание:** В чистых сценариях аудио RTC рекомендуется использовать VOICE_CHATROOM для входа в комнату. Если требуется трансляция видео или переадресация на CDN, сценарий входа в комнату должен использовать LIVE, так как VOICE_CHATROOM добавит параметры чистого аудио при переадресации, что вызовет сбой при передаче сообщений SEI. Ведущий певец/хорист должен использовать muteRemoteAudio(true) для отписки от потока аудио, загруженного экземпляром сопровождения, в противном случае музыка сопровождения будет воспроизводиться повторно локально и удаленно.

### 3. Экземпляр сопровождения входит в комнату и отправляет поток

```
TRTCCloudDef.TRTCParams bgmParams = new TRTCCloudDef.TRTCParams();bgmParams.sdkAppId = sdkAppId;bgmParams.userId = mUserId + "_bgm";bgmParams.userSig = userSig;bgmParams.role = TRTCCloudDef.TRTCRoleAnchor;bgmParams.roomId = mRoomId;subCloud.enterRoom(bgmParams, TRTCCloudDef.TRTC_APP_SCENE_LIVE);// Set media typesubCloud.setSystemVolumeType(TRTCCloudDef.TRTCSystemVolumeTypeMedia);// Enable preloadingsubCloud.callExperimentalAPI("{\\"api\\":\\"preloadMusic\\",\\"params\\": {\\"musicId\\":musicId,\\"path\\":\\"path\\",\\"startTimeMS\\":startTimeMS}}");// Play accompaniment music and push the stream (play at the agreed time)TXAudioEffectManager.AudioMusicParam param = new TXAudioEffectManager.AudioMusicParam(musicID, musicPath);// Send accompaniment music to the remote endparam.publish = true;subCloud.getAudioEffectManager().startPlayMusic(param);
```

> **Примечание:** Обратите внимание на различие между userId основного экземпляра и дополнительного экземпляра, обеспечивая отсутствие дублирования и легкую идентификацию. Параметры фоновой музыки экземпляра сопровождения AudioMusicParam: publish = true (во время воспроизведения музыки локально удаленные пользователи также могут слышать музыку); publish = false (значение по умолчанию, музыка может быть услышана только локально, удаленные пользователи не могут ее услышать).

### 4. Инициировать смешивание потока и отправку с транскодированием

```
// Create a TRTCPublishTarget objectTRTCCloudDef.TRTCPublishTarget target = new TRTCCloudDef.TRTCPublishTarget();// Push back to the room after mixing, if publishing to CDN, fill in TRTC_PublishMixStream_ToCdntarget.mode = TRTCCloudDef.TRTC_PublishMixStream_ToRoom;target.mixStreamIdentity.intRoomId = Integer.parseInt(mRoomId);// The userid of the mixing robot, which cannot be duplicated with other users' userid in the roomtarget.mixStreamIdentity.userId = mUserId + "_mix"; // Set the encoding parameters of the transcoded audio streamTRTCCloudDef.TRTCStreamEncoderParam trtcStreamEncoderParam = new TRTCCloudDef.TRTCStreamEncoderParam();trtcStreamEncoderParam.audioEncodedChannelNum = 2;trtcStreamEncoderParam.audioEncodedKbps = 64;trtcStreamEncoderParam.audioEncodedCodecType = 2;trtcStreamEncoderParam.audioEncodedSampleRate = 48000;// Set audio mixing parametersTRTCCloudDef.TRTCStreamMixingConfig trtcStreamMixingConfig = new TRTCCloudDef.TRTCStreamMixingConfig();// Support filling in empty values, which will automatically mix the audio of all hosts and outputtrtcStreamMixingConfig.audioMixUserList = null;// Initiate mixed stream transcoding and pushing requestmTRTCCloud.startPublishMediaStream(target, trtcStreamEncoderParam, trtcStreamMixingConfig);
```

> **Примечание:** Рекомендуется, чтобы ведущий певец в первую очередь инициировал смешивание потока и отправку через робота смешивания на серверную часть, смешивая музыку сопровождения и все потоки вокала и отправляя их обратно в комнату TRTC или отправляя на CDN трансляции. В режиме автоматической подписки хосты, участвующие в смешивании потока и транскодировании, по умолчанию будут извлекать отдельные потоки друг друга и не будут получать смешанный поток, отправленный обратно в комнату; аудитория будет автоматически извлекать смешанный поток, отправленный обратно в комнату, и больше не будет получать отдельные потоки. Метод смешивания потока и отправки startPublishMediaStream, используемый здесь, применяет совершенно новую архитектуру серверной части. Старая версия приложения должна предоставить SdkAppId для подачи заявки на обновление перед использованием.


---
*Источник: [https://trtc.io/document/57036](https://trtc.io/document/57036)*

---
*Источник (EN): [mixing-stream-solution.md](./mixing-stream-solution.md)*

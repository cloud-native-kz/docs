# Синхронизация песен

В решении реального времени требуется синхронизация хода воспроизведения песни в реальном времени, чтобы избежать увеличения сквозной задержки из-за ошибок песни после начала выступления. Синхронизация песни требует использования времени NTP, так как локальные часы разных устройств не совпадают и имеют некоторую погрешность. Поэтому необходимо использовать собственный сервис NTP Tencent Cloud. Кроме того, пользователи, присоединяющиеся к хору в середине процесса, также должны синхронизировать ход воспроизведения песни, прежде чем они смогут участвовать в хоре.

## Процесс реализации

Практика синхронизации песни выглядит следующим образом: ведущий певец договаривается начать воспроизведение песни в определенный момент в будущем (например, через задержку в N секунд), а другие пользователи участвуют в хоре. Время каждого конца основано на времени NTP, которое будет синхронизировано после инициализации TRTC SDK.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/0dc790fb5b7411ee974d5254005f490f.png)

Конкретный процесс следующий:

1. Каждая сторона выполняет калибровку NTP, обновляет и получает последнее время NTP T из облака TRTC.
2. Ведущий певец отправляет сигнал хора (пользовательское сообщение), согласовывая время начала T2 для хора.
3. Локальная сторона предварительно загружает песню в соответствии с T2 и воспроизводит её по расписанию.
4. Другие пользователи хора выполняют шаг 3 после получения сигнала хора.
5. В процессе проверяется локальный ход воспроизведения песни, и когда разница между TE и TC превышает 50 мс, выполняется калибровка поиска.

> **Примечание:** Упомянутая здесь погрешность в 50 мс является типичным значением и может быть отрегулирована в соответствии с допуском бизнеса. Рекомендуется колебаться около 50 мс.

## Диаграмма синхронизации

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3ffc0e8b5c1b11ee94c3525400d793d0.png)

Синхронизацию песни можно разделить в основном на три части: калибровку NTP, отправку и получение сигналов хора, а также коррекцию хода воспроизведения песни. Конкретная реализация кода для этих трех частей будет предоставлена ниже.

## Реализация ключевого кода

### **1.** Сервис калибровки NTP

```
TXLiveBase.setListener(new TXLiveBaseListener() {    @Override    public void onUpdateNetworkTime(int errCode, String errMsg) {        super.onUpdateNetworkTime(errCode, errMsg);        // errCode 0: Calibration is successful and the deviation is within 30ms;        //         1: Calibration is successful, but the deviation may be more than 30ms;        //         -1: Calibration failed.        if (errCode == 0) {            // Call getNetworkTimestamp of TXLivebase to get the NTP timestamp.            long ntpTime = TXLiveBase.getNetworkTimestamp();        } else {            // Call updateNetworkTime again to start a calibration.            TXLiveBase.updateNetworkTime();        }    }});TXLiveBase.updateNetworkTime();
```

### **2.** Ведущий певец отправляет сигнал хора

```
JSONObject jsonObject = new JSONObject();jsonObject.put("cmd", "startChorus");// Agree on a time for the chorus.jsonObject.put("startPlayMusicTS", startTs);jsonObject.put("musicId", "musicId");String body = jsonObject.toString();mTRTCCloud.sendCustomCmdMsg(0, body.getBytes(), false, false);
```

> **Примечание:** Рекомендуется, чтобы ведущий певец отправлял сообщения сигналов хора в комнату с фиксированным интервалом времени, чтобы пользователи хора могли присоединиться к хору в середине процесса. **Причина для неиспользования SEI сообщений для отправки сигналов хора:** Информация SEI будет вставлена в видеокадр, что приведет к тому, что видеопоток, полученный аудиторией, будет содержать много недействительной информации.

### **3.** Пользователь хора получает сигнал хора

```
public void onRecvCustomCmdMsg(String userId, int cmdID, int seq, byte[] message) {    JSONObject json = new JSONObject(new String(message, "UTF-8"));    String cmd = json.getString("cmd");    // Chorus command    if (cmd.equals("startChorus")) {    // Chorus start time    long startPlayMusicTs = json.getLong("startPlayMusicTS");    int musicId = json.getInt("musicId");    // The difference between the agreed chorus time and the current time    long delayMs = Math.abs(startPlayMusicTs - getNtpTime());    // Start preloading, and jump the song progress according to the agreed chorus time and the current NTP difference.    mTRTCCloud.callExperimentalAPI("{\\"api\\":\\"preloadMusic\\",\\"params\\": {\\"musicId\\":musicId,\\"path\\":\\"path\\",\\"startTimeMS\\":delayMs}}");    // Play the song    TXAudioEffectManager.AudioMusicParam param = new TXAudioEffectManager.AudioMusicParam(musicId, musicPath);    param.publish = false;    mTRTCCloud.getAudioEffectManager().startPlayMusic(param);}
```

> **Примечание:** После того как пользователь хора получит первый сигнал startChorus, статус должен измениться с "не в хоре" на "в хоре", и больше не отвечать на сигналы startChorus, чтобы избежать перезапуска воспроизведения BGM.

### **4.** Коррекция хода воспроизведения песни

```
long mStartPlayMusicTs = "The initially agreed chorus time"ï¼long currentProgress = subCloud.getAudioEffectManager().getMusicCurrentPosInMS(musicID);// The ideal playback progress of the current songlong estimatedProgress = getNtpTime() - mStartPlayMusicTs;// When the playback progress exceeds 50ms, make correctionsif (estimatedProgress >= 0 &&; Math.abs(currentProgress - estimatedProgress) > 50) {    subCloud.getAudioEffectManager().seekMusicToPosInMS(mMusicID, (int) estimatedProgress);}
```


---
*Источник: [https://trtc.io/document/57026](https://trtc.io/document/57026)*

---
*Источник (EN): [song-synchronization.md](./song-synchronization.md)*

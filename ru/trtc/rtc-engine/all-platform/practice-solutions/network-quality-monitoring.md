# Мониторинг качества сети

Чтобы помочь пользователям лучше осознавать качество сети, мы рекомендуем бизнес-персоналу выполнять тест скорости перед звонками, отслеживать качество сети и статус соединения во время звонков, а также предоставлять соответствующие подсказки в интерфейсе и уведомления. Таким образом, пользователи могут легко оценить текущее качество своей сети и своевременно отрегулировать параметры сети для оптимальной производительности звонков.

## Выполнение тестов скорости сети перед звонками

Обычные пользователи часто не осознают условия своей сети. Поэтому рекомендуется выполнить тест скорости перед звонками. Это поможет пользователям оценить текущее качество своей сети и своевременно отрегулировать параметры сети для оптимальной производительности звонков.

Принцип теста скорости заключается в том, что SDK отправляет пакет пробных пакетов на узлы сервера, затем вычисляет качество возвращаемых пакетов и уведомляет результаты теста скорости через API обратного вызова, как показано ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e5d37ecebea511f085a55254007c27c5.png)

Преимущества тестов скорости перед звонком:

- Результаты теста скорости будут использоваться для оптимизации политики выбора сервера в SDK. Поэтому мы рекомендуем выполнить тест скорости перед первым звонком пользователя, чтобы помочь SDK выбрать оптимальный сервер.
- Если результаты теста крайне неудовлетворительны, вы можете предложить пользователю через заметный интерфейс выбрать более хорошую сеть.

### Выполнение теста скорости через startSpeedTest

Android

iOS

Windows

```
// Пример кода для запуска теста скорости сети. Требуются sdkAppId и UserSig (для получения метода см. Базовые функции).// Вот пример запуска теста скорости после входа в системуpublic void onLogin(String userId, String userSig) {  TRTCCloudDef.TRTCSpeedTestParams params = new TRTCCloudDef.TRTCSpeedTestParams();  params.sdkAppId = GenerateTestUserSig.SDKAPPID;  params.userId = mEtUserId.getText().toString();  params.userSig = GenerateTestUserSig.genTestUserSig(params.userId);  params.expectedUpBandwidth = Integer.parseInt(expectUpBandwidthStr);  params.expectedDownBandwidth = Integer.parseInt(expectDownBandwidthStr);    // sdkAppID - это реальный AppID приложения, полученный в консоли    trtcCloud.startSpeedTest(params);}// Прослушивайте результаты теста скорости, наследуйте TRTCCloudListener и реализуйте следующий методvoid onSpeedTestResult(TRTCCloudDef.TRTCSpeedTestResult result){    // Получите результаты теста скорости по завершении теста}Android
```

```
// Пример кода для запуска теста скорости сети. Требуются sdkAppId и UserSig (для получения метода см. Базовые функции).// Вот пример запуска теста скорости после входа в систему- (void)onLogin:(NSString *)userId userSig:(NSString *)userSid {    TRTCSpeedTestParams *params;    // sdkAppID - это реальный AppID приложения, полученный в консоли    params.sdkAppID = sdkAppId;    params.userID = userId;    params.userSig = userSig;    // Ожидаемая полоса пропускания восходящего канала (Единица: кбит/с. Диапазон значений: 10–5000. Значение 0 означает отсутствие теста)    params.expectedUpBandwidth = 5000;    // Ожидаемая полоса пропускания нисходящего канала (Единица: кбит/с. Диапазон значений: 10–5000. Значение 0 означает отсутствие теста)    params.expectedDownBandwidth = 5000;    [trtcCloud startSpeedTest:params];}- (void)onSpeedTestResult:(TRTCSpeedTestResult *)result {    // Получите результаты теста скорости по завершении теста}
```

```
// Пример кода для запуска теста скорости сети. Требуются sdkAppId и UserSig (для получения метода см. Базовые функции).// Вот пример запуска теста скорости после входа в системуvoid onLogin(const char* userId, const char* userSig){    TRTCSpeedTestParams params;    // sdkAppID - это реальный AppID приложения, полученный в консоли    params.sdkAppID = sdkAppId;    params.userId = userid;    param.userSig = userSig;    // Ожидаемая полоса пропускания восходящего канала (Единица: кбит/с. Диапазон значений: 10–5000. Значение 0 означает отсутствие теста)    param.expectedUpBandwidth = 5000;    // Ожидаемая полоса пропускания нисходящего канала (Единица: кбит/с. Диапазон значений: 10–5000. Значение 0 означает отсутствие теста)    param.expectedDownBandwidth = 5000;    trtcCloud->startSpeedTest(params);}// Прослушивайте результаты теста скоростиvoid TRTCCloudCallbackImpl::onSpeedTestResult(             const TRTCSpeedTestResult& result){    // Получите результаты теста скорости по завершении теста}
```

Результаты теста скорости ([TRTCSpeedTestResult](https://trtc.io/document/50768?platform=android&product=rtcengine&menulabel=core%20sdk#25124dd8b486afcaeaabe326bfe10288)) содержат следующие поля:

| Поле | Значение | Описание |
| --- | --- | --- |
| success | Успешность теста | Успешно ли пройден текущий тест. |
| errMsg | Сообщение об ошибке | Подробная информация об ошибке теста полосы пропускания. |
| ip | IP-адрес сервера | IP-адрес тестового сервера. |
| [quality](https://trtc.io/document/50768?platform=android&product=rtcengine&menulabel=core%20sdk#1796fe5bcef4aec6d520bdd8e530474b) | Оценка качества сети | Качество сети, рассчитанное алгоритмом оценки. Чем меньше потери пакетов и чем меньше RTT, тем выше оценка. |
| upLostRate | Коэффициент потери пакетов восходящего канала | Диапазон: 0–1,0. Например, значение 0,3 означает, что 3 из каждых 10 отправляемых на сервер пакетов могут быть потеряны при передаче. |
| downLostRate | Коэффициент потери пакетов нисходящего канала | Диапазон: 0–1,0. Например, значение 0,2 означает, что 2 из каждых 10 полученных с сервера пакетов могут быть потеряны при передаче. |
| rtt | Задержка сети | Время, необходимое для полного цикла туда и обратно между SDK и сервером. Чем меньше значение, тем лучше. Нормальное значение составляет от 10 мс до 100 мс. |
| availableUpBandwidth | Полоса пропускания восходящего канала | Предполагаемая полоса пропускания восходящего канала. Единица: кбит/с. Значение -1 означает недействительный результат. |
| availableDownBandwidth | Полоса пропускания нисходящего канала | Предполагаемая полоса пропускания нисходящего канала. Единица: кбит/с. Значение -1 означает недействительный результат. |

### Выполнение теста скорости через инструменты

Если вы не хотите выполнять тест скорости сети через вызовы API, Real-Time Communication Engine (RTC Engine) также предоставляет инструмент тестирования скорости сети на основе ПК, который позволяет вам быстро получить подробную информацию о качестве сети. В зависимости от вашей платформы вы можете выбрать подходящий инструмент из предложенных ниже вариантов для загрузки. Программа поддерживает два варианта теста: быстрое тестирование и непрерывное тестирование.

- [Mac](https://liteav.sdk.qcloud.com/customer/%E6%B5%8B%E8%AF%95/%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7/trtc-network-tools-latest.dmg)
- [Windows](https://liteav.sdk.qcloud.com/customer/%E6%B5%8B%E8%AF%95/%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7/trtc-network-tools_Setup_latest.exe)

| Метрика | Значение |
| --- | --- |
| WiFi Quality | Качество сигнала Wi-Fi |
| DNS RTT | Время разрешения доменного имени теста скорости Tencent Cloud |
| MTR | Инструмент тестирования сети, который может обнаружить коэффициент потери пакетов и задержку между клиентом и узлом RTC Engine, а также отобразить подробную информацию о каждом переходе в маршруте |
| UDP Loss | Коэффициент потери пакетов UDP между клиентом и узлом RTC Engine |
| UDP RTT | Задержка UDP между клиентом и узлом RTC Engine |
| Local RTT | Задержка между клиентом и локальным шлюзом |
| Upload | Предполагаемая полоса пропускания восходящего канала |
| Download | Предполагаемая полоса пропускания нисходящего канала |

> **Примечание:** Не выполняйте тесты скорости во время видеозвонков, так как это может снизить качество звонка. Выполнение теста скорости потребляет небольшой объём трафика, что может привести к минимальным (практически пренебрежимо малым) дополнительным сборам за трафик.

## Обнаружение качества сети во время звонков

Чтобы помочь пользователям лучше осознавать потенциальные колебания сети во время звонков, рекомендуется добавить соответствующие оповещения в интерфейс звонка. Это особенно важно при плохих условиях сети, так как эти оповещения информируют пользователей о проблеме, позволяя им своевременно внести коррективы для улучшения качества сети.

### Прослушивание качества локальной сети через onNetworkQuality

Событие обратного вызова onNetworkQuality сообщает о текущем качестве сети каждые 2 секунды. Оно включает два параметра: localQuality и remoteQuality.

- localQuality: представляет ваше текущее качество сети. Качество разделено на 6 уровней: Excellent, Good, Poor, Bad, VeryBad и Down.
- remoteQuality: представляет качество сети удалённых пользователей. Это массив, где каждый элемент представляет качество сети удалённого пользователя.

| Качество | Имя | Описание |
| --- | --- | --- |
| 0 | Unknown | Не определено. |
| 1 | Excellent | Текущая сеть отличная. |
| 2 | Good | Текущая сеть хорошая. |
| 3 | Poor | Текущая сеть средняя. |
| 4 | Bad | Текущая сеть плохая, могут возникать явные зависания и задержки при звонках. |
| 5 | VeryBad | Текущая сеть очень плохая. RTC Engine может только поддерживать соединение, но не может гарантировать качество связи. |
| 6 | Down | Текущая сеть не удовлетворяет минимальным требованиям RTC Engine, и нормальные аудио и видеозвонки невозможны. |

Прослушивайте onNetworkQuality и предоставляйте соответствующие подсказки в интерфейсе.

Android

iOS&Mac

Windows

```
// Прослушивайте обратный вызов onNetworkQuality, чтобы оставаться в курсе изменений текущего статуса сети@Overridepublic void onNetworkQuality(TRTCCloudDef.TRTCQuality localQuality,                             ArrayList<trtcclouddef.trtcquality> remoteQuality){    // Получить качество вашей локальной сети    switch(localQuality) {        case TRTCQuality_Unknown:            Log.d(TAG, "SDK ещё не определил текущее качество сети.");            break;        case TRTCQuality_Excellent:            Log.d(TAG, "Текущая сеть очень хорошая.");            break;        case TRTCQuality_Good:            Log.d(TAG, "Текущая сеть хорошая.");            break;        case TRTCQuality_Poor:            Log.d(TAG, "Текущее качество сети едва соответствует требованиям.");            break;        case TRTCQuality_Bad:            Log.d(TAG, "Текущая сеть плохая, могут быть значительные зависания и задержки при звонках.");            break;        case TRTCQuality_VeryBad:            Log.d(TAG, "Текущая сеть очень плохая, качество связи не может быть гарантировано");            break;        case TRTCQuality_Down:            Log.d(TAG, "Текущая сеть не соответствует минимальным требованиям.");            break;        default:            break;    }    // Получить качество сети удалённых пользователей    for (TRTCCloudDef.TRTCQuality info : arrayList) {        Log.d(TAG, "удалённый пользователь : = " + info.userId + ", quality = " + info.quality);    }}
```

```
// Прослушивайте обратный вызов onNetworkQuality, чтобы оставаться в курсе изменений текущего статуса сети- (void)onNetworkQuality:(TRTCQualityInfo *)localQuality remoteQuality:(NSArray<trtcqualityinfo *=""> *)remoteQuality {    // Получить качество вашей локальной сети    switch(localQuality.quality) {        case TRTCQuality_Unknown:            NSLog(@"SDK ещё не определил текущее качество сети.");            break;        case TRTCQuality_Excellent:            NSLog(@"Текущая сеть очень хорошая.");            break;        case TRTCQuality_Good:            NSLog(@"Текущая сеть хорошая.");            break;        case TRTCQuality_Poor:            NSLog(@"Текущее качество сети едва соответствует требованиям.");            break;        case TRTCQuality_Bad:            NSLog(@"Текущая сеть плохая, могут быть значительные зависания и задержки при звонках.");            break;        case TRTCQuality_VeryBad:           NSLog(@"Текущая сеть очень плохая, качество связи не может быть гарантировано");            break;        case TRTCQuality_Down:            NSLog(@"Текущая сеть не соответствует минимальным требованиям.");            break;        default:            break;    }    // Получить качество сети удалённых пользователей    for (TRTCQualityInfo *info in arrayList) {        NSLog(@"удалённый пользователь : = %@, quality = %@", info.userId, @(info.quality));    }}iOSMac
```

```
// Прослушивайте обратный вызов onNetworkQuality, чтобы оставаться в курсе изменений текущего статуса сетиvoid onNetworkQuality(liteav::TRTCQualityInfo local_quality,    liteav::TRTCQualityInfo* remote_quality, uint32_t remote_quality_count) {    // Получить качество вашей локальной сети    switch (local_quality.quality) {    case TRTCQuality_Unknown:        printf("SDK ещё не определил текущее качество сети.");        break;    case TRTCQuality_Excellent:        printf("Текущая сеть очень хорошая.");        break;    case TRTCQuality_Good:        printf("Текущая сеть хорошая.");        break;    case TRTCQuality_Poor:        printf("Текущее качество сети едва соответствует требованиям.");        break;    case TRTCQuality_Bad:        printf("Текущая сеть плохая, могут быть значительные зависания и задержки при звонках.");        break;    case TRTCQuality_Vbad:        printf("Текущая сеть очень плохая, качество связи не может быть гарантировано");        break;    case TRTCQuality_Down:        printf("Текущая сеть не соответствует минимальным требованиям.");        break;    default:        break;    }    // Получить качество сети удалённых пользователей    for (int i = 0; i < remote_quality_count; ++i) {        printf("удалённый пользователь : = %s, quality = %d", remote_quality[i].userId, remote_quality[i].quality);    }}
```

### Прослушивание полного качества сети через onStatistics

Событие обратного вызова статистики [onStatistics](https://trtc.io/document/50763?product=rtcengine&menulabel=core%20sdk&platform=android#faca91305f246db336cb6c56f7bfbf25) вызывается каждые 2 секунды для уведомления о статистике профессиональных технических метрик, связанных с производительностью аудио, видео и сети в SDK. Метрики перечислены в [TRTCStatistics](https://trtc.io/document/50764?product=rtcengine&menulabel=core%20sdk&platform=android):

- Статистика видео: разрешение видео, частота кадров (FPS), битрейт и другая информация.
- Статистика аудио: частота дискретизации аудио (samplerate), количество аудиоканалов (channel), битрейт и другая информация.
- Статистика сети: длительность сетевого соединения (rtt), коэффициент потери пакетов (loss), поднаправленный трафик (sentBytes), полученный трафик (receivedBytes) и другая информация для полного цикла между SDK и облаком (SDK > Cloud > SDK).

| Тип перечисления | Описание |
| --- | --- |
| appCpu | Использование ЦПУ текущего приложения. Единица: %. Android 8.0 и более поздние версии не поддерживаются. |
| downLoss | Коэффициент потери пакетов нисходящего канала от облака к SDK. Единица: %. Чем меньше значение, тем лучше. Если downLoss равен 0%, качество сети нисходящего канала очень хорошее, и полученные данные из облака практически не теряются. Если downLoss равен 30%, 30% пакетов аудио и видео данных, передаваемых из облака в SDK, будут потеряны в канале передачи. |
| gatewayRtt | Задержка туда и обратно от SDK к локальному маршрутизатору. Единица: мс. Это значение представляет общее время, необходимое сетевому пакету для путешествия от SDK к локальному шлюзу маршрутизатора и обратно, то есть полный цикл "SDK > шлюз > SDK." Чем меньше значение, тем лучше. Значение gatewayRtt ниже 50 мс указывает на низкую задержку для аудио и видеозвонков, тогда как значение выше 200 мс указывает на высокую задержку для аудио и видеозвонков. Когда тип сети — сотовая сеть, значение недействительно. |
| localArray | Статистика локального аудио и видео. Поскольку локально могут быть доступны три потока аудио и видео (то есть основной поток высокого качества, вторичный поток низкого разрешения и подпоток), статистика локального аудио и видео предоставляется в виде массива. |
| receiveBytes | Общее количество полученных байтов (включая данные сигнализации и аудио и видео данные). Единица: байт. |
| remoteArray | Статистика удалённого аудио и видео. Поскольку одновременно могут быть несколько удалённых пользователей, и каждый из них может иметь несколько потоков аудио и видео (то есть основной поток высокого качества, вторичный поток низкого разрешения и подпоток), статистика удалённого аудио и видео предоставляется в виде массива. |
| rtt | Задержка туда и обратно от SDK к облаку. Единица: мс. Это значение представляет общее время, необходимое сетевому пакету для путешествия от SDK к облаку и обратно, то есть полный цикл "SDK > облако > SDK." Чем меньше значение, тем лучше. Значение rtt ниже 50 мс указывает на низкую задержку для аудио и видеозвонков, тогда как значение выше 200 мс указывает на высокую задержку для аудио и видеозвонков. **Примечание:** rtt представляет общую длительность на канале "SDK > облако > SDK." Поэтому различать upRtt и downRtt не требуется. |
| sendBytes | Общее количество отправленных байтов (включая данные сигнализации и аудио и видео данные). Единица: байт. |
| systemCpu | Использование ЦПУ текущей системы. Единица: %. Android 8.0 и более поздние версии не поддерживаются. |
| upLoss | Коэффициент потери пакетов восходящего канала от SDK к облаку. Единица: %. Чем меньше значение, тем лучше. Если upLoss равен 0%, качество сети восходящего канала очень хорошее, и отправленные в облако данные практически не теряются. Если upLoss равен 30%, 30% пакетов аудио и видео данных, отправляемых из SDK в облако, будут потеряны в канале передачи. |

Android

iOS&Mac

Windows

```
@Overridepublic void onStatistics(TRTCStatistics statistics) {    super.onStatistics(statistics);    // appCpu - это использование ЦПУ приложением    Log.d(TAG, "appCpu:" + statistics.appCpu);    // systemCpu - это использование ЦПУ системой    Log.d(TAG, "systemCpu:" + statistics.systemCpu);    // rtt - это задержка туда и обратно от SDK к облаку    Log.d(TAG, "rtt:" + statistics.rtt);    // upLoss - это коэффициент потери пакетов восходящего канала    Log.d(TAG, "upLoss:" + statistics.upLoss);    // downLoss - это коэффициент потери пакетов нисходящего канала    Log.d(TAG, "downLoss:" + statistics.downLoss);    // gatewayRtt - это задержка туда и обратно от шлюза к облаку    Log.d(TAG, "gatewayRtt:" + statistics.gatewayRtt);    // sendBytes - это количество отправленных байтов    Log.d(TAG, "sendBytes:" + statistics.sendBytes);    // receiveBytes - это количество полученных байтов    Log.d(TAG, "receiveBytes:" + statistics.receiveBytes);    if(statistics.localArray != null) {        for (int i = 0; i < statistics.localArray.size(); i++) {            // Ширина локального видео            Log.d(TAG, "localStatistics width:" + statistics.localArray.get(i).width);            // Высота локального видео            Log.d(TAG, "localStatistics height:" + statistics.localArray.get(i).height);            // Частота кадров локального видео            Log.d(TAG, "localStatistics frameRate:" + statistics.localArray.get(i).frameRate);            // Битрейт локального видео            Log.d(TAG, "localStatistics videoBitrate:" + statistics.localArray.get(i).videoBitrate);            // Битрейт локального аудио            Log.d(TAG, "localStatistics audioBitrate:" + statistics.localArray.get(i).audioBitrate);            // Статус захвата локального аудиоустройства (используется для контроля состояния звуковых периферийных устройств). 0: устройство захвата в нормальном состоянии; 1: обнаружено длительное молчание; 2: обнаружено обрезание аудио; 3: обнаружено необычное прерывание звука.            Log.d(TAG, "localStatistics audioCaptureState:" + statistics.localArray.get(i).audioCaptureState);            // Частота дискретизации локального аудио            Log.d(TAG, "localStatistics audioSampleRate:" + statistics.localArray.get(i).audioSampleRate);            // Тип локального потока            Log.d(TAG, "localStatistics streamType:" + statistics.localArray.get(i).streamType);        }    }    if(statistics.remoteArray != null) {        for (int i = 0; i < statistics.remoteArray.size(); i++) {            // userid удалённого пользователя            Log.d(TAG, "remoteStatistics userId:" + statistics.remoteArray.get(i).userId);            // Тип потока удалённого пользователя            Log.d(TAG, "remoteStatistics streamType:" + statistics.remoteArray.get(i).streamType);            // Ширина удалённого видео            Log.d(TAG, "remoteStatistics width:" + statistics.remoteArray.get(i).width);            // Высота удалённого видео            Log.d(TAG, "remoteStatistics height:" + statistics.remoteArray.get(i).height);            // Частота кадров удалённого видео            Log.d(TAG, "remoteStatistics frameRate:" + statistics.remoteArray.get(i).frameRate);            // Битрейт удалённого видео            Log.d(TAG, "remoteStatistics videoBitrate:" + statistics.remoteArray.get(i).videoBitrate);            // Коэффициент зависания удалённого видео. Единица: %. Коэффициент зависания видео (videoBlockRate) = совокупная длительность зависания воспроизведения видео (videoTotalBlockTime) / общая длительность воспроизведения видео.            Log.d(TAG, "remoteStatistics videoBlockRate:" + statistics.remoteArray.get(i).videoBlockRate);            // Совокупная длительность зависания при воспроизведении видео. Единица: мс.            Log.d(TAG, "remoteStatistics videoTotalBlockTime:" + statistics.remoteArray.get(i).videoTotalBlockTime);            // Общий коэффициент потери пакетов видеопотока            // videoPacketLoss представляет коэффициент потери пакетов, рассчитанный на стороне аудитории после прохождения видеопотока через полный канал передачи "anchor > cloud > audience."            // Чем меньше значение videoPacketLoss, тем лучше. Коэффициент потери пакетов 0 означает, что все данные видеопотока полностью достигли аудитории.            // Если downLoss == 0, но videoPacketLoss != 0, это означает, что видеопоток не испытал потери пакетов на канале облако

---
*Источник (EN): [network-quality-monitoring.md](./network-quality-monitoring.md)*

# Обнаружение качества сети

Обычным пользователям сложно оценить качество сети. Путем измерения скорости перед видеозвонком и получения обратной связи о качестве сети во время звонка пользователи могут более интуитивно оценить качество сети.

В этом документе описано, как обнаружить качество сети.

## Обнаружение качества сети перед звонком

> **Примечание:** Чтобы обеспечить качество звонка, не запускайте тест во время видеозвонка. Тестирование скорости потребляет трафик и, следовательно, может привести к небольшой плате за трафик (почти незначительной).

### Как работает тестирование скорости

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/fca26afc699911efb0e2525400a9236a.png)

- Во время тестирования скорости SDK отправляет пакет зондирующих пакетов на узел сервера, измеряет качество возвращаемых пакетов и возвращает результат тестирования через API обратного вызова.
- Результат тестирования можно использовать для оптимизации политики выбора сервера SDK, поэтому рекомендуется запустить тест перед первым звонком, что поможет SDK выбрать оптимальный сервер. Если результат неудовлетворительный, вы можете показать сообщение в пользовательском интерфейсе, предлагающее пользователям переключиться на лучшую сеть.
- Результат тестирования ([TRTCSpeedTestResult](https://liteav.sdk.qcloud.com/doc/api/en/group__TRTCCloudDef__ios.html#interfaceTRTCSpeedTestResult)) включает следующие параметры:

| Параметр | Тип | Описание |
| --- | --- | --- |
| success | Результат успеха | Успешно ли выполнено тестирование. |
| errMsg | Сообщение об ошибке | Сообщение об ошибке теста пропускной способности. |
| ip | Адрес сервера | IP-адрес тестового сервера |
| [quality](https://liteav.sdk.qcloud.com/doc/api/en/group__TRTCCloudDef__ios.html#ga25f9ccb045890cb18a5f647ef3c1f974) | Оценка качества сети | Качество сети, измеренное SDK. Более низкая потеря пакетов и более короткое RTT приводят к более высокой оценке качества сети. |
| upLostRate | Коэффициент потери пакетов восходящего потока | Диапазон значений: 0-1.0. `0.3` означает, что из каждых 10 пакетов данных, отправленных на сервер, 3 могут быть потеряны. |
| downLostRate | Коэффициент потери пакетов нисходящего потока | Диапазон значений: 0-1.0. `0.2` означает, что из каждых 10 пакетов данных, полученных с сервера, 2 могут быть потеряны. |
| rtt | Задержка | Время, необходимое для передачи данных от SDK на сервер и обратно. Чем короче RTT, тем лучше. Нормальный диапазон RTT составляет 10-100 мс. |
| availableUpBandwidth | Пропускная способность восходящего потока | Расчетная пропускная способность восходящего потока в Кбит/с. -1 указывает на недействительное значение. |
| availableDownBandwidth | Пропускная способность нисходящего потока | Расчетная пропускная способность нисходящего потока в Кбит/с. -1 указывает на недействительное значение. |

### Как протестировать скорость

- **С использованием API вызова**

Функция тестирования скорости может быть запущена через функцию `startSpeedTest` из `TRTCCloud`. Результат теста скорости будет вызван через функцию обратного вызова.

Objective-C

Java

C++

C#

```
// Пример кода для начала тестирования скорости. Требуются `sdkAppId` и `UserSig`. О том, как их получить, см. Основные функции.// Пример ниже запускается после входа.- (void)onLogin:(NSString *)userId userSig:(NSString *)userSid {    TRTCSpeedTestParams *params;    // `sdkAppID` — это фактический ID приложения, полученный из консоли.    params.sdkAppID = sdkAppId;    params.userID = userId;    params.userSig = userSig;    // Ожидаемая пропускная способность восходящего потока в Кбит/с. Диапазон значений: 10–5000. 0 означает не тестировать    params.expectedUpBandwidth = 5000;    // Ожидаемая пропускная способность нисходящего потока в Кбит/с. Диапазон значений: 10–5000. 0 означает не тестировать    params.expectedDownBandwidth = 5000;    [trtcCloud startSpeedTest:params];}- (void)onSpeedTestResult:(TRTCSpeedTestResult *)result {    // Результат теста скорости будет вызван после завершения теста}
```

```
// Пример кода для начала тестирования скорости. Требуются `sdkAppId` и `UserSig`. О том, как их получить, см. Основные функции.// Пример ниже запускается после входа.public void onLogin(String userId, String userSig) {  TRTCCloudDef.TRTCSpeedTestParams params = new TRTCCloudDef.TRTCSpeedTestParams();  params.sdkAppId = GenerateTestUserSig.SDKAPPID;  params.userId = mEtUserId.getText().toString();  params.userSig = GenerateTestUserSig.genTestUserSig(params.userId);  params.expectedUpBandwidth = Integer.parseInt(expectUpBandwidthStr);  params.expectedDownBandwidth = Integer.parseInt(expectDownBandwidthStr);    // `sdkAppID` — это фактический ID приложения, полученный из консоли.    trtcCloud.startSpeedTest(params);}// Прослушивание результата теста. Наследуйте `TRTCCloudListener` и реализуйте следующий метод.void onSpeedTestResult(TRTCCloudDef.TRTCSpeedTestResult result){    // Результат теста скорости будет вызван после завершения теста}
```

```
// Пример кода для начала тестирования скорости. Требуются `sdkAppId` и `UserSig`. О том, как их получить, см. Основные функции.// Пример ниже запускается после входа.void onLogin(const char* userId, const char* userSig){    TRTCSpeedTestParams params;    // `sdkAppID` — это фактический ID приложения, полученный из консоли.    params.sdkAppID = sdkAppId;    params.userId = userid;    param.userSig = userSig;    // Ожидаемая пропускная способность восходящего потока в Кбит/с. Диапазон значений: 10–5000. 0 означает не тестировать    param.expectedUpBandwidth = 5000;    // Ожидаемая пропускная способность нисходящего потока в Кбит/с. Диапазон значений: 10–5000. 0 означает не тестировать    param.expectedDownBandwidth = 5000;    trtcCloud->startSpeedTest(params);}// Прослушивание результата тестирования void TRTCCloudCallbackImpl::onSpeedTestResult(             const TRTCSpeedTestResult& result){    // Результат теста скорости будет вызван после завершения теста}
```

```
// Пример кода для начала тестирования скорости. Требуются `sdkAppId` и `UserSig`. О том, как их получить, см. Основные функции.// Пример ниже запускается после входа.private void onLogin(string userId, string userSig){    TRTCSpeedTestParams params;    // `sdkAppID` — это фактический ID приложения, полученный из консоли.    params.sdkAppID = sdkAppId;    params.userId = userid;    param.userSig = userSig;    // Ожидаемая пропускная способность восходящего потока в Кбит/с. Диапазон значений: 10–5000. 0 означает не тестировать    param.expectedUpBandwidth = 5000;    // Ожидаемая пропускная способность нисходящего потока в Кбит/с. Диапазон значений: 10–5000. 0 означает не тестировать    param.expectedDownBandwidth = 5000;    mTRTCCloud.startSpeedTest(params);}// Прослушивание результата тестирования public void onSpeedTestResult(TRTCSpeedTestResult result){    // Результат теста скорости будет вызван после завершения теста}
```

- **Инструмент тестирования скорости**

Если вы не хотите вызывать интерфейс для измерения скорости сети, вы можете использовать инструмент тестирования скорости сети для ПК, предоставленный TRTC, чтобы быстро получить детали качества сети. Выберите следующую программу в соответствии с вашей платформой для загрузки.

Программа предоставляет два варианта тестирования: быстрое тестирование и непрерывное тестирование.

[Mac](https://liteav.sdk.qcloud.com/customer/%E6%B5%8B%E8%AF%95/%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7/trtc-network-tools-latest.dmg) | [Windows](https://liteav.sdk.qcloud.com/customer/%E6%B5%8B%E8%AF%95/%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7/trtc-network-tools_Setup_latest.exe)

| Метрика | Описание |
| --- | --- |
| WiFi Quality | Качество приема сигнала Wi-Fi |
| DNS RTT | Время прохождения в оба конца (RTT) для тестового домена Tencent Cloud DNS |
| MTR | MTR — это инструмент для тестирования скорости сети, который может определить коэффициент потери пакетов и задержку между клиентом и узлом TRTC и отобразить детали каждого перехода маршрута |
| UDP Loss | Коэффициент потери пакетов UDP между клиентом и узлом TRTC |
| UDP RTT | Задержка UDP между клиентом и узлом TRTC |
| Local RTT | Задержка между клиентом и локальным шлюзом |
| Upload | Расчетная пропускная способность восходящего потока |
| Download | Расчетная пропускная способность нисходящего потока |

## Обнаружение качества сети во время звонка

TRTC предоставляет обратный вызов `onNetworkQuality` для отправки отчета о текущем качестве сети один раз в две секунды. Он содержит два параметра: `localQuality` и `remoteQuality`.

- **localQuality** указывает на ваше текущее качество сети, которое имеет шесть уровней: Excellent, Good, Poor, Bad, VeryBad и Down.
- **remoteQuality** — это массив, указывающий на качество сети удаленных пользователей. В этом массиве каждый элемент представляет качество сети удаленного пользователя.

| Качество | Название | Описание |
| --- | --- | --- |
| 0 | Unknown | Неизвестно |
| 1 | Excellent | Текущая сеть отличная. |
| 2 | Good | Текущая сеть хорошая. |
| 3 | Poor | Текущая сеть в порядке. |
| 4 | Bad | Текущая сеть плохая, могут наблюдаться явные зависания и задержки. |
| 5 | VeryBad | Текущая сеть очень плохая, TRTC может только поддерживать соединение, но не может гарантировать качество связи. |
| 6 | Down | Текущая сеть не соответствует минимальным требованиям TRTC, невозможно провести нормальный аудио/видеозвонок. |

Вам просто нужно прослушать `onNetworkQuality` из TRTC и отобразить соответствующее сообщение в пользовательском интерфейсе.

Android

iOS & Mac

Windows

```
// Прослушивание обратного вызова `onNetworkQuality` для получения изменения текущих условий сети@Overridepublic void onNetworkQuality(TRTCCloudDef.TRTCQuality localQuality,                             ArrayList<TRTCCloudDef.TRTCQuality> remoteQuality){    // Получить качество локальной сети    switch(localQuality) {        case TRTCQuality_Unknown:            Log.d(TAG, "SDK еще не определил текущее качество сети.");            break;        case TRTCQuality_Excellent:            Log.d(TAG, "Текущая сеть очень хорошая.");            break;        case TRTCQuality_Good:            Log.d(TAG, "Текущая сеть хорошая.");            break;        case TRTCQuality_Poor:            Log.d(TAG, "Текущее качество сети едва соответствует требованиям.");            break;        case TRTCQuality_Bad:            Log.d(TAG, "Текущая сеть плохая, могут наблюдаться значительные зависания и задержки вызовов.");            break;        case TRTCQuality_VeryBad:            Log.d(TAG, "Текущая сеть очень плохая, качество связи не может быть гарантировано");            break;        case TRTCQuality_Down:            Log.d(TAG, "Текущая сеть не соответствует минимальным требованиям.");            break;        default:            break;    }    // Получить качество сети удаленных пользователей    for (TRTCCloudDef.TRTCQuality info : arrayList) {        Log.d(TAG, "удаленный пользователь : = " + info.userId + ", качество = " + info.quality);    }}
```

```
// Прослушивание обратного вызова `onNetworkQuality` для получения изменения текущих условий сети- (void)onNetworkQuality:(TRTCQualityInfo *)localQuality remoteQuality:(NSArray<TRTCQualityInfo *> *)remoteQuality {    // Получить качество локальной сети    switch(localQuality.quality) {        case TRTCQuality_Unknown:            NSLog(@"SDK еще не определил текущее качество сети.");            break;        case TRTCQuality_Excellent:            NSLog(@"Текущая сеть очень хорошая.");            break;        case TRTCQuality_Good:            NSLog(@"Текущая сеть хорошая.");            break;        case TRTCQuality_Poor:            NSLog(@"Текущее качество сети едва соответствует требованиям.");            break;        case TRTCQuality_Bad:            NSLog(@"Текущая сеть плохая, могут наблюдаться значительные зависания и задержки вызовов.");            break;        case TRTCQuality_VeryBad:           NSLog(@"Текущая сеть очень плохая, качество связи не может быть гарантировано");            break;        case TRTCQuality_Down:            NSLog(@"Текущая сеть не соответствует минимальным требованиям.");            break;        default:            break;    }    // Получить качество сети удаленных пользователей    for (TRTCQualityInfo *info in arrayList) {        NSLog(@"удаленный пользователь : = %@, качество = %@", info.userId, @(info.quality));    }}
```

```
// Прослушивание обратного вызова `onNetworkQuality` для получения изменения текущих условий сетиvoid onNetworkQuality(liteav::TRTCQualityInfo local_quality,    liteav::TRTCQualityInfo* remote_quality, uint32_t remote_quality_count) {    // Получить качество локальной сети    switch (local_quality.quality) {    case TRTCQuality_Unknown:        printf("SDK еще не определил текущее качество сети.");        break;    case TRTCQuality_Excellent:        printf("Текущая сеть очень хорошая.");        break;    case TRTCQuality_Good:        printf("Текущая сеть хорошая.");        break;    case TRTCQuality_Poor:        printf("Текущее качество сети едва соответствует требованиям.");        break;    case TRTCQuality_Bad:        printf("Текущая сеть плохая, могут наблюдаться значительные зависания и задержки вызовов.");        break;    case TRTCQuality_Vbad:        printf("Текущая сеть очень плохая, качество связи не может быть гарантировано");        break;    case TRTCQuality_Down:        printf("Текущая сеть не соответствует минимальным требованиям.");        break;    default:        break;    }    // Получить качество сети удаленных пользователей    for (int i = 0; i < remote_quality_count; ++i) {        printf("удаленный пользователь : = %s, качество = %d", remote_quality[i].userId, remote_quality[i].quality);    }}
```

---
*Источник: [https://trtc.io/document/48272](https://trtc.io/document/48272)*

---
*Источник (EN): [detect-network-quality.md](./detect-network-quality.md)*

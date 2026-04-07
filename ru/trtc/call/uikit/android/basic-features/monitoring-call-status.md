# Мониторинг статуса звонка

В этой статье объясняется использование обратного вызова статуса звонка TUICallKit. Вы можете отслеживать события звонков (например, начало, окончание, присоединение и отключение участников) через регистрацию обратного вызова звонка.

> **Примечание:** На платформе Android при установке TUICallObserver для прослушивания обратных вызовов убедитесь, что класс, содержащий обратный вызов, не будет уничтожен. Например, не рекомендуется добавлять наблюдателя в LoginActivity, так как при уничтожении LoginActivity обратный вызов также будет уничтожен; рекомендуется использовать класс Application приложения или основной интерфейс приложения.

## Обратный вызов статуса звонка

Обнаруживайте ключевые изменения состояния на протяжении жизненного цикла звонка.

Kotlin

Swift

Dart

```
import com.tencent.qcloud.tuikit.TUICommonDefineimport com.tencent.qcloud.tuikit.tuicallengine.TUICallDefineimport com.tencent.qcloud.tuikit.tuicallengine.TUICallEngineimport com.tencent.qcloud.tuikit.tuicallengine.TUICallObserverprivate val observer: TUICallObserver = object : TUICallObserver() {    override fun onCallReceived(callId: String?, callerId: String?, calleeIdList: MutableList<String>?, mediaType: TUICallDefine.MediaType?, info: TUICallDefine.CallObserverExtraInfo?) {    }        override fun onCallBegin(roomId: TUICommonDefine.RoomId?, callMediaType: TUICallDefine.MediaType?, callRole: TUICallDefine.Role?) {    }        override fun onCallEnd(roomId: TUICommonDefine.RoomId?, callMediaType: TUICallDefine.MediaType?, callRole: TUICallDefine.Role?, totalTime: Long) {    }        override fun onCallNotConnected(callId: String?, mediaType: TUICallDefine.MediaType?, reason: TUICallDefine.CallEndReason?, userId: String?, info: TUICallDefine.CallObserverExtraInfo?) {    }    …}private fun initData() {    TUICallEngine.createInstance(context).addObserver(observer)}
```

```
import TUICallEngineTUICallEngine.createInstance().addObserver(self)func onCallReceived(_ callId: String, callerId: String, calleeIdList: [String], mediaType: TUICallMediaType, info: TUICallObserverExtraInfo) {}func onCallBegin(callId: String, mediaType: TUICallMediaType, info: TUICallObserverExtraInfo) {}func onCallEnd(callId: String, mediaType: TUICallMediaType, reason: TUICallEndReason, userId: String, totalTime: Float, info: TUICallObserverExtraInfo) {}func onCallNotConnected(callId: String, mediaType: TUICallMediaType, reason: TUICallEndReason, userId: String, info: TUICallObserverExtraInfo) {}
```

```
import 'package:tencent_calls_engine/tencent_calls_engine.dart';TUICallObserver observer = TUICallObserver(    onCallReceived: (String callId, String callerId, List<String> calleeIdList, TUICallMediaType mediaType, CallObserverExtraInfo info) {    }, onCallBegin: (String callId, TUICallMediaType mediaType, CallObserverExtraInfo info) {    }, onCallEnd: (String callId, TUICallMediaType mediaType, CallEndReason reason, String userId, double totalTime, CallObserverExtraInfo info) {    }, onCallNotConnected: (String callId, TUICallMediaType mediaType, CallEndReason reason, String userId, CallObserverExtraInfo info) {    }    …)void addObserver() {    TUICallEngine.instance.addObserver(observer);}
```

## Обратный вызов обновления участников звонка

Отслеживайте отдельные действия или изменения статуса участников звонка, в основном используется для реального отображения динамики участников (например, присоединение, отключение, отклонение).

Kotlin

Swift

Dart

```
import com.tencent.qcloud.tuikit.TUICommonDefineimport com.tencent.qcloud.tuikit.tuicallengine.TUICallDefineimport com.tencent.qcloud.tuikit.tuicallengine.TUICallEngineimport com.tencent.qcloud.tuikit.tuicallengine.TUICallObserverprivate val observer: TUICallObserver = object : TUICallObserver() {    override fun onUserJoin(userId: String?) {    }        override fun onUserLeave(userId: String?) {    }        override fun onUserInviting(userId: String?) {    }        override fun onUserReject(userId: String?) {    }    …}private fun initData() {    TUICallEngine.createInstance(context).addObserver(observer)}
```

```
import TUICallEngineTUICallEngine.createInstance().addObserver(self)func onUserJoin(userId: String) {}func onUserLeave(userId: String) {}func onUserInviting(userId: String) {}func onUserReject(userId: String) {}…
```

```
import 'package:tencent_calls_engine/tencent_calls_engine.dart';TUICallObserver observer = TUICallObserver(    onUserJoin: (String userId) {    }, onUserLeave: (String userId) {    }, onUserInviting: (String userId) {    }, onUserReject: (String userId) {    },    …)void addObserver() {    TUICallEngine.instance.addObserver(observer);}
```


---
*Источник: [https://trtc.io/document/59851](https://trtc.io/document/59851)*

---
*Источник (EN): [monitoring-call-status.md](./monitoring-call-status.md)*

# Пользовательский вид сетки мест

Этот документ в основном описывает, как настроить `SeatGridView`.

## Предварительные условия

Перед использованием `SeatGridView` необходимо [интегрировать и выполнить вход](https://www.tencentcloud.com/document/product/647/67506#) в SeatGridView, чтобы обеспечить надлежащую работу последующих функций.

## Руководство по использованию

### Шаг 1: Добавление SeatGridView в представление

Сначала необходимо импортировать модуль `SeatGridView`, затем создать объект SeatGridView и добавить его в ваше представление.

iOS

Android

```
import UIKitimport RTCRoomEngineimport SeatGridView class CustomizeSeatViewController: UIViewController {    private let seatGridView: SeatGridView = {         let view = SeatGridView()      self.seatGridView.setSeatViewDelegate(self)      return view    }        override func viewDidLoad() {        super.viewDidLoad()        self.seatGridView.setSeatViewDelegate(self)        // Add seatGridView to the view and set layout constraints    }}
```

```
import com.trtc.uikit.livekit.seatGridView.SeatGridView;public class CustomizeSeatViewActivity extends AppCompatActivity {    @Override    protected void onCreate(@Nullable Bundle savedInstanceState) {        super.onCreate(savedInstanceState);        SeatGridView seatGridView = new SeatGridView(this);        addContentView(seatGridView,                new ViewGroup.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));    }}
```

### Шаг 2: Настройка места

iOS

Android

Если вы хотите настроить представление места, вам необходимо реализовать делегат `SeatGridView` — `SGSeatViewDelegate`.

```
SGSeatViewDelegate
```

Ниже приведен пример использования:

```
SGSeatViewDelegate
```

Если вы хотите настроить представление места, вам необходимо реализовать адаптер `SeatGridView` — `SeatViewAdapter`.

```
public interface SeatViewAdapter {    View createSeatView(SeatGridView seatGridView, TUIRoomDefine.SeatInfo seatInfo);    void updateSeatView(SeatGridView seatGridView, TUIRoomDefine.SeatInfo seatInfo, View seatView);    void updateUserVolume(SeatGridView seatGridView, int volume, View seatView);}
```

Ниже приведен пример использования:

```
seatGridView.setSeatViewAdapter(new VoiceRoomDefine.SeatViewAdapter() {    @Override    View createSeatView(SeatGridView seatGridView, TUIRoomDefine.SeatInfo seatInfo) {        TextView seatUserName = new TextView(CustomizeSeatViewActivity.this);        seatUserName.setText(seatInfo.userName);        return seatUserName;    }        @Override    void updateSeatView(SeatGridView seatGridView, TUIRoomDefine.SeatInfo seatInfo, View seatView) {    }        @Override    void updateUserVolume(SeatGridView seatGridView, int volume, View seatView) {    }});
```


---
*Источник: [https://trtc.io/document/67499](https://trtc.io/document/67499)*

---
*Источник (EN): [custom-seat-view.md](./custom-seat-view.md)*

# Список трансляций в реальном времени

## Обзор функций

Этот документ содержит подробное описание **страницы списка трансляций в реальном времени** в TUILiveKit. Вы можете напрямую интегрировать нашу готовую страницу списка трансляций в ваш существующий проект или глубоко настроить стиль страницы, макет и функции в соответствии с вашими конкретными потребностями.

- **Двухколонный водопадный макет**: представление по умолчанию, одновременно отображающее предпросмотры 2 трансляционных комнат.
- **Одноколонный водопадный макет**: представление по умолчанию, одновременно отображающее предпросмотр 1 трансляционной комнаты.

| **Двухколонный водопадный макет** | **Одноколонный водопадный макет** |
| --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/5bdd6221991f11f0a3b8525400e889b2.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/61304d3a991f11f0961e52540099c741.png) |

> **Примечание:** При предпросмотре экранов трансляционной комнаты длительность предпросмотра учитывается в длительности аудио/видео зрителя. Для получения подробной информации о выставлении счетов см. [Ценообразование](https://www.tencentcloud.com/document/product/647/66078).

## Быстрый старт

### Шаг 1. Активация сервиса

Обратитесь к документу [Активация сервиса](https://www.tencentcloud.com/document/product/647/60033), чтобы включить бесплатный пробный период или официальный пакет.

### Шаг 2. Интеграция кода

Обратитесь к руководству [Подготовка](https://www.tencentcloud.com/document/product/647/72217), чтобы интегрировать TUILiveKit SDK.

### Шаг 3. Добавление страницы списка трансляций

Компонент **LiveListView** — это выделенное представление для отображения списка трансляций. Он автоматически загружает список трансляционных комнат и поддерживает различные стили отображения (**одноколонный** и **двухколонный**).

Kotlin

Java

```
import android.content.Contextimport android.os.Bundleimport androidx.appcompat.app.AppCompatActivityimport com.trtc.uikit.livekit.features.livelist.LiveListViewimport com.trtc.uikit.livekit.features.livelist.Styleclass YourActivity : AppCompatActivity() {    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        // 1. Create and initialize waterfall layout view        val view = createLiveListView(this)        // 2. Add the created LiveListView to your Activity or Fragment        setContentView(view)    }    fun createLiveListView(context: Context): LiveListView {        val liveListView = LiveListView(context)        // This code is a two-column waterfall layout initialization example. If you need to use a single column waterfall layout, change the initialization code to liveListView.init(this, Style.SINGLE_COLUMN)        liveListView.init(this, Style.DOUBLE_COLUMN)        return liveListView    }}
```

```
import android.content.Context;import android.os.Bundle;import androidx.appcompat.app.AppCompatActivity;import com.trtc.uikit.livekit.features.livelist.LiveListView;import com.trtc.uikit.livekit.features.livelist.Style;public class YourActivity extends AppCompatActivity {    @Override    protected void onCreate(Bundle savedInstanceState) {        super.onCreate(savedInstanceState);        // 1. Create and initialize waterfall layout view        LiveListView view = createLiveListView(this);        // 2. Add the created LiveListView to your Activity or Fragment        setContentView(view);    }    private LiveListView createLiveListView(Context context) {        LiveListView liveListView = new LiveListView(context);        // This code is a two-column waterfall layout initialization example. If you need to use a single column waterfall layout, change the initialization code to liveListView.init(this, Style.SINGLE_COLUMN, null, null);        liveListView.init(this, Style.DOUBLE_COLUMN, null, null);        return liveListView;    }}
```

### Шаг 4. Переход на страницу просмотра для зрителей

Вы можете настроить навигацию по страницам, установив слушатель нажатия. Для реализации страницы просмотра зрителями см. [Просмотр для зрителей](https://www.tencentcloud.com/document/product/647/72221):

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/cd2ba1fb992311f0961e52540099c741.png)

**Пример кода**:

Kotlin

Java

```
fun createLiveListView(context: Context): LiveListView {    val liveListView = LiveListView(context)    // This code is a two-column waterfall layout initialization example. If you need to use a single column waterfall layout, change the initialization code to liveListView.init(this, Style.SINGLE_COLUMN)    liveListView.init(this, Style.DOUBLE_COLUMN)    liveListView.setOnItemClickListener { view, liveInfo ->        click live list item to redirect to audience viewing page        val intent = Intent(context, YourAudienceActivity::class.java)        intent.putExtra("liveId", liveInfo.roomId)        context.startActivity(intent)    }    return liveListView}
```

```
private LiveListView createLiveListView(Context context) {    LiveListView liveListView = new LiveListView(context);    // This code is a two-column waterfall layout initialization example. If you need to use a single column waterfall layout, change the initialization code to liveListView.init(this, Style.SINGLE_COLUMN, null, null);    liveListView.init(this, Style.DOUBLE_COLUMN, null, null);    liveListView.setOnItemClickListener((view, liveInfo) -> {        click live list item to redirect to audience viewing page        Intent intent = new Intent(context, YourAudienceActivity.class);        intent.putExtra("liveId", liveInfo.roomId);        context.startActivity(intent);    });    return liveListView;}
```

## Настройка макета пользовательского интерфейса

**TUILiveKit** предоставляет гибкие интерфейсы для настройки компонента водопадного списка трансляций. Вы можете настроить источник данных и стили элементов списка в соответствии с потребностями вашего бизнеса.

### Настройка источника данных

Если ваш бэкэнд имеет отдельные данные списка трансляций, вы можете настроить источник данных, реализовав интерфейс `LiveListDataSource` вместо использования данных списка компонента по умолчанию.

Kotlin

Java

```
// 1. Import dependencyimport com.trtc.uikit.livekit.features.livelist.LiveListDataSource;// 2. Customize the data source by implementing LiveListDataSourceval dataSource = object : LiveListDataSource {    override fun fetchLiveList(param: FetchLiveListParam,callback: LiveListCallback) {        // Connect to your own business backend and return data to the UI component in the following format        val liveInfoList = mutableListOf<TUILiveListManager.LiveInfo>()        val liveInfo = TUILiveListManager.LiveInfo().apply {            roomInfo = TUIRoomDefine.RoomInfo().apply {                roomId = "live_123456"                name = "live_123456"            }        }        liveInfoList.add(liveInfo)        val cursor = "aabbccdd"        callback.onSuccess(cursor, liveInfoList)    }}// 3. Import a custom dataSource during initializationliveListView.init(this, Style.DOUBLE_COLUMN, dataSource = dataSource)
```

```
// 1. Import dependencyimport com.trtc.uikit.livekit.features.livelist.LiveListDataSource;// 2. Customize the data source by implementing LiveListDataSourceLiveListDataSource dataSource = (param, callback) -> {    // Connect to your own business backend and return data to the UI component in the following format    List<TUILiveListManager.LiveInfo> liveInfoList = new ArrayList<>();    TUILiveListManager.LiveInfo liveInfo = new TUILiveListManager.LiveInfo();    liveInfo.roomInfo = new TUIRoomDefine.RoomInfo();    liveInfo.roomInfo.roomId = "live_123456";    liveInfo.roomInfo.name = "live_123456";    liveInfoList.add(liveInfo);    String cursor = "aabbccdd";    callback.onSuccess(cursor, liveInfoList);};// 3. Import a custom dataSource during initializationliveListView.init(this, Style.DOUBLE_COLUMN, null, dataSource);
```

### Пользовательское представление

В нижней части элементов водопадного списка по умолчанию отображается видеопоток или обложка трансляции. Если вам нужно настроить элементы пользовательского интерфейса в верхней части элементов списка (например, аватар хоста, название трансляции и т. д.), вы можете сделать это, реализовав интерфейс `LiveListViewAdapter`.

Kotlin

Java

```
// 1. Import dependencyimport com.trtc.uikit.livekit.features.livelist.LiveListViewAdapter;// 2. Implement LiveListViewAdapter to customize widgetsval liveListViewAdapter = object : LiveListViewAdapter {    override fun createLiveInfoView(liveInfo: TUILiveListManager.LiveInfo): View {        // Custom view        val widgetView = YourView(context)        widgetView.init(liveInfo)        return widgetView    }    override fun updateLiveInfoView(view: View, liveInfo: TUILiveListManager.LiveInfo) {        // Refresh the bound data in the view        val widgetView = view as YourView        widgetView.updateLiveInfoView(liveInfo)    }}// 3. Import a custom liveListViewAdapter during initializationliveListView.init(this, Style.DOUBLE_COLUMN, adapter = liveListViewAdapter)
```

```
// 1. Import dependencyimport com.trtc.uikit.livekit.features.livelist.LiveListViewAdapter;// 2. Implement LiveListViewAdapter to customize widgetsLiveListViewAdapter liveListViewAdapter = new LiveListViewAdapter() {    @Override    public View createLiveInfoView(TUILiveListManager.LiveInfo liveInfo) {        // Custom view        CustomView widgetView = new CustomView(context);        widgetView.init(liveInfo);        return widgetView;    }    @Override    public void updateLiveInfoView(View view, TUILiveListManager.LiveInfo liveInfo) {        // Refresh the bound data in the view        CustomView widgetView = (CustomView) view;        widgetView.updateLiveInfoView(liveInfo);    }};// 3. Import a custom liveListViewAdapter during initializationliveListView.init(this, Style.DOUBLE_COLUMN, liveListViewAdapter, null);
```

## Дальнейшие шаги

Поздравляем! Вы успешно интегрировали функцию **Список трансляций в реальном времени**. Далее вы можете реализовать такие функции, как **Трансляция хостом** и **Просмотр для зрителей**. Обратитесь к таблице ниже:

| **Функция** | **Описание** | **Руководство по интеграции** |
| --- | --- | --- |
| **Трансляция хостом** | Полный рабочий процесс для хоста по запуску трансляции, включая подготовку перед трансляцией и различные взаимодействия во время трансляции. | [Трансляция хостом](https://www.tencentcloud.com/document/product/647/72219) |
| **Просмотр для зрителей** | Зрители могут смотреть прямую трансляцию после входа в трансляционную комнату якоря, с функциями, такими как подключение микрофона зрителя, информация о трансляционной комнате, онлайн-зрители и отображение чата. | [Просмотр для зрителей](https://www.tencentcloud.com/document/product/647/72221) |

## Часто задаваемые вопросы

### Что я должен делать, если на странице не отображаются трансляции после интеграции функции списка трансляций?

Если вы видите пустую страницу, вам нужно проверить, завершили ли вы [Полный вход](https://www.tencentcloud.com/document/product/647/72217#4b12969e-204b-4bcc-bdd3-702d8e20ea18). Для тестирования этой функции вы можете использовать два устройства: одно устройство для запуска трансляции и другое на странице списка трансляций для получения списка текущих трансляций.

### В чем разница между одноколонным и двухколонным водопадными макетами?

Одноколонный водопадный макет предпросматривает одну трансляционную комнату за раз, тогда как двухколонный водопадный макет одновременно предпросматривает две трансляционные комнаты. Вы можете выбрать подходящий макет в зависимости от требований вашего дизайна.

### Взимается ли плата за предпросмотр трансляций?

Да, длительность предпросмотра трансляционной комнаты учитывается в длительности аудио/видео зрителя, что является платной услугой. Для получения подробной информации о [Ценообразовании](https://www.tencentcloud.com/document/product/647/66078) вы можете обратиться к соответствующему содержимому в документации.


---
*Источник: [https://trtc.io/document/72220](https://trtc.io/document/72220)*

---
*Источник (EN): [live-stream-list.md](./live-stream-list.md)*

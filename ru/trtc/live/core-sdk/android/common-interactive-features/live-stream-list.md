# Список прямых трансляций

`LiveListStore` — это основной модуль **AtomicXCore**, отвечающий за управление списком прямых трансляций, создание и присоединение к комнатам, а также поддержание состояния комнаты. С помощью LiveListStore вы можете реализовать комплексное управление жизненным циклом прямых трансляций в вашем приложении.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a3e16b96b00111f0bb7b525400bf7822.png)

## Основные возможности

- **Получение списка комнат трансляций**: получение постраничного списка всех общедоступных комнат трансляций.
- **Управление жизненным циклом трансляции**: предоставляет полный набор интерфейсов для всего рабочего процесса трансляции, включая создание комнаты, начало трансляции, присоединение, выход и завершение сеанса.
- **Прослушивание событий в реальном времени**: прослушивание ключевых событий, таких как окончание сеанса трансляции или удаление пользователей из комнаты.

## Основные концепции

| **Основная концепция** | **Тип** | **Основная ответственность и описание** |
| --- | --- | --- |
| `LiveInfo` | `data class` | Представляет полную информационную модель комнаты трансляции. Включает ID комнаты трансляции (liveID), название (liveName), информацию о владельце (liveOwner) и пользовательские метаданные (metaData) и другие свойства. |
| `LiveListState` | `data class` | Представляет текущее состояние модуля списка трансляций. Основное свойство liveList — это StateFlow, содержащий полученный список комнат трансляций; currentLive представляет информацию о комнате трансляции, в которой в данный момент находится пользователь. |
| `LiveListListener` | `abstract class` | Обрабатывает глобальные события комнат трансляций, включая onLiveEnded (трансляция завершена) и onKickedOutOfLive (пользователь удален из трансляции) для реагирования на ключевые изменения состояния комнаты. |
| `LiveListStore` | `abstract class` | Основной класс управления для взаимодействия со списком комнат трансляций и жизненным циклом комнаты. Это глобальный синглтон, отвечающий за все операции, такие как создание, присоединение и обновление информации о комнате. |

## Реализация

### Шаг 1: интеграция компонентов

- **Видеотрансляция**: обратитесь к [Быстрому старту](https://www.tencentcloud.com/document/product/647/74593), чтобы интегрировать AtomicXCore и завершить реализацию функций [Трансляции видео ведущим](https://www.tencentcloud.com/document/product/647/74593#.E6.AD.A5.E9.AA.A4-1.-.E5.AE.9E.E7.8E.B0.E4.B8.BB.E6.92.AD.E8.A7.86.E9.A2.91.E5.BC.80.E6.92.AD) и [Присоединение аудитории и просмотр](https://www.tencentcloud.com/document/product/647/74593#.E6.AD.A5.E9.AA.A4-2.-.E5.AE.9E.E7.8E.B0.E8.A7.86.E4.BC.97.E8.BF.9B.E6.88.BF.E8.A7.86.E7.9C.8B).
- **Голосовая чат-комната**: обратитесь к [Быстрому старту](https://www.tencentcloud.com/document/product/647/74681), чтобы интегрировать AtomicXCore и завершить реализацию функций [Потоковой трансляции аудио ведущего](https://www.tencentcloud.com/document/product/647/74681#5cd97f75-6436-4ff6-964f-f5d1069b1f78) и [Присоединение аудитории и просмотр](https://www.tencentcloud.com/document/product/647/74681#5c50046e-16a6-4eba-b030-7e115313e07d).

### Шаг 2: реализация входа аудитории из списка комнат трансляций

Создайте страницу для отображения списка комнат трансляций с помощью RecyclerView для макета карточек комнат. Когда пользователь нажимает на карточку, получите liveId для этой комнаты и перейдите на страницу просмотра аудитории.

```
import android.content.Intentimport android.os.Bundleimport android.view.LayoutInflaterimport android.view.Viewimport android.view.ViewGroupimport androidx.appcompat.app.AppCompatActivityimport androidx.recyclerview.widget.GridLayoutManagerimport androidx.recyclerview.widget.RecyclerViewimport io.trtc.tuikit.atomicxcore.api.CompletionHandlerimport io.trtc.tuikit.atomicxcore.api.live.LiveInfoimport io.trtc.tuikit.atomicxcore.api.live.LiveListStoreimport kotlinx.coroutines.*import kotlinx.coroutines.flow.*class LiveListActivity : AppCompatActivity() {    private val liveListStore = LiveListStore.shared()    private var liveList: List<LiveInfo> = emptyList()    private val coroutineScope = CoroutineScope(Dispatchers.Main)    private lateinit var recyclerView: RecyclerView    private lateinit var adapter: LiveListAdapter    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        setContentView(R.layout.activity_live_list)        setupUI()        bindStore()        fetchLiveList()    }    private fun bindStore() {        // Subscribe to the state to automatically receive list updates        coroutineScope.launch {            liveListStore.liveState.liveList.collect { fetchedList ->                liveList = fetchedList                adapter.notifyDataSetChanged()            }        }    }    private fun fetchLiveList() {        liveListStore.fetchLiveList(            cursor = "",            count = 20,            completion = object : CompletionHandler {                override fun onSuccess() {                    println("Live room list fetched successfully")                }                override fun onFailure(code: Int, desc: String) {                    println("Failed to fetch live room list: $desc")                }            }        )    }    // When a user clicks an item in the list    private fun onLiveItemClick(liveInfo: LiveInfo) {        // Create the audience viewing page and pass the liveId        val intent = Intent(this, YourAudienceActivity::class.java)        intent.putExtra("liveId", liveInfo.liveID)        startActivity(intent)    }    // --- RecyclerView related methods ---    private fun setupUI() {        recyclerView = findViewById(R.id.recyclerView)        adapter = LiveListAdapter(liveList) { liveInfo ->            onLiveItemClick(liveInfo)        }        recyclerView.layoutManager = GridLayoutManager(this, 2)        recyclerView.adapter = adapter    }    override fun onDestroy() {        super.onDestroy()        coroutineScope.cancel()    }}// RecyclerView Adapterclass LiveListAdapter(    private var liveList: List<LiveInfo>,    private val onItemClick: (LiveInfo) -> Unit) : RecyclerView.Adapter<LiveListAdapter.LiveViewHolder>() {    class LiveViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {        // Define your ViewHolder view components        // val titleTextView: TextView = itemView.findViewById(R.id.titleTextView)        // val coverImageView: ImageView = itemView.findViewById(R.id.coverImageView)    }    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): LiveViewHolder {        val view = LayoutInflater.from(parent.context)            .inflate(R.layout.item_live_card, parent, false)        return LiveViewHolder(view)    }    override fun onBindViewHolder(holder: LiveViewHolder, position: Int) {        val liveInfo = liveList[position]        // Set data to ViewHolder        // holder.titleTextView.text = liveInfo.liveName        // Load cover image, etc.        holder.itemView.setOnClickListener {            onItemClick(liveInfo)        }    }    override fun getItemCount(): Int = liveList.size}
```

#### Справочник параметров LiveInfo

| **Имя параметра** | **Тип** | **Описание** |
| --- | --- | --- |
| `liveID` | `String` | Уникальный идентификатор комнаты трансляции |
| `liveName` | `String` | Название комнаты трансляции |
| `coverURL` | `String` | URL изображения обложки комнаты трансляции |
| `liveOwner` | [LiveUserInfo](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-user-info/index.html) | Личная информация владельца комнаты |
| `totalViewerCount` | `Int` | Общее количество зрителей в комнате трансляции |
| `categoryList` | `List<Int>` | Список тегов категорий для комнаты трансляции |
| `notice` | `String` | Информация об объявлении для комнаты трансляции |
| `metaData` | `Map<String, String>` | Определенные разработчиком метаданные для реализации продвинутых бизнес-сценариев |

## Продвинутые функции

### Сценарий 1: фильтрация по категориям списка комнат трансляций

На странице прямой трансляции пользователи могут выбирать теги категорий, такие как "Популярное", "Музыка", "Игры" и т. д. При выборе тега список комнат трансляций динамически фильтруется для отображения только комнат в выбранной категории, помогая пользователям быстро найти релевантный контент.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ecdcbe1db00311f09e195254007c27c5.png)

#### Реализация

Используйте свойство `categoryList` в модели `LiveInfo`. Когда ведущий выбирает категорию во время начала трансляции, API `fetchLiveList` возвращает объекты LiveInfo, которые включают эти сведения о категории. После получения полного списка комнат трансляции отфильтруйте его на клиенте на основе выбранной пользователем категории и обновите пользовательский интерфейс.

#### Пример кода

Следующий пример показывает, как расширить `LiveListManager` внутри `LiveListActivity` для обработки логики извлечения и фильтрации данных.

```
import android.os.Bundleimport androidx.appcompat.app.AppCompatActivityimport androidx.recyclerview.widget.RecyclerViewimport io.trtc.tuikit.atomicxcore.api.live.LiveInfoimport io.trtc.tuikit.atomicxcore.api.live.LiveListStoreimport kotlinx.coroutines.*import kotlinx.coroutines.flow.*// 1. Create a data manager to encapsulate data retrieval and filtering logicclass LiveListManager {    private val liveListStore = LiveListStore.shared()    private var fullLiveList: List<LiveInfo> = emptyList()    // Expose the final filtered live list externally    private val _filteredLiveList = MutableStateFlow<List<LiveInfo>>(emptyList())    val filteredLiveList: StateFlow<List<LiveInfo>> = _filteredLiveList    init {        // Listen for full list changes        CoroutineScope(Dispatchers.Main).launch {            liveListStore.liveState.liveList.collect { fetchedList ->                fullLiveList = fetchedList                // By default, publish the complete list                _filteredLiveList.value = fetchedList            }        }    }    fun fetchFirstPage() {        liveListStore.fetchLiveList(cursor = "", count = 20, completion = null)    }    /// Filter the live list by category    fun filterLiveList(categoryId: Int?) {        if (categoryId == null) {            // If categoryId is null, show the complete list            _filteredLiveList.value = fullLiveList            return        }        val filteredList = fullLiveList.filter { liveInfo ->            liveInfo.categoryList.contains(categoryId)        }        _filteredLiveList.value = filteredList    }}// 2. Use the Manager in your LiveListActivityclass LiveListActivity : AppCompatActivity() {    private val manager = LiveListManager()    private lateinit var recyclerView: RecyclerView    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        setContentView(R.layout.activity_live_list)        // setupUI()        // Bind data        CoroutineScope(Dispatchers.Main).launch {            manager.filteredLiveList.collect { filteredList ->                // Refresh UI               // adapter.updateList(filteredList)            }        }        // Fetch first page        manager.fetchFirstPage()    }    // When the user clicks a top category tag    fun onCategorySelected(categoryId: Int) {        manager.filterLiveList(categoryId)    }    // ... (RecyclerView related code)}
```

### Сценарий 2: потоковое воспроизведение при прокрутке списка комнат трансляций

Пользователи могут переключаться между комнатами трансляций, прокручивая вверх и вниз. Когда новая комната трансляции центрируется на экране, предпросмотр видео автоматически начинает воспроизводиться. Когда она покидает экран, воспроизведение автоматически останавливается для сохранения пропускной способности и ресурсов устройства.

> **Примечание**: **Потоковое воспроизведение при прокрутке** в настоящее время поддерживается только для видеотрансляций.

#### Поток взаимодействия

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/a4e1a14bc6c011f09e745254007c27c5.webp)

#### Реализация

`LiveCoreView` поддерживает несколько экземпляров. Создайте отдельный `LiveCoreView` для каждого `RecyclerView.ViewHolder`. Отслеживая состояние прокрутки `RecyclerView`, вы можете точно контролировать, когда начинать или останавливать потоковую передачу в каждом ViewHolder, добиваясь поведения "воспроизведение при прокрутке внутрь, остановка при прокрутке наружу".

#### Пример кода

Мы создаем пользовательский `LiveFeedViewHolder`, который внутренне содержит `LiveCoreView`. Затем мы управляем состоянием воспроизведения этих ViewHolders в `Activity`.

```
import android.os.Bundleimport android.view.LayoutInflaterimport android.view.Viewimport android.view.ViewGroupimport androidx.appcompat.app.AppCompatActivityimport androidx.recyclerview.widget.LinearLayoutManagerimport androidx.recyclerview.widget.RecyclerViewimport io.trtc.tuikit.atomicxcore.api.live.LiveInfoimport io.trtc.tuikit.atomicxcore.api.view.CoreViewTypeimport io.trtc.tuikit.atomicxcore.api.view.LiveCoreView// 1. Custom RecyclerView.ViewHolder, containing a LiveCoreView internallyclass LiveFeedViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {    private var liveCoreView: LiveCoreView? = null        fun setLiveInfo(liveInfo: LiveInfo) {        // Create a new LiveCoreView for the new live info        liveCoreView = LiveCoreView(itemView.context, viewType = CoreViewType.PLAY_VIEW)        liveCoreView?.let { view ->            (itemView as ViewGroup).addView(view)            view.layoutParams = ViewGroup.LayoutParams(                ViewGroup.LayoutParams.MATCH_PARENT,                ViewGroup.LayoutParams.MATCH_PARENT            )        }    }    fun startPlay(roomId: String) {        liveCoreView?.startPreviewLiveStream(roomId, false, callback = null)    }        fun stopPlay(roomId: String) {        liveCoreView?.stopPreviewLiveStream(roomId)    }}// 2. Manage playback logic in the Activityclass LiveFeedActivity : AppCompatActivity() {        private lateinit var recyclerView: RecyclerView    private var liveList: List<LiveInfo> = emptyList()    private var currentPlayingPosition: Int = -1    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        setContentView(R.layout.activity_live_feed)        setupRecyclerView()    }    private fun setupRecyclerView() {        recyclerView = findViewById(R.id.recyclerView)        recyclerView.layoutManager = LinearLayoutManager(this, LinearLayoutManager.VERTICAL, false)        recyclerView.adapter = LiveFeedAdapter(liveList) { position ->            playVideoAtPosition(position)        }        // Listen for scroll state        recyclerView.addOnScrollListener(object : RecyclerView.OnScrollListener() {            override fun onScrollStateChanged(recyclerView: RecyclerView, newState: Int) {                super.onScrollStateChanged(recyclerView, newState)                if (newState == RecyclerView.SCROLL_STATE_IDLE) {                    val layoutManager = recyclerView.layoutManager as LinearLayoutManager                    val firstVisiblePosition = layoutManager.findFirstCompletelyVisibleItemPosition()                    if (firstVisiblePosition != RecyclerView.NO_POSITION) {                        playVideoAtPosition(firstVisiblePosition)                    }                }            }        })    }    private fun playVideoAtPosition(position: Int) {        // Only switch playback when the centered position changes        if (currentPlayingPosition != position) {            // Stop current playback            if (currentPlayingPosition != -1) {                val currentViewHolder = recyclerView.findViewHolderForAdapterPosition(currentPlayingPosition)                if (currentViewHolder is LiveFeedViewHolder) {                    val liveInfo = liveList[currentPlayingPosition]                    currentViewHolder.stopPlay(liveInfo.liveID)                }            }                        // Start new playback            val newViewHolder = recyclerView.findViewHolderForAdapterPosition(position)            if (newViewHolder is LiveFeedViewHolder) {                val liveInfo = liveList[position]                newViewHolder.startPlay(liveInfo.liveID)                currentPlayingPosition = position            }        }    }        // RecyclerView Adapter    inner class LiveFeedAdapter(        private var liveList: List<LiveInfo>,        private val onItemClick: (Int) -> Unit    ) : RecyclerView.Adapter<LiveFeedViewHolder>() {                override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): LiveFeedViewHolder {            val view = LayoutInflater.from(parent.context)                .inflate(R.layout.item_live_feed, parent, false)            return LiveFeedViewHolder(view)        }        override fun onBindViewHolder(holder: LiveFeedViewHolder, position: Int) {            val liveInfo = liveList[position]            holder.setLiveInfo(liveInfo)            holder.itemView.setOnClickListener {                onItemClick(position)            }        }        override fun getItemCount(): Int = liveList.size    }}
```

## Документация API

Для получения подробной информации о всех открытых интерфейсах, свойствах и методах [LiveListStore](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-list-store/index.html) и связанных классов обратитесь к официальной документации API, включенной в фреймворк [AtomicXCore](https://tencent-rtc.github.io/TUIKit_Android/index.html). Соответствующие Store'ы, используемые в этом документе, приведены ниже:

| **Store/Компонент** | **Описание функции** | **Документация API** |
| --- | --- | --- |
| LiveCoreView | Основной компонент представления для отображения и взаимодействия с видеопотоком трансляции. Отвечает за рендеринг видеопотока и обработку виджетов представления, поддерживая сценарии, такие как трансляция ведущего, совместное участие аудитории и связь ведущего. | [Документация API](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.view/-live-core-view/index.html) |
| LiveListStore | Полное управление жизненным циклом комнат трансляций: создание, присоединение, выход, уничтожение комнат; запрос списка комнат; изменение информации о трансляции (название, объявление и т. д.); прослушивание статуса трансляции (таких как удаление или окончание). | [Документация API](https://tencent-rtc.github.io/TUIKit_Android/-atomic-x%20-core%20-a-p-i/io.trtc.tuikit.atomicxcore.api.live/-live-list-store/index.html) |

## Часто задаваемые вопросы

### Одинаковы ли данные списка для голосовых чат-комнат и видеотрансляций?

Да. Данные унифицированы; вам не нужно получать их отдельно. LiveListStore — это глобальный синглтон, который управляет жизненным циклом всех "прямых" комнат в вашем приложении, включая как видеокомнаты, так и голосовые чат-комнаты.

### Как я могу различать голосовые чат-комнаты и видеотрансляции в списке комнат трансляций?

`LiveListStore` не различает бизнес-типы комнат. Вы должны фильтровать и категоризировать список после получения на уровне приложения или пользовательского интерфейса.

Мы рекомендуем два подхода:

**Подход 1 (Рекомендуемый): использование seatLayoutTemplateID для различения.**

Этот ID шаблона определяет макет комнаты. Для поддерживаемых ID шаблонов и эффектов см. [Запуск и тестирование](https://www.tencentcloud.com/document/product/647/74593#.E8.BF.90.E8.A1.8C.E6.95.88.E6.9E.9C).

- **Шаг 1: укажите ID при создании комнаты**
  - При вызове `LiveListStore.shared.createLive` установите свойство `seatLayoutTemplateID` объекта `LiveInfo` на основе вашего бизнес-сценария:
  - Голосовые чат-комнаты: используйте ID шаблонов в диапазоне 1–199.
  - Видеотрансляции: используйте ID шаблонов в диапазоне 200–999.
- **Шаг 2: фильтруйте при получении списка**
  - На клиенте, после получения списка в `LiveListStore.state.liveList`, определите бизнес-сценарий, проверив диапазон ID шаблона.

> **Примечание**: если seatLayoutTemplateID не соответствует вашему бизнес-сценарию (голосовая чат-комната или видеотрансляция), функции макета мест могут работать не так, как ожидается.

**Подход 2:** **Добавьте бизнес-префикс к**`liveID`**.**

Это необязательное соглашение на уровне приложения для быстрой фильтрации комнат.

- **Шаг 1: добавьте префикс при создании комнаты**
  - При создании liveID и вызове createLive присвойте разные префиксы для каждого бизнес-типа. Например: ID видеокомнат начинаются с "Live_" (например, Live_12345), ID голосовых чат-комнат начинаются с "voice_" (например, voice_67890).
- **Шаг 2: проверьте префикс при получении списка**
  - На клиенте, после получения списка, различайте комнаты, проверяя префикс liveID.


---
*Источник: [https://trtc.io/document/74609](https://trtc.io/document/74609)*

---
*Источник (EN): [live-stream-list.md](./live-stream-list.md)*

# Вертикальная прокрутка прямых трансляций

В сценариях прямой трансляции, где большое количество ведущих предлагают разнообразный видеоконтент, позволение пользователям быстро просматривать и выбирать любимый контент путем прокрутки вверх или вниз может обеспечить улучшенный опыт пользователя. В этом документе описаны решения реализации для Android и iOS соответственно.

## Решение для вертикальной прокрутки прямых трансляций на iOS

В таких сценариях переключение между комнатами прямой трансляции может вызвать разрывы между видеопотоками текущей и следующей комнат, так как вход в новую комнату и получение потоков занимают время. Для решения этой проблемы доступны 3 решения. В этом документе подробно объясняются все 3 решения.

| **Метод реализации** | **Опыт пользователя** | **Потребление ресурсов** | **Логика реализации** |
| --- | --- | --- | --- |
| [Чёрный экран](https://www.tencentcloud.com/document/product/1228/73993#9ed39c99-904e-499e-a06c-18be6397e1a1) | Хороший. При переключении между комнатами прямой трансляции перед появлением нового видео отображается чёрный экран. | Без дополнительного потребления ресурсов. | Простой. Без дополнительной логики. |
| [Заполняющее изображение](https://www.tencentcloud.com/document/product/1228/73993#66cb12f1-0c90-48e1-814b-5a327734042d) | Немного лучше. При переключении между комнатами прямой трансляции перед появлением нового видео отображается фиксированное заполняющее изображение соответствующего ведущего. | Немного выше. Для каждого ведущего необходимо дополнительно хранить заполняющее изображение и загружать его на клиент. | Немного сложнее. Требуется дополнительная асинхронная загрузка заполняющих изображений перед переключением. |
| [Двойные экземпляры](https://www.tencentcloud.com/document/product/1228/73993#2ea458a4-4c26-489e-9994-35bbece92bcd) | Лучший. При переключении между комнатами прямой трансляции видео текущего и следующего ведущих отображаются плавно. | Выше. Два потока должны получаться одновременно в списке. После входа в комнату прямой трансляции требуется получение только 1 потока. | Более сложный. Требуются несколько экземпляров, и необходимо контролировать получение аудио и видео каждого экземпляра. |

### Чёрный экран

Путем прослушивания системных событий прокрутки код реализует вызов бизнес-персоналом API переключения комнат для переключения между комнатами прямой трансляции. До полной загрузки новой комнаты прямой трансляции содержимое не отображается, в результате чего появляется краткий чёрный экран. Для удобства, здесь продолжительность чёрного экрана составляет около 1 секунды. Конкретная продолжительность чёрного экрана зависит от условий сети и битрейта видео. Отображение выглядит следующим образом.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/e4fe1d26c36d11f0a6dd5254005ef0f7.gif)

Фрагмент кода для переключения комнат выглядит следующим образом:

```
let src = TRTCSwitchRoomConfig()// Generate the corresponding room ID and room entry credential according to business needs. In this example, generate the room entry credential on the client. For online businesses, obtain the information from the backend.src.strRoomId = strRoomIdsrc.userSig = GenerateTestUserSig.genTestUserSig(identifier: userId) as StringtrtcCloud.switchRoom(src)
```

### Заполняющее изображение

Путем прослушивания системных событий прокрутки код реализует вызов бизнес-персоналом API переключения комнат для переключения между комнатами прямой трансляции. В отличие от решения с чёрным экраном, это решение требует предварительной загрузки заполняющего изображения для каждой комнаты прямой трансляции. До появления видеопотока комнаты прямой трансляции отображается заполняющее изображение комнаты. Для удобства, здесь продолжительность заполняющего изображения составляет около 1 секунды. Конкретная продолжительность зависит от условий сети и битрейта видео.

#### Отображение

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/ff27dbedc36d11f0aa02525400e889b2.gif)

#### Этапы реализации

1. Установите фоновое изображение для первого ведущего.

```
bgView = UIImageView(frame: self.view.bounds)// The image should be the placeholder image for the corresponding live streaming room. Business personnel should obtain the image in advance.bgView.image = UIImage(named: "1.png")bgView.contentMode = .scaleAspectFillbgView.translatesAutoresizingMaskIntoConstraints = falseself.view.insertSubview(bgView, at: 0)NSLayoutConstraint.activate([    bgView.topAnchor.constraint(equalTo: view.topAnchor),    bgView.bottomAnchor.constraint(equalTo: view.bottomAnchor),    bgView.leadingAnchor.constraint(equalTo: view.leadingAnchor),    bgView.trailingAnchor.constraint(equalTo: view.trailingAnchor),])
```

2. Переключите фоновое изображение перед переключением между комнатами прямой трансляции.

```
DispatchQueue.main.async {    UIView.transition(            with: self.bgView,            duration: 0,            options: .transitionCrossDissolve,            animations: {                // Business personnel switches the corresponding placeholder image.                self.bgView.image = UIImage(named: strRoomId)            }, completion: nil)}let src = TRTCSwitchRoomConfig()// Generate the corresponding room ID and room entry credential according to business needs. In this example, generate the room entry credential on the client. For online businesses, obtain the information from the backend.src.strRoomId = strRoomIdsrc.userSig = GenerateTestUserSig.genTestUserSig(identifier: userId) as StringtrtcCloud.switchRoom(src)
```

3. Переключите фоновое изображение на видео, когда первый видеокадр начинает отображаться в новой комнате прямой трансляции.

```
// Pull video streams.func onUserVideoAvailable(_ userId: String, available: Bool) {    if available {        trtcCloud.startRemoteView(userId, streamType: .big, view: view)    } else {        trtcCloud.stopRemoteView(userId, streamType: .big)    }}// When the first video frame starts rendering, switch the placeholder image to the background and display the video.func onFirstVideoFrame(_ userId: String, streamType: TRTCVideoStreamType, width: Int32, height: Int32) {    // Adjust the sequence of the background image and the video rendering control as needed.    self.view.exchangeSubview(at: 1, withSubviewAt: 0)}
```

### Двойные экземпляры

> **Примечание:** Хотя это решение обеспечивает лучший эффект отображения и опыт пользователя, оно требует одновременного получения 2 потоков из текущей и следующей комнат прямой трансляции, когда пользователь прокручивает список. Хотя поток следующей комнаты прямой трансляции может прекратить предварительную загрузку после входа пользователя в комнату, это решение приводит к более высокому общему трафику и платежам.

#### Отображение

Для достижения наиболее плавного эффекта вертикальной прокрутки одновременно должны использоваться 2 экземпляра. Во время просмотра текущей комнаты прямой трансляции видеопоток следующей комнаты прямой трансляции предварительно загружается. Путём использования UIPageViewController или ручного регулирования позиций отображения текущего и следующего видео на основе положения прокрутки достигается естественный и плавный переход. Эффект прокрутки к следующей комнате прямой трансляции показан в примере слева ниже.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/4d58f8b6c36e11f0a6dd5254005ef0f7.gif)

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/50e63d51c36e11f08c0e52540044a08e.gif)

Общая логика этого решения выглядит следующим образом. После входа в текущую комнату прямой трансляции подэкземпляр немедленно используется для входа в следующую комнату прямой трансляции, получения видеопотока следующей комнаты и отображения потока на следующей странице UIPageViewController. После входа в новую комнату прямой трансляции включается аудиопоток новой комнаты. Этот цикл повторяется, обеспечивая наиболее плавный эффект вертикальной прокрутки. Между тем, во избежание чрезмерного потребления ресурсов, предварительно загружается только следующая комната прямой трансляции, в то время как менее часто используемая предыдущая комната прямой трансляции не предварительно загружается. В результате при переключении обратно на предыдущую комнату прямой трансляции всё ещё отображается краткий чёрный экран. Эффект просмотра предыдущей комнаты прямой трансляции показан в примере справа выше.

#### Этапы реализации

1. Определите служебный класс подэкземпляра.

```
import Foundationimport ObjectiveCimport TXLiteAVSDK_Professional@objc protocol SubCloudHelperDelegate : NSObjectProtocol {    @objc optional func onUserVideoAvailableWithSubId(subId: Int, userId: String, available: Bool)}class SubCloudHelper:NSObject,TRTCCloudDelegate {    var trtcCloud: TRTCCloud!    var subId: Int!    weak var delegate : SubCloudHelperDelegate? = nil        func initWithSubId(subId: Int, trtcIns: TRTCCloud) {        self.subId = subId        self.trtcCloud = trtcIns        self.trtcCloud.addDelegate(self)    }    func getCloud()->TRTCCloud {        return trtcCloud    }    func onUserVideoAvailable(_ userId: String, available: Bool) {        if self.delegate?.onUserVideoAvailableWithSubId?(subId: subId, userId: userId, available: available) == nil {            return        }    }}
```

2. Используйте подэкземпляр.

```
let trtcCloud = TRTCCloud()let subCloudHelper = SubCloudHelper()override func viewDidLoad() {    super.viewDidLoad()        subCloudHelper.initWithSubId(subId: 0, trtcIns: trtcCloud.createSub())    subCloudHelper.delegate = self}
```

3. Подготовьте UIPageViewController для переключения.

```
private var atRoom: Bool = falsevar pageViewController: UIPageViewController!var pageZero: UIViewController!var pageOne: UIViewController!var pageTwo: UIViewController!var pages: [UIViewController] = []var curPageIdx = 0var curIsSub = falsefunc setupPages() {    pageViewController = UIPageViewController(        transitionStyle: .scroll,        navigationOrientation: .vertical    )    pageViewController.dataSource = self    pageViewController.delegate = self    addChild(pageViewController)    view.addSubview(pageViewController.view)    pageViewController.didMove(toParent: self)    // pages    pageZero = UIViewController()    pageZero.view.backgroundColor = .black    pageOne = UIViewController()    pageOne.view.backgroundColor = .black    pageTwo = UIViewController()    pageTwo.view.backgroundColor = .black    pages = [pageZero, pageOne, pageTwo]        pageViewController.setViewControllers([pages[curPageIdx]], direction: .forward, animated: false)}
```

4. Реализуйте переключение страниц в pageViewController.

```
// Obtain the next/previous page.func getShowPage(isNext: Bool) -> UIViewController {    var newPageIdx = 0    if isNext {        newPageIdx = curPageIdx + 1    } else {        newPageIdx = curPageIdx - 1    }    if newPageIdx >= pages.count {        newPageIdx = 0    } else if newPageIdx < 0 {        newPageIdx = pages.count - 1    }    return pages[newPageIdx]}extension RtcDuplexVC: UIPageViewControllerDataSource {    func pageViewController(_ pageViewController: UIPageViewController, viewControllerBefore viewController: UIViewController) -> UIViewController? {        return getShowPage(isNext: false)    }    func pageViewController(_ pageViewController: UIPageViewController, viewControllerAfter viewController: UIViewController) -> UIViewController? {        return getShowPage(isNext: true)    }}
```

5. Основной экземпляр входит в комнату прямой трансляции, а подэкземпляр предварительно загружает следующую комнату.

```
// The primary instance enters the room.// Replace sdkAppId, roomID, strRoomId, userId, and userSig based on actual business needs.// In this example, generate userSig on the client. For online businesses, obtain the information from the backend.let params = TRTCParams()params.sdkAppId = UInt32(SDKAppID)params.roomId = 0params.strRoomId = strRoomIdLst.first ?? "1"params.userId = userIdparams.role = .anchorparams.userSig = GenerateTestUserSig.genTestUserSig(identifier: userId) as StringtrtcCloud.addDelegate(self)trtcCloud.enterRoom(params, appScene: .LIVE)// The sub-instance preloads and enters the next room.// Replace sdkAppId, roomID, strRoomId, userId, and userSig based on actual business needs.// In this example, generate userSig on the client. For online businesses, obtain the information from the backend.let subParams = TRTCParams()subParams.sdkAppId = UInt32(SDKAppID)subParams.roomId = 0subParams.strRoomId = strRoomIdLst[1]subParams.userId = userIdsubParams.role = .anchorsubParams.userSig = GenerateTestUserSig.genTestUserSig(identifier: userId) as StringsubCloudHelper.trtcCloud.enterRoom(subParams, appScene: .LIVE)subCloudHelper.trtcCloud.muteAllRemoteAudio(true)
```

6. Получайте видеопотоки на основе обратных вызовов и визуализируйте потоки на соответствующей странице.

```
func getPageByIdx(isNext: Bool) -> UIViewController {    var newPageIdx = curPageIdx    if isNext {        newPageIdx += 1    }    if newPageIdx >= pages.count {        newPageIdx = 0    }    return pages[newPageIdx]}extension RtcDuplexVC: TRTCCloudDelegate {    func onUserVideoAvailable(_ userId: String, available: Bool) {        if available {            trtcCloud.startRemoteView(userId, streamType: .big, view: getPageByIdx(isNext: curIsSub).view)        } else {            trtcCloud.stopRemoteView(userId, streamType: .big)        }    }}extension RtcDuplexVC: SubCloudHelperDelegate {    func onUserVideoAvailableWithSubId(subId: Int, userId: String, available: Bool) {        if available {            subCloudHelper.trtcCloud.startRemoteView(userId, streamType: .big, view: getPageByIdx(isNext: !curIsSub).view)        } else {            subCloudHelper.trtcCloud.stopRemoteView(userId, streamType: .big)        }    }}
```

7. Обновите комнату предварительной загрузки после переключения в новую комнату или обновите текущую отображаемую комнату во время прокрутки вверх.

```
func updateCurRoomIdx(isNext: Bool) {    if isNext {        curRoomIdx += 1        if curRoomIdx >= strRoomIdLst.count {            curRoomIdx = 0        }    } else {        curRoomIdx -= 1        if curRoomIdx < 0 {            curRoomIdx = strRoomIdLst.count - 1        }    }}// Here, you need to switch the room ID based on the actual business logic.func updateNewRoom(isNext: Bool) {    var newRoomIdx = 0    if isNext{        newRoomIdx = curRoomIdx + 1    } else {        newRoomIdx = curRoomIdx - 1    }    if newRoomIdx >= strRoomIdLst.count {        newRoomIdx = 0    } else if newRoomIdx < 0 {        newRoomIdx = strRoomIdLst.count - 1    }    let newRoomStrId = strRoomIdLst[newRoomIdx]        let src = TRTCSwitchRoomConfig()    src.strRoomId = newRoomStrId    src.userSig = GenerateTestUserSig.genTestUserSig(identifier: userId) as String    if curIsSub {        trtcCloud.switchRoom(src)        trtcCloud.muteAllRemoteAudio(true)    } else {        subCloudHelper.trtcCloud.switchRoom(src)        subCloudHelper.trtcCloud.muteAllRemoteAudio(true)    }}extension RtcDuplexVC: UIPageViewControllerDelegate {    func pageViewController(        _ pageViewController: UIPageViewController,        didFinishAnimating finished: Bool,        previousViewControllers: [UIViewController],        transitionCompleted completed: Bool    ) {        if completed {            guard let currentVC = pageViewController.viewControllers?.first else {return}            if let index = pages.firstIndex(of: currentVC) {                // Obtain the basis for determining whether the user scrolled up or down.                let iden = index - curPageIdx                // Update the index of the currently displayed page.                curPageIdx = index                // Scroll down.                if iden == 1 || iden == -2 {                    // Update the index of the current room.                    updateCurRoomIdx(isNext: true)                    // Update the instance of the currently displayed page.                    curIsSub.toggle()                    // Update the room.                    updateNewRoom(isNext: true)                }                // Scroll up.                if iden == -1 || iden == 2 {                    // Update the room.                    updateNewRoom(isNext: false)                    // Update the index of the current room.                    updateCurRoomIdx(isNext: false)                    // Update the instance of the currently displayed page.                    curIsSub.toggle()                    trtcCloud.muteAllRemoteAudio(true)                    subCloudHelper.trtcCloud.muteAllRemoteAudio(true)                }                // Unmute the current room.                if curIsSub {                    subCloudHelper.trtcCloud.muteAllRemoteAudio(false)                } else {                    trtcCloud.muteAllRemoteAudio(false)                }            }        }    }}
```

Кроме того, бизнес-персонал может различать состояния "прокрутка списка" и "в комнате прямой трансляции". При прокрутке вверх или вниз, обычно не требуется информация, включая детали комнаты и чаты. Эта информация должна отображаться только после входа в комнату прямой трансляции. Это различие может уменьшить нагрузку на бизнес-персонал по записи статуса комнаты прямой трансляции во время частой вертикальной прокрутки, одновременно уменьшая потребление ресурсов от предварительной загрузки.

Конкретный подход выглядит следующим образом. Только пользователи, которые прокручивают список, могут переключаться между комнатами прямой трансляции путём прокрутки вверх или вниз. В этом случае отображаются только визуальные элементы комнаты прямой трансляции и небольшое количество информации. После входа в комнату прямой трансляции отображаются полная комната прямой трансляции, чаты и другая информация. В этот момент пользователям не разрешается переключаться между комнатами прямой трансляции путём прокрутки вверх или вниз. Между тем, предварительная загрузка видеопотока для следующей комнаты прямой трансляции прекращается после входа пользователя в комнату и возобновляется, когда пользователи возвращаются в состояние "прокрутка списка". Эффект выглядит следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7e6452e6c37c11f0aa02525400e889b2.gif)

Конкретная реализация выглядит следующим образом:

```
// Handle the logic for entering a live streaming room.@objc func enterBtnClick() {    // Hide the UI component in the vertical scrolling list.    self.enterBtn.isHidden = true    // Display the UI component after the user enters a live streaming room.    self.exitBtn.isHidden = false    // ...        self.atRoom = true    // Forbid vertical scrolling once the user enters a live streaming room.    pageViewController.dataSource = nil        // Stop preloading.    if curIsSub{        trtcCloud.muteAllRemoteVideoStreams(true)    } else {        subCloudHelper.trtcCloud.muteAllRemoteAudio(true)    }}  // Handle the logic for exiting a live streaming room.@objc func exitBtnClick() {    // Hide the UI component in a live streaming room.    self.enterBtn.isHidden = false    // Display the UI component in the vertical scrolling list.    self.exitBtn.isHidden = true        self.atRoom = false    // Restore vertical scrolling once the user enters the vertical scrolling list.    pageViewController.dataSource = self    // Restore preloading.    if curIsSub{        trtcCloud.muteAllRemoteVideoStreams(false)    } else {        subCloudHelper.trtcCloud.muteAllRemoteAudio(false)    }}
```

## Решение для вертикальной прокрутки прямых трансляций на Android

В разделах двойных экземпляров и одного экземпляра ниже, отображение и пример кода содержат 3 страницы. Порядок 3 страниц выглядит следующим образом: A > B > C. A соответствует Room 1231, B соответствует Room 1232, а C соответствует Room 1233.

| **Метод реализации** | **Опыт пользователя** | **Потребление ресурсов** | **Логика реализации** |
| --- | --- | --- | --- |
| [Одиночный экземпляр](https://www.tencentcloud.com/document/product/1228/73993#03055b6b-0ecb-4e65-9843-2b8ba3ab4c28) | Как правило, во время прокрутки списка вы не можете просматривать 2 комнаты прямой трансляции одновременно. Соответствующая комната прямой трансляции отображается только после полного переключения страницы. В этом случае заполняющие изображения могут быть использованы для улучшения опыта пользователя. | Только 1 поток в списке потребляет трафик, и используется 1 объект воспроизведения видео. | Простой. Установите заполняющие изображения по мере необходимости. |
| [Двойные экземпляры](https://www.tencentcloud.com/document/product/1228/73993#b91115f4-9b26-41f5-8f50-49a29c090772) | Лучше. Вы можете войти в 2 комнаты прямой трансляции одновременно, и следующая комната прямой трансляции загружается заранее. Во время прокрутки списка вы можете просматривать как текущую, так и следующую комнаты прямой трансляции одновременно. | Два потока в списке потребляют трафик, что приводит к платежам за 2 потока, и используются 2 объекта воспроизведения видео. | Сложный. Требуются несколько экземпляров, и необходимо контролировать получение аудио и видео каждого экземпляра. |

### Одиночный экземпляр

При прокрутке вверх или вниз список прямых трансляций вы можете просматривать только 1 прямую трансляцию (одиночный экземпляр), что приводит к более низким затратам.

#### Отображение

При прокрутке со страницы A вы не можете просматривать прямую трансляцию на странице B одновременно. После переключения на страницу B вы можете просматривать прямую трансляцию на странице B, но больше не сможете просматривать прямую трансляцию на странице A.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2ec19a8ac36f11f0a0935254007c27c5.gif)

#### Принцип решения

При прокрутке между страницами вы можете просматривать только 1 прямую трансляцию в любой момент. После переключения страницы предыдущая прямая трансляция прекращается, и следующая прямая трансляция получается.

При прокрутке со страницы A на страницу B операции и состояние на каждом этапе выглядят следующим образом:

1. Когда страница A отображается на экране, экземпляр TRTCCloud 1 используется для входа в Room 1231, получения потока и воспроизведения аудио и видео на странице A.
2. Во время процесса прокрутки со страницы A на страницу B, если обратный вызов переключения на страницу B ещё не получен, страница A продолжает воспроизводить аудио и видео из Room 1231, в то время как страница B показывает заполняющее изображение или чёрный экран.
3. Во время процесса прокрутки со страницы A на страницу B, если обратный вызов переключения на страницу B получен, экземпляр TRTCCloud 1 используется для прекращения получения аудио и видео из Room 1231, выхода из комнаты, а затем входа в Room 1232 для получения и воспроизведения нового аудио и видео на странице B, в то время как страница A показывает заполняющее изображение или чёрный экран.

#### Код реализации

Используйте ViewPager2 и RecyclerView.Adapter для достижения эффекта полноэкранной прокрутки. В обратном вызове onPageSelected функции registerOnPageChangeCallback в ViewPager2 прекратите получение текущего потока, покиньте текущую комнату, войдите в новую комнату и начните получение нового потока. Ниже приведен полный код ScrollSwitchRoomActivity. Файл макета такой же, как в предыдущем разделе.

Код ScrollSwitchRoomActivity выглядит следующим образом:

```
public class ScrollSwitchRoomActivity extends TRTCBaseActivity {    PageAdapter mAdapter;    public String[] mRoomIds;    private TRTCCloud mTRTCCloud;    private TXCloudVideoView mRemoteVideoView;    private int mCurPos = -1;    @Override    protected void onCreate(Bundle savedInstanceState) {        super.onCreate(savedInstanceState);        setContentView(R.layout.activity_scroll_switch_room);        // Hide the title bar.        getSupportActionBar().hide();        mRoomIds = new String[]{"1231", "1232", "1233"};        if (checkPermission()) {            initView();        }    }    @Override    protected void onPermissionGranted() {        initView();    }    private void initView() {        mAdapter = new PageAdapter(this, mRoomIds);        ViewPager2 viewPager = findViewById(R.id.viewPager);        viewPager.setAdapter(mAdapter);        // Set the viewPager scrolling orientation.        viewPager.setOrientation(ViewPager2.ORIENTATION_VERTICAL);        // Set the viewPager preloading.        viewPager.setOffscreenPageLimit(1);        // Add a page switch listener.        viewPager.registerOnPageChangeCallback(new ViewPager2.OnPageChangeCallback() {            public void onPageSelected(int position) {                Log.d("ScrollSwitchRoom", "onPageSelected: " + position);                if (mCurPos == position) {                    return;                }                                RecyclerView recyclerViewImpl = (RecyclerView) viewPager.getChildAt(

---
*Источник (EN): [vertical-scrolling-of-live-streams.md](./vertical-scrolling-of-live-streams.md)*

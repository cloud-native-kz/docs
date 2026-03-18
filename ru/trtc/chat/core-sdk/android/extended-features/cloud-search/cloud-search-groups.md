# Поиск облачных групп

## Описание

Вы можете выполнять поиск облачных групп по ID группы, названию группы и другой информации, чтобы быстро найти требуемый профиль группы. Эта функция особенно полезна в сценариях, где необходимо найти конкретные группы, например при поиске интересующих вас групп для присоединения в социальных сетях.

> **Примечание:** Функция поиска облачных групп поддерживается только версией 8.4 и выше. Функция перевода сообщений доступна только для клиентов Pro Plus и Enterprise. Она может быть использована после [приобретения Pro Plus и Enterprise](https://console.trtc.io/subscription/buy/chat?packType=pro&language=en); версия Free Trial поддерживает [определённый лимит бесплатного пробного периода](https://www.tencentcloud.com/document/product/1047/67651#d1113f0d-47e8-4211-82c0-00d2efb72586), действительный в течение одного месяца. Если этот сервис не активирован, вызов интерфейса вернёт код ошибки 60020.

## Интерфейс поиска облачных групп

Вызовите интерфейс `searchCloudGroups` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a322641b6386d4698dd1611fee69891e0) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.searchcloudgroups(searchparam:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#a8c3f83c844be3c8bb13fe9cec6fd658a) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#afce316958d6b3e25512b6d2e4e6a19ba)) для поиска информации о группе в облаке.

Параметры `V2TIMGroupSearchParam` приведены ниже:

| Параметр | Значение | Описание |
| --- | --- | --- |
| keywordList | Список ключевых слов | Может содержать до пяти ключевых слов; ключевое слово будет автоматически совпадать с ID группы и названием группы. |
| keywordListMatchType | Тип совпадения списка ключевых слов | Вы можете установить поиск с логикой "ИЛИ" или "И". Значения — `V2TIM_KEYWORD_LIST_MATCH_TYPE_OR` и `V2TIM_KEYWORD_LIST_MATCH_TYPE_AND` соответственно. По умолчанию используется логика "ИЛИ". |
| searchCount | Количество результатов поиска | Должно быть больше 0, максимально поддерживаемое значение — 100, значение по умолчанию — 20. |
| searchCursor | Курсор поиска | Начальная позиция; при первом вызове введите пустую строку, при последующих вызовах введите `searchCursor` из последнего возвращённого `V2TIMGroupSearchResult`. |

### Класс результатов поиска группы

Класс результатов поиска группы — `V2TIMGroupSearchResult`：[Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupSearchResult.html) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMGroupSearchResult.html) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMGroupSearchResult.html) / [C++](https://im.sdk.qcloud.com/doc/en/structV2TIMGroupSearchResult.html)。Параметры описаны ниже:

| Параметр | Значение | Описание |
| --- | --- | --- |
| isFinished | Завершён ли поиск | Возвращены ли все группы, соответствующие критериям поиска. |
| totalCount | Всего результатов поиска | Общее количество групп, соответствующих критериям поиска. |
| nextCursor | Курсор для продолжения выборки | Курсор поиска для следующего облачного поиска. |
| groupList | Список групп | Список групп, возвращённый текущим облачным поиском. |

Ниже приведён пример кода:

Java

Swift

Objective-C

C++

```
V2TIMGroupSearchParam searchParam = new V2TIMGroupSearchParam();searchParam.setKeywordList(keywordList);searchParam.setKeywordListMatchType(param.V2TIM_KEYWORD_LIST_MATCH_TYPE_OR);searchParam.setSearchCount(20);searchParam.setSearchCursor("");V2TIMManager.getGroupManager().searchCloudGroups(searchParam, new V2TIMValueCallback<V2TIMGroupSearchResult>() {  @Override  public void onSuccess(V2TIMGroupSearchResult groupSearchResult) {       // search cloud groups succ  }  @Override  public void onError(int code, String desc) {      // search cloud groups succ failed  }});
```

```
let param = V2TIMGroupSearchParam()param.keywordList = ["keyword1", "keyword2"];param.keywordListMatchType = .V2TIM_KEYWORD_LIST_MATCH_TYPE_OR;param.searchCount = 20;param.searchCursor = "";V2TIMManager.shared.searchCloudGroups(searchParam: param) { searchResult in    // search cloud groups succ} fail: { code, desc in    // search cloud groups succ failed}
```

```
V2TIMGroupSearchParam *param = [[V2TIMGroupSearchParam alloc] init];param.keywordList = @[@"keyword1", @"keyword2"];param.keywordListMatchType = V2TIM_KEYWORD_LIST_MATCH_TYPE_OR;param.searchCount = 20;param.searchCursor = @"";[[V2TIMManager sharedInstance] searchCloudGroups:param succ:^(V2TIMGroupSearchResult *searchResult) {    // search cloud groups succ} fail:^(int code, NSString *desc) {    // search cloud groups succ failed}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMGroupSearchParam searchParam;searchParam.keywordList = keywordList;searchParam.keywordListMatchType = V2TIM_KEYWORD_LIST_MATCH_TYPE_OR;searchParam.searchCount = 20;searchParam.searchCursor = "";auto callback = new ValueCallback<V2TIMGroupSearchResult>{};callback->SetCallback(    [=](const V2TIMGroupSearchResult& groupSearchResult) {        // search cloud groups succ        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // search cloud groups succ failed        delete callback;    });V2TIMManager::GetInstance()->GetGroupManager()->SearchCloudGroups(searchParam, callback);
```


---
*Источник: [https://trtc.io/document/67836](https://trtc.io/document/67836)*

---
*Источник (EN): [cloud-search-groups.md](./cloud-search-groups.md)*

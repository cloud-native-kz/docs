# Поиск членов облачной группы

## Описание

Вы можете выполнять поиск членов облачной группы по ID участника, никнейму и информации карточки имени. Эта функция особенно полезна для быстрого поиска конкретных членов группы, например для быстрого обнаружения участника в большой группе.

> **Примечание:** Функция поиска членов облачной группы поддерживается только версией 8.4 и выше. Функция поиска облачных сообщений доступна только для клиентов **Pro Plus и Enterprise** и может использоваться после [покупки Pro Plus и Enterprise](https://console.trtc.io/subscription/buy/chat?packType=pro&language=en); версия Free Trial поддерживает [определённый лимит бесплатного пробного периода](https://www.tencentcloud.com/document/product/1047/67651#d1113f0d-47e8-4211-82c0-00d2efb72586), действительный в течение одного месяца. Если эта служба не активирована, вызов интерфейса вернёт код ошибки 60020.

## Интерфейс поиска членов облачной группы

Вызовите интерфейс `searchCloudGroupMembers` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a1db4218077a0db6c623a19d66ba72b5a) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Group.html#v2timmanager.searchcloudgroupmembers(searchparam:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Group_08.html#ae2f92bf458c5b6ef0149d66de7a01896) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMGroupManager.html#a1b162f6187a846c9ea05636c9135c59c)) для поиска информации о членах группы в облаке.

Параметры `V2TIMGroupMemberSearchParam` следующие:

| Параметр | Значение | Описание |
| --- | --- | --- |
| keywordList | Список ключевых слов | Может содержать до пяти ключевых слов, ключевое слово автоматически будет совпадать с ID участника группы, никнеймом и карточкой имени. |
| keywordListMatchType | Тип сопоставления списка ключевых слов | Вы можете установить поиск с логикой "ИЛИ" или "И". Значения: `V2TIM_KEYWORD_LIST_MATCH_TYPE_OR` и `V2TIM_KEYWORD_LIST_MATCH_TYPE_AND` соответственно. По умолчанию используется логика "ИЛИ". |
| groupIDList | Укажите список ID групп | Если `groupIDList` установлен в null, это означает поиск членов группы во всех группах, а возвращаемые результаты будут классифицированы по `groupID`. Если `groupIDList` установлен не равным null, это означает поиск членов группы в указанной группе. |
| searchCount | Количество результатов поиска | Должно быть больше 0, максимум 100, по умолчанию 20. |
| searchCursor | Курсор поиска | Начальная позиция, при первом запросе укажите пустую строку, а для последующих запросов укажите `searchCursor` из последнего полученного `V2TIMGroupMemberSearchResult`. |

### Класс результата поиска члена группы

Класс результата поиска сообщений — это `V2TIMGroupMemberSearchResult` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupMemberSearchResult.html) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMGroupMemberSearchResult.html) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMGroupMemberSearchResult.html) / [C++](https://im.sdk.qcloud.com/doc/en/structV2TIMGroupMemberSearchResult.html)). Параметры описаны ниже:

| Параметр | Значение | Описание |
| --- | --- | --- |
| isFinished | Завершён ли поиск | Возвращены ли все члены группы, соответствующие критериям поиска. |
| totalCount | Общее количество результатов поиска | Общее количество членов группы, соответствующих критериям поиска. |
| nextCursor | Курсор для продолжения получения данных | Курсор поиска для следующего облачного поиска. |
| memberList | Список членов | Список членов группы, возвращённый текущим облачным поиском. |

Ниже приведен пример кода:

Java

Swift

Objective-C

C++

```
V2TIMGroupMemberSearchParam searchParam = new V2TIMGroupMemberSearchParam();searchParam.setKeywordList(keywordList);searchParam.setKeywordListMatchType(param.V2TIM_KEYWORD_LIST_MATCH_TYPE_OR);searchParam.setGroupIDList(groupIDList);searchParam.setSearchCount(20);searchParam.setSearchCursor("");V2TIMManager.getGroupManager().searchCloudGroupMembers(searchParam, new V2TIMValueCallback<V2TIMGroupMemberSearchResult>() {  @Override  public void onSuccess(V2TIMGroupMemberSearchResult groupMemberSearchResult) {      // Search Group Member succ  }  @Override  public void onError(int code, String desc) {      // Search Group Member failed  }});
```

```
let param = V2TIMGroupMemberSearchParam()param.keywordList = ["keyword1", "keyword2"];param.keywordListMatchType = .V2TIM_KEYWORD_LIST_MATCH_TYPE_OR;param.groupIDList= ["groupID"];param.searchCount = 20;param.searchCursor = "";V2TIMManager.shared.searchCloudGroupMembers(searchParam: param) { searchResult in    // Search Group Member succ} fail: { code, desc in    // Search Group Member failed}
```

```
V2TIMGroupMemberSearchParam *param = [[V2TIMGroupMemberSearchParam alloc] init];param.keywordList = @[@"keyword1", @"keyword2"];param.keywordListMatchType = V2TIM_KEYWORD_LIST_MATCH_TYPE_OR;param.groupIDList= @[@"groupID"];param.searchCount = 20;param.searchCursor = "";[[V2TIMManager sharedInstance] searchCloudGroupMembers:param succ:^(V2TIMGroupMemberSearchResult *searchResult) {    // Search Group Member succ} fail:^(int code, NSString *desc) {    // Search Group Member failed}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMGroupMemberSearchParam param;param.keywordList = keywordList;param.keywordListMatchType = V2TIM_KEYWORD_LIST_MATCH_TYPE_OR;param.groupIDList = groupIDList;param.searchCount = 20;param.searchCursor = "";auto callback = new ValueCallback<V2TIMGroupMemberSearchResult>{};callback->SetCallback(    [=](const V2TIMGroupMemberSearchResult& groupMemberSearchResult) {        // Search Group Member succ        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Search Group Member failed        delete callback;    });V2TIMManager::GetInstance()->GetGroupManager()->SearchCloudGroupMembers(param, callback);
```


---
*Источник: [https://trtc.io/document/67837](https://trtc.io/document/67837)*

---
*Источник (EN): [cloud-search-group-members.md](./cloud-search-group-members.md)*

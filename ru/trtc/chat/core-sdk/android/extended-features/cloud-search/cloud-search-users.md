# Поиск облачных пользователей

## Описание

Вы можете искать облачных пользователей по идентификатору пользователя, нику, полу и другой информации, чтобы быстро найти требуемый профиль пользователя. Эта функция подходит для сценариев, когда необходимо найти конкретную информацию о пользователе, такую как поиск пользователей для добавления в друзья в знакомых социальных сценах или поиск пользователей для отслеживания в незнакомых социальных сценах.

> **Примечание:** Функция поиска облачных пользователей поддерживается только версией 8.4 и выше. Функция перевода сообщений доступна только для клиентов Pro Plus и Enterprise. Она может быть использована после [приобретения Pro Plus и Enterprise](https://console.trtc.io/subscription/buy/chat?packType=pro&language=en); бесплатная пробная версия поддерживает [определенный лимит бесплатной пробы](https://www.tencentcloud.com/document/product/1047/67651#d1113f0d-47e8-4211-82c0-00d2efb72586), действительный в течение одного месяца. Если эта услуга не активирована, вызов интерфейса вернет код ошибки 60020.

## Интерфейс поиска облачных пользователей

Вызовите интерфейс `searchUsers` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMUserSearchParam.html) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager.html#v2timmanager.searchusers(param:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMManager.html#a978df4d80011f4da38dc80f8ab217f48) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMManager.html#a6846339829066fec9fc4d6d72e01d5a0)) для поиска информации о пользователях в облаке. Этот интерфейс возвращает информацию о пользователях, хранящуюся в облаке, включая информацию о друзьях и не-друзьях. Вы можете вызвать интерфейс `checkFriend` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMFriendshipManager.html#a96bb74f3bbd1aef147ec914a81104d11) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Friendship.html#v2timmanager.checkfriend(useridlist:checktype:succ:fail:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Friendship_08.html#aad1b09fab6523d9a36147b4ed4efac67) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMFriendshipManager.html#a90046f679ca31dedc00bbecff065538f))

чтобы определить, является ли пользователь другом.

Параметры `V2TIMUserSearchParam` выглядят следующим образом:

| Параметр | Значение | Описание |
| --- | --- | --- |
| keywordList | Список ключевых слов | Может содержать до пяти ключевых слов. Ключевое слово будет автоматически совпадать с идентификатором пользователя и ником. |
| keywordListMatchType | Тип соответствия списка ключевых слов | Вы можете установить поиск с логикой "ИЛИ" или "И". Значения — `V2TIM_KEYWORD_LIST_MATCH_TYPE_OR` и `V2TIM_KEYWORD_LIST_MATCH_TYPE_AND` соответственно. По умолчанию используется логика "ИЛИ". |
| gender | Пол пользователя | Если не установлено, по умолчанию возвращаются как мужчины, так и женщины. |
| minBirthday | Минимальная дата рождения пользователя | Если не установлено, значение по умолчанию — 0. |
| maxBirthday | Максимальная дата рождения пользователя | Если не установлено, по умолчанию возвращаются все пользователи с датой рождения >= minBirthday. |
| searchCount | Количество поиска | Должно быть больше 0, максимально поддерживается 100, по умолчанию 20. |
| searchCursor | Курсор поиска | Начальная позиция, заполните пустую строку в первый раз и заполните `searchCursor` из последнего возвращенного `V2TIMUserSearchResult` для последующих выборок. |

### Класс результатов поиска пользователей

Класс результатов поиска сообщений — это `V2TIMUserSearchResult` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMUserSearchResult.html) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMUserSearchResult.html) / [Objective-C](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMUserSearchResult.html) / [C++](https://im.sdk.qcloud.com/doc/en/structV2TIMUserSearchResult.html)). Параметры описаны ниже:

| Параметр | Значение | Описание |
| --- | --- | --- |
| isFinished | Завершен ли поиск | Были ли возвращены все пользователи, соответствующие критериям поиска. |
| totalCount | Всего результатов поиска | Общее количество пользователей, соответствующих критериям поиска. |
| nextCursor | Продолжить курсор извлечения | Курсор поиска для следующего облачного поиска. |
| userList | Список пользователей | Список пользователей, возвращаемый при текущем облачном поиске. |

Ниже приведен пример кода:

Java

Swift

Objective-C

C++

```
V2TIMUserSearchParam searchParam = new V2TIMUserSearchParam();searchParam.setKeywordList(keywordList);searchParam.setKeywordListMatchType(param.V2TIM_KEYWORD_LIST_MATCH_TYPE_OR);searchParam.setSearchCount(20);searchParam.setSearchCursor("");V2TIMManager.getInstance().searchUsers(searchParam, new V2TIMValueCallback<V2TIMUserSearchResult>() {  @Override  public void onSuccess(V2TIMUserSearchResult userSearchResult) {      // search users succ  }  @Override  public void onError(int code, String desc) {      // search users failed  }});
```

```
let param = V2TIMUserSearchParam()param.gender = .V2TIM_GENDER_UNKNOWN;param.keywordList = ["keyword1", "keyword2"];param.keywordListMatchType = .V2TIM_KEYWORD_LIST_MATCH_TYPE_OR;param.searchCount = 20;param.searchCursor = "";V2TIMManager.shared.searchUsers(param: param) { searchResult in    // search users succ} fail: { code, desc in    // search users failed}
```

```
V2TIMUserSearchParam *param = [[V2TIMUserSearchParam alloc] init];param.gender = V2TIM_GENDER_UNKNOWN;param.keywordList = @[@"keyword1", @"keyword2"];param.keywordListMatchType = V2TIM_KEYWORD_LIST_MATCH_TYPE_OR;param.searchCount = 20;param.searchCursor = @"";[[V2TIMManager sharedInstance] searchUsers:param succ:^(V2TIMUserSearchResult *searchResult) {    // search users succ} fail:^(int code, NSString *desc) {    // search users failed}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMUserSearchParam searchParam;searchParam.keywordList = keywordList;param.keywordListMatchType = V2TIM_KEYWORD_LIST_MATCH_TYPE_OR;param.searchCount = 20;param.searchCursor = "";auto callback = new ValueCallback<V2TIMUserSearchResult>{};callback->SetCallback(    [=](const V2TIMUserSearchResult& userSearchResult) {        // search users succ        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // search users failed        delete callback;    });V2TIMManager::GetInstance()->SearchUsers(searchParam, callback);
```

---

*Источник: [https://trtc.io/document/67835](https://trtc.io/document/67835)*

---
*Источник (EN): [cloud-search-users.md](./cloud-search-users.md)*

# Поиск облачных сообщений

## Описание

Поиск облачных сообщений — это необходимая функция для повышения удобства пользователя приложения, которая позволяет пользователям быстро и удобно находить нужное содержимое из сложной информации. Она также может служить инструментом для операций, облегчая эффективное и лаконичное справочное руководство по связанному содержимому.

> **Примечание:** Функция поиска облачных сообщений поддерживается только версией 7.3.4358 и более поздними версиями. Функция поиска облачных сообщений доступна только для клиентов **Pro Plus и Enterprise** и может использоваться после [приобретения Pro Plus и Enterprise](https://console.trtc.io/subscription/buy/chat?packType=pro&language=en); версия Free Trial поддерживает [определённый лимит бесплатного пробного использования](https://www.tencentcloud.com/document/product/1047/67651#d1113f0d-47e8-4211-82c0-00d2efb72586), действительный в течение одного месяца. Если эта служба не активирована, вызов интерфейса вернёт код ошибки 60020.

## Класс поиска сообщений

### Класс параметров поиска сообщений

Классом параметров поиска сообщений является `V2TIMMessageSearchParam` ([Android](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchParam.html)/[iOS & Mac](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMMessageSearchParam.html)/[Windows](https://im.sdk.qcloud.com/doc/en/structV2TIMMessageSearchParam.html)). При поиске сообщений SDK будет выполнять различные логики поиска на основе параметров этого объекта.

Параметры `V2TIMMessageSearchParam` описаны далее:

| Параметр | Значение | Описание |
| --- | --- | --- |
| keywordList | Список ключевых слов | Может содержать до пяти ключевых слов. Если отправитель сообщения и тип сообщения не указаны, список ключевых слов должен быть установлен; в других случаях он может быть пустым. |
| keywordListMatchType | Тип соответствия списка ключевых слов | Можно установить поиск с логикой «OR» или «AND». Значения: `V2TIM_KEYWORD_LIST_MATCH_TYPE_OR` и `V2TIM_KEYWORD_LIST_MATCH_TYPE_AND` соответственно. По умолчанию используется логика «OR». |
| senderUserIDList | Поиск сообщений, отправленных указанным userID | Поддерживается до пяти. |
| messageTypeList | Набор типов сообщений для поиска | Если оставить пусто, будет выполняться поиск всех поддерживаемых типов сообщений (сообщения `V2TIMFaceElem` и `V2TIMGroupTipsElem` не подлежат поиску). Другие типы см. в `V2TIMElemType` ([Android](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessage.html#a00455865d1a14191b8c612252bf20a1c)/[iOS & Mac](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#a849af0e4698e8db9f227f9c8e54215b8)/[Windows](https://im.sdk.qcloud.com/doc/en/V2TIMMessage_8h.html#a6854ecfbc6f3b65ed381d8a2e14e2377)). |
| conversationID | Поиск «всех диалогов» или «указанного диалога» | Если `conversationID` пусто, осуществляется поиск по всем сеансам; если `conversationID` не пусто, осуществляется поиск в указанном сеансе. |
| searchTimePosition | Время начала поиска | По умолчанию 0 (поиск с текущего момента). Временная метка UTC в секундах. |
| searchTimePeriod | Прошедший период времени, начиная с времени начала | По умолчанию 0 (неограниченный временной диапазон). 24 x 60 x 60 представляет прошедший день в секундах. |
| searchCount | Количество результатов поиска | Количество поисков, поддерживает до 100. |
| searchCursor | Курсор поиска | Начальная позиция, при первом обращении введите пустую строку, при последующих обращениях введите `searchCursor` из последнего возвращённого `V2TIMMessageSearchResult`. |

### Класс результатов поиска сообщений

Классом результатов поиска сообщений является `V2TIMMessageSearchResult`([Android](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchResult.html)/[iOS & Mac](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMMessageSearchResult.html)/[Windows](https://im.sdk.qcloud.com/doc/en/structV2TIMMessageSearchResult.html)). Параметры описаны далее:

| Параметр | Значение | Описание |
| --- | --- | --- |
| totalCount | Общее количество элементов результатов поиска | Если осуществляется поиск в конкретном сеансе, будет возвращено общее количество сообщений, соответствующих критериям поиска; если осуществляется поиск по всем сеансам, будет возвращено общее количество сеансов, содержащих сообщения, соответствующие критериям поиска. |
| messageSearchResultItems | Список результатов поиска | Если осуществляется поиск в конкретном сеансе, возвращённый список результатов будет содержать только результаты из этого сеанса; если осуществляется поиск по всем сеансам, сообщения, соответствующие критериям поиска, будут сгруппированы по ID сеанса и результаты группировки будут возвращены с постраничной разбивкой. |
| searchCursor | Курсор для продолжения загрузки | Курсор, необходимый для продолжения при вызове API поиска |

Здесь `messageSearchResultItems` — это список, содержащий объекты `V2TIMMessageSearchResultItem`([Android](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageSearchResultItem.html)/[iOS & Mac](https://im.sdk.qcloud.com/doc/en/interfaceV2TIMMessageSearchResultItem.html)/[Windows](https://im.sdk.qcloud.com/doc/en/structV2TIMMessageSearchResultItem.html)), параметры которых описаны далее:

| Параметр | Значение | Описание |
| --- | --- | --- |
| conversationID | ID сеанса | - |
| messageCount | Количество сообщений | Общее количество сообщений, соответствующих критериям, найденных в текущем сеансе. |
| messageList | Список сообщений, соответствующих критериям поиска | Если осуществляется поиск в конкретном сеансе, `messageList` содержит список всех сообщений, соответствующих критериям поиска в этом сеансе. Если осуществляется поиск по всем сеансам, количество сообщений в `messageList` может иметь одно из двух значений: Если количество сообщений, найденных в сеансе, > 1, то `messageList` пусто, и на пользовательском интерфейсе можно отобразить «{`messageCount`} соответствующих записей». Если количество сообщений, найденных в сеансе, = 1, то `messageList` содержит найденное сообщение, и его можно отобразить на пользовательском интерфейсе и выделить ключевые слова поиска. |

## Поиск сообщений во всех сеансах

Когда пользователь вводит ключевые слова в поле поиска для поиска сообщений, можно вызвать `searchCloudMessages`([Android](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a16a4a38b3f08bf7707d949ba9674102f)/[iOS and Mac](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#ab672a5d549893b7e22c555593be40322)/[Windows](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#ab01326d278755b0968ca4c0bdb98d137)) для поиска сообщений.

Если требуется поиск в пределах всех сеансов, нужно просто оставить `conversationID` в `V2TIMMessageSearchParam` неустановленным или установить пустое значение.

Ниже приведён пример кода:

Android

iOS & Mac

Windows

```
List<String> keywordList = new ArrayList<>();keywordList.add("abc");keywordList.add("123");V2TIMMessageSearchParam searchParam = new V2TIMMessageSearchParam();// Set the keyword for the searchsearchParam.setKeywordList(keywordList);// Search for 20 data entriessearchParam.setSearchCount(20);// Start searching from the latest sessionsearchParam.setSearchCursor("");// Start searching from the current timesearchParam.setSearchTimePosition(0);// Search for messages within 10 minutessearchParam.setSearchTimePeriod(600);V2TIMManager.getMessageManager().searchCloudMessages(searchParam,newV2TIMValueCallback<V2TIMMessageSearchResult>() {    @Override    public void onSuccess(V2TIMMessageSearchResult v2TIMMessageSearchResult) {      // Data found successfully    }        @Override    public void onError(int code, String desc) {      // Failed to find the data    }});
```

```
V2TIMMessageSearchParam *param = [[V2TIMMessageSearchParam alloc] init];// Set the keyword for the searchparam.keywordList = @[@"abc", @"123"];param.messageTypeList = nil;param.conversationID = nil;param.searchTimePosition = 0;param.searchTimePeriod = 0;// Search for 20 data entriesparam.searchCount = 20;// Start searching from the latest sessionparam.searchCursor = @"";[V2TIMManager.sharedInstance searchCloudMessages:paramsucc:^(V2TIMMessageSearchResult *searchResult) {    // The search was successful, and the search results are returned in searchResult} fail:^(int code, NSString *desc) {    // Failed to find the data}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;        ValueCallback() = default;    ~ValueCallback() override = default;        void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {      success_callback_ = std::move(success_callback);      error_callback_ = std::move(error_callback);    }        void OnSuccess(const T& value) override {      if (success_callback_) {        success_callback_(value);      }    }    void OnError(int error_code, const V2TIMString& error_message) override {      if (error_callback_) {        error_callback_(error_code, error_message);      }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMMessageSearchParam searchParam;// Set the keyword for the searchsearchParam.keywordList.PushBack("abc");searchParam.keywordList.PushBack("123");// Search for 20 data entriessearchParam.searchCount = 20;// Start searching from the latest sessionsearchParam.searchCursor = "";auto callback = new ValueCallback<V2TIMMessageSearchResult>{};callback->SetCallback(    [=](const V2TIMMessageSearchResult& messageSearchResult) {      // Data found successfully      delete callback;    },    [=](int error_code, const V2TIMString& error_message) {      // Failed to find the data      delete callback;    });V2TIMManager::GetInstance()->GetMessageManager()->SearchCloudMessages(searchParam, callback);
```

## Поиск сообщений в указанном сеансе

Когда пользователь вводит ключевые слова в поле поиска для поиска сообщений, можно вызвать `searchCloudMessages` ([Android](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a16a4a38b3f08bf7707d949ba9674102f)/[iOS and Mac](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#ab672a5d549893b7e22c555593be40322)/[Windows](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#ab01326d278755b0968ca4c0bdb98d137)) для поиска сообщений.

Ниже приведён пример кода:

Android

iOS & Mac

Windows

```
List<String> keywordList = new ArrayList<>();keywordList.add("abc");keywordList.add("123");V2TIMMessageSearchParam searchParam = new V2TIMMessageSearchParam();// Search for one-to-one messages with the 'user1' usersearchParam.setConversationID("c2c_user1");// Set the keyword for the searchsearchParam.setKeywordList(keywordList);// Search for 20 data entriessearchParam.setSearchCount(20);// Start searching from the latest sessionsearchParam.setSearchCursor("");// Start searching from the current timesearchParam.setSearchTimePosition(0);// Search for messages within 10 minutessearchParam.setSearchTimePeriod(600);V2TIMManager.getMessageManager().searchCloudMessages(searchParam,newV2TIMValueCallback<V2TIMMessageSearchResult>() {    @Override    public void onSuccess(V2TIMMessageSearchResult v2TIMMessageSearchResult) {      // Data found successfully    }        @Override    public void onError(int code, String desc) {      // Failed to find the data    }});
```

```
V2TIMMessageSearchParam *param = [[V2TIMMessageSearchParam alloc] init];// Set the keyword for the searchparam.keywordList = @[@"abc", @"123"];param.messageTypeList = nil;// Search for one-to-one messages with the 'user1' userparam.conversationID = @"c2c_user1";param.searchTimePosition = 0;param.searchTimePeriod = 0;// Search for 20 data entriesparam.searchCount = 20;// Start searching from the latest sessionparam.searchCursor = @"";[V2TIMManager.sharedInstance searchCloudMessages:paramsucc:^(V2TIMMessageSearchResult *searchResult) {    // The search was successful, and the search results are returned in searchResult} fail:^(int code, NSString *desc) {    // Failed to find the data}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;        ValueCallback() = default;    ~ValueCallback() override = default;        void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {      success_callback_ = std::move(success_callback);      error_callback_ = std::move(error_callback);    }        void OnSuccess(const T& value) override {      if (success_callback_) {        success_callback_(value);      }    }    void OnError(int error_code, const V2TIMString& error_message) override {      if (error_callback_) {        error_callback_(error_code, error_message);      }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMMessageSearchParam searchParam;// Search for one-to-one messages with the 'user1' usersearchParam.conversationID = "c2c_user1";// Set the keyword for the searchsearchParam.keywordList.PushBack("abc");searchParam.keywordList.PushBack("123");// Search for 20 data entriessearchParam.searchCount = 20;// Start searching from the latest sessionsearchParam.searchCursor = "";auto callback = new ValueCallback<V2TIMMessageSearchResult>{};callback->SetCallback(    [=](const V2TIMMessageSearchResult& messageSearchResult) {      // Data found successfully      delete callback;    },    [=](int error_code, const V2TIMString& error_message) {      // Failed to find the data      delete callback;    });V2TIMManager::GetInstance()->GetMessageManager()->SearchCloudMessages(searchParam, callback);
```

## Типичные варианты использования поиска

В обычном программном обеспечении для общения пользовательский интерфейс поиска обычно отображается следующим образом:

| Рисунок 1. История чата | Рисунок 2. Больше истории чата | Рисунок 3. Сообщения в указанном сеансе |
| --- | --- | --- |
| ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/187560add19511efb1a552540099c741.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/187885a3d19511efa2ff52540044a08e.png) | ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/186b4b50d19511ef81865254005ef0f7.png) |

Далее описывается, как реализовать вышеперечисленные варианты использования через API поиска Chat SDK.

### Отображение последних активных сеансов

Как показано на рисунке 1, в нижней части отображается список последних трёх сеансов, к которым принадлежат найденные сообщения. Способ реализации следующий:

1. Установка параметров поиска `V2TIMMessageSearchParam`
  - `conversationID` установлен в `null`, что означает поиск сообщений из всех сеансов.
  - `searchCursor` установлен в "", что означает поиск последних данных.
  - `searchCount` установлен в 3, что означает возврат количества самых последних сеансов, обычно показывающих 3 записи на пользовательском интерфейсе.
2. Обработка результатов обратного вызова поиска `V2TIMMessageSearchResult`
  - `totalCount` указывает количество всех сеансов, к которым принадлежат найденные сообщения.
  - Список `messageSearchResultItems` содержит последние 3 сеанса (в соответствии с параметром `searchCount`). `messageCount` из `V2TIMMessageSearchResultItem` указывает общее количество найденных сообщений в текущем сеансе;
  - Если количество найденных сообщений > 1, то `messageList` будет пусто. На пользовательском интерфейсе можно отобразить «4 соответствующие записи чата», где 4 представляет `messageCount`.
  - Если количество найденных сообщений = 1, то `messageList` — это сообщение, соответствующее критериям. На пользовательском интерфейсе можно отобразить содержимое сообщения и выделить ключевое слово поиска, например, «test» на изображении в разделе [Типичные варианты использования поиска](#004e9efb-a26e-4ce3-bf9f-871253244baf).

Ниже приведён пример кода:

Android

iOS & Mac

Windows

```
List<String> keywordList = new ArrayList<>();keywordList.add("test");V2TIMMessageSearchParam v2TIMMessageSearchParam = new V2TIMMessageSearchParam();// Setting `conversationID` to `null` is to search for messages in all sessions and the results will be classified by sessionv2TIMMessageSearchParam.setConversationID(null);v2TIMMessageSearchParam.setKeywordList(keywordList);v2TIMMessageSearchParam.setSearchCursor("");v2TIMMessageSearchParam.setSearchCount(3);V2TIMManager.getMessageManager().searchCloudMessages(v2TIMMessageSearchParam, newV2TIMValueCallback<V2TIMMessageSearchResult>() {    @Override    public void onSuccess(V2TIMMessageSearchResult v2TIMMessageSearchResult) {      // Total number of matched sessions to which messages belong      int totalCount = v2TIMMessageSearchResult.getTotalCount();      // Last three messages classified by session      List<V2TIMMessageSearchResultItem> resultItemList = v2TIMMessageSearchResult.getMessageSearchResultItems();      for (V2TIMMessageSearchResultItem resultItem : resultItemList) {        // Session ID        String conversationID = resultItem.getConversationID();        // Total number of messages matching the session        int totalMessageCount = resultItem.getMessageCount();        // Message list: If totalMessageCount > 1, this list is empty; if totalMessageCount = 1, this list Element (XML) is this message        List<V2TIMMessage> v2TIMMessageList = resultItem.getMessageList();      }    }        @Override    public void onError(int code, String desc) {    }});
```

```
V2TIMMessageSearchParam *param = [[V2TIMMessageSearchParam alloc] init];param.keywordList = @[@"test"];// Setting `conversationID` to `nil` is to search for messages in all sessions and the results will be classified by sessionparam.conversationID = nil;param.searchCursor = @"";param.searchCount = 3;[V2TIMManager.sharedInstance searchCloudMessages:param succ:^(V2TIMMessageSearchResult *searchResult) {    // Total number of matched conversations to which messages belong    NSInteger totalCount = searchResult.totalCount;    // Last three messages classified by session    NSArray<V2TIMMessageSearchResultItem *> *messageSearchResultItems = searchResult.messageSearchResultItems;    for (V2TIMMessageSearchResultItem *searchItem in messageSearchResultItems) {      // Conversation ID      NSString *conversationID = searchItem.conversationID;      // Total number of messages matching the session      NSUInteger messageCount = searchItem.messageCount;      // Message list      NSArray<V2TIMMessage *> *messageList = searchItem.messageList ?: @[];    }} fail:^(int code, NSString *desc) {    // fail}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;        ValueCallback() = default;    ~ValueCallback() override = default;        void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {      success_callback_ = std::move(success_callback);      error_callback_ = std::move(error_callback);    }        void OnSuccess(const T& value) override {      if (success_callback_) {      success_callback_(value);      }    }    void OnError(int error_code, const V2TIMString& error_message) override {      if (error_callback_) {      error_callback_(error_code, error_message);      }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMMessageSearchParam searchParam;// Setting conversationID to null searches for messages in all sessions, and results will be classified by sessionsearchParam.conversationID = "";searchParam.keywordList.PushBack("test");searchParam.searchCursor = "";searchParam.searchCount = 3;auto callback = new ValueCallback<V2TIMMessageSearchResult>{};callback->SetCallback(    [=](const V2TIMMessageSearchResult& messageSearchResult) {      // Total number of matched sessions to which messages belong      uint32_t totalCount = messageSearchResult.totalCount;      // Last three messages classified by session      V2TIMMessageSearchResultItemVector messageSearchResultItems =      messageSearchResult.messageSearchResultItems;      for (size_t i = 0; i < messageSearchResultItems.Size(); ++i) {        // Session ID        V2TIMString conversationID = messageSearchResultItems[i].conversationID;        // Total number of messages matching the session        uint32_t messageCount = messageSearchResultItems[i].messageCount;        // Message list: If messageCount > 1, this list is empty; if messageCount = 1, this list Element (XML) is this message        V2TIMMessageVector messageList = messageSearchResultItems[i].messageList;      }      delete callback;      },      [=](int error_code, const V2TIMString& error_message) {        // Failed to find the data        delete callback;    });V2TIMManager::GetInstance()->GetMessageManager()->SearchCloudMessages(searchParam, callback);
```

### Отображение списка сеансов, к которым принадлежат найденные сообщения

При нажатии на кнопку «Больше записей чата» на рисунке 1 в разделе [Типичные варианты использования поиска](#004e9efb-a26e-4ce3-bf9f-871253244baf) вы перейдёте на рисунок 2, отображающий список сеансов, к которым принадлежат все найденные сообщения. Описание параметров поиска и результатов аналогично сценарию, описанному выше.

Чтобы предотвратить чрезмерное потребление памяти, мы настоятельно рекомендуем загружать список сеансов постранично. Например, загрузку по страницам, отображение 10 результатов сеансов на странице, параметр поиска `V2TIMMessageSearchParam` может быть установлен следующим образом:

1. При первом вызове: установите `searchCount` = 10, `searchCursor` = "". Вызовите `searchCloudMessages`, чтобы получить результаты поиска сообщений, проанализируйте и отобразите их на главной странице, и получите общее количество сеансов `totalCount` и курсор для следующего запроса `searchCursor` из обратного вызова результата.
2. Когда интерфейс почти прокручен до дна, продолжайте загружать данные следующей страницы на основе курсора `searchCursor` из результатов предыдущего запроса.

Ниже приведён пример кода:

Android

iOS & Mac

Windows

```
......// Logging the search cursorString searchCursor = "";......private void searchConversation(String cursor) {    List<String> keywordList = new ArrayList<>();    keywordList.add("test");    V2TIMMessageSearchParam v2TIMMessageSearchParam = new V2TIMMessageSearchParam();    v2TIMMessageSearchParam.setConversationID(null);    v2TIMMessageSearchParam.setKeywordList(keywordList);    v2TIMMessageSearchParam.setSearchCount(10);    v2TIMMessageSearchParam.setSearchCursor(cursor);    V2TIMManager.getMessageManager().searchCloudMessages(v2TIMMessageSearchParam, newV2TIMValueCallback<V2TIMMessageSearchResult>() {      @Override      public void onSuccess(V2TIMMessageSearchResult v2TIMMessageSearchResult) {        // Total number of matched sessions to which messages belong        int totalCount = v2TIMMessageSearchResult.getTotalCount();        // Cursor for the next page        searchCursor = v2TIMMessageSearchResult.getSearchCursor();        // Information of messages classified by session        List<V2TIMMessageSearchResultItem> resultItemList = v2TIMMessageSearchResult.getMessageSearchResultItems();        for (V2TIMMessageSearchResultItem resultItem : resultItemList) {          // Session ID          String conversationID = resultItem.getConversationID();          // Total number of messages matching the session          int totalMessageCount = resultItem.getMessageCount();          // Message list: If totalMessageCount > 1, this list is empty; if totalMessageCount = 1, this list Element (XML) is this message          List<V2TIMMessage> v2TIMMessageList = resultItem.getMessageList();        }      }          @Override      public void onError(int code, String desc) {      }    });  }// Load the next pagepublic void loadMore() {    searchConversation(searchCursor);}
```

```
......// Logging the search cursorNSString *searchCursor = @"";......- (void)searchConversation:(NSString *)cursor {    V2TIMMessageSearchParam *param = [[V2TIMMessageSearchParam alloc] init];    param.keywordList = @[@"test"];    param.conversationID = nil;    param.searchCursor = cursor;    param.searchCount = 10;    [V2TIMManager.sharedInstance searchCloudMessages:param succ:^(V2TIMMessageSearchResult *searchResult) {      // Total number of matched sessions to which messages belong      NSUInteger totalCount = searchResult.totalCount;      // Cursor for the next page      searchCursor = searchResult.searchCursor;      // Information of messages classified by session      NSArray<V2TIMMessageSearchResultItem *> *messageSearchResultItems = searchResult.messageSearchResultItems;      for (V2TIMMessageSearchResultItem *searchItem in messageSearchResultItems) {        // Session ID        NSString *conversationID = searchItem.conversationID;        // Total number of messages matching the session        NSUInteger totalMessageCount = searchItem.messageCount;        // Message list: If totalMessageCount > 1, this list is empty; if totalMessageCount = 1, this list

---
*Источник (EN): [cloud-search-messages.md](./cloud-search-messages.md)*

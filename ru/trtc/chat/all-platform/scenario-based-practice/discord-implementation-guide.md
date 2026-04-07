# Руководство по внедрению Discord

## Обзор Discord

Discord — это бесплатное приложение для обмена сообщениями в реальном времени и платформа цифрового распределения, разработанная для сообществ. Это позволяет пользователям в области игр, образования и бизнеса общаться друг с другом через сообщения, изображения, видео и аудио в канале чата приложения.

## Концепции Discord

### Сервер

В Discord существует тип группового чата, который отличается от обычных групп в программах обмена сообщениями и называется серверами (аналогично сообществам). Владельцы серверов могут создавать свои сообщества на серверах.

### Канал

На серверах вы можете создавать каналы чата, включая голосовые и текстовые каналы. Голосовой канал можно использовать для трансляции игр, общения и т. д. Каналы можно настроить для интеграции различных разрешений с группами идентичности, что делает систему сообществ Discord более разнообразной.

### Потоки

Пользователи могут обсуждать конкретные темы в потоках.

## Подготовка

### Создание приложений Tencent Cloud Chat

Это руководство основано на Tencent Cloud Chat. Поэтому вам необходимо создать приложение в [консоли Tencent Cloud Chat](https://console.trtc.io/). См. рисунок ниже.

После успешного создания приложения вы можете просмотреть основную информацию приложения на [странице основной информации](https://console.trtc.io/chat) приложения в консоли Chat.

### Изучение связанной конфигурации и возможностей

Для использования Tencent Cloud Chat при реализации функций Discord вам необходимо предварительно ознакомиться с основными концепциями, связанными с Tencent Cloud Chat, и некоторыми правильными терминами, которые будут упомянуты далее в этом руководстве, включая, но не ограничиваясь следующим:

- SDKAppID: Tencent Cloud Chat назначает SDKAppID для каждого приложения. SDKAppID приложения можно просмотреть на странице сведений приложения после создания приложения в консоли и используется при инициализации SDK Chat и расчёте билетов входа пользователя. Дополнительные сведения см. в разделе UI SDK [Инициализация](https://intl.cloud.tencent.com/document/product/1047/47968) и [Вход](https://intl.cloud.tencent.com/document/product/1047/47971).
- Key: Ключ приложения можно просмотреть на странице сведений приложения в консоли Tencent Cloud Chat и использовать для расчёта билетов входа SDK для пользователей.
- Учётная запись пользователя: Только пользователи с учётными записями Tencent Cloud Chat могут войти в Tencent Cloud Chat. Когда пользователь успешно [войдёт](https://intl.cloud.tencent.com/document/product/1047/47971) через SDK клиента, сервер Chat автоматически создаёт учётную запись Chat для пользователя. Кроме того, вы можете использовать серверный API, предоставляемый Chat, для [импорта пользователя в систему пользователей Chat](https://intl.cloud.tencent.com/document/product/1047/34953).
- Группа: На данный момент Chat предлагает [пять типов групп](https://intl.cloud.tencent.com/document/product/1047/33529) для различных сценариев, в которых пользователи могут отправлять и получать сообщения.
- Конфигурация Webhook: Вы можете активно интегрировать предоставляемые Chat API клиента и сервера, и Chat будет автоматически возвращать необходимую информацию на ваш сервер при срабатывании специфической бизнес-логики. Всё, что вам нужно сделать, это просто завершить связанную конфигурацию в модуле [Конфигурация Webhook](https://console.trtc.io/chat/callback-setting) консоли Chat. Chat предоставляет различные конфигурации webhook и обеспечивает высокую надёжность событий webhook. Вы можете использовать webhooks для реализации различных пользовательских требований.
- Пользовательское поле: По умолчанию Tencent Cloud Chat предоставляет разработчикам поля, отвечающие большинству их потребностей. Он также предоставляет следующие пользовательские поля для каждого модуля, чтобы удовлетворить потребности пользователей в расширенных полях:
  - [Пользовательские поля пользователя](https://console.tencentcloud.com/im/user-data)
  - [Пользовательские поля друга](https://console.tencentcloud.com/im/friends-diy-vars)
  - [Пользовательские поля группы](https://console.tencentcloud.com/im/qun-setting)
  - [Пользовательские поля участника группы](https://console.tencentcloud.com/im/qun-setting)

> **Примечание:** Для использования пользовательских полей вы можете настроить их в консоли, а затем читать/писать их через SDK/API.

### Интеграция SDK клиента и сервера

Для реализации функций Discord вам необходимо интегрировать SDK Tencent Cloud Chat. Chat предоставляет разнообразные и удобные в использовании SDK и серверные API. Сообщения синхронизируются между клиентами, если вы входите в приложение с одним SDKAppID. Выберите подходящий SDK в соответствии с вашим сценарием требования к бизнесу и стеком технологий.

## Функции Discord

Как показано на рисунке выше, функции Discord включают серверы, каналы и потоки. Разные серверы используются для разного контента. Например, у нас есть сервер Honor of Kings и сервер Game for Peace. Вы можете создавать различные типы каналов на сервере, такие как текстовый канал, голосовой канал и канал уведомлений. Пользователи общаются друг с другом в каналах. Если у них есть дополнительные идеи по определённой теме, они могут создать поток для дальнейшего обсуждения. Далее будет показано, как реализовать эти ключевые функции Discord через Tencent Cloud Chat одну за другой.

> **Примечание:** **Для примеров кода мы используем клиент Android (Java SDK) в качестве примера. Для вызова API других изданий SDK см.** [Решение интеграции (без пользовательского интерфейса)](https://intl.cloud.tencent.com/document/product/1047/34306)**.**

### Сервер

#### Создание сервера

Анализ выявил следующие характеристики списка серверов Discord:

1. Серверы могут иметь огромное количество пользователей.
2. Пользователи в действительности не общаются друг с другом на серверах. Вместо этого они общаются только в каналах или потоках на сервере.
3. Исторические сообщения чата на серверах необходимо хранить на серверах роуминга.
4. Пользователи имеют свободный доступ к серверам.
5. Каналы можно создавать на серверах.

Хотя Chat предоставляет пять типов групп, только [группы сообщества](https://intl.cloud.tencent.com/document/product/1047/33529) соответствуют характеристикам серверов Discord. Группа сообщества Chat позволяет пользователям свободно присоединяться и отказываться, поддерживает до 100 000 участников и сохраняет историю сообщений. Чтобы присоединиться к группе, пользователь должен найти ID группы и отправить заявку, и заявка не требует одобрения администратором, прежде чем пользователь сможет присоединиться к группе.

Вы можете использовать API `createGroup` для создания сервера (группы). Обратите внимание, что тип группы должен быть Community, а [setSupportTopic](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupInfo.html#af97a85fc91302dbbdf0f6c0a0a022ccd) должен быть `true`, чтобы каналы могли быть созданы на сервере. Далее приведён образец кода:

```
V2TIMGroupInfo  groupinfo = new V2TIMGroupInfo();groupinfo.setGroupName("Test server");groupinfo.setSupportTopic(true);// Initial group membersList<V2TIMCreateGroupMemberInfo> memberList = new LinkedList<V2TIMCreateGroupMemberInfo>();// Other settings, such as the server profile photoV2TIMManager.getGroupManager().createGroup(groupinfo, memberList, new V2TIMValueCallback<String>() {            @Override            public void onError(int i, String s) {                // Creation failed            }            @Override            public void onSuccess(String s) {                // The server is created successfully, and the server ID is returned.            }});
```

После успешного вызова API ID сервера будет возвращён в обратный вызов `onSuccess`, который будет использован позже при создании канала на сервере.

> **Внимание:** Вы также можете использовать [API создания сервера](https://intl.cloud.tencent.com/document/product/1047/34895), предоставляемый Chat. Основные параметры выглядят следующим образом:
> 
> ```
> {
>     "Type": "Community", // Group type (required)
>     "Name": "TestCommunityGroup", // Group name (required)
>     "SupportTopic": 1// Whether the topic option is supported. Valid values: `1`: yes; `0`: no.
> }
> ```

#### Список серверов

На дальней левой стороне Discord находится список серверов, присоединённых текущим пользователем. Для сценария сообщества Tencent Cloud Chat предоставляет выделенный API для запроса списка серверов.

```
V2TIMManager.getGroupManager().getJoinedCommunityList(new V2TIMValueCallback<List<V2TIMGroupInfo>>() {            @Override            public void onSuccess(List<V2TIMGroupInfo> v2TIMGroupInfos) {                // The server list is got successfully, and the basic information of the server list is provided in the returned `List<V2TIMGroupInfo>`.            }            @Override            public void onError(int i, String s) {              // Failed to get the service list.            }});
```

Возвращённый [V2TIMGroupInfo](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupInfo.html) предоставляет основную информацию о сервере. Однако возвращённая информация о сервере не включает информацию, такую как количество непрочитанных сообщений и пользовательский статус. Чтобы достичь того же эффекта, что и в Discord, нам нужно использовать другие API, предоставляемые Chat, для реализации количества непрочитанных сообщений для списка серверов, что будет обсуждаться далее в документе.

#### Категории серверов

При создании сервера для него автоматически создаётся категория по умолчанию. После создания сервера вы можете создать новую категорию. В Tencent Cloud Chat сервер по сути является сообществом. Поэтому мы можем установить пользовательское поле для группы сообщества, чтобы реализовать функцию типа сервера. Чтобы использовать пользовательское поле группы, выполните следующие действия:

1. Включите пользовательское поле `key` в консоли.
2. Используйте SDK клиента или серверный API для чтения/записи пользовательского поля.

Установите пользовательское поле группы с помощью [серверного API](https://intl.cloud.tencent.com/document/product/1047/34962) и [SDK клиента](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#ad4ceef92975fa00c4a5dddc8f7e1edcf).

> **Внимание:** Функция группы сообщества доступна только в выпусках Pro, Pro Plus или Enterprise. Прежде чем установить пользовательское поле для группы сообщества, вам необходимо приобрести выпуск Pro, Pro Plus или Enterprise.

#### Отображение количества непрочитанных сообщений и пользовательского статуса для сервера

![image-20221205031412051](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1aba6e14134c11efbf645254007bbd8c.png)

![image-20221205031429070](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/1ac17e2c134c11efa2935254005ac0ca.png)

Как было упомянуто ранее, API для получения списка присоединённых серверов не возвращает информацию, такую как количество непрочитанных сообщений и статус сервера. Следует отметить, что нам не только необходимо получить эти данные, но и прослушивать изменение этих данных, чтобы вовремя обновить пользовательский интерфейс клиента. Поскольку сервер реализован группой сообщества Chat, а группа сообщества не генерирует беседы в Chat, нам необходимо подсчитать сумму непрочитанных сообщений во всех беседах в общих и закрытых каналах. Мы можем использовать API [getUnreadCount](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMTopicInfo.html#ac2e3266d20b348145d75079020ac50c7) из [V2TIMTopicInfo](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMTopicInfo.html) для получения количества непрочитанных сообщений общих каналов и использовать API [getConversation](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#a619aaff2bb5664e094d2341819b95096) для получения количества непрочитанных сообщений закрытых каналов (потому что закрытые каналы реализуются рабочими группами).

```
// Public channelsList<String> conversationIDList = new LinkedList();conversationIDList.add("GROUP_$GROUPID");V2TIMManager.getConversationManager().getConversationList(conversationIDList, new V2TIMValueCallback<List<V2TIMConversation>>() {            @Override            public void onError(int i, String s) {                // Failed to get the conversation information of the server            }            @Override            public void onSuccess(V2TIMConversationList List<V2TIMConversation>) {               // Got the conversation information of the server successfully            }});// Private channelsV2TIMManager.getGroupManager().getTopicInfoList(groupID, topicIDList, new V2TIMValueCallback<List<V2TIMTopicInfoResult>>() {                @Override                public void onSuccess(List<V2TIMTopicInfoResult> v2TIMTopicInfoResults) {                }                @Override                public void onError(int i, String s) {                }});
```

Чтобы реализовать функцию пользовательского статуса для серверов, мы можем использовать API [setConversationCustomData](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#ac11ca7227145e3f359f6a3473ed600a5) для установки данных пользовательской беседы сервера.

```
List<String> conversationIDList = new LinkedList();String customData = "Busy"V2TIMManager.getConversationManager().setConversationCustomData(conversationIDList, customData, new V2TIMValueCallback<List<V2TIMConversationOperationResult>>() {            @Override            public void onSuccess(List<V2TIMConversationOperationResult> v2TIMConversationOperationResults) {                // The custom group conversation data is set successfully            }            @Override            public void onError(int i, String s) {                // Failed to set the custom group conversation data            }});
```

Когда изменяются данные, связанные с беседой на сервере, клиент должен попытаться обновить отображение пользовательского интерфейса. Для прослушивания изменений в беседе на сервере Chat предоставляет соответствующую функцию прослушивателя событий [addConversationListener](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMConversationManager.html#a806534684e5d4d01b94126cd1397fee4). Эта функция обратного вызова будет срабатывать в следующих случаях:

1. Сообщения сервера добавляются, удаляются или изменяются.
2. Количество непрочитанных сообщений сервера изменяется.
3. Пользовательская информация сервера изменяется.
4. Сервер закреплён в верхней части.
5. Конфигурация получения сообщения сервера изменяется.
6. Метка сервера изменяется.
7. Группа сервера изменяется.
8. ...

```
V2TIMConversationListener conversationLister = new V2TIMConversationListener() {            @Override            public void onSyncServerStart() {            }            @Override            public void onSyncServerFinish() {            }            @Override            public void onSyncServerFailed() {            }            @Override            public void onNewConversation(List<V2TIMConversation> conversationList) {            }            @Override            public void onConversationChanged(List<V2TIMConversation> conversationList) {            }            @Override            public void onTotalUnreadMessageCountChanged(long totalUnreadCount) {            }            @Override            public void onConversationGroupCreated(String groupName, List<V2TIMConversation> conversationList) {            }            @Override            public void onConversationGroupDeleted(String groupName) {            }            @Override            public void onConversationGroupNameChanged(String oldName, String newName) {            }            @Override            public void onConversationsAddedToGroup(String groupName, List<V2TIMConversation> conversationList) {ã            }            @Override            public void onConversationsDeletedFromGroup(String groupName, List<V2TIMConversation> conversationList) {            }}V2TIMManager.getConversationManager().addConversationListener(conversationLister);
```

В заключение мы можем использовать API `getJoinedCommunityList` и `getConversationList` и обратный вызов `addConversationListener` для реализации функции Discord отображения списка серверов.

### Канал

Несколько каналов можно создавать на сервере. Как показано на рисунке ниже, четыре канала создаются под сервером, и эти четыре канала размещаются в двух категориях.

Пользователи могут приглашать других присоединиться к каналу и изменять основные параметры канала. Большинство чатов в Discord происходят в каналах, поэтому возможности каналов имеют наибольшее значение в Discord. Возможности каналов в Discord соответствуют возможностям тем в Tencent Cloud Chat. Группы сообщества Chat предоставляют возможность создавать темы в группах.

#### Каналы по умолчанию

При создании сервера Discord создаёт четыре канала по умолчанию для сервера. Tencent Cloud Chat может также реализовать такую функцию. Процесс выглядит следующим образом:

1. Уведомьте бизнес-сервер об успешном создании сервера через webhook [После создания группы](https://console.trtc.io/chat/callback-setting).
2. Бизнес-сторона определяет, является ли созданная группа группой сообщества, чтобы не повлиять на бизнес, связанный с другими группами.
3. [Создайте тему на сервере](https://intl.cloud.tencent.com/document/product/1047/49471) в зависимости от атрибутов сервера.

Параметры для создания темы на сервере выглядят следующим образом:

```
{    "GroupId": "@TGS#_@TGS#cQVLVHIM62CJ", // Group ID of the topic, which is required    "TopicId": "@TGS#_@TGS#cQVLVHIM62CJ@TOPIC#_TestTopic", // Custom topic ID, which is optional    "TopicName": "TestTopic", // Topic name, which is required    "From_Account": "1400187352", // Member creating the topic    "CustomString": "This is a custom string",// Custom string    "FaceUrl": "http://this.is.face.url", // (Optional) Topic profile photo URL    "Notification": "This is topic Notification", // (Optional) Topic notice    "Introduction": "This is topic Introduction" // (Optional) Topic introduction}
```

#### Создание канала

На клиенте Discord пользователи могут создавать каналы в разных категориях каналов, как показано на рисунке ниже:

Создание канала в Discord эквивалентно созданию темы в группе сообщества в Chat. При создании темы в Chat вы можете установить категорию и основную информацию темы.

Вы можете использовать API [createTopicInCommunity](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMGroupManager.html#a52eed1b07ad64a3aa3d3561d8cd147f0) для реализации связанных функций.

```
String groupID = "Server ID"V2TIMTopicInfo info = new V2TIMTopicInfo();info.setCustomString("{'categray':'Game','type':'text'}") // Set the channel category and type// Set the basic information for `V2TIMTopicInfo`V2TIMManager.getGroupManager().createTopicInCommunity(groupID, info, new V2TIMValueCallback<String>() {            @Override            public void onSuccess(String s) {                // Channel created successfully            }            @Override            public void onError(int i, String s) {                // Failed to create the channel            }});
```

При создании канала вы можете вызвать метод [V2TIMTopicInfo](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMTopicInfo.html) для установки информации о канале и вызвать API [setCustomString](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMTopicInfo.html#aad0cc8249c21c5ccae385fdfb8ba32ea) для установки категории и типа канала.

При создании канала вы можете указать, является ли он приватным. Приватный канал отличается от обычного канала:

1. Пользователи не присоединяются к приватному каналу после присоединения к серверу.
2. Пользователи могут присоединиться к приватному каналу только если их пригласил администратор сервера.

Поэтому мы можем использовать рабочую группу для реализации функции приватного канала. Однако информацию о приватных каналах, связанных с сервером, необходимо хранить на бизнес-стороне.

#### Типы каналов

При создании канала в Discord вы можете установить тип канала как голосовой или текстовый. Текстовый канал позволяет общаться на основе текста, эмодзи и изображений, а голосовой канал позволяет аудио/видео общение. Обратите внимание, что пользователь может находиться только в одном голосовом канале одновременно. Чтобы присоединиться к новому голосовому каналу, пользователь должен покинуть текущий присоединённый голосовой канал.

Обратите внимание на следующее:

1. При создании канала вам нужно установить тип канала. Найдите метод установки в разделе создания канала.
2. Когда пользователь присоединяется к голосовому каналу, система должна определить, находится ли пользователь уже в другом голосовом канале.
3. Пользователь может присоединиться только к одному голосовому каналу в одном приложении.
4. Tencent Cloud Chat в настоящее время не предоставляет API для запроса того, находится ли пользователь в голосовом канале и в каком голосовом канале. Эта часть данных должна поддерживаться на бизнес-стороне.

Что касается последнего пункта выше, разработчики могут использовать обратные вызовы присоединения и выхода из группы, предоставляемые Tencent Cloud Chat, для поддержания статусов голосовых каналов пользователей и хранения статусов на бизнес-стороне. Обратите внимание, что обратные вызовы, предоставляемые Tencent Cloud Chat, могут иметь задержки, что означает, что после того, как пользователь покидает один голосовой канал, пользователь может быть не в состоянии присоединиться к другому голосовому каналу в течение короткого периода времени. Поэтому, чтобы решить эту проблему, мы также можем использовать клиент для передачи в реальном времени статуса присоединения или выхода пользователя из голосового канала на бизнес-сервер.

#### Приглашение пользователя на канал

Есть три способа, которыми пользователь может присоединиться к каналу:

1. Быть приглашённым присоединиться к серверу другим пользователем. Когда пользователь присоединяется к серверу, пользователь присоединяется ко всем общественным каналам сервера.
2. Найти сервер и затем присоединиться к серверу.
3. Быть приглашённым администратором сервера присоединиться к приватному каналу.

В соответствии с характеристиками сообщества пользователям нужно только присоединиться к серверу, чтобы присоединиться к общественным каналам.

1. Поддерживает присоединение к серверу путём точного поиска по ID группы.
2. Поддерживает присоединение к серверу через приглашение.
3. Поддерживает активное применение присоединиться к серверу, и одобрение не требуется.

#### Настройка канала

Вы можете отключить звук канала или включить его и настроить уведомления для канала. Соответствующие API — это [setAllMute](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMTopicInfo.html#a13fbe06ce357215cfd7053954552030b) и [setGroupReceiveMessageOpt](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a2735427ac22485626aea278a9d465b3e) соответственно.

```
// Set the basic channel informationV2TIMManager.getGroupManager().setTopicInfo(topicInfo, new V2TIMCallback() {    @Override    public void onSuccess() {        // Configured successfully    }    @Override    public void onError(int i, String s) {        // Failed to configure    }});
```

```
//

---
*Источник (EN): [discord-implementation-guide.md](./discord-implementation-guide.md)*

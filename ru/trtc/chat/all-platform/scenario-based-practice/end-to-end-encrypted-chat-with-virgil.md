# Сквозное шифрованное общение с Virgil

### **Обзор**

Это решение должно быть реализовано приложением клиента на основе E3Kit компании Virgil Security и Tencent Cloud Chat Sdk. Ссылка на документацию E3Kit: [Virtual gild E3Kit|Virtual gild Security](https://developer.virgilsecurity.com/docs/e3kit/)

Ознакомьтесь с документацией [GroupEncryption-End-to-End-Encryption-E3Kit|Virtual Security](https://developer.virgilsecurity.com/docs/e3kit/end-to-end-encryption/group-chat/) перед чтением следующих решений, особенно с JWT токеном (JSON Web Token), созданием канала/созданием группы, шифрованием и расшифровкой сообщений.

Откройте приложение в консоли Virgil Security перед использованием. Этот продукт платный. Подробную информацию о ценах см. в разделе [Pricing|Virgin Security](https://virgilsecurity.com/pricing/).

![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3a01d1a6260d11ee909c525400cea498.png)

На диаграмме ниже показан высокоуровневый поток общения:

![img](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/39f08000260d11eea27e525400c56988.png)

### **Общий обзор реализации (пример: Android)**

### **Инициализация**

1. Инициализация Tencent Cloud imsdk

```
// 1. Получите `SDKAppID` из консоли Chat.// 2. Инициализируйте объект `config`.V2TIMSDKConfig config = new V2TIMSDKConfig();// 3. Укажите уровень вывода журнала.config.setLogLevel(V2TIMSDKConfig.V2TIM_LOG_INFO);// 4. Добавьте слушатель событий `V2TIMSDKListener`. `sdkListener` — это класс реализации `V2TIMSDKListener`. Если вам не нужно отслеживать события IM SDK, пропустите этот шаг.V2TIMManager.getInstance().addIMSDKListener(sdkListener);// 5. Инициализируйте IM SDK. Вы можете вызвать API входа сразу же после вызова этого API.V2TIMManager.getInstance().initSDK(context, sdkAppID, config);
```

2. Инициализация E3Kit, передача информации конфигурации консоли и генерация jwt. Соответствующая ссылка на документацию операции: [GenerateClientTokens-GetStarted-E3Kit | VirgilSecurity](https://developer.virgilsecurity.com/docs/e3kit/get-started/generate-client-tokens/)

Сервер генерирует jwt токен и отправляет его клиенту

```
// генерация jwt// App Key (вы получили этот ключ на панели управления Virgil)String appKeyBase64 = "MC4CAQAwBQYDK2VwBCIEINlK4BhgsijAbNmUqU6us0ZU9MGi+HxdYCA6TdZeHjR4";byte[] appKeyData = ConvertionUtils.base64ToBytes(appKeyBase64);// Криптографическая библиотека импортирует пару ключейVirgilCrypto crypto = new VirgilCrypto();VirgilKeyPair keyPair = crypto.importPrivateKey(appKeyData);// Инициализируйте подписчика токена доступа, который подписывает JWT пользователяVirgilAccessTokenSigner accessTokenSigner = new VirgilAccessTokenSigner();// Используйте ваши учетные данные приложения, полученные на панели управления Virgil:String appId = "be00e10e4e1f4bf58f9b4dc85d79c77a";String appKeyId = "70b447e321f3a0fd";TimeSpan ttl = TimeSpan.fromTime(1, TimeUnit.HOURS); // 1 час - время жизни JWT// Установите генератор JWT с необходимыми параметрами:JwtGenerator jwtGenerator =    new JwtGenerator(appId, keyPair.getPrivateKey(), appKeyId, ttl, accessTokenSigner);// Генерируйте JWT для пользователя// Помните, что вы должны предоставить каждому пользователю уникальный JWT.// Каждый JWT содержит уникальную идентичность пользователя (в этом случае — Alice).// Идентичность может быть любым значением: имя, электронная почта, некоторый идентификатор и т. д.String identity = "Alice";Jwt aliceJwt = jwtGenerator.generateToken(identity);// В результате вы получаете JWT пользователя, он выглядит так: "eyJraWQiOiI3MGI0NDdlMzIxZjNhMGZkIiwidHlwIjoiSldUIiwiYWxnIjoiVkVEUzUxMiIsImN0eSI6InZpcmdpbC1qd3Q7dj0xIn0.eyJleHAiOjE1MTg2OTg5MTcsImlzcyI6InZpcmdpbC1iZTAwZTEwZTRlMWY0YmY1OGY5YjRkYzg1ZDc5Yzc3YSIsInN1YiI6ImlkZW50aXR5LUFsaWNlIiwiaWF0IjoxNTE4NjEyNTE3fQ.MFEwDQYJYIZIAWUDBAIDBQAEQP4Yo3yjmt8WWJ5mqs3Yrqc_VzG6nBtrW2KIjP-kxiIJL_7Wv0pqty7PDbDoGhkX8CJa6UOdyn3rBWRvMK7p7Ak".// Вы можете предоставить пользователям JWT на этапе регистрации или авторизации.// Отправьте JWT клиенту.String jwtString = aliceJwt.stringRepresentation();
```

Клиент Android инициализирует E3Kit, tokenCallback — это jwt токен, возвращаемый выше сервером, а User1 — это идентификатор пользователя

```
// инициализация E3Kit// создать EThreeParams с обязательными параметрами// такими как identity, tokenCallback и contextEThreeParams params = new EThreeParams("User1",   tokenCallback,context);// инициализируйте E3Kit с помощью EThreeParamsEThree ethree = new EThree(params);
```

### **Вход пользователя**

1. Вызовите метод входа Tencent Cloud Chat Sdk для входа в учетную запись

```
String userID = "your user id";//Генерирование UserSig | Tencent CloudString userSig = "userSig from your server";V2TIMManager.getInstance().login(userID, userSig, new V2TIMCallback() {   @Override   public void onSuccess() {       Log.i("imsdk", "success");   }    @Override   public void onError(int code, String desc) {       // Следующие коды ошибок указывают на истечение срока действия `userSig`, и вам необходимо создать новый для повторного входа.       // 1. ERR_USER_SIG_EXPIRED (6206)       // 2. ERR_SVR_ACCOUNT_USERSIG_EXPIRED (70001)       // Примечание: не вызывайте API входа в случае других кодов ошибок; в противном случае IM SDK может войти в бесконечный цикл входа.       Log.i("imsdk", "failure, code:" + code + ", desc:" + desc);   }});
```

2. Вызовите метод eThree.register для регистрации пользователя на Virgil Security. Соответствующая ссылка на документацию операции: [UserAuthentication-E3Kit | VirgilSecurity](https://developer.virgilsecurity.com/docs/e3kit/user-authentication/)

> Примечание: пользователь im_ID и пользователь, зарегистрированный на Virgil Security_id должны быть одинаковыми

### **Начало одноранговой беседы**

1. Вызовите метод ethree.createRatchetChannel в E3Kit для создания сеанса «один на один» (User1 и User2), соответствующая ссылка на документацию операции: [https://developer.virgilsecurity.com/docs/e3kit/end-to-end-encryption/double-ratchet/?#create-channel](https://developer.virgilsecurity.com/docs/e3kit/end-to-end-encryption/double-ratchet/#create-channel)

User1 создает канал с User2

```
// создать одноранговый канальethree.createRatchetChannel(users.get("User2"))      .addCallback(new OnResultListener<RatchetChannel>() {          @Override public void onSuccess(RatchetChannel ratchetChannel) {              // Канал создан и сохранен локально!          }          @Override public void onError(@NotNull Throwable throwable) {              // Обработка ошибки          }      });
```

User2 может присоединиться к каналу

```
// присоединиться к каналуethree.joinRatchetChannel(users.get("User1"))      .addCallback(new OnResultListener<RatchetChannel>() {    @Override public void onSuccess(RatchetChannel ratchetChannel) {        // Канал присоединен и сохранен локально!    }    @Override public void onError(@NotNull Throwable throwable) {        // Обработка ошибки    }});
```

### **Шифрование и расшифровка сообщений одноранговой беседы**

1. Используйте созданный выше канал для шифрования сообщений, ссылка на документацию: [https://developer.virgilsecurity.com/docs/e3kit/end-to-end-encryption/double-ratchet/?#encrypt-and-decrypt-messages](https://developer.virgilsecurity.com/docs/e3kit/end-to-end-encryption/double-ratchet/#encrypt-and-decrypt-messages)

```
// шифрование сообщения одноранговой беседы// подготовка сообщенияString messageToEncrypt = "Hello, User2!";String encrypted = channel.encrypt(messageToEncrypt);
```

2. Зашифрованное содержание сообщения отправляется в Tencent Cloud Chat Sdk и отправляется с пользовательским сообщением

```
// `msgID` возвращается API для использования по требованиюString msgID = V2TIMManager.getInstance().sendC2CCustomMessage("virgil encrypted msg", "receiver_userID", new V2TIMValueCallback<V2TIMMessage>() {@Overridepublic void onSuccess(V2TIMMessage message) {    // Одноранговое текстовое сообщение отправлено успешно}    @Overridepublic void onError(int code, String desc) {    // Ошибка при отправке одноранговой текстового сообщения}});
```

3. После получения пользовательского сообщения адресатом

```
// Установить слушатель событийV2TIMManager.getInstance().addSimpleMsgListener(simpleMsgListener);/*** Получить одноранговое пользовательское сообщение* @param msgID ID сообщения* @param sender Информация об отправителе* @param customData Отправленное содержание*/public void onRecvC2CCustomMessage(String msgID, V2TIMUserInfo sender, byte[] customData) {Log.i("onRecvC2CCustomMessage", "msgID:" + msgID + ", from:" + sender.getNickName() + ", content:" + new String(customData));//вызвать E3Kit для расшифровки сообщения}
```

4. Адресат вызывает E3Kit для расшифровки и визуализации, как показано ниже:

```
// Расшифровка сообщенияString decrypted = channel.decrypt(encrypted);
```

### **Начало канала (группы)**

1. Вызовите ethree.createGroup для создания группы, ссылка на документацию: [https://developer.virgilsecurity.com/docs/e3kit/end-to-end-encryption/group-chat/?#create-group-chat](https://developer.virgilsecurity.com/docs/e3kit/end-to-end-encryption/group-chat/#create-group-chat)

```
// создать группуethree.createGroup(groupId, users).addCallback(new OnResultListener<Group>() {    @Override public void onSuccess(Group group) {        // Группа создана и сохранена локально!    }    @Override public void onError(@NotNull Throwable throwable) {        // Обработка ошибки    }});
```

2. Если вам нужно добавить членов группы, код выглядит следующим образом. Вы можете вызвать метод remove для удаления члена группы. Ссылка на документацию: [https://developer.virgilsecurity.com/docs/e3kit/end-to-end-encryption/group-chat/?#add-new-participant](https://developer.virgilsecurity.com/docs/e3kit/end-to-end-encryption/group-chat/#add-new-participant)

```
// добавить члена группыgroup.add(users.get("Den")).addCallback(new OnCompleteListener() {    @Override public void onSuccess() {        // Den был добавлен!    }    @Override public void onError(@NotNull Throwable throwable) {        // Обработка ошибки    }});
```

3. Вызовите createGroup из Tencent Cloud Chat Sdk для создания группы, joinGroup или inviteUserToGroup для добавления членов группы

```
V2TIMManager.getInstance().createGroup(V2TIMManager.GROUP_TYPE_WORK, null, "groupA", new V2TIMValueCallback<String>() { @Override public void onSuccess(String s) {     // Группа успешно создана }  @Override public void onError(int code, String desc) {     // Ошибка при создании группы }});// Прослушивать уведомление о создании группыV2TIMManager.getInstance().addGroupListener(new V2TIMGroupListener() { @Override public void onGroupCreated(String groupID) {     // Группа была создана. `groupID` — это ID созданной группы. }});
```

```
// Пригласите пользователя `userA` присоединиться к группе `groupA`List<String> userIDList = new ArrayList<>();userIDList.add("userA");V2TIMManager.getGroupManager().inviteUserToGroup("groupA", userIDList, new V2TIMValueCallback<List<V2TIMGroupMemberOperationResult>>() { @Override public void onSuccess(List<V2TIMGroupMemberOperationResult> v2TIMGroupMemberOperationResults) {     // Пользователь успешно приглашен в группу }  @Override public void onError(int code, String desc) {     // Ошибка при приглашении пользователя в группу }});// Прослушивать событие приглашения в группуV2TIMManager.getInstance().addGroupListener(new V2TIMGroupListener() { @Override public void onMemberInvited(String groupID, V2TIMGroupMemberInfo opUser, List<V2TIMGroupMemberInfo> memberList) {     // Пользователь был приглашен в группу. Этот обратный вызов может содержать некоторые советы пользовательского интерфейса. }});
```

### **Шифрование и расшифровка сообщений группового чата**

1. Используйте созданную выше группу для шифрования сообщений, ссылка на документацию: [https://developer.virgilsecurity.com/docs/e3kit/end-to-end-encryption/group-chat/?#encrypt-and-decrypt-messages](https://developer.virgilsecurity.com/docs/e3kit/end-to-end-encryption/group-chat/#encrypt-and-decrypt-messages)

```
// шифрование сообщения группы// подготовка сообщенияString messageToEncrypt = "Hello, Bob and Carol!";String encrypted = group.encrypt(messageToEncrypt);
```

2. Зашифрованное содержание сообщения отправляется в Tencent Chat Sdk и [отправляется с пользовательским сообщением](https://www.tencentcloud.com/document/product/1047/47994)

```
String msgID = V2TIMManager.getInstance().sendGroupCustomMessage("virgil encrypted msg ".getBytes(), "groupID", V2TIMMessage.V2TIM_PRIORITY_NORMAL, new V2TIMValueCallback<V2TIMMessage>() {@Overridepublic void onSuccess(V2TIMMessage message) {    // Пользовательское сообщение группы отправлено успешно}
```

3. После получения пользовательского сообщения Tencent Cloud Chat Sdk [получит пользовательское сообщение](https://www.tencentcloud.com/document/product/1047/47995)

```
// Установить слушатель событийV2TIMManager.getInstance().addSimpleMsgListener(simpleMsgListener);/*** Получить пользовательское сообщение группы* @param msgID ID сообщения* @param groupID ID группы* @param sender Информация члена группы отправителя* @param customData Отправленное содержание*/public void onRecvGroupCustomMessage(String msgID, String groupID, V2TIMGroupMemberInfo sender, byte[] customData) {Log.i("onRecvGroupCustomMessage", "msgID:" + msgID + ", groupID:" + groupID + ", from:" + sender.getNickName() + ", content:" + new String(customData));//вызвать E3Kit для расшифровки сообщения}
```

4. Адресат расшифровывает и визуализирует, как показано ниже:

```
// расшифровка сообщения группыString decrypted = group.decrypt(encrypted, users.get("Alice"));
```

> **Примечание:** после использования этой схемы сквозного шифрования функция локального поиска истории чата imsdk будет недоступна

## **IM — группы разработчиков**

Присоединитесь к группе разработчиков Tencent Cloud IM для:

```
            ✓ Надежная техническая поддержка             ✓ Детали продукта            ✓ Постоянный обмен идеями
```

Группа Telegram (EN): [присоединиться](https://t.me/+1doS9AUBmndhNGNl)

Группа WhatsApp (EN): [присоединиться](https://chat.whatsapp.com/Gfbxk7rQBqc8Rz4pzzP27A)

Группа Telegram (ZH): [присоединиться](https://t.me/tencent_imsdk)

Группа WhatsApp (ZH): [присоединиться](https://chat.whatsapp.com/IVa11ZkVmKTEwSWsAzSyik)


---
*Источник: [https://trtc.io/document/53932](https://trtc.io/document/53932)*

---
*Источник (EN): [end-to-end-encrypted-chat-with-virgil.md](./end-to-end-encrypted-chat-with-virgil.md)*

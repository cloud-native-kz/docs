# Перевод

## Обзор

Функция перевода сообщений в настоящее время поддерживает перевод только текстовых сообщений, которые можно инициировать вручную через вызовы API. Нетекстовые сообщения, такие как изображения, видео, файлы, аудио и пользовательские сообщения, не могут быть переведены.

> **Примечание:** Функция перевода сообщений доступна только для клиентов **Pro Plus и Enterprise**. Она может быть использована после [приобретения Pro Plus и Enterprise](https://console.trtc.io/subscription/buy/chat?packType=pro&language=en); версия Free Trial поддерживает [определённый лимит бесплатного использования](https://www.tencentcloud.com/document/product/1047/67651#0182a443-4747-42cb-b5de-ad165eb5a2ff), действительный в течение одного месяца. Эта функция доступна только в SDK в версии v7.0 или более поздней.

## Эффект

Вы можете использовать функцию Message Translation для реализации эффекта перевода, показанного на диаграмме ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/b6952112215811ef95b8525400e64ebc.png)

> **Примечание:** Вы также можете непосредственно использовать плагин перевода с встроенным интерфейсом TUITranslationPlugin для быстрого получения возможностей перевода.

## Описание интерфейса

### Перевод текстовых сообщений

Вызовите API `translateText` ([Java](https://im.sdk.qcloud.com/doc/en/classcom_1_1tencent_1_1imsdk_1_1v2_1_1V2TIMMessageManager.html#a1e1806c27bc7b76a3b816492ed9cbe5c) / [Swift](https://im.sdk.qcloud.com/doc/en/swift_V2TIMManager+Message.html#v2timmanager.translatetext(sourcetextlist:sourcelanguage:targetlanguage:completion:)) / [Objective-C](https://im.sdk.qcloud.com/doc/en/categoryV2TIMManager_07Message_08.html#aee0c1e26b0401576ee82967698da35f6) / [C++](https://im.sdk.qcloud.com/doc/en/classV2TIMMessageManager.html#ad4df190bf4089a64f69b84a874a60028)) для перевода текстов.

Параметры API описаны следующим образом:

| Входной параметр | Определение | Описание |
| --- | --- | --- |
| sourceTextList | Список текстовых сообщений для перевода | За один раз можно передать несколько текстовых сообщений. Требуется кодировка UTF-8; в противном случае перевод не будет выполнен. Для текстов, содержащих HTML-теги и другие нетекстовые элементы, перевод может не удаться. Общий объём текста для перевода в одном запросе может содержать до 2000 символов (каждый китайский иероглиф, буква, знак пунктуации или пробел считаются за один символ). |
| sourceLanguage | Исходный язык | Передайте конкретный язык или `auto` (автоматически определить исходный язык). Если значение не передано, будет использовано значение по умолчанию `auto`. |
| targetLanguage | Целевой язык | Поддерживаются несколько целевых языков. Дополнительную информацию см. в разделе [Поддерживаемые языки для перевода текста](https://www.tencentcloud.com/document/product/1047/53434?lang=en&pg=). |
| callback | Обратный вызов результата перевода | В обратном вызове `key` указывает на текст для перевода, а `value` указывает на переведённый текст. |

Пример кода:

Java

Swift

Objective-C

C++

```
List<String> textList = new ArrayList<>();textList.add("");textList.add("");textList.add("");String targetLanguage = "en";V2TIMManager.getMessageManager().translateText(textList, null, targetLanguage, new V2TIMValueCallback<HashMap<String, String>>() {    @Override    public void onSuccess(HashMap<String, String> translateHashMap) {        // Тексты успешно переведены. `translateHashMap`: {"": "Good morning", "": "Good afternoon", "": "Good evening"}    }    @Override    public void onError(int code, String desc) {        // Ошибка перевода текста    }});
```

```
V2TIMManager.shared.translateText(sourceTextList: ["Hello","Bye"], sourceLanguage: "zh", targetLanguage: "en") { code, desc, map in    print("translateText result, code: \\(code), desc: \\(desc)")    map.forEach { (key: String, value: String) in        print( "\\(key): \\(value)")    }}
```

```
NSArray *sourceText = @[@"", @"", @""];NSString *targetLanguage = @"en";[[V2TIMManager sharedInstance] translateText:sourceText                              sourceLanguage:nil                              targetLanguage:targetLanguage                                  completion:^(int code, NSString *desc, NSDictionary<NSString *,NSString *> *result) {    if (code == 0) {        // Тексты успешно переведены. `result`: @{@"": @"Good morning", @"": @"Good afternoon", @"": @"Good evening"}    } else {        // Ошибка перевода текста    }}];
```

```
template <class T>class ValueCallback final : public V2TIMValueCallback<T> {public:    using SuccessCallback = std::function<void(const T&)>;    using ErrorCallback = std::function<void(int, const V2TIMString&)>;    ValueCallback() = default;    ~ValueCallback() override = default;    void SetCallback(SuccessCallback success_callback, ErrorCallback error_callback) {        success_callback_ = std::move(success_callback);        error_callback_ = std::move(error_callback);    }    void OnSuccess(const T& value) override {        if (success_callback_) {            success_callback_(value);        }    }    void OnError(int error_code, const V2TIMString& error_message) override {        if (error_callback_) {            error_callback_(error_code, error_message);        }    }private:    SuccessCallback success_callback_;    ErrorCallback error_callback_;};V2TIMStringVector textList;textList.PushBack(u8"");textList.PushBack(u8"");textList.PushBack(u8"");V2TIMString targetLanguage = u8"en";auto callback = new ValueCallback<V2TIMStringToV2TIMStringMap>{};callback->SetCallback(    [=](const V2TIMStringToV2TIMStringMap& result) {        // Тексты успешно переведены. `result`: {{"", "Good morning"}, {"", "Good afternoon"}, {"", "Good evening"}}        delete callback;    },    [=](int error_code, const V2TIMString& error_message) {        // Ошибка перевода текста        delete callback;    });V2TIMManager::GetInstance()->GetMessageManager()->TranslateText(textList, "", targetLanguage, callback);
```

## Поддерживаемые языки для перевода текста

| Исходный язык | Поддерживаемые целевые языки |
| --- | --- |
| zh (Упрощённый китайский) | en (английский), ja (японский), ko (корейский), fr (французский), es (испанский), it (итальянский), de (немецкий), tr (турецкий), ru (русский), pt (португальский), vi (вьетнамский), id (индонезийский), th (тайский) и ms (малайский) |
| zh-TW (Традиционный китайский) | en (английский), ja (японский), ko (корейский), fr (французский), es (испанский), it (итальянский), de (немецкий), tr (турецкий), ru (русский), pt (португальский), vi (вьетнамский), id (индонезийский), th (тайский) и ms (малайский) |
| en (английский) | zh (упрощённый китайский), ja (японский), ko (корейский), fr (французский), es (испанский), it (итальянский), de (немецкий), tr (турецкий), ru (русский), pt (португальский), vi (вьетнамский), id (индонезийский), th (тайский), ms (малайский), ar (арабский) и hi (хинди) |
| ja (японский) | zh (упрощённый китайский), en (английский), ko (корейский) |
| ko (корейский) | zh (упрощённый китайский), en (английский), ja (японский) |
| fr (французский) | zh (упрощённый китайский), en (английский), es (испанский), it (итальянский), de (немецкий), tr (турецкий), ru (русский) и pt (португальский) |
| es (испанский) | zh (упрощённый китайский), en (английский), fr (французский), it (итальянский), de (немецкий), tr (турецкий), ru (русский) и pt (португальский) |
| it (итальянский) | zh (упрощённый китайский), en (английский), fr (французский), es (испанский), de (немецкий), tr (турецкий), ru (русский) и pt (португальский) |
| de (немецкий) | zh (упрощённый китайский), en (английский), fr (французский), es (испанский), it (итальянский), tr (турецкий), ru (русский) и pt (португальский) |
| tr (турецкий) | zh (упрощённый китайский), en (английский), fr (французский), es (испанский), it (итальянский), de (немецкий), ru (русский) и pt (португальский) |
| ru (русский) | zh (упрощённый китайский), en (английский), fr (французский), es (испанский), it (итальянский), de (немецкий), tr (турецкий) и pt (португальский) |
| pt (португальский) | zh (упрощённый китайский), en (английский), fr (французский), es (испанский), it (итальянский), de (немецкий), tr (турецкий) и ru (русский) |
| vi (вьетнамский) | zh (упрощённый китайский), en (английский) |
| id (индонезийский) | zh (упрощённый китайский), en (английский) |
| th (тайский) | zh (упрощённый китайский), en (английский) |
| ms (малайский) | zh (упрощённый китайский), en (английский) |
| ar (арабский) | en (английский) |
| hi (хинди) | en (английский) |


---
*Источник: [https://trtc.io/document/53434](https://trtc.io/document/53434)*

---
*Источник (EN): [translation.md](./translation.md)*

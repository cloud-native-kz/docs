# Политика конфиденциальности Apple: PrivacyInfo.xcprivacy

В соответствии с [обновлением политики конфиденциальности App Store](https://developer.apple.com/news/?id=r1henawx) компании Apple Inc., начиная с весны 2024 года, приложения, размещённые в App Store, должны также предоставлять **манифест конфиденциальности**.

**Когда вы будете готовы распространять своё приложение, Xcode объединит манифесты конфиденциальности всех сторонних SDK, используемых приложением, в удобный для использования отчёт.**

Этот отчёт полностью суммирует все сторонние SDK в приложении, позволяя вам создавать теги конфиденциальности простым и точным способом.

Поэтому встроенные в приложение SDK и сторонние библиотеки должны включать **PrivacyInfo.xcprivacy**.

## Адаптация TRTC (Tencent Real-Time Communication)

В TRTC SDK **11.7** и более поздних версиях (включая облегченное и полнофункциональное издания) файл **PrivacyInfo.xcprivacy** включён по умолчанию.

В TUICallKit **2.3.0.920** и более поздних версиях файл **PrivacyInfo.xcprivacy** включён по умолчанию.

В TUIRoomKit **2.3.0** и более поздних версиях файл **PrivacyInfo.xcprivacy** включён по умолчанию.

В TUILiveKit **2.1.1** и более поздних версиях файл **PrivacyInfo.xcprivacy** включён по умолчанию.

- При интеграции через CocoaPod файл **PrivacyInfo.xcprivacy** будет добавлен в ваш проект через Pod, поэтому **дополнительной работы не требуется**.
- При ручной интеграции убедитесь, что вы **скопировали PrivacyInfo.xcprivacy из директории исходного кода в ваш проект кода**.

> **Примечание:** Схема TUIKit и полнофункциональное издание (Professional) TRTC SDK включают несколько продуктов SDK, и **PrivacyInfo.xcprivacy** может иметь незначительные различия в содержании. Поэтому вы можете выбрать соответствующую версию файла в зависимости от ваших потребностей.

### **PrivacyInfo.xcprivacy**, связанные с TRTC

Облегченное издание (TRTC) SDK

Полнофункциональное издание (Professional) SDK

TUICallKit

TUIRoomKit

TUILiveKit

```
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>	<key>NSPrivacyCollectedDataTypes</key>	<array>		<dict>			<key>NSPrivacyCollectedDataType</key>			<string>NSPrivacyCollectedDataTypeUserID</string>			<key>NSPrivacyCollectedDataTypeLinked</key>			<false/>			<key>NSPrivacyCollectedDataTypeTracking</key>			<false/>			<key>NSPrivacyCollectedDataTypePurposes</key>			<array>				<string>NSPrivacyCollectedDataTypePurposeAppFunctionality</string>			</array>		</dict>		<dict>			<key>NSPrivacyCollectedDataType</key>			<string>NSPrivacyCollectedDataTypeOtherDiagnosticData</string>			<key>NSPrivacyCollectedDataTypeLinked</key>			<false/>			<key>NSPrivacyCollectedDataTypeTracking</key>			<false/>			<key>NSPrivacyCollectedDataTypePurposes</key>			<array>				<string>NSPrivacyCollectedDataTypePurposeAppFunctionality</string>			</array>		</dict>		<dict>			<key>NSPrivacyCollectedDataType</key>			<string>NSPrivacyCollectedDataTypePhotosorVideos</string>			<key>NSPrivacyCollectedDataTypeLinked</key>			<false/>			<key>NSPrivacyCollectedDataTypeTracking</key>			<false/>			<key>NSPrivacyCollectedDataTypePurposes</key>			<array>				<string>NSPrivacyCollectedDataTypePurposeAppFunctionality</string>			</array>		</dict>		<dict>			<key>NSPrivacyCollectedDataType</key>			<string>NSPrivacyCollectedDataTypeAudioData</string>			<key>NSPrivacyCollectedDataTypeLinked</key>			<false/>			<key>NSPrivacyCollectedDataTypeTracking</key>			<false/>			<key>NSPrivacyCollectedDataTypePurposes</key>			<array>				<string>NSPrivacyCollectedDataTypePurposeAppFunctionality</string>			</array>		</dict>		<dict>			<key>NSPrivacyCollectedDataType</key>			<string>NSPrivacyCollectedDataTypePerformanceData</string>			<key>NSPrivacyCollectedDataTypeLinked</key>			<false/>			<key>NSPrivacyCollectedDataTypeTracking</key>			<false/>			<key>NSPrivacyCollectedDataTypePurposes</key>			<array>				<string>NSPrivacyCollectedDataTypePurposeAppFunctionality</string>			</array>		</dict>	</array>	<key>NSPrivacyAccessedAPITypes</key>	<array>		<dict>			<key>NSPrivacyAccessedAPIType</key>			<string>NSPrivacyAccessedAPICategoryUserDefaults</string>			<key>NSPrivacyAccessedAPITypeReasons</key>			<array>				<string>C56D.1</string>			</array>		</dict>		<dict>			<key>NSPrivacyAccessedAPIType</key>			<string>NSPrivacyAccessedAPICategoryFileTimestamp</string>			<key>NSPrivacyAccessedAPITypeReasons</key>			<array>				<string>0A2A.1</string>			</array>		</dict>		<dict>			<key>NSPrivacyAccessedAPIType</key>			<string>NSPrivacyAccessedAPICategorySystemBootTime</string>			<key>NSPrivacyAccessedAPITypeReasons</key>			<array>				<string>35F9.1</string>			</array>		</dict>	</array></dict></plist>
```

```
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>	<key>NSPrivacyCollectedDataTypes</key>	<array>		<dict>			<key>NSPrivacyCollectedDataType</key>			<string>NSPrivacyCollectedDataTypeUserID</string>			<key>NSPrivacyCollectedDataTypeLinked</key>			<false/>			<key>NSPrivacyCollectedDataTypeTracking</key>			<false/>			<key>NSPrivacyCollectedDataTypePurposes</key>			<array>				<string>NSPrivacyCollectedDataTypePurposeAppFunctionality</string>			</array>		</dict>		<dict>			<key>NSPrivacyCollectedDataType</key>			<string>NSPrivacyCollectedDataTypeOtherDiagnosticData</string>			<key>NSPrivacyCollectedDataTypeLinked</key>			<false/>			<key>NSPrivacyCollectedDataTypeTracking</key>			<false/>			<key>NSPrivacyCollectedDataTypePurposes</key>			<array>				<string>NSPrivacyCollectedDataTypePurposeAppFunctionality</string>			</array>		</dict>		<dict>			<key>NSPrivacyCollectedDataType</key>			<string>NSPrivacyCollectedDataTypePhotosorVideos</string>			<key>NSPrivacyCollectedDataTypeLinked</key>			<false/>			<key>NSPrivacyCollectedDataTypeTracking</key>			<false/>			<key>NSPrivacyCollectedDataTypePurposes</key>			<array>				<string>NSPrivacyCollectedDataTypePurposeAppFunctionality</string>			</array>		</dict>		<dict>			<key>NSPrivacyCollectedDataType</key>			<string>NSPrivacyCollectedDataTypeAudioData</string>			<key>NSPrivacyCollectedDataTypeLinked</key>			<false/>			<key>NSPrivacyCollectedDataTypeTracking</key>			<false/>			<key>NSPrivacyCollectedDataTypePurposes</key>			<array>				<string>NSPrivacyCollectedDataTypePurposeAppFunctionality</string>			</array>		</dict>		<dict>			<key>NSPrivacyCollectedDataType</key>			<string>NSPrivacyCollectedDataTypePerformanceData</string>			<key>NSPrivacyCollectedDataTypeLinked</key>			<false/>			<key>NSPrivacyCollectedDataTypeTracking</key>			<false/>			<key>NSPrivacyCollectedDataTypePurposes</key>			<array>				<string>NSPrivacyCollectedDataTypePurposeAppFunctionality</string>			</array>		</dict>	</array>	<key>NSPrivacyAccessedAPITypes</key>	<array>		<dict>			<key>NSPrivacyAccessedAPIType</key>			<string>NSPrivacyAccessedAPICategoryDiskSpace</string>			<key>NSPrivacyAccessedAPITypeReasons</key>			<array>				<string>E174.1</string>			</array>		</dict>		<dict>			<key>NSPrivacyAccessedAPIType</key>			<string>NSPrivacyAccessedAPICategoryUserDefaults</string>			<key>NSPrivacyAccessedAPITypeReasons</key>			<array>				<string>C56D.1</string>			</array>		</dict>		<dict>			<key>NSPrivacyAccessedAPIType</key>			<string>NSPrivacyAccessedAPICategoryFileTimestamp</string>			<key>NSPrivacyAccessedAPITypeReasons</key>			<array>				<string>0A2A.1</string>			</array>		</dict>		<dict>			<key>NSPrivacyAccessedAPIType</key>			<string>NSPrivacyAccessedAPICategorySystemBootTime</string>			<key>NSPrivacyAccessedAPITypeReasons</key>			<array>				<string>35F9.1</string>			</array>		</dict>	</array></dict></plist>
```

```
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>	<key>NSPrivacyTracking</key>	<false/>	<key>NSPrivacyTrackingDomains</key>	<array/>    <key>NSPrivacyCollectedDataTypes</key>    <array>        <dict>            <key>NSPrivacyCollectedDataType</key>            <string>NSPrivacyCollectedDataTypeUserID</string>            <key>NSPrivacyCollectedDataTypeLinked</key>            <false/>            <key>NSPrivacyCollectedDataTypeTracking</key>            <false/>            <key>NSPrivacyCollectedDataTypePurposes</key>            <array>                <string>NSPrivacyCollectedDataTypePurposeAppFunctionality</string>            </array>        </dict>    </array>	<key>NSPrivacyAccessedAPITypes</key>	<array>        <dict>            <key>NSPrivacyAccessedAPIType</key>            <string>NSPrivacyAccessedAPICategoryDiskSpace</string>            <key>NSPrivacyAccessedAPITypeReasons</key>            <array>                <string>E174.1</string>            </array>        </dict>        <dict>            <key>NSPrivacyAccessedAPIType</key>            <string>NSPrivacyAccessedAPICategoryUserDefaults</string>            <key>NSPrivacyAccessedAPITypeReasons</key>            <array>                <string>CA92.1</string>            </array>        </dict>	</array></dict></plist>
```

```
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>	<key>NSPrivacyTracking</key>	<false/>	<key>NSPrivacyTrackingDomains</key>	<array/>    <key>NSPrivacyCollectedDataTypes</key>    <array>        <dict>            <key>NSPrivacyCollectedDataType</key>            <string>NSPrivacyCollectedDataTypeUserID</string>            <key>NSPrivacyCollectedDataTypeLinked</key>            <false/>            <key>NSPrivacyCollectedDataTypeTracking</key>            <false/>            <key>NSPrivacyCollectedDataTypePurposes</key>            <array>                <string>NSPrivacyCollectedDataTypePurposeAppFunctionality</string>            </array>        </dict>    </array>	<key>NSPrivacyAccessedAPITypes</key>	<array>		<dict>			<key>NSPrivacyAccessedAPIType</key>			<string>NSPrivacyAccessedAPICategorySystemBootTime</string>			<key>NSPrivacyAccessedAPITypeReasons</key>			<array>				<string>35F9.1</string>			</array>		</dict>	</array></dict></plist>
```

```
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>	<key>NSPrivacyTracking</key>	<false/>	<key>NSPrivacyTrackingDomains</key>	<array/>    <key>NSPrivacyCollectedDataTypes</key>    <array>        <dict>            <key>NSPrivacyCollectedDataType</key>            <string>NSPrivacyCollectedDataTypeUserID</string>            <key>NSPrivacyCollectedDataTypeLinked</key>            <false/>            <key>NSPrivacyCollectedDataTypeTracking</key>            <false/>            <key>NSPrivacyCollectedDataTypePurposes</key>            <array>                <string>NSPrivacyCollectedDataTypePurposeAppFunctionality</string>            </array>        </dict>    </array>	<key>NSPrivacyAccessedAPITypes</key>	<array>		<dict>			<key>NSPrivacyAccessedAPIType</key>			<string>NSPrivacyAccessedAPICategorySystemBootTime</string>			<key>NSPrivacyAccessedAPITypeReasons</key>			<array>				<string>35F9.1</string>			</array>		</dict>	</array></dict></plist>
```

### Ручный импорт в своё приложение

Помимо автоматического импорта PrivacyInfo через CocoaPod, вы также можете напрямую заполнить условия **PrivacyInfo.xcprivacy** TRTC SDK (или соответствующей версии) в файл **PrivacyInfo.xcprivacy** вашего приложения. Для получения конкретных методов заполнения вы можете обратиться к следующему контенту:

- Добавление с исходным кодом

В Xcode используйте исходный код для открытия **PrivacyInfo.xcprivacy** под проектом приложения. Скопируйте записи из **PrivacyInfo.xcprivacy** Tencent Cloud, стараясь не добавлять дубликаты и не нарушать порядок строк.

- Добавление со списком свойств

В Xcode дважды щёлкните, чтобы открыть файл **PrivacyInfo.xcprivacy**, нажмите +, и Xcode предложит дополнительные условия и настраиваемые элементы. Дополните их в соответствии с вашими потребностями.


---
*Источник: [https://trtc.io/document/60152](https://trtc.io/document/60152)*

---
*Источник (EN): [apple-privacy-policy-privacyinfoxcprivacy.md](./apple-privacy-policy-privacyinfoxcprivacy.md)*

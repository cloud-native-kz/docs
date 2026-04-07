# Локализация

## Описание функции

React Native UIKit поставляется с языковыми пакетами по умолчанию для **английского** и **упрощенного китайского** языков в качестве языков отображения интерфейса.

Следуя этой документации, вы можете использовать языковые пакеты по умолчанию или настроить возможности интернационализации в соответствии с вашими потребностями, включая добавление новых языков и обновление содержимого переводов.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/27455121b92911ef935c525400f69702.png)

## Использование языка по умолчанию

### Инициализация языка

При инициализации приложения необходимо зарегистрировать и инициализировать языковые ресурсы для механизма трансляции в файле `App.tsx`.

```
import { TUITranslateService } from '@tencentcloud/chat-uikit-engine';import uikitResources from '@tencentcloud/chat-uikit-react-native/i18n'; // Init localization TUITranslateService.provideLanguages(uikitResources); TUITranslateService.useI18n('en-US');
```

### Переключение языка

Если ваше приложение имеет запись переключения языка, вы можете вызвать `TUITranslateService.changeLanguage` для реализации функции переключения языка.

```
import { TUITranslateService } from '@tencentcloud/chat-uikit-engine';// language is the target language you switch toTUITranslateService.changeLanguage(language)
```

## Добавление языковых ресурсов приложения

Если ваше приложение требует перевода других страниц (например, страницы входа, страницы настроек) помимо UIKit, вы можете создать каталог ресурсов i18n в корневом каталоге приложения для добавления соответствующих записей. Используйте `TUITranslateService` для перевода. Вы можете инициализировать его со следующим примером кода, предполагая, что в корневом каталоге вашего проекта находится каталог `i18n`.

```
import { TUITranslateService } from '@tencentcloud/chat-uikit-engine';import uikitResources from '@tencentcloud/chat-uikit-react-native/i18n';import appResources from './i18n'; // Init localizationTUITranslateService.provideLanguages({    'en-US': {      ...appResources['en-US'],      ...uikitResources['en-US'],    },    'zh-CN': {      ...appResources['zh-CN'],      ...uikitResources['zh-CN'],    },}); TUITranslateService.useI18n('en-US');
```

## Обновление терминов перевода

Если условия перевода по умолчанию не соответствуют вашим потребностям, вы можете обновить условия перевода, выполнив следующие действия.

Скопируйте `node_modules/@tencentcloud/chat-uikit-react-native/` `i18n` в корневой каталог вашего проекта и переименуйте его на `i18n-uikit`. Измените содержимое перевода по мере необходимости. После изменения измените `uikitResources` для импорта из вашей локальной `import`.

```
import uikitResources from './i18n-uikit';
```

## Добавление типа языка

Если вам нужно добавить новый язык, скопируйте `node_modules/@tencentcloud/chat-uikit-react-native/i18n` `en-US` в каталог `i18n` в корневом каталоге вашего проекта, переименуйте его на новое имя языка (например, 'zh-TW') и измените содержимое перевода по мере необходимости.

## Использование API перевода

Если ваше приложение должно использовать возможности перевода, предоставляемые механизмом трансляции, вы можете использовать его следующим образом.

Например, если вы добавили термин перевода для модуля Login и хотите локализовать [username], условия для модуля Login определяются следующим образом:

`en-US` ：

```
export const Login = {  USER_NAME: 'UserName',};
```

`zh-CN` ：

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/20b32329bdd211ef8a945254002693fd.png)

Используйте функцию перевода на странице входа:

```
import { TUITranslateService } from '@tencentcloud/chat-uikit-engine';TUITransalteService.t('Login.USER_NAME')
```

Чтобы узнать, как реализовать переключение языка, вы можете обратиться к [исходному коду демо UIKit](https://github.com/TencentCloud/chat-demo-react-native).


---
*Источник: [https://trtc.io/document/67279](https://trtc.io/document/67279)*

---
*Источник (EN): [localization.md](./localization.md)*

# Параметры языка

## Поддерживаемые языки

В настоящее время поддерживает **упрощённый китайский, английский, японский**.

## Переключение языка

TUICallKit будет отдавать приоритет языку браузера. Если это один из языков китайский, английский или японский, будет использоваться язык браузера. В противном случае будет использоваться английский. Если вы хотите переключить языки, вы можете использовать интерфейс [setLanguage](https://www.tencentcloud.com/document/product/647/51015#setLanguage).

```
import { TUICallKitAPI, CallMediaType } from '@trtc/calls-uikit-vue';TUICallKitAPI.setLanguage("zh-cn"); // "en" | "zh-cn" | "ja_JP"
```

## Добавление нового языка

Если вам требуется поддержка других языков, вы можете изменить файл источника языка путём интеграции исходного кода.

### Шаг 1: интеграция исходного кода

> **Примечание:** интеграция исходного кода подходит для проектов `Vue + TypeScript` и версии `TUICallKit` 3.2.2 и выше.

1. **Загрузка исходного кода**

Vue3

```
npm install @trtc/calls-uikit-vue
```

2. **Скопируйте исходный код в ваш собственный проект, на примере копирования в каталог** `src/components/`:

macOS + Vue3

Windows + Vue3

```
mkdir -p ./src/components/TUICallKit && cp -r ./node_modules/@trtc/calls-uikit-vue/* ./src/components/TUICallKit
```

```
xcopy .\\node_modules\\@trtc\\calls-uikit-vue  .\\src\\components\\TUICallKit /i /e
```

3. **Изменение пути импорта**

Вам нужно изменить импорт TUICallKit на локальный файл, как показано в коде ниже. Для получения дополнительной информации об использовании см. [Быстрая интеграция TUICallKit](https://www.tencentcloud.com/zh/document/product/647/50993).

```
import { TUICallKit, TUICallKitAPI, CallMediaType } from "./components/TUICallKit/src/index";
```

4. **Решение ошибок, которые могут возникнуть при копировании исходного кода**

Если при использовании компонента TUICallKit возникает ошибка, не беспокойтесь. В большинстве случаев это вызвано несоответствиями между конфигурациями ESLint и TSConfig. Вы можете обратиться к документации и настроить конфигурацию по мере необходимости. Если вам нужна помощь, не стесняйтесь связаться с нами, и мы обеспечим успешное использование этого компонента. Вот некоторые распространённые проблемы:

Ошибка ESLint

Ошибка TypeScript

Если TUICallKit вызывает ошибку из-за несоответствия стилю кода вашего проекта, вы можете заблокировать этот каталог компонента, добавив файл `.eslintignore` в корневой каталог вашего проекта, например:

```
# .eslintignoresrc/components/TUICallKit
```

1. Если вы столкнулись с ошибкой 'Cannot find module '../package.json'', это потому, что TUICallKit ссылается на JSON-файл. Вы можете добавить соответствующую конфигурацию в tsconfig.json, пример:

```
{  "compilerOptions": {    "resolveJsonModule": true  }}
```

Для других проблем TSConfig см. [TSConfig Reference](https://www.typescriptlang.org/tsconfig).

2. Если вы столкнулись с ошибкой 'Uncaught SyntaxError: Invalid or unexpected token', это потому, что TUICallKit использует декораторы. Вы можете добавить соответствующую конфигурацию в tsconfig.json, пример:

```
{  "compilerOptions": {    "experimentalDecorators": true  }}
```

### Шаг 2: добавление новой языковой пакета

**Например, добавление вьетнамского языка:**

1. Создание файла источника целевого языка.

Добавьте новый файл с именем vi.ts в каталог src/components/TUICallKit/src/TUICallService/locales. Скопируйте содержимое файла src/components/TUICallKit/src/TUICallService/locales/zh-cn.ts в vi.ts и затем переведите значения JSON на вьетнамский язык.

```
export const vi = {    // Note the export variable here  'hangup': 'Hang Up',  'reject': 'Reject',  'accept': 'Acceptance',  'camera': 'Camera',  'microphone': 'Microphone',  'speaker': 'Speaker',  'open camera': 'Turn on the camera',  'close camera': 'Turn off the camera',  'open microphone': 'Open microphone',  'close microphone': 'Turn off the microphone',  'video-to-audio': 'Switch to audio call',  'virtual-background': 'Blur background',  'other side reject call': 'The other side has rejected',  'reject call': 'Reject call',  'cancel': 'Cancel call',  ...};
```

2. Экспорт из index.ts

Измените файл src/components/TUICallKit/src/TUICallService/locales/index.ts.

```
import { TUIStore } from '../CallService/index';import { NAME, StoreName } from '../const/index';import { en } from './en';import { zh } from './zh-cn';import { ja_JP } from './ja_JP';import { vi } from './vi';  // Import new language file.....export const languageData: languageDataType = {  en,  'zh-cn': zh,  ja_JP,  vi,       // Export new language file};
```

3. Добавление нового перечисления LanguageType.

Измените файл src/components/TUICallKit/src/TUICallService/const/call.ts

```
export enum LanguageType {  EN = 'en',  'ZH-CN' = 'zh-cn',  JA_JP = 'ja_JP',  VI = 'vi',   // Add new enum type}
```

4. Переключение языка

Переключайте языки в проекте, вызывая интерфейс [setLanguage](https://www.tencentcloud.com/document/product/647/51015#setLanguage).

```
import { TUICallKitAPI, CallMediaType } from '@trtc/calls-uikit-vue';TUICallKitAPI.setLanguage("vi");
```


---
*Источник: [https://trtc.io/document/62424](https://trtc.io/document/62424)*

---
*Источник (EN): [language-settings.md](./language-settings.md)*

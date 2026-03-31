# 2. Импорт SDK

В этом документе описывается, как быстро интегрировать TRTC Electron SDK в ваш проект.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/05f95b8937ff11ed8088525400463ef7.png)

## Поддерживаемые платформы

- Windows
- macOS

## Импорт SDK

### Шаг 1. Установка Node.js

Windows

macOS

1. Загрузите последнюю версию [Node.js](https://nodejs.org/en/download/) `Windows Installer (.msi) 64-bit`.
2. Откройте `Node.js command prompt` из списка приложений и откройте окно терминала.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/061313f137ff11edb1de525400c56988.png)

1. Откройте окно терминала и выполните следующую команду для установки Homebrew. Если вы уже установили его, пропустите этот шаг.

```
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

2. Выполните следующую команду для установки Node.js (версия v10.0 или выше).

```
$ brew install node
```

### Шаг 2. Установка Electron

```
$ npm install electron@latest --save-dev
```

### Шаг 3. Установка TRTC Electron SDK

```
$ npm install trtc-electron-sdk@latest --save
```

> **Примечание:** Информацию о последней версии TRTC Electron SDK можно найти [здесь](https://www.npmjs.com/package/trtc-electron-sdk).

2. В скрипте проекта импортируйте и используйте модуль:

```
const TRTCCloud = require('trtc-electron-sdk').default;// import TRTCCloud from 'trtc-electron-sdk';this.rtcCloud = new TRTCCloud();// Get the SDK version numberthis.rtcCloud.getSDKVersion();
```

Начиная с версии v7.9.348, TRTC Electron SDK включает `trtc.d.ts` для разработчиков, использующих TypeScript.

```
import TRTCCloud from 'trtc-electron-sdk';const rtcCloud: TRTCCloud = new TRTCCloud();// Get the SDK version numberrtcCloud.getSDKVersion();
```

### Шаг 4. Создание исполняемой программы

```
$ npm install electron-builder@latest --save-dev
```

Для правильной упаковки TRTC Electron SDK (`trtc_electron_sdk.node`) необходимо также выполнить следующую команду для установки `native-ext-loader`.

```
$ npm install native-ext-loader@latest --save-dev
```

### Шаг 5. Изменение конфигурации сборки (`webpack.config.js`)

- Обычно `webpack.config.js` находится в корневой директории проекта.
- Если вы создали проект с помощью `create-react-app`, файл конфигурации будет `node_modules/react-scripts/config/webpack.config.js`.
- Если вы создали проект с помощью `vue-cli`, конфигурация webpack будет находиться в свойстве `configureWebpack` файла `vue.config.js`.
- Если ваш проект настроен особым образом, найдите конфигурацию webpack в соответствии с вашим проектом.
1. Сначала добавьте следующий код перед `module.exports` так, чтобы `webpack.config.js` принимал параметр командной строки `--target_platform`, что позволит правильно собрать проект для целевой платформы.

```
const os = require('os');const targetPlatform = (function(){     let target = os.platform();     for (let i=0; i<process.argv.length; i++) {         if (process.argv[i].includes('--target_platform=')) {             target = process.argv[i].replace('--target_platform=', '');             break;         }     }     if (!['win32', 'darwin'].includes) target = os.platform();     return target;})();
```

> **Примечание:** В результате, возвращаемом `os.platform()`, `darwin` означает macOS, а `win32` означает Windows (64-разрядная или 32-разрядная версия).

2. Добавьте следующую конфигурацию в опцию `rules`. Переменная `targetPlatform` гарантирует, что `rewritePath` автоматически изменяется в зависимости от целевой платформы.

```
rules: [  {          test: /\\.node$/,          loader: 'native-ext-loader',          options: {              rewritePath: targetPlatform === 'win32' ? './resources' : '../Resources'             // Build for different platforms             // rewritePath: './node_modules/trtc-electron-sdk/build/Release'         }      },]
```

Приведённый выше код достигает следующего:

- При создании файла EXE для Windows `native-ext-loader` будет загружать TRTC SDK из `[корневая директория приложения]/resources`.
- При создании файла DMG для macOS `native-ext-loader` будет загружать TRTC SDK из `[директория приложения]/Contents/Frameworsk/../Resources`.
- При локальной сборке `native-ext-loader` будет загружать TRTC SDK из `./node_modules/trtc-electron-sdk/build/Release`. Дополнительные сведения см. в [конфигурации TRTCSimpleDemo](https://github.com/LiteAVSDK/TRTC_Electron/blob/main/TRTCSimpleDemo/vue.config.js).

Вам также необходимо добавить параметр `--target_platform` в скрипт сборки `package.json`, что приводит нас к следующему шагу.

### Шаг 6. Изменение `package.json`

1. Измените `main`.

```
// В большинстве случаев имя файла `main` можно настраивать. Например, в TRTCSimpleDemo `main` можно настроить следующим образом:"main": "main.electron.js",// Однако для проектов, созданных с помощью инструмента `create-react-app`, `main` необходимо настроить следующим образом:"main": "public/electron.js",
```

2. Скопируйте следующую конфигурацию `build` в ваш файл `package.json` для чтения `electron-builder`.

```
"build": {  "appId": "[Custom appId]",  "directories": { "output": "./bin"  },  "win": { "extraFiles": [   {     "from": "node_modules/trtc-electron-sdk/build/Release/",     "to": "./resources",     "filter": ["**/*"]   } ]  },  "mac": { "extraFiles": [   {      "from": "node_modules/trtc-electron-sdk/build/Release/trtc_electron_sdk.node",      "to": "./Resources"    } ]  }},
```

3. Добавьте скрипты команд для сборки и упаковки в `scripts`.
Следующие скрипты команд предназначены для проектов, созданных с помощью `create-react-app` и `vue-cli`. Они предоставляют примеры для проектов, созданных с помощью других инструментов.

```
// Используйте эту конфигурацию для проектов, созданных с помощью `create-react-app`."scripts": {  "build:mac": "react-scripts build --target_platform=darwin",  "build:win": "react-scripts build --target_platform=win32",  "compile:mac": "node_modules/.bin/electron-builder --mac",  "compile:win64": "node_modules/.bin/electron-builder --win --x64",  "pack:mac": "npm run build:mac && npm run compile:mac",  "pack:win64": "npm run build:win && npm run compile:win64"}// Используйте эту конфигурацию для проектов, созданных с помощью `vue-cli`."scripts": {  "build:mac": "vue-cli-service build --target_platform=darwin",  "build:win": "vue-cli-service build --target_platform=win32",  "compile:mac": "node_modules/.bin/electron-builder --mac",  "compile:win64": "node_modules/.bin/electron-builder --win --x64",  "pack:mac": "npm run build:mac && npm run compile:mac",  "pack:win64": "npm run build:win && npm run compile:win64"}
```

| Параметр | Описание |
| --- | --- |
| main | Файл точки входа Electron, который может быть настроен в большинстве случаев. Однако если ваш проект создан с помощью create-react-app, файл точки входа должен быть public/electron.js. |
| build.win.extraFiles | При сборке для Windows electron-builder скопирует все файлы в директорию, указанную в from, в bin/win-unpacked/resources (все в нижнем регистре). |
| build.mac.extraFiles | При упаковке для macOS electron-builder скопирует файл trtc_electron_sdk.node, указанный в from, в bin/mac/your-app-name.app/Contents/Resources (с заглавной буквой в начале каждого слова) |
| build.directories.output | Путь вывода. В приведённом выше примере выходной файл сохраняется в bin. Вы можете изменить его при необходимости. |
| build.scripts.build:mac | Скрипт для сборки для macOS. |
| build.scripts.build:win | Скрипт для сборки для Windows. |
| build.scripts.compile:mac | Создаёт файл DMG для macOS |
| build.scripts.compile:win64 | Создаёт файл EXE для Windows |
| build.scripts.pack:mac | Вызывает build:mac для сборки проекта, а затем `compile:mac` для создания файла DMG |
| build.scripts.pack:win64 | Вызывает build:win для сборки проекта, а затем `compile:win64` для создания файла EXE |

### Шаг 7. Запуск команды сборки

```
$ cd [Project directory]$ npm run pack:mac
```

Инструмент сборки создаст файл установки с именем `bin/your-app-name-0.1.0.dmg`. Опубликуйте этот файл.

- Сборка проекта в файл EXE для Windows:

```
$ cd [Project directory]$ npm run pack:win64
```

Инструмент сборки создаст файл установки с именем `bin/your-app-name Setup 0.1.0.exe`. Опубликуйте этот файл.

> **Примечание:** В настоящее время TRTC Electron SDK не поддерживает кроссплатформенную сборку. Это означает, что вы не можете собрать проект в файл EXE на macOS или в файл DMG на Windows. Мы работаем над этим и можем добавить поддержку в будущем.

## Часто задаваемые вопросы

### С какими ограничениями брандмауэра сталкивается TRTC?

SDK использует протокол UDP для передачи аудио и видео, поэтому его нельзя использовать в корпоративных сетях, которые блокируют UDP. Если вы столкнулись с такой проблемой, см. [Ограничения брандмауэра](https://intl.cloud.tencent.com/document/product/647/35164).

### Что мне делать, если при установке или сборке TRTC Electron SDK возникает ошибка?

## Дополнительная информация

- [Руководство по API SDK](https://web.sdk.qcloud.com/trtc/electron/doc/en-us/trtc_electron_sdk/TRTCCloud.html)
- [Примечания к выпуску (Electron)](https://intl.cloud.tencent.com/document/product/647/38702)
- [Исходный код простой демонстрации](https://github.com/LiteAVSDK/TRTC_Electron/tree/main/TRTCSimpleDemo)
- [Исходный код примера API](https://github.com/LiteAVSDK/TRTC_Electron/tree/main/TRTC-API-Example)
- [Часто задаваемые вопросы](https://intl.cloud.tencent.com/document/product/647/43093)


---
*Источник: [https://trtc.io/document/35097](https://trtc.io/document/35097)*

---
*Источник (EN): [2importing-the-sdk.md](2-импорт-sdk.md)*

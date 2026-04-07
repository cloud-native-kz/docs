# UIKitProvider

## Введение

`UIKitProvider` — это React Context Provider для глобального управления состоянием, таким как тема и интернационализация для всего приложения. Это основа системы компонентов UIKit, обеспечивающая единообразный Context дочерним компонентам для согласованных тем стилей, многоязычной поддержки и конфигурации компонентов.

Поставщик имеет следующие особенности:

- **Управление темой** — поддержка переключения светлой и темной темы и настройка темы
- **Поддержка интернационализации** — встроенная многоязычная поддержка с расширяемыми пользовательскими языковыми пакетами

## Компонент UIKitProvider

### Параметры Props

| Параметр | Тип | Значение по умолчанию | Описание |
| --- | --- | --- | --- |
| language | string | 'auto' | Настройка языка |
| languageResources | LanguageResource[] | [] | Пользовательский языковой ресурс |
| theme | 'light' \| 'dark' | 'light' | Настройки темы |

### Определение типа

```
interface UIKitProviderProps {  language?: string;  languageResources?: ILanguageResource[];  theme?: 'light' | 'dark';}
```

### Определение типа языкового ресурса

```
interface LanguageResource {  lng: string;  translation: Record<string, any>;}
```

## Hook useUIKit

### Возвращаемое значение

| Поле | Тип | Описание |
| --- | --- | --- |
| language | string | текущий язык |
| setLanguage | (lng: string) => void | Метод установки языка |
| t | i18n['t'] | Функция перевода интернационализации |
| i18n | i18n | экземпляр i18next |
| theme | 'light' \| 'dark' | текущая тема |
| setTheme | React.Dispatch<React.SetStateAction<ThemeType>> | Метод установки темы |

## Примеры использования

### Базовое использование

Самый простой способ использования, предоставляющий основу для поддержки тем и языков:

```
import React from 'react';import { UIKitProvider, useUIKit } from '@tencentcloud/chat-uikit-react';function App() {  return (    <UIKitProvider theme="light" language="zh-CN">      <ChatApp />    </UIKitProvider>  );}function ChatApp() {  const { theme, language } = useUIKit();    return (    <div>      <p>Current theme: {theme}</p>      <p>Current language: {language}</p>    </div>  );}export default App;
```

### Переключение темы

Демонстрация реализации функциональности переключения темы

```
import React from 'react';import { UIKitProvider, useUIKit } from '@tencentcloud/uikit-base-component-react';function App() {  return (    <UIKitProvider theme="light">      <ThemeDemo />    </UIKitProvider>  );}function ThemeDemo() {  const { theme, setTheme } = useUIKit();  const toggleTheme = () => {    setTheme(theme === 'light' ? 'dark' : 'light');  };  return (    <div>      <h2>Theme Switching Example</h2>      <p>Current theme: {typeof theme === 'string' ? theme : `${theme.mode} (${theme.primaryColor})`}</p>      <button onClick={toggleTheme}>        Switch to {theme === 'light' ? 'dark' : 'light'} theme      </button>    </div>  );}export default App;
```

### Многоязычная поддержка

Демонстрация использования функции многоязычности:

```
import React from 'react';import { UIKitProvider, useUIKit } from '@tencentcloud/uikit-base-component-react';// Custom Language Resourceconst customLanguageResources = [  {    lng: 'de',    translation: {      'Hello': 'Hallo',      'Welcome': 'Willkommen',      'Settings': 'Einstellungen',    }  },  {    lng: 'fr',    translation: {      'Hello': 'Bonjour',      'Welcome': 'Bienvenue',      'Settings': 'ParamÃ¨tres',    }  }];function App() {  return (    <UIKitProvider       language="zh-CN"       languageResources={customLanguageResources}    >      <LanguageDemo />    </UIKitProvider>  );}function LanguageDemo() {  const { language, setLanguage, t } = useUIKit();  const languages = [    { code: 'zh-CN', name: 'Chinese' },    { code: 'en-US', name: 'English' },    { code: 'de', name: 'Deutsch' },    { code: 'fr', name: 'FranÃ§ais' },  ];  return (    <div>      <h2>{t('Settings')}</h2>      <p>{t('Welcome')}</p>      <p>Current language: {language}</p>      <div>        {languages.map(lang => (          <button             key={lang.code}            onClick={() => setLanguage(lang.code)}            style={{               margin: '0 8px',              fontWeight: language === lang.code ? 'bold' : 'normal'            }}          >            {lang.name}          </button>        ))}      </div>    </div>  );}export default App;
```

## Рекомендации по использованию

### Уровень Provider

```
// Recommend: Use UIKitProvider at the root partfunction App() {  return (    <UIKitProvider theme="light" language="zh-CN">      <Router>        <Routes>          <Route path="/" element={<Home />} />          <Route path="/chat" element={<Chat />} />        </Routes>      </Router>    </UIKitProvider>  );}
```

### 2. Сохранение темы

```
function App() {  const [theme, setTheme] = useState(() => {    return localStorage.getItem('theme') || 'light';  });  useEffect(() => {    localStorage.setItem('theme', theme);  }, [theme]);  return (    <UIKitProvider theme={theme}>      <AppContent />    </UIKitProvider>  );}
```

### Определение языка

```
function App() {  const [language, setLanguage] = useState(() => {    const saved = localStorage.getItem('language');    if (saved) return saved;        // Automatically detect browser language    const browserLang = navigator.language;    if (browserLang.startsWith('zh')) return 'zh-CN';    if (browserLang.startsWith('en')) return 'en-US';    return 'auto';  });  return (    <UIKitProvider language={language} languageResources={customResources}>      <App />    </UIKitProvider>  );}
```

## Важные замечания

1. **Расположение Provider**: UIKitProvider должен находиться в верхнем слое компонентов, использующих useUIKit.
2. **Переключение темы**: переключение темы вызывает обновление переменных CSS и может повлиять на производительность.
3. **Языковой ресурс**: пользовательские языковые ресурсы будут объединены со встроенными ресурсами. Идентичные ключи переопределяют встроенные ресурсы.
4. **Обновление конфигурации**: обновления конфигурации реактивны и немедленно влияют на ВСЕ связанные компоненты.
5. **Безопасность типов**: при использовании TypeScript убедитесь, что входная конфигурация соответствует определению типа.


---
*Источник: [https://trtc.io/document/72048](https://trtc.io/document/72048)*

---
*Источник (EN): [uikitprovider.md](./uikitprovider.md)*

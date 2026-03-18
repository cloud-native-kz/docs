# Поиск

## Обзор компонента

Search — это полнофункциональное решение для поиска с полным набором компонентов, включая поисковую строку, отображение результатов, расширенный поиск и другие функции. Он подходит для поиска пользователей, групп и сообщений в сценариях мгновенного обмена сообщениями, онлайн-конференций и онлайн-образования.

> **Примечание:** Эта функция относится к VAS. Вам необходимо приобрести плагин облачного поиска. Пожалуйста, нажмите [приобрести](https://console.trtc.io/chat/plugin/TUICloudSearch).

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d66ac806621811f091585254001c06ec.png)

## Архитектура компонента

```
Search (main component)
├── SearchBar              # Search bar component
├── SearchResults          # Search result component
├── SearchAdvanced         # Advanced search component
├── SearchResultsItem      # Search result item component
│   ├── User               # User result item
│   ├── Group              # Group result item
│   ├── Message            # Message result item
│   └── Conversation       # Session result item
```

## Режимы поиска

| **Мини-режим** | **Стандартный режим** | **Встроенный режим** |
| --- | --- | --- |
| Подходит для боковой панели или небольшого контейнераОтображает ограниченное количество результатовПоддерживает расширение для просмотра большего количества | Подходит для полноэкранного интерфейса поискаДемонстрация функцийПоддержка расширенного поиска | Подходит для интерфейса чатаСосредоточен на поиске сообщенийОптимизированная разметка |
|  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/9041fa01622911f0b324525400e889b2.png) |  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2019d8cc622a11f0bac1525400454e06.png) |  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/eeff790f622911f091585254001c06ec.png) |

## Свойства

| Название атрибута | Тип | Значение по умолчанию | Описание |
| --- | --- | --- | --- |
| variant | VariantType | VariantType.MINI | Режим поиска: mini, standard, embedded |
| SearchBar | React.ComponentType<SearchBarProps> | DefaultSearchBar | Компонент пользовательского поиска |
| SearchResults | React.ComponentType<SearchResultsProps> | DefaultSearchResults | Компонент пользовательского отображения результатов |
| SearchAdvanced | React.ComponentType<SearchAdvancedProps> | DefaultSearchAdvanced | Компонент пользовательского расширенного поиска |
| SearchResultsPresearch | React.ComponentType | - | Компонент заполнителя поиска |
| SearchResultsLoading | React.ComponentType | - | Компонент заполнителя загрузки |
| SearchResultsEmpty | React.ComponentType | - | Компонент заполнителя пустого результата |
| SearchResultItem | React.ComponentType<ResultItemProps> | - | Компонент пользовательского элемента результата поиска |
| debounceTime | number | 300 | Время дебаунса поиска (мс) |
| autoFocus | boolean | false | Автоматический фокус на поисковую строку |
| className | string | - | Название пользовательского класса стиля |
| style | React.CSSProperties | - | пользовательский стиль |
| onKeywordChange | (keyword: string) => void | - | обратный вызов при изменении ключевого слова поиска |
| onSearchComplete | (results: Map<SearchType, SearchResult>) => void | - | обратный вызов при завершении поиска |
| onResultItemClick | (data: SearchResultItem, type: SearchType) => void | - | обратный вызов при клике на результат поиска |
| onError | (error: Error) => void | - | обратный вызов при ошибке поиска |

## Базовое использование

```
import { Search, VariantType } from '@tencentcloud/chat-uikit-react';

function App() {
  return (
    <Search
      variant={VariantType.STANDARD}
      onResultItemClick={(data, type) => {
        console.log('Search result click:', data, type);
      }}
    />
  );
}
```

## Пользовательские возможности

`Search` предоставляет пользователям различные и многомерные API Props, позволяя им настраивать функции, пользовательский интерфейс и модули.

Компонент `Search` предоставляет несколько заменяемых подкомпонентов, позволяя пользователям настраивать `SearchBar`, `SearchResults`, `SearchAdvanced`, `SearchResultItem`, `SearchResultsPresearch`, `SearchResultsLoading`, `SearchResultsEmpty`. Пользователи также могут использовать компоненты по умолчанию для вторичной разработки и настройки.

Пользовательская поисковая строка

Пользовательские результаты поиска

Пользовательский расширенный поиск

Пользовательский элемент результата поиска

Компонент пользовательского заполнителя

**Свойства**

| Название атрибута | Тип | Значение по умолчанию | Описание |
| --- | --- | --- | --- |
| data | SearchResultItem | - | данные результата поиска |
| type | SearchType | - | тип результата поиска |
| keyword | string | - | ключевое слово поиска |
| onClick | (data: SearchResultItem, type: SearchType) => void | - | обратный вызов при клике |
| className | string | - | Название пользовательского класса стиля |

**Пример**

```
const CustomSearchBar = ({ value, onChange, onClear, placeholder }) => (
  <div className="custom-search-bar">
    <input
      type="text"
      value={value}
      onChange={onChange}
      placeholder={placeholder}
    />
    {value && <button onClick={onClear}>Clear</button>}
  </div>
);

<Search SearchBar={CustomSearchBar} />
```

**Свойства**

| Название атрибута | Тип | Значение по умолчанию | Описание |
| --- | --- | --- | --- |
| results | `Map<SearchType, SearchResult>` | - | данные результата поиска |
| isLoading | `boolean` | - | загружается ли |
| error | `Error \| null` | - | Сообщение об ошибке |
| keyword | `string` | - | ключевое слово поиска |
| typeLabels | `Record<SearchType, string>` | - | метка типа поиска |
| onLoadMore | `(type: SearchType) => void` | - | обратный вызов для загрузки большего |
| onResultItemClick | `(data: SearchResultItem, type: SearchType) => void` | - | обратный вызов при клике на элемент результата |
| SearchResultsLoading | `React.ComponentType` | `Loading` | компонент пользовательской загрузки |
| SearchResultsPresearch | `React.ComponentType` | - | компонент заполнителя поиска |
| SearchResultsEmpty | `React.ComponentType` | `EmptyResult` | компонент заполнителя пустого результата |
| SearchResultItem | `React.ComponentType<ResultItemProps>` | `DefaultSearchResultsItem` | компонент пользовательского элемента результата |
| variant | `VariantType` | `VariantType.STANDARD` | режим отображения |
| searchType | `SearchType \| 'all'` | `'all'` | текущий тип поиска |

**Пример**

```
const CustomSearchResults = ({ results, keyword, onResultItemClick }) => (
  <div className="custom-results">
    {Array.from(results.entries()).map(([type, result]) => (
      <div key={type}>
        <h3>{type}</h3>
        {result.resultList.map((item, index) => (
          <div key={index} onClick={() => onResultItemClick(item, type)}>
            {/* Custom result item */}
          </div>
        ))}
      </div>
    ))}
  </div>
);

<Search SearchResults={CustomSearchResults} />
```

**Свойства**

| Название атрибута | Тип | Значение по умолчанию | Описание |
| --- | --- | --- | --- |
| variant | `VariantType` | - | режим отображения |
| searchType | `SearchTabType` | - | текущий тип поиска |
| advancedParams | `Map<SearchType, SearchParamsMap[SearchType]>` | - | параметры расширенного поиска |
| onAdvancedParamsChange | `(type: SearchType, params: SearchParamsMap[SearchType]) => void` | - | обратный вызов при изменении параметра |

**Пример**

```
SearchAdvanced
```

**Свойства**

| Название атрибута | Тип | Значение по умолчанию | Описание |
| --- | --- | --- | --- |
| data | `SearchResultItem` | - | данные результата поиска |
| type | `SearchType` | - | тип результата поиска |
| keyword | `string` | - | ключевое слово поиска |
| onClick | `(data: SearchResultItem, type: SearchType) => void` | - | обратный вызов при клике |
| className | `string` | - | Название пользовательского класса стиля |

**Пример**

```
SearchResultItem
```

**Свойства**

| Название атрибута | Тип | Значение по умолчанию | Описание |
| --- | --- | --- | --- |
| SearchResultsPresearch | `React.ComponentType` | - | компонент заполнителя поиска |
| SearchResultsLoading | `React.ComponentType` | - | компонент заполнителя загрузки |
| SearchResultsEmpty | `React.ComponentType` | - | компонент заполнителя пустого результата |

**Пример**

```
<Search
  SearchResultsPresearch={() => <div>Enter keywords to start search</div>}
  SearchResultsLoading={() => <div>Searching...</div>}
  SearchResultsEmpty={() => <div>No result found</div>}
/>
```

## Часто задаваемые вопросы

### Как настроить формат отображения результатов поиска

О: Используйте свойство `SearchResultItem` для импорта пользовательского компонента.

### Как решить проблемы производительности поиска

О: Отрегулируйте `debounceTime`, используйте React.memo и рассмотрите кеширование результатов.

### Как оптимизировать мобильный терминал

О: Компонент автоматически адаптируется к мобильным терминалам и может быть дополнительно настроен через CSS.

### Как поддерживать многоязычность

О: Компонент имеет встроенную поддержку интернационализации. Используйте `useUIKit` для получения переводов.


---
*Источник: [https://trtc.io/document/72091](https://trtc.io/document/72091)*

---
*Источник (EN): [search.md](./search.md)*

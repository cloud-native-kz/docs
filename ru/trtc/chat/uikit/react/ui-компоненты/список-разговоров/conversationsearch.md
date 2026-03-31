# ConversationSearch

`ConversationSearch` использует компонент Search, поддерживающий функциональность поиска по пользователям, группам и сообщениям. Он интегрирует такие функции как строка поиска, расширенный поиск и отображение результатов поиска.

## Основное использование

```
SearchResultItem
```

## Props

| **Имя параметра** | **Тип** | **Значение по умолчанию** | **Описание** |
| --- | --- | --- | --- |
| visible | boolean | true | Видимость компонента. |
| [Search](/document/product/182866808150605824) | ComponentType<SearchProps> | - | пользовательский компонент поиска |
| variant | VariantType | VariantType.MINI | Режим поиска: mini, standard, embedded |
| [SearchBar](/document/product/182866808150605824#.E8.87.AA.E5.AE.9A.E4.B9.89.E8.83.BD.E5.8A.9B) | React.ComponentType<SearchBarProps> | DefaultSearchBar | пользовательский компонент строки поиска |
| [SearchResults](/document/product/182866808150605824#.E8.87.AA.E5.AE.9A.E4.B9.89.E8.83.BD.E5.8A.9B) | React.ComponentType<SearchResultsProps> | DefaultSearchResults | пользовательский компонент результатов поиска |
| [SearchAdvanced](/document/product/182866808150605824#.E8.87.AA.E5.AE.9A.E4.B9.89.E8.83.BD.E5.8A.9B) | React.ComponentType<SearchAdvancedProps> | DefaultSearchAdvanced | пользовательский компонент расширенного поиска |
| SearchResultsPresearch | React.ComponentType | - | компонент заполнителя поиска |
| SearchResultsLoading | React.ComponentType | - | компонент заполнителя загрузки |
| SearchResultsEmpty | React.ComponentType | - | компонент заполнителя пустого результата |
| SearchResultItem | React.ComponentType<ResultItemProps> | - | пользовательский компонент элемента результата поиска |
| debounceTime | number | 300 | время debounce поиска (мс) |
| autoFocus | boolean | false | Автоматический фокус на поле поиска |
| className | string | - | пользовательское имя класса стиля |
| style | React.CSSProperties | - | пользовательский стиль |
| onKeywordChange | (keyword: string) => void | - | обратный вызов при изменении ключевых слов поиска |
| onSearchComplete | (results: Map<SearchType, SearchResult>) => void | - | обратный вызов при завершении поиска |
| onResultItemClick | (data: SearchResultItem, type: SearchType) => void | - | обратный вызов при клике на результат поиска |
| onError | (error: Error) => void | - | обратный вызов ошибки |

###


---
*Источник: [https://trtc.io/document/64706](https://trtc.io/document/64706)*

---
*Источник (EN): [conversationsearch.md](./conversationsearch.md)*

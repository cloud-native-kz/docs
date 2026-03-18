# Search State

SearchState — это хук управления состоянием поиска на основе Zustand, предоставляющий полные возможности управления статусом для компонента Search. Поддерживает различные режимы поиска (стандартный режим, встроенный режим) и управляет ключевыми словами поиска, результатами поиска, статусом загрузки, обработкой ошибок и другими функциями. Если возможности настройки компонента недостаточны для вашего бизнеса, вы можете использовать SearchState для реализации ваших потребностей.

#### Данные

| Имя атрибута | Тип | Описание |
| --- | --- | --- |
| keyword | string | текущее ключевое слово поиска |
| results | Map<SearchType, SearchResult<SearchType>> | набор результатов поиска |
| isLoading | boolean | выполняется ли поиск |
| error | Error \| null | информация об ошибке |
| searchAdvancedParams | Map<ISearchType, SearchParamsMap[SearchType]> | Расширенные параметры поиска |
| selectedSearchType | SearchType \| 'all' | Текущий тип поиска |

#### Метод операции

| Имя метода | Тип | Описание |
| --- | --- | --- |
| setKeyword | (k: string) => void | Установить ключевое слово поиска |
| loadMore | (type?: SearchType) => Promise<void> | Загрузить больше результатов поиска |
| setSelectedType | (type: SearchType \| 'all') => void | Установить тип поиска |
| setSearchMessageAdvancedParams | (params: SearchCloudMessagesParams) => void | Установить расширенные параметры поиска сообщений |
| setSearchUserAdvancedParams | (params: SearchCloudUsersParams) => void | Установить расширенные параметры поиска пользователей |
| setSearchGroupAdvancedParams | (params: SearchCloudGroupsParams) => void | Установить расширенные параметры поиска групп |

## Примеры использования

```
import { useSearchState, VariantType } from '@tencentcloud/chat-uikit-react';const {    keyword,    results,    isLoading,    error,    setKeyword,    setSelectedType,    loadMore  } = useSearchState(VariantType.STANDARD);
```

##


---
*Источник: [https://trtc.io/document/72092](https://trtc.io/document/72092)*

---
*Источник (EN): [search-state.md](./search-state.md)*

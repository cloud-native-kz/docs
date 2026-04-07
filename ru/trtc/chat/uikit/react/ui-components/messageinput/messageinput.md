# MessageInput

## Обзор

MessageInput — это полнофункциональный компонент ввода сообщений, предоставляющий основные функции ввода чата, такие как редактирование текста, выбор эмодзи, вложение файлов и кнопка отправки. Поддерживает различные пользовательские параметры, включая конфигурацию поведения ввода, настройку панели инструментов, замену компонентов и расширение слотов, удовлетворяя персонализированным требованиям различных сценариев чата.

## Props

| Поле | Тип | Значение по умолчанию | Описание |
| --- | --- | --- | --- |
| [autoFocus](#0633f6e0-65d3-41d6-a379-cb3bded1cbe6) | boolean | true | Автоматически ли фокусировать ввод при монтировании |
| [disabled](#8c176ad9-d21a-4630-b391-4b875c9c38e4) | boolean | false | Отключить ли компонент ввода |
| [hideSendButton](#b8151dc8-e87b-4237-a5e7-2530fbfbf3a6) | boolean | false | Скрывать ли кнопку отправки |
| [placeholder](#da6cb1d1-3a46-4e13-8e74-42f8fefb9f2c) | string | '' | Текст подсказки в поле ввода |
| [className](#12dafe1a-7a5e-4b65-bb6e-2aaf3a43563a) | string | undefined | Пользовательское имя класса CSS корневого контейнера |
| [style](#89805682-5b73-4480-b45a-7e441b3cce5d) | React.CSSProperties | undefined | Пользовательский встроенный стиль корневого контейнера |
| [attachmentPickerMode](#e7acec21-6bf4-435e-b6c2-d9d74093dfbb) | 'collapsed' \| 'expanded' | 'collapsed' | Режим отображения селектора вложений |
| [actions](#17ac5267-8cad-460e-ad41-444702871b93) | MessageInputActions | ['EmojiPicker', 'AttachmentPicker'] | Конфигурация кнопок действий панели инструментов |
| [slots](#f1a3b8c4-0ab6-46bd-b2b0-453d06738818) | MessageInputSlots | undefined | Объект конфигурации слотов |
| [TextEditor](#abb5c4e3-61e1-4909-ae58-d29e8e95e88b) | JSX.Element | undefined | Пользовательский компонент текстового редактора |
| [EmojiPicker](#29fef4a0-d8fb-4d5c-9eee-df7c3c2af65b) | JSX.Element | undefined | Пользовательский компонент селектора эмодзи |
| [AttachmentPicker](#75289d5b-078f-4b09-a351-4490ec9663a6) | JSX.Element | undefined | Пользовательский компонент селектора вложений |
| [FilePicker](#e7acec21-6bf4-435e-b6c2-d9d74093dfbb) | JSX.Element | undefined | Пользовательский компонент селектора файлов |
| [ImagePicker](#e7acec21-6bf4-435e-b6c2-d9d74093dfbb) | JSX.Element | undefined | Пользовательский компонент селектора изображений |
| [VideoPicker](#e7acec21-6bf4-435e-b6c2-d9d74093dfbb) | JSX.Element | undefined | Пользовательский компонент селектора видео |

## Объяснение Props

### autoFocus

**тип**: `boolean`

autoFocus используется для установки автоматической фокусировки на поле ввода при монтировании, значение по умолчанию — `true`.

### disabled

**тип**: `boolean`

disabled используется для отключения всего компонента ввода, включая текстовый ввод и все кнопки операций, значение по умолчанию — `false`.

### hideSendButton

**тип**: `boolean`

hideSendButton используется для скрытия кнопки отправки, подходит для сценариев, когда требуется пользовательский режим триггера отправки, значение по умолчанию — `false`.

### placeholder

**тип**: `string`

placeholder используется для установки текста подсказки в поле ввода, значение по умолчанию — пустая строка.

### className

**тип**: `string`

className используется для установки пользовательского имени класса CSS для корневого контейнера, значение по умолчанию — `undefined`.

### style

**тип**: `React.CSSProperties`

style используется для установки пользовательского встроенного стиля для корневого контейнера, значение по умолчанию — `undefined`.

### attachmentPickerMode

**тип**: `'collapsed' | 'expanded'`

attachmentPickerMode используется для установки режима отображения селектора вложений, значение по умолчанию — `'collapsed'`.

- `collapsed`: режим сворачивания, разворачивание параметров после клика
- `expanded`: расширенный режим, вывод всех параметров напрямую

> **Примечание:** По умолчанию AttachmentPicker относится к селектору вложений, включая выбор файлов, выбор изображений и выбор видео. Когда attachmentPickerMode имеет значение "collapsed", клик по селектору вложений выводит меню с выбором файлов, выбором изображений и выбором видео. Когда attachmentPickerMode имеет значение "expanded", селектор вложений разворачивается по умолчанию, выводя выбор файлов, выбор изображений и выбор видео в плиточном представлении.

### actions

**тип**: `MessageInputActions`

Actions для конфигурации кнопок действий панели инструментов, значение по умолчанию `['EmojiPicker', 'AttachmentPicker']`.

```
type BuiltInAction =  | 'EmojiPicker'  | 'ImagePicker'  | 'FilePicker'  | 'VideoPicker'  | 'AttachmentPicker';type CustomAction = {  key: string;  label?: string | undefined;  component?: React.ComponentType<any> | undefined;  className?: string | undefined;  style?: React.CSSProperties | undefined;  iconSize?: number | undefined;};type MessageInputActions = Array<BuiltInAction | CustomAction>;
```

#### Пример 1: Настройка последовательности кнопок панели инструментов

```
import { Chat, MessageInput } from '@tencentcloud/chat-uikit-react';function ChatWithCustomActions() {  // Пользовательская последовательность кнопок: файл, изображение, видео, эмодзи  const customActions = ['FilePicker', 'ImagePicker', 'VideoPicker', 'EmojiPicker'];    return (    <Chat>      <MessageInput actions={customActions} />    </Chat>  );}
```

Результат отображения показан на рисунке ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c7b9cdb0623d11f0bac1525400454e06.png)

#### Пример 2: Добавление пользовательских кнопок действий — система быстрого ответа в центре обслуживания

```
import { Chat, MessageInput, useMessageInputState } from '@tencentcloud/chat-uikit-react';// Компонент быстрого ответаfunction QuickReplyPicker() {  const { setContent } = useMessageInputState();    const quickReplies = [    'Hello, happy to serve you!',    'Please wait, I will check for you...',    'Thank you for your consultation, any other issues?',    The issue has been resolved. Have a pleasant life!,  ];  const handleQuickReply = (text: string) => {    setContent(text);  };  return (    <div style={{ position: 'relative' }}>      <button title="quick reply">â¡</button>      <div style={{        position: 'absolute',        bottom: '100%',        left: 0,        background: 'white',        border: '1px solid #ccc',        borderRadius: '4px',        padding: '8px',        minWidth: '200px'      }}>        {quickReplies.map((reply, index) => (          <div            key={index}            onClick={() => handleQuickReply(reply)}            style={{              padding: '4px 8px',              cursor: 'pointer',              borderRadius: '2px'            }}          >            {reply}          </div>        ))}      </div>    </div>  );}function CustomerServiceChat() {  const actions = [    {      key: 'quickReply',      label: 'quick reply',      component: QuickReplyPicker    },    'EmojiPicker',    'FilePicker'  ];    return (    <Chat>      <MessageInput actions={actions} />    </Chat>  );}
```

Результат отображения показан на рисунке ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/d9f5658666d511f0924f5254005ef0f7.png)

### slots

**тип**: `MessageInputSlots`

Slots используются для вставки пользовательского содержимого в определенные места компонента ввода, значение по умолчанию — `undefined`.

```
interface MessageInputSlots {  headerToolbar?: () => React.ReactNode;  footerToolbar?: () => React.ReactNode;  leftInline?: () => React.ReactNode;  rightInline?: () => React.ReactNode;  inputPrefix?: () => React.ReactNode;  inputSuffix?: () => React.ReactNode;}
```

![Диаграмма архитектуры MessageInput](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c7d0aae5623d11f0ad0f5254005ef0f7.png)

#### Пример 1: Добавление отображения статистики сообщений

```
import { Chat, MessageInput, useMessageInputState } from '@tencentcloud/chat-uikit-react';function ChatWithMessageStats() {  const { inputRawValue } = useMessageInputState();    // Верхняя панель инструментов: отображение статистики символов  const HeaderToolbar = () => !inputRawValue    ? null    : (      <div style={{        padding: '4px 12px',        fontSize: '12px',        color: '#666',        borderBottom: '1px solid #eee',      }}      >        Character count:        {' '}        {inputRawValue?.reduce((acc, item) => acc + (item.type === 'text' ? item.content.length : 1), 0) || 0}        /500      </div>    );  // Панель инструментов: отображение уведомления отправки  const FooterToolbar = () => (    <div style={{      padding: '4px 12px',      fontSize: '12px',      color: '#999',      textAlign: 'right'    }}>      Press Ctrl+Enter to enter a new line    </div>  );  return (    <Chat>      <MessageInput         slots={{          headerToolbar: HeaderToolbar,          footerToolbar: FooterToolbar        }}      />    </Chat>  );}
```

Результат отображения показан на рисунке ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c7b8bf50623d11f0a64452540099c741.png)

#### Пример 2: Функция префикса/суффикса поля ввода

```
import { Chat, MessageInput } from '@tencentcloud/chat-uikit-react';function ChatWithInputPrefixSuffix() {  // Префикс поля ввода: функция @напоминание  const InputPrefix = () => (    <button       style={{         border: 'none',         background: 'transparent',        color: '#1890ff',        cursor: 'pointer'      }}      onClick={() => {        // Триггер выбора @пользователя        console.log('toggle on @user selection')      }}    >      @    </button>  );  // Суффикс поля ввода: голосовой ввод  const InputSuffix = () => (    <button      style={{        border: 'none',        background: 'transparent',        cursor: 'pointer'      }}      onClick={() => {        // Начать голосовой ввод        console.log('start voice input')      }}    >      ð¤    </button>  );  return (    <Chat>      <MessageInput         slots={{          inputPrefix: InputPrefix,          inputSuffix: InputSuffix        }}      />    </Chat>  );}
```

Результат отображения показан на рисунке ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c7d0d55c623d11f097ec52540044a08e.png)

#### Пример 3: Полная настройка панели инструментов с обеих сторон

```
import { Chat, MessageInput } from '@tencentcloud/chat-uikit-react';function ChatWithCustomToolbars() {  // Левая панель инструментов: оставить только эмодзи и изображения  const LeftInline = () => (    <div style={{ display: 'flex', gap: '8px' }}>      <button>ð</button>      <button>ð·</button>    </div>  );  // Панель инструментов справа: пользовательская область отправки  const RightInline = () => (    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>      <span style={{ fontSize: '12px', color: '#666' }}>        Enter      </span>      <button        style={{          padding: '6px 12px',          background: '#1890ff',          color: 'white',          border: 'none',          borderRadius: '4px',          cursor: 'pointer'        }}      >        Send      </button>    </div>  );  return (    <Chat>      <MessageInput         slots={{          leftInline: LeftInline,          rightInline: RightInline        }}      />    </Chat>  );}
```

Результат отображения показан на рисунке ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c7b6dc29623d11f0a64452540099c741.png)

### TextEditor

**тип**: `JSX.Element`

TextEditor используется для замены компонента текстового редактора по умолчанию. Значение по умолчанию: `undefined`.

#### Пример: интеграция редактора с расширенным форматированием

```
import { Chat, MessageInput, useMessageInputState } from '@tencentcloud/chat-uikit-react';// Пользовательский редактор с расширенным форматированиемfunction RichTextEditor() {  const { sendMessage } = useMessageInputState();  const [inputValue, setInputValue] = useState('');  const handleContentChange = (content: string) => {    setInputValue(content);  };  const handleKeyDown = (e: React.KeyboardEvent) => {    // Enter для отправки сообщения    if (e.key === 'Enter') {      // Триггер логики отправки      e.preventDefault();      sendMessage(inputValue);      // Очистить ввод в редактируемом div      const editableDiv = document.querySelector('.editable-div');      if (editableDiv) {        editableDiv.textContent = '';      }    }  };  return (    <div style={{      flex: 1,      border: '1px solid #d9d9d9',      borderRadius: '6px',      padding: '8px 12px',      minHeight: '32px',      maxHeight: '120px',      overflow: 'auto',    }}    >      <div        contentEditable        className="editable-div"        style={{          outline: 'none',          minHeight: '20px',          lineHeight: '20px',        }}        onInput={(e) => {          handleContentChange(e.currentTarget.textContent || '');        }}        onKeyDown={handleKeyDown}      />    </div>  );}function ChatWithRichTextEditor() {  return (    <Chat>      <MessageInput TextEditor={<RichTextEditor />} />    </Chat>  );}
```

Результат отображения показан на рисунке ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c7b56124623d11f0bac1525400454e06.png)

### EmojiPicker

**тип**: `JSX.Element`

EmojiPicker заменяет компонент селектора эмодзи по умолчанию, значение по умолчанию `undefined`.

#### Пример: пользовательская панель эмодзи

```
import { Chat, MessageInput, useMessageInputState } from '@tencentcloud/chat-uikit-react';// Пользовательский селектор эмодзиfunction CustomEmojiPicker() {  const { insertContent } = useMessageInputState();  const emojiCategories = {    common: ['ð', 'ð', 'ð¥°', 'ð', 'ð¤', 'ð­', 'ð¡', 'ð'],    hands: ['ð', 'ð¤', 'ð', 'ð', 'âï¸', 'ð¤', 'ð¤', 'ð'],    animals: ['ð¶', 'ð±', 'ð­', 'ð¹', 'ð°', 'ð¦', 'ð»', 'ð¼'],  };  const [activeCategory, setActiveCategory] = useState('common');  const [showPicker, setShowPicker] = useState(false);  const insertEmoji = (emoji: string) => {    insertContent(emoji);    setShowPicker(false);  };  return (    <div style={{ position: 'relative' }}>      <button        onClick={() => setShowPicker(!showPicker)}        style={{ border: 'none', background: 'transparent', cursor: 'pointer' }}      >        ð      </button>      {showPicker && (        <div style={{          position: 'absolute',          bottom: '100%',          left: 0,          background: 'white',          border: '1px solid #ccc',          borderRadius: '8px',          padding: '12px',          width: '280px',          boxShadow: '0 4px 12px rgba(0,0,0,0.1)',        }}        >          {/* Тег категории */}          <div style={{ display: 'flex', marginBottom: '8px' }}>            {Object.keys(emojiCategories).map(category => (              <button                key={category}                onClick={() => setActiveCategory(category)}                style={{                  padding: '4px 8px',                  border: 'none',                  background: activeCategory === category ? '#1890ff' : 'transparent',                  color: activeCategory === category ? 'white' : '#666',                  borderRadius: '4px',                  cursor: 'pointer',                  fontSize: '12px',                }}              >                {category}              </button>            ))}          </div>          {/* Сетка эмодзи */}          <div style={{            display: 'grid',            gridTemplateColumns: 'repeat(8, 1fr)',            gap: '4px',          }}          >            {emojiCategories[activeCategory].map(emoji => (              <button                key={emoji}                onClick={() => insertEmoji(emoji)}                style={{                  border: 'none',                  background: 'transparent',                  fontSize: '20px',                  cursor: 'pointer',                  padding: '4px',                  borderRadius: '4px',                }}              >                {emoji}              </button>            ))}          </div>        </div>      )}    </div>  );}function ChatWithCustomEmoji() {  return (    <Chat>      <MessageInput EmojiPicker={<CustomEmojiPicker />} />    </Chat>  );}
```

Результат отображения показан на рисунке ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c7d124c8623d11f0b30d5254007c27c5.png)

### AttachmentPicker

**тип**: `JSX.Element`

AttachmentPicker используется для замены компонента селектора вложений по умолчанию, значение по умолчанию — `undefined`.

#### Пример: селектор вложений с интеграцией облачного хранилища

```
import { Chat, MessageInput } from '@tencentcloud/chat-uikit-react';// Селектор вложений с интеграцией облачного хранилищаfunction CloudAttachmentPicker() {  const [showPicker, setShowPicker] = useState(false);    const attachmentTypes = [    { key: 'local', label: 'local file', icon: 'ð' },    { key: 'cloud', label: 'cloud file', icon: 'âï¸' },    { key: 'recent', label: 'recent file', icon: 'ð' },    { key: 'screenshot', label: 'screenshot', icon: 'ð·' }  ];  const handleAttachmentSelect = async (type: string) => {    switch (type) {      case 'local':        // Открыть выбор локального файла        const input = document.createElement('input');        input.type = 'file';        input.multiple = true;        input.onchange = (e) => {          const files = (e.target as HTMLInputElement).files;          console.log('selected local files:', files);        };        input.click();        break;              case 'cloud':        // Триггер выбора облачного файла        console.log('Toggle on cloud file selection');        break;              case 'recent':        // Отобразить недавние файлы        console.log('Display recent files');        break;              case 'screenshot':        // Начать скриншот        console.log('start screenshot')        break;    }    setShowPicker(false);  };  return (    <div style={{ position: 'relative' }}>      <button         onClick={() => setShowPicker(!showPicker)}        style={{ border: 'none', background: 'transparent', cursor: 'pointer' }}      >        ð      </button>            {showPicker && (        <div style={{          position: 'absolute',          bottom: '100%',          left: 0,          background: 'white',          border: '1px solid #ccc',          borderRadius: '8px',          padding: '8px',          minWidth: '160px',          boxShadow: '0 4px 12px rgba(0,0,0,0.1)'        }}>          {attachmentTypes.map(type => (            <div              key={type.key}              onClick={() => handleAttachmentSelect(type.key)}              style={{                display: 'flex',                alignItems: 'center',                gap: '8px',                padding: '8px 12px',                cursor: 'pointer',                borderRadius: '4px',                fontSize: '14px'              }}            >              <span>{type.icon}</span>              <span>{type.label}</span>            </div>          ))}        </div>      )}    </div>  );}function ChatWithCloudAttachment() {  return (    <Chat>      <MessageInput AttachmentPicker={<CloudAttachmentPicker />} />    </Chat>  );}
```

Результат отображения показан на рисунке ниже:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/c7ba5f92623d11f092fe525400bf7822.png)

## Резюме

Компонент MessageInput предоставляет полную функциональность ввода сообщений и различные пользовательские параметры. Благодаря правильной конфигурации Props и использованию системы слотов вы можете создать интерфейс ввода, отвечающий конкретным бизнес-требованиям. Рекомендуется выбирать подходящую схему настройки на основе реальных сценариев использования и поддерживать хороший пользовательский опыт и производительность.


---
*Источник: [https://trtc.io/document/72088](https://trtc.io/document/72088)*

---
*Источник (EN): [messageinput.md](./messageinput.md)*

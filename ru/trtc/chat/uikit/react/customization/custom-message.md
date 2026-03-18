# Пользовательское сообщение

TUIKit предоставляет стандартную реализацию для отправки и отображения базовых типов сообщений, таких как текст, изображение, голос, видео и файл. Если эти типы сообщений не соответствуют вашим требованиям, вы можете добавить пользовательские типы сообщений.

## Базовый тип сообщения

| Тип сообщения | Эффект отображения |
| --- | --- |
| Текстовые сообщения |  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/09173f52621911f0ad0f5254005ef0f7.png) |
| Графические сообщения |  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/3a62057e621911f0ad0f5254005ef0f7.png) |
| Видеосообщения |  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/2d3e482a621a11f097ec52540044a08e.png) |
| Файловые сообщения |  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/63df7501621a11f0b324525400e889b2.png) |

## Пользовательское уведомление

Если базовый тип сообщения не соответствует вашим требованиям, вы можете использовать пользовательские сообщения в соответствии с актуальными потребностями вашего бизнеса.

| Предустановленный стиль пользовательского сообщения | Эффект отображения |
| --- | --- |
| Гипертекстовые сообщения |  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/36e096e5622b11f0bac1525400454e06.png) |
| Сообщения с рейтингом |  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/40124a67622b11f0b30d5254007c27c5.png) |
| Сообщения о заказе |  ![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/349600bd623111f0bac1525400454e06.png) |

В следующем контексте используется отправка гипертекста, который может переходить в браузер в качестве пользовательского сообщения, чтобы помочь вам быстро понять процесс реализации.

### Требуются пользовательские данные

Для сообщения, которое может перейти на другой веб-сайт, требуется текст описания и ссылка на URL.

```
import { TUIChatService } from "@tencentcloud/chat-uikit-engine";const sendCustomMessageParams = {    payload: {      data: JSON.stringify({        Welcome to the Tencent Cloud family        url: 'https://cloud.tencent.com/document/product/269'      }),      description: "text_with_link",      extension: "text_with_link"    },};// simulation send a custom messageTUIChatService.sendCustomMessage(sendCustomMessageParams)    .catch(err => { /** */ });
```

Отправка пользовательских сообщений. Ссылка на [документацию ChatEngine API](https://web.sdk.qcloud.com/im/doc/chat-engine/ITUIChatService.html#sendCustomMessage).

### 2. Создание компонентов для анализа пользовательских данных

Здесь создается компонент CustomMessage. Когда тип сообщения — это пользовательское сообщение и поле расширения сообщения равно определённому выше `text_with_link`, мы можем пользовательским образом отрендерить содержимое; если это другие типы сообщений, используйте компонент Message по умолчанию для отрендеривания.

```
import { TUIChatEngine } from '@tencentcloud/chat-uikit-engine';import { UIKitProvider,  Message } from '@tencentcloud/chat-uikit-react';function CustomMessage(props: React.ComponentProps<typeof Message>) {  if (props.message.type === TUIChatEngine.TYPES.MSG_CUSTOM) {    const { data, extension } = props.message.payload;    if (data && extension === 'text_with_link') {      const { text, url } = JSON.parse(data);      return (        <div style={{          backgroundColor: 'lightblue',          padding: '10px',          borderRadius: '10px',        }}        >          <div>{text}</div>          <a href={url} target="_blank" rel="noopener noreferrer">            Jump to          </a>        </div>      );    }  }  return <Message {...props} />;}function ChatApp() {  return (      <UIKitProvider language="auto" theme="light">        <div style={{ display: 'flex', height: '100vh' }}>          <ConversationList />          <MessageList Message={CustomMessage} />        </div>      </UIKitProvider>  );}export default ChatApp;
```


---
*Источник: [https://trtc.io/document/72002](https://trtc.io/document/72002)*

---
*Источник (EN): [custom-message.md](./custom-message.md)*

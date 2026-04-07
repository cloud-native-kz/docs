# Управление контекстом

Управление контекстом имеет большое значение для больших языковых моделей. Оно позволяет модели предоставлять более точные ответы на основе истории чата. Tencent Real-Time Communication (Tencent RTC) AI предлагает базовые возможности управления контекстом и также поддерживает разработчиков в создании собственных решений для управления богатым контекстом.

## Базовое управление контекстом:

Tencent RTC AI предоставляет базовые функции управления контекстом. В параметрах LLMConfig мы вводим параметр History для управления контекстом:

History:

- Используется для установки количества раундов контекста LLM со значением по умолчанию 0 (управление контекстом не предоставляется).
- Максимальное значение: 50 (управление контекстом предоставляется для последних 50 раундов).

Ниже приведен соответствующий пример конфигурации:

```
"LLMConfig": {          "LLMType": "openai",            "Model":"gpt-4o",          "APIKey":"api-key",          "APIUrl":"https://api.openai.com/chat/completions",          "Streaming": true,          "SystemPrompt": "You are a personal assistant",          "Timeout": 3.0,          "History": 5    // Up to 50 rounds of conversations are supported, with a default value of 0.  }
```

## Пользовательское управление контекстом:

Служба разговоров Tencent RTC AI поддерживает стандартные спецификации OpenAI, позволяя разработчикам реализовать пользовательское управление контекстом в своей собственной деятельности. Процесс реализации выглядит следующим образом:

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/7d5f0a6194dd11ef810152540055f650.png)

На этой диаграмме показаны основные этапы пользовательского управления контекстом. Разработчики могут корректировать и оптимизировать этот процесс в соответствии со своими конкретными потребностями.

### Пример реализации

Разработчики могут реализовать интерфейс большой языковой модели, совместимый с OpenAI API, на своем собственном бизнес-сервере и отправлять запросы больших языковых моделей, инкапсулированные с логикой контекста, в сторонние большие языковые модели. Вот упрощенный пример кода:

```
import timefrom fastapi import FastAPI, HTTPExceptionfrom fastapi.middleware.cors import CORSMiddlewarefrom pydantic import BaseModelfrom typing import List, Optionalfrom langchain_core.messages import HumanMessage, SystemMessagefrom langchain_openai import ChatOpenAIapp = FastAPI(debug=True)# Add CORS middleware.app.add_middleware(    CORSMiddleware,    allow_origins=["*"],    allow_credentials=True,    allow_methods=["*"],    allow_headers=["*"],)class Message(BaseModel):    role: str    content: strclass ChatRequest(BaseModel):    model: str    messages: List[Message]    temperature: Optional[float] = 0.7class ChatResponse(BaseModel):    id: str    object: str    created: int    model: str    choices: List[dict]    usage: dict@app.post("/v1/chat/completions")async def chat_completions(request: ChatRequest):    try:        # Convert the request message to the LangChain message format.        langchain_messages = []        for msg in request.messages:            if msg.role == "system":                langchain_messages.append(SystemMessage(content=msg.content))            elif msg.role == "user":                langchain_messages.append(HumanMessage(content=msg.content))        # Add more histories.        # Use LangChain's ChatOpenAI model.        chat = ChatOpenAI(temperature=request.temperature,                          model_name=request.model)        response = chat(langchain_messages)        print(response)        # Construct a response that conforms to the OpenAI API format.        return ChatResponse(            id="chatcmpl-" + "".join([str(ord(c))                                     for c in response.content[:8]]),            object="chat.completion",            created=int(time.time()),            model=request.model,            choices=[{                "index": 0,                "message": {                    "role": "assistant",                    "content": response.content                },                "finish_reason": "stop"            }],            usage={                "prompt_tokens": -1,  # LangChain does not provide this information, so we use a placeholder value.                "completion_tokens": -1,                "total_tokens": -1            }        )    except Exception as e:        raise HTTPException(status_code=500, detail=str(e))if __name__ == "__main__":    import uvicorn    uvicorn.run(app, host="0.0.0.0", port=8000)
```

[Нажмите, чтобы просмотреть пример](https://github.com/Tencent-RTC/trtc-conversation-ai-example).


---
*Источник: [https://trtc.io/document/65318](https://trtc.io/document/65318)*

---
*Источник (EN): [context-management.md](./context-management.md)*

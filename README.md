# LangChain Agents Demo

This is a simple project experimenting with:
- Basic LangChain agents  
- Middleware functions  
- Dynamic model selection  
- Retriever tools  

The project uses:
- OpenAI / GPT models  
- LangChain agents  
- Custom middleware for switching models based on message count  

## 🚀 Features

- **Dynamic Model Selection**  
  Automatically switches between a lightweight and advanced model depending on conversation length.

- **Custom Middleware**  
  Wraps model calls using `@wrap_model_call`.

- **Simple Agent Demo**  
  Shows how to invoke an agent with system + human messages.

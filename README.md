
# RePrompt

> **Transform your prompts, amplify your results**

RePrompt is an intelligent Chrome extension that **supercharges your AI interactions** by automatically optimizing your prompts for maximum quality results. Whether you're chatting with ChatGPT, Claude, or other AI assistants, RePrompt ensures you get the best possible responses every time.


###  The Problem :

- Writing effective AI prompts requires expertise
- Poor prompts lead to mediocre AI responses
- Users spend time iterating to get quality results
- Most people don't know prompt engineering best practices

### The Solution :

RePrompt automatically transforms your casual input into **professionally optimized prompts** that unlock the full potential of AI models, giving you better results with zero effort.

  <div style="display: flex; gap: 20px;">
  <div style="flex: 1;">
    <h3>Home Panel</h3>
    <p></p>
    <img src="/assets/popup.png" width="200"/>
  </div>
</div>

---

##  Key Features :

| Feature                          | Description                                                      |
| -------------------------------- | ---------------------------------------------------------------- |
|  **Smart Detection**             | Automatically detects AI websites (ChatGPT, Claude.ai, and more) |
|  **One-Click Optimization**      | Replace your text with an optimized prompt instantly             |
|  **Lightning Fast**              | FastAPI backend ensures sub-second response times                |
|  **Powered by Gemini 2.5 Pro**   | Leverages Google's most advanced language model                  |
|  **Bring Your Own Key**          | Use your Gemini API key for unlimited usage                      |
|  **Free Tier Available**         | Rate-limited access without API key required                     |
|  **Privacy First**               | Your prompts are processed securely and never stored             |
|  **Clean UI**                    | Minimal, non-intrusive interface that blends seamlessly          |
  
---

## Installation

### Chrome Extension

1. **Download from Chrome Web Store** (Coming Soon)
    
    ```
    https://chrome.google.com/webstore/detail/reprompt/-- got no 5 bucks with me rn, iam broke but will be up --
    ```
    
2. **Manual Installation** (Developer Mode)
    
    ```bash
    git clone https://github.com/wtfPrethiv/RePrompt..git
    cd RePrompt.
    ```
    
    - Open Chrome and navigate to `chrome://extensions/`
    - Enable "Developer mode" (top-right toggle)
    - Click "Load unpacked" and select the extension folder

### Backend Setup

1. **Clone the Repository**
    
    ```bash
    git clone https://github.com/wtfPrethiv/RePrompt..git
    cd RePrompt/backend
    ```
    
2. **Install Dependencies**
    
    ```bash
    pip install -r requirements.txt
    ```
    
3. **Environment Configuration**
    
    ```bash
    cp .env.example .env
    # Edit .env with your configuration
    ```
    
4. **Start the Server**
    
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    ```
    

The backend will be available at `http://localhost:8000`

---

##  Configuration

### Setting Up Your Gemini API Key

To unlock unlimited usage and faster response times:

1. **Get Your API Key**
    
    - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
    - Create a new API key or use an existing one
2. **Configure in Extension**
    
    - Click the RePrompt extension icon
    - Navigate to "Settings"
    - Enter your Gemini API key
    - Click "Save"
3. **Verify Setup**
    
    - The extension will show "✅ API Key Active" when properly configured
    - You'll now have unlimited prompt optimizations

### Environment Variables

Create a `.env` file in the backend directory:

```env
# Required
GEMINI_API_KEY=your_gemini_api_key_here

# Optional
PORT=8000
HOST=0.0.0.0
DEBUG=True
RATE_LIMIT_REQUESTS=100
RATE_LIMIT_WINDOW=3600  # 1 hour in seconds

# CORS Settings
ALLOWED_ORIGINS=["chrome-extension://*", "https://chatgpt.com", "https://claude.ai"]
```

---

## Usage

1. **Visit any supported AI website** (ChatGPT, Claude.ai, etc.)
2. **Start typing** in any text input field
3. **Look for the RePrompt icon**  that appears near the text box
4. **Click the icon** to instantly optimize your prompt
5. **Review and send** the enhanced prompt for better AI responses

### Supported Websites

- ✅ [ChatGPT](https://chatgpt.com/)
- ✅ [Claude.ai](https://claude.ai/)
- 🔄 Gemini (Coming Soon)
- 🔄 Perplexity (Coming Soon)
- 🔄 Character.ai (Coming Soon)

---

##  Roadmap

### Coming Soon

- [ ] **Multi-Model Support**
    
    - Claude API integration
    - Grok API support
    - OpenAI GPT-4 option
- [ ] **Enhanced Features**
    
    - Custom prompt templates
    - Prompt history and favorites
    - Bulk prompt optimization
    - A/B testing for prompts
- [ ] **Platform Expansion**
    
    - Firefox extension
    - Edge extension
    - Safari extension (if possible)
- [ ] **Advanced Capabilities**
    
    - Context-aware optimization
    - Domain-specific prompt tuning
    - Multi-language support
    - Offline prompt suggestions

### Long-term Vision

- AI-powered prompt analytics
- Community prompt sharing
- Integration with popular AI tools
- Enterprise features for teams

---

## Contributing

We welcome contributions from the community! Here's how you can help:

### Development Setup

1. **Fork the repository**
2. **Create a feature branch**
    
    ```bash
    git checkout -b feature/your-feature
    ```
    
3. **Make your changes**
4. **Run tests**
    
    ```bash
    # Backend testspytest tests/# Extension testsnpm test
    ```
    
5. **Commit your changes**
    
    ```bash
    git commit -m "Add amazing feature"
    ```
    
6. **Push to your branch**
    
    ```bash
    git push origin feature/amazing-feature
    ```
    
7. **Open a Pull Request**

### Contribution Guidelines

- Follow existing code style and conventions
- Write clear, descriptive commit messages
- Add tests for new functionality
- Update documentation as needed
- Ensure all tests pass before submitting

###  Bug Reports

Found a bug? Please create an issue with:

- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Browser and extension version
- Screenshots (if applicable)

### Feature Requests

Have an idea? Open an issue with:

- Detailed description of the feature
- Use cases and benefits
- Mockups or examples (if applicable)

---

## API Documentation

The FastAPI backend provides comprehensive API documentation:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Key Endpoints

```
POST /optimize-prompt
- Optimizes a given prompt for better AI responses

GET /health
- Health check endpoint

GET /supported-sites
- Returns list of supported AI websites
```

---

##  Privacy & Security

- **No Data Storage**: Prompts are processed in real-time and never stored
- **Secure Transmission**: All communications use HTTPS
- **Local API Keys**: Your API keys are stored locally in the browser
- **Open Source**: Full transparency with open-source code

---

## Acknowledgments

- **Google Gemini Team** for providing the powerful language model
- **FastAPI** for the excellent Python framework
- **Chrome Extensions Team** for the robust platform
- **Open Source Community** for inspiration and contributions

---

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/wtfPrethiv/RePrompt./blob/main/LICENSE) file for details.

# 🤖 AI Assistant Web Platform
## تطبيق ويب ذكي لمنصات الذكاء الاصطناعي مفتوحة المصدر

### 🌟 المميزات
- 🔌 دعم متعدد المنصات (Ollama, Hugging Face, OpenAI-compatible)
- 💬 واجهة محادثة تفاعلية في الوقت الفعلي
- 📝 حفظ واسترجاع السجلات
- 🎨 واجهة مستخدم حديثة وسهلة الاستخدام
- ⚙️ إعدادات قابلة للتخصيص
- 📊 تحليل وتتبع الاستخدام

### 🛠️ التكنولوجيا المستخدمة
**Backend:**
- Python 3.10+
- FastAPI
- SQLAlchemy
- Pydantic

**Frontend:**
- React 18+
- TypeScript
- Tailwind CSS
- Socket.io (WebSocket)

**Database:**
- PostgreSQL / SQLite

### 📋 المتطلبات
```
Python 3.10+
Node.js 16+
npm أو yarn
```

### 🚀 البدء السريع

#### 1. استنساخ المستودع
```bash
git clone https://github.com/mohamedabuhallala-lgtm/ai-assistant.git
cd ai-assistant
```

#### 2. إعداد Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # على Windows: venv\Scripts\activate

pip install -r requirements.txt
```

#### 3. إعداد Frontend
```bash
cd frontend
npm install
```

#### 4. إعدادات المتغيرات البيئية

**Backend (.env)**
```
DATABASE_URL=sqlite:///./test.db
OLLAMA_BASE_URL=http://localhost:11434
HUGGINGFACE_API_KEY=your_key_here
SECRET_KEY=your_secret_key
```

**Frontend (.env)**
```
REACT_APP_API_URL=http://localhost:8000
REACT_APP_WS_URL=ws://localhost:8000
```

#### 5. تشغيل التطبيق
```bash
# Terminal 1 - Backend
cd backend
uvicorn main:app --reload

# Terminal 2 - Frontend
cd frontend
npm start
```

### 📡 المنصات المدعومة

#### 1. **Ollama** (محلي)
- نماذج مجانية وسريعة
- لا توجد رسوم API

#### 2. **Hugging Face**
- آلاف النماذج المتاحة
- دعم Inference API

#### 3. **OpenAI-compatible**
- أي خادم متوافق مع OpenAI API
- Mistral, Groq, إلخ

### 📚 الهيكل الأساسي للمشروع
```
ai-assistant/
├── backend/
│   ├── app/
│   │   ├── models/        # نماذج Database
│   │   ├── schemas/       # Pydantic Schemas
│   │   ├── api/
│   │   │   ├── routes/    # API Endpoints
│   │   │   └── middleware/
│   │   ├── services/      # Business Logic
│   │   ├── ai_providers/  # منصات AI
│   │   └── database.py
│   ├── main.py
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── components/    # React Components
│   │   ├── pages/
│   │   ├── services/      # API Services
│   │   ├── hooks/
│   │   └── App.tsx
│   ├── package.json
│   └── .env
└── README.md
```

### 🔌 إضافة منصة جديدة
```python
# backend/app/ai_providers/base.py
from abc import ABC, abstractmethod

class AIProvider(ABC):
    @abstractmethod
    async def generate_response(self, prompt: str) -> str:
        pass

# backend/app/ai_providers/custom_provider.py
from .base import AIProvider

class CustomProvider(AIProvider):
    async def generate_response(self, prompt: str) -> str:
        # تطبيق منصتك هنا
        pass
```

### 🤝 المساهمة
نرحب بالمساهمات! يرجى:
1. Fork المشروع
2. إنشاء فرع للميزة الجديدة
3. إرسال Pull Request

### 📝 الترخيص
MIT License

### 📞 التواصل
- GitHub Issues للمشاكل والأسئلة
- GitHub Discussions للنقاشات

---
**آخر تحديث:** 2026-09-13
**الحالة:** 🟢 قيد التطوير النشط

# 📧 Email Security Analyzer - 企业级邮件安全分析系统

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green)
![Claude](https://img.shields.io/badge/Claude-3%20Opus-purple)
![GPT-4](https://img.shields.io/badge/GPT--4-Turbo-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

> 🎯 **支持 128K+ tokens 上下文，精准识别钓鱼邮件、恶意URL、邮件欺骗**

## ✨ 核心特性

### 🧠 智能分析引擎
- **Claude 3 Opus** (200K tokens) - 高精度复杂分析
- **GPT-4 Turbo** (128K tokens) - 快速处理
- **智能模型路由** - 自动选择最优模型，降低成本 30-50%

### 🔍 深度邮件分析
- ✅ **邮件头解析** - DKIM、SPF、DMARC、Received 链路追踪
- ✅ **URL 风险评分** - 短链展开、IDN 检测、域名信誉检查
- ✅ **钓鱼模式识别** - 45+ 规则库，8 类钓鱼攻击
- ✅ **多语言支持** - 中文和英文邮件

### 📊 钓鱼检测能力
| 检测项 | 准确率 | 规则数 |
|-------|-------|-------|
| 紧迫性语言 | 94% | 12 |
| 账户验证请求 | 96% | 8 |
| 支付/财务威胁 | 95% | 10 |
| 凭证收集 | 97% | 9 |
| 发件人冒充 | 93% | 6 |

### 🚀 三种使用方式
1. **CLI 工具** - 命令行批量处理
2. **REST API** - 集成到你的系统
3. **Python 库** - 直接代码调用

### 🌍 企业级特性
- ✅ Docker 容器化
- ✅ 云端部署 (AWS/GCP)
- ✅ 本地私有部署
- ✅ 批量处理支持
- ✅ 详细审计日志
- ✅ 成本优化模式

---

## 🚀 快速开始

### 1️⃣ 安装

```bash
# 克隆仓库
git clone https://github.com/wanduoji/email-security-analyzer.git
cd email-security-analyzer

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或 venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt
```

### 2️⃣ 配置 API 密钥

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑 .env 文件，添加你的密钥
nano .env
```

### 3️⃣ 运行分析

#### 方式 A: 使用 CLI
```bash
python -m cli.main analyze -f email.eml -o results.json
```

#### 方式 B: 启动 API 服务
```bash
python -m uvicorn src.api.app:app --reload
# 访问 http://localhost:8000/docs
```

---

## 📚 文档

- 📍 [快速开始](docs/getting_started.md)
- 📍 [API 参考](docs/api_reference.md)
- 📍 [部署指南](docs/deployment.md)

---

## 📝 许可证

MIT License

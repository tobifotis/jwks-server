# 📌 JWKS Server 
![Python Version](https://img.shields.io/badge/python-3.x-blue) 
![License](https://img.shields.io/github/license/yourusername/jwks-server) 
![Build](https://img.shields.io/github/actions/workflow/status/yourusername/jwks-server/ci.yml?branch=main) 

This is a simple implementation of a **JWKS (JSON Web Key Set) server** that provides public keys for verifying **JWTs (JSON Web Tokens).** 

--- 

## 📖 Table of Contents
- [Requirements](#requirements)
- [Setup](#setup)
- [Endpoints](#endpoints)
- [Example API Response](#example-api-response)
- [License](#license)

---

## 📌 Requirements

Before running the server, make sure you have the following installed:
- ✅ Python 3.x
- ✅ Flask
- ✅ PyJWT
- ✅ Cryptography

You can install the dependencies automatically by following the **Setup** steps below.

--- 

## ⚙️ Setup 
To get started, follow these steps: 

1️⃣ **Clone the repository:** 
```bash
git clone https://github.com/tobifotis/jwks-server.git
```
2️⃣ **Navigate into the project directory:** 
```bash 
cd jwks-server
```
3️⃣ **Install dependencies:** 
```bash 
pip install -r requirements.txt
```
4️⃣ **Run the server:** 
```bash 
python -m jwks_server.main
```

--- 

## 📡 Endpoints 
| **Endpoint** | **Description** | 
|--------------------------------------|-------------------------------------------| 
| `POST /auth` | Generates and returns a JWT | 
| `GET /.well-known/jwks.json` | Returns the JWKS with public keys | 

--- 

## 📌 Example Response ### **Request:** 
To retrieve the JSON Web Key Set (JWKS), run: 
```bash 
curl -X GET http://localhost:5000/.well-known/jwks.json
```

### **Response:** 
```json 
{
  "keys": [
    {
      "kty": "RSA",
      "kid": "1234",
      "use": "sig",
      "n": "base64-encoded-key",
      "e": "AQAB"
    }
  ]
}
```

--- 

## 📝 License 
This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for more details. 

--- 

## ⭐ Contributing 
Contributions are welcome! If you find any issues or improvements, feel free to open an issue or submit a pull request.

# 📌 JWKS Server 
![Python Version](https://img.shields.io/badge/python-blue) 

This is a simple implementation of a **JWKS (JSON Web Key Set) server** that provides public keys for verifying **JWTs (JSON Web Tokens).** 

---

## 📌 Requirements

Before running the server, make sure you have the following installed:
- ✅ Python
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

## 📌 Example Response 
### **Request:** 
To retrieve the JSON Web Key Set (JWKS), run: 
```bash 
curl http://127.0.0.1:8080/.well-known/jwks.json
```

### **Response:** 
```json 
{
  "keys": [
    {
      "alg": "RS256",
      "e": "AQAB",
      "kid": "5fe782e6-e0f7-4e74-8f0b-c0ebc9d51026",
      "kty": "RSA",
      "n": "2FE8sF48p33uPwmsRI57LqWK9LvWVhMb-GXxJvdWBnX0x_9DTba41FwxWrE9aP-SeHpK70svXrmUrIKXAK52Gg75OfAa_Zuso1aRxOICZsS-NUJCJSLLaok0ytqzued-d2mcdYj8ADqsSB4dpwXpdzyLoV5YVeksS8FMaW_lINZM7Z_bJNi7M1EJ_-0oyfa8Y9M5jnBGFdMlSL5HsUelFH49ZkYcNzTfGW7xZnEmGF63vm7RxGWqbz5Joa0BhyxfDeU2Ky71dWNU0tVZ7AdqGBOhmr-NjuTZs_nBRmYLBaIwU1PALruSg1B17pzFTpTpNQZLw7_QDSmIfZhwjoWGaQ",
      "use": "sig"
    }
  ]
}

```

--- 

## ⭐ Contributing 
Contributions are welcome! If you find any issues or improvements, feel free to open an issue or submit a pull request.

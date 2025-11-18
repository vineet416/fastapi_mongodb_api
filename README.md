# FastAPI MongoDB API 🚀

A simple yet powerful REST API built with FastAPI and MongoDB that provides CRUD (Create, Read, Update, Delete) operations for managing user data.

## 🌐 Live Demo

The API is deployed and accessible at: [https://fastapi-mongodb-api-5q42.onrender.com/docs](https://fastapi-mongodb-api-5q42.onrender.com/docs)

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Usage Examples](#usage-examples)
- [Project Structure](#project-structure)
- [Deployment](#deployment)
- [Author](#author)

## ✨ Features

- ✅ Insert new records
- ✅ Full update of existing records (PUT)
- ✅ Partial update of existing records (PATCH)
- ✅ Delete records
- ✅ Retrieve all records
- ✅ Async/Await support for better performance
- ✅ Data validation using Pydantic
- ✅ Interactive API documentation (Swagger UI)
- ✅ MongoDB integration with Motor (async driver)
- ✅ RESTful API design with proper HTTP methods

## 🛠️ Tech Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **MongoDB** - NoSQL database
- **Motor** - Async Python driver for MongoDB
- **Pydantic** - Data validation using Python type annotations
- **Python-dotenv** - Environment variable management
- **Uvicorn** - ASGI server

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- MongoDB Atlas account (or local MongoDB instance)
- pip (Python package manager)
- Git

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/vineet416/fastapi_mongodb_api.git
cd fastapi_mongodb_api
```

### Step 2: Create a Virtual Environment

**On Windows:**
```bash
python -m venv apienv
apienv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv apienv
source apienv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

### Step 1: Create a `.env` File

Create a `.env` file in the root directory of the project:

```bash
echo. > .env
```

### Step 2: Add MongoDB Connection String

Open the `.env` file and add your MongoDB connection string:

```env
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority
```

**To get your MongoDB URI:**

1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Log in or create a free account
3. Create a new cluster (if you don't have one)
4. Click "Connect" → "Connect your application"
5. Copy the connection string and replace `<username>` and `<password>` with your credentials

## ▶️ Running the Application

### Local Development

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at:
- **API Base URL:** http://127.0.0.1:8000
- **Interactive Docs (Swagger UI):** http://127.0.0.1:8000/docs
- **Alternative Docs (ReDoc):** http://127.0.0.1:8000/redoc

## 📡 API Endpoints

| Method | Endpoint | Description | Parameters |
|--------|----------|-------------|------------|
| GET | `/` | Home route - Welcome message | None |
| GET | `/api/getdata` | Retrieve all records | None |
| POST | `/api/insert` | Insert a new record | Request Body: JSON object |
| PUT | `/api/fullupdate` | Full update of a record (all fields required) | Query: `id`, Request Body: JSON object |
| PATCH | `/api/partialupdate` | Partial update of a record (only specified fields) | Query: `id`, Request Body: JSON object |
| DELETE | `/api/delete` | Delete a record | Query: `id` |

### Data Model

```json
{
  "name": "string",
  "phone": 0,
  "city": "string",
  "course": "string"
}
```

## 💡 Usage Examples

### 1. Home Route

**Endpoint:** `GET /`

**Response:**
```json
{
  "message": "Welcome to the FastAPI MongoDB CRUD API. Visit /docs for API documentation."
}
```

### 2. Get All Data

**Endpoint:** `GET /api/getdata`

**Response:**
```json
[
  {
    "id": "507f1f77bcf86cd799439011",
    "name": "John Doe",
    "phone": 1234567890,
    "city": "New York",
    "course": "Computer Science"
  }
]
```

### 3. Insert Data

**Endpoint:** `POST /api/insert`

**Request Body:**
```json
{
  "name": "John Doe",
  "phone": 1234567890,
  "city": "New York",
  "course": "Computer Science"
}
```

**Response:**
```json
{
  "message": "Data inserted successfully",
  "id": "507f1f77bcf86cd799439011"
}
```

### 4. Full Update Data (PUT)

**Endpoint:** `PUT /api/fullupdate?id=507f1f77bcf86cd799439011`

**Description:** Updates all fields of a record. All fields must be provided.

**Request Body:**
```json
{
  "name": "John Doe",
  "phone": 9876543210,
  "city": "Los Angeles",
  "course": "Data Science"
}
```

**Response:**
```json
{
  "message": "Data fully updated successfully"
}
```

### 5. Partial Update Data (PATCH)

**Endpoint:** `PATCH /api/partialupdate?id=507f1f77bcf86cd799439011`

**Description:** Updates only the specified fields. You can update one or more fields without providing all fields.

**Request Body (update single field):**
```json
{
  "city": "Mumbai"
}
```

**Request Body (update multiple fields):**
```json
{
  "city": "Mumbai",
  "phone": 9876543210
}
```

**Response:**
```json
{
  "message": "Data partially updated successfully"
}
```

### 6. Delete Data

**Endpoint:** `DELETE /api/delete?id=507f1f77bcf86cd799439011`

**Response:**
```json
{
  "message": "Data deleted successfully"
}
```

## 📁 Project Structure

```
fastapi_mongodb_api/
│
├── main.py                 # Main application file with API endpoints
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in repo)
├── README.md              # Project documentation
└── apienv/                # Virtual environment (not in repo)
```

## 🌍 Deployment

This project is deployed on [Render](https://render.com/). To deploy your own instance:

1. Fork this repository
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Set the build and start commands
5. Add environment variables (MONGO_URI)
6. Add environment variables (PORT = 8000)
7. Deploy!

**Build Command:**
```bash
pip install -r requirements.txt
```

**Start Command:**
```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

## 🧪 Testing the API

### Using Swagger UI (Recommended)

1. Navigate to http://127.0.0.1:8000/docs (local) or the deployed URL
2. Click on any endpoint to expand it
3. Click "Try it out"
4. Fill in the required parameters
5. Click "Execute"

### Using cURL

**Get All Data:**
```bash
curl -X GET "http://127.0.0.1:8000/api/getdata"
```

**Insert Data:**
```bash
curl -X POST "http://127.0.0.1:8000/api/insert" -H "Content-Type: application/json" -d "{\"name\":\"Jane Smith\",\"phone\":5551234567,\"city\":\"Chicago\",\"course\":\"AI/ML\"}"
```

**Full Update:**
```bash
curl -X PUT "http://127.0.0.1:8000/api/fullupdate?id=YOUR_ID_HERE" -H "Content-Type: application/json" -d "{\"name\":\"Jane Smith\",\"phone\":9999999999,\"city\":\"Mumbai\",\"course\":\"Data Science\"}"
```

**Partial Update:**
```bash
curl -X PATCH "http://127.0.0.1:8000/api/partialupdate?id=YOUR_ID_HERE" -H "Content-Type: application/json" -d "{\"city\":\"Delhi\"}"
```

**Delete Data:**
```bash
curl -X DELETE "http://127.0.0.1:8000/api/delete?id=YOUR_ID_HERE"
```

### Using Python Requests

```python
import requests

base_url = "http://127.0.0.1:8000"

# Get all data
response = requests.get(f"{base_url}/api/getdata")
print(response.json())

# Insert data
response = requests.post(
    f"{base_url}/api/insert",
    json={
        "name": "Jane Smith",
        "phone": 5551234567,
        "city": "Chicago",
        "course": "AI/ML"
    }
)
print(response.json())
inserted_id = response.json()["id"]

# Full update (all fields required)
response = requests.put(
    f"{base_url}/api/fullupdate",
    params={"id": inserted_id},
    json={
        "name": "Jane Smith",
        "phone": 9999999999,
        "city": "Mumbai",
        "course": "Data Science"
    }
)
print(response.json())

# Partial update (only specified fields)
response = requests.patch(
    f"{base_url}/api/partialupdate",
    params={"id": inserted_id},
    json={
        "city": "Delhi"
    }
)
print(response.json())

# Delete data
response = requests.delete(
    f"{base_url}/api/delete",
    params={"id": inserted_id}
)
print(response.json())
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 👤 Author

**Vineet Patel**
- Email: vineetpatel468@gmail.com
- GitHub: [@vineet416](https://github.com/vineet416)
- LinkedIn: [@vineet416](https://www.linkedin.com/in/vineet416/)

## 📞 Support

If you have any questions or need help, feel free to reach out or open an issue on GitHub.

---

⭐ Star this repository if you find it helpful!
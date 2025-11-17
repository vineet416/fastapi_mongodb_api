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
- ✅ Update existing records
- ✅ Delete records
- ✅ Retrieve all records
- ✅ Async/Await support for better performance
- ✅ Data validation using Pydantic
- ✅ Interactive API documentation (Swagger UI)
- ✅ MongoDB integration with Motor (async driver)

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
| POST | `/api/insert` | Insert a new record | Request Body: JSON object |
| POST | `/api/update` | Update an existing record | Query: `name`, Request Body: JSON object |
| POST | `/api/delete` | Delete a record | Query: `name` |
| GET | `/api/getdata` | Retrieve all records | None |

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

### 1. Insert Data

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

### 2. Update Data

**Endpoint:** `POST /api/update`

**Query Parameter:** `name=John Doe`

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
  "message": "Data updated successfully"
}
```

### 3. Delete Data

**Endpoint:** `POST /api/delete`

**Query Parameter:** `name=John Doe`

**Response:**
```json
{
  "message": "Data deleted successfully"
}
```

### 4. Get All Data

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

**Insert Data:**
```bash
curl -X POST "http://127.0.0.1:8000/api/insert" -H "Content-Type: application/json" -d "{\"name\":\"Jane Smith\",\"phone\":5551234567,\"city\":\"Chicago\",\"course\":\"AI/ML\"}"
```

**Get All Data:**
```bash
curl -X GET "http://127.0.0.1:8000/api/getdata"
```

### Using Python Requests

```python
import requests

# Insert data
response = requests.post(
    "http://127.0.0.1:8000/api/insert",
    json={
        "name": "Jane Smith",
        "phone": 5551234567,
        "city": "Chicago",
        "course": "AI/ML"
    }
)
print(response.json())

# Get all data
response = requests.get("http://127.0.0.1:8000/api/getdata")
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
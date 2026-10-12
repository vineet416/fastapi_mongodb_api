# FastAPI MongoDB CRUD API

A small async REST API that stores and manages person records (name, phone, city, course) in MongoDB.
It uses FastAPI for routing and validation, and Motor as the async MongoDB driver.
Swagger UI is generated automatically at `/docs`.

## Project Files

| File | Description |
|------|-------------|
| [main.py](main.py) | The whole app: Mongo connection, Pydantic model, 6 routes (90 lines) |
| [requirements.txt](requirements.txt) | 5 unpinned dependencies |
| [.gitignore](.gitignore) | Ignores `__pycache__/`, `apienv/` and `.env` |
| `.env` (not in repo) | Must define `MONGO_URI` |

## Data Model

Documents live in database `fastapi`, collection `fastapi_coll` (hard-coded). The repo ships no sample data.

| Field | Type | Notes |
|-------|------|-------|
| `name` | string | Required |
| `phone` | integer | Required; stored as a number |
| `city` | string | Required |
| `course` | string | Required |
| `id` | string | Returned by the API; Mongo `_id` as a string |

## API Endpoints

| Method | Path | Input | Success | Failure |
|--------|------|-------|---------|---------|
| GET | `/` | none | Welcome message | none |
| GET | `/api/getdata` | none | List of all records | none |
| POST | `/api/insert` | JSON body (4 fields) | Message + new `id` | 422, 500 |
| PUT | `/api/fullupdate` | `?id=` + JSON body (4 fields) | Message | 404, 422 |
| PATCH | `/api/partialupdate` | `?id=` + any JSON object | Message | 404 |
| DELETE | `/api/delete` | `?id=` | Message | 404 |

## Approach

1. Load `MONGO_URI` from `.env` and open an async Motor client.
2. Define the `apidata` Pydantic model so bad bodies are rejected with 422.
3. Write one async handler per CRUD operation.
4. Convert `_id` to a string `id`; raise `HTTPException` (404/500) when a write affects no document.

## Verified Behaviour

Checked by running the app with FastAPI's `TestClient` against a stubbed collection (see Data Notes).

| Check | Result |
|-------|--------|
| Registered app routes | 6 (plus `/docs`, `/redoc`, `/openapi.json`) |
| POST with a missing field | 422 |
| POST with `phone` = `"abc"` | 422 |
| PUT on a valid id, values unchanged | 404 |
| DELETE with a malformed id (`"123"`) | 500 |
| PATCH with an unknown field | Passes validation (body is a plain `dict`) |
| `data.dict()` on the model | `PydanticDeprecatedSince20` warning |

## Tech Stack

Python · FastAPI · Uvicorn · Motor / PyMongo (`pymongo[srv]`) · MongoDB (Atlas or local) · Pydantic · python-dotenv

## How to Use

```bash
git clone https://github.com/vineet416/fastapi_mongodb_api.git
cd fastapi_mongodb_api
python -m venv apienv && apienv\Scripts\activate   # macOS/Linux: source apienv/bin/activate
pip install -r requirements.txt
echo MONGO_URI=<your-mongodb-connection-string> > .env
uvicorn main:app --reload   # then open http://127.0.0.1:8000/docs
```

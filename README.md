# Like Button API

This Django REST Framework API provides a "Like" button feature for articles. The API allows anyone to view the number of likes on an article and increment the like count without requiring user authentication.

## Deployed link
```
https://like-button-api.onrender.com
```


## Project Setup

### Requirements
- Django REST Framework

### Installation

1. **Clone the repository:**

    ```
    git clone https://github.com/iConnell/norebase-backend-challenge.git
    cd Like-button
    ```

2. **Create and activate a virtual environment:**

    ```
    python3 -m venv myenv
    source myenv/bin/activate
    ```

    - On Windows:

    ```
    myenv\Scripts\activate
    ```

3. **Install dependencies:**

    ```
    pip install -r requirements.txt
    ```

4. **Run migrations:**

    ```
    python manage.py migrate
    ```

5. **Start the development server:**

    ```
    python manage.py runserver
    ```

### Creating Articles (Sample Data)
For testing purposes, you can create articles via the Django admin panel or Django shell.

1. Open the Django shell:

    ```
    python manage.py shell
    ```

2. Create a sample article:

    ```python
    from likes.models import Article  
    article = Article.objects.create(title="Sample Article", content="This is a sample article.")
    ```

## API Endpoints

### Get Article Details

- **URL**: `/articles/<int:article_id>/`
- **Method**: `GET`
- **Description**: Retrieve details of an article, including the like count.
- **Response**:
  - `200 OK`: Returns article details, including the current like count.
  - `404 Not Found`: Article not found.

**Example Request**:

```
curl -X GET http://127.0.0.1:8000/articles/1/
```
**Example Response**:

```
{
  "id": 1,
  "title": "Sample Article",
  "content": "This is a sample article.",
  "likes": 0
}
```


### Like an Article

- **URL**: `/articles/<int:article_id>/like/
- **Method**: `POST`
- **Description**: Increment the like count for a specific article.
- **Permissions**: No authentication required.
- **Response**:
- `200 OK`: Returns the updated article details with the incremented like count.
- `404 Not Found`: Article not found.

**Example Request**:

```
curl -X POST http://127.0.0.1:8000/articles/1/like/
```
**Example Request**:

```

{
  "id": 1,
  "title": "Sample Article",
  "content": "This is a sample article.",
  "likes": 1
}
```

## Contributing

1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes.
4. Open a pull request to the master branch.

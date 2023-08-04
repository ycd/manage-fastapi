## Example leaderboard project

Example leaderboard project to demonstrate how to get started with templates.

It includes 3 endpoints:

## `/api/v1/user/create`

### Request

```json
HTTP POST /api/v1/user/create

{
  "country": "tr",
  "display_name": "yagu"
}
```

### Response

```json
{
  "error": "",
  "success": true,
  "data": {
    "user_id": "2be26a1d-ee4e-45b1-98fe-f66e3a224c9b"
  }
}
```


## `/api/v1/score/submit`


### Request

```json
HTTP POST /api/v1/user/create

{
  "user_id": "2be26a1d-ee4e-45b1-98fe-f66e3a224c9b",
  "score": 43
}
```

### Response

```json
{
  "error": "",
  "success": true,
  "data": {}
}
```




## `/api/v1/leaderboard`

### Request

```json
HTTP GET /api/v1/leaderboard
```

### Response

```json
{
  "error": "",
  "success": true,
  "data": [
    {
      "user_id": "7cacffca-3cd0-44e0-a7ef-d1675211a4ca",
      "name": "yagu",
      "country": "tr",
      "points": 100,
      "rank": 1
    },
    {
      "user_id": "2be26a1d-ee4e-45b1-98fe-f66e3a224c9b",
      "name": "yagu",
      "country": "tr",
      "points": 43,
      "rank": 2
    }
  ]
}
```


### How to run the project?


1. Create the docker image with `docker build . -t leaderboard` 
1. Run `docker-compose up` which will start the project
1. Check out the api at http://0.0.0.0:8000/docs


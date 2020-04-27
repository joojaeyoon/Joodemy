# API Doc

### 1. Course List

```
GET /api/courses
```

##### Parameters

| Parameter | Types | Description |
| :-------- | :---- | :---------- |
|           |       |             |

##### Response Body

```json
[
  {
    "id": 1,
    "img": "https://cdn.vuetifyjs.com/images/cards/docks.jpg",
    "title": "Complete Python Bootcamp: Go from zero to hero in Python3",
    "description": "Learn Python like a Professional! Start from the basics and go all the way to creating your own applications and games!",
    "instructor": "Joo",
    "price": "29.99$"
  },
  {
    "id": 2,
    "img": "https://cdn.vuetifyjs.com/images/cards/docks.jpg",
    "title": "Spring Boot For Beginners ",
    "description": "Build enterprise applications faster",
    "instructor": "Kim",
    "price": "19.99$"
  }
]
```

### 2. Content List

```
GET /api/contents/<course_id>
```

##### Parameters

| Parameter | Types | Description                 |
| :-------- | :---- | :-------------------------- |
| course_id | int   | (필수) 조회하려는 강의의 id |

##### Response Body

```json
[
  {
    "id": 1,
    "title": "First class",
    "url": "http://techslides.com/demos/sample-videos/small.mp4",
    "time": "03:48"
  },
  {
    "id": 2,
    "title": "Second class",
    "url": "http://techslides.com/demos/sample-videos/small.mp4",
    "time": "05:22"
  },
  {
    "id": 3,
    "title": "Third class",
    "url": "http://techslides.com/demos/sample-videos/small.mp4",
    "time": "04:54"
  }
]
```

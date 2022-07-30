# Python Flask WebDev Blog

## Main Project Components

```mermaid
flowchart TB
    PythonFlaskBlog --> Core & Users & BlogPosts
```

## Project Views

```mermaid
flowchart TB
    Core --> Index & InfoPage
```

```mermaid
flowchart TB
    Users --> Register & Login & Logout & Account & BlogPost
```

```mermaid
flowchart TB
    BlogPosts --> Create & Update & Delete & ViewBlogPost
```

## Models

```mermaid
classDiagram
direction LR
Users<|-- BlogPosts

class Users{
    +INT ID
    +String email
    +String username
    +String password
    +String posts
    +register(email, password)
    +login(email, password)
    +Logout()
    +account()
    +view_owned_post()
}
class BlogPosts{
    +INT ID
    +INT User_ID
    +DATETIME Date
    +String Title
    +String Text
    +create_post()
    +update_post(email, password)
    +delete_post()
    +view_post()
}
```





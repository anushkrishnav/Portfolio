# Design Document

## Background

Overall objective of this project is to implment a minimalistic Blog application where a user can register with the platform and share a post.

### Terminologies used
DAC - Data Access controller
CONT - Controller

### Objects 
#### User
- username
- password

#### Post
- post_id
- created_at
- likes
- post_url

##### ImagePost
- url
- caption
##### Textpost
- body

#### UserPostDetails
- user_id
- post_id


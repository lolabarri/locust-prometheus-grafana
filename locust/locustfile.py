from locust import HttpUser, task, between
import json


class UserBehavior(HttpUser):
    wait_time = between(3, 5)
    host = 'https://jsonplaceholder.typicode.com'

    @task(2)
    def get_posts(self):
        self.client.get('/posts')

    @task(3)
    def get_users(self):
        self.client.get('/users')

    @task(1)
    def post_post(self):
        post = {"title": "Load test", "body": "This is load testing, baby!", "userId": 2}
        post = json.dumps(post)
        headers = {"Content-Type": "application/json"}

        self.client.post("/posts", data=post, headers=headers)
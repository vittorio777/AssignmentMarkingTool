from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2.5)  # 用户在执行任务之间等待1-2.5秒
    host = "https://waynez.online"  # 设置目标主机

    @task(1)
    def visit_homepage(self):
        # 访问主页
        self.client.get("/")

    # @task(2)
    # def visit_random_pages(self):
    #     # 模拟访问一些常见页面
    #     pages = ["/about", "/archives", "/categories"]
    #     for page in pages:
    #         self.client.get(page)

    def on_start(self):
        # 用户开始测试时的行为
        self.client.get("/")
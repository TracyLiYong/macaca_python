import unittest
import time
from macaca import WebDriver

desired_caps = {
    "platformName": "Android",
    "package": "",
    "activity": "",
    "deviceName": ""
}

server_url = {
    "hostname": "127.0.0.1",
    "port": 3456
}


class MacacaTest(unittest.TestCase):

    def setUp(self):
        self.driver = WebDriver(desired_caps, server_url)
        self.driver.init()

    def tearDown(self):
        self.driver.quit()

    def test_macaca(self):
        el = self.driver.element()
        el.click()
        time.sleep(2)


if __name__ == "__main__":
    unittest.main

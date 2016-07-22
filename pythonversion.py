from remote_api import env, cd, run
import private
import unittest

env.host_string = 'ssh.pythonanywhere.com'
env.user = private.user
env.password = private.password

class Test_000_Calculator(unittest.TestCase):

    def test_000_python3(self):
        result = run("python3 --version")
        self.assertTrue("3.4" in result)

if __name__ == "__main__":
    unittest.main()
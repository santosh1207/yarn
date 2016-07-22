from remote_api import env, cd, run
import private
import unittest

env.host_string = 'ssh.pythonanywhere.com'
env.user = private.user
env.password = private.password

class Test_000_Calculator(unittest.TestCase):

    def test_002_directories(self):
        with cd("Yarn"):
            result = run('ls')
            self.assertTrue("yarn" in result.split())
        with cd("Yarn/yarn"):
            result = run('ls')
            self.assertTrue("tests" in result.split())
        with cd("Yarn/yarn/tests"):
            result = run('ls')
            self.assertTrue("test_env.py" in result.split())
            self.assertTrue("yarnfile.py" in result.split())

if __name__ == "__main__":
    unittest.main()
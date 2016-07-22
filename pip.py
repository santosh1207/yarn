from remote_api import env, cd, run
import private
import unittest
  
env.host_string = 'ssh.pythonanywhere.com'
env.user = private.user
env.password = private.password

class Test_000_Calculator(unittest.TestCase):

    def test_001_pip(self):
        result = run("pip --version")
        self.assertTrue("7.1.2" in result)

if __name__ == "__main__":
    unittest.main()
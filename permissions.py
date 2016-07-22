from remote_api import env, cd, run
import private
import unittest
  
env.host_string = 'ssh.pythonanywhere.com'
env.user = private.user
env.password = private.password

class Test_000_Calculator(unittest.TestCase):

    def test_003_directory_pemission(self):
        with cd("software_testing_class"):
            result = run("ls -l")
            results = result.split("\n")
            for result in results:
                if "slides" in result:
                    self.assertTrue("drwxrwxr-x" in result)

if __name__ == "__main__":
    unittest.main()
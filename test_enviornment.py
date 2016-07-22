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

    def test_001_pip(self):
        result = run("pip --version")
        self.assertTrue("7.1.2" in result)

    def test_002_directory(self):
        with cd("~/software_testing_class/lecture_9"):
            result = run("ls")
            self.assertTrue(result.startswith("abcd.py"))

    def test_003_directory(self):
        with cd("~/software_testing_class/lecture_9"):
            result = run("ls -l")
            results = result.split("\n")
            for result in results:
                if "abcd.py" in result:
                    self.assertTrue("-rw-------" in result)


if __name__ == "__main__":
    unittest.main()

from remote_api import env, cd, run
import private
import unittest
  
env.host_string = 'ssh.pythonanywhere.com'
env.user = private.user
env.password = private.password

class Test_000_Calculator(unittest.TestCase):

    def test_004_deletion(self):
        print("we are running test cases which would delete the folder from a particular directory")
        with cd("~"):
            result = run("ls")
            print(result)
            run('rm -rf sample.txt')
            result = run("ls")
            print("------------------------------------------------")
            print("After DELETION results")
            print(result)
            self.assertFalse("sample.txt" in result.split())
            print("we have deleted the sample.txt from the directory")
            print("END OF deleting sample.txt TEST CASE EXECUTION")

if __name__ == "__main__":
    unittest.main()
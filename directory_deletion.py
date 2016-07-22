from remote_api import env, cd, run
import private
import unittest
  
env.host_string = 'ssh.pythonanywhere.com'
env.user = private.user
env.password = private.password

class Test_000_Calculator(unittest.TestCase):

    def test_005_deleting_dir(self):
        with cd("~"):
		print("------------------------------------------------------")
		print("Directory Deletion Test case")
        print("\n")
		result = run('mkdir sbajjuri')
		print("-----------------Directory creation------------------")
		result = run("ls")
		print(result)
		self.assertTrue('sbajjuri' in result.split())
		run('rm -rf sbajjuri')
		print("-------------------------Directory Deletion-------------------------")
		result = run("ls")
		print(result)
		self.assertFalse('sbajjuri' in result.split())
		
if __name__=="__main__":
    unittest.main()
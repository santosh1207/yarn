from remote_api import env, cd, run
import private
import unittest
import os
#import touch

env.host_string = 'ssh.pythonanywhere.com'
env.user = private.user
env.password = private.password

class Test_000_Calculator(unittest.TestCase):

    def test_005_deleting_dir(self):
        with cd("~"):
            print("\n")
            print("--------------------------Directory Creation Test case-------------------------------")
            print("\n")
            result = run("mkdir sbajjuri")
            #print("-----------------Directory creation------------------")
            result = run("ls")
            print(result)
            self.assertTrue('sbajjuri' in result.split())
            #self.assertFalse("drwxrwxr-x" in result)
            with cd("sbajjuri"):
                print("---------------------Sub directory creation test case------------------------------")
                result = run("mkdir sub")
                result = run("ls")
                print(result)
                self.assertTrue('sub' in result.split())
                with cd("sub"):
                    print("-------------------------Text File Creation-----------------------")
                    result = run("touch sbajjuri.txt")
                    with open("sbajjuri.txt","a") as myfile:
                        myfile.write("appenede text I am")
                    #result = run("echo SANTOSH BAJJURI | cat - sbajjuri.txt")
                    result = run("ls -l")
                    print(result)
                    print("\n")
                    print("-------------------------Changing Premissions of the text file-----------------------")
                    #print("\n")
                    result = run("chmod u+x sbajjuri.txt")
                    result = run("ls -l")
                    print(result)
                #if "sub" in result:
                    #self.assertTrue("drwxrwxr-x" in result)
            #run('rm -rf sbajjuri')
            #print("-------------------------Directory Deletion-------------------------")
            #result = run("ls")
            #print(result)
            #self.assertFalse('sbajjuri' in result.split())

    #def test(self):
     #   with cd("sub"):
      #      if os.path.exists('text.txt'):
       #         print 'yes'

if __name__ == "__main__":
    unittest.main()
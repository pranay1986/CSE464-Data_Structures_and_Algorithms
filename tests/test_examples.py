import subprocess, pathlib, unittest, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
class TestExamples(unittest.TestCase):
    def test_all_standalone_examples(self):
        for path in sorted(ROOT.glob('Module_*/*.py')):
            with self.subTest(path=str(path.relative_to(ROOT))):
                result=subprocess.run([sys.executable,str(path)],capture_output=True,text=True,timeout=12)
                self.assertEqual(result.returncode,0,result.stderr)
                self.assertTrue(result.stdout.strip())
if __name__=='__main__':unittest.main()

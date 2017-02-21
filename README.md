1.  Version.
```
PyCharm 2017.1 EAP
Build #PY-171.3224.4, built on February 14, 2017
PyCharm EAP User
Expiration date: March 16, 2017
JRE: 1.8.0_112-release-b702 amd64
JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
Linux 4.8.0-38-generic
```

2. Put breakpoint in tests/test_magic.py on line 5.
3. Open project, right click on tests, select 'Run py.test in tests'
4. Breakpoint is ignored.

Output:

```bash
/home/bernat/.pyenv/versions/magic/bin/python /opt/apps/pycharm/pycharm-171.3224.4/helpers/pydev/pydevd.py --multiproc --qt-support --client 127.0.0.1 --port 39979 --file /opt/apps/pycharm/pycharm-171.3224.4/helpers/pycharm/_jb_pytest_runner.py --path /home/bernat/PycharmProjects/py_tester/tests
Testing started at 12:21 ...
pydev debugger: process 5237 is connecting

Connected to pydev debugger (build 171.3224.4)
 Launching py.test with arguments /home/bernat/PycharmProjects/py_tester/tests
============================= test session starts ==============================
platform linux2 -- Python 2.7.12, pytest-3.0.6, py-1.4.32, pluggy-0.4.0
benchmark: 3.0.0 (defaults: timer=time.time disable_gc=False min_rounds=5 min_time=5.00us max_time=1.00s calibration_precision=10 warmup=False warmup_iterations=100000)
rootdir: /home/bernat/PycharmProjects/py_tester, inifile: setup.cfg
plugins: xdist-1.15.0, verbose-parametrize-1.2.2, profiling-1.2.2, cov-2.4.0
collected 1 items
 
tests/test_magic.py    . Coverage.py warning: Module bre was never imported.
Coverage.py warning: No data was collected.
ERROR: Failed to generate report: No data to report.



============================ pytest-warning summary ============================
WP1 None Module already imported so can not be re-written: xdist
WP1 None Module already imported so can not be re-written: xdist
WP1 None Module already imported so can not be re-written: xdist
WP1 None Module already imported so can not be re-written: pytest_verbose_parametrize
WP1 None Module already imported so can not be re-written: pytest_profiling
WP1 None Module already imported so can not be re-written: pytest_pep257
WP1 None Module already imported so can not be re-written: pytest_flake8
WP1 None Module already imported so can not be re-written: pytest_cov
WP1 None Module already imported so can not be re-written: pytest_benchmark
================= 1 passed, 9 pytest-warnings in 0.02 seconds ==================
  
Process finished with exit code 0
```

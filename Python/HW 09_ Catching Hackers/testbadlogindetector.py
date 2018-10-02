import unittest
from badlogindetector import BadLoginDetector
from logentry import LogEntry

class TestBadLoginDetector(unittest.TestCase):
    def testinit(self):
        BadLoginDetector(3,10)
        BadLoginDetector(30,10000)

    def testprocess_all_success(self):
        log = ['[%d][1.1.1.1][SUCCESS]' % i for i in range(1000)]
        d = BadLoginDetector(3,1000)
        for e in log:
            newentry = LogEntry.fromstring(e)
            self.assertTrue(d.process(newentry))

    def testprocess_somefails(self):
        log = ['[%d][1.1.1.1][SUCCESS]' % i for i in range(1000)]
        log[100] = '[100][2.2.2.2][FAIL]'
        log[200] = '[200][2.2.2.2][FAIL]'
        log[300] = '[300][2.2.2.2][FAIL]'
        d = BadLoginDetector(3,1000)
        for e in log:
            newentry = LogEntry.fromstring(e)
            if newentry.time == 300:
                self.assertFalse(d.process(newentry))
            else:
                self.assertTrue(d.process(newentry))

    def testprocess_fails_far_apart(self):
        log = ['[%d][1.1.1.1][SUCCESS]' % i for i in range(1000)]
        log[100] = '[100][2.2.2.2][FAIL]'
        log[200] = '[200][2.2.2.2][FAIL]'
        log[300] = '[300][2.2.2.2][FAIL]'
        d = BadLoginDetector(3,200)
        for e in log:
            newentry = LogEntry.fromstring(e)
            self.assertTrue(d.process(newentry))

    def testprocess_allfails_far_apart(self):
        log = ['[%d][1.1.1.1][FAIL]' % i for i in range(1000)]
        d = BadLoginDetector(3,2)
        for e in log:
            newentry = LogEntry.fromstring(e)
            self.assertTrue(d.process(newentry))

    def testreport_onefail(self):
        log = ['[%d][1.1.1.1][SUCCESS]' % i for i in range(1000)]
        log[100] = '[100][2.2.2.2][FAIL]'
        log[200] = '[200][2.2.2.2][FAIL]'
        log[300] = '[300][2.2.2.2][FAIL]'
        d = BadLoginDetector(3,201)
        for e in log:
            newentry = LogEntry.fromstring(e)
            d.process(newentry)
        self.assertEqual(d.report(), ['2.2.2.2'])

    def testreport_twofails_same_ip(self):
        log = ['[%d][1.1.1.1][SUCCESS]' % i for i in range(1000)]
        log[100] = '[100][2.2.2.2][FAIL]'
        log[200] = '[200][2.2.2.2][FAIL]'
        log[300] = '[300][2.2.2.2][FAIL]'
        log[400] = '[400][2.2.2.2][FAIL]'
        d = BadLoginDetector(3,1000)
        for e in log:
            newentry = LogEntry.fromstring(e)
            d.process(newentry)
        self.assertEqual(d.report(), ['2.2.2.2'])

    def testreport_lots_of_fails(self):
        log = ['[%d][1.1.1.%d][FAIL]' % (i, i//3) for i in range(900)]
        d = BadLoginDetector(3,3)
        for e in log:
            newentry = LogEntry.fromstring(e)
            d.process(newentry)
        self.assertEqual(len(d.report()), 300)

    def testreport_onefail_too_far_apart(self):
        log = ['[%d][1.1.1.1][SUCCESS]' % i for i in range(1000)]
        log[100] = '[100][2.2.2.2][FAIL]'
        log[200] = '[200][2.2.2.2][FAIL]'
        log[300] = '[300][2.2.2.2][FAIL]'
        d = BadLoginDetector(3,150)
        for e in log:
            newentry = LogEntry.fromstring(e)
            d.process(newentry)
        self.assertEqual(d.report(), [])


if __name__ == '__main__':
    unittest.main()

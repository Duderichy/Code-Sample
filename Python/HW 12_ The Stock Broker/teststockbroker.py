from stockbroker import *
import unittest

class TestBroker(unittest.TestCase):
    
    def testkeyfunction(self):
        broker = Broker([Request(0, 10), Request(0, 20)], [Request(0, 10), Request(0, 20)])

    def testtrade(self):
        bids = [(79.00, 100), (78.50, 100), (80.00, 100)]
        asks = [(99.00, 100), (95.00, 100), (88.00, 100), (89.00, 100), (85.00, 100)]
        broker = Broker([Request(x[0], x[1]) for x in bids], [Request(x[0], x[1]) for x in asks])
        self.assertEqual(broker.trade(), None)
    
    def testtradefixed(self):
        bids = [(90.00, 100), (91.00, 100), (89.00, 100), (78.50, 100), (80.00, 100)]
        asks = [(99.00, 100), (95.00, 100), (88.00, 100), (89.00, 100), (85.00, 100)]
        broker = Broker([Request(x[0], x[1]) for x in bids], [Request(x[0], x[1]) for x in asks])
        self.assertEqual(broker.trade(), (Request(91.0, 100), Request(85.0, 100)))
        self.assertEqual(broker.getprofit(), 600)
        self.assertEqual(broker.trade(), (Request(90.0, 100), Request(88.0, 100)))
        self.assertEqual(broker.getprofit(), 800)
        
    def testtradevariable(self):
        bids = [(82, 100), (85, 30), (90, 10), (89, 40), (84, 20), (91, 5), (80, 50)]
        asks = [(84, 20), (96, 60), (80, 20), (83, 30), (90, 1), (85, 5), (87, 50)]
        broker = Broker([Request(x[0], x[1]) for x in bids], [Request(x[0], x[1]) for x in asks])
        self.assertEqual(broker.trade(), (Request(91, 5), Request(80, 5)))
        self.assertEqual(broker.getprofit(), 55)
        self.assertEqual(broker.trade(), (Request(90, 10), Request(80, 10)))
        self.assertEqual(broker.getprofit(), 155)
        self.assertEqual(broker.trade(), (Request(89, 5), Request(80, 5)))
        self.assertEqual(broker.getprofit(), 200)
        self.assertEqual(broker.trade(), (Request(89, 30), Request(83, 30)))
        self.assertEqual(broker.getprofit(), 380)
    
    def testtradeallfixed(self):
        bids = [(90.00, 100), (91.00, 100), (89.00, 100), (78.50, 100), (80.00, 100)]
        asks = [(99.00, 100), (95.00, 100), (88.00, 100), (89.00, 100), (85.00, 100)]
        broker = Broker([Request(x[0], x[1]) for x in bids], [Request(x[0], x[1]) for x in asks])
        res = [(Request(91.0, 100), Request(85.0, 100)),
               (Request(90.0, 100), Request(88.0, 100)),
               (Request(89.0, 100), Request(89.0, 100))]
        self.assertEqual(broker.tradeall(), res)
        self.assertEqual(broker.getprofit(), 800)
        
    def testtradeallvariable(self):
        bids = [(82, 100), (85, 30), (90, 10), (89, 40), (84, 20), (91, 5), (80, 50)]
        asks = [(84, 20), (96, 60), (80, 20), (83, 30), (90, 1), (85, 5), (87, 50)]
        broker = Broker([Request(x[0], x[1]) for x in bids], [Request(x[0], x[1]) for x in asks])
        res = [(Request(91, 5), Request(80, 5)),
             (Request(90, 10), Request(80, 10)),
             (Request(89, 5), Request(80, 5)),
             (Request(89, 30), Request(83, 30)),
             (Request(89, 5), Request(84, 5)),
             (Request(85, 15), Request(84, 15)),
             (Request(85, 5), Request(85, 5))]
        self.assertEqual(broker.tradeall(), res)
        self.assertEqual(broker.getprofit(), 420)
    

if __name__ == '__main__':
    unittest.main()

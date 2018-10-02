from priorityqueue import *

class Request:
    def __init__(self, price, share):
        self.price = price
        self.share = share
        
    def __eq__(self, other):
        if other == None:
            return False
        return self.price == other.price and self.share == other.share
    
class Broker:
    # implement this method
    def __init__(self, bids, asks):
        if bids == None:
            self.bid = PriorityQueue(key=lambda x: 1 / (x.price + 1))
        else:
            self.bid = PriorityQueue(bids, key=lambda x: 1 / (x.price + 1))
        if asks == None:
            self.ask = PriorityQueue(key=lambda x: x.price)
        else:
            self.ask = PriorityQueue(asks, key=lambda x: x.price)
        self.profits = 0

    # implement this method
    def trade(self):
        # this should execute a trade?
        # careful about that, will change tradeall()
        bid = self.bid.findtop()
        ask = self.ask.findtop()
        # so we shouldn't have to compare to None?
        if bid == None or ask == None:
            return None
        if bid.price >= ask.price:
            if bid.share == ask.share:
                share = ask.share
                self.ask.removetop()
                self.bid.removetop()
            elif bid.share > ask.share:
                share = ask.share
                self.ask.removetop()
                bid.share -= ask.share
            else:
                share = bid.share
                self.bid.removetop()
                ask.share -= bid.share
            self.profits += (bid.price - ask.price) * share
            return (Request(bid.price, share), Request(ask.price, share))
        else:
            return None

    def tradetest(self):
            # this should execute a trade?
            # careful about that, will change tradeall()
            bid = self.bid.findtop()
            ask = self.ask.findtop()
            # so we shouldn't have to compare to None?
            if bid == None or ask == None:
                return None
            if bid.price >= ask.price:
                if bid.share == ask.share:
                    share = ask.share
                elif bid.share > ask.share:
                    share = ask.share
                else:
                    share = bid.share
                return (Request(bid.price, share), Request(ask.price, share))
            else:
                return None

    # implement this method
    def tradeall(self):
        # can have different numbers of shares, need to be able to subtract them off
        trade_list = []
        while 1 == 1:
            trade_result = self.trade()
            if trade_result != None:
                trade_list.append(trade_result)
            else:
                break
        return trade_list


    # implement this method
    def getprofit(self):
        return self.profits

if __name__=="__main__":
    print([Request(91, 5), Request(80,5)] == [Request(91, 5), Request(80,5)])
    bids = [(82, 100), (85, 30), (90, 10), (89, 40), (84, 20), (91, 5), (80, 50)]
    asks = [(84, 20), (96, 60), (80, 20), (83, 30), (90, 1), (85, 5), (87, 50)]
    broker = Broker([Request(x[0], x[1]) for x in bids], [Request(x[0], x[1]) for x in asks])
    result = broker.trade()
    print([(x.price, x.share) for x in result])
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
    print("tradeall test")
    print([((x[0].price, x[0].share), (x[1].price, x[1].share)) for x in broker.tradeall()])
    print([((x[0].price, x[0].share), (x[1].price, x[1].share)) for x in res])
    print(broker.getprofit(), 420)




    
    

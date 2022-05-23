from http import client


try:
    SellSta= client.get_order(symbol=Symb,orderId=SellOrderNum,recvWindow=Delay)
except Exception as e:
    if e.code==-2013:
        print ("Order does not exist.");
    elif e.code==-2014:
        print ("API-key format invalid.");
    #End If
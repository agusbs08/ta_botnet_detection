'''
Created on May 13, 2020

@author: root
'''

class CicLog(object):
    
    def __init__(self, FlowID, SrcIP, SrcPort, DstIP, DstPort, Protocol, Timestamp, FlowDuration, TotFwdPkts, TotBwdPkts, TotLenFwdPkts, TotLenBwdPkts, FwdPktLenMax, FwdPktLenMin, FwdPktLenMean, FwdPktLenStd, BwdPktLenMax, BwdPktLenMin, BwdPktLenMean, BwdPktLenStd, FlowBytspers, FlowPktspers, FlowIATMean, FlowIATStd, FlowIATMax, FlowIATMin, FwdIATTot, FwdIATMean, FwdIATStd, FwdIATMax, FwdIATMin, BwdIATTot, BwdIATMean, BwdIATStd, BwdIATMax, BwdIATMin, FwdPSHFlags, BwdPSHFlags, FwdURGFlags, BwdURGFlags, FwdHeaderLen, BwdHeaderLen, FwdPktspers, BwdPktspers, PktLenMin, PktLenMax, PktLenMean, PktLenStd, PktLenVar, FINFlagCnt, SYNFlagCnt, RSTFlagCnt, PSHFlagCnt, ACKFlagCnt, URGFlagCnt, CWEFlagCount, ECEFlagCnt, DownperUpRatio, PktSizeAvg, FwdSegSizeAvg, BwdSegSizeAvg, FwdBytsperbAvg, FwdPktsperbAvg, FwdBlkRateAvg, BwdBytsperbAvg, BwdPktsperbAvg, BwdBlkRateAvg, SubflowFwdPkts, SubflowFwdByts, SubflowBwdPkts, SubflowBwdByts, InitFwdWinByts, InitBwdWinByts, FwdActDataPkts, FwdSegSizeMin, ActiveMean, ActiveStd, ActiveMax, ActiveMin, IdleMean, IdleStd, IdleMax, IdleMin, Label):
        self.FlowID = FlowID
        self.SrcIP = SrcIP
        self.SrcPort = SrcPort
        self.DstIP = DstIP
        self.DstPort = DstPort
        self.Protocol = Protocol
        self.Timestamp = Timestamp
        self.FlowDuration = FlowDuration
        self.TotFwdPkts = TotFwdPkts
        self.TotBwdPkts = TotBwdPkts
        self.TotLenFwdPkts = TotLenFwdPkts
        self.TotLenBwdPkts = TotLenBwdPkts
        self.FwdPktLenMax = FwdPktLenMax
        self.FwdPktLenMin = FwdPktLenMin
        self.FwdPktLenMean = FwdPktLenMean
        self.FwdPktLenStd = FwdPktLenStd
        self.BwdPktLenMax = BwdPktLenMax
        self.BwdPktLenMin = BwdPktLenMin
        self.BwdPktLenMean = BwdPktLenMean
        self.BwdPktLenStd = BwdPktLenStd
        self.FlowBytspers = FlowBytspers
        self.FlowPktspers = FlowPktspers
        self.FlowIATMean = FlowIATMean
        self.FlowIATStd = FlowIATStd
        self.FlowIATMax = FlowIATMax
        self.FlowIATMin = FlowIATMin
        self.FwdIATTot = FwdIATTot
        self.FwdIATMean = FwdIATMean
        self.FwdIATStd = FwdIATStd
        self.FwdIATMax = FwdIATMax
        self.FwdIATMin = FwdIATMin
        self.BwdIATTot = BwdIATTot
        self.BwdIATMean = BwdIATMean
        self.BwdIATStd = BwdIATStd
        self.BwdIATMax = BwdIATMax
        self.BwdIATMin = BwdIATMin
        self.FwdPSHFlags = FwdPSHFlags
        self.BwdPSHFlags = BwdPSHFlags
        self.FwdURGFlags = FwdURGFlags
        self.BwdURGFlags = BwdURGFlags
        self.FwdHeaderLen = FwdHeaderLen
        self.BwdHeaderLen = BwdHeaderLen
        self.FwdPktspers = FwdPktspers
        self.BwdPktspers = BwdPktspers
        self.PktLenMin = PktLenMin
        self.PktLenMax = PktLenMax
        self.PktLenMean = PktLenMean
        self.PktLenStd = PktLenStd
        self.PktLenVar = PktLenVar
        self.FINFlagCnt = FINFlagCnt
        self.SYNFlagCnt = SYNFlagCnt
        self.RSTFlagCnt = RSTFlagCnt
        self.PSHFlagCnt = PSHFlagCnt
        self.ACKFlagCnt = ACKFlagCnt
        self.URGFlagCnt = URGFlagCnt
        self.CWEFlagCount = CWEFlagCount
        self.ECEFlagCnt = ECEFlagCnt
        self.DownperUpRatio = DownperUpRatio
        self.PktSizeAvg = PktSizeAvg
        self.FwdSegSizeAvg = FwdSegSizeAvg
        self.BwdSegSizeAvg = BwdSegSizeAvg
        self.FwdBytsperbAvg = FwdBytsperbAvg
        self.FwdPktsperbAvg = FwdPktsperbAvg
        self.FwdBlkRateAvg = FwdBlkRateAvg
        self.BwdBytsperbAvg = BwdBytsperbAvg
        self.BwdPktsperbAvg = BwdPktsperbAvg
        self.BwdBlkRateAvg = BwdBlkRateAvg
        self.SubflowFwdPkts = SubflowFwdPkts
        self.SubflowFwdByts = SubflowFwdByts
        self.SubflowBwdPkts = SubflowBwdPkts
        self.SubflowBwdByts = SubflowBwdByts
        self.InitFwdWinByts = InitFwdWinByts
        self.InitBwdWinByts = InitBwdWinByts
        self.FwdActDataPkts = FwdActDataPkts
        self.FwdSegSizeMin = FwdSegSizeMin
        self.ActiveMean = ActiveMean
        self.ActiveStd = ActiveStd
        self.ActiveMax = ActiveMax
        self.ActiveMin = ActiveMin
        self.IdleMean = IdleMean
        self.IdleStd = IdleStd
        self.IdleMax = IdleMax
        self.IdleMin = IdleMin
        self.Label = Label
        
    def setLabel(self, Label):
        self.Label = Label

class SnortLog(object):
    
    def __init__(self, timestamp, label, portSource, 
                 ipDestination, portDestination, ipSource):
        self.timestamp = timestamp
        self.label = label
        self.portSource = portSource
        self.ipDestination = ipDestination
        self.portDestination = portDestination
        self.ipSource = ipSource

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
from collections import OrderedDict
from pymongo import MongoClient
from sklearn.externals import joblib
import numpy as np

class Singleton:

    def __init__(self, cls):
        self._cls = cls

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)
    
@Singleton
class DBConnection(object):
    __instance = None
    def __init__(self):
        """Initialize your database connection here."""
        self.myclient = MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["botnetlog"]
        pass
 
    def __str__(self):
        return 'Database connection object'
     
    def getDB(self):
        return self.mydb

model_url = "/home/agus/ta/iscx_data/New_SVM_Botnet_Model_Detection.pkl"

model = joblib.load(model_url)
list_mean = [23.65849737914968,
 28.704031936567212,
 63.37909726266744,
 128.2894800243995,
 84.55889110044123,
 1051094.1243234547,
 2422302.8876295863,
 76.0404720371156,
 0.41289458357600467,
 0.38062317996505535,
 0.07716948165404776,
 0.7005591147350029,
 91.00627134537031,
 38.74423687281205,
 128.2894800243995,
 61.18669190448457,
 4836.225492137449,
 1993.1230751310425,
 15.58669772859639]

list_std = [23.842922457100688,
 74.69036114931471,
 72.22987314034394,
 182.56068081957284,
 223.14036950053261,
 4678872.910766755,
 9488955.365773845,
 91.58887201858201,
 0.5144307518344211,
 0.8278102226027391,
 0.38916346087404663,
 0.4830907800973356,
 97.40176195575397,
 37.03719240355085,
 182.56068081957284,
 87.24835767231909,
 12114.846971226856,
 8989.310016391279,
 9.207139107014305]

# list_median = [2.0, 39.0, 29.0, 37.0, 0.0, 86.0, 48.0, 40.0, 34.712278729999994, 29.0, 54.8, 0.0, 0.0, 0.0, 1.0, 71.0, 37.0, 71.0, 2.0, 20.0]

sc = SparkContext(appName="SparkTAPySpark")
ssc = StreamingContext(sc, 30)
topic = ["ciclog", "snortlog"]
brokers = "localhost:9092"
kafkaParams = dict({"metadata.broker.list":brokers})
kafkaStream = KafkaUtils.createDirectStream(ssc, topic, kafkaParams, messageHandler=(lambda msg : (msg.topic, msg.message)))

list_fs = ['Fwd Packet Length Min', 'Fwd Packet Length Std',
       'Bwd Packet Length Min', 'Bwd Packet Length Mean',
       'Bwd Packet Length Std', 'Flow IAT Std', 'Flow IAT Max',
       'Packet Length Mean', 'FIN Flag Count', 'SYN Flag Count',
       'RST Flag Count', 'Down/Up Ratio', 'Average Packet Size',
       'Fwd Segment Size Avg', 'Bwd Segment Size Avg', 'Subflow Bwd Bytes',
       'FWD Init Win Bytes', 'Bwd Init Win Bytes', 'Fwd Seg Size Min']

def preprocessing(ciclog):
    global list_mean, list_std, list_median
    
    for i in range(len(ciclog)):
#         if ciclog[i] == np.inf:
#             ciclog[i] = np.nan
            
#         handling missing value
#         if ciclog[i] == np.nan:
#             ciclog[i] = list_median[i]
        
#         normalization
        ciclog[i] = (ciclog[i] - list_mean[i]) / list_std[i]
    
    return ciclog
    

def insertCicLogToMongoDb(resultDict, cicDocs) :
#     cicLogObj = CicLog(**resultDict)
    global model, list_fs
#     data = np.array([cicLogObj.TotBwdPkts, cicLogObj.FwdPktLenMax, cicLogObj.FwdPktLenMin,
#                      cicLogObj.FwdPktLenMean, cicLogObj.FwdPktLenStd, cicLogObj.BwdPktLenMax,
#                      cicLogObj.BwdPktLenMin, cicLogObj.BwdHeaderLen, cicLogObj.BwdPktspers,
#                      cicLogObj.PktLenMin, cicLogObj.PktLenMean, cicLogObj.PSHFlagCnt, 
#                      cicLogObj.ACKFlagCnt, cicLogObj.URGFlagCnt, cicLogObj.DownperUpRatio, 
#                      cicLogObj.PktSizeAvg, cicLogObj.FwdSegSizeAvg, cicLogObj.BwdSegSizeAvg, 
#                      cicLogObj.SubflowFwdPkts, cicLogObj.FwdSegSizeMin])
    data = np.array([resultDict[list_fs[0]], resultDict[list_fs[1]], resultDict[list_fs[2]],
                     resultDict[list_fs[3]], resultDict[list_fs[4]], resultDict[list_fs[5]],
                     resultDict[list_fs[6]], resultDict[list_fs[7]], resultDict[list_fs[8]],
                     resultDict[list_fs[9]], resultDict[list_fs[10]], resultDict[list_fs[11]],
                     resultDict[list_fs[12]],resultDict[list_fs[13]], resultDict[list_fs[14]],
                     resultDict[list_fs[15]], resultDict[list_fs[16]], resultDict[list_fs[17]],
                     resultDict[list_fs[18]], resultDict[list_fs[19]]
                     ])
    
    data = preprocessing(data)
    
    label = ""
    pred = model.predict(data.reshape(1, -1))
    if pred[0] == 0:
        label = "Benign"
    else:
        label = "Bot"
    
    resultDict.update({'Label': label})
#     cicLogObj.setLabel(label)
    print(resultDict["Label"])
    cicDocs.insert_one(resultDict)

def insertSnortLogToMongoDb(resultDict, snortDocs) :
    snortLog = SnortLog(**resultDict)
    print(snortLog.label)
    snortDocs.insert_one(resultDict)

def getAction(d):
#     myclient = MongoClient("mongodb://localhost:27017/")
#     mydb = myclient['botnetlog']
    mydb = DBConnection.Instance().getDB()
    cicDocs = mydb["ciclog"]
    snortDocs = mydb["snortlog"]
    
    topic = str(d[0])
    value = str(d[1])
    resultDict = json.loads(value, object_pairs_hook=OrderedDict)
    if topic == "ciclog":
        insertCicLogToMongoDb(resultDict, cicDocs)
    elif topic == "snortlog":
        insertSnortLogToMongoDb(resultDict, snortDocs)

kafkaStream.foreachRDD(lambda rdd : rdd.foreach(lambda d : getAction(d)))

ssc.start()
ssc.awaitTermination()
    



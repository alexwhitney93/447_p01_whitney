#!/usr/bin/python

from scipy import spatial
import struct
import sys

def knn(pts, queries, k):
    tree = spatial.KDTree(pts)
    knns = []
    for query in queries:
        res = tree.query([query],k)
        indices = res[1][0]
        knn = []
        for i in indices:
            knn.append(pts[i])
        knns.append(knn)
    return knns

def readFile(filename):
    f = open(filename,"rb")
    name = f.read(8).decode("utf-8").rstrip('\0')
    if name == 'TRAINING':
        fileid = struct.unpack('Q',f.read(8))[0]
        numpts = struct.unpack('Q',f.read(8))[0]
        numdim = struct.unpack('Q',f.read(8))[0]
        pts = []
        for i in range(numpts):
            pt = []
            for j in range(numdim):
                val = struct.unpack('f',f.read(4))[0]
                pt.append(val)
            pts.append(tuple(pt))
        ret = {'fileid': fileid,
               'numpts': numpts,
               'numdim': numdim,
               'pts': pts}
    elif name == 'QUERY':
        fileid = struct.unpack('Q',f.read(8))[0]
        numqueries = struct.unpack('Q',f.read(8))[0]
        numdim = struct.unpack('Q',f.read(8))[0]
        k = struct.unpack('Q',f.read(8))[0]
        queries = []
        for i in range(numqueries):
            query = []
            for j in range(numdim):
                val = struct.unpack('f',f.read(4))[0]
                query.append(val)
            queries.append(tuple(query))
        ret = {'fileid': fileid,
               'numqueries': numqueries,
               'numdim': numdim,
               'k': k,
               'queries': queries}
    elif name == 'RESULT':
        trainingfileid =	struct.unpack("Q",f.read(8))[0]
        queryfileid =		struct.unpack("Q",f.read(8))[0]
        fileid =			struct.unpack("Q",f.read(8))[0]
        numqueries =		struct.unpack("Q",f.read(8))[0]
        numdim =			struct.unpack("Q",f.read(8))[0]
        k =					struct.unpack("Q",f.read(8))[0]
        knns = []
        for i in range(numqueries):
            knn = []
            for j in range(k):
                n = []
                for l in range(numdim):
                    val = struct.unpack('f',f.read(4))[0]
                    n.append(val)
                knn.append(tuple(n))
            knns.append(knn)
        ret = {'trainingfileid': trainingfileid,
               'queryfileid': queryfileid,
               'fileid': fileid,
               'numqueries': numqueries,
               'numdim': numdim,
               'k': k,
               'knns': knns}
    else:
        sys.exit(-1)
    f.close()
    return ret

# read the 3 files
trainingInfo = readFile(sys.argv[1])
queryInfo = readFile(sys.argv[2])
resultInfo = readFile(sys.argv[3])

# check that ids match
if resultInfo['trainingfileid'] != trainingInfo['fileid']:
    sys.exit(-1)
if resultInfo['queryfileid'] != queryInfo['fileid']:
    sys.exit(-1)

# check that number of dimensions match
if trainingInfo['numdim'] != queryInfo['numdim']:
    sys.exit(-1)
if queryInfo['numdim'] != resultInfo['numdim']:
    sys.exit(-1)

# check that numqueries and k match
if queryInfo['numqueries'] != resultInfo['numqueries']:
    sys.exit(-1)
if queryInfo['k'] != resultInfo['k']:
    sys.exit(-1)

# compute correct knns
knns = knn(trainingInfo['pts'], queryInfo['queries'], queryInfo['k'])

# compare correct knns with resultfile knns
for i in range(resultInfo['numqueries']):
    correct = sorted(knns[i])
    result = sorted(resultInfo['knns'][i])
    if correct != result:
        sys.exit(-1)

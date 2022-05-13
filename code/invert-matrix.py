# invert a 3*3 matrix
# 11/02/2022

m = [1, 0, 0,
     0, 1, 0,
     0, 0, 1]


def findDet(m):
    global det
    detA = m[0] * (m[4] * m[8] - m[5] * m[7])
    detB = m[1] * (m[3] * m[8] - m[5] * m[6])
    detC = m[2] * (m[3] * m[7] - m[4] * m[6])
    det = detA - detB + detC


def matrixOfMinors(m):
    global mm
    mm = [(m[4] * m[8] - m[5] * m[7]),
          (m[3] * m[8] - m[5] * m[6]),
          (m[3] * m[7] - m[3] * m[8]),
          (m[1] * m[8] - m[2] * m[7]),
          (m[0] * m[8] - m[2] * m[6]),
          (m[0] * m[7] - m[1] * m[6]),
          (m[1] * m[5] - m[2] * m[4]),
          (m[0] * m[5] - m[2] * m[3]),
          (m[0] * m[4] - m[1] * m[3])]


def matrixOfCofactors(m):
    global mc
    mc = [m[0], m[1] * -1, m[2],
          m[3] * -1, m[4], m[5] * -1,
          m[6], m[7] * -1, m[8]]


def transposeMatrix(m):
    global mt
    mt = [m[0], m[3], m[6],
          m[1], m[4], m[7],
          m[2], m[5], m[8]]


def divideDeterminant(m):
    global mi
    mi = [m[0] / det, m[1] / det, m[2] / det,
          m[3] / det, m[4] / det, m[5] / det,
          m[6] / det, m[7] / det, m[8] / det]


def cleanMatrix(m):
    print(str(mi[0]) + "  " + str(mi[1]) + "  " + str(mi[2]))
    print(str(mi[3]) + "  " + str(mi[4]) + "  " + str(mi[5]))
    print(str(mi[6]) + "  " + str(mi[7]) + "  " + str(mi[8]))
    

def invertMatrix():
    findDet(m)
    matrixOfMinors(m)
    matrixOfCofactors(mm)
    transposeMatrix(mc)
    divideDeterminant(mt)
    cleanMatrix(mi)

invertMatrix()
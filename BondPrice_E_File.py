

def getBondPrice_E(face, couponRate, yc):
    m=len(yc)
    coupon=face*couponRate
    bondPrice=0

    for t in range(1,m+1):
        cf=coupon
        if t==m:
            cf=cf+face
        bondPrice=bondPrice+cf/((1+yc[t-1])**t)
    return(bondPrice)

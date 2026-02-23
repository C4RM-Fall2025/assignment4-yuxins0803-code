

def getBondPrice_Z(face, couponRate, times, yc):
    coupon=face*couponRate
    bondPrice=0
    m=len(times)

    for i,(t,r)in enumerate(zip(times,yc)):
        cf=coupon
        if i==m-1:
            cf=cf+face
        bondPrice=bondPrice+cf/((1+r)**t    
    return(bondPrice)

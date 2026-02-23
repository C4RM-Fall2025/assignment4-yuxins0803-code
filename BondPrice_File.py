def getBondPrice(y, face, couponRate, m, ppy=1):
    y_eff=y/ppy
    c_eff=couponRate/ppy
    m_eff=m*ppy

    coupon=face*c_eff
    bondPrice=0

    for t in range(1,m_eff+1):
        bondPrice=bondPrice+coupon/((1+y_eff)**t)
    bondPrice=bondPrice+face/((1+y_eff)**m_eff)
    return bondPrice

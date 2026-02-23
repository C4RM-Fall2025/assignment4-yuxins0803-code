
def getBondDuration(y, face, couponRate, m, ppy = 1):
    y_eff=y/ppy
    c_eff=couponRate/ppy
    m_eff=m*ppy

    pvcfsum=0
    t_pvcfsum=0

    for t in range(1,m_eff+1):
        cf=face*c_eff
        if t==m_eff:
            cf=cf+face
        pvcf=cf/((1+y_eff)**t)
        pvcfsum=pvcfsum+pvcf
        t_pvcfsum=t_pvcfsum+(t/ppy)*pvcf

    bondDuration=t_pvcfsum/pvcfsum
    return bondDuration

import numpy as np

def getRiskCol(loanStatus, returnCoversionDict= False):
    """
    Returns the three-way risk classfication:
        yes: defaulting
        no: reliable, e.g. current loan, fully paid, issued
        maybe: in grace, late, etc.
      
    (and possibly the conversion dictionary)

    Required:
    ---------
    * loanStatus: string array: status of the borrowers' loans.
    
    Optional:
    ---------
    * returnCoversionDict: bool: True if want the conversion dictionary/
                                 Default: False
                            
    
    """
    great= ["Fully Paid",'Does not meet the credit policy. Status:Fully Paid']

    unsure= ["In Grace Period", 
             "Late (16-30 days)", "Late (31-120 days)",
            "Current",  "Issued"]
    bad= ["Default", "Charged Off", "Does not meet the credit policy. Status:Charged Off", ]

    conversionDict= {}
    
    for status in bad:
        conversionDict[status]= 'Default'
    for status in unsure:
        conversionDict[status]= 'Maybe'
    for status in great:
        conversionDict[status]= 'NotDefault'

    risk= loanStatus.copy()
    for entry in np.unique(loanStatus):
        risk[risk==entry]= conversionDict[entry]
        
    if returnCoversionDict:
        return risk, conversionDict
    else:
        return risk

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
    great= ["Current", "Fully Paid", "Issued", 'Does not meet the credit policy. Status:Fully Paid']

    unsure= ["Charged Off", "Does not meet the credit policy. Status:Charged Off", 
             "In Grace Period", 
             "Late (16-30 days)", "Late (31-120 days)"]
    bad= ["Default"]

    conversionDict= {}
    #for status in great:
    #    conversionDict[status]= 'No'
    for status in bad:
        conversionDict[status]= 'Yes'
    for status in unsure:
        conversionDict[status]= 'Maybe'
    for status in great:
        conversionDict[status]= 'No'

    risk= loanStatus.copy()
    for entry in np.unique(loanStatus):
        risk[risk==entry]= conversionDict[entry]
        
    if returnCoversionDict:
        return risk, conversionDict
    else:
        return risk

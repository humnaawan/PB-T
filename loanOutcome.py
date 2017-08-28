import numpy as np
import matplotlib.pyplot as plt

def loanApprovalStatus(risk_Default, risk_Maybe, risk_NotDefault, int_rate, loanTerm, funded_amount): 
    # assume daily compounding
    # defaulting: rejected.
    # risky & nonrisky: all accepted - high risk with the former.
    tot= len(risk_Default)
    profit= np.zeros(tot)
    
    int_rate= int_rate/100.
    ##
    default= np.where(risk_Default==1)[0]
    profit[default]= np.nan

    # assume monthly compounding
    n= 365.

    # calculate profit
    notdefault= np.where(risk_NotDefault==1)[0]
    nYears= loanTerm[notdefault]/12.
    profit[notdefault]= funded_amount[notdefault]*(1.+((int_rate[notdefault])/n))**(n*nYears)-funded_amount[notdefault]

    risky= np.where(risk_Maybe==1)[0]
    nYears= (loanTerm[risky]+6.)/12.   # assume risky would take 6months extra?
    profit[risky]= funded_amount[risky]*(1+((int_rate[risky])/n))**(n*nYears)-funded_amount[risky]

    ind= range(10)
              
    # profit percent
    profitPercent= profit/funded_amount

    # plot histogram: profit %
    bins= 20
    alpha= 0.5
    fontsize= 14
    histtype= 'bar'
    plt.hist(profitPercent[risky], label= 'maybe', alpha= alpha, bins= bins, histtype=histtype)
    plt.hist(profitPercent[notdefault], label= 'not default', alpha= alpha, bins= bins, histtype=histtype)
    plt.xlabel('profit (% funded)', fontsize= fontsize)
    plt.legend(fontsize= fontsize)
    plt.gcf().set_size_inches(12,6)
    plt.show()

    # loan approval? accept everything thats not 100% defaulting.
    loanApproval= np.zeros(tot)+1
    loanApproval[default]= 0.

    # histogram
    #plt.hist(loanApproval)
    #plt.xlabel('loan approval', fontsize= fontsize)
    #plt.show()

    print 'Approval rate (%): ', 100.*(1.-float(len(default))/tot)
    
    return loanApproval

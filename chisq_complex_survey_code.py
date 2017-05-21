
def independance_test_complex_survey(prva,druha,prva_txt,druha_txt):
    col_1=prva_txt
    col_2=druha_txt
    prva_m=prva.unique()
    druha_m=druha.unique()
    y = np.zeros((len(prva.unique()), len(druha.unique())))
    suma_vah=float(data['vahy'].sum())
    for i in range(0,len(prva_m)):
        for j in range(0,len(druha_m)):
            zf=data[(data[col_1]==prva_m[i])&(data[col_2]==druha_m[j])]
            p=float(zf['vahy'].sum())/float(suma_vah) 
            y[int(i)][int(j)]=float(p)
    mf=pd.DataFrame(y)
    #vysledok_testu= stats.chi2_contingency(observed= mf)
    crit = stats.chi2.ppf(q = 0.95, # kriticka hodnota*
                      df = (len(prva.unique())-1)*(len(druha.unique()-1)))
       
    y_suma_stlpcov= y.sum(axis=0)
    y_suma_riadkov= y.sum(axis=1)

    ###X2
    xxx=np.array([])
    for i in range(0,(len(prva_m))):
        for j in range(0,(len(druha_m))):        
            xxx=np.append(xxx,((y[i][j]- (y_suma_stlpcov[j]*y_suma_riadkov[i]))*(y[i][j]- (y_suma_stlpcov[j]*y_suma_riadkov[i])))/(y_suma_stlpcov[j]*y_suma_riadkov[i]))

    ##zosumovanie   
    
    n=len(prva)
    X_2=n*xxx.sum()
    
    print 'suma', xxx.sum()
    print 'kriticka hodnota' , crit
    print 'testovacia hodnota', X_2

    return X_2,crit
    
def independance_test(prva,druha):
    #nahadzanie dat do kontingencnej tabulky
    kontingencna = pd.crosstab(prva, druha, margins = True)
    ######
    #pomenovanie columns
    col=prva.unique()
    riadok=druha.unique()
    col=len(col)
    riadok=len(riadok)
    col=np.arange(col)
    riadok=np.arange(riadok)
    alist=[]
    blist=[]
    for item in col:
        x=str(item)
        alist.append(x)
    alist.append("All")
    for item in riadok:
        b=str(item)
        blist.append(b)
    blist.append("All")  
    kontingencna.columns = [blist]
    kontingencna.index = [alist]
    #dlzky riadkov/stlpcov
    dlzka_row_bez_sum=(len(kontingencna.index)-1)
    dlzka_col_bez_sum=(len(kontingencna.columns)-1)
    #iba odrezania stlpcovych sum a riadkov 
    observed = kontingencna.ix[0:dlzka_row_bez_sum,0:dlzka_col_bez_sum]   # Get table without totals for later use
    kontingencna
    #expected
    expected =  np.outer(kontingencna["All"][0:dlzka_row_bez_sum],
                         kontingencna.ix["All"][0:dlzka_col_bez_sum]) / float(kontingencna['All']['All'])
    expected=pd.DataFrame(expected)
    expected=expected.astype(float)
    observed=observed.astype(float)
    vysledok_testu= stats.chi2_contingency(observed= observed)    
    crit = stats.chi2.ppf(q = 0.95, # kriticka hodnota*
                      df = (len(alist)-1)*(len(blist)-1)   )
    return vysledok_testu,crit    

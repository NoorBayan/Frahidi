import pandas as pd
import pyarabic.araby as araby
from arroth_template import *
from IPython.display import display, HTML

# المدونة الشعرية العروضية
arud_corpus=pd.read_csv('corpus/poems.csv',sep='\t',encoding='utf-16')
#  الاحرف الابجدية والتشكيلات 
abgd=list('ءٱاإأآبةتثجحخدذرزسشصضطظعغفقكلمنهوؤىيئ')
hrkh=list('ًٌٍَُِّْٰ~')
#  الاحرف الشمسية والقمرية
shmsi=list('ةتثدذرزسشصضطظلن')
kamri=list('ءٱاإأآبجحخعغفقكمهوؤىيئ')
# ترميز معلومات القصيدة للعرض
peoms_info={
"topics":dict(pd.read_csv('corpus/Topics.csv',sep='\t',encoding='utf-16').Topic),
"rhymes":dict(pd.read_csv('corpus/Rhymes.csv',sep='\t',encoding='utf-16').Qafih),
"periods":dict(pd.read_csv('corpus/Periods.csv',sep='\t',encoding='utf-16').Period),
"authers":dict(pd.read_csv('corpus/Authers.csv',sep='\t',encoding='utf-16').Auther),
"sea":dict(pd.read_csv('corpus/Seas.csv',sep='\t',encoding='utf-16').Sname)}

############ أستدعاء قاعدة بيانات صور جميع البحور الشعرية
tafilat=pd.read_csv('corpus/tafilat_patterns.csv',sep='\t',encoding='utf-16')
seas=pd.read_csv('corpus/Seas_info.csv',sep='\t',encoding='utf-16')
sea=list(seas.Snum)

#################
b1= """
<div align="right" style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri","sans-serif";'>
    <table dir="rtl" style="float: right;width: 4.9e+2pt;border-collapse:collapse;border:none;margin-left:6.75pt;margin-right:6.75pt;">
        <tbody>
    """
b2="""
        </tbody>
    </table>
</div>
"""

# ارجاع صور تفعيلات البحر 
def get_Sea_tafilat_info(sid):
    sp=tafilat[tafilat.Sid==sid]
    tafilat_info={
        "ptid":list(sp.Tid),
        "tc1":[str(i) for i in list(sp.tcode)],
        "tt":[str(i) for i in list(sp.type)],
        "ttt":[str(i) for i in list(sp.ttt)],
        "t21":[str(i) for i in list(sp.t21)],
        "t22":[str(i) for i in list(sp.t22)],
        "t23":[str(i) for i in list(sp.t23)],
        "t24":[str(i) for i in list(sp.t24)],
        "t25":[str(i) for i in list(sp.t25)],
        "t26":[str(i) for i in list(sp.t26)],
        "t27":[str(i) for i in list(sp.t27)],
        "t28":[str(i) for i in list(sp.t28)]}
    return tafilat_info

def remove_saids_spaces(text):
    for i in range(10):
        if text[0]  == " " : text=text[1:]
        if text[-1] == " " : text=text[:-1]
    return text

def concatenate_list_into_string(lis_strs):
    result = ""
    for el in lis_strs:
        result += " " + el
    return result

def remove_single_letters(text):
    words = text.split(' ')
    waw = 'و'
    for word in words:
        if len(word.strip()) == 1:
            if word != waw:
                words.remove(word)
    text = concatenate_list_into_string(words)
    return text

def remove_unnecessary_spaces(text):
    return re.sub(' +',' ',text)




# تقطيع الكلمات للاحرف والتشكيلات
def get_klmh_split(vt):
    vtl=[]
    n=[i for i in range(len(vt)) if vt[i] in abgd]
    for i in range(1,len(n)):
        tt=""
        for j in range(n[i-1],n[i]):
            tt=tt+vt[j]
        vtl.append(tt)
    tt=""
    for i in range(n[-1],len(vt)):
        tt=tt+vt[i]
    vtl.append(tt)
    return vtl

def get_length_hrof(hrf):               
    return [len(i) for i in hrf]

def get_init_tafilah(hrf,le):
    tf=[1]
    for i in range(1,len(le)):
        if le[i]==1:
            tf.append(3)
        else:
            if hrf[i][1:].find("ْ")!=-1:
                tf.append(0)
            else:
                tf.append(1)                
    return tf

# تقطيع البيت الى كلمات
def get_vers_split(shatr,t):
    shatr=remove_saids_spaces(remove_single_letters(shatr))
    #shatr=remove_saids_spaces(shatr)
    klimat=[]
    if t==0:
        klimat=shatr.split()
        hrof=[get_klmh_split(i) for i in klimat]
        lng=[get_length_hrof(i) for i in hrof]
        tfilh=[get_init_tafilah(hrof[i],lng[i]) for i in range(len(lng))]
    return klimat,hrof,lng,tfilh


def strip_tashkeel(klimah):
    klimah=[i[0] for i in klimah]
    return klimah

# هل الكلمة تحمل ال التعريف

def get_al_atarif(klimah):
    klimah=strip_tashkeel(klimah)
    if len(klimah)>3 and klimah[0]=="ا" and klimah[1]=="ل":
        index=2
    elif len(klimah)>4 and klimah[0] in ["ف","ب","و","ك"] and klimah[1]=="ا" and klimah[2]=="ل":
        index=3
    elif len(klimah)>5 and klimah[0]+klimah[1] in ["وب","فب"] and klimah[2]=="ا" and klimah[3]=="ل":
        index=4
    else:
        index=-1
    
    return index

def get_shmsi_kamri(hrf):
    #al,index=get_al_atarif(klimah)
    if hrf in shmsi:
        al="shmsi"
    elif hrf in kamri:
        al="kamri"
    return al




def last_letter_check(klimah):
    return klimah [-1][-1][0] in ["ى","ا","ي","و"]


def get_wsl(shatr):
    ind1=[]; ind2=[]
    if len(shatr)>1:
        for i in range(len(shatr)-1):
            if last_letter_check(shatr[i]):
                ind=get_al_atarif(shatr[i+1])
                if ind>1:
                    ind1.append(i)
                    ind2.append(ind)
    return ind1,ind2

def al_shmsi_handling(klimah,i,ial,tfilh):
    klimah[i][ial-1] = klimah[i][ial][0]+"ْ"
    tfilh[i][ial-1] = 0
    klimah[i][ial] = klimah[i][ial][0].replace("ّ","") 
    tfilh[i][ial] = 1
    if i!=0:
        del klimah[i][ial-2]
        del tfilh[i][ial-2]
    return klimah,tfilh


def al_kamri_handling(klimah,i,ial,tfilh):
    del klimah[i][ial-2]
    del tfilh[i][ial-2]
    return klimah,tfilh

def alf_waw_aljmaah_handling(klimah,tfilh):
    if klimah[-1][0] == "ا" and klimah[-2][0] == "و" :
        del klimah[-1]
        del tfilh[-1]
    return klimah,tfilh

# هل الكلمة الاخيرة للشطر مشبعة
# حركة الكلمة الاخيرة للشطر 
def replace_last_harkh(klimah,tfilh):
    ishba=["َ","ِ","ُ"]
    hrkat={
    " َ":"ا",
    "ُ":"و",
    "ِ":"ي"}
    hrkh=klimah[-1][-1][1:]
    if len(hrkh)==1:
        if hrkh in ishba:
            klimah[-1].append(hrkat[hrkh]+"ْ")
            tfilh[-1].append(0)
    return klimah,tfilh

def replace_last_harkh(klimah,tfilh):
    ishba=["َ","ِ","ُ"]
    hrkat={
    " َ":"ا",
    "ُ":"و",
    "ِ":"ي"}
    klm=klimah[-1][-1]
    hrkh=klm[1:]
    if len(hrkh)==1:
        if hrkh in ishba:
            if hrkh=="َ" and klm in ["ا","ء"]:
                klimah[-1].append("اْ")
            elif hrkh=="َ" and klm in ["ى"]:
                klimah[-1].append("ء")
            elif hrkh=="َ":
                klimah[-1].append("اْ")
            else:
                klimah[-1].append(hrkat[hrkh]+"ْ")
            tfilh[-1].append(0)
    return klimah,tfilh

# معالجة المدة
def almddh_handling(klimah,tfilh):
    for j in range(len(klimah)):
        for i in range(len(klimah[j])):
            if klimah[j][i][0] == "آ":
                klimah[j][i]=klimah[j][i].replace("ْ","")
                klimah[j][i]=klimah[j][i].replace("ّ","")
                klimah[j][i]="أ"+klimah[j][i][1:]
                tfilh[j][i] =1
                klimah[j].insert(i+1, "اْ")           
                tfilh[j].insert(i+1,0)           
    return klimah,tfilh

# معالجة التنوين
def tanwin_handling(klimah,i,tfilh):
    tnwin=["ً","ٍ","ٌ"]
    md=["ا","و","ي"]
    htnwin={
    "ً":"َ",
    "ٍ":"ِ",
    "ٌ":"ُ"}
    tn=klimah[i][-1][-1]
    if tn in tnwin:
        if klimah[i][-1][0] in md:
            klimah[i][-2]=klimah[i][-2][0]+htnwin[tn]
            klimah[i][-1]="نْ"
            tfilh[i][-2]=1
            tfilh[i][-1]=0
        elif klimah[i][-1][0] == "ة":
            klimah[i][-1]="ت"+htnwin[tn]
            klimah[i].append("نْ")
            tfilh[i].append(0)
        else:
            klimah[i][-1]=klimah[i][-1][0]+htnwin[tn]
            klimah[i].append("نْ")            
            tfilh[i].append(0)
            
        for j in range(len(tnwin)):
            klimah[i][-2]=klimah[i][-2].replace(tnwin[j],"")
    return klimah,tfilh

#معالجة الشدة
def alshdda_handling(klimah,tfilh):
    for j in range(len(klimah)):
        for i in range(len(klimah[j])):
            if klimah[j][i].find("ّ") !=-1:
                klimah[j][i]=klimah[j][i].replace("ّ","")
                extra=klimah[j][i][1:]
                klimah[j][i]=klimah[j][i][0]+"ْ"
                tfilh[j][i] =0
                klimah[j].insert(i+1,klimah[j][i][0]+extra) 
                tfilh[j].insert(i+1,1)                           
    return klimah,tfilh

def diacritizer(klimah,tfilh,dshtr):
    shtr,dklimah,lng,dtfilh=get_vers_split(dshtr,0)
    if len(klimah)==len(dklimah):
        for i in range(len(klimah)):
            if strip_tashkeel(klimah[i]) == strip_tashkeel(dklimah[i]):
                for j in range(len(tfilh[i])):
                    if tfilh[i][j]==3 and dtfilh[i][j]==0:
                        tfilh[i][j]=0
                        klimah[i][j]=klimah[i][j]+"ْ"
    return klimah,tfilh

def arroth(shaatr,t):
    i=0
    shtr,klimah,lng,tfilh=get_vers_split(shaatr,0)
    #klimah,tfilh=diacritizer(klimah,tfilh,dshaatr)
    klimah,tfilh=almddh_handling(klimah,tfilh)
    ial=get_al_atarif(klimah[i])
    if ial>1:
        if get_shmsi_kamri(klimah[i][ial][i]) == "shmsi":
            klimah,tfilh=al_shmsi_handling(klimah,i,ial,tfilh)
    klimah[i],tfilh[i]=alf_waw_aljmaah_handling(klimah[i],tfilh[i])
    klimah,tfilh=tanwin_handling(klimah,i,tfilh)
    for i in range(1,len(klimah)):
        ial=get_al_atarif(klimah[i])
        if ial>1:
            if get_shmsi_kamri(klimah[i][ial][0]) == "shmsi":
                klimah,tfilh=al_shmsi_handling(klimah,i,ial,tfilh)
            elif get_shmsi_kamri(klimah[i][ial][0]) == "kamri":
                klimah,tfilh=al_kamri_handling(klimah,i,ial,tfilh)
                
            if last_letter_check(klimah[i-1]):
                del klimah[i-1][-1]  
                del tfilh[i-1][-1]
        klimah[i],tfilh[i]=alf_waw_aljmaah_handling(klimah[i],tfilh[i])
        klimah,tfilh=tanwin_handling(klimah,i,tfilh)
    klimah,tfilh=alshdda_handling(klimah,tfilh)
    if t==2:
        klimah,tfilh=replace_last_harkh(klimah,tfilh)       
    return klimah,tfilh

def tafilh_org(shatr):
    shtr=[]
    for i in shatr:
        a=[]
        for j in i:
            for d in j:
                a.append(str(d))
        shtr.append(a)
    return shtr


def shtr_org(shatr):
    shtr=[]
    for i in shatr:
        texts=""
        for j in i:
            text=""
            for d in j:
                text=text+str(d)
            texts=texts+" "+text
        shtr.append(remove_saids_spaces(texts))
    return shtr

def tafilh_matching(sdk,agk,sdt,agt,f):
    h1=[int(i) for i in hs1[f]]
    k1=sdk[:-len(t24[f])]
    t1=sdt[:-len(t24[f])]
    h2=[int(i) for i in hs2[f]]
    k2=agk[:-len(t28[f])]
    t2=agt[:-len(t28[f])]

    for i in range(len(t1)):
        if t1[i]==3 and k1[i] in ["و","ي","ا","ن"] and h1[i]==0:
            t1[i]=0
    for i in range(len(t2)):
        if t2[i]==3 and k2[i] in ["و","ي","ا","ن"] and h2[i]==0:
            t2[i]=0
    tt=len([i for i in t1 if i==3])+len([i for i in t2 if i==3])
    return tt


def arroth_write(shatr):
    shtr=[]; texts=""
    for i in shatr:
        text=""
        for d in i:
            text=text+str(d) 
        shtr.append(text)
        texts=texts+" "+text
    texts=remove_saids_spaces(texts)
    aroth_write=[shtr,texts]
    return aroth_write

def get_verse_arroth_info(sdr,agz,vid):
    sadr=arroth(sdr[vid],1)
    agaz=arroth(agz[vid],2)
    if sadr[-1][-1][-1]==1 and sadr[0][-1][-1][0]==agaz[0][-1][-2][0]:
        replace_last_harkh(sadr[0],sadr[-1])
    sdr_merge = shtr_org(sadr)
    sdr_merge[1]=sdr_merge[1].replace(" ","")
    sdr_split = tafilh_org(sadr)
    agz_merge = shtr_org(agaz)
    agz_merge[1]=agz_merge[1].replace(" ","")
    agz_split = tafilh_org(agaz)
    return sdr_merge, sdr_split, agz_merge, agz_split


############## مكتبة نظام قواعد احكام القافية
# ترتيب عرض حروف القافية
def get_order_qafih_letters(qafih_hrof,loc):
    ql_list=[[''.join(qafih_hrof[i][0:loc[i]]), qafih_hrof[i][loc[i]], ''.join(qafih_hrof[i][loc[i]+1:])]\
               if loc[i] != -1 else -1 for i in range(len(qafih_hrof))]
    return ql_list
# استرجاع احكام القافية
def get_qafih_ahkam(verses,tafilat,pattern_ids):
    #qafih_hrkh=[]; qafih_type=[]; qafih_scope=[]
    rawy_loc=[]; wsl_loc=[]; krg_loc=[]; rdf_loc=[]; tasis_loc=[];  dkil_loc=[]
    qafih_hrof=[(verses[i][-2]+verses[i][-1]) [-(tafilat[tafilat.Tid==pattern_ids[i]].squeeze().to_dict()["qafih"]):]\
                   for i in range(len(pattern_ids))]
    qafih_tfilh=[str(tafilat.qtfilh.iloc[int(i)]) for i in pattern_ids]
    rawy=[tafilat.rawy.iloc[int(i)] for i in pattern_ids]
    qscope=[tafilat.qscope.iloc[int(i)] for i in pattern_ids]
    #rawy_list=[qafih_hrof[i][-(rawy[i]):-(rawy[i]-1)] for i in range(len(qafih_hrof))]


    for i in range(len(qafih_hrof)):
        # ايجاد الرَّوي
        r=len(qafih_hrof[i])-(rawy[i])  # الافتراضي
        if qafih_hrof[i][-(rawy[i]):-(rawy[i]-1)] == "ه" and qafih_tfilh[i][-(rawy[i]+1):-(rawy[i])] == "1":
            r=r-1
        # ايجاد الوصل
        w=r+1 # الافتراضي
        if qafih_tfilh[i][w] != "0":
            for j in range(w+1,len(qafih_tfilh[i])):
                if qafih_tfilh[i][j]=="0":
                    w=j
        # ايجاد الخرج
        if len(qafih_tfilh[i])-1>w:
            if  qafih_hrof[i][w] == "ه" and qafih_tfilh[i][w+1]=="0":
                k=w+1
            else:
                k=-1
        else:
            k=-1

        # ايجاد الردف  
        if qafih_hrof[i][r-1] in ["ا","ى","و","ي"] and qafih_tfilh[i][r-1]=="0":
            rdf=r-1
        else:
            rdf=-1

        # ايجاد التاسيس والدخيل  
        if qafih_hrof[i][r-2] in ["ا","ى"] and qafih_tfilh[i][r-1]=="1":
            t=r-2
            d=r-1
        else:
            t=-1
            d=-1

        rawy_loc.append(r)
        wsl_loc.append(w)
        krg_loc.append(k)
        rdf_loc.append(rdf)
        tasis_loc.append(t)
        dkil_loc.append(d)
    
    qafih_letters ={"rawy_list":get_order_qafih_letters(qafih_hrof,rawy_loc),
                    "wsl_list":get_order_qafih_letters(qafih_hrof,wsl_loc),
                    "krg_list":get_order_qafih_letters(qafih_hrof,krg_loc),
                    "rdf_list":get_order_qafih_letters(qafih_hrof,rdf_loc),
                    "tasis_list":get_order_qafih_letters(qafih_hrof,tasis_loc),
                    "dkil_list":get_order_qafih_letters(qafih_hrof,dkil_loc),
                }
    qafih_hrkat,qafih_type=get_qafih_hrkat(qafih_hrof,qafih_tfilh,rawy_loc,wsl_loc,krg_loc,rdf_loc,tasis_loc,dkil_loc)
    qsn,qst=get_qafih_scope(qafih_hrof,qscope,rawy)
    defect=get_qafih_defects(qafih_hrkat["mgry"])
    return qafih_letters,qafih_hrkat,qafih_type,qsn,qst,defect

# استرجاع حركات القافية
def get_qafih_hrkat(qafih_hrof,qafih_tfilh,rawy_loc,wsl_loc,krg_loc,rdf_loc,tasis_loc,dkil_loc):
    mgry=[]; tojih=[]; nfath=[]; ishba=[]; hdo=[]; ras=[]; qtype=[]
    qt={1:"مطلقة مجردة من الردف والتأسيس موصولة بلين.",
    2:"مطلقة مجردة موصولة بهاء.",
    3:"مطلقة مردوفة موصولة بلين.",
    4:"مطلقة مردوفة موصولة بهاء.",
    5:"مطلقة مؤسسة موصولة بلين.",
    6:"مطلقة مؤسسة موصولة بهاء.",
    7:"مقيدة مجردة من الردف والتأسيس.",
    8:"مقيدة مردوفة.",
    9:"مقيدة مؤسسة.",}
    
    for i in range(len(rawy_loc)):
        # اكتشاف المجري
        if len(qafih_hrof[i][rawy_loc[i]])>1:
            mgry.append("ـ"+qafih_hrof[i][rawy_loc[i]][-1])
        elif qafih_tfilh[i][rawy_loc[i]]=="0":
            mgry.append("لا يوجد")
        else:
            mgry.append("0")

        # اكتشاف التَّوجيه
        if len(qafih_hrof[i][rawy_loc[i]-1])>1 and qafih_tfilh[i][rawy_loc[i]]=="0":
            tojih.append("ـ"+qafih_hrof[i][rawy_loc[i]-1][-1])
        else:
            tojih.append("لا يوجد")

        # اكتشاف النَّفاذ
        if qafih_hrof[i][wsl_loc[i]]=="ه":
            if len(qafih_hrof[i][wsl_loc[i]])>1:
                nfath.append("ـ"+qafih_hrof[i][wsl_loc[i]][-1])
            elif qafih_tfilh[i][rawy_loc[i]]=="0":
                nfath.append("ـ"+"ْ")
            else:
                nfath.append("0")
        else:
            nfath.append("لا يوجد")

        # اكتشاف الإشباع
        if dkil_loc[i]!=-1:
            if len(qafih_hrof[i][dkil_loc[i]])>1:
                ishba.append("ـ"+qafih_hrof[i][dkil_loc[i]][-1])
            else:
                ishba.append("0")
        else:
            ishba.append("لا يوجد")

        # اكتشاف الحَذْو
        if rdf_loc[i]!=-1:
            if len(qafih_hrof[i][rdf_loc[i]-1])>1:
                hdo.append("ـ"+qafih_hrof[i][dkil_loc[i]-1][-1])
            else:
                hdo.append("0")
        else:
            hdo.append("لا يوجد")

        # اكتشاف الرَّسّ
        if tasis_loc[i]!=-1:
            ras.append("ـ"+"َ")
        else:
            ras.append("لا يوجد")
            
    ## التعرف على نوع القافية
        if rdf_loc[i]==-1 and tasis_loc[i]==-1 and qafih_hrof[i][wsl_loc[i]]!="ه" and qafih_tfilh[i][rawy_loc[i]]=="1":
            qtype.append(1)
        elif rdf_loc[i]==-1 and tasis_loc[i]==-1 and qafih_hrof[i][wsl_loc[i]]=="ه" and qafih_tfilh[i][rawy_loc[i]]=="1":
            qtype.append(2)
        elif rdf_loc[i]!=-1 and qafih_hrof[i][wsl_loc[i]]!="ه" and qafih_tfilh[i][rawy_loc[i]]=="1":
            qtype.append(3)
        elif rdf_loc[i]!=-1 and qafih_hrof[i][wsl_loc[i]]=="ه" and qafih_tfilh[i][rawy_loc[i]]=="1":
            qtype.append(4)
        elif tasis_loc[i]!=-1 and qafih_hrof[i][wsl_loc[i]]!="ه" and qafih_tfilh[i][rawy_loc[i]]=="1":
            qtype.append(5)
        elif tasis_loc[i]==-1 and qafih_hrof[i][wsl_loc[i]]=="ه" and qafih_tfilh[i][rawy_loc[i]]=="1":
            qtype.append(6)
        elif rdf_loc[i]==-1 and tasis_loc[i]==-1 and qafih_tfilh[i][rawy_loc[i]]=="0":
            qtype.append(7)
        elif rdf_loc[i]!=-1 and qafih_tfilh[i][rawy_loc[i]]=="0":
            qtype.append(8)
        elif tasis_loc[i]!=-1 and qafih_tfilh[i][rawy_loc[i]]=="0":
            qtype.append(9)
        
    #frequency = dict(collections.Counter(mgry))
    qafih_hrkat ={"mgry":mgry,
                    "tojih":tojih,
                    "nfath":nfath,
                    "ishba":ishba,
                    "hdo":hdo,
                    "ras":ras,}
    qafih_type=[qt[i] for i in qtype]
    return qafih_hrkat,qafih_type

# استرجاع عيوب القافية
def get_qafih_defects(mgry):
    defect=""
    m=[i for i in mgry if i not in ["0","ْ","لا يوجد"]]
    g=set(m)
    if len(g)==1:
        defect="لا يوجد عيب"
    elif len(g)==2:
        # عيوب الإقواء والإصراف
        if "ِ" in g and "ُ" in g:
            defect="يوجد عيب الإقواء في القافية ناتج عن اختلاف حركة الروي في القافية بين الضم والكسر. "
        elif "َ" in g and "ُ" in g:
            defect="يوجد عيب الإصراف في القافية ناتج عن اختلاف حركة الروي في القافية بين الفتح والضم. "
        elif "َ" in g and "ِ" in g:
            defect="يوجد عيب الإصراف في القافية ناتج عن اختلاف حركة الروي في القافية بين الفتح والكسر. "
    elif len(g)>2 and  "ِ" in g and "ُ" in g and "َ" in g: 
            defect="يوجد عيب الإصراف في القافية ناتج عن اختلاف حركة الروي في القافية بين الفتح والكسر والضم. "
    return defect

#حدود القافية
def get_qafih_scope(qafih_hrof,qscope,rawy):
    qs={0:"المترادِف (00)",
        1:"المتواتِر (010)",
        2:"المتدارِك (0110)",
        3:"المتراكِب (01110)",
        4:"المتكاوِس (011110)",
        }
    qsn=[qs[i] for i in qscope]
    qst=[[''.join(qafih_hrof[i][0:2]), ''.join(qafih_hrof[i][2:-(rawy[i]-1)]), ''.join(qafih_hrof[i][-(rawy[i]-1):])]\
          for i in range(len(qafih_hrof))]
    return qsn,qst
####################### بناء فضاء الحلول
def get_verse_matching_info(tafilat_count,ptid,p1,p2,p3,p4,p5,p6,p7,p8,sdr_split, agz_split):
    lp=len(p1)
    if tafilat_count==8:
        lshtr1=[p1[i]+p2[i]+p3[i]+p4[i] for i in range(lp)]
        lshtr2=[p5[i]+p6[i]+p7[i]+p8[i] for i in range(lp)]
        shtr1=[[[j for j in p1[i]], [j for j in p2[i]],[j for j in p3[i]],[j for j in p4[i]]] for i in range(lp)]
        shtr2=[[[j for j in p5[i]], [j for j in p6[i]],[j for j in p7[i]],[j for j in p8[i]]] for i in range(lp)]
    elif tafilat_count==6:
        lshtr1=[p1[i]+p2[i]+p3[i] for i in range(lp)]
        lshtr2=[p4[i]+p5[i]+p6[i] for i in range(lp)]
        shtr1=[[[j for j in p1[i]], [j for j in p2[i]],[j for j in p3[i]]] for i in range(lp)]
        shtr2=[[[j for j in p4[i]], [j for j in p5[i]],[j for j in p6[i]]] for i in range(lp)]        
    if tafilat_count==4:
        lshtr1=[p1[i]+p2[i] for i in range(lp)]
        lshtr2=[p3[i]+p4[i] for i in range(lp)]
        shtr1=[[[j for j in p1[i]], [j for j in p2[i]]] for i in range(lp)]
        shtr2=[[[j for j in p3[i]], [j for j in p4[i]]] for i in range(lp)]
        #######
    vers_matched=[i for i in range(lp) if len(sdr_split[1])==len(lshtr1[i]) and len(agz_split[1])==len(lshtr2[i])]
    sdr_matched=[i for i in range(lp) if len(sdr_split[1])==len(lshtr1[i]) if i not in vers_matched]
    agz_matched=[i for i in range(lp) if len(agz_split[1])==len(lshtr2[i]) if i not in vers_matched]
    #######        
    vers_matched_ids=[ptid[i] for i in range(lp) if len(sdr_split[1])==len(lshtr1[i]) and len(agz_split[1])==len(lshtr2[i])]
    sdr_matched_ids=[ptid[i] for i in range(lp) if len(sdr_split[1])==len(lshtr1[i]) if i not in vers_matched]
    agz_matched_ids=[ptid[i] for i in range(lp) if len(agz_split[1])==len(lshtr2[i]) if i not in vers_matched]
    return shtr1,shtr2,vers_matched,sdr_matched,agz_matched,vers_matched_ids,sdr_matched_ids,agz_matched_ids

def get_mapping_solutions(tafilat_count,solutions_space,length_tafilh):
    match_kilmh=[]; match_hrf=[] #; mapping_solutions={}
    for i in range(len(solutions_space['Ptid'])):
        # مطابقة التفعيلة الواحدة ككل 
        match_kilmh.append([1 if solutions_space['tfilh'][i][j] == solutions_space['patte'][i][j] else 0 for j \
                            in range(tafilat_count)])
        
        # مطابقة اجزاء التفعيلة الواحدة  
        match_hrf.append([[1 if (solutions_space['tfilh'][i][j][n] == solutions_space['patte'][i][j][n]) or\
                           (solutions_space['tfilh'][i][j][n]=="3") else 0 for n\
                             in range(len(solutions_space['tfilh'][i][j]))] for j in range(tafilat_count)])
        
    match_hrf_count  = [[len([n for n in j if n==1]) for j in i] for i in match_hrf]
    all_harf_match   = [sum(i) for i in match_hrf_count]
   
    solutions_space['all_matched'] = all_harf_match
    solutions_space['length']      = [length_tafilh for i in range(len(match_kilmh))]
    solutions_space['dif']      = [length_tafilh-i for i in all_harf_match]
    solutions_space['klmh_matched']= [len([j for j in i if j==1]) for i in match_kilmh]
    solutions_space['hrf_matched'] = match_hrf_count
    solutions_space['klmh']        = match_kilmh
    solutions_space['hrf']         = match_hrf
    return solutions_space

def get_verse_matching(num,sid,sp,tafilat_count,sdr_split, agz_split):
    solutions_space={}
    if tafilat_count==8:
        shtr1,shtr2,vers_matched,sdr_matched,agz_matched,vers_matched_ids,sdr_matched_ids,agz_matched_ids=\
        get_verse_matching_info(tafilat_count,sp["ptid"],sp["t21"],sp["t22"],sp["t23"],sp["t24"],\
                                sp["t25"],sp["t26"],sp["t27"],sp["t28"],sdr_split, agz_split)
        orgnal_byt_tfilh=[[sdr_split[1][:len(shtr1[i][0])],sdr_split[1][len(shtr1[i][0]):len(shtr1[i][0])+len(shtr1[i][1])],\
                           sdr_split[1][len(shtr1[i][0])+len(shtr1[i][1]):len(shtr1[i][0])+len(shtr1[i][1])+len(shtr1[i][2])],\
                           sdr_split[1][len(shtr1[i][0])+len(shtr1[i][1])+len(shtr1[i][2]):],\
                           agz_split[1][:len(shtr2[i][0])],agz_split[1][len(shtr2[i][0]):len(shtr2[i][0])+len(shtr2[i][1])],\
                           agz_split[1][len(shtr2[i][0])+len(shtr2[i][1]):len(shtr2[i][0])+len(shtr2[i][1])+len(shtr2[i][2])],\
                           agz_split[1][len(shtr2[i][0])+len(shtr2[i][1])+len(shtr2[i][2]):]] for i in vers_matched]
        orgnal_byt_kilmh=[[sdr_split[0][:len(shtr1[i][0])],sdr_split[0][len(shtr1[i][0]):len(shtr1[i][0])+len(shtr1[i][1])],\
                           sdr_split[0][len(shtr1[i][0])+len(shtr1[i][1]):len(shtr1[i][0])+len(shtr1[i][1])+len(shtr1[i][2])],\
                           sdr_split[0][len(shtr1[i][0])+len(shtr1[i][1])+len(shtr1[i][2]):],\
                           agz_split[0][:len(shtr2[i][0])],agz_split[0][len(shtr2[i][0]):len(shtr2[i][0])+len(shtr2[i][1])],\
                           agz_split[0][len(shtr2[i][0])+len(shtr2[i][1]):len(shtr2[i][0])+len(shtr2[i][1])+len(shtr2[i][2])],\
                           agz_split[0][len(shtr2[i][0])+len(shtr2[i][1])+len(shtr2[i][2]):]] for i in vers_matched]
        patten_byt_matched=[[shtr1[i][0],shtr1[i][1],shtr1[i][2],shtr1[i][3],shtr2[i][0],shtr2[i][1],shtr2[i][2],shtr2[i][3]]\
                            for i in vers_matched]
    elif tafilat_count==6:
        shtr1,shtr2,vers_matched,sdr_matched,agz_matched,vers_matched_ids,sdr_matched_ids,agz_matched_ids=\
        get_verse_matching_info(tafilat_count,sp["ptid"],sp["t21"],sp["t22"],sp["t23"],sp["t24"],\
                                sp["t25"],sp["t26"],"","",sdr_split, agz_split)
        orgnal_byt_tfilh=[[sdr_split[1][:len(shtr1[i][0])],sdr_split[1][len(shtr1[i][0]):len(shtr1[i][0])+len(shtr1[i][1])],\
                           sdr_split[1][len(shtr1[i][0])+len(shtr1[i][1]):],\
                           agz_split[1][:len(shtr2[i][0])],agz_split[1][len(shtr2[i][0]):len(shtr2[i][0])+len(shtr2[i][1])],\
                           agz_split[1][len(shtr2[i][0])+len(shtr2[i][1]):]] for i in vers_matched]
        orgnal_byt_kilmh=[[sdr_split[0][:len(shtr1[i][0])],sdr_split[0][len(shtr1[i][0]):len(shtr1[i][0])+len(shtr1[i][1])],\
                           sdr_split[0][len(shtr1[i][0])+len(shtr1[i][1]):],\
                           agz_split[0][:len(shtr2[i][0])],agz_split[0][len(shtr2[i][0]):len(shtr2[i][0])+len(shtr2[i][1])],\
                           agz_split[0][len(shtr2[i][0])+len(shtr2[i][1]):]] for i in vers_matched]
        patten_byt_matched=[[shtr1[i][0],shtr1[i][1],shtr1[i][2],shtr2[i][0],shtr2[i][1],shtr2[i][2]] for i in vers_matched]

    elif tafilat_count==4:
        shtr1,shtr2,vers_matched,sdr_matched,agz_matched,vers_matched_ids,sdr_matched_ids,agz_matched_ids=\
        get_verse_matching_info(tafilat_count,sp["ptid"],sp["t21"],sp["t22"],sp["t23"],sp["t24"],\
                                "","","","",sdr_split, agz_split)
        orgnal_byt_tfilh=[[sdr_split[1][:len(shtr1[i][0])],sdr_split[1][len(shtr1[i][0]):],\
                           agz_split[1][:len(shtr2[i][0])],agz_split[1][len(shtr2[i][0]):]] for i in vers_matched]
        orgnal_byt_kilmh=[[sdr_split[0][:len(shtr1[i][0])],sdr_split[0][len(shtr1[i][0]):],\
                           agz_split[0][:len(shtr2[i][0])],agz_split[0][len(shtr2[i][0]):]] for i in vers_matched]
        patten_byt_matched=[[shtr1[i][0],shtr1[i][1],shtr2[i][0],shtr2[i][1]] for i in vers_matched]
    
    solutions_space['num']   = [int(num) for i in vers_matched_ids]
    solutions_space['Ptid']  = vers_matched_ids
    solutions_space['tt']    = [sp["tt"][i] for i in vers_matched]
    solutions_space['ttt']   = [sp["ttt"][i] for i in vers_matched]
    solutions_space['kilmh'] = orgnal_byt_kilmh
    solutions_space['tfilh'] = orgnal_byt_tfilh
    solutions_space['patte'] = patten_byt_matched
    solutions_space['arod']  = [i[int(tafilat_count/2)-1] for i in orgnal_byt_tfilh]
    solutions_space['drb']   = [i[-1] for i in orgnal_byt_tfilh]
    
    solutions_space = get_mapping_solutions(tafilat_count,solutions_space,len(sdr_split[1])+len(agz_split[1]))
    return solutions_space

###############################
def get_poem(poem_id,t,tool):
    if t==1:
        v1=arud_corpus[arud_corpus.pid==poem_id]
    elif t==2:
        v1=arud_corpus[arud_corpus.num.isin(poem_id)]
    num=list(v1.num)
    
    if tool=="F":
        sdr=list(v1.Sdr)
        agz=list(v1.Agz)
    elif tool=="M":
        sdr=list(v1.cv_sdr)
        agz=list(v1.cv_agz)
    elif tool=="W":
        sdr=list(v1.fcv_sdr)
        agz=list(v1.fcv_agz)
    else:
        sdr=list(v1.sdr_fcv)
        agz=list(v1.agz_fcv)
        
    poem_info={"title":sdr[0],"poet":peoms_info["authers"][v1.Aid.iloc[0]],"period":peoms_info["periods"][v1.Fid.iloc[0]],\
               "topic":peoms_info["topics"][v1.Tid.iloc[0]],"Cluster":v1.Cluster.iloc[0]}
    return poem_info,num,sdr,agz

def get_solutions_space(poem_id,tool):
    solutions_space=[];sdr_writing=[];agz_writing=[]
    poem_info,num,sdr,agz=get_poem(poem_id,1,tool)
    for vid in range(len(num)):
        sdr_merge, sdr_split, agz_merge, agz_split = get_verse_arroth_info(sdr,agz,vid)
        sdr_writing.append(araby.strip_tashkeel(sdr_merge[0]))
        agz_writing.append(araby.strip_tashkeel(agz_merge[0]))
        sp=get_Sea_tafilat_info(poem_info["Cluster"])
        tafilat_count=int(seas[seas.Snum==poem_info["Cluster"]].Tc.iloc[0])
        solutions_space.append(get_verse_matching(num[vid],poem_info["Cluster"],sp,tafilat_count,sdr_split, agz_split))
    return solutions_space,num,poem_info,sdr_writing,agz_writing

def get_arroth_optimal_solution(poem_id,tool):
    solutions_space,num,poem_info,sdr_writing,agz_writing=get_solutions_space(poem_id,tool)
    df = pd.DataFrame.from_dict(solutions_space[0])
    for i in range(1,len(solutions_space)):
        df=pd.concat([df,pd.DataFrame.from_dict(solutions_space[i])])
    ad=df.groupby(["tt","ttt"]).size().to_frame('size').reset_index( ).sort_values("size", ascending=[False])
    num1=[];ptid1=[];tfilh1=[];kilmh1=[];patte1=[];brokes=[]
    for i in num:
        for j in range(len(ad)):
            greedy=df[(df.tt==ad.tt.iloc[j]) & (df.ttt==ad.ttt.iloc[j]) & (df.num==i)].\
            sort_values(by=['dif','klmh_matched'], ascending=[True,True])
            if len(greedy)>0:
                num1.append(greedy.num.iloc[0])
                ptid1.append(greedy.Ptid.iloc[0])
                tfilh,broke,kilmh=get_optimal_solution(greedy.tfilh.iloc[0],greedy.patte.iloc[0],greedy.kilmh.iloc[0])
                #kilmh1.append(greedy.kilmh.iloc[0])
                patte1.append(greedy.patte.iloc[0])
                #tfilh2.append(greedy.tfilh.iloc[0])
                kilmh1.append(kilmh)
                tfilh1.append(tfilh)
                brokes.append(broke)
                break
    
    return num1,ptid1,kilmh1,poem_info,sdr_writing,agz_writing,tfilh1,brokes

def get_optimal_solution(tfilh1,patte1,kilmh1):
    broke = [1 for i in range(len(patte1))]
    for i in range(len(patte1)):
        if patte1[i]!=tfilh1[i]:
            n=0
            if tfilh1[i][0]=="0":
                tfilh1[i][0]=patte1[i][0]
                kilmh1[i][0]=kilmh1[i][0][0]
            for j in range(len(patte1[i])):
                if patte1[i][j]!=tfilh1[i][j]:
                    n+=1
                    if tfilh1[i][j] =='3':
                        tfilh1[i][j]=patte1[i][j]
                        kilmh1[i][j]=kilmh1[i][j][0]
                    elif kilmh1[i][j][0] in ["ا","ى","ئ","ن","ي","و",] :
                        tfilh1[i][j]=patte1[i][j]
                        kilmh1[i][j]=kilmh1[i][j][0]+"ْ"
                    else:
                        broke[i]=0
                        
            
            for j in range(len(patte1[i])):                    
                if n<3:
                    broke[i]=1
                    #get_kmaen_
                    if patte1[i][j]!=tfilh1[i][j]:
                        tfilh1[i][j]=patte1[i][j]
                        kilmh1[i][j]=kilmh1[i][j][0]
    return tfilh1,broke,kilmh1

def get_arroth_writing(poem_id,sdr_writing,agz_writing,num):
    nid=list(arud_corpus[arud_corpus.pid==poem_id].num)    
    index=[1 if (nid[i] in num) else 0 for i in range(len(nid))]
    sdr_writing=[sdr_writing[i] for i in range(len(index)) if index[i]==1]
    agz_writing=[agz_writing[i] for i in range(len(index)) if index[i]==1]
    return  sdr_writing,agz_writing

def get_most_frequent_rawy(pattern_ids,agz_writing):
    rawy_list=[agz_writing[i][-(tafilat[tafilat.Tid==pattern_ids[i]].squeeze().to_dict()["rawy"]):]\
               for i in range(len(pattern_ids))]
    counter = 0
    rawi = rawy_list[0]
     
    for i in rawy_list:
        curr_frequency = rawy_list.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            rawi = i
    rawy1=" "+ rawi
    if rawi[-1]=="ي":
        rawy2=" ( "+ rawi[-2] +" المكسورة)"
    elif rawi[-1]=="ا":
        rawy2=" ( "+ rawi[-2] +" المفتوحة)"
    elif rawi[-1]=="و":
        rawy2=" ( "+ rawi[-2] +" المضمومة)"
    else:
        rawy2=" ( "+ rawi[-2] +" )"
    rawy=rawy1+rawy2
 
    return rawy

def arud_representation(peom_id,tool):
    vers_ids,pattern_ids,verses,poem_info,sdr_writing,agz_writing,tfilh,brokes=get_arroth_optimal_solution(peom_id,tool)
    
    if len(vers_ids)!=0:
        poem_info,num,sdr,agz=get_poem(vers_ids,2,tool)
        sdr_writing,agz_writing=get_arroth_writing(peom_id,sdr_writing,agz_writing,num)
        #test
        #sdr_arroth=[arroth_write([strip_tashkeel(j) for j in i[:int(len(i)/2)]]) for i in verses]
        #agz_arroth=[arroth_write([strip_tashkeel(j) for j in i[int(len(i)/2):]]) for i in verses]
        sdr_arroth=[arroth_write([strip_tashkeel(j) for j in i[:int(len(i)/2)]]) for i in verses]
        agz_arroth=[arroth_write([strip_tashkeel(j) for j in i[int(len(i)/2):]]) for i in verses]

        # ترتيب بيانات البيت الشعري الصدر والعجز الكتابة الاملائية والكتابة العروضية
        vers_info  ={"num":num,
                    "sdr_imlaai_writeing":sdr,
                    "agz_imlaai_writeing":agz,
                    "sdr_arroth_writeing":sdr_writing,
                    "agz_arroth_writeing":agz_writing}
        # ترتيب بيانات التقطيع للبيت الشعري
        vers_split=[]
        sdr_split_writeing=[i[0] for i in sdr_arroth]
        agz_split_writeing=[i[0] for i in agz_arroth]
        tafilat_count=int(seas[seas.Snum==poem_info["Cluster"]].Tc.iloc[0])

        for i in range(len(sdr_split_writeing)):
            vers_merge=[]
            vers_merge.extend(sdr_split_writeing[i])
            vers_merge.extend(agz_split_writeing[i])
            vers_split.append(vers_merge)
        
        qafih_letters,qafih_hrkat,qafih_type,qsn,qst,defect=get_qafih_ahkam(verses,tafilat,pattern_ids)
        
    return poem_info,vers_info,vers_split,pattern_ids,tafilat_count,tfilh,brokes,qafih_letters,qafih_hrkat,qafih_type,\
            qsn,qst,defect

################ التمثيل المرئي

def minify_html(html):
    return html.strip().replace('    ', '').replace('\n', '')

def escape_html(text):
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    text = text.replace('"', '&quot;')
    return text

class PoemArrothRenderer(object):
    style = 'arroth'
    def __init__(self, options={}):
        self.font = options.get('font', 'Aldhabi')
        #self.colspan = options.get('colspan', '8')
        

    def render_arroth_tasks(self, render_id,poem_info,vers_info,tafilat,vers_split,pattern_ids,tafilat_count,tfilh,brokes,\
                            qafih_letters,qafih_hrkat,qafih_type,qsn,qst,defect,ptype):
        path="C:\\Users\\wk\\SmartPoet\\Audio\\arud\\"
        if ptype=="G":
            path="C:\\Users\\wk\\SmartPoet\\Audio\\generation\\"
        colspan={4:[12,6,3,2],6:[6,3,1,1],8:[24,12,3,4],}
        poem_heder=POEM_INFO.format(id=render_id, font=self.font,colspan1=colspan[tafilat_count][0],
                                      title  =poem_info["title"],
                                      poet   =poem_info["poet"],
                                      period =poem_info["period"],
                                      topic  =poem_info["topic"],
                                      sea    =peoms_info["sea"][poem_info["Cluster"]],
                                      Rawy   =get_most_frequent_rawy(pattern_ids,vers_info["agz_arroth_writeing"]))        
        verses_table=""
        for i in range(len(vers_info["sdr_imlaai_writeing"])):
            poem_ids=POEM_ID.format(id=render_id, font=self.font, colspan1=colspan[tafilat_count][0], poem_id=i+1)    
            poem_vers=POEM_VERSE.format(id=render_id, font=self.font,colspan2=colspan[tafilat_count][1],
                                          sdr_imlaai_writeing  =vers_info["sdr_imlaai_writeing"][i],
                                          agz_imlaai_writeing  =vers_info["agz_imlaai_writeing"][i],
                                          sdr_arroth_writeing  =vers_info["sdr_arroth_writeing"][i],
                                          agz_arroth_writeing  =vers_info["agz_arroth_writeing"][i],
                                          audio_sdr=path+"sdr\\s"+str(vers_info["num"][i])+".wav",
                                          audio_agz=path+"agz\\a"+str(vers_info["num"][i])+".wav")

            pattern= tafilat[tafilat.Tid==pattern_ids[i]].squeeze().to_dict()
            verse_words_split="";verse_tafilat_split=""
            set_tafilat_code="";set_zhaaf_eilah=""
            tfilh_broke=[]; solve_broke={}
            # تفاصيل تفعيلات البيت
            for j in range(len(vers_split[0])):
                if brokes[i][j] ==1:
                    bcolor="white";fcolor="black"
                    verse_words_split   = verse_words_split+"\n"+\
                                    VERSE_WORDS_SPLIT.format(bcolor=bcolor,fcolor=fcolor,colspan3=colspan[tafilat_count][2],\
                                                                   words_split=vers_split[i][j])
                    verse_tafilat_split = verse_tafilat_split+"\n"+\
                                    VERSE_TAFILAT_SPLIT.format(bcolor=bcolor,fcolor=fcolor,colspan3=colspan[tafilat_count][2],\
                                                                     tafilat_split=pattern["t1"+str(j+1)])
                    set_tafilat_code    = set_tafilat_code+"\n"+\
                                    VERSE_TAFILAT_CODE.format(bcolor=bcolor,fcolor=fcolor,colspan3=colspan[tafilat_count][2],\
                                                                    tafilat_code =str(pattern["t2"+str(j+1)])[::-1])
                    set_zhaaf_eilah     = set_zhaaf_eilah+"\n"+\
                                    VERSE_ZHAAF_EILAH.format(bcolor=bcolor,fcolor=fcolor,colspan3=colspan[tafilat_count][2],\
                                                                   zhaaf_eilah=pattern["t"+str(j+1)])
                else:
                    bcolor="#FAF6F6";fcolor="red"
                    verse_words_split   = verse_words_split+"\n"+\
                                    VERSE_WORDS_SPLIT.format(bcolor=bcolor,fcolor=fcolor,colspan3=colspan[tafilat_count][2],\
                                                                   words_split=vers_split[i][j])
                    verse_tafilat_split = verse_tafilat_split+"\n"+\
                                    VERSE_TAFILAT_SPLIT.format(bcolor=bcolor,fcolor=fcolor,colspan3=colspan[tafilat_count][2],\
                                                                     tafilat_split="مكسورة")
                    set_tafilat_code    = set_tafilat_code+"\n"+\
                                    VERSE_TAFILAT_CODE.format(bcolor=bcolor,fcolor=fcolor,colspan3=colspan[tafilat_count][2],\
                                                                    tafilat_code = [''.join(tfilh[i][j][::-1])][0])
                    set_zhaaf_eilah     = set_zhaaf_eilah+"\n"+\
                                    VERSE_ZHAAF_EILAH.format(bcolor=bcolor,fcolor=fcolor,colspan3=colspan[tafilat_count][2],\
                                                                   zhaaf_eilah="مكسورة")
                    tfilh_broke.append(str(j+1))
                    solve_broke[str(j+1)]= [[''.join(tfilh[i][j][::-1])][0],str(pattern["t2"+str(j+1)])[::-1],\
                                            pattern["t1"+str(j+1)], pattern["t"+str(j+1)]]
                
                   
                
            words_split_body  = WORDS_SPLIT_BODY.format(id=render_id, font=self.font,verse_words_split=verse_words_split)
            tafilat_split_body= TAFILAHT_SPLIT_BODY.format(id=render_id, font=self.font,verse_tafilat_split=verse_tafilat_split)
            tafilat_code_body = TAFILAHT_CODE_BODY.format(id=render_id, font=self.font,set_tafilat_code=set_tafilat_code)
            zhaaf_eilah_body  = ZHAAF_EILAH_BODY.format(id=render_id, font=self.font,set_zhaaf_eilah=set_zhaaf_eilah)
            
            split_table_body =  words_split_body+"\n"+tafilat_split_body+"\n"+tafilat_code_body+"\n"+zhaaf_eilah_body
            if 0 not in brokes[i]:
                verse_brokeing = VERSE_BROKEING.format(colspan1=colspan[tafilat_count][0], tafilat_brokeing="البيت الشعري صحيح ليس فيه اي كسر")
                verse_correct_brokeing = VERSE_CORRECT_BROKEING.format\
                (colspan1=colspan[tafilat_count][0], tafilat_correct_brokeing="لا يوجد كسر في البيت الشعري حتى يتم تصحيحة")
            else:
                text1="البيت الشعري فيه تكسير في "
                if len(tfilh_broke)==1:
                    text2="التفعيلة رقم "
                elif len(tfilh_broke)==2:
                    text2="التفعيلتين "
                elif len(tfilh_broke)>2:
                    text2="التفعيلات "
                txt=""
                for j in tfilh_broke:
                    txt=txt+" يمكن تصحيحة التفعيلة رقم "+str(j) +" بالترميز " + str(solve_broke[j][0])+\
                    " لتصبح كالتالي: "+str(solve_broke[j][1])+\
                    " , "+str(solve_broke[j][2])+" , "+str(solve_broke[j][3]+".  ")
                verse_brokeing = VERSE_BROKEING.format(colspan1=colspan[tafilat_count][0],\
                                                       tafilat_brokeing=text1+text2+['،'.join(tfilh_broke)][0]+". ")
                verse_correct_brokeing = VERSE_CORRECT_BROKEING.format(colspan1=colspan[tafilat_count][0],\
                                                                       tafilat_correct_brokeing=txt)
            verse_Rhyme=VERSE_RHYME.format(colspan1=colspan[tafilat_count][0],\
                                           rhyme=vers_info["agz_arroth_writeing"][i][-pattern["qafih"]:]\
                                        ,loc1=qsn[i]+", ("+qst[i][0],loc2=qst[i][1],loc3=qst[i][2]+")",qafih_type=qafih_type[i])
            
            verse_rhyme_letters=RHYME_LETTERS.format(colspan4=colspan[tafilat_count][3]
                                                     ,rawy   = render_qafih_labels(qafih_letters["rawy_list"][i])
                                                     ,wsl   = render_qafih_labels(qafih_letters["wsl_list"][i])
                                                     ,krg   = render_qafih_labels(qafih_letters["krg_list"][i])
                                                     ,rdf   = render_qafih_labels(qafih_letters["rdf_list"][i])
                                                     ,tasis = render_qafih_labels(qafih_letters["tasis_list"][i])
                                                     ,dkil  = render_qafih_labels(qafih_letters["dkil_list"][i])
                                                     ,mgry = render_qafih_labels1(qafih_hrkat["mgry"][i])
                                                     ,tojih= render_qafih_labels1(qafih_hrkat["tojih"][i])
                                                     ,nfath= render_qafih_labels1(qafih_hrkat["nfath"][i])
                                                     ,ishba= render_qafih_labels1(qafih_hrkat["ishba"][i])
                                                     ,hdo  = render_qafih_labels1(qafih_hrkat["hdo"][i])
                                                     ,ras  = render_qafih_labels1(qafih_hrkat["ras"][i]))
            
            verses_table = verses_table +"\n"+ poem_ids+"\n"+poem_vers+"\n"+split_table_body+"\n"+\
                            verse_brokeing+"\n"+verse_correct_brokeing+"\n"+verse_Rhyme+"\n"+verse_rhyme_letters
                           
        return ARROTH_TABLE.format(id=render_id, font=self.font,colspan1=colspan[tafilat_count][0], poem_heder=poem_heder,\
                                   verses_table=verses_table,defect=defect )

    
def render_qafih_labels(labels):
    if labels==-1:
        return QAFIH_LABELS1.format(loc1="لا ",loc2="يوجد")
    else:
        return QAFIH_LABELS2.format(loc1=labels[0],loc2=labels[1],loc3=labels[2])

def render_qafih_labels1(labels):
    if labels=='لا يوجد':
        return QAFIH_LABELS1.format(loc1="لا ",loc2="يوجد")
    else:
        return QAFIH_LABELS2.format(loc1=labels,loc2=labels,loc3=labels)

def arud_visualization(peom_id,tool,ptype):
    poem_info,vers_info,vers_split,pattern_ids,tafilat_count,tfilh,brokes,qafih_letters,qafih_hrkat,qafih_type,qsn,qst,defect\
    =arud_representation(peom_id,tool)
    html = PoemArrothRenderer()
    htm = html.render_arroth_tasks(peom_id,poem_info,vers_info,tafilat,vers_split,pattern_ids,tafilat_count,tfilh,brokes,\
                                  qafih_letters,qafih_hrkat,qafih_type,qsn,qst,defect,ptype)
    poem=minify_html(htm)
    return poem
#################
def get_test_data(peom_id,tool):
    poem_info,vers_info,vers_split,pattern_ids,tafilat_count,tfilh,brokes,qafih_letters,qafih_hrkat,qafih_type,qsn,qst,defect\
    =arud_representation(peom_id,tool)
    poem=pd.DataFrame({'sdr':vers_info['sdr_imlaai_writeing'],'agz':vers_info['agz_imlaai_writeing'],'brokes':brokes,\
              'sdr_write':vers_info['sdr_arroth_writeing'],'agz_write':vers_info['agz_arroth_writeing'],\
                       'ksr':[len([j for j in i if j==0]) for i in brokes],'tfilh':tfilh,'vers_split':vers_split})
    return poem

def arud_tasks(pid,tool,ptype,task):
    from bs4 import BeautifulSoup
    poem=arud_visualization(pid,tool,ptype)
    soup = BeautifulSoup(poem, 'html.parser')
    soup.find_all('tr', class_="qafih_letters")
    # المهام
    tasks=soup.find_all('tr', class_="tasks")
    #عيوب القافية
    defect=soup.find_all('tr', class_="defect")
    # القصيدة
    title=soup.find_all('tr', class_="title")
    # الشاعر
    poet=soup.find_all('tr', class_="poet")
    # الفترة
    period=soup.find_all('tr', class_="period")
    # الموضوع
    topic=soup.find_all('tr', class_="topic")
    # البحر
    sea=soup.find_all('tr', class_="sea")
    # حرف الروي
    rawy=soup.find_all('tr', class_="rawy")
    # البيت رقم
    poem_id=soup.find_all('tr', class_="poem_id")
    # تشطير البيت
    byt=soup.find_all('tr', class_="byt")
    # الكتابة العروضية
    arroth_writeing=soup.find_all('tr', class_="arroth_writeing")
    # التقطيع
    verse_words_split=soup.find_all('tr', class_="verse_words_split")
    # التفعيلات
    verse_tafilat_split=soup.find_all('tr', class_="verse_tafilat_split")
    # الترميز
    set_tafilat_code=soup.find_all('tr', class_="set_tafilat_code")
    # الزحافات والعلل
    set_zhaaf_eilah=soup.find_all('tr', class_="set_zhaaf_eilah")
    # التفاصيل
    zhaaf_eilah_det=soup.find_all('tr', class_="zhaaf_eilah_det")
    # التكسير
    tafilat_brokeing=soup.find_all('tr', class_="tafilat_brokeing")
    # تصحيح التكسير
    tafilat_correct_brokeing=soup.find_all('tr', class_="tafilat_correct_brokeing")
    # القافية
    rhyme=soup.find_all('tr', class_="rhyme")
    # حدود القافية
    loc=soup.find_all('tr', class_="loc")
    # نوع القافية
    qafih_type=soup.find_all('tr', class_="qafih_type")
    # حروف القافية
    qafih_letters1=soup.find_all('tr', class_="qafih_letters1")
    qafih_letters2=soup.find_all('tr', class_="qafih_letters2")
    # حركات القافية
    qafih_hrkat1=soup.find_all('tr', class_="qafih_hrkat1")
    qafih_hrkat2=soup.find_all('tr', class_="qafih_hrkat2")
    ###########
    b=[]
    b.append(b1)
    b.extend(tasks)
    if task in [1,2,3,4,5,6]:
        b.extend(title)
        b.extend(poet)
    if task in [1]:    
        b.extend(period)
        b.extend(topic)
    if task in [1,2,3,4,5,6]:            
        b.extend(sea)
    if task in [1,6]:                
        b.extend(rawy)
    for i in range(len(byt)):
        #b.append(poem_id[i])
        if task in [2,3,4,5,6]:
            b.append(byt[i])
        if task in [2,3,4,5]:
            b.append(arroth_writeing[i])
        if task in [3,4,5]:
            b.append(verse_words_split[i])
        if task in [4,5]:        
            b.append(verse_tafilat_split[i])
            b.append(set_tafilat_code[i])
            b.append(set_zhaaf_eilah[i])
        if task ==5:        
            b.append(tafilat_brokeing[i])
            b.append(tafilat_correct_brokeing[i])
        if task ==6:        
            b.append(rhyme[i])
            b.append(loc[i])
            b.append(qafih_type[i])
            b.append(qafih_letters1[i])
            b.append(qafih_letters2[i])
            b.append(qafih_hrkat1[i])
            b.append(qafih_hrkat2[i])
    if task ==6:        
        b.extend(defect)
    b.append(b2)
    htm=''
    for i in b:
        htm = htm +str(i)+'\n'
    if task ==0:        
        htm=poem
    return htm

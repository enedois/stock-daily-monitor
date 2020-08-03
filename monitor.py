from yahoo_fin import stock_info as si
import pandas as pd
import pprint as pp
import datetime
import json
from prettytable import PrettyTable
import operator
from gtts import gTTS
import os
from playsound import playsound

stocks = [
"^BVSP",
##"AALR3.SA",
##"ABCB4.SA",
"ABEV3.SA",
##"ADHM3.SA",
"AGRO3.SA",
##"ALPA3.SA",
##"ALPA4.SA",
##"ALSO3.SA",
##"ALUP11.SA",
##"AMAR3.SA",
##"ANIM3.SA",
##"APER3.SA",
##"ARZZ3.SA",
"AZUL4.SA",
"B3SA3.SA",
##"BAHI3.SA",
##"BBAS3.SA",
##"BBDC3.SA",
##"BBDC4.SA",
##"BBRK3.SA",
"BBSE3.SA",
"BEEF3.SA",
##"BGIP4.SA",
##"BIDI11.SA",
##"BIDI4.SA",
##"BIOM3.SA",
"BKBR3.SA",
##"BMGB4.SA",
"BPAC11.SA",
##"BPAN4.SA",
##"BRAP3.SA",
##"BRAP4.SA",
"BRDT3.SA",
"BRFS3.SA",
"BRKM3.SA",
"BRKM5.SA",
##"BRML3.SA",
##"BRPR3.SA",
"BRSR3.SA",
"BRSR6.SA",
##"BSEV3.SA",
"BTOW3.SA",
"CAML3.SA",
##"CARD3.SA",
##"CCPR3.SA",
##"CCRO3.SA",
##"CEAB3.SA",
##"CEDO4.SA",
##"CESP3.SA",
##"CESP6.SA",
##"CGRA3.SA",
##"CGRA4.SA",
"CIEL3.SA",
##"CLSC4.SA",
##"CMIG3.SA",
##"CMIG4.SA",
"CNTO3.SA",
##"COCE5.SA",
##"COGN3.SA",
##"CPFE3.SA",
##"CPLE3.SA",
##"CPLE6.SA",
##"CPRE3.SA",
##"CRDE3.SA",
"CRFB3.SA",
##"CSAN3.SA",
##"CSMG3.SA",
##"CSNA3.SA",
##"CTNM4.SA",
##"CVCB3.SA",
##"CYRE3.SA",
##"DIRR3.SA",
"DTEX3.SA",
##"ECOR3.SA",
"EGIE3.SA",
##"ELEK4.SA",
##"ELET3.SA",
##"ELET6.SA",
##"EMBR3.SA",
##"ENAT3.SA",
"ENBR3.SA",
##"ENEV3.SA",
##"ENGI11.SA",
"EQTL3.SA",
##"EUCA4.SA",
##"EVEN3.SA",
##"EZTC3.SA",
##"FESA4.SA",
"FLRY3.SA",
##"FRAS3.SA",
##"GEPA4.SA",
##"GFSA3.SA",
##"GGBR3.SA",
##"GGBR4.SA",
##"GNDI3.SA",
##"GOAU3.SA",
##"GOAU4.SA",
##"GOLL4.SA",
##"GRND3.SA",
##"GSHP3.SA",
##"GUAR3.SA",
##"HAPV3.SA",
##"HBOR3.SA",
##"HGTX3.SA",
##"HYPE3.SA",
##"IDVL3.SA",
##"IDVL4.SA",
##"IGTA3.SA",
"IRBR3.SA",
"ITSA3.SA",
"ITSA4.SA",
##"ITUB3.SA",
##"ITUB4.SA",
##"JBSS3.SA",
##"JFEN3.SA",
##"JHSF3.SA",
##"JSLG3.SA",
##"KEPL3.SA",
"KLBN11.SA",
"LAME3.SA",
"LAME4.SA",
##"LCAM3.SA",
##"LEVE3.SA",
##"LIGT3.SA",
"LINX3.SA",
##"LIQO3.SA",
##"LLIS3.SA",
##"LOGG3.SA",
##"LOGN3.SA",
##"LPSB3.SA",
##"LREN3.SA",
"LWSA3.SA",
##"MDIA3.SA",
##"MDNE3.SA",
"MEAL3.SA",
##"MGLU3.SA",
"MILS3.SA",
##"MOVI3.SA",
##"MRFG3.SA",
##"MRVE3.SA",
##"MTRE3.SA",
##"MULT3.SA",
##"MYPK3.SA",
##"NEOE3.SA",
##"NTCO3.SA",
##"ODPV3.SA",
##"OFSA3.SA",
##"OMGE3.SA",
##"PARD3.SA",
##"PCAR3.SA",
##"PCAR4.SA",
##"PETR3.SA",
##"PETR4.SA",
##"PFRM3.SA",
##"PINE4.SA",
##"PMAM3.SA",
##"POMO3.SA",
##"POMO4.SA",
##"POSI3.SA",
##"PRIO3.SA",
##"PRNR3.SA",
##"PSSA3.SA",
##"PTBL3.SA",
##"PTNT4.SA",
##"QUAL3.SA",
##"RADL3.SA",
##"RAIL3.SA",
##"RAPT3.SA",
##"RAPT4.SA",
##"RDNI3.SA",
##"RENT3.SA",
##"RLOG3.SA",
##"RNEW11.SA",
##"RNEW3.SA",
##"RNEW4.SA",
"ROMI3.SA",
##"RSID3.SA",
##"SANB11.SA",
"SAPR11.SA",
##"SAPR4.SA",
##"SBSP3.SA",
##"SCAR3.SA",
##"SEER3.SA",
##"SGPS3.SA",
##"SHOW3.SA",
"SLCE3.SA",
##"SMLS3.SA",
##"SMTO3.SA",
##"SQIA3.SA",
##"STBP3.SA",
##"SULA11.SA",
"SUZB3.SA",
"TAEE11.SA",
##"TASA3.SA",
##"TASA4.SA",
##"TCSA3.SA",
##"TECN3.SA",
##"TEND3.SA",
##"TESA3.SA",
##"TGMA3.SA",
##"TIET11.SA",
##"TIMP3.SA",
"TOTS3.SA",
##"TRIS3.SA",
"TRPL4.SA",
##"TUPY3.SA",
##"UCAS3.SA",
##"UGPA3.SA",
##"UNIP6.SA",
##"USIM3.SA",
##"USIM5.SA",
##"VALE3.SA",
##"VIVA3.SA",
##"VIVT4.SA",
##"VLID3.SA",
##"VULC3.SA",
##"VVAR3.SA",
"WEGE3.SA",
##"WIZS3.SA",
##"YDUQ3.SA"
]

low = dict.fromkeys(stocks,999999999)
high = dict.fromkeys(stocks,0)

while(bool(True)):
    t = PrettyTable()
    t.field_names = ["Ticker","Agora","Min","Max","DeltaMin","DeltaMax"]

    for stock in stocks:
        try:
            precoagora = si.get_live_price(stock)
            
            #print(stock, si.get_live_price(stock))
            if (low.get(stock)> precoagora):
                print(stock,"no mínimo ->","%.2f" % precoagora)
                low[stock] = precoagora

                #play sound
                #mytext = (stock+"no mínimo")
                #myobj = gTTS(text=mytext, lang="pt", slow=False)
                #myobj.save("msg.mp3")
                # Playing the converted file
                #playsound('msg.mp3')
                #os.remove("msg.mp3")

                #print(precoagora)

            if (high.get(stock)< precoagora):
                #print(stock,"no máximo ->","%.2f" % precoagora)
                high[stock] = precoagora
                #print(precoagora)        
            t.add_row([stock,
                       round(precoagora,2),                      
                       round(low.get(stock),2),
                       round(high.get(stock),2),
                       round(float(precoagora/(low.get(stock))-1)*100,4),
                       round(float(precoagora/(high.get(stock))-1)*100,4)])
  
        except Exception as e:
            print("Erro:", e, stock)

    
    print (t.get_string(sortby="DeltaMin",reversesort = False))

    #json.dump(low, open('low.json', 'w'))
    #json.dump(high, open('high.json', 'w'))
    #pp.pprint(low)
    #pp.pprint(high)

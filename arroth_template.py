# coding: utf8
from __future__ import unicode_literals


# setting explicit height and max-width: none on the Html is required for
# Jupyter to render it properly in a cell
            
ARROTH_TABLE = """
<div align="right" style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;line-height:107%;font-size:15px;font-family:"Calibri","sans-serif";'>
    <table dir="rtl" style="float: right;width: 4.9e+2pt;border-collapse:collapse;border:none;margin-left:6.75pt;margin-right:6.75pt;">
        <tbody>
            <tr class="tasks">
                <td style="width: 58.4pt;border: 1pt solid windowtext;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><em><span style="font-size:24px;font-family:Aldhabi;">المهام</span></em></p>
                </td>
                <td colspan="{colspan1}" style="width:431.6pt;border:solid windowtext 1.0pt;border-right:none;background:#FBE4D5;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><em><span style="font-size:24px;font-family:Aldhabi;">التفاصيل</span></em></p>
                </td>
            </tr>

            {poem_heder} 
            
            
            {verses_table}
            
          <tr class="defect">
                <td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><em><span style="font-size:24px;font-family:Aldhabi;">عيوب القافية:</span></em></p>
                </td>
                <td colspan="{colspan1}" style="width:431.6pt;border-top:none;border-left:  solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:  none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><em><span style="font-size:24px;font-family:Aldhabi;">&nbsp;{defect} &nbsp;</span></em></p>
                </td>
            </tr>
            
        </tbody>
    </table>
</div>
"""
                                  

POEM_INFO = """
<tr class="title">
                <td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><em><span style="font-size:24px;font-family:Aldhabi;">القصيدة:</span></em></p>
                </td>
                <td colspan="{colspan1}" style="width:431.6pt;border-top:none;border-left:  solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:  none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><em><span style="font-size:24px;font-family:Aldhabi;">&nbsp;{title}&nbsp;</span></em></p>
                </td>
            </tr>
            <tr class="poet">
                <td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><em><span style="font-size:24px;font-family:Aldhabi;">الشاعر:</span></em></p>
                </td>
                <td colspan="{colspan1}" style="width:431.6pt;border-top:none;border-left:  solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:  none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><em><span style="font-size:24px;font-family:Aldhabi;">{poet}</span></em></p>
                </td>
            </tr>
            <tr class="period">
                <td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><em><span style="font-size:24px;font-family:Aldhabi;">الفترة:</span></em></p>
                </td>
                <td colspan="{colspan1}" style="width:431.6pt;border-top:none;border-left:  solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:  none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><em><span style="font-size:24px;font-family:Aldhabi;">{period}</span></em></p>
                </td>
            </tr>
            <tr class="topic">
                <td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><em><span style="font-size:24px;font-family:Aldhabi;">الموضوع:</span></em></p>
                </td>
                <td colspan="{colspan1}" style="width:431.6pt;border-top:none;border-left:  solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:  none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><em><span style="font-size:24px;font-family:Aldhabi;">{topic}</span></em></p>
                </td>
            </tr>
            <tr class="sea">
                <td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><em><span style="font-size:24px;font-family:Aldhabi;">البحر:</span></em></p>
                </td>
                <td colspan="{colspan1}" style="width:431.6pt;border-top:none;border-left:  solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:  none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><em><span style="font-size:24px;font-family:Aldhabi;"> &nbsp;{sea}</span></em></p>
                </td>
            </tr>
            <tr class="rawy">
                <td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">حرف الروي:</span></p>
                </td>
                <td colspan="{colspan1}" style="width:431.6pt;border-top:none;border-left:  solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:  none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Arabic Typesetting;">{Rawy}</span></p>
                </td>
            </tr>
"""




POEM_ID="""
            <tr class="poem_id">
                <td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">البيت رقم:</span></p>
                </td>
                <td colspan="{colspan1}" style="width:431.6pt;border-top:none;border-left:  solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:  none;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><strong><span style='font-size:29px;font-family:"Arabic Typesetting";'>{poem_id}</span></strong></p>
                </td>
            </tr>
"""


POEM_VERSE="""
            <tr class="byt">
                <td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">تشطير البيت:</span></p>
                </td>
                <td colspan="{colspan2}" style="width:215.6pt;border-top:none;border-left:  solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:  none;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">{sdr_imlaai_writeing}</span></p>
                    <audio src="{audio_sdr}" controls=""> Your browser does not support the audio element.</audio>
                </td>
                <td colspan="{colspan2}" style="width:3.0in;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">{agz_imlaai_writeing}</span></p>
                    <audio src="{audio_agz}" controls=""> Your browser does not support the audio element.</audio>
                </td>
            </tr>
            <tr class="arroth_writeing">
                <td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">الكتابة العروضية:</span></p>
                </td>
                <td colspan="{colspan2}" style="width:215.6pt;border-top:none;border-left:  solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:  none;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">{sdr_arroth_writeing}</span></p>
                </td>
                <td colspan="{colspan2}" style="width:3.0in;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">{agz_arroth_writeing}</span></p>
                </td>
            </tr>
"""



#VERSE_BODY=="""{tafilat_pattern_table}"""



WORDS_SPLIT_BODY="""
<tr class="verse_words_split">           
<td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">التقطيع:</span></p>
                </td>
               {verse_words_split}
            </tr>           
"""



VERSE_WORDS_SPLIT="""
<td colspan="{colspan3}" style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:{bcolor};padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;color:{fcolor};">{words_split}</span></p>
                </td>
"""

TAFILAHT_SPLIT_BODY="""
            <tr class="verse_tafilat_split">           
<td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">التفعيلات:</span></p>
                </td>
               {verse_tafilat_split}
            </tr>           
"""



VERSE_TAFILAT_SPLIT="""
<td colspan="{colspan3}" style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:{bcolor};padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;color:{fcolor};">{tafilat_split}</span></p>
                </td>
"""



TAFILAHT_CODE_BODY="""
            <tr class="set_tafilat_code">           
<td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">الترميز:</span></p>
                </td>
               {set_tafilat_code}
            </tr>           
"""



VERSE_TAFILAT_CODE="""
<td colspan="{colspan3}" style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:{bcolor};padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;color:{fcolor};">{tafilat_code}</span></p>
                </td>
"""


ZHAAF_EILAH_BODY="""
            <tr class="set_zhaaf_eilah">           
<td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">الزحافات والعلل:</span></p>
                </td>
               {set_zhaaf_eilah}
            </tr>  
            
"""



VERSE_ZHAAF_EILAH="""
<td colspan="{colspan3}" style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:{bcolor};padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;color:{fcolor};">{zhaaf_eilah}</span></p>
                </td>
"""

ZHAAF_EILAH_INFO="""
            <tr class="zhaaf_eilah_det">
                <td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">التفاصيل:</span></p>
                </td>
                <td colspan="{colspan1}" style="width:431.6pt;border-top:none;border-left:  solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:  none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Arabic Typesetting;">زحاف جرى مجرى العلة في الضرب</span></p>
                </td>
"""

VERSE_BROKEING="""
<tr class="tafilat_brokeing">
                <td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">التكسير:</span></p>
                </td>
                <td colspan="{colspan1}" style="width:431.6pt;border-top:none;border-left:  solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:  none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Arabic Typesetting;">{tafilat_brokeing}</span></p>
                </td>
            </tr>
"""

VERSE_CORRECT_BROKEING="""
<tr class="tafilat_correct_brokeing">
                <td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">تصحيح التكسير:</span></p>
                </td>
                <td colspan="{colspan1}" style="width:431.6pt;border-top:none;border-left:  solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:  none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:20px;font-family:Arabic Typesetting;">{tafilat_correct_brokeing}</span></p>
                </td>
            </tr>
"""


VERSE_RHYME="""
            <tr class="rhyme">
                <td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">القافية:</span></p>
                </td>
                <td colspan="{colspan1}" style="width:431.6pt;border-top:none;border-left:  solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:  none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">{rhyme}</span></p>
                </td>
            </tr>
            
            <tr class="loc">
                <td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">حدود القافية:</span></p>
                </td>
                <td colspan="{colspan1}" style="width:431.6pt;border-top:none;border-left:  solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:  none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">{loc1}<span style="color:red;">{loc2}</span>{loc3}</span></p>
                </td>
            </tr>
            
            <tr class="qafih_type">
                <td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">نوع القافية:</span></p>
                </td>
                <td colspan="{colspan1}" style="width:431.6pt;border-top:none;border-left:  solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:  none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">{qafih_type}</span></p>
                </td>
            </tr>
"""


RHYME_LETTERS="""
            <tr class="qafih_letters1">
                <td rowspan="2" style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">حروف القافية:</span></p>
                </td>
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">الرَّويّ</span></p>
                </td>
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">الوصل</span></p>
                </td>
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">الخروج</span></p>
                </td>
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">الرَّدْف</span></p>
                </td>
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">التَّأسيس</span></p>
                </td>
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">الدَّخيل</span></p>
                </td>
            </tr>
            <tr class="qafih_letters2">            
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {rawy}
                </td>
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {wsl}
                </td>
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {krg}
                </td>
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {rdf}
                </td>
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {tasis}
                </td>
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {dkil}
                </td>
         
            </tr>

            <tr class="qafih_hrkat1">
                <td rowspan="2" style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">حركات القافية:</span></p>
                </td>
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">المَجرَى</span></p>
                </td>
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">التَّوجيه</span></p>
                </td>
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">النَّفاذ</span></p>
                </td>
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">الإشباع</span></p>
                </td>
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">الحَذْو</span></p>
                </td>
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">الرَّسّ</span></p>
                </td>
            </tr>
            <tr class="qafih_hrkat2">
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {mgry}
                </td>
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {tojih}
                </td>
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {nfath}
                </td>
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {ishba}
                </td>
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {hdo}
                </td>
                <td colspan="{colspan4}" style="width:71.9pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {ras}
                </td>
            </tr>
"""

RHYME_LETTERS1="""
            <tr>
                <td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">حروف القافية:</span></p>
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">الرَّويّ</span></p>
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">الوصل</span></p>
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">الخروج</span></p>
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">الرَّدْف</span></p>
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">التَّأسيس</span></p>
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">الدَّخيل</span></p>
                </td>
            </tr>
            <tr> 
                <td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">تفاصيل حروف القافية:</span></p>
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {rawy}
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {wsl}
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {krg}
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {rdf}
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {tasis}
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {dkil}
                </td>
         
            </tr>

            <tr>
                <td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">حركات القافية:</span></p>
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">المَجرَى</span></p>
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">التَّوجيه</span></p>
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">النَّفاذ</span></p>
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">الإشباع</span></p>
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">الحَذْو</span></p>
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:#DEEAF6;padding:0in 5.4pt 0in 5.4pt;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">الرَّسّ</span></p>
                </td>
            </tr>
            <tr>
                <td style="width: 58.4pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(251, 228, 213);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">تفاصيل حركات القافية:</span></p>
                </td>
                            <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {mgry}
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {tojih}
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {nfath}
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {ishba}
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {hdo}
                </td>
                <td style="width:53.95pt;border-top:none;border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:none;background:white;padding:0in 5.4pt 0in 5.4pt;">
                    {ras}
                </td>
            </tr>
"""


QAFIH_LABELS1="""
<p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">{loc1}</span></p>
<p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">{loc2}</span></p>
"""
QAFIH_LABELS2="""
<p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">{loc2}</span></p>
                    <p dir="RTL" style='margin-right:0in;margin-left:0in;font-size:15px;font-family:"Calibri","sans-serif";margin-top:12.0pt;margin-bottom:  12.0pt;line-height:107%;text-align:center;'><span style="font-size:24px;font-family:Aldhabi;">{loc1}<span style="color:red;">{loc2}</span>{loc3}</span></p>
"""


from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivy.lang.builder import Builder

stringy = """
<districtie>:
    ScrollView:
        MDList:
            id:list_district
            #orientation:"vertical"
            padding: "20dp","50dp"
            spacing:"30dp"
            size_hint:(1,None)
            #adaptive_width: True
            adaptive_hieght: True
<district_attribute>:
    radius:[30,]
    size_hint_y:None
    adaptive_height:True
    # size_hint_x:None
    # adaptive_width:True
    #size_hint:(None,None)
    size:"120dp","150dp"
    pos_hint:{"center_x":0.5,"center_y":0.5}
    elevation:8
    MDScreen:
        md_bg_color:61/255,132/255,184/255,1
        radius:["20dp",]
        MDFillRoundFlatButton:
            md_bg_color:1,0,0,0
            size_hint:(1,1)
            on_release:
                app.on_tab_switch_district("Hospital")
                app.change_hospital_page(lb_district_name.text)
        MDBoxLayout:
            orientation:"vertical"
            padding: "20dp","30dp"
            MDLabel:
                id: lb_district_name
                markup:True
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                font_style: "H4"
                halign: "right"
            MDLabel:
                id: lb_district_hospital
                markup:True
                size_hint_y:None
                adaptive_height:True
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                font_style: "Body1"
                halign: "right"
            



"""

class district_attribute(MDCard):
    pass
class districtie(MDScreen):
    pass


Builder.load_string(stringy)
# class startie(MDApp):
#     def build(self):
#         return districtie()
#
# startie().run()
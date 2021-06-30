from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder

stringy="""
<statie>:
    md_bg_color:0.8,0.8,0.8,0.5
    ScrollView:
        MDList:
            #orientation:"vertical"
            padding: "20dp","50dp"
            spacing:"30dp"
            size_hint:(1,None)
            #adaptive_width: True
            adaptive_hieght: True
            MDCard:
                md_bg_color:186/255,245/255,59/255,1
                radius:[30,]
                size_hint_y:None
                adaptive_height:True
                # size_hint_x:None
                # adaptive_width:True
                #size_hint:(None,None)
                size:"210dp","300dp"
                pos_hint:{"center_x":0.5,"center_y":0.5}
                elevation:8
                MDScreen:
                    md_bg_color:186/255,245/255,59/255,1
                    radius:["20dp",]
                    MDFillRoundFlatButton:
                        md_bg_color:1,0,0,0
                        size_hint:(1,1)
                        on_release: app.on_tab_switch_district("District")
                    MDBoxLayout:
                        orientation:"vertical"
                        padding: "20dp","10dp"
                        MDLabel:
                            markup:True
                            text:"[color=#000000]TamilNadu[/color]"
                            font_style: "H4"
                            halign: "right"
                        MDLabel:
                            markup:True
                            size_hint_y:None
                            adaptive_height:True
                            theme_text_color: "Custom"
                            text_color: 0.05,0.05,0.05,1
                            text:"Latest Update: 12-05-2021"
                            font_style: "Body1"
                            halign: "right"
                        MDLabel:
                            markup:True
                            theme_text_color: "Custom"
                            text_color: 0.05,0.05,0.05,1
                            text:"Available Hospital: 566"
                            font_style: "Body1"
                            halign: "right"
            MDCard:
                md_bg_color:186/255,245/255,59/255,1
                radius:[30,]
                size_hint_y:None
                adaptive_height:True
                # size_hint_x:None
                # adaptive_width:True
                #size_hint:(None,None)
                size:"210dp","300dp"
                pos_hint:{"center_x":0.5,"center_y":0.5}
                elevation:8
                MDScreen:
                    md_bg_color:254/255,162/255,227/255,1
                    radius:["20dp",]
                    MDFillRoundFlatButton:
                        md_bg_color:1,0,0,0
                        size_hint:(1,1)
                    MDBoxLayout:
                        orientation:"vertical"
                        padding: "20dp","10dp"
                        MDLabel:
                            markup:True
                            text:"[color=#000000]Kerala[/color]"
                            font_style: "H4"
                            halign: "right"
                        MDLabel:
                            markup:True
                            size_hint_y:None
                            adaptive_height:True
                            theme_text_color: "Custom"
                            text_color: 0.05,0.05,0.05,1
                            text:"Latest Update: Coming Soon..!"
                            font_style: "Body1"
                            halign: "right"
                        MDLabel:
                            markup:True
                            theme_text_color: "Custom"
                            text_color: 0.05,0.05,0.05,1
                            text:"Available Hospital: Coming Soon..!"
                            font_style: "Body1"
                            halign: "right"
            MDCard:
                md_bg_color:186/255,245/255,59/255,1
                radius:[30,]
                size_hint_y:None
                adaptive_height:True
                # size_hint_x:None
                # adaptive_width:True
                #size_hint:(None,None)
                size:"210dp","300dp"
                pos_hint:{"center_x":0.5,"center_y":0.5}
                elevation:8
                MDScreen:
                    md_bg_color:186/255,245/255,59/255,1
                    radius:["20dp",]
                    MDFillRoundFlatButton:
                        md_bg_color:1,0,0,0
                        size_hint:(1,1)
                    MDBoxLayout:
                        orientation:"vertical"
                        padding: "20dp","10dp"
                        MDLabel:
                            markup:True
                            text:"[color=#000000]AndraPradesh[/color]"
                            font_style: "H4"
                            halign: "right"
                        MDLabel:
                            markup:True
                            size_hint_y:None
                            adaptive_height:True
                            theme_text_color: "Custom"
                            text_color: 0.05,0.05,0.05,1
                            text:"Latest Update: Coming Soon..!"
                            font_style: "Body1"
                            halign: "right"
                        MDLabel:
                            markup:True
                            theme_text_color: "Custom"
                            text_color: 0.05,0.05,0.05,1
                            text:"Available Hospital: Coming Soon..!"
                            font_style: "Body1"
                            halign: "right"
            MDCard:
                md_bg_color:254/255,162/255,227/255,1
                radius:[30,]
                size_hint_y:None
                adaptive_height:True
                # size_hint_x:None
                # adaptive_width:True
                #size_hint:(None,None)
                size:"210dp","300dp"
                pos_hint:{"center_x":0.5,"center_y":0.5}
                elevation:8
                MDScreen:
                    md_bg_color:254/255,162/255,227/255,1
                    radius:["20dp",]
                    MDFillRoundFlatButton:
                        md_bg_color:1,0,0,0
                        size_hint:(1,1)
                    MDBoxLayout:
                        orientation:"vertical"
                        padding: "20dp","10dp"
                        MDLabel:
                            markup:True
                            text:"[color=#000000]Karnataka[/color]"
                            font_style: "H4"
                            halign: "right"
                        MDLabel:
                            markup:True
                            size_hint_y:None
                            adaptive_height:True
                            theme_text_color: "Custom"
                            text_color: 0.05,0.05,0.05,1
                            text:"Latest Update: Coming Soon..!"
                            font_style: "Body1"
                            halign: "right"
                        MDLabel:
                            markup:True
                            theme_text_color: "Custom"
                            text_color: 0.05,0.05,0.05,1
                            text:"Available Hospital: Coming Soon..!"
                            font_style: "Body1"
                            halign: "right"
                
            
    
"""
class statie(MDScreen):
    pass
Builder.load_string(stringy)
# class startie(MDApp):
#     def build(self):
#         return statie()
#
# startie().run()
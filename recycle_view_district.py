from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty,StringProperty
from kivy.clock import Clock


stringy = """
<District_screen>:
    id:hos_district
    MDBoxLayout:
        orientation:"vertical"
        spacing:"10dp"
        md_bg_color:0.8,0.8,0.8,0.5
        MDBoxLayout:
            md_bg_color:0.8,0.8,0.8,0.9
            size_hint_y:None
            padding: "20sp","10sp"
            adaptive_height:True
            pos_hint:{"center_x":0.5}
            MDIconButton:
                icon:"magnify"
                pos_hit: {"center_x":0, "center_y":1}
            MDTextField:
                id:text_input
                line_color_focus: 0, 0, 0, 0.5
                hint_text: "Search"
                mode: "rectangle"
                on_text:root.district_list(root.api,text_input.text)
        RecycleView:
            id: rv
            key_viewclass: "viewclass"
            key_size: "height"
            RecycleBoxLayout:
                padding: "20dp","20dp"
                spacing: "20dp"
                id:rv_bx
                default_size: None, dp(200)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: "vertical"

<Districtscroll>:
    id:starting_id
    value_1:""
    value_2:""
    radius:[30,]
    size_hint_y:None
    adaptive_height:True
    # size_hint_x:None
    # adaptive_width:True
    #size_hint:(None,None)
    # size:"120dp","150dp"
    # height: "300dp"
    pos_hint:{"center_x":0.5,"center_y":0.5}
    #elevation:8
    MDScreen:
        md_bg_color:root.md_bg_color
        radius:["20dp",]
        MDFillRoundFlatButton:
            id:starting_id
            md_bg_color:1,0,0,0
            size_hint:(1,1)
            on_release:
                app.change_hospital_page(root.value_1)
                app.on_tab_switch_district("Hospital")
        MDBoxLayout:
            orientation:"vertical"
            padding: "20dp","30dp"
            MDLabel:
                markup:True
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style: "H5"
                halign: "right"
                text:root.value_1
            MDLabel:
                markup:True
                size_hint_y:None
                adaptive_height:True
                theme_text_color: "Custom"
                text_color: 0,0,0,1
                font_style: "Body1"
                halign: "right"
                text:root.value_2




"""
class Districtscroll(MDCard):
    value_1 = StringProperty("llalal")
    value_2 = StringProperty("lla")

class District_screen(MDScreen):

    def add_icon_item(self,distrcit,hospital_no,color):
        self.ids.rv.data.append(
            {
                "viewclass": "Districtscroll",
                "value_1":distrcit,
                "value_2":hospital_no,
                "md_bg_color": color
            }
        )
    def district_list (self, api,text=""):
        """Builds a list of icons for the screen MDIcons."""
        self.ids.rv.data = []
        self.api=api
        self.color_flag=0
        for district in api.api_dict_available_beds["district_sorted_hospital"]:
            if self.color_flag==1:
                self.color_flag=0
                colorie=(254/255,162/255,227/255,1)
            else:
                self.color_flag=1
                colorie=(186/255,245/255,59/255,1)
            if text!=None and text!="":
                if text in district or text in district.lower():
                    self.add_icon_item(district,"Available Hospital Count:"+str(len(api.api_dict_available_beds["district_sorted_hospital"].get(district))),colorie)
            else:
                self.add_icon_item(district, "Available Hospital Count:" + str(len(api.api_dict_available_beds["district_sorted_hospital"].get(district))),colorie)
                print("Available Hospital Count:" + str(len(api.api_dict_available_beds["district_sorted_hospital"].get(district))))
Builder.load_string(stringy)
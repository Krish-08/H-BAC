from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from kivy.clock import Clock
import time

#color:white 240/255,235/255,204/255,1  F0EBBC
#color:blue 61/255,132/255,184/255   3D84B4

stringie="""
<screen_manager_main>:
    MDScreen:
        name:"loading_page"
        FitImage:
            size:self.size
            pos:self.pos
            source:"images/b-hac.png"
        MDBoxLayout:
            orientation:"vertical"
            spacing:"10dp"
            padding: "10dp","10dp"
            size_hint:(0.8,0.8)
            md_bg_color:0.5,0.5,0.5,0.5
            radius:[25,]
            pos_hint:{'center_x': .5, 'center_y': .5}
            MDLabel:
                text:"[color=#ffffff]Beds Availability:\\n[size=30]By Py-Developers[/color]"
                halign:"center"
                font_style:"H2"
                markup:True
                pos_hint:{'center_x': .5, 'center_y': .5}
            MDBoxLayout:
                size_hint:(0.9,None)
                adaptive_height:True
                halign:"right"
                MDLabel:
                    text:"Loading....."
                    font_style:"H5"
                    halign:"center"
                    theme_text_color:"Custom"
                    text_color:1,1,1,1
    MDScreen:
        id:startie
        md_bg_color:240/255,235/255,204/255,1
        MDBoxLayout:
            orientation:"vertical"
            MDToolbar:
                specific_text_color:  240/255,235/255,204/255,1
                markup:True
                title:"Bed's Availability Covid-19"
                md_bg_color:61/255,132/255,184/255,1
                pos_hint:{"top":1}
                elevation:"15dp"
                right_action_items:[["menu",lambda x: nav_drawer.set_state("open")]]
            ScreenManager:
                id:sub_screen_manager
                Screen:
                    name: "home_page"
                    MDTabs:
                        id: tabs
                        background_color: 61/255,132/255,184/255,1
                        text_color_normal: 240/255,235/255,204/255,1
                        text_color_active: 240/255,235/255,204/255,1
                        indicator_color :   1,0,0,1
        
        MDNavigationLayout:
            MDNavigationDrawer:
                id:nav_drawer
                md_bg_color:61/255,132/255,184/255,1
                anchor:"right"
                elevation:"20dp"
                orientation:"vertical"
                padding:"20sp","10sp"
                MDLabel:
                    size_hint_y: None
                    #md_bg_color:0.5,0.5,0.5,0.3
                    height: self.texture_size[1]
                    text_size: self.width, None
                    padding: 10, 10
                    font_style:"H6"
                    markup:True
                    text:"[color=#f0ebcc]Py_developers:[/color]"
                    icon:"home"
                ScrollView:
                    MDList:
                        spacing:"10dp"
                        MDCard:
                            canvas:
                                RoundedRectangle:
                                    size:self.size
                                    pos:self.pos
                                    source:"images/nav_draw_image.jpg"
                            radius:[30,]
                            size_hint_y:None
                            adaptive_height:True
                            # size_hint_x:None
                            # adaptive_width:True
                            #size_hint:(None,None)
                            size:"210dp","190dp"
                            pos_hint:{"center_x":0.5,"center_y":0.5}
                            elevation:"12dp"
                        OneLineIconListItem:
                            text:"[color=#f0ebcc]Home[/color]"
                            markup:True
                            on_release: 
                                root.change_to_home()
                                nav_drawer.set_state("close")
                            
                            IconLeftWidget:
                                icon:"home"
                                theme_text_color: "Custom"
                                text_color:240/255,235/255,204/255,1
                                on_release: 
                                    root.change_to_home()
                                    nav_drawer.set_state("close")
                                
                        OneLineIconListItem:
                            text:"[color=#f0ebcc]Info[/color]"
                            markup:True
                            on_release: 
                                root.change_to_info()
                                nav_drawer.set_state("close")
                            
                            IconLeftWidget:
                                icon:"alpha-i-circle"
                                theme_text_color: "Custom"
                                text_color:240/255,235/255,204/255,1
                                on_release: root.change_to_info()
                                on_release: 
                                    root.change_to_info()
                                    nav_drawer.set_state("close")
                        OneLineIconListItem:
                            text:"[color=#f0ebcc]About us[/color]"
                            markup:True
                            on_release: 
                                root.change_to_about()
                                nav_drawer.set_state("close")
                            
                            IconLeftWidget:
                                icon:"alpha-a-circle"
                                theme_text_color: "Custom"
                                text_color:240/255,235/255,204/255,1
                                on_release: root.change_to_info()
                                on_release: 
                                    root.change_to_about()
                                    nav_drawer.set_state("close")
                            
            
        
<home>:
    MDBoxLayout:
        MDLabel:
            text:"hello world"
            font_style:"H2"
<info>:
    MDBoxLayout:
        orientation:"vertical"
        padding:"20dp"
        spacing:"20dp"
        md_bg_color:0.5,0.5,0.5,0.3
        radius:[20,]
        size_hint:(0.9,0.9)
        pos_hint:{"center_x":0.5,"center_y":0.5}
        MDLabel:
            size_hint_y: None
            #md_bg_color:0.5,0.5,0.5,0.3
            height: self.texture_size[1]
            text_size: self.width, None
            padding: 10, 10
            font_style:"H5"
            markup:True
            text:"[color=#000000]Info:[/color]"
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True
            MDList:
                spacing:"10dp"
                MDCard:
                    canvas:
                        RoundedRectangle:
                            size:self.size
                            pos:self.pos
                            source:"images/info_card.jpg"
                    radius:[30,]
                    size_hint_y:None
                    adaptive_height:True
                    size_hint_x:None
                    adaptive_widget:True
                    #size_hint:(None,None)
                    size:"210dp","150dp"
                    pos_hint:{"center_x":0.5,"center_y":0.5}
                
                
    
                MDLabel:
                    size_hint_y: None
                    height: self.texture_size[1]
                    #text_size: self.width, None
                    padding: 10, 10
                    font_style:"Body1"
                    markup:True
                    text: "Covid-19 Bed's Availability:\\n      [color=#595959]With this app you can see the available number of beds."
<about>:
    MDBoxLayout:
        orientation:"vertical"
        padding:"20dp"
        spacing:"20dp"
        md_bg_color:0.5,0.5,0.5,0.3
        radius:[20,]
        size_hint:(0.9,0.9)
        pos_hint:{"center_x":0.5,"center_y":0.5}
        MDLabel:
            size_hint_y: None
            #md_bg_color:0.5,0.5,0.5,0.3
            height: self.texture_size[1]
            text_size: self.width, None
            padding: 10, 10
            font_style:"H5"
            markup:True
            text:"[color=#000000]About Us:[/color]"
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True
            MDList:
                spacing:"10dp"
                MDCard:
                    canvas:
                        RoundedRectangle:
                            size:self.size
                            pos:self.pos
                            source:"images/about_card.jpg"
                    radius:[30,]
                    size_hint_y:None
                    adaptive_height:True
                    size_hint_x:None
                    adaptive_widget:True
                    #size_hint:(None,None)
                    size:"210dp","150dp"
                    pos_hint:{"center_x":0.5,"center_y":0.5}
                
                
    
                MDLabel:
                    size_hint_y: None
                    height: self.texture_size[1]
                    #text_size: self.width, None
                    padding: 10, 10
                    font_style:"Body1"
                    markup:True
                    text:"Py-developers: \\nStudents of Thiagrajar College of Engineering.\\n\\nProgrammer: [color=#595959]Krish Prasanna & Dhanushwaran PS[/color]\\n\\nContact Us: [color=#595959]krish@student.tce.edu or dhanushwaran@student.tce.edu"
        
<Tab>:
<Tab_screen_manager>:
    hospital_tab:hospital_tab
    ScreenManager: 
        id:hospital_tab
        MDScreen:
            md_bg_color:255/255,0.6,0.6,0
            MDLabel:
                text:"[color=#3d84b4]Click some district in the district Tab[/color]"
                pos_hint:{"center_x":0.6,"center_y":0.5}
                markup:True
                font_style:"H2"
<dialog_box>:
    padding:"20dp","10dp"
    spacing: "10dp"
    size_hint_y: None
    size_hint_x: None
    orientation:"vertical"
    MDLabel:
        id:dialog_title
        font_style:"H4"
        size_hint_y:None
        adaptive_height:True
    ScrollView:
        do_scroll_x: False
        do_scroll_y: True
        MDList:
            MDLabel:
                id:dialog_content
                size_hint_y: None
                height: self.texture_size[1]
                #text_size: self.width, None
                padding: 10, 10
                font_style:"Body1"
                markup:True
        
    
"""
class loading_screen(MDScreen):
    pass

class hospital_tab_screen_manager(ScreenManager):
    pass
class Tab(MDFloatLayout, MDTabsBase):
    pass
class Tab_screen_manager(MDFloatLayout, MDTabsBase):
    hospital_tab=ObjectProperty(None)
class dialog_box(MDBoxLayout):
    pass
class screen_manager_main(ScreenManager):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.current="loading_page"
    def adding_widget(self):
        self.ids.startie.name="startie_page"

        # self.homie=home(name="home_page")
        # self.tab=Tab(title="Home")
        # self.tab.add_widget(self.homie)
        # self.ids.tabs.add_widget(self.tab)
        # self.homie.get_parent(self)
        import statie, districtie

        self.statie=statie.statie(name="state_page")
        self.tab=Tab(title="State",tab_label_text="State")
        self.tab.add_widget(self.statie)
        self.ids.tabs.add_widget(self.tab)

        self.districtie=districtie.districtie(name="district_page")
        self.tab=Tab(title="District",tab_label_text="District")
        self.tab.add_widget(self.districtie)
        self.ids.tabs.add_widget(self.tab)

        self.hospital_tab=Tab_screen_manager(title="Hospital")
        self.ids.tabs.add_widget(self.hospital_tab)

        self.infoie=info(name="info_page")
        self.ids.sub_screen_manager.add_widget(self.infoie)
        self.infoie.get_parent(self)

        self.aboutie = about(name="about_page")
        self.ids.sub_screen_manager.add_widget(self.aboutie)
        self.aboutie.get_parent(self)

    def change_to_home(self):
        #self.ids.nav_drawer.set_state="close"
        self.ids.sub_screen_manager.current="home_page"
        self.transition.direction="right"
    def change_to_info(self):
        #self.ids.nav_drawer.set_state="close"
        self.ids.sub_screen_manager.current = "info_page"
        self.transition.direction="right"
    def change_to_about(self):
        #self.ids.nav_drawer.set_state="close"
        self.ids.sub_screen_manager.current = "about_page"
        self.transition.direction="right"


class home(MDScreen):
    def get_parent(self,parent_obj):
        self.parent_obj=parent_obj
    def nav_draw(self):
        self.parent_obj.ids.nav_drawer.set_state="open"
class info(MDScreen):
    def get_parent(self,parent_obj):
        self.parent_obj=parent_obj
    def nav_draw(self):
        self.parent_obj.ids.nav_drawer.set_state="open"
class about(MDScreen):
    def get_parent(self,parent_obj):
        self.parent_obj=parent_obj
    def nav_draw(self):
        self.parent_obj.ids.nav_drawer.set_state="open"

Builder.load_string(stringie)
class gui_start(MDApp):
    dialog=None
    start=None
    end=None
    end_basic=None
    end_loop_1=None
    end_loop_2=None
    def build(self):
        self.start=time.perf_counter()
        self.main=screen_manager_main()
        Clock.schedule_once(self.adding_widget, 5)
        return self.main
    def adding_widget(self,*args):
        self.main.adding_widget()
        self.end_basic=time.perf_counter()
        import districtie, json_api, hospitalie
        self.api=json_api.json_api()
        for district in self.api.api_dict_available_beds["district_sorted_hospital"]:
            district_card=districtie.district_attribute()
            district_card.ids.lb_district_name.text=district
            district_card.ids.lb_district_hospital.text ="Available Hospital:"+str(len(self.api.api_dict_available_beds["district_sorted_hospital"][district]))
            self.main.districtie.ids.list_district.add_widget(district_card)
        self.end_loop_1=time.perf_counter()
        for district in self.api.api_dict_available_beds["district_sorted_hospital"]:
            district_hospital_screen=hospitalie.hospitalie_district(name=district)
            for sn_no in self.api.api_dict_available_beds["district_sorted_hospital"][district]:
                district_hospital_card = hospitalie.hospital_attribute()
                hospital_name=self.api.api_dict_available_beds["Institution"][sn_no]
                bed_vacant = self.api.api_dict_available_beds["COVID BEDS Vacant"][sn_no]
                district_hospital_card.id=str(sn_no)
                district_hospital_card.ids.lb_hospital_name.text=hospital_name
                district_hospital_card.ids.lb_available_beds.text = "Available_vacant_beds"+str(bed_vacant)
                district_hospital_screen.ids.list_hospital.add_widget(district_hospital_card)
            district_hospital_screen.ids.district_name.text=district
            self.main.hospital_tab.hospital_tab.add_widget(district_hospital_screen)
            break

        self.main.current="startie_page"
        self.end=time.perf_counter()
        print(self.end-self.start," ",self.end_basic-self.start," ",self.end_loop_1-self.start)



    def on_tab_switch_district(self,name):
        try:
            self.main.ids.tabs.switch_tab(name)
        except StopIteration:
            self.switch_tab_by_name(name)
            pass

    def change_hospital_page(self,name):
        self.main.hospital_tab.hospital_tab.current=name
    def show_dialog_box(self,id):
        if not self.dialog:
            self.dialog_box=dialog_box()
            self.dialog_box.height = f"{Window.size[1]-300}dp"
            self.dialog_box.width=f"{Window.size[0]-70}dp"
            self.dialog_box.ids.dialog_title.text = self.api.api_dict_available_beds["Institution"][id]
            for hospital in self.api.api_dict_available_beds:
                self.dialog_box.ids.dialog_content.text=self.dialog_box.ids.dialog_content.text+"\n\n"+str(hospital)+" : "+str(self.api.api_dict_available_beds[hospital].get(id))
                print("h",str(self.api.api_dict_available_beds[hospital].get(id)))

            print(Window.size[1])
            self.dialog = MDDialog(
                title="Address:",
                type="custom",
                content_cls=self.dialog_box,
                buttons=[
                    MDFlatButton(
                        text="Close", text_color=self.theme_cls.primary_color,on_release=self.close_dialog
                    ),
                ],
            )
            self.dialog.open()
        print("id:",id)
    def close_dialog(self,*args):
        try:
            self.dialog.dismiss()
            self.dialog=None
        except:
            print("ey")
            self.dialog = None
            pass


def starting():
    print(multiprocessing.cpu_count())
    gui_start().run()
import multiprocessing
if __name__=="__main__":
    p1=multiprocessing.Process(target=starting)
    p1.start()

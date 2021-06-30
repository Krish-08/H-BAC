from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivy.core.window import Window
from kivy.clock import Clock
import time

# color:white 1,1,1,1  F0EBBC
# color:blue 50/255,50/255,50/255   3D84B4

stringie = """
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
            padding: "40dp","40dp"
            size_hint:(0.9,None)
            radius:[25,]
            adaptive_height:True
            MDLabel:
                text:"Loading....."
                font_style:"H5"
                halign:"center"
                theme_text_color:"Custom"
                text_color:1,1,1,1
    MDScreen:
        id:startie
        md_bg_color:1,1,1,1
        MDBoxLayout:
            orientation:"vertical"
            MDToolbar:
                specific_text_color:  1,1,1,1
                markup:True
                title:"H-BAC"
                md_bg_color:50/255,50/255,50/255,1
                pos_hint:{"top":1}
                elevation:"8dp"
                right_action_items:[["menu",lambda x: nav_drawer.set_state("open")]]
            ScreenManager:
                id:sub_screen_manager
                Screen:
                    name: "home_page"
                    FitImage:
                        size:self.size
                        pos:self.pos
                        source:"images/pattern_texture.jpg"
                    MDTabs:
                        id: tabs
                        background_color: 50/255,50/255,50/255,1
                        text_color_normal: 1,1,1,1
                        text_color_active: 1,1,1,1
                        indicator_color :   1,0,0,1
                        on_tab_switch: app.on_switch(*args)

        MDNavigationLayout:
            MDNavigationDrawer:
                id:nav_drawer
                md_bg_color:50/255,50/255,50/255,1
                anchor:"right"
                elevation:"5dp"
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
                    text:"[color=#ffffff]Py_developers:[/color]"
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
                            text:"[color=#ffffff]Home[/color]"
                            markup:True
                            on_release: 
                                root.change_to_home()
                                nav_drawer.set_state("close")

                            IconLeftWidget:
                                icon:"home"
                                theme_text_color: "Custom"
                                text_color:1,1,1,1
                                on_release: 
                                    root.change_to_home()
                                    nav_drawer.set_state("close")

                        OneLineIconListItem:
                            text:"[color=#ffffff]Info[/color]"
                            markup:True
                            on_release: 
                                root.change_to_info()
                                nav_drawer.set_state("close")

                            IconLeftWidget:
                                icon:"alpha-i-circle"
                                theme_text_color: "Custom"
                                text_color:1,1,1,1
                                on_release: root.change_to_info()
                                on_release: 
                                    root.change_to_info()
                                    nav_drawer.set_state("close")
                        OneLineIconListItem:
                            text:"[color=#ffffff]About us[/color]"
                            markup:True
                            on_release: 
                                root.change_to_about()
                                nav_drawer.set_state("close")

                            IconLeftWidget:
                                icon:"alpha-a-circle"
                                theme_text_color: "Custom"
                                text_color:1,1,1,1
                                on_release: root.change_to_info()
                                on_release: 
                                    root.change_to_about()
                                    nav_drawer.set_state("close")
                        OneLineIconListItem:
                            text:"[color=#ffffff]Close[/color]"
                            markup:True
                            on_release: 
                                nav_drawer.set_state("close")
                                app.stop()


                            IconLeftWidget:
                                icon:"close"
                                theme_text_color: "Custom"
                                text_color:1,1,1,1
                                on_release: root.change_to_info()
                                on_release: 
                                    nav_drawer.set_state("close")
                                    app.stop()



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
                    text: "H-BAC:\\n      [color=#595959]This application can be used to check the availability of beds in a hospital of your choice"
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
                    text:"Py-Developers: \\nStudents of Thiagrajar College of Engineering(TCE).\\n\\nProgrammer: [color=#595959]Krish Prasanna C R & Dhanushwaran PS[/color]\\n\\nContact Us:\\n\\t[color=#595959]krish@student.tce.edu\\n\\tdhanushwaran@student.tce.edu"

<Tab>:
<Tab_screen_manager>:
    hospital_tab:hospital_tab
    ScreenManager: 
        id:hospital_tab
        MDScreen:
            md_bg_color:0.8,0.8,0.8,0.5
            MDLabel:
                md_bg_color:0.8,0.8,0.8,0.9
                text:"[color=#000000]Click some district in the district Tab[/color]"
                pos_hint:{"center_x":0.5,"center_y":0.5}
                halign:"center"
                padding: "20dp","20dp"
                radius: ["30dp",]
                size_hint:(0.8,0.8)
                markup:True
                font_style:"H2"
<dialog_box>:
    padding:"20dp","10dp"
    spacing: "10dp"
    size_hint_y: None
    #size_hint_x: None
    height: "300dp"
    orientation:"vertical"
    MDLabel:
        id:dialog_title
        font_style:"H6"
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
    hospital_tab = ObjectProperty(None)


class dialog_box(MDBoxLayout):
    pass


class screen_manager_main(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current = "loading_page"

    def adding_widget(self):
        self.ids.startie.name = "startie_page"

        # self.homie=home(name="home_page")
        # self.tab=Tab(title="Home")
        # self.tab.add_widget(self.homie)
        # self.ids.tabs.add_widget(self.tab)
        # self.homie.get_parent(self)
        import statie

        self.statie = statie.statie(name="state_page")
        self.tab = Tab(title="State", tab_label_text="State")
        self.tab.add_widget(self.statie)
        self.ids.tabs.add_widget(self.tab)

        self.infoie = info(name="info_page")
        self.ids.sub_screen_manager.add_widget(self.infoie)
        self.infoie.get_parent(self)

        self.aboutie = about(name="about_page")
        self.ids.sub_screen_manager.add_widget(self.aboutie)
        self.aboutie.get_parent(self)

    def change_to_home(self):
        # self.ids.nav_drawer.set_state="close"
        self.ids.sub_screen_manager.current = "home_page"
        self.transition.direction = "right"

    def change_to_info(self):
        # self.ids.nav_drawer.set_state="close"
        self.ids.sub_screen_manager.current = "info_page"
        self.transition.direction = "right"

    def change_to_about(self):
        # self.ids.nav_drawer.set_state="close"
        self.ids.sub_screen_manager.current = "about_page"
        self.transition.direction = "right"


class home(MDScreen):
    def get_parent(self, parent_obj):
        self.parent_obj = parent_obj

    def nav_draw(self):
        self.parent_obj.ids.nav_drawer.set_state = "open"


class info(MDScreen):
    def get_parent(self, parent_obj):
        self.parent_obj = parent_obj

    def nav_draw(self):
        self.parent_obj.ids.nav_drawer.set_state = "open"


class about(MDScreen):
    def get_parent(self, parent_obj):
        self.parent_obj = parent_obj

    def nav_draw(self):
        self.parent_obj.ids.nav_drawer.set_state = "open"


Builder.load_string(stringie)


class gui_start(MDApp):
    dialog = None
    start = None
    end = None
    end_basic = None
    end_loop_1 = None
    end_loop_2 = None

    def build(self):
        self.main = screen_manager_main()
        self.main.adding_widget()
        Clock.schedule_once(self.adding_widget, 5)
        Clock.schedule_once(self.get_api, 3)
        self.current_tab_name = "State"
        self.dialog = None
        return self.main

    def adding_widget(self, *args):
        self.start = time.perf_counter()
        import recycle_view_district, recycle_viewie_test,json_api

        self.district_screen = recycle_view_district.District_screen(name="district_tab")
        self.district_screen.district_list(self.api)
        tab = Tab(title="District", tab_label_text="District")
        tab.add_widget(self.district_screen)
        self.main.ids.tabs.add_widget(tab)

        print(self.start - time.perf_counter())

        ####hospital
        self.hospital_tab = Tab_screen_manager(title="Hospital")
        self.main.ids.tabs.add_widget(self.hospital_tab)
        for district in self.api.api_dict_available_beds["district_sorted_hospital"]:
            district_hospital_screen = recycle_viewie_test.hospital_screen(name=district)
            district_hospital_screen.hospital_list(district, self.api)
            self.hospital_tab.hospital_tab.add_widget(district_hospital_screen)
        print(self.start - time.perf_counter())
        self.main.current = "startie_page"
        self.back_key()

    def get_api(self, *args):
        import json_api
        self.api = json_api.json_api()

    def back_key(self):
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    def hook_keyboard(self, window, key, *largs):
        if key == 27:
            try:
                self.main.ids.nav_drawer.set_state("close")
            except:
                pass
            if self.main.ids.sub_screen_manager.current == "about_page" or self.main.ids.sub_screen_manager.current == "info_page":
                try:
                    self.main.ids.sub_screen_manager.current = "home_page"
                except:
                    pass

            try:
                if self.current_tab_name == "State":
                    print("stop")
                    self.stop()
            except:
                pass
            try:
                if self.current_tab_name == "District":
                    print("u1")
                    self.on_tab_switch_district("State")
            except:
                pass
            try:
                if self.current_tab_name == "Hospital":
                    print("uu")
                    self.on_tab_switch_district("District")
            except:
                pass
            print("jjjjj")
            return True

    def on_tab_switch_district(self, name):
        try:
            self.main.ids.tabs.switch_tab(name)
            self.current_tab_name = name
        except StopIteration:
            self.switch_tab_by_name(name)
            pass

    def on_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        print(instance_tabs, instance_tab, instance_tab_label, tab_text)
        print("text:", tab_text)
        self.current_tab_name = tab_text

    def change_hospital_page(self, name):
        self.hospital_tab.hospital_tab.current = name

    def share_call(self, *args):
        call = self.share_callie
        call = int(float(call))
        if call != 0:
            from kivy import platform

            if platform == 'android':
                from jnius import autoclass
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                Intent = autoclass('android.content.Intent')
                Uri = autoclass('android.net.Uri')
                String = autoclass('java.lang.String')
                intent = Intent(Intent.ACTION_CALL)
                intent.setData(Uri.parse("tel:" + str(call)))
                PythonActivity.mActivity.startActivity(intent)

    def share_text(self, *args):
        print("text")
        from kivy import platform
        if platform == 'android':
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            String = autoclass('java.lang.String')
            intent = Intent()
            intent.setAction(Intent.ACTION_SEND)
            intent.putExtra(Intent.EXTRA_TEXT, String('{}'.format(self.share_textie)))
            intent.setType('text/plain')
            chooser = Intent.createChooser(intent, String("whatapp"))
            PythonActivity.mActivity.startActivity(chooser)

    def show_dialog_box(self, id):
        print(id, type(id))
        # id=int(id)
        print(id, type(id), self.dialog)
        self.dialog = None
        if not self.dialog:
            self.dialog_box = dialog_box()
            self.dialog_box.ids.dialog_title.text = self.api.api_dict_available_beds["Institution"][id]
            for hospital in self.api.api_dict_available_beds:
                self.dialog_box.ids.dialog_content.text = self.dialog_box.ids.dialog_content.text + "\n\n" + str(
                    hospital) + " : " + str(self.api.api_dict_available_beds[hospital].get(id))
            self.share_textie = self.dialog_box.ids.dialog_content.text
            self.share_callie = self.api.api_dict_available_beds["Contact Number"][id]

            print(Window.size[1])
            self.dialog = MDDialog(
                title="Address:",
                type="custom",
                content_cls=self.dialog_box,
                buttons=[
                    MDIconButton(
                        icon="phone", on_release=self.share_call
                    ),
                    MDIconButton(
                        icon="share-variant", on_release=self.share_text
                    ),
                    MDFlatButton(
                        text="Close", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                    ),
                ],
            )
            self.dialog.open()
        print("id:", id)

    def close_dialog(self, *args):
        try:
            self.dialog.dismiss()
            self.dialog = None
        except:
            print("dis")
            self.dialog = None
            pass


def starting():
    gui_start().run()


if __name__ == "__main__":
    starting()
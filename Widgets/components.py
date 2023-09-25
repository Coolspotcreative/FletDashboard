import flet
from Template.sidebar_items import menu_items
from flet import Page



class Navbar(flet.UserControl):
    def build(self):
        navbar = flet.Container(
            bgcolor='white',
            height=50,
            expand=True,
            content=flet.ResponsiveRow(
                controls=[
                    flet.Column(
                        col=10,
                        controls=[
                            flet.Container(
                                bgcolor='red',
                                expand=True,
                            ),
                        ]
                    ),
                    flet.Column(
                        col=2,
                        controls=[
                            flet.ResponsiveRow(
                                controls=[
                                    flet.Container(col=4,alignment=flet.alignment.center,margin=flet.margin.only(top=10),content=flet.Icon(
                                        flet.icons.NOTIFICATIONS,
                                        size=30,
                                        color='blue'
                                    )),
                                    flet.Container(col=4,alignment=flet.alignment.center,margin=flet.margin.only(top=10),content=flet.Icon(
                                        flet.icons.WECHAT,
                                        size=30,
                                        color='blue'
                                    )),
                                    flet.Container(col=4,alignment=flet.alignment.center,margin=flet.margin.only(top=10),content=flet.Icon(
                                        flet.icons.PERSON,
                                        size=30,
                                        color='blue',
                                    ))
                                ]
                            )
                        ]
                    )
                ]
            ),
        )
        return navbar

def on_hover(e):
    e.control.bgcolor = "blue" if e.data == "true" else "transparent"
    e.control.update()
def clicked():
    pass
class SidebarItems:
    def __init__(self, menu_items):
        self.menu_items = menu_items
    def generate_sidebar(self):
        sidebar_items = []
        first_run=True
        for item in self.menu_items:
            sidebar_item = flet.Column(
                col=12,
                spacing=0,
                expand=True,
                
                controls=[
                    flet.Container(
                        on_hover=on_hover,
                        #on_click= page.go(menu_items['url']),
                        height=75,
                        content=flet.Container(
                            padding=flet.padding.only(top=25),
                            expand=True,
                            content=flet.ResponsiveRow(
                                controls=[
                                    flet.Column(
                                        col={"sm": 12, "md": 4, "xl": 4},
                                        controls=[
                                            flet.Container(
                                                alignment=flet.alignment.center_right,
                                                content=flet.Icon(
                                                    item["icon"],
                                                    size=25,
                                                    color='white'
                                                )
                                            )
                                        ]
                                    ),
                                    flet.Column(
                                        col={"sm": 12, "md": 8, "xl": 8},
                                        controls=[
                                            flet.Container(
                                                alignment=flet.alignment.center_left,
                                                content=flet.Text(value=item["name"], size=14, color='white')
                                            )
                                        ]
                                    )
                                ]
                            )
                        )
                    ),
                ]
            )


            sidebar_items.append(sidebar_item)
            

        return sidebar_items  # Return the list of sidebar items
sidebar_generator = SidebarItems(menu_items)
generated_sidebar_items = sidebar_generator.generate_sidebar()
class Sidebar(flet.UserControl):
    def __init__(self,page):
        super().__init__()
        self.page=page
    def build(self):
        
        sidebar = flet.ResponsiveRow(
            controls=[
                # Branding top left corner
                flet.Container(
                    border=flet.border.only(right=flet.BorderSide(width=2,color='white')),
                    expand=True,
                    content=flet.Column(
                        col=12,
                        expand=True,
                        controls=[
                            # Divider under branding
                            flet.ResponsiveRow(
                                vertical_alignment=flet.CrossAxisAlignment.CENTER,
                                controls=[
                                    flet.Container(
                                        margin=flet.margin.only(top=10,bottom=50),
                                        content=flet.Icon(
                                            flet.icons.PERSON,
                                            size=50,
                                            color='white'
                                        ),
                                    )
                                    # Sidebar menu items container
                                    # Use a for loop to add generated_sidebar_items
                                ] + generated_sidebar_items  # Add the generated sidebar items directly
                            )
                        ]
                    )
                )
            ]
        )

        return sidebar
    
class ProgressRing:
    def build(slef):
        progress_ring=flet.Column(
            alignment='center',
            controls=[
                flet.Text("Indeterminate cicrular progress", style="headlineSmall",text_align='center'),
                flet.Column(
                    [flet.ProgressRing(), flet.Text("I'm going to run for ages...")],
                    horizontal_alignment=flet.CrossAxisAlignment.CENTER,
                )
            ]
        )
        return progress_ring
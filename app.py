import flet
import Style.colors
import Widgets.components
from screeninfo import get_monitors

def main(page:flet.Page):
    page.title='Magic Uploader'
    padding=page.padding=0
    border_radius=flet.border_radius.all(50)
    page.window_maximized=True
    pr = flet.ProgressRing(width=16, height=16, stroke_width = 2)
    sidebar=Widgets.components.Sidebar(page)
    page.add(
        flet.Column(
            spacing=0,
            controls=[
                flet.ResponsiveRow(
                    spacing=0,
                    controls=[
                        flet.Column(col=1.2,expand=True,controls=[
                            flet.Container(expand=True,bgcolor=flet.colors.BLUE_GREY_900,content=sidebar)
                        ],height=height),
                        flet.Column(
                            col=10.8,
                            controls=[
                                flet.ResponsiveRow(
                                    controls=[
                                        Widgets.components.Navbar()
                                    ]
                                ),
                                flet.ResponsiveRow(
                                    controls=[
                                        flet.Column(
                                            col=12,
                                            expand=True,
                                            controls=[]
                                        ),
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    )
if __name__=='__main__':
    for m in get_monitors():
        if m.is_primary:
            width=m.width
            height=m.height
    flet.app(target=main, view=flet.AppView.FLET_APP)


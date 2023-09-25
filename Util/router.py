import flet

class Router:
    def __init__(self,page,flet):
        self.page=page
        self.flet=flet
        self.routes={
            '/':'Dashboard',
            '/new_video':'New_video',
            '/video_catalog':'Video_Catalog',
            '/settings':'Settings',
            '/logout':'Logout',
            '/my_account':'My Account',
            '/support':'Support',
            '/notifications':'Notifications',
        }

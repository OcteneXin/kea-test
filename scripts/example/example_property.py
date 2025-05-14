from kea import *

class Test1(KeaTest):

    @initializer()
    def pass_welcome_pages(self):
        d(resourceId="com.android.permissioncontroller:id/permission_allow_button").click()

    @precondition(lambda self: d(resourceId="it.feio.android.omninotes.alpha:id/search_src_text").exists())
    @rule()
    def search_bar_should_exist_after_rotation(self):
        pass
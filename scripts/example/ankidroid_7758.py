from kea import *

class Test(KeaTest):
    
    # Get through Permission
    @initializer()
    def set_up(self):
        d(resourceId="com.ichi2.anki.debug:id/get_started").click()
        d(resourceId="com.ichi2.anki.debug:id/switch_widget").click()
        d(resourceId="com.android.permissioncontroller:id/permission_allow_button").click()
        d(resourceId="com.ichi2.anki.debug:id/continue_button").click()
        d.click(0.826, 0.274)

    # Add a deck
    @mainPath()
    def addDeckMainPath(self):
        d(resourceId="com.ichi2.anki.debug:id/fab_main").click()
        d(resourceId="com.ichi2.anki.debug:id/add_deck_action").click()
        d.xpath('//*[@resource-id="com.ichi2.anki.debug:id/dialog_text_input_layout"]/android.widget.FrameLayout[1]').set_text("1")
        d(resourceId="android:id/button1").click()

    # Prevent Login
    @precondition(
        lambda self: d(text="Log in to AnkiWeb").exists()
    )
    @rule()
    def card_info_should_be_translated(self):
        d(resourceId="com.ichi2.anki.debug:id/alertTitle").exists()
        d(resourceId="android:id/button2").click()
    

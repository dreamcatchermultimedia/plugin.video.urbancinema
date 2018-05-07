# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Thanks to the Authors of the base code
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# modified by: Urban Cinema
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.urbancinema'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UC7b8ilqZ96H2q1wvsXnFDHA" 	#Urban Cinema
YOUTUBE_CHANNEL_ID_2 = "UU7b8ilqZ96H2q1wvsXnFDHA" 	#Urban Cinema All


# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Urban Cinema",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://rajat.info/Urban-Cinema.jpg",
		fanart="",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Urban Cinema All",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://rajat.info/Urban-Cinema.jpg",
		fanart="https://i.ytimg.com/vi/annc05pfzm0/hqdefault.jpg",
        folder=True )


		
run()

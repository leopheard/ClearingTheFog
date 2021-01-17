from xbmcswift2 import Plugin, xbmcgui
from resources.lib import clearingthefog

plugin = Plugin()
URL = "https://clearingthefogradioshow.libsyn.com/rss"

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/6/2/3/e/623e3618da36f78a/FOG_Radio_logo_final_392x283.jpg"},
        {
            'label': plugin.get_string(30001),
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/6/2/3/e/623e3618da36f78a/FOG_Radio_logo_final_392x283.jpg"},
    ]
    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    soup = clearingthefog.get_soup(URL)
    playable_podcast1 = clearingthefog.get_playable_podcast1(soup)
    items = clearingthefog.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/all_episodes/')
def all_episodes():
    soup = clearingthefog.get_soup(URL)
    playable_podcast = clearingthefog.get_playable_podcast(soup)
    items = clearingthefog.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()

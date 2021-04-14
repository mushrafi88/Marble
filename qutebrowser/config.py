config.load_autoconfig(True)



#cookies
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')
config.set('content.cookies.accept', 'all', 'devtools://*')
config.set('content.desktop_capture', True, 'https://www.facebook.com')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version} Edg/{upstream_browser_version}', 'https://accounts.google.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')
config.set('content.images', True, 'chrome-devtools://*')
config.set('content.images', True, 'devtools://*')

# Enable JavaScript.
config.set('content.javascript.enabled', True, 'chrome-devtools://*')
config.set('content.javascript.enabled', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')
#media_Capture
config.set('content.media.audio_capture', True, 'https://www.facebook.com')
config.set('content.media.audio_video_capture', True, 'https://www.facebook.com')
config.set('content.media.video_capture', True, 'https://www.facebook.com')
#notification
config.set('content.notifications', False, 'https://kickasstorrents.to')
config.set('content.notifications', False, 'https://www.1377x.to')
config.set('content.notifications', True, 'https://www.facebook.com')
config.set('content.notifications', True, 'https://www.reddit.com')
config.set('content.notifications', True, 'https://www.upwork.com')
config.set('content.notifications', False, 'https://www.youtube.com')
config.set('content.register_protocol_handler', True, 'https://mail.google.com?extsrc=mailto&url=%25s')





#general
c.aliases = {'w': 'session-save',
             'q': 'close', 
             'qa': 'quit',
             'wq': 'quit --save', 
             'wqa': 'quit --save',
             'ge': 'open -t https://wiki.archlinux.org/index.php/Forum_Etiquette',
             'gp': 'open -t http://127.0.0.1:4000'}
c.url.default_page = 'file:///home/venerable_white/startpage-browser/index.html'
c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}',
                       'aw': 'https://wiki.archlinux.org/?search={}',
                       'aur': 'https://aur.archlinux.org/packages/?O=0&K={}',
                       'go': 'http://www.google.com/search?hl=en&source=hp&ie=ISO-8859-l&q={}',
                       'yt': 'https://www.youtube.com/results?search_query={}',
                       'gh': 'https://github.com/search?q={}&type=Code',
                       'ap': 'https://www.archlinux.org/packages/?sort=&q={}',
                       'ny': 'https://nyaa.si/?f=0&c=0_0&q={}&s=seeders&o=desc'}
c.url.start_pages = ['file:///home/venerable_white/startpage-browser/index.html']
c.new_instance_open_target = 'tab-bg'
c.session.lazy_restore = False
c.content.autoplay = False
c.content.cache.size = 52428800
c.content.blocking.enabled = True
# Valid values:
#   - auto: Use Brave's ABP-style adblocker if available, host blocking otherwise
#   - adblock: Use Brave's ABP-style adblocker
#   - hosts: Use hosts blocking
#   - both: Use both hosts blocking and Brave's ABP-style adblocker
c.content.blocking.method = 'both'

c.content.blocking.adblock.lists = [
        "https://easylist.to/easylist/easylist.txt",
        "https://easylist.to/easylist/easyprivacy.txt",
        "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt",
        "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2020.txt",
        "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/legacy.txt",
        "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt",
        "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt",
        "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt",
        "https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=1&mimetype=plaintext&_=223428",
        "https://raw.githubusercontent.com/brave/adblock-lists/master/brave-lists/brave-social.txt",
        "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt",
        "https://raw.githubusercontent.com/brave/adblock-lists/master/brave-unbreak.txt",
        "/home/venerable_white/.config/qutebrowser/blocked-hosts"]
c.content.geolocation = False
c.content.notifications = False
c.content.pdfjs = True
c.content.webgl = True
c.completion.height = '30%'
c.completion.web_history.exclude = []
c.completion.web_history.max_items = 1000
c.downloads.location.directory = '/mnt/downloads/qt/'
c.downloads.location.prompt = False
c.downloads.location.remember = True
c.downloads.open_dispatcher = None
c.downloads.remove_finished = 1000
c.completion.open_categories = ['quickmarks', 'history', 'searchengines']
c.hints.border = '1px solid #CCCCCC'
c.hints.chars = 'asdfghjkl'
c.hints.min_chars = 1
c.hints.mode = 'letter'
c.input.insert_mode.auto_load = True
c.input.partial_timeout = 4000
c.prompt.filebrowser = False
c.content.fullscreen.overlay_timeout = 4000
c.messages.timeout = 4000
c.scrolling.bar = 'overlay'
c.scrolling.smooth = False
c.statusbar.show = 'always'
c.statusbar.widgets = ['keypress', 'url', 'scroll', 'history', 'tabs', 'progress']
c.tabs.background = True
c.tabs.favicons.show = 'never'
c.tabs.new_position.related = 'last'
c.tabs.show = 'always'
c.tabs.title.format = '{index}:{current_title}'
#c.zoom.default = '125%'
c.qt.highdpi = True

#darkmode
c.colors.webpage.bg = "black"
c.colors.webpage.darkmode.algorithm = 'lightness-cielab'
c.colors.webpage.darkmode.contrast = 0.75
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.grayscale.all = True
c.colors.webpage.darkmode.grayscale.images = 0.2
c.colors.webpage.darkmode.policy.images = 'smart'
c.colors.webpage.darkmode.policy.page = 'smart'
#c.colors.webpage.darkmode.threshold.background = 0
c.colors.webpage.darkmode.threshold.text = 120




#colors
c.colors.completion.fg = '#899CA1'
c.colors.completion.category.fg = '#F2F2F2'
c.colors.completion.category.bg = '#555555'
c.colors.completion.item.selected.fg = 'white'
c.colors.completion.item.selected.bg = '#333333'
c.colors.completion.item.selected.border.top = '#333333'
c.colors.completion.item.selected.border.bottom = '#333333'
c.colors.completion.item.selected.match.fg = '#0080FF'
c.colors.completion.match.fg = '#66FFFF'
c.colors.downloads.start.fg = 'black'
c.colors.downloads.start.bg = '#BFBFBF'
c.colors.downloads.stop.fg = 'black'
c.colors.downloads.stop.bg = '#F0F0F0'
c.colors.hints.bg = '#CCCCCC'
c.colors.hints.match.fg = '#000'
c.colors.keyhint.fg = '#FFFFFF'
c.colors.keyhint.suffix.fg = '#FFFF00'
c.colors.keyhint.bg = 'rgba(0, 0, 0, 80%)'
c.colors.messages.error.bg = '#8A2F58'
c.colors.messages.error.border = '#8A2F58'
c.colors.messages.warning.bg = '#BF85CC'
c.colors.messages.warning.border = '#BF85CC'
c.colors.messages.info.bg = '#333333'
c.colors.prompts.fg = '#333333'
c.colors.prompts.bg = '#DDDDDD'
c.colors.prompts.selected.bg = '#4779B3'
c.colors.statusbar.normal.fg = '#899CA1'
c.colors.statusbar.normal.bg = '#222222'
c.colors.statusbar.insert.fg = '#899CA1'
c.colors.statusbar.insert.bg = '#222222'
c.colors.statusbar.passthrough.bg = '#4779B3'
c.colors.statusbar.command.fg = '#F0F0F0'
c.colors.statusbar.command.bg = '#555555'
c.colors.statusbar.caret.bg = '#5E468C'
c.colors.statusbar.caret.selection.fg = 'white'
c.colors.statusbar.progress.bg = '#333333'
c.colors.statusbar.url.fg = '#899CA1'
c.colors.statusbar.url.error.fg = '#8A2F58'
c.colors.statusbar.url.hover.fg = '#2B7694'
c.colors.statusbar.url.success.http.fg = '#899CA1'
c.colors.statusbar.url.success.https.fg = '#53A6A6'
c.colors.statusbar.url.warn.fg = '#914E89'
c.colors.tabs.bar.bg = '#222222'
c.colors.tabs.indicator.start = '#222222'
c.colors.tabs.indicator.stop = '#222222'
c.colors.tabs.indicator.error = '#8A2F58'
c.colors.tabs.odd.fg = '#899CA1'
c.colors.tabs.odd.bg = '#222222'
c.colors.tabs.even.fg = '#899CA1'
c.colors.tabs.even.bg = '#222222'
c.colors.tabs.selected.odd.fg = 'white'
c.colors.tabs.selected.odd.bg = '#222222'
c.colors.tabs.selected.even.fg = 'white'
c.colors.tabs.selected.even.bg = '#222222'






#fonts
c.fonts.default_family = ['Noto Sans Mono', 'DejaVu Sans Mono', 'Liberation Mono']
c.fonts.completion.entry = '8pt Noto Sans Mono'
c.fonts.completion.category = '8pt Noto Sans Mono'
c.fonts.downloads = '8pt Noto Sans Mono'
c.fonts.hints = '13px Noto Sans Mono'
c.fonts.keyhint = '10pt Noto Sans Mono'
c.fonts.messages.error = '7pt Noto Sans Mono'
c.fonts.messages.info = '7pt Noto Sans Mono'
c.fonts.messages.warning = '7pt Noto Sans Mono'
c.fonts.prompts = '8pt Noto Sans Mono'
c.fonts.statusbar = '8pt Noto Sans Mono'
c.fonts.tabs.selected = '7pt Noto Sans Mono'
c.fonts.tabs.unselected = '7pt Noto Sans Mono'






# Bindings for normal mode
config.bind('<Ctrl-Shift-a>','hint --rapid links spawn --userscript umpv {hint-url}')
config.bind(';vc', 'spawn youtube-dl -ci -f bestvideo[ext=mp4][height<1200]+bestaudio[ext=m4a]/best -o /mnt/downloads/youtube-dl/%(title)s.%(ext)s {url}')
config.bind(';vh', 'hint links spawn youtube-dl -ci -f bestvideo[ext=mp4][height<1200]+bestaudio[ext=m4a]/best -o /mnt/downloads/youtube-dl/%(title)s.%(ext)s {hint-url}')
config.bind(';nf', 'spawn firefox-beta {url}' )
config.bind('<Ctrl-Shift-d>', 'hint links spawn fdm {hint-url}')
config.bind('<Ctrl-Shift-u>', 'spawn mpv --profile=youtube {url}')
config.bind('<Ctrl-Shift-y>', 'hint links spawn mpv --profile=youtube {hint-url}')
config.bind('th', 'config-cycle tabs.show always switching')
config.bind('ah', 'config-cycle statusbar.show always never;;config-cycle tabs.show always switching')
config.bind("'", 'enter-mode jump_mark')
config.bind('+', 'zoom-in')
config.bind('-', 'zoom-out')
config.bind('.', 'repeat-command')
config.bind('/', 'set-cmd-text /')
config.bind(':', 'set-cmd-text :')
config.bind(';I', 'hint images tab')
config.bind(';O', 'hint links fill :open -t -r {hint-url}')
config.bind(';R', 'hint --rapid links window')
config.bind(';Y', 'hint links yank-primary')
config.bind(';b', 'hint all tab-bg')
config.bind(';d', 'hint links download')
config.bind(';f', 'hint all tab-fg')
config.bind(';h', 'hint all hover')
config.bind(';i', 'hint images')
config.bind(';o', 'hint links fill :open {hint-url}')
config.bind(';r', 'hint --rapid links tab-bg')
config.bind(';t', 'hint inputs')
config.bind(';y', 'hint links yank')
config.bind('<Alt-1>', 'tab-focus 1')
config.bind('<Alt-2>', 'tab-focus 2')
config.bind('<Alt-m>', 'tab-mute')
config.bind('<Ctrl-A>', 'navigate increment')
config.bind('<Ctrl-Alt-p>', 'print')
config.bind('<Ctrl-B>', 'scroll-page 0 -1')
config.bind('<Ctrl-D>', 'scroll-page 0 0.5')
config.bind('<Ctrl-F5>', 'reload -f')
config.bind('<Ctrl-F>', 'scroll-page 0 1')
config.bind('<Ctrl-N>', 'open -w')
config.bind('<Ctrl+r>', 'restart')
config.bind('b', 'back')
config.bind('t', 'set-cmd-text -s :open -t')
# Bindings for passthrough mode
config.bind('<Escape>', 'mode-leave', mode='passthrough')

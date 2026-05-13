# =============================================================================
# DotBip - Open Source BIP39 Visualizer
# =============================================================================
# A 12-bit human-readable BIP39 word visualizer for Raspberry Pi Pico 2
# with Pimoroni Display Pack 2.0
#
# Features:
# - Visual binary representation of BIP39 words
# - Multiple input methods: binary dots, keyboard, word number, wordlist
# - 12-word mnemonic grid with real-time word display
# - Compact SeedQR generation for air-gapped signing
# - Stateless operation - no persistent storage
# - Battery-free USB operation
#
# Hardware Requirements:
# - Raspberry Pi Pico 2
# - Pimoroni Pico Display Pack 2.0 (320x240 ST7789)
# - 4 buttons (A, B, X, Y)
#
# Software:
# - MicroPython
# - Pimoroni Picographics library
#
# Security Features:
# - All data stored in RAM only
# - No flash storage writes
# - Complete wipe on power-off
# - Air-gapped design
#
# Project: https://dotbip.com
# License: Open Source
# =============================================================================

BIP39_WORDLIST = """abandon ability able about above absent absorb abstract absurd abuse access accident account accuse achieve acid acoustic acquire across act action actor actress actual adapt add addict address adjust admit adult advance advice aerobic affair afford afraid again age agent agree ahead aim air airport aisle alarm album alcohol alert alien all alley allow almost alone alpha already also alter always amateur amazing among amount amused analyst anchor ancient anger angle angry animal ankle announce annual another answer antenna antique anxiety any apart apology appear apple approve april arch arctic area arena argue arm armed armor army around arrange arrest arrive arrow art artefact artist artwork ask aspect assault asset assist assume asthma athlete atom attack attend attitude attract auction audit august aunt author auto autumn average avocado avoid awake aware away awesome awful awkward axis baby bachelor bacon badge bag balance balcony ball bamboo banana banner bar barely bargain barrel base basic basket battle beach bean beauty because become beef before begin behave behind believe below belt bench benefit best betray better between beyond bicycle bid bike bind biology bird birth bitter black blade blame blanket blast bleak bless blind blood blossom blouse blue blur blush board boat body boil bomb bone bonus book boost border boring borrow boss bottom bounce box boy bracket brain brand brass brave bread breeze brick bridge brief bright bring brisk broccoli broken bronze broom brother brown brush bubble buddy budget buffalo build bulb bulk bullet bundle bunker burden burger burst bus business busy butter buyer buzz cabbage cabin cable cactus cage cake call calm camera camp can canal cancel candy cannon canoe canvas canyon capable capital captain car carbon card cargo carpet carry cart case cash casino castle casual cat catalog catch category cattle caught cause caution cave ceiling celery cement census century cereal certain chair chalk champion change chaos chapter charge chase chat cheap check cheese chef cherry chest chicken chief child chimney choice choose chronic chuckle chunk churn cigar cinnamon circle citizen city civil claim clap clarify claw clay clean clerk clever click client cliff climb clinic clip clock clog close cloth cloud clown club clump cluster clutch coach coast coconut code coffee coil coin collect color column combine come comfort comic common company concert conduct confirm congress connect consider control convince cook cool copper copy coral core corn correct cost cotton couch country couple course cousin cover coyote crack cradle craft cram crane crash crater crawl crazy cream credit creek crew cricket crime crisp critic crop cross crouch crowd crucial cruel cruise crumble crunch crush cry crystal cube culture cup cupboard curious current curtain curve cushion custom cute cycle dad damage damp dance danger daring dash daughter dawn day deal debate debris decade december decide decline decorate decrease deer defense define defy degree delay deliver demand demise denial dentist deny depart depend deposit depth deputy derive describe desert design desk despair destroy detail detect develop device devote diagram dial diamond diary dice diesel diet differ digital dignity dilemma dinner dinosaur direct dirt disagree discover disease dish dismiss disorder display distance divert divide divorce dizzy doctor document dog doll dolphin domain donate donkey donor door dose double dove draft dragon drama drastic draw dream dress drift drill drink drip drive drop drum dry duck dumb dune during dust dutch duty dwarf dynamic eager eagle early earn earth easily east easy echo ecology economy edge edit educate effort egg eight either elbow elder electric elegant element elephant elevator elite else embark embody embrace emerge emotion employ empower empty enable enact end endless endorse enemy energy enforce engage engine enhance enjoy enlist enough enrich enroll ensure enter entire entry envelope episode equal equip era erase erode erosion error erupt escape essay essence estate eternal ethics evidence evil evoke evolve exact example excess exchange excite exclude excuse execute exercise exhaust exhibit exile exist exit exotic expand expect expire explain expose express extend extra eye eyebrow fabric face faculty fade faint faith fall false fame family famous fan fancy fantasy farm fashion fat fatal father fatigue fault favorite feature february federal fee feed feel female fence festival fetch fever few fiber fiction field figure file film filter final find fine finger finish fire firm first fiscal fish fit fitness fix flag flame flash flat flavor flee flight flip float flock floor flower fluid flush fly foam focus fog foil fold follow food foot force forest forget fork fortune forum forward fossil foster found fox fragile frame frequent fresh friend fringe frog front frost frown frozen fruit fuel fun funny furnace fury future gadget gain galaxy gallery game gap garage garbage garden garlic garment gas gasp gate gather gauge gaze general genius genre gentle genuine gesture ghost giant gift giggle ginger giraffe girl give glad glance glare glass glide glimpse globe gloom glory glove glow glue goat goddess gold good goose gorilla gospel gossip govern gown grab grace grain grant grape grass gravity great green grid grief grit grocery group grow grunt guard guess guide guilt guitar gun gym habit hair half hammer hamster hand happy harbor hard harsh harvest hat have hawk hazard head health heart heavy hedgehog height hello helmet help hen hero hidden high hill hint hip hire history hobby hockey hold hole holiday hollow home honey hood hope horn horror horse hospital host hotel hour hover hub huge human humble humor hundred hungry hunt hurdle hurry hurt husband hybrid ice icon idea identify idle ignore ill illegal illness image imitate immense immune impact impose improve impulse inch include income increase index indicate indoor industry infant inflict inform inhale inherit initial inject injury inmate inner innocent input inquiry insane insect inside inspire install intact interest into invest invite involve iron island isolate issue item ivory jacket jaguar jar jazz jealous jeans jelly jewel job join joke journey joy judge juice jump jungle junior junk just kangaroo keen keep ketchup key kick kid kidney kind kingdom kiss kit kitchen kite kitten kiwi knee knife knock know lab label labor ladder lady lake lamp language laptop large later latin laugh laundry lava law lawn lawsuit layer lazy leader leaf learn leave lecture left leg legal legend leisure lemon lend length lens leopard lesson letter level liar liberty library license life lift light like limb limit link lion liquid list little live lizard load loan lobster local lock logic lonely long loop lottery loud lounge love loyal lucky luggage lumber lunar lunch luxury lyrics machine mad magic magnet maid mail main major make mammal man manage mandate mango mansion manual maple marble march margin marine market marriage mask mass master match material math matrix matter maximum maze meadow mean measure meat mechanic medal media melody melt member memory mention menu mercy merge merit merry mesh message metal method middle midnight milk million mimic mind minimum minor minute miracle mirror misery miss mistake mix mixed mixture mobile model modify mom moment monitor monkey monster month moon moral more morning mosquito mother motion motor mountain mouse move movie much muffin mule multiply muscle museum mushroom music must mutual myself mystery myth naive name napkin narrow nasty nation nature near neck need negative neglect neither nephew nerve nest net network neutral never news next nice night noble noise nominee noodle normal north nose notable note nothing notice novel now nuclear number nurse nut oak obey object oblige obscure observe obtain obvious occur ocean october odor off offer office often oil okay old olive olympic omit once one onion online only open opera opinion oppose option orange orbit orchard order ordinary organ orient original orphan ostrich other outdoor outer output outside oval oven over own owner oxygen oyster ozone pact paddle page pair palace palm panda panel panic panther paper parade parent park parrot party pass patch path patient patrol pattern pause pave payment peace peanut pear peasant pelican pen penalty pencil people pepper perfect permit person pet phone photo phrase physical piano picnic picture piece pig pigeon pill pilot pink pioneer pipe pistol pitch pizza place planet plastic plate play please pledge pluck plug plunge poem poet point polar pole police pond pony pool popular portion position possible post potato pottery poverty powder power practice praise predict prefer prepare present pretty prevent price pride primary print priority prison private prize problem process produce profit program project promote proof property prosper protect proud provide public pudding pull pulp pulse pumpkin punch pupil puppy purchase purity purpose purse push put puzzle pyramid quality quantum quarter question quick quit quiz quote rabbit raccoon race rack radar radio rail rain raise rally ramp ranch random range rapid rare rate rather raven raw razor ready real reason rebel rebuild recall receive recipe record recycle reduce reflect reform refuse region regret regular reject relax release relief rely remain remember remind remove render renew rent reopen repair repeat replace report require rescue resemble resist resource response result retire retreat return reunion reveal review reward rhythm rib ribbon rice rich ride ridge rifle right rigid ring riot ripple risk ritual rival river road roast robot robust rocket romance roof rookie room rose rotate rough round route royal rubber rude rug rule run runway rural sad saddle sadness safe sail salad salmon salon salt salute same sample sand satisfy satoshi sauce sausage save say scale scan scare scatter scene scheme school science scissors scorpion scout scrap screen script scrub sea search season seat second secret section security seed seek segment select sell seminar senior sense sentence series service session settle setup seven shadow shaft shallow share shed shell sheriff shield shift shine ship shiver shock shoe shoot shop short shoulder shove shrimp shrug shuffle shy sibling sick side siege sight sign silent silk silly silver similar simple since sing siren sister situate six size skate sketch ski skill skin skirt skull slab slam sleep slender slice slide slight slim slogan slot slow slush small smart smile smoke smooth snack snake snap sniff snow soap soccer social sock soda soft solar soldier solid solution solve someone song soon sorry sort soul sound soup source south space spare spatial spawn speak special speed spell spend sphere spice spider spike spin spirit split spoil sponsor spoon sport spot spray spread spring spy square squeeze squirrel stable stadium staff stage stairs stamp stand start state stay steak steel stem step stereo stick still sting stock stomach stone stool story stove strategy street strike strong struggle student stuff stumble style subject submit subway success such sudden suffer sugar suggest suit summer sun sunny sunset super supply supreme sure surface surge surprise surround survey suspect sustain swallow swamp swap swarm swear sweet swift swim swing switch sword symbol symptom syrup system table tackle tag tail talent talk tank tape target task taste tattoo taxi teach team tell ten tenant tennis tent term test text thank that theme then theory there they thing this thought three thrive throw thumb thunder ticket tide tiger tilt timber time tiny tip tired tissue title toast tobacco today toddler toe together toilet token tomato tomorrow tone tongue tonight tool tooth top topic topple torch tornado tortoise toss total tourist toward tower town toy track trade traffic tragic train transfer trap trash travel tray treat tree trend trial tribe trick trigger trim trip trophy trouble truck true truly trumpet trust truth try tube tuition tumble tuna tunnel turkey turn turtle twelve twenty twice twin twist two type typical ugly umbrella unable unaware uncle uncover under undo unfair unfold unhappy uniform unique unit universe unknown unlock until unusual unveil update upgrade uphold upon upper upset urban urge usage use used useful useless usual utility vacant vacuum vague valid valley valve van vanish vapor various vast vault vehicle velvet vendor venture venue verb verify version very vessel veteran viable vibrant vicious victory video view village vintage violin virtual virus visa visit visual vital vivid vocal voice void volcano volume vote voyage wage wagon wait walk wall walnut want warfare warm warrior wash wasp waste water wave way wealth weapon wear weasel weather web wedding weekend weird welcome west wet whale what wheat wheel when where whip whisper wide width wife wild will win window wine wing wink winner winter wire wisdom wise wish witness wolf woman wonder wood wool word work world worry worth wrap wreck wrestle wrist write wrong yard year yellow you young youth zebra zero zone zoo"""
BIP39_WORDS = BIP39_WORDLIST.split()

from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2
from pimoroni import Button
from time import sleep, ticks_ms
import gc

# =============================================================================
# HARDWARE SETUP
# =============================================================================

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2)
W, H = 320, 240

# Color Palette - Base colors
YELLOW = display.create_pen(255, 255, 255)
ORANGE = display.create_pen(252, 85, 51)  # Original orange
BLACK = display.create_pen(23, 29, 47)
WHITE = display.create_pen(255, 255, 255)
GREY = display.create_pen(180, 180, 180)
display.set_font("bitmap8")

# For QR we need true black/white
QR_BLACK = display.create_pen(0, 0, 0)
QR_WHITE = display.create_pen(255, 255, 255)

# =============================================================================
# COLOR SCHEME SYSTEM
# =============================================================================
# User can select from 3 color schemes on page 7/9 Settings
# The device is stateless, so color preference resets on power-off

# Available color schemes (Orange is default)
COLOR_SCHEMES = {
    'orange': {
        'bg': display.create_pen(252, 85, 51),        # Orange background (DEFAULT)
        'text': display.create_pen(23, 29, 47),       # Black text
        'selector': display.create_pen(255, 255, 255),# White selector
    },
    'white': {
        'bg': display.create_pen(255, 255, 255),      # White background
        'text': display.create_pen(23, 29, 47),       # Black text
        'selector': display.create_pen(252, 85, 51),  # Orange selector
    },
    'yellow': {
        'bg': display.create_pen(255, 235, 0),        # Yellow background
        'text': display.create_pen(23, 29, 47),       # Black text
        'selector': display.create_pen(255, 255, 255),# White selector
    },
    'pink': {
        'bg': display.create_pen(255, 105, 180),      # Pink background (Hot Pink)
        'text': display.create_pen(23, 29, 47),       # Black text
        'selector': display.create_pen(255, 255, 255),# White selector
    }
}

# Current color scheme (default is orange)
current_color_scheme = 'orange'
color_scheme_names = ['orange', 'white', 'yellow', 'pink']
color_scheme_index = 0  # Index for current scheme (orange = 0, default)

def get_bg_color():
    """Get current background color based on selected scheme"""
    return COLOR_SCHEMES[current_color_scheme]['bg']

def get_text_color():
    """Get current text color based on selected scheme"""
    return COLOR_SCHEMES[current_color_scheme]['text']

def get_selector_color():
    """Get current selector/highlight color based on selected scheme"""
    return COLOR_SCHEMES[current_color_scheme]['selector']

def set_color_scheme(scheme_name):
    """
    Change the active color scheme
    
    Args:
        scheme_name: One of 'white', 'black', 'blue', 'yellow', 'orange'
    """
    global current_color_scheme, color_scheme_index
    if scheme_name in COLOR_SCHEMES:
        current_color_scheme = scheme_name
        color_scheme_index = color_scheme_names.index(scheme_name)
QR_WHITE = display.create_pen(255, 255, 255)

# Display Pack 2.0 buttons
button_a = Button(12)  # A = Previous/Left
button_b = Button(13)  # B = Page Turner
button_x = Button(14)  # X = Next/Right
button_y = Button(15)  # Y = Confirm/Enter

# =============================================================================
# KEYBOARD LAYOUTS
# =============================================================================

ROW1 = list("QWERTYUIOP")
ROW2 = list("ASDFGHJKL")
ROW3 = list("ZXCVBNM")

# =============================================================================
# STATE VARIABLES
# =============================================================================

# Binary representation (12 bits for BIP39 word values 1-2048)
BIT_VALUES = [1 << i for i in range(11, -1, -1)]  # [2048, 1024, 512, ..., 2, 1]
BIT_VALUES_11 = [1 << i for i in range(10, -1, -1)]  # For 11-bit operations
bits = [False] * 12  # Current binary state
selected = 11  # Current selected bit (0-11) - start at rightmost (box 12)
page = 1  # Current page number
NUM_PAGES = 9  # Total number of pages

# 12x12 Grid for 12-word mnemonic (each row is one word)
# NOW EXPANDED: 24x12 grid for 24-word mnemonic support
grid_bits = [[False for _ in range(12)] for _ in range(24)]  # 24 rows for 24 words
grid_selected_row = 0
grid_selected_col = 0
grid_mask_on = False  # Mask mode for viewing grid without distractions
grid_page = 1  # Current grid page: 1 (words 1-12) or 2 (words 13-24)

# Word input state
word_buffer = ""
MAX_WORD_LEN = 10
suggestion_active = False
suggestion_word = ""
num_buffer = ""
num_error = ""  # Error message for invalid number input
wordlist_index = 0
wordlist_last_press = 0

# Save mode state (page 1/9 - Binary Dots)
save_selected_index = -1  # -1=normal mode, 0-11=selecting word position
save_word_position = None  # Which word position was confirmed
save_confirmed_msg = False  # Show "Saved!" message

# QR zoom mode state (page 6/9 - Compact SeedQR)
qr_zoom_mode = False  # Toggle for QR-only display mode
qr_zoom_brightness = 1.0  # Brightness in zoom mode (0.1 to 1.0)

# Button debouncing
DEBOUNCE_MS = 120
_last = 0

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def is_pressed(btn):
    """
    Debounced button press detection.
    
    Args:
        btn: Button object to check
        
    Returns:
        True if button was pressed (with debouncing), False otherwise
    """
    global _last
    now = ticks_ms()
    if btn.read() and now - _last > DEBOUNCE_MS:
        _last = now
        return True
    return False

def clamp_value(v):
    """Clamp value to valid BIP39 word range (1-2048)"""
    if v <= 0: return 0
    if v >= 2048: return 2048
    return v

def current_value():
    """Calculate current word value from binary representation"""
    return clamp_value(sum(BIT_VALUES[i] for i, b in enumerate(bits) if b))

def is_word_position_filled(word_index):
    """Check if a word position (0-23) has been filled with data"""
    if 0 <= word_index < 24:
        # Check if any bit is set in this word's row in grid_bits
        return any(grid_bits[word_index])
    return False

def get_word_for_value(val):
    """
    Get BIP39 word for a given value.
    
    Args:
        val: Word number (1-2048)
        
    Returns:
        BIP39 word string, or empty string if invalid
    """
    if val <= 0: return ""
    if val >= 2048: return "zoo"
    idx = val - 1
    if 0 <= idx < len(BIP39_WORDS):
        return BIP39_WORDS[idx]
    return ""

def load_word_number_to_bits(word_num):
    """
    Load a word number into the binary representation.
    
    Args:
        word_num: BIP39 word number (1-2048)
    """
    global bits
    if word_num <= 0 or word_num > 2048:
        return
    
    # Decompose word number into bit values
    bits = [False] * 12
    remaining = word_num
    for i, bit_value in enumerate(BIT_VALUES):
        if remaining >= bit_value:
            bits[i] = True
            remaining -= bit_value

def set_bits_from_value(val):
    global bits
    if val <= 0:
        bits = [False]*12
        return
    v = min(val, 2048)
    if v == 2048:
        bits = [False]*12
        bits[0] = True
        return
    rem = v
    b = []
    for bit in BIT_VALUES:
        if rem >= bit:
            b.append(True)
            rem -= bit
        else:
            b.append(False)
    bits = b

def toggle_bit(idx):
    """
    Toggle a bit in the binary representation with special rules.
    
    Special behavior:
    - Bit 0 (2048/zoo): Setting it clears all other bits
    - Other bits: Cannot be set if bit 0 is set
    
    Args:
        idx: Bit index to toggle (0-11)
    """
    global bits
    if idx < 0 or idx >= 12: return
    v = BIT_VALUES[idx]
    if v == 2048:
        # Toggling bit 0 (2048)
        if not bits[idx]:
            bits = [False]*12
            bits[idx] = True
        else:
            bits[idx] = False
    else:
        # Toggling other bits - clear bit 0 first if set
        if bits[0]:
            bits[0] = False
        bits[idx] = not bits[idx]

def build_key_list():
    keys = []
    for c, ch in enumerate(ROW1):
        keys.append({'label': ch, 'row': 0, 'col': c, 'type': 'key'})
    keys.append({'label': 'BACK', 'row': 0, 'col': len(ROW1), 'type': 'back'})
    for c, ch in enumerate(ROW2):
        keys.append({'label': ch, 'row': 1, 'col': c, 'type': 'key'})
    for c, ch in enumerate(ROW3):
        keys.append({'label': ch, 'row': 2, 'col': c, 'type': 'key'})
    keys.append({'label': 'ENTER', 'row': 1, 'col': len(ROW2), 'type': 'enter'})
    return keys

def build_num_list():
    keys = []
    numbers = ['1','2','3','4','5','6','7','8','9']
    for i, n in enumerate(numbers):
        r = i // 3
        c = i % 3
        keys.append({'label': n, 'row': r, 'col': c, 'type': 'num'})
    keys.append({'label': 'BACK', 'row': 3, 'col': 0, 'type': 'back'})
    keys.append({'label': '0', 'row': 3, 'col': 1, 'type': 'num'})
    keys.append({'label': 'ENTER', 'row': 3, 'col': 2, 'type': 'enter'})
    return keys

KEY_BUTTONS = build_key_list()
NUM_BUTTONS = build_num_list()
kbd_index = 0
num_index = 0

# =============================================================================
# UI HELPER FUNCTIONS
# =============================================================================

def recalc_suggestion():
    """Recalculate word suggestion based on current input buffer"""
    global suggestion_active, suggestion_word
    suggestion_active = False
    suggestion_word = ""
    if len(word_buffer) == 0:
        return
    pref = word_buffer.lower()
    matches = []
    for w in BIP39_WORDS:
        if w.startswith(pref):
            matches.append(w)
            if len(matches) > 1:
                break
    if len(matches) == 1:
        suggestion_active = True
        suggestion_word = matches[0]

def keyboard_geometry(y_offset=-6):
    """Calculate keyboard layout geometry with optional Y offset"""
    kb_height = 120
    kb_y = H - kb_height + y_offset  # Adjustable Y position
    usable_w = int(W * 0.99)
    cols = max(len(ROW1) + 1, len(ROW2) + 1, len(ROW3))
    btn_size = usable_w // cols
    total_w = btn_size * cols
    x0 = (W - total_w) // 2
    return {'x': x0, 'y': kb_y, 'btn': btn_size, 'cols': cols}

def draw_page_header(title):
    """Draw standard page header with themed background"""
    display.set_pen(get_bg_color())
    display.clear()
    display.set_pen(get_text_color())
    display.text(title, 10, 10, W - 10, 3)

# =============================================================================
# PAGE DRAWING FUNCTIONS
# =============================================================================

# =============================================================================
# COLOR SCHEME PATTERN DOCUMENTATION
# =============================================================================
# This page demonstrates how to use the color scheme system.
# Apply this pattern to other pages:
#
# 1. Background: Use get_bg_color() for page backgrounds
# 2. Text: Use get_text_color() for all text elements
# 3. Selector/Highlight: Use get_selector_color() for selected elements
# 4. Borders: Generally use BLACK for consistency, or get_text_color() for themed borders
# 5. QR Codes: Always use QR_BLACK and QR_WHITE (never themed colors)
# 6. Warning Banners: Use BLACK background with WHITE text (always)
#
# Example replacements:
#   display.set_pen(ORANGE) → display.set_pen(get_bg_color())
#   display.set_pen(BLACK) for text → display.set_pen(get_text_color())
#   display.set_pen(WHITE) for selector → display.set_pen(get_selector_color())
# =============================================================================

def draw_page1():
    """
    Page 1/9: Binary Dots
    Visual binary input with 12 colored squares representing bit values.
    Users toggle dots to build word values, then save to the 24-word grid.
    
    COLOR SCHEME AWARE:
    - Background uses themed color
    - Text uses themed text color
    - Selector uses themed selector color
    """
    draw_page_header("1/9 Binary Dots")
    usable_w = int(W * 0.90)
    x_left = (W - usable_w) // 2
    square_size = usable_w // 12
    if square_size < 8: square_size = 8
    total_row_w = square_size * 12
    x_left += (usable_w - total_row_w) // 2
    BORDER_THICK = 2
    y_center = 90
    y0 = y_center - square_size // 2
    
    # =============================================================================
    # BINARY DOTS (12 squares representing bit values)
    # =============================================================================
    for i in range(12):
        cx = x_left + i * square_size + square_size // 2
        x = x_left + i * square_size
        y = y0
        
        # Draw border (always use themed text color for borders)
        display.set_pen(get_text_color())
        for t in range(BORDER_THICK):
            display.rectangle(x - t, y - t, square_size + 2*t, square_size + 2*t)
        
        # Determine if this is the selected bit (not in save mode)
        is_selected = (i == selected and selected < 12 and save_selected_index == -1)
        
        # Fill box: themed selector color if selected, background color if not
        if is_selected:
            display.set_pen(get_selector_color())
        else:
            display.set_pen(get_bg_color())
        inner_inset = BORDER_THICK
        inner_w = square_size - inner_inset * 2
        if inner_w > 0:
            display.rectangle(x + inner_inset, y + inner_inset, inner_w, inner_w)
        
        # Draw dot if bit is set (use themed text color)
        if bits[i]:
            dot_r = max(2, inner_w // 6)
            display.set_pen(get_text_color())
            display.circle(cx, y_center, dot_r)
        
        # Draw number above box
        # Use BLACK if this box is selected (for readability on white/light selector)
        # Otherwise use themed text color
        val = BIT_VALUES[i]
        val_str = str(val)
        if is_selected:
            display.set_pen(BLACK)  # Black numbers on selected (white) box
        else:
            display.set_pen(get_text_color())  # Themed color for non-selected
        char_height = 8
        total_height = len(val_str) * char_height
        start_y = y - total_height - 2
        for char_idx, char in enumerate(val_str):
            char_x = cx - 3
            char_y = start_y + (char_idx * char_height)
            display.text(char, char_x, char_y, square_size, 1)
    
    # =============================================================================
    # WORD INFO AND SAVE PANEL (only show if value > 0)
    # =============================================================================
    val = current_value()
    if val > 0:
        # TWO COLUMN LAYOUT - Left: calculation/word, Right: save panel
        left_col_x = 10
        right_col_x = 170
        content_y = 130
        
        # LEFT COLUMN - Word info (use themed text color)
        parts = [str(BIT_VALUES[i]) for i in range(12) if bits[i]]
        calc = " + ".join(parts) + " = " + str(val)
        display.set_pen(get_text_color())
        display.text(calc, left_col_x, content_y, 150, 1)
        word = get_word_for_value(val)
        display.text(word, left_col_x, content_y + 20, 150, 2)
        display.text(str(val), left_col_x, content_y + 40, 150, 2)
        
        # RIGHT COLUMN - Save panel
        panel_x = right_col_x
        panel_y = content_y
        
        display.set_pen(get_text_color())
        display.text("Save as word:", panel_x, panel_y, 150, 1)
        
        # Draw word number buttons (1-24) in 4 rows of 6
        btn_size = 18
        btn_spacing = 4
        
        for i in range(24):
            row = i // 6
            col = i % 6
            btn_x = panel_x + col * (btn_size + btn_spacing)
            btn_y = panel_y + 12 + row * (btn_size + btn_spacing)
            
            # Check if this position has been filled
            is_filled = is_word_position_filled(i)
            
            # Determine colors based on selection state and filled status
            if save_selected_index == i:
                # Selected: themed selector with themed text border
                display.set_pen(get_text_color())
                display.rectangle(btn_x, btn_y, btn_size, btn_size)
                display.set_pen(get_selector_color())
                display.rectangle(btn_x + 2, btn_y + 2, btn_size - 4, btn_size - 4)
                # Use black numbers on selected (white/light) background
                num_color = BLACK
            elif is_filled:
                # Filled position: WHITE/EMPTY button with BLACK number (inverted)
                display.set_pen(get_text_color())  # Black border
                display.rectangle(btn_x, btn_y, btn_size, btn_size)
                display.set_pen(get_bg_color())  # Fill with background color (empty look)
                display.rectangle(btn_x + 2, btn_y + 2, btn_size - 4, btn_size - 4)
                # Black number on empty background
                num_color = BLACK
            else:
                # Not selected and not filled: themed text color square (original style)
                display.set_pen(get_text_color())
                display.rectangle(btn_x, btn_y, btn_size, btn_size)
                # Use white numbers on dark background
                num_color = WHITE
            
            # Draw number with appropriate color
            display.set_pen(num_color)
            num_text = str(i + 1)
            # Add 3px left margin to the text
            text_x = btn_x + ((btn_size - len(num_text) * 8) // 2) + 3
            text_y = btn_y + 5
            display.text(num_text, text_x, text_y, btn_size, 1)
        
        # Show "Saved" message in top-right corner
        if save_confirmed_msg:
            display.set_pen(get_text_color())
            display.text("Saved", W - 55, 10, 50, 2)
    
    display.update()

def draw_page2():
    global suggestion_active, suggestion_word
    draw_page_header("2/9 Word")
    typed_y = 40
    
    # Center the typed word - calculate center based on current length
    typed_text = word_buffer.lower()
    if len(typed_text) > 0:
        # Simple centering: character width at scale 3
        # Testing assumption: 6 pixels per char at base, so scale 3 = 18 pixels
        char_width = 6 * 3
        text_width = len(typed_text) * char_width
        text_x = (W - text_width) // 2
        display.set_pen(get_text_color())
        display.text(typed_text, text_x, typed_y, W - text_x, 3)
    
    # Center the suggestion and confirmation message
    if suggestion_active and suggestion_word:
        # Center the suggestion word - scale 2
        char_width = 6 * 2
        text_width = len(suggestion_word) * char_width
        text_x = (W - text_width) // 2
        display.set_pen(get_text_color())
        display.text(suggestion_word, text_x, typed_y + 28, W - text_x, 2)
        
        # Center "(Enter to confirm)" below the suggestion - scale 2
        confirm_text = "(Enter to confirm)"
        confirm_char_width = 5 * 2  # Use 5*2=10 like error message for better centering
        confirm_width = len(confirm_text) * confirm_char_width
        confirm_x = (W - confirm_width) // 2
        display.text(confirm_text, confirm_x, typed_y + 50, W - confirm_x, 2)
    elif len(word_buffer) > 0:
        pref = word_buffer.lower()
        matches = 0
        for w in BIP39_WORDS:
            if w.startswith(pref):
                matches += 1
                break
        if matches == 0:
            # Center error message - 2 lines, scale 2, same position as suggestion
            display.set_pen(get_text_color())
            
            # Line 1: "This word does not exist"
            line1 = "This word does not exist"
            char_width = 5 * 2  # scale 2, trying 5px base (smaller than 6 or 8)
            line1_width = len(line1) * char_width
            line1_x = (W - line1_width) // 2
            display.text(line1, line1_x, typed_y + 28, W - line1_x, 2)
            
            # Line 2: "in the BIP39 wordlist"
            line2 = "in the BIP39 wordlist"
            line2_width = len(line2) * char_width
            line2_x = (W - line2_width) // 2
            display.text(line2, line2_x, typed_y + 46, W - line2_x, 2)  # 18 pixels below line 1 (more spacing)
    
    geo = keyboard_geometry(y_offset=1)
    bx, by, bs = geo['x'], geo['y'], geo['btn']
    offset1, offset2, offset3 = 0, bs // 2, bs
    
    for idx, k in enumerate(KEY_BUTTONS):
        r, c = k['row'], k['col']
        if k['type'] == 'enter':
            back_x = bx + len(ROW1) * bs + offset1
            ex, ey, ew, eh = back_x - 1, by + bs, bs + 6, bs * 2 - 4
            display.set_pen(get_text_color())
            display.rectangle(ex, ey, ew, eh)
            display.set_pen(YELLOW)
            display.text("ENTER", ex + 6, ey + (eh - 8) // 2, ew, 1)
            k['x'], k['y'], k['w'], k['h'] = ex, ey, ew, eh
            continue
        if r == 0: rx, ry = bx + c * bs + offset1, by
        elif r == 1: rx, ry = bx + c * bs + offset2, by + bs
        else: rx, ry = bx + c * bs + offset3, by + bs * 2
        bw, bh = bs - 5, bs - 5
        display.set_pen(get_text_color())
        display.rectangle(rx + 3, ry + 3, bw, bh)
        display.set_pen(YELLOW)
        label = k['label']
        if len(label) == 1:
            display.text(label, rx + 10, ry + 8, bw, 2)
        else:
            bw_back = bs + 2
            display.set_pen(BLACK)
            display.rectangle(rx + 3, ry + 3, bw_back, bh)
            display.set_pen(YELLOW)
            display.text(label, rx + 9, ry + 3 + (bh - 8) // 2, bw_back, 1)
            bw = bw_back
        k['x'], k['y'], k['w'], k['h'] = rx + 3, ry + 3, bw, bh
    sel = KEY_BUTTONS[kbd_index]
    sx, sy, sw, sh = sel['x'], sel['y'], sel['w'], sel['h']
    display.set_pen(YELLOW)
    display.rectangle(sx, sy, sw, sh)
    display.set_pen(BLACK)
    display.rectangle(sx, sy, sw, 3)
    display.rectangle(sx, sy + sh - 3, sw, 3)
    display.rectangle(sx, sy, 3, sh)
    display.rectangle(sx + sw - 3, sy, 3, sh)
    label = sel['label']
    if len(label) == 1:
        display.text(label, sx + 7, sy + 5, sw, 2)
    else:
        display.text(label, sx + 6, sy + (sh - 8) // 2, sw, 1)
    display.update()

def draw_page3():
    draw_page_header("3/9 Word Number")
    typed_y = 58  # 30 pixels spacing from header (header ends ~28, 28+30=58)
    
    # Center the typed number - scale 3
    if len(num_buffer) > 0:
        char_width = 6 * 3
        text_width = len(num_buffer) * char_width
        text_x = (W - text_width) // 2
        display.set_pen(get_text_color())
        display.text(num_buffer, text_x, typed_y, W - text_x, 3)
    
    # Center the error message if present - scale 1
    if num_error:
        char_width = 6 * 1
        text_width = len(num_error) * char_width
        text_x = (W - text_width) // 2
        display.set_pen(get_text_color())
        display.text(num_error, text_x, typed_y + 30, W - text_x, 1)
    
    geo = keyboard_geometry()
    bx, by, bs = geo['x'], geo['y'], geo['btn']
    cols, total_w = 3, bs * 3
    start_x = (W - total_w) // 2
    for idx, k in enumerate(NUM_BUTTONS):
        r, c = k['row'], k['col']
        rx = start_x + c * bs - 4 if k['type'] == 'back' else start_x + c * bs
        ry = by + r * bs
        bw = bs + 6 if k['type'] == 'enter' else (bs + 2 if k['type'] == 'back' else bs - 6)
        bh = bs - 6
        display.set_pen(get_text_color())
        display.rectangle(rx + 3, ry + 3, bw, bh)
        display.set_pen(YELLOW)
        display.text(k['label'], rx + 9, ry + 7, bw, 2 if len(k['label'])==1 else 1)
        k['x'], k['y'], k['w'], k['h'] = rx + 3, ry + 3, bw, bh
    sel = NUM_BUTTONS[num_index]
    sx, sy, sw, sh = sel['x'], sel['y'], sel['w'], sel['h']
    display.set_pen(YELLOW)
    display.rectangle(sx, sy, sw, sh)
    display.set_pen(get_text_color())
    display.rectangle(sx, sy, sw, 3)
    display.rectangle(sx, sy+sh-3, sw, 3)
    display.rectangle(sx, sy, 3, sh)
    display.rectangle(sx+sw-3, sy, 3, sh)
    display.text(sel['label'], sx+6, sy+4, sw, 2 if len(sel['label'])==1 else 1)
    display.update()

def draw_page4():
    global grid_mask_on
    grid_size = 14
    grid_start_x = (W - (grid_size * 12)) // 2 - 20
    grid_start_y = 45
    
    if grid_mask_on:
        display.set_pen(get_text_color())
        display.clear()
        mask_margin, corner_radius = 10, 3
        ox, oy = grid_start_x - mask_margin, grid_start_y - mask_margin
        ow, oh = (grid_size * 12) + (mask_margin * 2), (grid_size * 12) + (mask_margin * 2)
        display.set_pen(GREY)
        display.rectangle(ox + corner_radius, oy, ow - corner_radius * 2, oh)
        display.rectangle(ox, oy + corner_radius, ow, oh - corner_radius * 2)
        display.circle(ox + corner_radius, oy + corner_radius, corner_radius)
        display.circle(ox + ow - corner_radius - 1, oy + corner_radius, corner_radius)
        display.circle(ox + corner_radius, oy + oh - corner_radius - 1, corner_radius)
        display.circle(ox + ow - corner_radius - 1, oy + oh - corner_radius - 1, corner_radius)
        # Calculate row offset based on grid page
        row_offset = (grid_page - 1) * 12
        for display_row in range(12):
            actual_row = row_offset + display_row
            for col in range(12):
                x, y = grid_start_x + col * grid_size, grid_start_y + display_row * grid_size
                display.set_pen(GREY)
                display.rectangle(x, y, grid_size, grid_size)
                display.set_pen(get_text_color())
                display.rectangle(x, y, grid_size, 2)
                display.rectangle(x, y, 2, grid_size)
                if grid_bits[actual_row][col]:
                    display.circle(x + grid_size // 2, y + grid_size // 2, grid_size // 2 - 1)
        display.set_pen(get_text_color())
        display.rectangle(grid_start_x + 12 * grid_size - 1, grid_start_y, 2, 12 * grid_size)
        display.rectangle(grid_start_x, grid_start_y + 12 * grid_size - 1, 12 * grid_size, 2)
        display.set_pen(get_selector_color())
        display.rectangle(W - 20, 5, 15, 15)
        display.update()
        return

    display.set_pen(get_bg_color())
    display.clear()
    display.set_pen(get_text_color())
    display.text("5/9 Binary Grid", 10, 10, W - 10, 3)
    
    # TWO INDICATOR SQUARES for grid pages (left=page 2, right=page 1)
    toggle_size = 15
    toggle_spacing = 4
    toggle_y = 5
    # Right square (page 1)
    toggle_right_x = W - 25
    # Left square (page 2)
    toggle_left_x = toggle_right_x - toggle_size - toggle_spacing
    
    # Check if words exist on each page
    page1_has_words = any(grid_bits[row][col] for row in range(12) for col in range(12))
    page2_has_words = any(grid_bits[row][col] for row in range(12, 24) for col in range(12))
    
    # Draw left square (page 2 indicator)
    if grid_selected_row == 0 and grid_selected_col == -4:
        # Selected
        display.set_pen(get_selector_color())
        display.rectangle(toggle_left_x, toggle_y, toggle_size, toggle_size)
        display.set_pen(get_text_color())
        display.rectangle(toggle_left_x, toggle_y, toggle_size, 1)
        display.rectangle(toggle_left_x, toggle_y + toggle_size - 1, toggle_size, 1)
        display.rectangle(toggle_left_x, toggle_y, 1, toggle_size)
        display.rectangle(toggle_left_x + toggle_size - 1, toggle_y, 1, toggle_size)
    else:
        # Not selected
        display.set_pen(get_text_color())
        display.rectangle(toggle_left_x, toggle_y, toggle_size, toggle_size)
        display.set_pen(get_bg_color())
        display.rectangle(toggle_left_x + 2, toggle_y + 2, toggle_size - 4, toggle_size - 4)
    # Draw dot if page 2 has words
    if page2_has_words:
        dot_size = 4  # Increased from 3 to 4
        dot_x = toggle_left_x + (toggle_size - dot_size) // 2
        dot_y = toggle_y + (toggle_size - dot_size) // 2
        display.set_pen(get_text_color())
        display.circle(dot_x + dot_size // 2, dot_y + dot_size // 2, dot_size // 2)
    
    # Draw right square (page 1 indicator) 
    if grid_selected_row == 0 and grid_selected_col == -3:
        # Selected
        display.set_pen(get_selector_color())
        display.rectangle(toggle_right_x, toggle_y, toggle_size, toggle_size)
        display.set_pen(get_text_color())
        display.rectangle(toggle_right_x, toggle_y, toggle_size, 1)
        display.rectangle(toggle_right_x, toggle_y + toggle_size - 1, toggle_size, 1)
        display.rectangle(toggle_right_x, toggle_y, 1, toggle_size)
        display.rectangle(toggle_right_x + toggle_size - 1, toggle_y, 1, toggle_size)
    else:
        # Not selected
        display.set_pen(get_text_color())
        display.rectangle(toggle_right_x, toggle_y, toggle_size, toggle_size)
        display.set_pen(get_bg_color())
        display.rectangle(toggle_right_x + 2, toggle_y + 2, toggle_size - 4, toggle_size - 4)
    # Draw dot if page 1 has words
    if page1_has_words:
        dot_size = 4  # Increased from 3 to 4
        dot_x = toggle_right_x + (toggle_size - dot_size) // 2
        dot_y = toggle_y + (toggle_size - dot_size) // 2
        display.set_pen(get_text_color())
        display.circle(dot_x + dot_size // 2, dot_y + dot_size // 2, dot_size // 2)
    
    # Draw page indicator text below squares
    display.set_pen(get_text_color())
    page_text = f"Page {grid_page}"
    display.text(page_text, toggle_left_x, toggle_y + toggle_size + 2, 50, 1)

    # "Clear" button at bottom-left corner
    clear_x = 5
    clear_y = grid_start_y + 11 * grid_size + 3 + 15  # Bottom row position + 15px lower
    clear_text = "Clear"
    clear_width = len(clear_text) * 8  # 8 pixels per character at scale 1
    
    # Draw selection rectangle if selected (35% narrower to fit just the word)
    if grid_selected_row == 11 and grid_selected_col == -2:
        display.set_pen(get_selector_color())
        highlight_width = int((clear_width + 4) * 0.65)  # 35% narrower
        display.rectangle(clear_x, clear_y - 3, highlight_width, 14)
    
    # Draw "Clear" text
    display.set_pen(get_text_color())
    display.text(clear_text, clear_x + 2, clear_y, clear_width, 1)
    
    # Calculate row offset based on grid page
    row_offset = (grid_page - 1) * 12  # Page 1: rows 0-11, Page 2: rows 12-23
    
    for display_row in range(12):
        actual_row = row_offset + display_row
        for col in range(12):
            x, y = grid_start_x + col * grid_size, grid_start_y + display_row * grid_size
            display.set_pen(get_bg_color())
            display.rectangle(x, y, grid_size, grid_size)
            display.set_pen(get_text_color())
            display.rectangle(x, y, grid_size, 1)
            display.rectangle(x, y, 1, grid_size)
            if grid_bits[actual_row][col]:
                # Draw dot with themed text color
                # (Selected cell dot will be redrawn in black after selector)
                dot_radius = grid_size // 2 - 2
                dot_center_x = x + grid_size // 2
                dot_center_y = y + grid_size // 2
                display.set_pen(get_text_color())
                display.circle(dot_center_x, dot_center_y, dot_radius)
    display.set_pen(get_text_color())
    display.rectangle(grid_start_x + 12 * grid_size, grid_start_y, 1, 12 * grid_size)
    display.rectangle(grid_start_x, grid_start_y + 12 * grid_size, 12 * grid_size, 1)
    
    # Draw thicker vertical dividers at columns 4 and 8 (5th and 9th lines)
    # This creates visual grouping: 4 cols | 4 cols | 4 cols
    display.rectangle(grid_start_x + 4 * grid_size, grid_start_y, 2, 12 * grid_size)  # After column 4
    display.rectangle(grid_start_x + 8 * grid_size, grid_start_y, 2, 12 * grid_size)  # After column 8
    
    # Draw thicker horizontal dividers at rows 4 and 8 (5th and 9th lines)
    # This creates visual grouping: 4 rows | 4 rows | 4 rows
    display.rectangle(grid_start_x, grid_start_y + 4 * grid_size, 12 * grid_size, 2)  # After row 4
    display.rectangle(grid_start_x, grid_start_y + 8 * grid_size, 12 * grid_size, 2)  # After row 8
    
    # Draw word numbers on the left side of the grid (adjusted for current page)
    word_num_x = grid_start_x - 20
    for display_row in range(12):
        word_num = row_offset + display_row + 1  # Word 1-12 for page 1, 13-24 for page 2
        word_num_y = grid_start_y + display_row * grid_size + 3
        display.set_pen(get_text_color())
        display.text(str(word_num), word_num_x, word_num_y, 20, 1)
    
    # Draw words on the right side of the grid
    word_x = grid_start_x + 12 * grid_size + 5
    for display_row in range(12):
        actual_row = row_offset + display_row
        row_value = sum(BIT_VALUES[col] for col in range(12) if grid_bits[actual_row][col])
        if row_value > 0:
            word = get_word_for_value(row_value)
            display.set_pen(get_text_color())
            display.text(word, word_x, grid_start_y + display_row * grid_size, 100, 2)
    
    # Selector with 1px offset to stay within grid borders
    # Note: Clear button has its own wider selection rectangle drawn earlier
    if 0 <= grid_selected_row < 12 and 0 <= grid_selected_col < 12:
        display.set_pen(get_selector_color())
        display.rectangle(grid_start_x + grid_selected_col * grid_size + 1,
                         grid_start_y + grid_selected_row * grid_size + 1,
                         grid_size - 1, grid_size - 1)
        
        # If selected cell has a dot, redraw it in BLACK on top of white selector
        actual_selected_row = row_offset + grid_selected_row
        if grid_bits[actual_selected_row][grid_selected_col]:
            dot_radius = grid_size // 2 - 2
            dot_center_x = grid_start_x + grid_selected_col * grid_size + grid_size // 2
            dot_center_y = grid_start_y + grid_selected_row * grid_size + grid_size // 2
            display.set_pen(BLACK)
            display.circle(dot_center_x, dot_center_y, dot_radius)
    
    display.update()

def draw_page5():
    draw_page_header("8/9 Project DotBip")
    display.set_pen(get_text_color())
    
    # More margin between header and first paragraph
    start_y = 50
    
    display.text("DotBip: Open-source 12-bit (11-bit index) BIP39", 10, start_y, W - 10, 1)
    display.text("visualizer for RP Pico 2. Decipher steel-stamped", 10, start_y + 12, W - 10, 1)
    display.text("backups (KeyTag, NanoSeed, TinySeed) or encode", 10, start_y + 24, W - 10, 1)
    display.text("words/numbers to binary grids. Generates Compact", 10, start_y + 36, W - 10, 1)
    display.text("SeedQR for 12/24-word phrases. Compatible with", 10, start_y + 48, W - 10, 1)
    display.text("Krux/SeedSigner/Jade. Stateless, air-gapped,", 10, start_y + 60, W - 10, 1)
    display.text("RAM-only. Power off = complete wipe. Please find", 10, start_y + 72, W - 10, 1)
    display.text("the latest code and more information on our", 10, start_y + 84, W - 10, 1)
    display.text("Github page.", 10, start_y + 96, W - 10, 1)
    
    display.text("github.com/DotBip/Pico2", 10, start_y + 120, W - 10, 2)
    display.update()

def draw_page_wordlist():
    draw_page_header("4/9 BIP39 Wordlist")
    
    # Get current word (wordlist_index is 0-2047)
    word_num = wordlist_index + 1
    word = BIP39_WORDS[wordlist_index]
    
    # Build the display text
    word_text = f"{word_num}. {word}"
    
    # Calculate center position - scale 2
    char_width = 6 * 2
    text_width = len(word_text) * char_width
    text_x = (W - text_width) // 2
    text_y = 100
    
    display.set_pen(get_text_color())
    
    # Draw centered word and number
    display.text(word_text, text_x, text_y, W - text_x, 2)
    
    # Draw < arrow on left edge - white text on black box
    arrow_box_w = 20
    arrow_box_h = 20
    arrow_y = text_y - 2
    
    # Left arrow box
    display.set_pen(get_text_color())
    display.rectangle(5, arrow_y, arrow_box_w, arrow_box_h)
    display.set_pen(WHITE)
    display.text("<", 8, text_y, arrow_box_w, 2)
    
    # Right arrow box
    display.set_pen(get_text_color())
    display.rectangle(W - 25, arrow_y, arrow_box_w, arrow_box_h)
    display.set_pen(WHITE)
    display.text(">", W - 20, text_y, arrow_box_w, 2)
    
    display.update()

def draw_page6():
    """
    Page 7/9: Settings
    Allows user to select color scheme and view navigation/security info
    """
    draw_page_header("7/9 Settings")
    display.set_pen(get_text_color())
    
    # =========================================================================
    # COLOR SCHEME SELECTION
    # =========================================================================
    
    display.text("UI COLOR SCHEMES", 10, 40, W - 20, 1)
    
    # Draw 4 color scheme boxes (Orange, White, Yellow, Pink)
    box_size = 30
    box_spacing = 12
    box_y = 55
    start_x = 10  # Left-aligned with text
    
    # Define colors for the 4 schemes (in order: Orange, White, Yellow, Pink)
    scheme_colors = [
        display.create_pen(252, 85, 51),    # Orange (default)
        display.create_pen(255, 255, 255),  # White
        display.create_pen(255, 235, 0),    # Yellow
        display.create_pen(255, 105, 180),  # Pink (Hot Pink)
    ]
    
    for i in range(4):
        box_x = start_x + i * (box_size + box_spacing)
        
        # Selected scheme: 2px stroke around the color square
        # Non-selected: No stroke, just the color square
        if i == color_scheme_index:
            # Draw 2px border for selected scheme
            display.set_pen(get_text_color())
            display.rectangle(box_x - 2, box_y - 2, box_size + 4, box_size + 4)
        
        # Draw the colored square
        display.set_pen(scheme_colors[i])
        display.rectangle(box_x, box_y, box_size, box_size)
    
    # =========================================================================
    # NAVIGATION INSTRUCTIONS
    # =========================================================================
    
    display.set_pen(get_text_color())
    display.text("NAVIGATION", 10, 105, W - 20, 1)
    display.text("Button A (top left): Previous/Left", 10, 120, W - 20, 1)
    display.text("Button X (top right): Next/Right", 10, 132, W - 20, 1)
    display.text("Button B (lower left): Page down", 10, 144, W - 20, 1)
    display.text("Button Y (lower right): Confirm/Enter", 10, 156, W - 20, 1)
    
    # =========================================================================
    # SECURITY INFORMATION
    # =========================================================================
    
    display.text("SECURITY", 10, 180, W - 10, 1)
    display.text("This is a stateless device. It has no battery and", 10, 192, W - 10, 1)
    display.text("operates only with a 5V power source. All data during", 10, 204, W - 10, 1)
    display.text("usage is stored in RAM only. No data is saved to flash", 10, 216, W - 10, 1)
    display.text("memory. Power off = complete wipe.", 10, 228, W - 10, 1)
    
    display.update()


def mnemonic_to_entropy(words):
    import hashlib
    indices = [BIP39_WORDS.index(w) for w in words]
    bits = []
    for idx in indices:
        for i in range(10, -1, -1):
            bits.append((idx >> i) & 1)
    entropy_bits = bits[:128]
    checksum_bits = bits[128:]
    entropy = bytearray(16)
    for i in range(16):
        v = 0
        for j in range(8):
            v = (v << 1) | entropy_bits[i * 8 + j]
        entropy[i] = v
    sha = hashlib.sha256(bytes(entropy)).digest()
    sha_bits = []
    for b in sha:
        for i in range(7, -1, -1):
            sha_bits.append((b >> i) & 1)
    if checksum_bits != sha_bits[:4]:
        raise ValueError("Invalid BIP39 mnemonic")
    return bytes(entropy)

def draw_page7():
    """Draw Compact SeedQR page (12 or 24 word) with optional zoom mode"""
    global qr_zoom_mode, qr_zoom_brightness
    
    try:
        from qr_encoder import create_qr_v1_l, create_qr_v2_l
    except ImportError:
        display.set_pen(get_bg_color())
        display.clear()
        display.set_pen(BLACK)
        display.text("6/9 Compact SeedQR", 10, 10, W - 20, 3)
        display.text("qr_encoder.py not found", 10, 60, W - 20, 2)
        display.update()
        return

    # Detect if we have 24-word seed (any words in rows 12-23)
    has_24_words = any(grid_bits[row][col] for row in range(12, 24) for col in range(12))
    
    bits = []
    # Process all 24 rows if 24-word mode, otherwise just first 12
    num_words = 24 if has_24_words else 12
    for row in range(num_words):
        row_value = sum(BIT_VALUES[col] for col in range(12) if grid_bits[row][col])
        if row_value > 0:
            word_index = row_value - 1
        else:
            word_index = 0
        for bit_pos in range(10, -1, -1):
            bits.append((word_index >> bit_pos) & 1)

    # Extract entropy bits (128 for 12 words, 256 for 24 words)
    entropy_bit_count = 256 if has_24_words else 128
    entropy_bits = bits[:entropy_bit_count]
    entropy_byte_count = entropy_bit_count // 8
    entropy = bytearray(entropy_byte_count)
    for i in range(entropy_byte_count):
        v = 0
        for j in range(8):
            v = (v << 1) | entropy_bits[i * 8 + j]
        entropy[i] = v

    # Use Version 1 (21x21) for 12-word, Version 2 (25x25) for 24-word
    if has_24_words:
        matrix = create_qr_v2_l(bytes(entropy))
    else:
        matrix = create_qr_v1_l(bytes(entropy))
    
    qr_size = len(matrix)
    
    # =========================================================================
    # QR ZOOM MODE - 200x200px QR only with brightness control
    # =========================================================================
    if qr_zoom_mode:
        # Set brightness for zoom mode
        display.set_backlight(qr_zoom_brightness)
        
        # White background for better QR scanning
        display.set_pen(WHITE)
        display.clear()
        
        # Draw 200x200 QR centered on screen
        qr_display_size = 200
        scale = qr_display_size // qr_size  # Calculate scale to fit 200px
        qr_pixel_size = qr_size * scale
        offset_x = (W - qr_pixel_size) // 2
        offset_y = (H - qr_pixel_size) // 2
        
        for y in range(qr_size):
            for x in range(qr_size):
                display.set_pen(BLACK if matrix[y][x] else WHITE)
                display.rectangle(
                    offset_x + x * scale,
                    offset_y + y * scale,
                    scale,
                    scale
                )
        
        display.update()
        return
    
    # =========================================================================
    # NORMAL MODE - Standard QR display with text and warning
    # =========================================================================
    
    # Ensure brightness is at default when not in zoom mode
    display.set_backlight(1.0)
    
    display.set_pen(get_bg_color())
    display.clear()
    display.set_pen(BLACK)
    display.text("6/9 Compact SeedQR", 10, 6, W - 20, 3)
    
    # Normal QR size
    if has_24_words:
        scale = 5  # Smaller scale for 25x25 to fit on screen
    else:
        scale = 6  # Larger scale for 21x21
    
    qr_pixel_size = qr_size * scale
    offset_x = (W - qr_pixel_size) // 2
    offset_y = 48

    for y in range(qr_size):
        for x in range(qr_size):
            display.set_pen(BLACK if matrix[y][x] else get_bg_color())
            display.rectangle(
                offset_x + x * scale,
                offset_y + y * scale,
                scale,
                scale
            )

    warning_height = 22
    warning_y = H - warning_height - 4
    text_y = warning_y - 32

    display.set_pen(get_text_color())
    display.text(
        "A CompactSeedQR is your seed phrase in another format. "
        "Treat it with extreme care, as anyone who can scan it can access your funds.",
        10,
        text_y,
        W - 20,
        1
    )

    display.set_pen(BLACK)
    display.rectangle(10, warning_y, W - 20, warning_height)
    display.set_pen(WHITE)
    display.text(
        "NEVER SCAN WITH ONLINE DEVICE",
        14,
        warning_y + 5,
        W - 28,
        2
    )
    display.update()

def draw_page8():
    """Draw Donate page with optional zoom mode"""
    global qr_zoom_mode, qr_zoom_brightness
    
    # FIX: Define color constants using display.create_pen()
    RED = display.create_pen(255, 0, 0)
    # WHITE already defined globally
    
    # Import your specific QR encoder file
    import qr_encoder
    
    donation_url = "is.gd/0ZeCoT" 
    data_bytes = donation_url.encode('utf-8')
    
    # Check if URL fits in the 17-byte limit
    if len(data_bytes) > 17:
        display.set_pen(get_bg_color())
        display.clear()
        draw_page_header("9/9 Donate")
        display.set_pen(RED)
        qr_x = (W - 126) // 2
        qr_y = 48
        display.text("Error:", qr_x + 5, qr_y + 30, 116, 1)
        display.text("URL too long!", qr_x + 5, qr_y + 45, 116, 1)
        display.text("Limit is 17 chars.", qr_x + 5, qr_y + 60, 116, 1)
        display.update()
        return 
    
    # Generate the matrix (21x21 grid)
    qr_matrix = qr_encoder.create_qr_v1_l(data_bytes)
    qr_size = 21
    
    # =========================================================================
    # QR ZOOM MODE - 200x200px QR only with brightness control
    # =========================================================================
    if qr_zoom_mode:
        # Set brightness for zoom mode
        display.set_backlight(qr_zoom_brightness)
        
        # White background for better QR scanning
        display.set_pen(WHITE)
        display.clear()
        
        # Draw 200x200 QR centered on screen
        qr_display_size = 200
        scale = qr_display_size // qr_size  # Calculate scale to fit 200px
        qr_pixel_size = qr_size * scale
        offset_x = (W - qr_pixel_size) // 2
        offset_y = (H - qr_pixel_size) // 2
        
        for r in range(qr_size):
            for c in range(qr_size):
                if qr_matrix[r][c]:
                    display.set_pen(BLACK)
                    display.rectangle(
                        offset_x + (c * scale),
                        offset_y + (r * scale),
                        scale,
                        scale
                    )
        
        display.update()
        return
    
    # =========================================================================
    # NORMAL MODE - Standard QR display with text and warning
    # =========================================================================
    
    # Ensure brightness is at default when not in zoom mode
    display.set_backlight(1.0)
    
    display.set_pen(get_bg_color())
    display.clear()
    draw_page_header("9/9 Donate")
    display.set_pen(BLACK)
    
    # ============================================================
    # CENTERED QR CODE (same position as page 6/9)
    # ============================================================
    
    # Use same QR size as page 6/9 for consistency
    qr_x = (W - 126) // 2  # 21 * 6 = 126px
    qr_y = 48  # Same as page 6/9
    
    # Calculate scaling - same as page 6/9
    scale = 6
    qr_pixel_size = 21 * scale  # 126 pixels
    offset_x = (126 - qr_pixel_size) // 2
    offset_y = (126 - qr_pixel_size) // 2
    
    # Draw the QR code
    for r in range(21):
        for c in range(21):
            if qr_matrix[r][c]:
                display.set_pen(BLACK)
                display.rectangle(
                    qr_x + offset_x + (c * scale),
                    qr_y + offset_y + (r * scale),
                    scale,
                    scale
                )
    
    # ============================================================
    # SUPPORT TEXT (between QR and warning banner)
    # ============================================================
    
    warning_height = 22
    warning_y = H - warning_height - 4
    text_y = warning_y - 28  # Adjust for 2 lines instead of 4
    
    display.set_pen(get_text_color())
    display.text("Your support lets us focus on further development. Thank you!", 10, text_y, W - 20, 1)
    display.text("URL: https://is.gd/0ZeCoT routes to Opennode's secure checkout.", 10, text_y + 12, W - 20, 1)
    
    # ============================================================
    # WARNING BANNER AT BOTTOM (same style as page 6/9)
    # ============================================================
    
    display.set_pen(BLACK)
    display.rectangle(10, warning_y, W - 20, warning_height)
    display.set_pen(WHITE)
    display.text("SAFE TO SCAN WITH YOUR PHONE", 14, warning_y + 5, W - 28, 2)
    
    # Add subtle border around warning
    display.set_pen(BLACK)
    display.rectangle(10, warning_y, W - 20, 2)
    display.rectangle(10, warning_y + warning_height - 2, W - 20, 2)
    display.rectangle(10, warning_y, 2, warning_height)
    display.rectangle(W - 12, warning_y, 2, warning_height)
    
    display.update()
def draw_current_page():
    if page == 1: draw_page1()      # 1/9 Binary Dots
    elif page == 2: draw_page2()    # 2/9 Word
    elif page == 3: draw_page3()    # 3/9 Word Number
    elif page == 4: draw_page_wordlist()  # 4/9 BIP39 Wordlist
    elif page == 5: draw_page4()    # 5/9 Binary Grid
    elif page == 6: draw_page7()    # 6/9 Compact SeedQR
    elif page == 7: draw_page6()    # 7/9 Navigation
    elif page == 8: draw_page5()    # 8/9 Project DotBip
    elif page == 9: draw_page8()    # 9/9 Donate

def kbd_next():
    global kbd_index
    kbd_index = (kbd_index + 1) % len(KEY_BUTTONS)

def kbd_prev():
    global kbd_index
    kbd_index = (kbd_index - 1) % len(KEY_BUTTONS)

def num_next():
    global num_index
    num_index = (num_index + 1) % len(NUM_BUTTONS)

def num_prev():
    global num_index
    num_index = (num_index - 1) % len(NUM_BUTTONS)

def kbd_confirm():
    global word_buffer, suggestion_active, suggestion_word, page, selected, save_selected_index
    kb = KEY_BUTTONS[kbd_index]
    t = kb['type']
    if suggestion_active and suggestion_word and t != 'back':
        try:
            idx = BIP39_WORDS.index(suggestion_word)
            set_bits_from_value(idx + 1)
            word_buffer = ""
            suggestion_active = False
            suggestion_word = ""
            save_selected_index = 0  # Select word button #1
            page = 1
            return
        except ValueError:
            return
    if t == 'key':
        if len(word_buffer) < MAX_WORD_LEN:
            word_buffer = word_buffer + kb['label']
            recalc_suggestion()
    elif t == 'back':
        if len(word_buffer) > 0:
            word_buffer = word_buffer[:-1]
            recalc_suggestion()
    elif t == 'enter':
        w = word_buffer.lower()
        if w in BIP39_WORDS:
            idx = BIP39_WORDS.index(w)
            set_bits_from_value(idx + 1)
            word_buffer = ""
            suggestion_active = False
            suggestion_word = ""
            save_selected_index = 0  # Select word button #1
            page = 1

def num_confirm():
    global num_buffer, page, selected, save_selected_index, num_error
    nb = NUM_BUTTONS[num_index]
    t = nb['type']
    if t == 'num':
        if len(num_buffer) < 4:
            num_buffer = num_buffer + nb['label']
            num_error = ""  # Clear error when typing
    elif t == 'back':
        if len(num_buffer) > 0:
            num_buffer = num_buffer[:-1]
            num_error = ""  # Clear error when deleting
    elif t == 'enter':
        if len(num_buffer) > 0:
            try:
                v = int(num_buffer)
                if 1 <= v <= 2048:
                    set_bits_from_value(v)
                    num_buffer = ""
                    num_error = ""
                    save_selected_index = 0  # Select word button #1
                    page = 1
                elif v == 0 or v < 1:
                    # Number too low
                    num_error = "Word number is too low. It needs to be in the range 1-2048."
                else:
                    # Number too high (> 2048)
                    num_error = "Word number is too high. Max 2048 words."
            except:
                num_error = "Invalid number"

# =============================================================================
# MAIN LOOP
# =============================================================================

# =============================================================================
# SPLASH SCREEN SEQUENCE
# =============================================================================

def show_splash_screen(filename, duration=1.0):
    """Display a splash screen JPEG image for specified duration"""
    try:
        import jpegdec
        
        # Create JPEG decoder
        j = jpegdec.JPEG(display)
        
        # Clear screen
        display.set_pen(BLACK)
        display.clear()
        
        # Open and decode JPEG
        j.open_file(filename)
        j.decode(0, 0, jpegdec.JPEG_SCALE_FULL)
        display.update()
        sleep(duration)
        return True
        
    except Exception as e:
        # If image fails, show error
        display.set_pen(get_bg_color())
        display.clear()
        display.set_pen(BLACK)
        display.text(f"Error loading: {filename}", 10, H//2 - 10, W - 20, 1)
        display.update()
        sleep(duration)
        return False

# Show splash sequence
recalc_suggestion()
show_splash_screen("splash2.jpg", 3.0)
show_splash_screen("splash3.jpg", 3.0)

draw_current_page()

while True:
    try:
        # B = Page turner
        if is_pressed(button_b):
            # Exit QR zoom mode and reset brightness if currently in zoom mode
            if qr_zoom_mode:
                qr_zoom_mode = False
                qr_zoom_brightness = 1.0
                display.set_backlight(1.0)
            
            page += 1
            if page > NUM_PAGES: page = 1
            draw_current_page()
            sleep(0.12)
        
        if page == 1:
            val = current_value()
            
            # Check if we're in save mode
            if save_selected_index >= 0:
                # SAVE MODE NAVIGATION
                if is_pressed(button_a):
                    if save_selected_index == 0:
                        # Go back to bit 11
                        save_selected_index = -1
                        selected = 11
                    else:
                        save_selected_index = (save_selected_index - 1) % 24
                    draw_current_page()
                
                if is_pressed(button_x):
                    if save_selected_index == 23:
                        # From word #24, go back to bit 0
                        save_selected_index = -1
                        selected = 0
                    else:
                        save_selected_index = (save_selected_index + 1) % 24
                    draw_current_page()
                
                if is_pressed(button_y):
                    # Save directly to selected word position (1-24)
                    row = save_selected_index
                    for c in range(12):
                        grid_bits[row][c] = bits[c]
                    # Show confirmation
                    save_confirmed_msg = True
                    draw_current_page()
                    sleep(0.5)
                    # Reset everything: clear bits, reset to bit 11 (box 12, rightmost)
                    for i in range(12):
                        bits[i] = False
                    selected = 11
                    save_selected_index = -1
                    save_word_position = None
                    save_confirmed_msg = False
                    draw_current_page()
            else:
                # NORMAL MODE NAVIGATION
                if is_pressed(button_a):
                    if selected == 0 and val > 0:
                        # Jump to save mode at last word position (23 = word #24)
                        save_selected_index = 23
                    else:
                        selected = (selected - 1) % 12
                    draw_current_page()
                
                if is_pressed(button_x):
                    if selected == 11 and val > 0:
                        # Jump to save mode at first word position (0 = word #1)
                        save_selected_index = 0
                    else:
                        selected = (selected + 1) % 12
                    draw_current_page()
                
                if is_pressed(button_y):
                    if selected < 12:
                        toggle_bit(selected)
                    draw_current_page()
        
        elif page == 2:
            if is_pressed(button_a): kbd_prev(); draw_current_page()
            if is_pressed(button_x): kbd_next(); draw_current_page()
            if is_pressed(button_y): kbd_confirm(); draw_current_page()
        elif page == 3:
            if is_pressed(button_a): num_prev(); draw_current_page()
            if is_pressed(button_x): num_next(); draw_current_page()
            if is_pressed(button_y): num_confirm(); draw_current_page()
        elif page == 4:
            # Page 4: BIP39 Wordlist - Custom debouncing
            now = ticks_ms()
            
            # Check if enough time has passed since last press
            if now - wordlist_last_press > DEBOUNCE_MS:
                # Check A button (previous word)
                if button_a.read():
                    wordlist_last_press = now
                    wordlist_index = (wordlist_index - 1) % 2048
                    draw_current_page()
                
                # Check X button (next word)
                elif button_x.read():
                    wordlist_last_press = now
                    wordlist_index = (wordlist_index + 1) % 2048
                    draw_current_page()
                
                # Check Y button (select word and load to page 1)
                elif button_y.read():
                    wordlist_last_press = now
                    # Load selected word into bits and go to page 1
                    word_num = wordlist_index + 1
                    load_word_number_to_bits(word_num)
                    page = 1
                    save_selected_index = 0  # Select word button #1
                    draw_current_page()
        elif page == 5:
            # Page 5: Binary Grid
            if grid_mask_on:
                if is_pressed(button_y):
                    grid_mask_on = False
                    draw_current_page()
                continue
            
            if is_pressed(button_a):
                # A button = Previous/Left
                if grid_selected_row == 0 and grid_selected_col == 0:
                    # From grid spot 1 (row 0, col 0), go to page 1 square
                    grid_selected_row = 0
                    grid_selected_col = -3
                elif grid_selected_row == 0 and grid_selected_col == -3:
                    # From page 1 square, go to page 2 square
                    grid_selected_col = -4
                elif grid_selected_row == 0 and grid_selected_col == -4:
                    # From page 2 square, go to Clear
                    grid_selected_row = 11
                    grid_selected_col = -2
                elif grid_selected_row == 11 and grid_selected_col == -2:
                    # From Clear, go to last grid spot (row 11, col 11)
                    grid_selected_col = 11
                else:
                    # Normal grid navigation
                    grid_selected_col -= 1
                    if grid_selected_col < 0:
                        grid_selected_col = 11
                        grid_selected_row -= 1
                        if grid_selected_row < 0: grid_selected_row = 11
                draw_current_page()
                
            if is_pressed(button_x):
                # X button = Next/Right
                if grid_selected_row == 11 and grid_selected_col == 11:
                    # From last grid spot (row 11, col 11), go to Clear
                    grid_selected_col = -2
                elif grid_selected_row == 11 and grid_selected_col == -2:
                    # From Clear, go to page 2 square
                    grid_selected_row = 0
                    grid_selected_col = -4
                elif grid_selected_row == 0 and grid_selected_col == -4:
                    # From page 2 square, go to page 1 square
                    grid_selected_col = -3
                elif grid_selected_row == 0 and grid_selected_col == -3:
                    # From page 1 square, go to grid spot 1 (row 0, col 0)
                    grid_selected_col = 0
                else:
                    # Normal grid navigation
                    grid_selected_col += 1
                    if grid_selected_col > 11:
                        grid_selected_col = 0
                        grid_selected_row += 1
                        if grid_selected_row > 11: grid_selected_row = 0
                draw_current_page()
            
            if is_pressed(button_y):
                if grid_selected_row == 0 and grid_selected_col == -4:
                    # Left square: switch to page 2
                    grid_page = 2
                    draw_current_page()
                elif grid_selected_row == 0 and grid_selected_col == -3:
                    # Right square: switch to page 1
                    grid_page = 1
                    draw_current_page()
                elif grid_selected_row == 11 and grid_selected_col == -2:
                    # Clear button: clear current page's 12 words
                    row_offset = (grid_page - 1) * 12
                    for r in range(row_offset, row_offset + 12):
                        for c in range(12):
                            grid_bits[r][c] = False
                    draw_current_page()
                elif 0 <= grid_selected_row < 12 and 0 <= grid_selected_col < 12:
                    # Calculate actual row based on current page
                    actual_row = (grid_page - 1) * 12 + grid_selected_row
                    if grid_selected_col == 0:
                        # Toggling column 0 (2048/zoo)
                        if not grid_bits[actual_row][0]:
                            # Turning it ON: clear all other columns first
                            for c in range(12):
                                grid_bits[actual_row][c] = False
                            grid_bits[actual_row][0] = True
                        else:
                            # Turning it OFF: just turn it off
                            grid_bits[actual_row][0] = False
                    else:
                        # Toggling any other column
                        if grid_bits[actual_row][0]:
                            # If column 0 is ON, turn it OFF first
                            grid_bits[actual_row][0] = False
                        # Then toggle the selected column
                        grid_bits[actual_row][grid_selected_col] = not grid_bits[actual_row][grid_selected_col]
                    draw_current_page()
        
        elif page == 6:
            # Page 6/9: Compact SeedQR - QR zoom mode with brightness control
            if is_pressed(button_y):
                # Toggle QR zoom mode
                qr_zoom_mode = not qr_zoom_mode
                if not qr_zoom_mode:
                    # Exiting zoom mode - reset brightness to default
                    qr_zoom_brightness = 1.0
                    display.set_backlight(1.0)
                draw_current_page()
            
            if qr_zoom_mode:
                # Only handle brightness controls when in zoom mode
                if is_pressed(button_a):
                    # Decrease brightness by 10% (min 0.2 / 20%)
                    qr_zoom_brightness = max(0.2, qr_zoom_brightness - 0.1)
                    draw_current_page()
                
                if is_pressed(button_x):
                    # Increase brightness by 10% (max 1.0 / 100%)
                    qr_zoom_brightness = min(1.0, qr_zoom_brightness + 0.1)
                    draw_current_page()
        
        elif page == 7:
            # Page 7/9: Settings - Color scheme selection
            # A/X buttons change color scheme instantly (no confirm needed)
            if is_pressed(button_a):
                # Previous color scheme
                color_scheme_index = (color_scheme_index - 1) % 4
                set_color_scheme(color_scheme_names[color_scheme_index])
                draw_current_page()
            
            if is_pressed(button_x):
                # Next color scheme
                color_scheme_index = (color_scheme_index + 1) % 4
                set_color_scheme(color_scheme_names[color_scheme_index])
                draw_current_page()
        
        elif page == 9:
            # Page 9/9: Donate - QR zoom mode with brightness control
            if is_pressed(button_y):
                # Toggle QR zoom mode
                qr_zoom_mode = not qr_zoom_mode
                if not qr_zoom_mode:
                    # Exiting zoom mode - reset brightness to default
                    qr_zoom_brightness = 1.0
                    display.set_backlight(1.0)
                draw_current_page()
            
            if qr_zoom_mode:
                # Only handle brightness controls when in zoom mode
                if is_pressed(button_a):
                    # Decrease brightness by 10% (min 0.2 / 20%)
                    qr_zoom_brightness = max(0.2, qr_zoom_brightness - 0.1)
                    draw_current_page()
                
                if is_pressed(button_x):
                    # Increase brightness by 10% (max 1.0 / 100%)
                    qr_zoom_brightness = min(1.0, qr_zoom_brightness + 0.1)
                    draw_current_page()
        
        sleep(0.05)
    except KeyboardInterrupt:
        break

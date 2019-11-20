#-----------------------------------------------------------------------------------------------------------------------

# AS A DEADHEAD, ARCHIVE.ORG IS AN INVALUABLE RESOURCE.  WE ARE ALL FAMILIAR WITH SHOWS THAT ALLOW YOU TO DOWNLOAD FLACS OR MP3S,
# AND FOR 'STREAM ONLY' SHOWS THERE IS OUR BELOVED GRATEFUL GRABBER.  BUT WHAT IF YOU WANT EVERY SHOW?  YES, EVERY SHOW. OR EVERY SHOW OF A PARTICULAR YEAR.
# PARANOID BY NATURE, I BEGAN IMAGINING A DISASTER SCENARIO WHERE THE ZOMBIE (OR OTHER) APOCALYPSE TAKES DOWN THE INTERNET,
# AND WITH IT, OUR BELOVED ARCHIVE.  IN THAT BRAVE NEW LANDSCAPE I STILL WANT TO DISCOVER NEW SHOWS AND LISTEN TO THEM AS I PLEASE,
# ON A GENERATOR POWERED STEREO, AS I WAIT FOR THE UNKNOWN.

# AS OF 11/20/2019 THERE ARE EXACTLY 14000 SHOWS IN THE ARCHIVE'S GRATEFUL DEAD COLLECTION.
# IF YOU HAVE A GOOD INTERNET CONNECTION AND PLENTY OF STORAGE SPACE, YOU CAN DOWNLOAD ALL 14000 SHOWS WITH 7 LINES OF CODE.
# THOUGH SOME MAY FIND IT MORE MANAGEABLE TO SEGMENT AND DOWNLOAD SHOWS BY YEAR.

# AFTER EXTENSIVE RESEARCH AND MUCH TRIAL AND ERROR I STUMBLED UPON THESE RESOURCES WHICH LED TO THE SOLUTION:

    # ARCHIVE HAS IT'S OWN PYTHON API FOR DOWNLOADING STUFF???  THIS IS WAY EASIER THAN THE BEAUTIFUL SOUP STUFF I WAS TRYING:
    # https://gareth.halfacree.co.uk/2013/04/bulk-downloading-collections-from-archive-org

    # HOW TO OBTAIN LISTS OF IDENTIFIERS USED TO DOWNLOAD SHOWS:
    # https://blog.archive.org/2012/04/26/downloading-in-bulk-using-wget/

    # internetarchive API QUICK START GUIDE:
    # https://archive.org/services/docs/api/internetarchive/quickstart.html

# PRE-REQUISITES:

# DOWNLOAD AND INSTALL PYTHON: https://www.python.org/downloads/

# DOWNLOAD A PYTHON IDE (OPTIONAL): https://www.jetbrains.com/pycharm/

# GET internetarchive PACKAGE: (from command line) pip install internetarchive

# CREATE CONFIG FILE WITH ARCHIVE.ORG CREDENTIALS:

    # (from command line) ia configure

    # Enter your archive.org credentials below to configure 'ia'.
    #
    # Email address: user@example.com
    # Password:
    #
    # Config saved to: /home/user/.config/ia.ini

# OBTAIN CSV LIST OF ALL SHOWS:

    # GO TO ARCHIVE.ORG: UNDER THE SEARCH BAR CLICK 'Advanced Search'; IN THE UPPER 'ADVANCED SEARCH' BLOCK: SEARCH:

            #       AND           Collection:        is           GratefulDead          <--must type exactly this

    # HIT SEARCH; THIS REDIRECTS TO SEARCH RESULTS WITH SYNTAX IN SEARCH FIELD:     collection:(GratefulDead)
    # COPY SEARCH SYNTAX AND GO BACK TO ADVANCED SEARCH PAGE
    #
    # IN LOWER 'Advanced Search returning JSON, XML, and more' BLOCK: PASTE:        collection:(GratefulDead)       INTO 'Query' FIELD
    # SELECT 'identifier' IN 'Fields to return' list
    # CHANGE 'NUMBER OF RESULTS' TO 15000
    # SELECT 'CSV FORMAT'
    # HIT SEARCH
    # HIT 'OK' ON POP-UP NOTE
    # OPEN CSV FILE, DELETE 'IDENTIFIER' COLUMN HEADER
    # SAVE, CLOSE
    # SET PATH TO CSV FILE (HARDCODE IN .PY FILE)
    # SET PATH TO LOCAL DIRECTORY TO SAVE FILES (HARDCODE IN .PY FILE)
    # RUN SELECTED .PY FILE FROM COMMAND LINE
    	# OPTION 1: DOWNLOAD ALL 14000 GRATEFUL DEAD SHOWS AT ONCE: download_all_gd.py
    	# OPTION 2: SEGMENT AND DOWNLOAD SHOWS BY YEAR: download_gd_by_year.py

    # NOTE TO SELF: COLLECTION NAME FOR DEAD & COMPANY: collection:(DeadAndCompany)
    # NOTE TO ALL:  YOU CAN FIND THESE 'COLLECTION NAMES' ON ARCHIVE, YOU JUST GOTTA POKE AROUND	

# STATS FROM SEGMENTATION AND DOWNLOAD BY YEAR BASED ON 1975:

# INTERNET CONNECTION DETAILS:
# DOWNLOAD Mbps: 887.41
# UPLOAD Mbps: 839.64
# https://www.speedtest.net/

# 1975: 55 shows
# time to download all 1975: 81.11 minutes
# download time per show: 1.47 minutes
# total size of 1975: 6.35 GB
# average file size per show:  115.45 MB

# Estimate regarding all 14000 shows based on 1975 stats:
# Approx: 1.62 TB TOTAL
# Approx: 344 Total hours to download (14 days!)
# MILEAGE WILL VARY

# BREAKDOWN: NUMBER OF SHOWS BY YEAR (as of 11/20/2019):
# 65: 3 shows
# 66: 69 shows
# 67: 48 shows
# 68: 113 shows
# 69: 291 shows
# 70: 340 shows
# 71: 307 shows
# 72: 325 shows
# 73: 379 shows
# 74: 270 shows
# 75: 55 shows
# 76: 251 shows
# 77: 352 shows
# 78: 462 shows
# 79: 453 shows
# 80: 613 shows
# 81: 638 shows
# 82: 524 shows
# 83: 812 shows
# 84: 688 shows
# 85: 874 shows
# 86: 497 shows
# 87: 772 shows
# 88: 684 shows
# 89: 854 shows
# 90: 933 shows
# 91: 682 shows
# 92: 406 shows
# 93: 576 shows
# 94: 412 shows
# 95: 315 shows
# gdnrps: 2 shows
# Total: 14000 shows

# TESTING SOME FUNCTIONALITY IN THE internetarchive API

#-----------------------------------------------------------------------------------------------------------------------

# TESTING:

# DOWNLOADABLE SHOW

                             #THIS IS THE IDENTIFIER
#download('gd1977-11-05.aud.zimmerman.minches.81180.sbeok.flac16', verbose=True, glob_pattern='*.mp3') # SUCCESS

#-----------------------------------------------------------------------------------------------------------------------

# TESTING:

# STREAM-ONLY SHOW

                   #THIS IS THE IDENTIFIER
#download('gd73-06-10.sbd.hollister.174.sbeok.shnf', verbose=True, glob_pattern='*.mp3', destdir=r"H:\gd") # SUCCESS

#-----------------------------------------------------------------------------------------------------------------------


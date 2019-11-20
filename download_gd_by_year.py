from internetarchive import get_item
from internetarchive import download
from internetarchive import search_items
import time as t

#-----------------------------------------------------------------------------------------------------------------------

# START TIME OF JOB

start = t.time()

#-----------------------------------------------------------------------------------------------------------------------

# READ CSV FILE INTO LIST

f = open(r"H:\14000.csv") # PATH TO CSV FILE
x = f.readlines()
f.close()

with open(r"H:\14000.csv") as f:
    x = f.read().splitlines()

#-----------------------------------------------------------------------------------------------------------------------

# SEGMENT BY YEAR

gd65_matchers = ['gd65', 'gd1965']
gd65_matching = [s for s in x if any(xs in s for xs in gd65_matchers)]

gd66_matchers = ['gd66', 'gd1966']
gd66_matching = [s for s in x if any(xs in s for xs in gd66_matchers)]

gd67_matchers = ['gd67', 'gd1967']
gd67_matching = [s for s in x if any(xs in s for xs in gd67_matchers)]

gd68_matchers = ['gd68', 'gd1968']
gd68_matching = [s for s in x if any(xs in s for xs in gd68_matchers)]

gd69_matchers = ['gd69', 'gd1969']
gd69_matching = [s for s in x if any(xs in s for xs in gd69_matchers)]

gd70_matchers = ['gd70', 'gd1970']
gd70_matching = [s for s in x if any(xs in s for xs in gd70_matchers)]

gd71_matchers = ['gd71', 'gd1971']
gd71_matching = [s for s in x if any(xs in s for xs in gd71_matchers)]

gd72_matchers = ['gd72', 'gd1972']
gd72_matching = [s for s in x if any(xs in s for xs in gd72_matchers)]

gd73_matchers = ['gd73', 'gd1973']
gd73_matching = [s for s in x if any(xs in s for xs in gd73_matchers)]

gd74_matchers = ['gd74', 'gd1974']
gd74_matching = [s for s in x if any(xs in s for xs in gd74_matchers)]

gd75_matchers = ['gd75', 'gd1975']
gd75_matching = [s for s in x if any(xs in s for xs in gd75_matchers)]

gd76_matchers = ['gd76', 'gd1976']
gd76_matching = [s for s in x if any(xs in s for xs in gd76_matchers)]

gd77_matchers = ['gd77', 'gd1977']
gd77_matching = [s for s in x if any(xs in s for xs in gd77_matchers)]

gd78_matchers = ['gd78', 'gd1978']
gd78_matching = [s for s in x if any(xs in s for xs in gd78_matchers)]

gd79_matchers = ['gd79', 'gd1979']
gd79_matching = [s for s in x if any(xs in s for xs in gd79_matchers)]

gd80_matchers = ['gd80', 'gd1980']
gd80_matching = [s for s in x if any(xs in s for xs in gd80_matchers)]

gd81_matchers = ['gd81', 'gd1981']
gd81_matching = [s for s in x if any(xs in s for xs in gd81_matchers)]

gd82_matchers = ['gd82', 'gd1982']
gd82_matching = [s for s in x if any(xs in s for xs in gd82_matchers)]

gd83_matchers = ['gd83', 'gd1983']
gd83_matching = [s for s in x if any(xs in s for xs in gd83_matchers)]

gd84_matchers = ['gd84', 'gd1984']
gd84_matching = [s for s in x if any(xs in s for xs in gd84_matchers)]

gd85_matchers = ['gd85', 'gd1985']
gd85_matching = [s for s in x if any(xs in s for xs in gd85_matchers)]

gd86_matchers = ['gd86', 'gd1986']
gd86_matching = [s for s in x if any(xs in s for xs in gd86_matchers)]

gd87_matchers = ['gd87', 'gd1987']
gd87_matching = [s for s in x if any(xs in s for xs in gd87_matchers)]

gd88_matchers = ['gd88', 'gd1988']
gd88_matching = [s for s in x if any(xs in s for xs in gd88_matchers)]

gd89_matchers = ['gd89', 'gd1989']
gd89_matching = [s for s in x if any(xs in s for xs in gd89_matchers)]

gd90_matchers = ['gd90', 'gd1990']
gd90_matching = [s for s in x if any(xs in s for xs in gd90_matchers)]

gd91_matchers = ['gd91', 'gd1991']
gd91_matching = [s for s in x if any(xs in s for xs in gd91_matchers)]

gd92_matchers = ['gd92', 'gd1992']
gd92_matching = [s for s in x if any(xs in s for xs in gd92_matchers)]

gd93_matchers = ['gd93', 'gd1993']
gd93_matching = [s for s in x if any(xs in s for xs in gd93_matchers)]

gd94_matchers = ['gd94', 'gd1994']
gd94_matching = [s for s in x if any(xs in s for xs in gd94_matchers)]

gd95_matchers = ['gd95', 'gd1995']
gd95_matching = [s for s in x if any(xs in s for xs in gd95_matchers)]

gdnrps_matchers = ['gd_nrps']
gdnrps_matching = [s for s in x if any(xs in s for xs in gdnrps_matchers)]

# DOWNLOAD BY YEAR

for a in gd75_matching: ## YEAR TO DOWNLOAD; CHANGE AS DESIRED
    download(a, verbose=True, glob_pattern='*.mp3', destdir=r"C:\Users\username\Desktop\gd") # LOCAL DIRECTORY TO SAVE FILES

#-----------------------------------------------------------------------------------------------------------------------

# END TIME OF JOB

end = t.time()
print('time to complete: ' + str((end - start) / 60) + ' minutes')

#-----------------------------------------------------------------------------------------------------------------------

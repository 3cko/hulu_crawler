#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

#hulu start
start = 441968
#hulu end
end = 442258
detail_lines = []
# Series Name
string_to_match = "Star Trek: The Next Generation"
# filenames to save as
file_save_formatting = "tng.s{0:02d}e{1:02d}.{2}.flv"
# list of valid files matching the info
list_of_urls = 'tng.list.to.dl'
####
####
#
# To download from the list, bash!
# while read url delim name; do $(get_flash_videos -r high -f "./downloads/$name" "$url") ; done < tng.list.to.dl
#
####
####

def find_details(param, html):
    invalids = ['"', ' ', "'"]
    element = "Hulu.Models.Video"
    element = html.find(element)
    dig = html.find(param, element)
    start = html.find(":", dig)
    end = html.find(",", start)
    found = html[start + 2: end]
    for inv in invalids:
        found = found.replace(inv, '')
    return found


#with open('tng.episodes.list') as epi_list:
for x in range(start, end + 1):
    url = "http://www.hulu.com/watch/{0}".format(x)
    try:
        request = urllib2.Request(url)
        request.add_header('User-Agent', 'Mozilla')
        request.add_header('Referer', 'yea!')

        response = urllib2.urlopen(request)
        html = response.read()
        tit = find_details("title", html)
        season = find_details("season_number", html)
        epi = find_details("episode_number", html)
        if string_to_match in html:
            print "{0} - {1}".format(season, epi)
            print url
            file_name = file_save_formatting.format(int(season), int(epi), tit.lower())
            const = "{0} - {1}".format(url.rstrip('\n\r'), file_name)
            detail_lines.append(const)
        else:
            pass

    except urllib2.URLError:
        pass
        #print 'failure {0}'.format(x)

f = open(list_of_urls, 'w')
for line in detail_lines:
    f.write(line)
    f.write('\n')

f.close()

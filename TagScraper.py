import bs4, requests, logging, random, os
import pendulum

serverLogFile = '/tmp/TagScraperLog.txt'

# Logfile location on a server:
if os.path.isfile(serverLogFile):
    os.remove(serverLogFile)

# Create the new fresh log called 'TagScraperLog.txt':
logging.basicConfig(filename='/tmp/TagScraperLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s -%(message)s')

def scrapeTags():
    r = requests.get('https://bandcamp.com/tags')
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    genre_tag_list = []
    location_tag_list = []
    genre_tags = soup.find(id='tags_cloud').find_all('a')
    logging.debug('\n\nCYCLING THROUGH genre_tags:')
    for item in genre_tags:
        logging.debug('\n' + 'https://bandcamp.com' + str(item.attrs['href']))
        genre_tag_list.append(str('https://bandcamp.com' + str(item.attrs['href'])))
        location_tags = soup.find(id='locations_cloud').find_all('a')
        logging.debug('\n\nCYCLING THROUGH location_tags:')
    for item in location_tags:
        logging.debug('\n' + 'https://bandcamp.com' + str(item.attrs['href']))
        location_tag_list.append(str('https://bandcamp.com' + str(item.attrs['href'])))
        
    return genre_tag_list, location_tag_list

            
def writeTags(genre_tag_list, location_tag_list):
    genre_tag_list = sorted(genre_tag_list)
    # Remove the blank tag if present:
    genre_tag_list.remove('https://bandcamp.com/tag/')
    location_tag_list = sorted(location_tag_list)
    current_date_eastern = pendulum.now('America/New_York').format('dddd, MMMM D, YYYY')
    current_time_eastern = pendulum.now('America/New_York').format('hh:mm:ss A')
    logging.debug('\n\nCREATING USER FORM DATA:')
    with open('/var/www/musimatic/pythonprojectwebsites/Bandcamper/tags.html', 'w') as f:
        f.write('<html>')
        f.write('<link rel="stylesheet" href="css/bandcamper.css" type="text/css"/>')
        f.write('<head>')
        f.write('<title>Bandcamper</title>')
        f.write('<meta charset="utf-8"/>')        
        f.write('<link rel="stylesheet" href="css/output.css" type="text/css"/>')
        # JS Code Adapted From This StackOverflow Example:
        # https://stackoverflow.com/questions/46737895/how-to-display-a-list-of-links-as-a-drop-down-select
        # Another example:
        # https://jsfiddle.net/198bdcec/5/
        f.write('</head>')
        f.write('<body>')
        f.write('<h1>Bandcamper</h1>')
        f.write('<h2>Last Time Updated: ' + str(current_date_eastern) + ' at ' + str(current_time_eastern) + ' EDT</h2>')
        f.write('<br />')
        f.write('<a href="http://www.musimatic.xyz">BACK TO HOMEPAGE</a>')
        f.write('<br />')
        f.write('<br />')
        f.write('<a href="https://git.musimatic.xyz/Bandcamper/tree/">Source Code Link</a>')
        f.write('<br />')
        f.write('<br />')
        f.write('<p>Pick a genre or a location from one of the two drop-down menus to visit Bandcamp and discover new bands!</p>')
        f.write('<br />')
        f.write('<form>')
        f.write('<br />')
        f.write('<label for="genre-select">Choose A Genre: </label>')
        f.write('<select name="genre" id="genre-select">')
        f.write('<option value="">--Please Choose A Genre--</option>')
        for genre in genre_tag_list:
            f.write('<option value="' + str(genre) + '"><a href="' + str(genre) + '">')
            f.write(genre)
            f.write('</a></option>')
            f.write('\n')
        f.write('</select>')
        f.write('<button id="genreGoButton">GO!</button>')            
        f.write('</form>')
        f.write('<br />')
        f.write('<br />')
        f.write('<form>')
        f.write('<label for="location-select">Choose A Location: </label>')
        f.write('<select name="location" id="location-select">')
        f.write('<option value="">--Please Choose A Location--</option>')        
        for location in location_tag_list:
            f.write('<option value="' + str(location) + '"><a href="' + str(location) + '">')
            f.write(location)
            f.write('</a></option>')
            f.write('\n')
        f.write('</select>')
        f.write('<button id="locationGoButton">GO!</button>')            
        f.write('</form>')
        f.write('<br />')
        f.write('<br />')
        f.write('<script src="js/tags.js"></script>')
        f.write('</body>')
        f.write('</html>')
    f.close()

        
def main():
    genre_tag_list, location_tag_list = scrapeTags()
    logging.debug('\n\nCHECKING genre_tag_list: ')
    for item in genre_tag_list:
        logging.debug('\n' + str(item))
        logging.debug('\n\nCHECKING location_tag_list: ')
    for item in location_tag_list:
        logging.debug('\n' + str(item))
        writeTags(genre_tag_list, location_tag_list)


if __name__ == "__main__":
    main()

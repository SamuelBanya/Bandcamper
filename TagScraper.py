import bs4, requests, logging, random, os
import pendulum
import shutil
from dotenv import load_dotenv
from pathlib import Path

# Global Variables:
load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)
WEBSITE_PATH = os.getenv("WEBSITE_PATH")
print('WEBSITE_PATH: ' + str(WEBSITE_PATH))
# art_gallery_path = '/var/www/musimatic/images/ArtGallery'
art_portfolio_path = str(WEBSITE_PATH) + str("/images/ArtPortfolio")
WEBSITE_ADDRESS = os.getenv("WEBSITE_ADDRESS")
print('WEBSITE_ADDRESS: ' + str(WEBSITE_ADDRESS))
WEBSITE_FULL_ADDRESS = os.getenv("WEBSITE_FULL_ADDRESS")
print('WEBSITE_FULL_ADDRESS: ' + str(WEBSITE_FULL_ADDRESS))
PROJECT_DIRECTORY = os.getenv("PROJECT_DIRECTORY")
print('PROJECT_DIRECTORY: ' + str(PROJECT_DIRECTORY))
serverLogFile = '/tmp/TagScraperLog.txt'

# Logfile location on a server:
if os.path.isfile(serverLogFile):
    os.remove(serverLogFile)

# Create the new fresh log called 'TagScraperLog.txt':
logging.basicConfig(filename='/tmp/TagScraperLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s -%(message)s')

def copyOverCSSAndJS():
    css_file_path = str(WEBSITE_PATH + '/css/bandcamper.css')
    print('css_file_path: ' + str(css_file_path))
    shutil.copyfile(str(PROJECT_DIRECTORY) + '/css/bandcamper.css', css_file_path)

    # Create JS script for art gallery page using project's example:
    js_file_path = str(WEBSITE_PATH + '/js/tags.js')
    shutil.copyfile(str(PROJECT_DIRECTORY) + '/js/tags.js', js_file_path)

    
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
        f.write('<head>')        
        f.write('<link rel="stylesheet" href="css/bandcamper.css" type="text/css"/>')
        f.write('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">')
        f.write('<title>Bandcamper</title>')
        f.write('<meta charset="utf-8"/>')
        # JS Code Adapted From This StackOverflow Example:
        # https://stackoverflow.com/questions/46737895/how-to-display-a-list-of-links-as-a-drop-down-select
        # Another example:
        # https://jsfiddle.net/198bdcec/5/
        f.write('</head>')
        f.write('<body>')
        f.write('<div id="content">')
        f.write('<nav class="navbar navbar-expand-lg navbar-dark bg-dark" aria-label="Ninth navbar example">')
        f.write('<div class="container-xl">')
        f.write('<a class="navbar-brand" href="#">Bandcamper</a>')
        f.write('<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsExample07XL" aria-controls="navbarsExample07XL" aria-expanded="false" aria-label="Toggle navigation">')
        f.write('<span class="navbar-toggler-icon"></span>')
        f.write('</button>')
        f.write('<div class="collapse navbar-collapse" id="navbarsExample07XL">')
        f.write('<ul class="navbar-nav me-auto mb-2 mb-lg-0">')
        f.write('<li class="nav-item">')
        f.write('<a class="nav-link active" aria-current="page" href="http://www.musimatic.xyz">Home</a>')
        f.write('</li>')
        f.write('</div>')
        f.write('</div>')
        f.write('</nav>')
        f.write('<h1>Bandcamper</h1>')
        f.write('<h2>Last Time Updated: ' + str(current_date_eastern) + ' at ' + str(current_time_eastern) + ' EDT</h2>')
        f.write('<br />')
        f.write('<a class="btn btn-primary" href="https://github.com/SamuelBanya/Bandcamper">Source Code Link</a>')
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
        f.write('<button type="button" class="btn btn-success" id="genreGoButton">GO!</button>')            
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
        f.write('<button type="button" class="btn btn-success" id="locationGoButton">GO!</button>')            
        f.write('</form>')
        f.write('<br />')
        f.write('<br />')
        f.write('<script src="js/tags.js"></script>')
        f.write('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">')
        f.write('</div>')
        f.write('</body>')
        f.write('</html>')
    f.close()

        
def main():
    copyOverCSSAndJS()
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

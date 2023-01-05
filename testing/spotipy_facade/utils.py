




def get_all_pages(spotify_obj, page):
    all_items = page['items']
    while page['next']:
        page = spotify_obj.next(page)
        all_items.extend(page['items'])
    return all_items
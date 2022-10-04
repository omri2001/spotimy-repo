




def get_all_pages(spotify_obj, page):
    all_items = page['items']
    while page['next']:
        result = spotify_obj.next(page)
        all_items.extend(result['items'])
    return all_items
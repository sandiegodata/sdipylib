"""Functions for loading and saving URLS"""

import requests
def cache_url(url):
    """Load a url to a local file, or return the file path  if it already exists
    This function will download the given URL to the current directory, with a file name of the
    last path element in the URL. """
    import os
    import urlparse
    from IPython.display import display, clear_output
    import sys
    
    parts = urlparse.urlparse(url)
    
    if not parts.scheme in ['http','https', 'ftp']:
        raise Exception("Probably not a valid URL")
    
    # Return the file directly if it already exists
    fn = os.path.basename(parts.path)
    if os.path.exists(fn):
        return os.path.abspath(fn)
    
    r = requests.get(url, stream=True)

    total = 0
    with open(fn, 'wb') as fd:
        for chunk in r.iter_content(2**20): # Read about 1MB, final len() is longer because of decompression
            fd.write(chunk)
            clear_output(wait=True)
            total += len(chunk)
            print "Wrote {} bytes, total {}".format(len(chunk), total)
            sys.stdout.flush()
            
    return os.path.abspath(fn)

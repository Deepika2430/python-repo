# Creating a Playlist Feed

This document outlines the steps to create an applicaster feed for a playlist. Follow the steps below to ensure all necessary elements are included.

## Steps

### 1. **Set ID**
   - Assign feedid of playlist as ID to the feed.

### 2. **Set feed type**
   - Set the feed type to "feed".

### 3. **Set the feed title**
   - Assign title of playlist as feed title.

### 4. **Set the entry section to the feed**
- For each playlist item, perform the following actions:

#### **Set Type**: 
    Define the type based on the content type. Example types: video (default), episode, etc...

#### **Set Metadata**: 
    Include the title and sources for each item. 
    Set each playlist item description as summary.

#### **Set Content Type**: 
    By default, set the content type to 'video/hls'.

#### **Set ID**: 
    Set the mediaid of playlist item as id.

#### **Set Media Group**: 
    It is a JSON array.
        - Set the type as an image and media_item as the list of images in the playlist item. For each image, use its width as the key and its src as src.

#### **Set Extensions**: 
    Place remaining attributes which are not default attributes (title, summary, mediaID, link, image, images, sources, tracks, tags, variations) in extensions.

#### **Set Tags**: 
    Convert tags to lowercase, split the tags by commas, and set tags as a list.
    
#### ***Note***: 
    Ignore links, tracks, images, and variations.

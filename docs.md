# Creating a Media Feed

This document outlines the steps to create a media feed for a playlist. Follow the steps below to ensure all necessary elements are included.

## Steps

1. **Set ID**
   - Assign Playlist ID as feed ID.

2. **Choose Feed Type**
   - Set the feed type to "feed".

3. **Set the Playlist Title**
   - Use the playlist title as the feed title.

4. **Create Feed Entry for the Playlist**
    - For each playlist item, perform the following actions:
        - **Set Type**: Define the type based on the content type.
            - Example types: video (default), episode, etc.
        - **Set Metadata**: Include the title and sources for each item.
            - Change each playlist item description to summary.
        - **Set ID**: Use the media ID as the identifier for each playlist item.
        - **Set Content Type**: By default, the content type is 'video/hls'.
        - **Set Media Group**: It is a JSON array.
            - Choose the type as an image and include a list of images in the playlist item.
            - For each image, use its width as the key and its source url as the src.
        - **Create Extensions**: Place any attributes that are not default attribute keys (title, summary, mediaID, link, image, images, sources, tracks, tags, variations) in extensions.
        - **Set Tags**: Convert tags to lowercase, split the tags by commas, and set tags as a list.
        - ***Note***: Ignore links, tracks, images, and variations.

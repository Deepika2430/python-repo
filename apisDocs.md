# FBA (Feed Builder for Applicaster) API Documentation

### List of API's
- Fetch JW-playlist
- Convert to pipe2 feed
- Get filters
- Search filters
- Save pipe2 config
- Get media feed
- Get media feed by name
- Edit media feed

### 1. Fetch JW-Playlist

**Method**: `GET`  
**Endpoint**: `/feed/playlist/{playlistId}`

**Description**: Fetch the playlist from the JWPlayer with given playlist Id.  
**Response**:
- **Success (200 OK)**:
    ```json
    {
        "playlistId": "xxxx",
        "data": {},
        "status": true
    }
    ```
    - **Example Response**:
        ```json  
        {
            "title": "Sight & Sound Theatres: DAVID",
            "description": "Master Poet. Fearless Warrior. Anointed King. From still waters to shadowed valleys, David's ascent to the throne is filled with towering giants, wild animals, and Philistine soldiers. After unprecedented victories lead to devastating failures, this passionate warrior will face the biggest battle of all: the one within himself. Come alongside this young shepherd on his journey to become a man after God's own heart.",
            "kind": "DYNAMIC",
            "feedid": "i8yF1MSC" ,
            // ......
        }
        ``` 
- **Error (4xx/5xx)**:
    ```json
    {
        "error": "Playlist not found",
        "code": 404
    }
    ```
### 2. Convert to Pipe2 feed

**Method**: `POST`  
**Endpoint**: `/feed/pipe2`  
**Body**: `playlist` and remaining parameters

**Description**: Convert the fetched jwplayer playlist to the Pipe2 format and include any additional parameters.  
**Response**:
- **Success**:
    ```json
        {
            "status": "success",
            "data": { /* Converted Pipe2 data */ }
        }
    ```
    - **Example Response**:
        ```json  
        {
            "id": "i8yF1MSC",
            "title": "Sight & Sound Theatres: DAVID",
            "type": {
                "value": "feed"
            },
            "entry": [
                {
                    "type": {
                        "value": "episode"
                    },
            // ......
                }
            // ......
            ]
            // ......
        }
        ```
- **Error (4xx/5xx)**:
    ```json
    {
        "error": "Conversion failed",
        "code": 400
    }
    ```
### 3. Get filters
- **Method:** GET
- **Query Params:** `type = itemFilter or feedFilter (Optional)`
- **Endpoint:** `feed/filters?type=xxxxxxxx`
- **Description:** To get all the filters or specific type of filters.
- **Response:**
  - **Success (200 OK):** A JSON object with the filters available for the specified type.
    ```json
    {
      "filters": [
        {
          "id": "filter1",
          "name": "Filter 1",
          "type": "itemFilter",
          // Additional filter details
        },
        {
          "id": "filter2",
          "name": "Filter 2",
          "type": "feedFilter",
          // Additional filter details
        }
        // More filters
      ]
    }
    ```
  - **Error (4xx/5xx):** Error message and code indicating the issue with the request.
    ```json
    {
      "error": "Invalid type parameter",
      "code": 400
    }
    ```

### 4. Search Filters
- **Endpoint:** `feed/filter?name=xxxx`
- **Method:** GET
- **Query Params:** `Filter Name`
- **Description:** To get the specified filter by name or functionality.
- **Response:**      
  - **Success**:
    ```json 
        {
          "data": [{
            "id": "filter1",
            "name": "Filter 1",
            "type": "itemFilter",
            // Additional filter details
          }],
          "status": true
        }
    ```
  - **Error (4xx/5xx):** Error message and code indicating the issue with the request.
    ```json
    {
      "error": "Invalid type parameter",
      "code": 400
    }
    ```

### 5. Save Pipe2Config
- **Endpoint:** `feed/media/pipe2Config`
- **Method:** POST
- **Body:** `config`
  ```json
  {
    "name": "media feed pipeline name",
    "pipeline": [
      // Pipeline configuration details
    ]
  }
- **Description:** Saves pipeline configuration details.
- **Response:**      
  - **Success**:
    ```json
        {
          "status": "success",
          "message": "status message"
        }
    ```
  - **Error (4xx/5xx):** Error message and code indicating the issue with the request.
    ```json
    {
      "error": "Invalid type parameter",
      "code": 400
    }
    ```
### 6. Get media feed 
- **Endpoint:** `feed/media`
- **Method:** GET
- **Description:** Retrieves all the media feed's with its endpoint and method
- **Response:**
  - **Success**:
    ```json
      {
        "data":[{
          "name": "feed-name",
          "endpoint": "endpoint"
        },
        // More media feeds
        ] 
      }
    ```
  - **Error (4xx/5xx):** Error message and code indicating the issue with the request.
    ```json
    {
      "error": "Invalid type parameter",
      "code": 400
    }
    ```
### 7. Get media feed by name
- **Endpoint:** `feed/media/name=xxxx`
- **Method:** GET
- **Description:** Retrieves given media feed's pipeline and configuration 
- **Response:**
  - **Success**:
    ```json
    {
      "name": "Name of the media feed",
      "pipeline":[
        // Pipeline configuration details
      ]
    }
    ```
  - **Error (4xx/5xx):** Error message and code indicating the issue with the request.
    ```json
    {
      "error": "Invalid type parameter",
      "code": 400
    }
    ```

### 8. Edit media feed
- **Endpoint:** `feed/media`
- **Method:** PUT
- **Description:** Updates media feed can be order of filters or configuration of filters
- **Response:**
 - **Body:** `config`
  ```json
  {
    "name": "media feed pipeline name",
    "pipeline": [
      // Pipeline configuration details
    ]
  }
 ```
- **Description:** Saves pipeline configuration details.
- **Response:**      
  - **Success**:
    ```json
        {
          "status": "success",
          "message": "status message"
        }
    ```
  - **Error (4xx/5xx):** Error message and code indicating the issue with the request.
    ```json
    {
      "error": "Invalid type parameter",
      "code": 400
    }
    ```








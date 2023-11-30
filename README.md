# ETL WITH DOCKER

The project is extracting data from NASA's Patents API. Modifying date values from `YYYY-MM-DDT00:00:00Z` into `YYYY-MM-DD`. Also there are missing objects attributes in some objects, those will be filled as `UNKNOWN`.

At the end of the process a CSV file is generated, with the processed data.

### Env Variables needed
 
-  **API URL:** [NASAs Patents]("https://data.nasa.gov/resource/gquh-watm.json")

-  **PORT:** You can decide de port value. Ex: `8000`

-  **HOST:** You can use your own host. Ex: `0.0.0.0`

### Endpoint

To download the CSV file you can use the following endpoint:

- **GET:** `/data`
>  Example:
>  - `{your_host}:{PORT}/data` -> `http://localhost:8000/data`


### Docker Commands

- **Build Image:** `docker build -t image_name .`
- **Run Container:** `docker run -p 8000:8000 image_name`

> Port should be the same as `PORT` in env variables
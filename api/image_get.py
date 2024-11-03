import ee
from pprint import pprint
from datetime import datetime, timedelta
from tqdm import tqdm 

ee.Authenticate()
ee.Initialize(project='ee-neelrages')

def get_satellite_images(latitude, longitude, radius=20):
    radius_meters = radius * 1609.34
    point = ee.Geometry.Point([longitude, latitude])
    roi = point.buffer(radius_meters)

    # Extend date range
    start_date = (datetime.now() - timedelta(days=200)).strftime('%Y-%m-%d')

    end_date = datetime.now().strftime('%Y-%m-%d')

    # Adjust cloud cover threshold
    collection = (
        ee.ImageCollection('COPERNICUS/S2_HARMONIZED')
        .filterBounds(roi)
        .filterDate(start_date, end_date)

    )

    # Print number of images
    print('Number of images:', collection.size().getInfo())

    vis_params = {
        'min': 0,
        'max': 0.3,

        'bands': ['B4', 'B3', 'B2'],
    }

    image_urls = []
    images = collection.toList(collection.size())
    for i in tqdm(range(images.size().getInfo())):
        image = ee.Image(images.get(i))

        # Increase image resolution
        url = image.getThumbURL({
            'region': roi.getInfo()['coordinates'],
            'dimensions': 128,
            'format': 'png',
            **vis_params
        })
        image_urls.append((url, latitude, longitude))

    return image_urls

images = get_satellite_images(43.000, -71.299)

with open('image_urls.py', 'w') as f:
    f.write(images)

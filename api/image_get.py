import ee
import math
from datetime import datetime, timedelta

ee.Authenticate()

ee.Initialize(project='ee-neelrages')

def get_satellite_images(latitude, longitude, radius=10):

    radius_meters = radius * 1609.34
    
    point = ee.Geometry.Point([longitude, latitude])
    roi = point.buffer(radius_meters) 
    
    start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')
    
    collection = (
        ee.ImageCollection('COPERNICUS/S2_HARMONIZED')
        .filterBounds(roi)
        .filterDate(start_date, end_date)
        .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))

    )

    vis_params = {
        'min': 0,
        'max': 3000,
        'bands': ['B4', 'B3', 'B2'], 
    }

    image_urls = []
    images = collection.toList(collection.size()) 
    for i in range(images.size().getInfo()):
        image = ee.Image(images.get(i))
        url = image.getThumbURL({'region': roi, 'dimensions': 512, 'format': 'png', **vis_params})
        image_urls.append(url)

    return image_urls

images = get_satellite_images(43.000, -71.299)
print(images)
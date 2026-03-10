import urllib.request
import os

# Create directories
os.makedirs('public/images/cocktails', exist_ok=True)
os.makedirs('public/images/services', exist_ok=True)
os.makedirs('public/images/hero', exist_ok=True)
os.makedirs('public/images/cases', exist_ok=True)
os.makedirs('public/images/blog', exist_ok=True)

# List of images to download
images = [
    # Hero images
    ('https://images.unsplash.com/photo-1537521537707-da8fbf3b3efb?w=1200&h=600&fit=crop', 'public/images/hero/hero-main.jpg'),
    ('https://images.unsplash.com/photo-1608439773649-abc10fbb03e0?w=500&h=500&fit=crop', 'public/images/services/cocktail-bar.jpg'),
    ('https://images.unsplash.com/photo-1492684223066-81342ee5ff30?w=500&h=500&fit=crop', 'public/images/services/coffee.jpg'),
    ('https://images.unsplash.com/photo-1590080876351-cd381e72e601?w=500&h=500&fit=crop', 'public/images/services/smoothie.jpg'),
    ('https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=500&h=500&fit=crop', 'public/images/services/vip.jpg'),
    # Cocktail images
    ('https://images.unsplash.com/photo-1536038482416-3f7ee3a2ad99?w=400&h=400&fit=crop', 'public/images/cocktails/martini.jpg'),
    ('https://images.unsplash.com/photo-1608270861620-7d5efd10d313?w=400&h=400&fit=crop', 'public/images/cocktails/margarita.jpg'),
    ('https://images.unsplash.com/photo-1609318384864-a93a3ff61d7e?w=400&h=400&fit=crop', 'public/images/cocktails/mojito.jpg'),
    ('https://images.unsplash.com/photo-1608380066682-8cd1e91a14d4?w=400&h=400&fit=crop', 'public/images/cocktails/manhattan.jpg'),
    ('https://images.unsplash.com/photo-1542326202-d21dc79b2d6e?w=400&h=400&fit=crop', 'public/images/cocktails/cosmopolitan.jpg'),
    ('https://images.unsplash.com/photo-1582158471865-45f2075e33e2?w=400&h=400&fit=crop', 'public/images/cocktails/old-fashioned.jpg'),
    # Non-alcoholic
    ('https://images.unsplash.com/photo-1590080876351-cd381e72e601?w=400&h=400&fit=crop', 'public/images/cocktails/virgin-mojito.jpg'),
    ('https://images.unsplash.com/photo-1600788148184-289e4e87fac9?w=400&h=400&fit=crop', 'public/images/cocktails/lemonade.jpg'),
    # Coffee
    ('https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=400&h=400&fit=crop', 'public/images/cocktails/espresso.jpg'),
    ('https://images.unsplash.com/photo-1517668808822-9ebb02ae2a0e?w=400&h=400&fit=crop', 'public/images/cocktails/cappuccino.jpg'),
    ('https://images.unsplash.com/photo-1524432888867-9ca67f2e2133?w=400&h=400&fit=crop', 'public/images/cocktails/latte.jpg'),
]

downloaded = []
for url, path in images:
    try:
        urllib.request.urlretrieve(url, path)
        downloaded.append(path)
        print(f'Downloaded: {path}')
    except Exception as e:
        print(f'Error downloading {url}: {e}')

print(f'\nTotal downloaded: {len(downloaded)} images')

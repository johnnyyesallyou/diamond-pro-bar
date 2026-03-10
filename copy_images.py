import shutil
import os

src_dir = r'c:\Users\jonny\test site\zimin site\images'
dst_dir = r'c:\Users\jonny\test site\diamond-pro-bar-complete\public\images'

os.makedirs(dst_dir, exist_ok=True)

count = 0
for f in os.listdir(src_dir):
    src = os.path.join(src_dir, f)
    dst = os.path.join(dst_dir, f)
    if os.path.isfile(src):
        shutil.copy2(src, dst)
        count += 1
        print(f'Copied: {f}')

print(f'\nTotal copied: {count} files')

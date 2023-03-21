#!/usr/bin/env python3
import argparse
import sys
import glob
import os
import json
import multiprocessing

from PIL import Image
Image.MAX_IMAGE_PIXELS = 1000000000
import imagehash

#import warnings
#warnings.filterwarnings("error")


def calcualte_hash(img):
    try:
        with Image.open(img) as image:
            hash = imagehash.phash(image)
        return {
            "image": img,
            "hash": str(hash)
        }
    except Exception as e:
        print(f"problem with image: {img}")
        print(e)
        sys.exit(-1)



def main(_):
    # argument parsing
    parser = argparse.ArgumentParser(description='lists near duplicates of images of a given folder',
                                     epilog="stg7 2023",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("image_folder", type=str, help="folder to check")
    parser.add_argument('--cpu_count', type=int, default=multiprocessing.cpu_count(), help='thread/cpu count')
    parser.add_argument("--del", action="store_true", help="delete detected dumplicate files")

    a = vars(parser.parse_args())

    pool = multiprocessing.Pool(a["cpu_count"])

    hashes = pool.map(calcualte_hash, glob.glob(a["image_folder"] + "/*"))

    collisions = {}
    for h in hashes:
        collisions[h["hash"]] = collisions.get(h["hash"], []) + [h["image"]]

    collisions_detected = {k:collisions[k] for k in collisions if len(collisions[k]) > 1}
    print("detected duplicates")
    print(json.dumps(collisions_detected, indent=4))

    to_be_deleted_files = sum([collisions_detected[x][1:] for x in collisions_detected], [])
    print(f"files to be deleted: {len(to_be_deleted_files)}")
    print("\n".join(to_be_deleted_files))

    if a["del"]:
        print("files will be deleted...")
        for f in to_be_deleted_files:
            os.remove(f)
    print("done")



if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

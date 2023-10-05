from sys import platform


def main():
    # checks platform
    if platform == "linux" or platform == "linux2":
        print("The platform is Linux")
    elif platform == "darwin":
        print("The platform is Mac")
    elif platform == "win32":
        print("The platform is Windows")
        print("Download and install the required packages for Windows")
        # install required packages for Windows : libimobiledevice
        # checks the architecture of the system

        # import required libraries
        import sys
        import hashlib
        import tempfile
        import shutil
        from zipfile import ZipFile
        from urllib.request import urlopen


        print("Importing....")

        if sys.maxsize >> 32:
            imd_url = "https://github.com/libimobiledevice-win32/imobiledevice-net/releases/download/v1.3.17/libimobiledevice.1.2.1-r1122-win-x64.zip"
        else:
            imd_url = "https://github.com/libimobiledevice-win32/imobiledevice-net/releases/download/v1.3.17/libimobiledevice.1.2.1-r1122-win-x86.zip"

        print("Downloading imobiledevice from " + imd_url)
        # set temp_dir and comp

        imd_comp = "imobiledevice-" + hashlib.md5(imd_url.encode("utf-8")).hexdigest()
        imd_temp_dir = tempfile.gettempdir() + "/" + imd_comp
        dll_path = imd_temp_dir + "imobiledevice.dll"

        # if the path exists, then skip the download
        if not os.exists(dll.path):
            # download the file
            print("Downloading imobiledevice from " + imd_url)
            download_dir = imd_dir + "_dl"
            donwload_zip = imd_dir + "_dl.zip"

            with urlopen(imd_url) as response, open(download_zip, "wb") as out_file:
                shutil.copyfileobj(response, out_file)


if __name__ == "__main__":
    main()

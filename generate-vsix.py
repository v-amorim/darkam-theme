import zipfile
import os
import sys


def zipfolder(version):
    """
    Zip the contents of an entire folder (with that folder included
    in the archive). Empty subfolders will be included in the archive
    as well.

    Parameters
    ----------
    version : str
        The version number of the theme to be zipped.

    Examples
    --------
    >>> zipfolder("2.0.2")

    """
    extension = "vsix"
    root_folder = os.getcwd()
    old_versions_folder = os.path.join(root_folder, "old_versions")
    os.makedirs(old_versions_folder, exist_ok=True)
    vsix_files = [
        f for f in os.listdir(root_folder) if f.endswith(".vsix") and f != f"darkam-theme-v{version}.{extension}"
    ]
    for old_vsix in vsix_files:
        os.rename(os.path.join(root_folder, old_vsix), os.path.join(old_versions_folder, old_vsix))
    zipobj = zipfile.ZipFile(f"darkam-theme-v{version}.{extension}", "w", zipfile.ZIP_DEFLATED)
    rootlen = len("./src") + 1
    for base, _dirs, files in os.walk("./src"):
        for file in files:
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])
    sys.exit()


zipfolder("2.4.6")

import zipfile
import os
import sys


def zipfolder(filename, target_dir):
    """
    Zip the contents of an entire folder (with that folder included
    in the archive). Empty subfolders will be included in the archive
    as well.

    Parameters
    ----------
    filename : str
        The name of the zip file.
    target_dir : str
        The path of the folder to be zipped.

    Returns
    -------
    None
        Nothing is returned.

    Examples
    --------
    >>> zipfolder("myzipfile", "myfolder")

    """
    extension = "vsix"
    zipobj = zipfile.ZipFile(f"{filename}.{extension}", "w", zipfile.ZIP_DEFLATED)
    rootlen = len(target_dir) + 1
    for base, _dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])
    return sys.exit()


zipfolder("darkam-theme-v2.0.0", "./src")

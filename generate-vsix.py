import zipfile
import os
import sys


def zipfolder(foldername, target_dir):
    """
    Zip a folder and its contents.

    Parameters
    ----------
    foldername : str
        The name of the folder to be zipped.
    target_dir : str
        The path to the folder to be zipped.

    Returns
    -------
    None

    Examples
    --------
    >>> zipfolder("my_folder", "path/to/my_folder")
    None

    """
    zipobj = zipfile.ZipFile(f"{foldername}.vsix", "w", zipfile.ZIP_DEFLATED)
    rootlen = len(target_dir) + 1
    for base, _dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])


zipfolder("VTheme", "./Theme")
sys.exit()

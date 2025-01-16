import sys
import zipfile
from pathlib import Path


def move_old_versions(root_folder, old_versions_folder, versioned_file):
    old_versions_folder.mkdir(parents=True, exist_ok=True)
    for file in root_folder.glob("*.vsix"):
        if file.name != versioned_file.name:
            file.rename(old_versions_folder / file.name)


def zip_folder(src_folder, output_file):
    with zipfile.ZipFile(output_file, "w", zipfile.ZIP_DEFLATED) as zipobj:
        for file in src_folder.rglob("*"):
            if file.is_file():
                zipobj.write(file, file.relative_to(src_folder))


def zipfolder():
    version = input("Enter the version number: ").strip()
    extension = "vsix"
    root_folder = Path.cwd()
    old_versions_folder = root_folder / "old_versions"
    versioned_file = root_folder / f"darkam-theme-v{version}.{extension}"

    move_old_versions(root_folder, old_versions_folder, versioned_file)
    zip_folder(root_folder / "src", versioned_file)
    print(f"Created {versioned_file}")
    sys.exit()


if __name__ == "__main__":
    zipfolder()

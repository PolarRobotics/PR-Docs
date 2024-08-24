# Documentation Style Guide
- This document contains rules that are to be followed when creating or updating this documentation repository.

## File Locations
- All documentation files (generally Markdown) must be located within `/docs/source/` or a subfolder.
	- Most documentation category folders are located exactly at this level of the file structure.
- Static assets (essentially anything that is not a Markdown file) shall be placed in `/docs/source/_static`.
	- All image files shall be placed in `/docs/source/_static/images` or subfolders.
	- All other asset files (ex. PDF) shall be placed in `/docs/source/_static/files` for now.
- All static assets shall be placed in a subfolder reflecting their reference location in the main file tree.
	- For example, if the file `foo.png` is embedded within `/docs/source/metadocs/bar.md`, then `foo.png` shall be placed in `/docs/source/_static/images/metadocs`.
	- If there are many related images only used in a single note within that category, it is strongly preferred to create a folder sharing the title of the note to place those images in.
		- In the same example, `foo1.png` ... `foo20.png` would be placed in `/docs/source/_static/images/metadocs/bar`.

## Naming Conventions
- Do not use capital lettering for any folder or file name without explicit approval from the project manager.
- Documentation category folder names (i.e., folders under `/docs/source/`) shall use lower kebab case (ex. `data-aq`).
- File names shall use lower snake case (ex. `documentation_style_guide.md`).

